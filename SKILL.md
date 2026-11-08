---
name: hyperframes-saas-demo
description: Create stunning, professional, winning SaaS demo videos from a prompt using HyperFrames — story-led motion graphics with the patterns and equations that make motion feel professional. No .aep required.
---

# HyperFrames SaaS Demo — Prompt to Video

Turn a prompt into a SaaS demo video that wins: punchy, high-energy, dense with deliberate motion, and faithful to the story. The prompt names the product and the capability. The story carries the motion. The patterns and equations make it feel professional. No .aep file required — the motion is generated from the patterns, not parsed from a template.

## Who this is for

An AI agent (or a human) that has to produce a SaaS demo video from a short prompt — a product name, a capability, and the one thing the viewer should feel or understand. The agent may have no design file, no template, and no motion-graphics experience. This skill is the whole method: how to turn the prompt into a story, how to turn the story into motion, how to make the motion feel professional, and how to verify the result before delivering it.

## How to use this skill

Read the whole skill once before starting. Then work in order:

1. **Read the prompt.** Extract the product, the capability to show, and the one feeling or understanding the viewer should leave with. If any of the three is missing, ask — a demo without a capability is a slideshow.
2. **Write the story.** Turn the prompt into story beats (Hook → Prompt → Response → Result → End card). Write the beats down with their timings before touching any motion. The story is the plan.
3. **Apply the patterns and equations.** For each beat, pick the patterns that carry it and compute the motion with the equations. Do not invent motion; generate it from the formulas.
4. **Build the video.** Assemble the HyperFrames build (HTML + GSAP timeline), render it, encode it.
5. **Verify.** Watch the video frame by frame against the verification checklist. Fix the mechanism (the generator), not the output. Re-render once.
6. **Deliver.** The video plus an honest list of what is and isn't in it.

## Prompt → Story → Motion → Video

The flow, in full:

```
Prompt
  → Story (beats with timings)
    → Motion (patterns + equations per beat)
      → Video (HyperFrames build, render, encode)
        → Verify (watch every frame)
          → Deliver
```

**1. Prompt.** The user gives a prompt: the product, the capability to show, and the one thing the viewer should feel or understand. Example: "Show a product that turns a typed sentence into a live physics simulation — the viewer should feel that typing a sentence makes physics happen." If the prompt is vague ("make a video about my SaaS"), ask for the capability and the feeling. A demo without a capability is a slideshow; a demo without a feeling is a manual.

**2. Story.** Turn the prompt into a story with beats. The story decides what appears, in what order, and what the viewer reads at each moment. Write the beats down with timings (see "Story-led motion graphics" below) before touching any motion. The story is the plan; the motion is the execution.

**3. Motion.** For each story beat, apply the patterns and equations. The motion is the story made visible. Every movement must carry a story beat; if it doesn't, cut it.

**4. Video.** Assemble the HyperFrames build, render it at 12fps / 640×360, encode it. The render is the receipt — it proves the motion works.

**5. Verify.** Watch the video frame by frame. The verification checklist is at the end of this skill.

**6. Deliver.** The video plus an honest list of what is and isn't in it.

The .aep templates are ONE source of these patterns — they are where the patterns were learned. But the skill does not need a .aep. If a .aep IS available, its keyframes are the ground truth for that template's motion; otherwise, generate the motion from the patterns below.

## Story-led motion graphics — how story drives the motion

Motion graphics is not decoration. The story decides the motion. Every movement must carry a story beat; if it doesn't, cut it.

### The story beats — the spine of any SaaS demo

Every SaaS demo has the same five beats. The beats are the spine; the patterns are the muscle.

**1. Hook (0–3s). The brand and the promise.**
One line, large, moving. The viewer must know what this is and why it matters in the first 3 seconds. If the viewer doesn't understand the product by 3 seconds, they won't watch the next 30.
- What it is: the product name, or the one-line promise ("Type a sentence. Watch physics happen.").
- Motion: the brand enters with a beat — it doesn't just appear. It slides, pops, or reveals in, holds, and makes room for the next beat.
- Common failure: a static logo on a flat colour for 3 seconds. That is a title card, not a hook. The hook must MOVE.

**2. The prompt / the need (3–12s). A user asks for something.**
A user asks for something (types a prompt, states a need, clicks a button). This is the story's question. The viewer must see the ask clearly, because the ask is what the product answers.
- What it is: the input — a typed prompt, a spoken request, a chosen option.
- Motion: the prompt TYPES — character by character, because typing is the story of asking. The input is the story's question. A prompt that appears all at once doesn't feel asked; a prompt that types feels like someone is asking right now.
- Common failure: the prompt appears as a block of text. It reads as a label, not a question.

**3. The response (12–18s). The product answers.**
The product answers. This is the story's turn — the moment the viewer sees that the product understood the ask.
- What it is: the product's reply — a confirmation, a loading state, the first sign of the result.
- Motion: the answer ARRIVES — it pops, slides, or unfolds into the frame. The response is the story's turn. It should feel like a handoff: the ask goes in, the answer comes out.
- Common failure: the response is a static "Done" checkmark. The response should show the product working, not just confirm it worked.

**4. The result / the payoff (18–30s). The capability is shown working.**
The capability is shown working — the animation, the number, the outcome. This is the proof. It must genuinely show the capability, never a scripted mock.
- What it is: the product doing the thing — the simulation running, the chart drawing, the number counting, the file converting.
- Motion: the result PLAYS — it moves on its own. This is the longest beat, because the proof needs time to be believed. The result must move continuously; a static screenshot of a result is not a result, it's a picture of one.
- Common failure: a static screenshot of the product. A screenshot doesn't prove the product works; a moving recording does.

**5. The end card (30–36s). The brand + the URL.**
The brand and the URL, clean and fully visible. No truncation. The viewer must be able to read the URL and remember the name.
- What it is: the product name + its real URL, fully visible, no truncation.
- Motion: it settles. The end card is the one beat that is allowed to be calm — it arrives, holds, and the video ends. But it still arrives with motion (a pop or a slide), not a cut.
- Common failure: the URL is too small to read, or the brand name is cut off at the edge.

### How the story controls timing

- **The hold is reading time.** A beat holds long enough for the viewer to read it (0.67s for a concept), then exits to make room for the next beat. If the viewer can't read it, the hold is too short. If the viewer is bored, the hold is too long. Scale the hold with the amount of text: a short word needs ~0.5s; a full sentence needs ~1.5s. Read the beat out loud at normal speed — that's the hold.
- **The transition is the story moving forward.** A beat doesn't vanish; it exits with motion (slides out, scales away) while the next beat enters. The overlap is the flow. A hard cut says "the story stopped"; a moving transition says "the story continues."
- **One thing moves at a time (mostly).** The element carrying the story beat moves; everything else supports it. If everything moves at once, the viewer doesn't know where to look. The exception is the payoff beat, where the result itself moves and the UI around it can move too — but the result is still the focus.
- **The camera moves.** The frame is a space, not a slide. A slow push or pan keeps the eye engaged even when the content is still. A static camera over a static frame is a photograph.

### Deriving beats from a prompt — worked method

Take the prompt and ask three questions:
1. **What does the user ask for?** (This is beat 2 — the prompt.)
2. **What does the product do in response?** (This is beats 3 and 4 — the response and the result.)
3. **What should the viewer remember?** (This is beats 1 and 5 — the hook and the end card.)

Write one sentence per beat. Then assign each beat a time window (using the beat equation below). Then, for each beat, write what moves. If you cannot write what moves for a beat, the beat is not a motion beat — rewrite it until it moves.

Example — prompt: "Show a product that turns a typed sentence into a live physics simulation."
- Beat 1 (Hook, 0–3s): "Type a sentence. Watch physics happen." — the line reveals letter by letter, large, centred.
- Beat 2 (Prompt, 3–12s): the user types "Simulate a falling ball" in the product's input — the text types character by character.
- Beat 3 (Response, 12–16s): the product replies "Simulation active" — the reply slides in, the controls appear.
- Beat 4 (Result, 16–30s): the ball falls, the trajectory draws, the live data ticks — the simulation plays, continuously moving.
- Beat 5 (End card, 30–36s): the product name + URL — settles, fully visible.

### The story test

For each beat, ask: "What does the viewer learn here, and what moves to teach it?" If a beat teaches nothing, cut it. If a movement teaches nothing, cut it. If the video can be described in one sentence ("text fades in, then a screenshot"), it is too simple — a winning video needs a sentence per beat.

### Story failure modes

- **The prompt appears three times.** The viewer is asked the same question three times and stops caring. Prompt once; the rest of the video is the answer.
- **The result is a static image.** A static screenshot of a product doesn't prove it works. The result must move.
- **The hook is a logo on a flat colour.** No motion, no promise, no reason to keep watching.
- **The end card is unreadable.** The URL is too small or the name is cut off. The viewer can't act on the video.
- **The beats are out of order.** The result appears before the prompt. The viewer doesn't know what they're looking at.

## The patterns

These are the recurring motion patterns that make a video feel professional. They are the things the professional templates do, extracted as reusable patterns. Each pattern has a purpose (what story beat it carries), a motion (how it moves), and a warning (how it goes wrong).

### 1. The beat — in / hold / out

Every element enters, holds, and exits. The beat is the unit of motion. If you only learn one pattern, learn this one.
- **In:** the element arrives (0.95s). It arrives with intent — a slide, a pop, a reveal — not a fade. The entrance should match the story: a question slides in gently; a result pops in confidently.
- **Hold:** the element stays (0.67s for a concept). This is reading time. The hold is the only part of the beat where nothing moves — and it must be long enough to read, short enough not to bore.
- **Out:** the element leaves (0.87s). It exits with motion, making room for the next beat. An element that just disappears feels like a glitch; an element that exits feels like the story moving on.
- **Overlap:** beats overlap slightly — the next beat starts entering as the previous one exits. That overlap is the flow. A good rule: the next beat's "in" starts when the previous beat is halfway through its "out."
- **When it goes wrong:** an element that fades in and fades out has no beat — it has no arrival and no departure. An element that never exits crowds the frame. An element that exits instantly feels cut.

### 2. Per-letter motion — text as geometry

Text doesn't appear as a block. It arrives letter by letter, because text is geometry and each letter is a shape with its own timing.
- **Each letter is its own element** (inline-block, so transforms apply). If the letters are not separate elements, the per-letter motion cannot happen — the whole word moves as one block, and the text feels dead.
- **Letters stagger in**, one after another (delay = 0.08s × index). A 10-letter word takes 0.8s to fully arrive. The stagger is what makes text feel typed, spoken, alive.
- **Letters can wave, blur, or drop.** An animator drives a value across the letters (a sweep). A Start sweep reveals letters char by char; an Offset sweep drives a blur/drop wave across the word. The wave is the text breathing.
- **When it goes wrong:** text that appears all at once reads as a label. Text with no stagger reads as a slide. Text where the letters are not separate elements cannot stagger at all — check that the spans exist before assuming the motion will work.

### 3. Stagger — groups arrive in sequence

When a group enters (a list, a row of cards, a set of controls, a set of feature words), the items arrive one after another, 30–80ms apart. The stagger makes the group feel choreographed, not dumped.
- **The stagger is short.** 30–80ms per item. A 5-item list takes 0.15–0.4s to fully arrive. Longer than that and the group feels slow; shorter and the stagger is invisible.
- **The stagger is consistent.** Every item uses the same delay step. An inconsistent stagger feels like a bug.
- **When it goes wrong:** a group that appears all at once feels dumped. A group with a 200ms stagger feels like it's lagging.

### 4. Easing as emotion

The easing curve IS the feeling. The same movement with a different easing reads as a different emotion.
- **expo.out = clean, confident, professional.** Fast start, gentle landing. The default for most entrances. Use it when the element should feel competent.
- **back.out = overshoot = personality.** The element goes slightly past its target (~10% overshoot) and settles back. Use it for the moments that should feel alive — a pop, a score, a result, a payoff. Don't use it for everything; if every element overshoots, nothing feels special.
- **Ease-out for entrances, never ease-in.** Ease-in feels sluggish (slow start); ease-out gives instant feedback (fast start). An entrance that starts slow feels like the video is buffering.
- **Custom cubic-bezier curves, not the defaults.** The defaults are generic. A custom curve (e.g. a slightly longer ease-out) is a signature.
- **Transform/opacity-only motion.** Never animate layout properties (width, height, margin, top/left). Layout animation is slow and janky; transform and opacity are GPU-composited and smooth.
- **When it goes wrong:** linear easing (no easing) feels robotic. Ease-in on an entrance feels like lag. Animating width/height feels like the page is reflowing.

### 5. Moving-shape transitions

Scenes don't cut and don't fade. A shape moves across the frame (a wipe, a panel sliding, a card expanding) and the next scene is revealed behind it. The transition is a moving shape.
- **The shape is the transition.** A rectangle wipes across; a circle expands; a card slides in from the side and covers the old scene, then the new scene is underneath it. The viewer watches the shape move, and the scene changes behind it.
- **The shape should match the story.** A wipe that moves left-to-right says "forward." A card that expands says "here's more." A panel that slides up says "next."
- **When it goes wrong:** a fade says nothing — it's the absence of a transition. A hard cut says "the story stopped." A shape that moves too slowly feels like a loading screen.

### 6. The built space

The frame is a stage, not a slide. Before any text appears, build the space: a high-key studio background, diffused ambient light, soft shadows, glass cards. The content sits IN the space.
- **The space is built first.** The background, the light, the shadows, and the cards exist before the text arrives. The text enters a space that is already there.
- **The space has depth.** A flat colour is not a space. Depth comes from: a gradient background (light to lighter), soft shadows under cards, glass panels with blur, and elements at different depths (background blobs, mid-ground cards, foreground text).
- **The space is high-key.** Bright, clean, lots of light. A dark, flat background with white text is a terminal, not a studio.
- **When it goes wrong:** text on a flat colour is a slideshow. A dark, unedited screen recording inside white borders is a recording in a frame, not a video. No depth = no space = no professionalism.

### 7. Overlap as flow

Beats overlap. The next element starts entering before the previous one has fully left. The overlap is what makes the video feel continuous instead of choppy.
- **Intentional overlap:** the next beat's "in" starts when the previous beat is halfway through its "out." The viewer sees the handoff.
- **Accidental overlap is a defect.** A static shape sitting in an animated layer's path reads as a strikethrough or a collision. Static-vs-animated collision is the real defect class — check for it explicitly before rendering. If a static element overlaps a moving element, move one of them.
- **When it goes wrong:** no overlap = choppy (each beat is isolated). Too much overlap = cluttered (two beats fighting for attention). Accidental overlap = a bug the viewer will notice.

### 8. Scale pop — the result arrives

When the result/payoff appears, it pops: scale from 0.94 → 1.0 with back.out. The pop says "here it is."
- **One pop, for the payoff.** Use it once, for the result. If every element pops, nothing feels special.
- **The pop is small.** 0.94 → 1.0 is a 6% scale change. It is subtle — the viewer feels it more than sees it. A pop from 0.5 → 1.0 is a cartoon.
- **When it goes wrong:** no pop on the result = the result just appears, and the payoff falls flat. A pop on everything = the video feels like a bouncy castle.

### 9. The reveal — a value sweeps across

A reveal is a value (opacity, blur, position, colour) that sweeps across an element, driven by an animator. The most common reveal is the Start sweep: the element is revealed char by char, left to right, as if a curtain is being pulled.
- **Start sweep:** reveals the element from one end to the other. The sweep speed is the reading speed — it should match how fast the viewer can read.
- **Offset sweep:** drives a wave (blur, drop, vanish) across the element. The wave moves; the element is still. The wave is the motion.
- **When it goes wrong:** a reveal that is too fast is invisible; a reveal that is too slow feels like the video is stuck.

### 10. The count-up — a number that earns itself

When a number matters (a score, a range, a percentage), it counts up from 0 (or from a starting value) to its final value, rather than appearing all at once. The count-up says "this number was earned."
- **The count-up is fast.** A 3-digit number counts up in ~1s. Slower and it feels like a loading bar.
- **The count-up uses easing.** It starts fast and slows as it approaches the final value (ease-out). A linear count-up feels like a timer.
- **When it goes wrong:** a number that appears all at once is a label. A number that counts up too slowly is a progress bar.

### 11. The draw-on — a line that draws itself

When a trajectory, a path, a chart, or a line matters, it draws itself — the line grows from one end to the other, rather than appearing whole. The draw-on says "this path was travelled."
- **The draw is the motion.** The line grows at the speed the thing it represents moves. A trajectory draws at the speed of the projectile; a chart draws at the speed of the data.
- **When it goes wrong:** a line that appears whole is a diagram. A line that draws too slowly feels like it's buffering.

### 12. Parallax / camera — the frame has depth

The camera moves, and elements at different depths move at different speeds (parallax). The background moves slowly, the foreground moves fast. The parallax is what makes the frame feel like a space rather than a flat image.
- **A slow push (zoom in 2–5% over a beat)** keeps the eye engaged even when the content is still.
- **A pan (left/right, up/down)** follows the story — the camera pans to the next beat.
- **When it goes wrong:** a static camera over a static frame is a photograph. A camera that moves too fast is seasickness.

### 13. The loop — the payoff keeps moving

The result/payoff beat should loop or continue moving for its whole duration. A simulation keeps simulating; a chart keeps updating; a number keeps ticking. The payoff is not a still image — it is a living thing. If the payoff stops moving, the video stops.
- **When it goes wrong:** a payoff that freezes after 1 second is a screenshot with a 1-second intro. The payoff must move for its entire beat.

## The equations

The motion is not vibes. It is formulas. These are the equations that make the patterns precise. Each equation has a worked example so you can compute the motion instead of guessing it.

### Per-letter delay

```
delay(i) = 0.08 × i        (i = character index, 0-based; seconds)
```

Each letter starts 0.08s after the previous one.

**Worked example — the word "Simulate" (8 letters):**
| Letter | Index i | Delay (s) |
|---|---|---|
| S | 0 | 0.00 |
| i | 1 | 0.08 |
| m | 2 | 0.16 |
| u | 3 | 0.24 |
| l | 4 | 0.32 |
| a | 5 | 0.40 |
| t | 6 | 0.48 |
| e | 7 | 0.56 |

The word takes 0.56s to start its last letter, plus the letter's own entrance (~0.3s), so the full word is visible at ~0.86s. A 20-letter sentence takes 1.52s to start its last letter — that is why long sentences need longer holds.

**How to use it:** for each letter, set its animation-delay to `0.08 × i`. Do not use a fixed delay for all letters. Do not guess the stagger — compute it.

### Per-letter motion — damped cosine

A letter's offset over time follows a damped cosine: it overshoots and settles.

```
y(t) = A · e^(−λt) · cos(ωt)
```

- **A** = the initial amplitude (how far the letter starts offset, in px). Typical: 20–40px for a large headline, 8–16px for body text.
- **λ** = the damping (how fast it settles). Typical: λ ≈ 3–5 /s. Higher λ = settles faster, less bounce. Lower λ = more bounce.
- **ω** = the frequency (how fast it oscillates). Typical: ω ≈ 10–15 rad/s (about 1.5–2.5 oscillations per second).

**Worked example — a headline letter, A = 30px, λ = 4, ω = 12:**
| t (s) | e^(−4t) | cos(12t) | y(t) (px) |
|---|---|---|---|
| 0.00 | 1.00 | 1.00 | +30.0 |
| 0.10 | 0.67 | 0.36 | +7.3 |
| 0.20 | 0.45 | −0.74 | −10.0 |
| 0.30 | 0.30 | −0.90 | −8.1 |
| 0.40 | 0.20 | 0.09 | +0.5 |
| 0.50 | 0.14 | 0.96 | +3.9 |
| 0.80 | 0.04 | −0.99 | −1.2 |
| 1.00 | 0.02 | 0.84 | +0.5 |

The letter starts 30px offset, swings past its resting position (to −10px at 0.2s), and settles to ~0 by 0.8s. That single overshoot is what makes the motion feel springy and alive instead of mechanical. A letter with no overshoot (pure ease-out) feels flat; a letter with too many oscillations feels like it's vibrating.

**How to use it:** implement the damped cosine as a keyframe function (or approximate it with a back.out ease, which is a single overshoot). If you use back.out, the overshoot is built in — you don't need the cosine. If you want a specific number of oscillations, use the cosine.

### The beat

```
in = 0.95s    hold = 0.67s    out = 0.87s
```

A concept beat: 0.95s to arrive, 0.67s to be read, 0.87s to leave. Total ~2.5s per concept.

**Worked example — a 36-second video with 5 story beats:**
| Beat | Start | In (0.95s) | Hold (0.67s) | Out (0.87s) | End |
|---|---|---|---|---|---|
| 1. Hook | 0.0s | 0.0–0.95s | 0.95–1.62s | 1.62–2.49s | 2.5s |
| 2. Prompt | 2.5s | 2.5–3.45s | 3.45–4.12s | — | — |
| 3. Response | 12.0s | 12.0–12.95s | 12.95–13.62s | 13.62–14.49s | 14.5s |
| 4. Result | 16.0s | 16.0–16.95s | 16.95–28.0s | 28.0–28.87s | 29s |
| 5. End card | 30.0s | 30.0–30.95s | 30.95–36.0s | — | 36s |

Notes:
- The Prompt beat (beat 2) has a long hold because typing takes time — the hold is the typing duration, not 0.67s. The 0.67s hold is for a concept (a short phrase); a typed prompt holds for as long as it takes to type.
- The Result beat (beat 4) has a very long hold because the payoff must play — the simulation runs, the data ticks. The hold is the proof.
- The End card (beat 5) has a long hold because the viewer needs to read the URL and remember the name.
- Scale the hold with the amount of text and the importance of the beat. Keep the in/out tight (0.95s / 0.87s) — those are the transitions, and they should be snappy.

### Group stagger

```
delay(j) = 0.03–0.08 × j     (j = item index; seconds)
```

Each item in a group starts 30–80ms after the previous one.

**Worked example — a list of 5 feature words, 50ms stagger:**
| Item | Index j | Delay (s) |
|---|---|---|
| Type a sentence | 0 | 0.00 |
| Watch it simulate | 1 | 0.05 |
| Live 3D physics | 2 | 0.10 |
| It obeys your words | 3 | 0.15 |
| Try it now | 4 | 0.20 |

The group takes 0.20s to start its last item, plus the item's own entrance (~0.3s), so the full group is visible at ~0.5s. The stagger is short — the group feels choreographed, not slow.

### Easing curves

- **expo.out:** `1 − 2^(−10t)` — fast start, gentle landing. At t=0.1, it's already at 50%; at t=0.5, it's at 97%. Clean and confident. The default for most entrances.
- **back.out:** overshoots the target by ~10% (overshoot factor ~1.7) then settles back. The element goes past its target and comes back. Personality. Use it for the moments that should feel alive.
- **Never ease-in for an entrance.** Ease-in starts slow — it feels like the video is buffering.

**How to choose:** if the element should feel competent, use expo.out. If the element should feel alive (a pop, a score, a result), use back.out. If you use back.out for everything, nothing feels special.

### Scale pop (the payoff)

```
scale: 0.94 → 1.0, ease back.out
```

The result scales from 94% to 100% with an overshoot. One pop, for the payoff.

**Worked example:** a result card appears at 22.4s. It scales from 0.94 to 1.0 over 0.4s with back.out. At 0.2s it overshoots to ~1.02, then settles to 1.0 at 0.4s. The pop is subtle (6% scale change) — the viewer feels it more than sees it.

### The animator (how a value sweeps across letters)

When an animator (a reveal, a blur, a wave) drives a value across text:

```
value = base + Σ (amount/100) × (animator(t) − base)
```

Each letter's value is its base plus the animator's contribution, scaled by the amount.

**Worked example — a Start sweep revealing "Hello" (opacity, amount = 100):**
- The animator goes from 0 to 1 across the word over 0.5s.
- At t=0.25s, the animator is at 0.5. The letters whose sweep position is < 0.5 are fully visible (opacity 1); the letters whose sweep position is > 0.5 are invisible (opacity 0); the letter at 0.5 is mid-reveal.
- The result: "Hel" is visible, "lo" is not yet — the word reveals left to right.

**Worked example — an Offset sweep driving a blur wave (amount = 50):**
- The animator is a wave that moves across the word. Each letter's blur = 50/100 × wave(t, letter_position).
- The letters the wave has passed are sharp; the letters the wave is on are blurred; the letters ahead are sharp. The blur moves across the word like a ripple.

### Gradient (colour across a range)

A gradient interpolates between stops:

```
color(x) = lerp(stop_A, stop_B, x)     (x = position along the gradient, 0–1)
```

**Worked example — a text gradient from navy rgb(12,30,51) to bright blue rgb(35,160,231):**
| Position x | Colour |
|---|---|
| 0.0 (left) | rgb(12,30,51) — navy |
| 0.25 | rgb(18,62,96) |
| 0.5 (middle) | rgb(24,95,141) |
| 0.75 | rgb(29,128,186) |
| 1.0 (right) | rgb(35,160,231) — bright blue |

For text, apply the gradient per character: each letter gets the full-text gradient, sized to the text width and offset by the letter's x position. A gradient on the parent does not paint through per-character spans — the spans inherit a transparent colour and the parent background isn't clipped to transformed descendants. Each span must carry its own gradient.

**For a background:** a linear gradient from one corner to the opposite. The angle is the direction from the start point to the end point (CSS 0deg = to top). A light-blue-to-white gradient (top-left light blue → bottom-right near-white) is the high-key studio background.

### Density (the floor)

```
keyframes ≥ 10 per second
layers ≥ 100
tweens ≥ 1500
text animators ≥ 5 (with per-char motion)
scenes ≥ 5
```

**Worked example — a 36-second video:**
- Keyframes: 36s × 10/s = 360 minimum. A good build has 400–500.
- Layers: 100 minimum. A good build has 150–220.
- Tweens: 1500 minimum. A good build has 2000–2500.
- Text animators: 5 minimum, with per-char motion. A good build has 10–18.
- Scenes: 5 minimum. A good build has 5–11.

If the numbers are below these, the video is too simple and will feel emotionless. Count the numbers before rendering — if the build is below the floor, add more beats, more layers, more animators. Do not render a thin build and hope the viewer won't notice; they will.

## Baseline numbers — the density floor

A video below these numbers ends up too simple and emotionless. These are FLOORS, not targets. Count the numbers before rendering — if the build is below the floor, add more beats, more layers, more animators.

| Measure | Minimum | Why | Reference |
|---|---|---|---|
| Keyframes | **300 total, ≥10 per second** | Below ~10/s the motion thins out and the video feels static. | A 52s demo ran 545 (~10.5/s). |
| Layers | **≥100** | A sparse layer tree = a sparse frame = no density of decisions. | Reference builds ran 168 and 216. |
| Tweens | **≥1500** | Tweens are the motion; under 1500 the video is mostly still. | Reference builds ran 2007 and 2416. |
| Text animators | **≥5, with per-char motion** | Per-letter motion is what makes text feel alive. | A reference build ran 18 (per-char reveals + blur/drop waves). |
| Scenes | **≥5** | One scene is a slideshow, not a demo. | Reference builds ran 11 and 5. |
| Segment length | **2–3s per segment** | Build slowly, 2–3s at a time, review every frame. Longer segments go stale. | — |
| Max static hold | **~2s** | No frame should sit still longer than ~2s. If nothing moves, the beat is dead. | — |
| Per-letter stagger | **0.08s × index** | The formula. Per-letter motion must be a formula, not a guess. | — |
| Concept beat | **in 0.95s / hold 0.67s / out 0.87s** | The choreography. Holds are reading time; the out makes room for the next beat. | — |
| Group stagger | **30–80ms** | For groups entering together. | — |
| UI durations | **sub-300ms** | Snappy, not sluggish. | — |
| Duration | **30–52s** | Shorter than 30s can't carry the story; longer than ~52s drags. | Reference builds ran 52s, 36s, 38s. |
| Render | **12fps, 640×360** | The pipeline standard. 12fps changes judgment — judge in motion, but a frozen frame must still read correctly. | — |
| Verification frames | **≥5 timestamps, viewed by you** | Across the timeline (opening, prompt, result, mid, end). Never deliver a video you haven't watched frame by frame. | — |

**The density ladder.** If a build is below the floor, add density in this order (cheapest first):
1. More text animators (per-char reveals are cheap and make the biggest difference).
2. More beats (split a long beat into two shorter beats with a transition).
3. More layers (add background blobs, glass cards, shadows — the built space).
4. More tweens (animate the background, the camera, the secondary elements).

**The density test:** if you can describe the video in one sentence ("text fades in, then a screenshot"), it is too simple. A winning video needs a sentence per beat — and the beats must be driven by the formulas above, not by invention.

## Craft rules — what makes it stunning, professional, winning

- **Punchy SaaS, high-energy.** Not calm white-studio, not minimal-poster. The video must feel like a product launch, not a screensaver. The energy comes from the beat rate (a beat every ~2.5s), the easing (expo.out and back.out, not linear), and the density (many layers moving). A calm video is a video with no beats.
- **The frame is a built space first.** Native high-key 3D studio space: diffused ambient light, soft shadows, glass cards. Soft blobs and a grade before any text appears. The space is built first; the content enters a space that is already there. A video that is just text on a flat colour is a slideshow.
- **Motion is choreography with beats.** In / hold / out. Holds are reading time. Overlap is intentional flow, not a bug. The beats are the choreography; the equations are the notation.
- **Easing is the emotion.** expo.out = clean. back.out = overshoot = personality. Ease-out (never ease-in) for entrances. Custom cubic-bezier curves. Transform/opacity-only motion. The easing curve IS the feeling — choose it the way you would choose a word.
- **Text is geometry.** Per-letter motion is a formula (0.08s × index, damped cosine). Text animators are real: Start sweeps reveal char-by-char; Offset sweeps drive blur/drop waves. Text that appears as a block is a label; text that arrives letter by letter is a voice.
- **Transitions are moving shapes, not fades.** Container/text transforms. Never fade-in/fade-out. A fade is the absence of a transition.
- **Real UI elements.** Liquid glass, real component libraries. Never custom-CSS styling passed off as glass. Never fake 2D as 3D. If the product has a real UI, show the real UI — a recreation of it is a mock.
- **Narrated actions must be shown on screen, not merely described.** If the voice says it, the frame must show it. A narration that describes an action the viewer cannot see is a radio ad.
- **The camera must move. No dead-air static text intros. No hard cuts.** The camera is the viewer's eye; if it doesn't move, the viewer is staring at a photograph.
- **Stunning = density of deliberate decisions.** The professional templates carry hundreds of layers and keyframes because every beat is a decision. If the decisions aren't there, the video is slop. Density is not clutter — it is the accumulation of deliberate choices.
- **JEV (Just Evaluate) for the demo idea itself:** start from what's trending TODAY that can actually be tested. Take that capability → build a simple WebGL site for engagement → a creative visualization take displaying the capability's performance → it must genuinely use the feature, never a scripted mock. The visual has to be instantly legible and eye-catching. Existing projects are OPTIONAL touches, never mandatory — do not force them in.
- **The viewer's eyes outrank every claim.** Never assert a quality gain the viewer can see through. Plain admission + a rebuilt real thing is what buys trust back.

## Antipatterns — every faulty step, do NOT do these

Each antipattern has a before (what it looks like when you do it) and an after (what to do instead).

| Antipattern | Before (the fault) | After (the fix) |
|---|---|---|
| Rebuild from video pixels / scene detection | "I'll extract the motion from the preview video." The card segment fails; the motion is lossy. | Generate the motion from the patterns and equations. Use video only to choose a reference. |
| Hand-patch the output to fix a visual flaw | "The text is off, I'll nudge it in the HTML." The flaw is in the mechanism; the patch doesn't survive the next build. | Fix the generator/converter, verify the output, then render once. |
| Render → spot-fix → re-render loop | "I'll render, see what's wrong, patch it, render again." Burns renders, never finds the root cause. | Fix the mechanism first, verify, then render once. |
| Fade-in / fade-out transitions | A scene fades out, the next fades in. It feels like a PowerPoint. | Moving-shape transitions: a wipe, a panel, a card. |
| Custom-CSS "glass" | A grey rectangle with a border, called "glass." It reads as grey. | Real liquid glass / real component libraries. |
| Fake 2D as 3D | A flat shape with a shadow, called "3D." The viewer calls it slop. | Actual 3D (Three.js / CSS 3D / a cloned 3D path). |
| Dead-air static text intro | White text on a flat colour, sitting still for 3 seconds. | The camera moves; the text arrives letter by letter; the space is built. |
| Hard cuts | Scene A, cut, scene B. The story stops and restarts. | Moving-shape transitions; the next beat enters as the previous exits. |
| Letterbox a dark recording in white borders | A dark screen recording inside white borders. It looks like an unedited recording in a frame. | Native high-key studio space, diffused light, soft shadows, glass cards. |
| Scripted mock passed off as the real feature | A fake UI that pretends to be the product. Hard line — the viewer can tell. | Show the real product working (live, recorded, or captured — genuinely). |
| Text running off the edge | A replacement phrase longer than the original runs off the right edge ("to simulate physic"). | Measure the text; shorten the phrase or reposition. |
| Static shape overlapping an animated layer | A static rect sits in scrolling text's path and reads as a strikethrough. | Check for static-vs-animated collision explicitly before rendering. |
| Trust a third-party critique without checking the file | A critique describes a version that was never rendered. Two of three audits were fabricated/stale. | Verify every critique claim against the delivered file (extract frames) before building on it. |
| Present a video you haven't watched frame by frame | "The render finished, so it's done." The viewer catches flaws the agent's verification missed. | Extract and view frames yourself before delivering. |
| Claim a quality gain the viewer can see through | "This version is much smoother." The viewer watches it and it isn't. | Plain admission + a rebuilt real thing. |
| One scene, one beat | A single static scene for 30 seconds. That is a slideshow. | At least 5 scenes, a beat every ~2.5s, the camera moving. |
| Everything moves at once | Every element animates simultaneously. The viewer doesn't know where to look. | One thing moves at a time (mostly). The element carrying the beat moves; the rest supports it. |
| The payoff freezes | The result plays for 1 second then freezes. It's a screenshot with an intro. | The payoff keeps moving for its entire beat (the loop pattern). |
| The end card is unreadable | The URL is too small or the name is cut off. The viewer can't act on the video. | The end card settles, fully visible, no truncation. The URL is legible. |
| The prompt appears three times | The viewer is asked the same question three times and stops caring. | Prompt once; the rest of the video is the answer. |

## Building the video — implementation

How to turn the story and the patterns into a rendered video. This is the mechanics of the build, not the motion itself.

### The HyperFrames build (HTML + GSAP)

The video is an HTML page driven by a GSAP timeline. The page is a stage (1920×1080 or 3840×2160, scaled to 640×360 on encode). Each element is a DOM node; each motion is a GSAP tween on the timeline.

**Structure:**
- **Stage:** a full-stage div. The background (gradient, blobs, grade) is built first, as the lowest layers.
- **Layers:** each visual element is a node. Text is split into per-character spans (inline-block, so transforms apply). Shapes are SVG or divs. The result (a recording or a live product) is a video element or an image sequence.
- **Timeline:** a single GSAP timeline. Each beat is a set of tweens at its time window (in / hold / out). The timeline is the score; the tweens are the notes.
- **Per-character text:** split the text into spans, one per character. Each span gets its own delay (`0.08 × index`) and its own gradient (sized to the full text width, offset by the character's x). Spaces are `&nbsp;` spans; line breaks are empty spans + `<br>`.

**GSAP timeline sketch (the shape of the code, not a full implementation):**
```js
const tl = gsap.timeline({ defaults: { ease: "expo.out" } });
// Beat 1 — Hook (0–2.5s): the brand reveals letter by letter
tl.from(".hook .char", { y: 30, opacity: 0, duration: 0.95, stagger: 0.08 }, 0);
// Beat 2 — Prompt (2.5–12s): the prompt types
tl.from(".prompt .char", { opacity: 0, duration: 0.05, stagger: 0.08 }, 2.5);
// Beat 3 — Response (12–16s): the answer pops in
tl.from(".response", { scale: 0.94, opacity: 0, duration: 0.4, ease: "back.out(1.7)" }, 12);
// Beat 4 — Result (16–30s): the payoff plays (a video / image sequence)
tl.fromTo(".result", { scale: 0.94 }, { scale: 1, duration: 0.4, ease: "back.out(1.7)" }, 16);
tl.to(".result", { /* the result's own motion plays */ }, 16.4);
// Beat 5 — End card (30–36s): the brand + URL settle
tl.from(".endcard", { y: 20, opacity: 0, duration: 0.95 }, 30);
```

**Key implementation rules:**
- Apply the stage scale explicitly after every timeline jump (goto). The stage is larger than the viewport; the scale must be re-applied or the elements render at the wrong size.
- Per-character spans need `display:inline-block` or transforms silently don't apply.
- For a gradient on text, apply the gradient to EACH per-character span (background-clip:text), not to the parent — a parent gradient does not paint through transformed spans.
- For a video/image-sequence result, drive it from the timeline (seek the video to the beat's time, or advance the image sequence with the timeline). Verify the result is actually moving in the rendered frames, not frozen on its first frame.

### Render and encode

- **Render:** Playwright (Chromium) loads the page, seeks the GSAP timeline to each frame time (12fps), and screenshots. The render is a frame capture, not a screen recording — each frame is a deterministic seek, so the output is reproducible.
- **Encode:** `ffmpeg -framerate 12 -i frames/f%04d.png -vf scale=640:360 -c:v libx264 -pix_fmt yuv420p`. Verify the duration and the frame count (no gaps, no zero-byte frames).
- **Check the density before rendering:** run `scripts/check_density.py` on the build (see the repo's `scripts/`). It counts keyframes, layers, tweens, text animators, and scenes and reports PASS / FAIL against the floors. If a measure is below the floor, add density (animators first, then beats, then layers, then tweens) before rendering. Do not render a thin build.
- **Start from the starter:** the repo's `templates/starter.html` is a minimal working HyperFrames page with the five story beats and the patterns applied. Copy it and adapt it to your product. It is intentionally minimal — the density check will report it below the floor; that is expected for a starter.
- **Verify before you call it done:** see the checklist below.

### A note on .aep (optional, not required)

If a .aep file IS available, it is a source of motion patterns: its keyframes are the ground truth for that template's motion. Parsing it (py-aep) gives the layer tree, the keyframes, and the eases as text. The converter rules that matter most when a .aep is present: key parent/child by unique layer id (never by name — templates duplicate names); text justification is anchor-dependent (check the anchor before applying a translateX); extract Gradient Ramps (never ignore them — they define the colour world); clone 3D paths and substitute a placeholder 3D when the model is unavailable; bake pre-comp instances with their parent chain (flattening drops it). But none of this is required — the patterns and equations above are sufficient to generate the motion from a prompt alone.

## Worked example — a complete prompt-to-video build

A full walkthrough, from prompt to timeline, so you can see the method applied end to end.

**Prompt:** "Show a product that turns a typed sentence into a live physics simulation — the viewer should feel that typing a sentence makes physics happen."

**Step 1 — The story (beats with timings, 36s total):**

| Beat | Time | What the viewer learns | What moves |
|---|---|---|---|
| 1. Hook | 0–3s | The promise: "Type a sentence. Watch physics happen." | The line reveals letter by letter, large, centred. |
| 2. Prompt | 3–12s | A user asks: "Simulate a falling ball." | The prompt types character by character in the product's input. |
| 3. Response | 12–16s | The product answers: "Simulation active." | The reply slides in; the controls appear (staggered). |
| 4. Result | 16–30s | The ball falls, the trajectory draws, the data ticks. | The simulation plays continuously — the ball moves, the trajectory draws, the numbers tick. |
| 5. End card | 30–36s | The product name + URL. | The brand + URL settle, fully visible. |

**Step 2 — The motion (patterns + equations per beat):**

- **Beat 1 (Hook):** the line "Type a sentence. Watch physics happen." (34 characters, including spaces). Per-letter delay: `0.08 × i`. The last letter starts at `0.08 × 33 = 2.64s`. With a 0.3s letter entrance, the full line is visible at ~2.94s — inside the 3s hook window. Pattern: per-letter motion (damped cosine, A=30px, λ=4, ω=12). Easing: expo.out. The background (high-key gradient + soft blobs) is already built.
- **Beat 2 (Prompt):** the prompt "Simulate a falling ball" (24 characters) types in the input. Per-letter delay: `0.08 × i`, so the last letter starts at `0.08 × 23 = 1.84s`. The typing takes ~2.1s total. The input box itself slides in first (0.95s, expo.out), then the typing starts. Pattern: per-letter motion (typing — opacity only, no offset, because typing is a reveal, not a bounce).
- **Beat 3 (Response):** the reply "Simulation active" slides in (0.95s, expo.out), and the controls (4 items) stagger in at 50ms each (0, 0.05, 0.10, 0.15s). Pattern: stagger + beat (in/hold/out).
- **Beat 4 (Result):** the simulation plays. The ball falls (a draw-on trajectory + a moving ball), the live data ticks (a count-up for the height/distance), the trajectory draws itself. The result pops in with a scale pop (0.94 → 1.0, back.out) at 16s, then plays continuously for 14s. Patterns: scale pop, draw-on, count-up, the loop (the payoff keeps moving). This beat has the most keyframes and the most tweens — it is the density centre of the video.
- **Beat 5 (End card):** the brand + URL. The brand reveals letter by letter (per-letter, 0.08 × i), the URL fades in below it (opacity, 0.4s). The end card holds for 6s so the viewer can read the URL.

**Step 3 — The density check (before rendering):**
- Keyframes: Hook (~34 letters × 2 keyframes each = 68) + Prompt (~24 × 2 = 48) + Response (~20) + Result (~200, the simulation) + End card (~30) = ~366. Target: ≥300 total, ≥10/s. 366 / 36s = 10.2/s. Pass.
- Layers: background (gradient + 3 blobs + grade = 5) + Hook (1) + Prompt (input + text = 2) + Response (reply + 4 controls = 5) + Result (sim viewport + ball + trajectory + data panel = 4) + End card (2) + camera/grade overlays (2) = ~21 layers. That is BELOW the ≥100 floor — add more layers: more background blobs, glass cards, shadows, secondary UI elements, decorative shapes. A thin layer tree is the most common reason a build feels simple. Add layers until the count is ≥100.
- Tweens: each keyframe is a tween (or a set of tweens). ~366 keyframes → ~400+ tweens. That is BELOW the ≥1500 floor — the Result beat needs more tweens (the ball, the trajectory, the data, the camera, the background all moving). Add tweens until the count is ≥1500. If the tween count is low, the video is mostly still.
- Text animators: Hook (1), Prompt (1), Response (1), End card (1) = 4. That is BELOW the ≥5 floor — add one more (e.g. a feature-word animator in the Response beat, or a per-letter wave on the Hook). 
- Scenes: 5 (one per beat). Pass (≥5).
- The density check caught three shortfalls (layers, tweens, animators) BEFORE rendering. Fix them now — add the layers, the tweens, the animator — then render. Do not render a thin build and hope the viewer won't notice.

**Step 4 — Render, verify, deliver.** Render at 12fps, encode, extract 5+ frames (t=1, t=8, t=14, t=22, t=33), view them, check the checklist below, deliver.

## Verification — the checklist

Before you call a video done, check every item. If an item fails, fix the mechanism (the generator), not the output, and re-render once.

**Story:**
- [ ] The five beats are all present (Hook, Prompt, Response, Result, End card).
- [ ] The prompt appears exactly once (or the story explicitly justifies a repeat).
- [ ] The result is the product actually working (moving), not a static image.
- [ ] The end card (brand + URL) is fully visible, no truncation, legible.

**Motion:**
- [ ] Keyframes ≥10/s, layers ≥100, tweens ≥1500, text animators ≥5, scenes ≥5. (Count them.)
- [ ] No frame sits still longer than ~2s. (Scrub the timeline; if a stretch is static, add motion.)
- [ ] The camera moves (a push or a pan is visible across the video).
- [ ] No fade-in/fade-out transitions. (Transitions are moving shapes.)
- [ ] Text arrives letter by letter (per-letter motion), not as a block.
- [ ] The payoff has a scale pop and keeps moving for its whole beat.

**Correctness:**
- [ ] Text is legible at every checked timestamp (not cut off, not overlapping, not the wrong colour).
- [ ] No duplication (each string appears exactly once unless the story duplicates it).
- [ ] No truncation (no word cut at the frame edge).
- [ ] No static-vs-animated collision (no static shape in a moving layer's path).
- [ ] The result animation is actually moving in the rendered frames (not frozen on its first frame). Compare two frames 1s apart in the result beat — they must differ.

**Honesty:**
- [ ] The video genuinely shows the real capability (not a mock). If a capability is shown, verify it exists.
- [ ] The number/score shown is the product's real number, not a computed or placeholder value.
- [ ] Gaps are named (transitions, grades, or effects not reproduced). Don't fake them.
- [ ] The video was watched frame by frame by you (≥5 timestamps viewed), not just rendered.

## The one-sentence version

Prompt → story beats (Hook → Prompt → Response → Result → End card) → patterns and equations (per-letter 0.08s × index, damped cosine, in 0.95 / hold 0.67 / out 0.87, expo.out / back.out, moving-shape transitions, built space, scale pop 0.94→1) → dense, high-energy video that genuinely shows the real product — verified frame by frame, with the density floors met (≥300 keyframes, ≥100 layers, ≥1500 tweens, ≥5 animators, ≥5 scenes) so it never feels simple and emotionless.
