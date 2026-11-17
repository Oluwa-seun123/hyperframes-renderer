# HyperFrames Image Motion Studio (first build)

This is an experimental, phone-friendly image-to-motion authoring tool that extends the existing HyperFrames renderer. It does not replace HyperFrames.

## What is included

- `editor/index.html`: a browser-based editor. Choose a still image, describe the shot in plain English, select duration and aspect ratio, preview the interpreted camera move, and export a self-contained HyperFrames HTML composition.
- `project/`: a small HyperFrames project with a procedural product-shaped demo scene, plus pinned CLI scripts.
- `.github/workflows/render-image-motion.yml`: checks and renders changes to the project folder, then uploads MP4 output as a downloadable workflow artifact.

## Use the editor

Open `editor/index.html` in a modern browser. On Android, download the file from this repository and open it in Chrome, or publish this folder as a static site. Select a photo and try prompts such as:

- `Slow cinematic push in, pan gently to the left`
- `Pull out slowly and tilt up`
- `Subtle orbit with a dramatic reveal`

The first motion compiler recognises camera-direction phrases and turns them into a deterministic GSAP timeline. It is intentionally rule-based in this first milestone; it does not call a paid AI API.

## Export and render

The exported HTML embeds the chosen image as a data URL, so it is a single file. Put that HTML at `project/index.html` (replacing the demo) and push the change. The workflow runs the pinned HyperFrames check and render commands. The resulting MP4 is uploaded as a GitHub Actions artifact.

You can also run the project locally:

```bash
npm run check
npm run render
```

Run those commands from this `project/` directory.

## Current limits — important

- This version animates the pixels in the uploaded photograph. It creates cinematic camera motion, a soft depth-like background treatment, lighting glow and text reveals.
- It does **not yet** segment the subject from the background, estimate a depth map, inpaint hidden regions, or reconstruct a true 3D model. Those are the next Image Intelligence / Photo-to-Scene milestones.
- A single photo cannot reveal accurate unseen sides of a product. For a faithful 360-degree orbit, supply an official 3D model or several accurate views.
- The editor's preview is a quick browser approximation; the HyperFrames render is the final output.


## Phase 2 — Image Intelligence and Photo-to-Scene

The editor now includes two optional, browser-run AI tools:

- **AI isolate subject** uses `Xenova/modnet` through Transformers.js to produce a transparent product cutout. The model card declares Apache-2.0. MODNet was designed for portrait matting, so results on phones, reflective products, thin camera rings and complex edges must be checked visually.
- **Generate depth map** uses `onnx-community/depth-anything-v2-small` through Transformers.js. The model card declares Apache-2.0. Its relative depth estimate is converted into four overlapping transparent depth bands. The exported HyperFrames composition moves those bands at different rates for a stronger parallax effect.

Both models run on the user's device (WebGPU when available, WASM CPU fallback). The first use downloads model weights from Hugging Face and requires an internet connection. The depth model download is roughly 300 MB; this may be slow or memory-intensive on some Android phones. Keep the browser tab open while it loads and processes. No image is uploaded to our own server by these two tools.

### What this phase does not do yet

- The four bands are approximate slices of a monocular depth map, not separate object meshes.
- There is no generative inpainting yet, so the system cannot convincingly fill the background behind a removed object.
- MODNet is a portrait-matting model; product cutout quality varies and must be inspected.
- There is no image-to-3D reconstruction or true 360-degree orbit yet. For accurate hidden sides, use a genuine product GLB/GLTF or multiple official views.
- Model weights are fetched from their publishers at runtime; commercial use should follow each model's published licence and attribution terms.

Official model references:
- [Transformers.js browser inference](https://huggingface.co/docs/transformers.js)
- [Xenova MODNet (Apache-2.0)](https://huggingface.co/Xenova/modnet)
- [Depth Anything V2 Small ONNX (Apache-2.0)](https://huggingface.co/onnx-community/depth-anything-v2-small)

No paid video-generation API is used.


## Phase 3 — Multi-view Product Sequence

A new phone-friendly editor is available at `multiview.html`. It accepts several separate product-view images, lets the user label each view, reorder shots, set seconds per view and output aspect ratio, preview the sequence, and export a self-contained HyperFrames HTML composition.

This is designed for products supplied as multiple official/reference views when a true 3D asset is not available. Each angle remains a separate shot with its own subtle push-in and crossfade. The sequence can reveal rear, side, bottom/ports, front display and camera details before a final hero title.

### Important accuracy boundary

- This is a multi-angle editorial sequence, not a 3D model and not a continuous 360-degree orbit.
- It does not synthesize unseen surfaces or interpolate physically correct rotation between photographs.
- Use matching, clean, high-resolution views of the same product and remove any captions or sheet borders before upload.
- The exported HTML embeds the selected images. HyperFrames still performs the final render.

Open `multiview.html` in a mobile browser, select multiple cleaned views, reorder them, preview, then export.


## Phase 4 — HFX Scene Language

The experimental `scene-studio.html` adds a small declarative language for directing product-ad scenes. It parses project settings, aspect ratio, frame rate, background/light mood, title/subtitle, asset declarations and shot commands. Each shot specifies an uploaded asset, duration, camera-move preset, movement strength, transition and label.

The compiler validates syntax, declared assets and uploaded image availability before exporting a self-contained HTML composition with a deterministic GSAP timeline. The exported scene exposes `window.__timelines.main` for seeking.

See [HFX Scene Language reference](SCENE_LANGUAGE.md) for grammar and examples.

This phase is a real compiler and multi-view 2D scene pipeline, not a 3D renderer. Real product orbit, physically based materials, lighting rigs and GLB/GLTF import are future compiler/runtime targets. It does not invent unseen product surfaces. No paid generative-video API is used.


## Phase 5 — Cinematic Director

The experimental `cinematic-director.html` converts cinematography choices into structured shot plans and HFX Scene Language shot skeletons. It captures framing, named camera technique, lens/focal length, focus behaviour, key-light placement, composition, duration, transition, story purpose and continuity guardrails.

The shot recipes are adapted from the ASO Creative Studio's Cinematic Techniques Reference. The director distinguishes 2D-safe moves from techniques that require genuine multi-view footage or GLB/GLTF geometry. It does not fake a 360 orbit or product rotation from a single still.

The Master Idea Library's creative sequence — real object/task, specific tension, visible choice, satisfying reveal, honest invitation — is used as a planning check, not as a copied idea or performance promise.

See [Cinematic Director documentation](CINEMATIC_DIRECTOR.md).


## Phase 6 — HFX 3D Product Engine

The experimental `3d-engine.html` is a phone-responsive browser studio for loading real GLB/GLTF product models. It uses Three.js GLTFLoader and OrbitControls, normalizes the model into the camera view, and provides manual camera orbit/zoom, animated camera orbit, vertical-axis product turntable, camera height/distance, studio key/rim/fill lights, background, material metalness/roughness offsets, PNG still capture and browser WebM viewport recording.

Prefer a self-contained GLB on mobile. The tool loads the selected model locally in the browser and does not upload it to our server. Three.js modules load from jsDelivr, so an internet connection is required.

See [3D Engine documentation](3D_ENGINE.md).

### Phase 6 limits

- This is a real-time GLB/GLTF viewer and capture stage, not yet a full production renderer or integrated HyperFrames 3D timeline.
- PNG and WebM captures are browser outputs. WebM is not the final HyperFrames MP4.
- No HDRI environment lighting, ray tracing, path tracing, physically calibrated camera/lens simulation or AI image-to-3D reconstruction is included.
- Large models may exceed Android memory/GPU limits. Optimize geometry and textures before loading.
- JavaScript syntax passed a static check; Android device testing and a completed model capture remain unverified.


## Phase 7 — HFX Production Pipeline

The experimental `render-pipeline.html` connects real GLB/GLTF geometry to a deterministic shot timeline. Load a product model, create and reorder shots, select camera orbit (180°/360°), object turntable, push/pull, rise or hero hold, choose duration/elevation/transition/caption, preview the sequence, and record a WebM viewport preview.

The pipeline exports/imports a versioned `hfx-shot-plan.json` document with ordered shot cues and output aspect/FPS metadata. This is the hand-off contract for the next HyperFrames render adapter.

See [Phase 7 documentation](PHASE7_RENDER_PIPELINE.md).

### Phase 7 boundaries

- The 3D camera and object movements operate on actual loaded model geometry.
- The browser preview is responsive; the selected aspect ratio and frame rate are recorded in the shot plan. Exact fixed-dimension output is for the render adapter.
- WebM recording is a browser preview/master, not the final MP4.
- There is no voice, music, sound-effects, true cross-dissolve, or server-side Three.js-to-HyperFrames renderer in this phase.
- The browser studio module syntax is checked in GitHub Actions. A successful syntax check does not prove Android compatibility or a completed render with a real phone model.


## Phase 8 — HFX HyperFrames Exporter

The experimental `hfx-hyperframes-exporter.html` bridges a Phase 7 shot-plan JSON and the existing HyperFrames HTML-to-video renderer. It accepts a self-contained GLB plus the shot-plan JSON, embeds the GLB bytes in one generated HTML composition, and compiles a deterministic Three.js scene controlled by a paused GSAP timeline exposed at `window.__timelines.main`.

The generated composition uses fixed output dimensions (1080×1920 portrait, 1920×1080 landscape, or 1080×1080 square), shot timing, camera orbit/turntable/push/pull/rise/hero moves, captions, transitions and frame-rate metadata. The GLB is loaded before the timeline is exposed, using top-level await so the render page load waits for model parsing.

See [Phase 8 exporter documentation](PHASE8_HYPERFRAMES_EXPORTER.md).

### Phase 8 boundaries

- This creates a HyperFrames-ready HTML composition; it does not itself execute the render or guarantee an MP4.
- The output is a single HTML file with embedded GLB bytes. Use self-contained GLB files; external-resource GLTF packages are not bundled.
- Three.js and GSAP load from jsDelivr at render time.
- The composition must still pass the HyperFrames check and a real CI render before it is considered production-verified.
- Voice, music and sound effects are not yet included.


## Phase 9 — HFX Production Intelligence

The experimental `production-intelligence.html` is a phone-first, rule-based creative producer. It turns a product and campaign brief into a story arc, timed cinematic shot list, continuity rules, asset inventory and render-readiness checklist. It exports the exact version 1 `hfx-shot-plan.json` schema consumed by Phase 7 and a standalone Markdown production brief.

The director adapts its story beats to campaign objective and duration, and applies physical-truth guardrails: actual orbit/turntable recommendations require a supplied GLB; a photo-only sequence uses safe framing moves and treats each real view as a separate shot. The preflight highlights missing imagery, insufficient view coverage, missing logo/end card, oversized GLB input, missing CTA and claims requiring official verification.

See [Phase 9 documentation](PHASE9_PRODUCTION_INTELLIGENCE.md).

### Phase 9 boundaries

- This is a deterministic planning assistant, not an LLM or image/video generator.
- Selected assets are inventoried in-browser but not embedded into the shot plan or uploaded.
- It does not independently inspect image contents, confirm the correct product angle or verify product specifications.
- Its readiness score is a simple checklist indicator, not a guarantee of advert quality or approval.
- Export the HFX JSON to Phase 7, then use Phase 8 with the same GLB to prepare the HyperFrames HTML composition.
- It does not create the final MP4 and does not yet add voiceover, music or sound effects.


## Phase 10 — HFX Audio Production Studio

The experimental `audio-studio.html` adds a phone-first multitrack audio editor for voiceover, music and sound effects. Import local audio files, set timeline offsets and trim points, adjust clip gain and fades, optionally duck music beneath voiceover, preview the full mix, and export a stereo 16-bit PCM WAV master at 44.1 or 48 kHz. It also exports an editable `hfx-audio-cues.json` file with the mix decisions.

See [Phase 10 Audio Studio documentation](PHASE10_AUDIO_STUDIO.md).

### Phase 10 boundaries

- Audio decoding, mixing and WAV export run locally in the browser using Web Audio APIs; no paid service or upload is required.
- The cue sheet does not contain the audio bytes. Keep the original files; re-import them when rebuilding a project.
- The current Phase 8 HTML composition remains visual-only. Phase 10 produces the audio master separately; a later render/mux phase must combine the WAV with the rendered video into MP4.
- Browser codec support and mobile memory limits vary. Android device testing and a completed audiovisual MP4 render remain outstanding.


## Phase 11 — Automated Render & Quality Control

The GitHub Actions render workflow now runs a post-render delivery step through `tools/package-render.mjs`. It validates the rendered MP4, optionally muxes a supplied Phase 10 WAV master as AAC, checks the final media streams and duration, writes JSON/Markdown QC reports, and creates a ZIP package.

To include audio, place the Phase 10 WAV master at `project/audio/audio-master.wav` before triggering the workflow. Without it, the pipeline explicitly packages a video-only file and reports that audio is missing.

See [Phase 11 Render & QC documentation](PHASE11_RENDER_QC.md).

This is technical file validation, not automated visual judgement. Human review of realism, continuity, product accuracy and image quality remains necessary. GitHub Actions execution and a real downloadable artifact must be confirmed before calling a production render verified.
