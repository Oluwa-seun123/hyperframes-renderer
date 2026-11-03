# HunyuanVideo 1.5 feasibility for the $0 HyperFrames workflow

Checked: 2026-11-03

## Decision

HunyuanVideo 1.5 is a strong open-weight candidate for future image-to-video and text-to-video shots, but it is **not currently runnable in this repository's GitHub Actions pipeline** and is not directly runnable on a typical Android phone.

Official upstream: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
Official model card: https://huggingface.co/tencent/HunyuanVideo-1.5
Official license: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE

## Verified capabilities

- 8.3B-parameter video model with text-to-video and image-to-video workflows.
- 480p and 720p model variants; official repository lists multiple distilled variants.
- Official instructions specify an NVIDIA CUDA GPU and a minimum of 14 GB GPU memory with model offloading.
- Official repository documents a 480p image-to-video step-distilled model; it recommends 8 or 12 inference steps and reports testing on an RTX 4090.
- ComfyUI and Diffusers integrations are documented upstream.

## $0 operating constraints

The model weights and inference code are available without a model purchase, but generation still requires GPU compute, storage, and bandwidth. GitHub-hosted runners do not promise a suitable NVIDIA GPU, so do not attempt to download the full checkpoints or claim that Actions can run this model for free.

A hosted community demo or third-party endpoint must be checked independently for current free quota, account requirements, commercial-use rights, output watermarking, retention/privacy, and terms. Do not assume that a public demo or free trial is durable or suitable for commercial advertising.

Creating a separate account for a distinct service is acceptable when the provider's terms permit it. Do not create accounts to evade quotas, rate limits, bans, or eligibility rules; do not use disposable-account rotation or false identities.

## License review before commercial use

The Tencent Hunyuan Community License is royalty-free within its defined Territory, but it is not an unrestricted permissive license. The official license excludes the European Union, United Kingdom, and South Korea from the Territory and includes additional terms and acceptable-use restrictions. Nigeria is not listed among those excluded territories, but the complete license and applicable law still need review before production use. The license says Tencent claims no rights in generated Outputs; users remain responsible for their use.

## Recommended role in our advert workflow

If a legitimate hosted option offers sufficient free compute, use HunyuanVideo 1.5 primarily for short supporting image-to-video shots (fruit, yoghurt pour, creamy texture, lifestyle scenes). Keep actual Megamix bottles, tubs, logo, and label text as original supplied images composited in HyperFrames. Never ask the model to redraw packaging or invent product claims.

Until a verified $0 hosted GPU route is available, use rights-cleared live-action footage and the original product packshots. HyperFrames remains the final compositor.

## Do not mark as production-ready yet

No Hunyuan model weights are installed, no inference environment is provisioned, no hosted provider has been approved, and no Hunyuan clip has been generated or tested in this repository.
