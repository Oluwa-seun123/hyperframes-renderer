# THE NIGHT HAS NO LIMITS
**Samsung Galaxy S26 Ultra Cobalt Violet — 30-second vertical spec advertisement**

- Master: 1080 × 1920, 9:16, 30 fps, 30 seconds
- Structure: six scenes, exactly five seconds each
- Creative direction: premium cinematic photorealism
- Audio: no voiceover; original cinematic score and designed effects planned as a separate pass
- Subjects: no humans

## Current build status
The first render is a procedural motion-design / greybox pass built from original HTML, CSS and SVG. It validates timing, typography, scene order and the render workflow. It is not the photoreal final commercial and the generic Scene 06 phone placeholder is not an accurate Galaxy S26 Ultra depiction.

The photoreal upgrade is now specified in:
- `assets/PHOTOREAL-PRODUCTION-BRIEF.md` — scene-by-scene visual direction, generation guidance, transitions, audio and approval gates.
- `assets/photoreal-assets.json` — machine-readable asset manifest for all six scenes and official product-reference requirements.
- `assets/ASSET-REGISTER.md` — provenance and usage-rights register.

## Official product accuracy
Use Samsung's official Galaxy S26 Ultra Cobalt Violet imagery as a visual reference for accuracy. Important rights gate: Samsung Mobile Press's published Terms of Use restrict its materials to personal, informational and non-commercial use and prohibit modification, derivative works and other exploitation without authorization. Do not composite, alter or publish those press assets or logo artwork in the advert unless Samsung grants written permission for that specific use. Until then, keep them reference-only and hold the final branded hero shot or obtain a separately licensed product asset. Do not generate the phone or Samsung logo with an image model. Preserve the exact silhouette, camera island, lenses, frame, colour and proportions. The optical assembly in Scene 04 is conceptual, not a teardown or verified internal diagram. Do not add unapproved performance claims.

Reference sources:
- Samsung Mobile Press media library: https://www.samsungmobilepress.com/media-assets/galaxy-s26-ultra?category=Product
- Samsung product page: https://www.samsung.com/us/smartphones/galaxy-s26-ultra/

Written permission is required before use of Samsung Mobile Press assets in the advert; the site terms do not grant advertising/compositing rights. This is an independent speculative concept, not affiliated with, sponsored by or endorsed by Samsung.

## Asset workflow
1. Obtain the official Cobalt Violet product views and logo artwork; record provenance and usage permissions.
2. Create six distinct scene plates using the production brief. AI-created environments must not contain text, logos or an invented phone.
3. Prefer 2160 × 3840 source plates and 5–7 second motion plates; minimum final-use plate size is 1080 × 1920.
4. Review still frames first, then animate and approve a low-resolution assembly.
5. Composite the official phone into Scene 06, add the separately typeset brand/end-card elements and original audio.
6. Run both asset-manifest and MP4 validation before calling the project final.

Run the manifest preflight (missing assets are reported as expected until supplied):
```bash
npm run validate:assets
```

## Render from GitHub
The workflow `.github/workflows/galaxy-s26-night-limits.yml` runs on pushes to this branch when this project or workflow changes, and can also be started manually from GitHub Actions. It runs the asset-manifest preflight, HyperFrames check, snapshots, MP4 render, technical validation and ZIP packaging.

The workflow uses GitHub-hosted CPU runners and free/open-source project dependencies. GitHub Actions usage is subject to the account's included minutes and storage limits; it is not an unlimited free GPU service. No paid AI generation API is called.

## Local commands
From this folder with Node.js 22+, Python 3 and FFmpeg installed:
```bash
npm run validate:assets
npm run check
npm run snapshot
npm run render
python3 scripts/validate_render.py renders/<rendered-file>.mp4
```
