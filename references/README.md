# Reference builds

Two verified HyperFrames builds, included as reference. These are the real, rendered templates the skill was learned from — not the starter. Read them to see how the patterns and equations look in a full, dense build: the layer tree, the GSAP timeline, the per-character text animators, the gradient handling, and the density numbers.

The third template (the AI Intro) is **excluded** — it is the broken one, and the skill does not build on it.

## `saas-v3/` — Template 1: SaaS (52s)

- **File:** `saas-hyperframes-v3.html` (631 KB)
- **Rendered video:** 52s, 624 frames, 12fps, 640×360
- **What it is:** a SaaS product promo built from a purchased After Effects template. 11 scenes, 168 layers, 545 keyframes, 18 Range Selector text animators (per-character reveals + blur/drop waves). The density reference for the skill's floors.
- **What to look at:** the per-character spans and their Range Selector animators (the `text_animator` output), the beat structure (in 0.95s / hold 0.67s / out 0.87s), the moving-shape transitions, and the built space (gradient background, soft blobs, glass cards).
- **Fonts (free, Google Fonts):** Darker Grotesque (Medium), Plus Jakarta Sans (Medium). Download the TTFs and place them in a `fonts/` folder next to the HTML — the `@font-face` rules already point there. Without them the page falls back to a system sans-serif; the motion and structure still work.

## `ui-demo-v3/` — Template 2: UI Demo (36s)

- **File:** `ui-demo-anim.html` (682 KB)
- **Rendered video:** 36.083s, 433 frames, 12fps, 640×360
- **What it is:** a UI walkthrough (prompt → preferences window → message panel → end card), built from an After Effects template. 56 comps, 216 layers, 77 parented. The verified build — v3 fixed the two converter bugs (text justification and name-keyed parent/child) that broke v1 and v2.
- **What to look at:** the id-keyed parent/child structure (duplicate layer names are handled by unique id), the anchor-dependent text justification (RIGHT/CENTER/LEFT handled by anchor, not by blind translateX), and the pre-comp instances (the message panel, the prompt input, the preferences window).
- **Fonts (free, Google Fonts):** Bricolage Grotesque (Regular, Medium, SemiBold, ExtraBold), Roboto (Light, Regular, Medium, Bold). Download the TTFs and place them in a `fonts/` folder next to the HTML — the `@font-face` rules already point there. Without them the page falls back to a system sans-serif; the motion and structure still work.

## How to view them

Each folder is self-contained apart from the fonts (see above). Open the HTML in a browser — the GSAP timeline plays automatically. `gsap.min.js` is included in each folder (same version in both).

## Why the fonts are not in the repo

The TTFs are binary files and this repo is pushed as text. They are all free Google Fonts — download them from Google Fonts (or the links in each template's font list) and drop them into `fonts/` next to the HTML. The `@font-face` rules are already written; nothing else needs to change.
