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

No paid video-generation API is used.
