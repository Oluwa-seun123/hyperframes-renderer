# Phase 10 — HFX Audio Production Studio

## Purpose
A phone-first, browser-based multitrack audio editor for preparing the audio master for a HyperFrames advert. It uses the browser's Web Audio API and does not call paid APIs or upload source audio.

## Open
Open `audio-studio.html` in a modern browser. Add voiceover, music and sound-effect files from the device.

## Workflow
1. Set the project duration (20–90 seconds) and WAV sample rate (44.1 or 48 kHz).
2. Add one or more voice, music and SFX clips.
3. Set each clip's timeline start, trim-in, trim-out, gain, fade-in and fade-out.
4. Choose optional music ducking under voiceover.
5. Preview the rendered mix and export a stereo PCM WAV master.
6. Export the HFX audio cue sheet JSON to preserve the edit decisions.

## Audio cue contract
The JSON uses `format: "hfx-audio-cues"`, version 1, project name, duration, sample rate, ducking amount and a track list. Each track stores kind, source filename, source duration, timeline offset, trim range, gain and fades. Audio bytes are not embedded; retain the original source files and reselect them when rebuilding a project.

## Implementation
- Decodes selected local audio using `AudioContext.decodeAudioData`.
- Renders the complete mix with `OfflineAudioContext`.
- Exports 16-bit stereo PCM WAV at the selected sample rate.
- Applies per-clip gain and fade envelopes.
- Music ducking reduces music gain during voiceover cue intervals.
- No audio is uploaded to a server by the editor.

## Boundaries
- This phase creates a real WAV master and editable cue sheet; it does not generate voice, music or sound effects.
- Browser support depends on the device's audio decoder and OfflineAudioContext implementation. Large or long mixes can exceed mobile memory limits.
- The current Phase 8 HyperFrames HTML exporter is visual-only. The WAV must be combined with the rendered video in a later MP4 muxing phase. Phase 10 does not claim to produce a final audiovisual MP4.
- Cue-sheet import restores project settings only; the original source audio files must be reselected and re-added.
- No Android device test or complete video-plus-audio MP4 render has been completed.
