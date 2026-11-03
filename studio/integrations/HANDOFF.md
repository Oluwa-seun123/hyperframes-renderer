# Using the media handoff

OpenMontage exports approved video/image scenes. VoiceStudio exports narration audio. Keep each export in a folder and create a JSON file with an `assets` array.

Each asset needs:
- `id`: unique identifier
- `source`: path relative to the source folder
- `kind`: `video`, `image`, or `audio`
- `role`: `scene`, `voiceover`, `music`, `sfx`, `product`, `logo`, or `reference`
- optional `scene_id`, `source_tool`, `license`, and `notes`

Run from the repository root:

```sh
python3 studio/integrations/import_production.py --manifest exports/aso-handoff.json --source-root exports --project-root megamix-ad
```

The importer copies approved files to `<project>/assets/aso-imported/` and writes `aso-import-manifest.json`. It checks file paths, extensions, IDs and SHA-256 hashes. Identical video files are rejected unless `--allow-duplicate-video` is explicitly supplied.

This is a file handoff, not automatic execution of either upstream application. VoiceStudio inference still needs a supported local/remote machine and downloaded models. OpenMontage's agent workflow runs in its supported agent environment. The Studio's GitHub runner is not a persistent GPU host.
