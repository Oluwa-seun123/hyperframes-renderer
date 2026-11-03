# OpenMontage integration — zero-cost profile

This project uses [OpenMontage](https://github.com/calesthio/OpenMontage) as the production playbook and capability/tool reference, while this repository's HyperFrames renderer remains the final compositor.

## Non-negotiable budget rule

**Default budget: $0.** Do not call, configure, or silently fall back to any paid or credit-consuming provider. In particular, do not use fal.ai, Runway, Kling, Veo, paid Comfy Cloud API execution, or any pay-as-you-go endpoint. Do not add billing details or create provider accounts.

OpenMontage itself is AGPL-3.0 and is maintained upstream. This project references it rather than copying its source; keep upstream notices and license obligations intact if code is ever vendored.

## What can run for free

- Use public-domain or openly licensed footage from Archive.org, NASA, and Wikimedia Commons, checking the individual asset's rights/attribution before commercial use.
- Optionally use Pexels or Pixabay stock footage under their respective terms. API keys are optional and must never be treated as permission to spend.
- Use supplied product photographs as the factual source of truth. Do not regenerate packaging, logo, label text, or product claims.
- Use HyperFrames + FFmpeg on the GitHub Actions runner to compose, animate, validate, and export the finished MP4.
- Use local/offline Piper TTS only when a suitable runtime is available; narration remains optional. The user can add voiceover/music later.

## Honest limitations

A GitHub-hosted runner has no guaranteed free dedicated AI-video GPU. Free/open-source video models such as Wan can be run without model fees **only when suitable GPU hardware is available**; model weights, storage, and compute still have infrastructure costs. Therefore the default cloud workflow must not pretend to generate cinematic AI motion for free. It should use licensed real footage, product photos, and polished motion-graphics composition instead.

OpenMontage is agent-directed: the AI assistant reads its pipeline manifests/skills and invokes its tools. Cloning it in GitHub Actions does not, by itself, create an autonomous agent. The integration should be assistant-led for creative decisions and GitHub Actions-led for repeatable checks/rendering.

## Production sequence

1. Confirm the brief, audience, duration, format, and factual claims.
2. Plan scenes using OpenMontage's pipeline guidance.
3. Source free footage or use the supplied product assets; record source URL and license/attribution for every external clip.
4. Keep product packshots as original overlays in HyperFrames.
5. Render with HyperFrames/FFmpeg.
6. Check dimensions, duration, frame rate, audio, black frames, missing assets, and final file existence.
7. Publish the MP4 as a downloadable build artifact. Never say a render or generation succeeded until the output is verified.

## Upstream

- OpenMontage: https://github.com/calesthio/OpenMontage
- Upstream agent guide: https://github.com/calesthio/OpenMontage/blob/main/AGENT_GUIDE.md
- Provider and cost guide: https://github.com/calesthio/OpenMontage/blob/main/docs/PROVIDERS.md
- License: AGPL-3.0
