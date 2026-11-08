# HyperFrames SaaS Demo

**Turn a prompt into a SaaS demo video that wins — story-led motion graphics with the patterns and equations that make motion feel professional. No .aep required.**

This is a skill for AI agents (and humans) that have to produce a stunning, professional, winning SaaS demo video from a short prompt — a product name, a capability, and the one thing the viewer should feel or understand. No design file, no template, and no motion-graphics experience required. The skill is the whole method.

## What it is

A complete method for prompt-to-video SaaS demos, built on HyperFrames:

```
Prompt → Story → Motion → Video
```

- **Prompt.** The product, the capability to show, and the one feeling the viewer should leave with.
- **Story.** Five beats — Hook → Prompt → Response → Result → End card. The story decides what appears, in what order, and what the viewer reads at each moment.
- **Motion.** The patterns and equations that make motion feel professional — not vibes, formulas.
- **Video.** Rendered with HyperFrames (12fps, 640×360), verified frame by frame, delivered with an honest list of what is and isn't in it.

## What's inside

| File | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The full skill — story-led motion graphics, the patterns, the equations, the baseline numbers, the craft rules, the antipatterns, the implementation, a complete worked example, and the verification checklist. |
| [`skill.yaml`](skill.yaml) | The skill descriptor (name, title, description, category) for agent skill loaders. |
| [`scripts/check_density.py`](scripts/check_density.py) | A working density checker — run it on a HyperFrames HTML build and it counts keyframes, layers, tweens, text animators, and scenes, then reports PASS / FAIL against the skill's floors. Use it before rendering to find the shortfalls. |
| [`templates/starter.html`](templates/starter.html) | A minimal working HyperFrames starter — the five story beats with the patterns applied (per-letter hook, typing prompt, staggered controls, scale pop + draw-on + count-up result, end card). Copy it and adapt it to your product. Intentionally minimal; the density check will report it below the floor, which is expected. |
| [`references/`](references/) | The two verified template builds as reference — the SaaS v3 HTML (52s, 11 scenes, 18 text animators) and the UI Demo v3 HTML (36s, 56 comps, 216 layers), each with `gsap.min.js`. The third template (AI Intro) is excluded — it is the broken one. Fonts are free Google Fonts; see `references/README.md` for the list and where to put them. |

## The patterns

The recurring motion patterns that make a video feel professional:

- **The beat** — in / hold / out (0.95s / 0.67s / 0.87s). The unit of motion.
- **Per-letter motion** — text as geometry; each letter is its own element.
- **Stagger** — groups arrive in sequence, 30–80ms apart.
- **Easing as emotion** — expo.out is clean; back.out is personality.
- **Moving-shape transitions** — scenes don't cut and don't fade.
- **The built space** — the frame is a stage, not a slide.
- **Overlap as flow** — beats overlap; the overlap is the flow.
- **Scale pop** — the result arrives (0.94 → 1.0, back.out).
- **The reveal, the count-up, the draw-on, parallax / camera, the loop** — and more, each with its purpose, its motion, and how it goes wrong.

## The equations

The motion is not vibes. It is formulas:

- **Per-letter delay:** `delay(i) = 0.08 × i` (i = character index, seconds)
- **Per-letter motion (damped cosine):** `y(t) = A · e^(−λt) · cos(ωt)`
- **The beat:** `in = 0.95s, hold = 0.67s, out = 0.87s`
- **Group stagger:** `delay(j) = 0.03–0.08 × j`
- **Easing:** expo.out `1 − 2^(−10t)`; back.out overshoots ~10% then settles
- **Scale pop:** `0.94 → 1.0, ease back.out`
- **The animator:** `value = base + Σ (amount/100) × (animator(t) − base)`
- **Gradient:** `color(x) = lerp(stop_A, stop_B, x)`

Every equation in the skill has a worked example with real numbers, so you can compute the motion instead of guessing it.

## Baseline numbers — the density floor

A video below these numbers ends up too simple and emotionless. These are floors, not targets:

| Measure | Minimum |
|---|---|
| Keyframes | 300 total, ≥10 per second |
| Layers | ≥100 |
| Tweens | ≥1500 |
| Text animators | ≥5, with per-character motion |
| Scenes | ≥5 |
| Segment length | 2–3s per segment |
| Max static hold | ~2s |
| Duration | 30–52s |
| Render | 12fps, 640×360 |
| Verification frames | ≥5 timestamps, viewed by you |

**The density test:** if you can describe the video in one sentence ("text fades in, then a screenshot"), it is too simple. A winning video needs a sentence per beat.

## The story beats

Every SaaS demo has the same five beats:

1. **Hook (0–3s)** — the brand and the promise. One line, large, moving.
2. **The prompt / the need** — a user asks for something. The prompt types, character by character.
3. **The response** — the product answers. The answer arrives.
4. **The result / the payoff** — the capability is shown working. The result plays, continuously.
5. **The end card** — the brand + the URL, clean and fully visible.

## How to use it

**For an AI agent:** load `SKILL.md` and follow it in order — read the prompt, write the story, apply the patterns and equations, build the video, verify it frame by frame, deliver it. The skill includes a complete worked example (a full prompt-to-video build with the story, the beats, the patterns, the equations, and a density check) so you can see the method applied end to end.

**For a human:** read the story section and the patterns first, then the equations. The antipatterns table (every faulty step, with a before and an after) is the fastest way to avoid the mistakes that make a video look like slop.

## Principles

- **The .aep is one source of the patterns, not a requirement.** The skill does not need a .aep file. If one is available, its keyframes are the ground truth for that template's motion; otherwise, generate the motion from the patterns.
- **The story decides the motion.** Every movement must carry a story beat; if it doesn't, cut it.
- **The demo must genuinely show the real capability.** Never a scripted mock. The result must move — a static screenshot of a product doesn't prove it works.
- **The viewer's eyes outrank every claim.** Never assert a quality gain the viewer can see through. Plain admission + a rebuilt real thing is what buys trust back.
- **Verify frame by frame.** Never deliver a video you haven't watched. Extract at least 5 timestamps and view them yourself.

## License

MIT. Use it, adapt it, build with it.
