# Phase 13 — Cinematic Image Stage

## Purpose
A phone-first editor for real product-reference images. It lets the producer import a sequence, configure shot-specific camera-style motion, preview timing, and export a self-contained portable HTML composition with embedded images.

## Features
- Multi-image import from phone or desktop.
- Per-shot title, movement preset, duration, zoom intensity, image fit, fade/cut and contrast toggle.
- Reorder by removing and re-importing in the intended order (timeline drag-reordering is not yet implemented).
- Preview playback, portable HTML export.
- Export keeps source images embedded, not linked to the original file paths.

## Important limits
- Camera motion is simulated with CSS transform over a still image. It is not true camera movement or 3D.
- Depth-style parallax is a restrained 2D scale treatment; no depth map is computed.
- Preview/export is HTML. This page does not render MP4 or mux audio. Use Phase 11 GitHub Actions pipeline for supported final render workflow.
- It does not remove backgrounds or hallucinate missing product views.
- Image files remain client-side in the browser tab/session; no upload service.

## Android use
Open the file in a browser with the source served (GitHub Pages or another static host). GitHub's blob view is not a runnable web app. Select the product image files together, then edit individual shots, preview, and export.
