# Phase 10 audio hand-off

Export your stereo WAV master from `image-motion-studio/audio-studio.html` and upload it into this folder as `audio-master.wav`. The Phase 11 GitHub Actions workflow will mux it into the rendered MP4. Keep the original source audio and cue-sheet JSON with your project backup; the WAV master is the file consumed by the workflow.

If no `audio-master.wav` is present, Phase 11 creates a clearly labelled video-only MP4 and reports that the audio master was missing.