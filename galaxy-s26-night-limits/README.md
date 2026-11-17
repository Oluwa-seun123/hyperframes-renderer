# THE NIGHT HAS NO LIMITS
**Samsung Galaxy S26 Ultra — 30-second vertical spec advertisement**

- Master: 1080 × 1920, 9:16, 30 fps, 30 seconds
- Structure: six scenes, exactly five seconds each
- Audio: silent master by design; no voiceover
- Subjects: no humans
- Visual world: midnight navy, black glass, cool silver, cyan and restrained violet

## Current build status
This branch contains the first HyperFrames composition and a GitHub Actions render workflow. It is an animated motion-design / greybox pass built from original HTML, CSS and SVG elements. It is not yet a photoreal final commercial. It deliberately avoids repeated stock footage.

## Product and brand accuracy gate
The phone in Scene 06 is a neutral composition placeholder. Replace it with an approved, verified Galaxy S26 Ultra product image or 3D model before calling the film final. Use official Samsung logo artwork supplied by Samsung; do not redraw the logo. The storyboard's optical assembly is conceptual, not a teardown or verified internal lens diagram. Do not add camera-performance claims that are not approved.

Official reference starting points:
- Samsung Galaxy S26 Ultra product page: https://www.samsung.com/africa_en/smartphones/galaxy-s26-ultra/
- Samsung Mobile Press media assets: https://www.samsungmobilepress.com/media-assets/galaxy-s26-ultra?category=Product

## Render from GitHub
The workflow `.github/workflows/galaxy-s26-night-limits.yml` runs on pushes to this branch when this project or workflow changes, and can also be started manually from GitHub Actions. It runs HyperFrames check, captures snapshots, renders an MP4, validates its technical properties, and packages a delivery ZIP as a workflow artifact.

The workflow uses GitHub-hosted CPU runners and free/open-source project dependencies. GitHub Actions usage is subject to the account's included minutes and storage limits; it is not an unlimited free GPU service. No paid AI generation API is called.

## Local commands
From this folder with Node.js 22+, Python 3 and FFmpeg installed:
```bash
npm run check
npm run snapshot
npm run render
python3 scripts/validate_render.py renders/<rendered-file>.mp4
```

## Next production steps
1. Review the 12 scene snapshots and the rendered preview.
2. Replace the Scene 06 placeholder with verified official product artwork / approved 3D.
3. Add separately approved photographic or generated cinematic assets if the target must be photorealistic; track source and usage rights in `assets/ASSET-REGISTER.md`.
4. Add original score and designed sound effects as a separate approved audio pass; keep the master voiceover-free as specified.
5. Re-render and inspect the entire MP4, including safe areas, transitions, flicker, and final end-card hold.

Independent speculative concept for portfolio / learning. Not affiliated with, sponsored by or endorsed by Samsung.
