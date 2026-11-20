# Phase 8 — HFX HyperFrames Exporter

## Purpose

Bridge the Phase 7 HFX shot-plan JSON to the existing HyperFrames HTML-to-video renderer. This phase creates a real Three.js-based HTML composition that HyperFrames can seek and capture frame by frame.

## Use
1. In Phase 7, load a product GLB and create the shot sequence.
2. Export the shot-plan JSON.
3. Open hfx-hyperframes-exporter.html.
4. Select the same self-contained GLB and the exported shot-plan JSON.
5. Choose output dimensions and frame rate.
6. Compile and download hfx-hyperframes-composition.html.
7. Place that file at image-motion-studio/project/index.html on the feature branch.
8. Run the existing HyperFrames check and render workflow. Inspect the generated MP4 before delivery.

## Composition contract

The generated root composition includes data-hf-id, data-composition-id, data-start, data-duration, data-width, data-height and data-fps metadata. The GLB bytes are embedded as base64. Three.js GLTFLoader parses the model before the module finishes loading; only then is the paused GSAP timeline exposed as window.__timelines.main. Seeking that timeline drives the model and camera to a deterministic frame.

Supported shot moves: orbit (180 degrees), orbit360, turntable, push, pull, rise and hero. Each shot includes duration, elevation, transition and caption.

## Fixed output sizes

- Portrait: 1080 × 1920
- Landscape: 1920 × 1080
- Square: 1080 × 1080

The frame rate is stored in composition metadata. HyperFrames CLI uses the project/composition FPS according to the renderer's supported configuration.

## Validation and limitations

The GitHub Actions workflow statically checks the browser editor scripts and existing HyperFrames demo composition. The generated composition still needs to be rendered with a real GLB to verify the asynchronous module load, model decode, Three.js capture and final MP4 output.

Use self-contained GLB only. External-resource GLTF files are not packaged. The exporter rejects files larger than 100 MB to reduce browser memory risk. Three.js and GSAP are loaded from jsDelivr, so the rendering environment requires internet access.

This phase does not yet add voice, music, sound effects, HDRI environment maps, path tracing, true lens simulation, or a cloud render service. It produces the HyperFrames composition input; it does not claim the MP4 render is already complete.
