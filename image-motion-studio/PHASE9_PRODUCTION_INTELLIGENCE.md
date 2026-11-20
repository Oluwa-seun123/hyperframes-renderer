# Phase 9 — HFX Production Intelligence

## Purpose
A phone-first, deterministic creative producer that converts a product/campaign brief into a structured cinematic story, HFX shot plan, asset inventory and preflight checklist.

## Open
Open `production-intelligence.html` in a modern browser. It runs locally in the browser and does not upload the selected assets.

## Workflow
1. Enter product, finish, campaign objective, audience, verified product advantage, customer tension, creative direction and CTA.
2. Optionally select a self-contained GLB, multiple real product photographs and a logo/end card.
3. Generate the production plan.
4. Review the story beats, shot durations/moves/captions, continuity rules and preflight actions.
5. Export `hfx-shot-plan.json` and import it into Phase 7 Production Pipeline.
6. If using a GLB, use the same file with the Phase 8 HyperFrames Exporter. Export the HTML composition and run the existing HyperFrames check/render workflow.
7. Export the Markdown production brief for the editor, asset creator or collaborator.

## HFX shot-plan contract
The JSON uses the Phase 7 format:
- `format: "hfx-shot-plan"`
- `version: 1`
- `project`
- `output: { aspect, fps }`
- ordered `shots` containing `order, name, duration, move, elevation, transition, caption`

Allowed movement values are compatible with Phase 7/8: orbit, orbit360, turntable, push, pull, rise and hero. The Phase 9 director deliberately selects only real geometry-based orbit/turntable moves when a GLB is present. Without a GLB it favours safe hero/push/pull/rise framing and warns that photographs must be treated as separate views.

## Story structure
The generated arc follows a useful advertising sequence: hook → customer tension → product reveal → feature/detail → payoff/proof → hero → invitation. The exact beat labels adapt to campaign objective and the plan duration. It is a deterministic rule-based planning tool, not an AI model and not a substitute for creative review.

## Preflight checks
Checks for product image/GLB presence, number of views, logo/end card, large GLB input, missing CTA and claims needing official verification. The score is a simple issue-count indicator, not a quality guarantee or legal/product approval.

## Limitations
- Assets are inventoried by filename and size only. The app does not inspect image content, verify that a photograph really shows the labelled side, or upload/attach selected assets into the exported shot plan.
- It does not generate images, video, 3D models, voiceover, music or sound effects.
- It does not verify product claims against manufacturer sources. Human verification is required.
- It creates the same Phase 7 shot-plan schema so it can hand off to existing tools; it does not render an MP4 itself.
- GLB geometry is required for true orbit and turntable. Multiple product photos remain separate real views; no hidden sides are invented.
- Android browser testing and a complete GLB-to-MP4 render remain outstanding.
- No paid API or paid generative-video service is used.
