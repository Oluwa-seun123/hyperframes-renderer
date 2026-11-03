# Three-tool production workflow

This repository integrates three independent upstream projects through explicit file handoffs. It does not vendor their code or claim to host their inference runtimes.

## 1. OpenMontage — creative direction and scene assets

Upstream: https://github.com/calesthio/OpenMontage (AGPL-3.0; see upstream licence).

OpenMontage is an agent-driven production environment, not a browser widget or hosted API. Its documented setup requires Python, FFmpeg, Node.js, an AI coding assistant and a local project environment. Optional providers may require API keys; zero-key workflows use local/free sources but still consume local compute and may have capability limits.

Use it to build the campaign brief, script and timed scene plan; source footage and create original visual assets where supported; review and approve each scene; then export approved media and a manifest. Do not export unreviewed drafts as final scenes.

The export contract is the assets array described in HANDOFF.md. Each clip/image needs a unique ID, scene ID, kind, role, source path, source tool and licence/provenance note.

## 2. VoiceStudio — narration

Upstream: https://github.com/debpalash/VoiceStudio (AGPL-3.0; see upstream licence).

VoiceStudio is a separate application with desktop, Android and other supported builds. On Android, install from upstream release/F-Droid instructions, download a suitable model, generate narration and export a WAV file. Model downloads use device storage and compute; offline generation is possible after model installation, but speed and model compatibility depend on the phone.

Export WAV, preferably mono PCM at 44.1 kHz or 48 kHz. Keep the approved script, speaker/model identity, model licence and voice-consent note with the export. Do not clone another person's voice without permission. Do not upload private voice recordings or keys into a public repository.

Register narration in the handoff manifest as kind audio and role voiceover, with a unique ID and relative source path.

## 3. HyperFrames — composition and delivery

HyperFrames is the renderer in this repository. It consumes HTML/CSS/GSAP scenes and local assets, then renders the MP4 in the GitHub Actions workflow.

The importer copies approved files into the project assets/aso-imported folder and writes aso-import-manifest.json. This is an asset handoff, not an automatic scene editor: the composition must explicitly reference approved imported paths. Do not assume an imported clip is automatically placed on the timeline.

Before render, confirm distinct approved sources unless the storyboard deliberately calls for a reprise; confirm owner-supplied product packshots and logo; check licences; run importer tests and creative QA; run HyperFrames check, snapshot, render and FFprobe validation; then inspect the actual snapshots and full video. Technical validation alone is not creative approval.

## Handoff sequence

1. OpenMontage exports a reviewed scene plan and approved visuals.
2. VoiceStudio exports approved narration WAV.
3. Put exports in one folder and create aso-handoff.json using HANDOFF.md.
4. Run import_production.py locally to copy and hash-check the media.
5. Map approved imported paths into the HyperFrames composition and run quality gates.
6. Render, inspect, revise and only then publish.

## Cost and execution boundaries

The integration code and GitHub Actions workflow use free/open-source components. GitHub-hosted runners provide temporary CPU execution, not a persistent GPU workstation. Open-source software does not make inference, storage, mobile data or hosted compute unlimited. No paid API should be called implicitly; any provider requiring payment must be explicitly enabled by the project owner.

Do not create new accounts or rotate accounts to evade provider quotas. When a free limit is reached, use a genuinely free/local workflow, wait for quota reset, or choose a different licensed source.

## Current implementation status

- Implemented: file manifest importer, SHA-256 provenance record, duplicate-video rejection, importer unit tests, basic repeated-source creative gate, HyperFrames render workflow.
- Documented: OpenMontage and VoiceStudio export responsibilities and constraints.
- Not implemented yet: automatic OpenMontage agent execution, automatic VoiceStudio remote control, automatic timeline authoring from imported assets, background removal, full creative review automation.
- Not verified yet: end-to-end production with real OpenMontage exports, VoiceStudio narration and a reviewed HyperFrames render.