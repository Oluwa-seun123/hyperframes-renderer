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
