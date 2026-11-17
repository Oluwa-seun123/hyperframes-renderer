# Phase 11 — Automated Render & Quality Control

## What it does
The existing GitHub Actions workflow still runs the pinned HyperFrames CLI check and render. Phase 11 adds a post-render packaging step using FFmpeg and ffprobe.

1. Find the newest MP4 generated inside `image-motion-studio/project/` (excluding the output directory).
2. Validate that it contains a video stream and a positive duration.
3. Compare rendered duration with the HTML composition's `data-duration` metadata when present.
4. If a WAV master exists, mux it into the video as AAC at 320 kb/s, preserving the rendered video stream and padding a short audio track to the video duration.
5. If no WAV exists, package the video-only MP4 and mark audio as a warning rather than silently pretending sound was included.
6. Probe the final file again, write JSON and Markdown quality reports, and create a ZIP delivery package.

## Add the Phase 10 audio master
Place the exported WAV at:

`image-motion-studio/project/audio/audio-master.wav`

Commit it to the feature branch before the render workflow runs. The workflow also accepts an alternate path through the `HFX_AUDIO_FILE` environment variable when run in a configured environment.

The WAV is user-supplied; this pipeline does not synthesize narration, music or sound effects.

## Outputs
The workflow packages files in `image-motion-studio/project/output/delivery/`:
- `hfx-final-delivery.mp4` when a WAV is supplied.
- `hfx-final-delivery-video-only.mp4` when no WAV is supplied.
- `quality-report.json` and `quality-report.md`.
- `hfx-final-delivery.zip`, containing the delivered MP4 and both reports.

The GitHub Actions artifact includes the delivery directory and remains available according to the workflow's seven-day retention setting.

## Quality checks and limits
- Confirms MP4 container readability, video stream presence, resolution/codec metadata and positive duration.
- Confirms whether the final MP4 has an audio stream when an audio master was supplied.
- Checks output duration remains aligned with the source render.
- The composition-duration comparison is a warning, not a hard failure, because some renderers may include small timing differences.
- This is technical media QC, not a computer-vision judgement of realism, focus, framing, product correctness, colour, flicker or visual continuity. Human review is still required.
- A successful script syntax check is not proof of a successful real render. CI and actual MP4/ZIP artifact verification remain necessary.
- Android testing remains outstanding. This pipeline runs in GitHub-hosted Actions; no local PC is required to trigger or retrieve the artifact through GitHub.
