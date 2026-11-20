# Phase 17 — Integrated 3D Advertising Sequencer

A mobile-first local GLB viewer and camera shot sequencer.

## Features
- Load GLB locally in browser with Three.js GLTFLoader.
- Camera orbit and smooth shot interpolation around model bounding-box center.
- Editable shot azimuth, elevation, camera distance and duration.
- Add/remove shots, play/stop/reset.
- Export shot plan JSON.
- Capture browser WebM preview using MediaRecorder (not final MP4).

## Connected workflow

Exported JSON now uses the shared `hfx-shot-plan` schema and includes compatibility `move`, `elevation`, `transition`, and `caption` fields. Import it directly into Phase 7 Production Pipeline, then use that plan in Phase 8 HyperFrames Exporter. The Phase 17 azimuth/elevation/distance values are retained as extra fields for reference. The generated export defaults to portrait 9:16 at 30 fps; review framing before compiling.


## Validation limits
- Camera azimuth presets are geometric, not automatically labeled as exact front/back without user visual confirmation.
- Model is locally loaded; not committed to repo.
- Final MP4 rendering and visual quality must be verified separately in the CI renderer.
- WebM recording support varies by mobile browser.
