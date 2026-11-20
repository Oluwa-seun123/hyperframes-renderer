# HFX Scene Language (HSL)

HFX Scene Language is a small declarative language for authoring deterministic product-ad scenes. It is compiled in the browser by `scene-studio.html` into a self-contained HTML composition with an exposed GSAP timeline.

## Open the studio

Open `scene-studio.html` from the `feature/image-motion-studio` branch. On a phone, upload the individual product images, assign each image the asset key used in the script, compile, preview, and export.

## Example

```hfx
project "Galaxy S26 Ultra"
format portrait
fps 30
background "#050713"
light violet intensity 0.75
title "GALAXY S26 ULTRA" at 0.86
subtitle "PRECISION IN EVERY DETAIL" at 0.92

asset rear
asset left
asset right
asset bottom
asset front
asset camera

shot rear use rear for 5s move push-in strength 0.07 transition crossfade label "SCULPTED FROM EVERY ANGLE"
shot left use left for 3s move drift-right strength 0.035 transition crossfade label "PRECISION ENGINEERING"
shot right use right for 3s move drift-left strength 0.035 transition crossfade label "REFINED FROM EDGE TO EDGE"
shot bottom use bottom for 4s move push-in strength 0.05 transition crossfade label "EVERY DETAIL CONSIDERED"
shot front use front for 5s move reveal-up strength 0.055 transition crossfade label "AN IMMERSIVE VIEW"
shot camera use camera for 4s move macro strength 0.08 transition crossfade label "PRO-LEVEL CAMERA DETAIL"
shot hero use rear for 6s move hero strength 0.025 transition fade label "GALAXY S26 ULTRA"
```

## Grammar

- `project "name"`
- `format portrait|landscape|square`
- `fps 12..60`
- `background "#RRGGBB"`
- `light <mood> intensity 0..1`
- `title "text" at 0..1`
- `subtitle "text" at 0..1`
- `asset <key>`
- `shot <id> use <asset-key> for <seconds>s move <move> strength <0..1> transition <crossfade|fade|cut> label "text"`

Supported camera move presets: `push-in`, `drift-right`, `drift-left`, `reveal-up`, `macro`, `hero`, `rotate`, `hold`.

Lines beginning with `#` are comments. Each referenced asset must be declared and uploaded. The compiler reports line-specific syntax errors and missing assets before export.

## Current capabilities and limits

- The current compiler produces a deterministic 2D multi-view sequence with independent camera motion per shot, crossfades, labels, title and subtitle.
- Image files are embedded in the exported HTML. The exported composition exposes `window.__timelines.main` for timeline seeking.
- The current preview is a browser approximation; the HyperFrames render is the final output.
- This is not a 3D renderer. A sequence of photographs does not become a physically correct orbit, and no unseen product surfaces are fabricated.
- The language is intentionally small and versionable. Future compiler targets can add real GLB/GLTF scenes, lights, materials, camera rigs, audio cues and render settings without forcing users to learn a different workflow.
- No paid generative-video API is used.
