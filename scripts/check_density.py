#!/usr/bin/env python3
"""
check_density.py — Check a HyperFrames build against the skill's density floor.

Usage:
    python3 check_density.py <build.html> [duration_seconds]

Reads a HyperFrames HTML file and counts the density measures from the
hyperframes-saas-demo skill, then reports PASS / FAIL against the floors:

    keyframes       >= 300 total, >= 10 per second
    layers          >= 100
    tweens          >= 1500
    text animators  >= 5 (with per-character motion)
    scenes          >= 5

These are heuristics, not an exact count — they count what is countable in
the HTML/JS source:

  - layers:         DOM elements inside the stage (#stage, or <body> if no stage)
  - tweens:         GSAP tween calls (gsap.to/from/fromTo/set and tl.to/from/...)
  - keyframes:      CSS @keyframes rules + animated property entries across
                    all GSAP tweens (each tweened property counts as a keyframe)
  - text animators: distinct parents that contain per-character spans
                    (elements with class "char"); each parent = one animator
  - scenes:         elements with class "scene" or "beat" (or data-scene)

If a count is below the floor, the script tells you which density-ladder
step to take (more animators first, then more beats, then more layers,
then more tweens). See SKILL.md "Baseline numbers" and "The density ladder".

Exit code 0 if every measure passes, 1 otherwise.
"""

import re
import sys

# Floors from SKILL.md — the density floor. Do not lower these.
FLOORS = {
    "keyframes_total": 300,
    "keyframes_per_second": 10,
    "layers": 100,
    "tweens": 1500,
    "text_animators": 5,
    "scenes": 5,
}

# Properties that are not animated values (GSAP config keys), skipped when
# counting animated property entries inside a tween's vars object.
GSAP_CONFIG_KEYS = {
    "duration", "delay", "ease", "stagger", "onComplete", "onStart",
    "onUpdate", "repeat", "yoyo", "repeatDelay", "paused", "id",
    "scrollTrigger", "immediateRender", "overwrite", "defaults",
}


def read_source(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def count_layers(source):
    """DOM elements inside the stage (#stage if present, else <body>)."""
    m = re.search(r'<div[^>]*id=["\']stage["\'][^>]*>(.*)</div>\s*</body>',
                  source, re.DOTALL | re.IGNORECASE)
    scope = m.group(1) if m else source
    # Count opening tags (excluding closing tags, comments, doctype).
    tags = re.findall(r'<(?!/)(?!!--)[a-zA-Z][a-zA-Z0-9-]*', scope)
    return len(tags)


def count_tweens(source):
    """GSAP tween calls: gsap.to/from/fromTo/set and tl.* equivalents."""
    pattern = re.compile(
        r'\b(?:gsap|tl|timeline)\s*\.\s*(?:to|from|fromTo|set|toTo|fromTo)\s*\(',
        re.IGNORECASE)
    return len(pattern.findall(source))


def count_keyframes(source):
    """CSS @keyframes rules + animated property entries in GSAP tweens."""
    css_keyframes = len(re.findall(r'@keyframes\s+[\w-]+\s*\{', source))
    # For each GSAP tween call, count the property keys in its vars object.
    # Heuristic: find gsap/tl calls, take the first {...} after the target,
    # count top-level keys that are not GSAP config keys.
    tween_props = 0
    for m in re.finditer(
            r'\b(?:gsap|tl|timeline)\s*\.\s*(?:to|from|fromTo|set)\s*\(',
            source, re.IGNORECASE):
        rest = source[m.end():m.end() + 2000]
        # The vars object is the second argument: (target, { ... }, position)
        # Find the first '{' after the first ','.
        comma = rest.find(',')
        if comma == -1:
            continue
        brace = rest.find('{', comma)
        if brace == -1:
            continue
        # Take a balanced-ish slice of the object (up to 800 chars).
        obj = rest[brace:brace + 800]
        keys = re.findall(r'([a-zA-Z][\w-]*)\s*:', obj)
        # Only count keys that look like animatable properties.
        props = [k for k in keys if k not in GSAP_CONFIG_KEYS]
        tween_props += len(set(props))
    return css_keyframes + tween_props


def count_text_animators(source):
    """Distinct parents containing per-character spans (class 'char').

    Each parent with .char children is one text animator (one per-char
    motion). Returns (animator_count, total_char_spans).

    Counts both static .char spans in the HTML and spans created at
    runtime by a splitChars(el, "text") call — each splitChars call is
    one animator, and the length of its string literal is the char count.
    """
    char_spans = len(re.findall(
        r'class=["\'][^"\']*\bchar\b[^"\']*["\']', source))
    parents = set()
    for m in re.finditer(r'class=["\'][^"\']*\bchar\b[^"\']*["\']', source):
        # Look backwards for the nearest opening tag with a class/id.
        window = source[max(0, m.start() - 400):m.start()]
        tags = re.findall(
            r'<([a-zA-Z][a-zA-Z0-9-]*)[^>]*?(?:class|id)=["\']([^"\']+)["\']',
            window)
        if tags:
            parents.add(tags[-1][1])
    # Runtime-generated spans: splitChars(el, "text") — one animator per
    # call, char count = the string literal's length (spaces count as spans).
    for m in re.finditer(
            r'splitChars\s*\(\s*[^,]+,\s*["\']([^"\']*)["\']', source):
        text = m.group(1)
        char_spans += len(text)
        parents.add(f"splitChars:{text[:24]}")
    return len(parents), char_spans


def count_scenes(source):
    """Elements with class 'scene' or 'beat', or a data-scene attribute."""
    scenes = len(re.findall(
        r'class=["\'][^"\']*\b(?:scene|beat)\b[^"\']*["\']', source))
    scenes += len(re.findall(r'data-scene\s*=', source))
    return scenes


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check_density.py <build.html> [duration_seconds]")
        sys.exit(2)
    path = sys.argv[1]
    duration = float(sys.argv[2]) if len(sys.argv) > 2 else 36.0

    source = read_source(path)
    layers = count_layers(source)
    tweens = count_tweens(source)
    keyframes = count_keyframes(source)
    animators, char_spans = count_text_animators(source)
    scenes = count_scenes(source)
    kps = keyframes / duration if duration > 0 else 0

    checks = [
        ("keyframes (total)", keyframes, FLOORS["keyframes_total"], ">="),
        ("keyframes (per second)", round(kps, 1),
         FLOORS["keyframes_per_second"], ">="),
        ("layers", layers, FLOORS["layers"], ">="),
        ("tweens", tweens, FLOORS["tweens"], ">="),
        ("text animators", animators, FLOORS["text_animators"], ">="),
        ("scenes", scenes, FLOORS["scenes"], ">="),
    ]

    print(f"Density check — {path}  (duration {duration:g}s)")
    print("-" * 58)
    all_pass = True
    for name, value, floor, _op in checks:
        ok = value >= floor
        all_pass = all_pass and ok
        mark = "PASS" if ok else "FAIL"
        print(f"  {name:<24} {value:>6}   floor {floor:<5}  [{mark}]")
    print("-" * 58)
    print(f"  per-char spans: {char_spans}  (each .char span is one letter)")
    if all_pass:
        print("  All measures meet the floor. Render it.")
    else:
        print("  Below the floor. Add density in this order (cheapest first):")
        print("    1. More text animators (per-char reveals are cheap, biggest difference)")
        print("    2. More beats (split a long beat into two shorter beats)")
        print("    3. More layers (background blobs, glass cards, shadows — the built space)")
        print("    4. More tweens (animate the background, the camera, secondary elements)")
        print("  Do not render a thin build and hope the viewer won't notice.")
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
