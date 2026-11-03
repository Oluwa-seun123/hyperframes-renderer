# Product video production pipeline

This folder defines the production workflow for turning a product brief and real product photos into a polished advert.

## Quality-first approach

1. **Plan the advert**: create a timed scene list, claims checklist, shot prompts, and delivery spec.
2. **Generate motion scenes**: use a hosted ComfyUI/Wan image-to-video workflow for cinematic lifestyle, ingredient, texture, and environment shots.
3. **Protect product truth**: keep the supplied logo and packaging as original assets. Prefer generated scenes without readable packaging; composite original packshots and labels in Hyperframes so AI does not redraw brand text.
4. **Assemble**: use Hyperframes for typography, transitions, pacing, brand colours, product packshots, and end card.
5. **Review**: validate duration, resolution, frame rate, missing assets, black frames, and output file before sharing.
6. **Deliver silent master**: voiceover and music are left out unless separately supplied.

## Important cost / access note

The repository can orchestrate rendering, but it cannot provide a free GPU. Comfy Cloud's interactive free allowance is not the same as API automation. Its official API quickstart currently says API workflow execution requires a paid subscription and an API key. Do not add a paid plan or spend credits without the account owner's explicit approval.

Official references:
- Comfy Cloud API quickstart: https://docs.comfy.org/development/api-development/quickstart
- Comfy Cloud API spec: https://github.com/Comfy-Org/docs/blob/main/openapi-cloud.yaml
- Hyperframes: https://hyperframes.dev/

## Current readiness

- Hyperframes render automation has already succeeded for the MÁADÁN test project on the `test/maadan-90s-spec-ad` branch.
- This folder is the production design/specification, not a claim that Wan video generation is already connected.
- A tested Wan 2.2 image-to-video API workflow export and an approved hosted GPU/API account are still required before end-to-end AI clip generation can be called production-ready.
- Never put API keys in this repository. Store them as GitHub Actions secrets only after the owner creates and approves the provider account.

## Asset rules

- Use the exact product images supplied by the owner.
- Never invent ingredients, health benefits, certifications, prices, availability, or claims.
- Do not let AI regenerate logos, label copy, bottle geometry, or package colours for final product shots.
- Generate supporting footage (pour, fruit, milk/yoghurt texture, lifestyle scenes) separately and composite original packshots over it.
- Flag any generated frame that changes a product label or makes a factual claim.

## Recommended 90-second structure

Use 10–14 scenes, mostly 4–8 seconds each, rather than attempting one 90-second AI generation. Keep the first 2 seconds visually strong, show the product early, build sensory/lifestyle interest, then finish with a clean product and brand end card.

See `scene-plan-template.json` for the scene data structure.
