# HFX Cinematic Director — Phase 5

The Cinematic Director turns choices from the ASO Creative Studio's Cinematic Techniques Reference into structured shot plans and HFX Scene Language output.

## Open

`image-motion-studio/cinematic-director.html`

## Technique coverage

- Push In: a physical camera move toward the subject; still-image export is explicitly a 2D scale/crop approximation.
- Slider Shot: short lateral move (the reference describes roughly 60–120 cm); current still-image export is a pan/parallax approximation.
- Arc / 360-Degree Orbit: camera travel around the subject. Requires real multi-view material or 3D geometry for truthful results.
- Lazy Susan: product rotates while camera distance remains stable. Requires real turntable footage or a model.
- 3D Rotation: virtual turntable around the object; requires GLB/GLTF geometry.
- Rack Focus: focus plane shifts between named distances while composition stays largely fixed. Current export only provides a layered-depth proxy, not optical focus.
- Extreme Close-Up / Insert: detail-first framing; current still workflow can crop supplied source detail.
- Wiggle: tiny viewpoint change; authentic depth requires at least two nearby views.

## Shot specification

Each planned shot records framing, camera technique, lens/focal length, focus behaviour, key-light placement, composition, duration, transition, purpose and continuity guardrails. The export writes these as readable HFX comments and generates the compatible HFX shot skeleton. It flags techniques that cannot be truthfully executed from a single still.

The Cinematic Techniques Reference's governing camera-move rule is applied: specify start framing, direction, speed/duration and the end composition. Zoom is optical; dolly, truck, crane and orbit are physical camera travel with parallax.

## Master Idea Library influence

The Master Idea Library's recurring creative standard is applied as a planning check: real object or task → specific tension → visible choice → satisfying reveal → honest invitation. This is a structural guide, not a copied concept or guarantee of social performance. Any speculative product features must remain clearly labeled as concept work.

## Limits

Phase 5 is a shot-planning and HFX-script authoring tool. It does not itself add a physical camera simulator, optical lens engine, 3D geometry, focus rendering, audio, or final MP4 output. The output remains compatible with the existing multi-view scene workflow; 3D-only moves are explicitly flagged instead of faked.
