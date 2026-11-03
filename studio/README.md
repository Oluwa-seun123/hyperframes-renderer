# Production Studio foundation

Mobile-first control room for the ASO Production Studio. This is intentionally a separate app surface inside the renderer repository so the HyperFrames projects remain intact.

## First integration slice
- Studio dashboard and a creative brief form
- Provider-aware media plan: original images, generated video, licensed stock fallback
- Gemini adapter boundary documented without embedding API keys in browser code
- HyperFrames remains the rendering/export engine

## Gemini support and the $0 requirement
Gemini text models may have a free tier, but Google's current Gemini API pricing page lists image generation models without free-tier API access and its video-generation model as paid-tier only. Therefore this studio must never imply Gemini image/video generation is free. Keep Gemini as an optional provider behind a server-side adapter, with a clear quota/billing gate; default to user-supplied assets and licensed stock until a genuinely free image/video backend is configured.

Official pricing: https://ai.google.dev/gemini-api/docs/pricing

## Security rules
- Never put a Gemini API key in client-side JavaScript, HTML, a public repository, or a checked-in .env file.
- Add generation through a server-side endpoint and environment secret only.
- Do not auto-send prompts or uploaded assets to an external provider without a clear user action.
- Keep provider output and license/provenance metadata with each generated asset.

## Next slices
1. Add server-side API and safe provider configuration.
2. Connect generated assets to the HyperFrames project asset manifest.
3. Add narration provider interface (VoiceStudio/local engines).
4. Add job status and artifact download UI.
