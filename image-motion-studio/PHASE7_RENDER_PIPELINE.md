# Phase 7 — HFX Production Pipeline

The Production Pipeline connects the real-time GLB/GLTF stage to a deterministic, ordered shot timeline.

## Open
Open render-pipeline.html in a modern mobile browser. It loads Three.js modules from jsDelivr, so an internet connection is required. Prefer a self-contained GLB file on Android.

## Workflow
1. Load a GLB/GLTF product model.
2. Add shots or load the six-shot product reveal template.
3. Choose duration, camera/object movement, orbit elevation, transition and caption for each shot.
4. Reorder or remove shots in the timeline.
5. Preview the full sequence.
6. Export the HFX shot plan JSON for persistence or downstream integration.
7. Record a WebM preview/master from the WebGL canvas.

## Shot-plan format

The exported JSON uses format "hfx-shot-plan", version 1, output aspect/FPS settings, and an ordered shots array. Supported moves are orbit, orbit360, turntable, push, pull, rise, and hero. Each cue stores a name, duration, elevation, transition and caption.

## Accuracy and rendering boundaries
- Orbit and turntable moves operate on actual GLB/GLTF geometry, not a flat photograph.
- The preview uses Three.js and the user's browser GPU. Large models can exceed mobile memory or GPU limits.
- Browser recording is WebM and records the stage viewport. It is not a final MP4 and does not yet render voice, music or sound effects.
- The shot-plan JSON is the integration contract for the next server-side/HyperFrames render adapter. This phase does not claim that HyperFrames currently renders the Three.js scene or that MP4 export is complete.
- Transitions are hard cuts or fade-through-black; this is not yet a multi-camera cross-dissolve.
- The requested aspect/FPS are saved in the shot plan. The current browser preview uses the responsive stage dimensions and selected FPS for recording; exact output canvas sizing is a later render-adapter responsibility.
- No paid generative-video API is used. Model loading and rendering happen in the browser; the Three.js modules are downloaded from jsDelivr.

## Validation
The repository workflow includes a Node syntax check for the browser studio modules. Static syntax validation does not replace Android testing with a real model or a completed MP4 render.
