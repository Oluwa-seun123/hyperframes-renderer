# HFX 3D Product Engine — Phase 6

## Open the studio

Open `image-motion-studio/3d-engine.html` from the `feature/image-motion-studio` branch. It is a browser-based, mobile-responsive GLB/GLTF viewer and product-shot preview tool.

## Load a product

- Prefer a self-contained `.glb` file on a phone. A `.gltf` file may reference external texture and buffer files; those dependencies must also be available to the loader.
- The selected file is loaded locally in the browser using Three.js GLTFLoader and an object URL.
- The engine normalizes the model's bounding box and frames it in the camera.
- It does not upload the model to our own server.

## Camera and product motion

- Drag to orbit manually; pinch/scroll to zoom using OrbitControls.
- Start camera orbit to animate the virtual camera around the real model.
- Start turntable to rotate the model around its vertical axis while the camera remains fixed.
- Set horizontal, elevated or low orbit path.
- Adjust camera distance and height, or use the object rotation slider.

These are genuine 3D transforms of the loaded model, not motion fabricated from a still photograph.

## Studio lighting and materials

The scene uses a hemisphere light, directional key, rim and fill lights, a dark studio floor/grid, ACES filmic tone mapping and sRGB output. Key/rim/fill intensities and background can be adjusted. Metalness and roughness controls apply offsets to compatible glTF material values; selecting Original restores the source material values.

This is a basic real-time studio rig, not a full physically calibrated product-rendering pipeline. No HDR environment map, ray-traced reflections, path tracing or true depth-of-field renderer is included yet.

## Capture and shot cues

- Save PNG captures the current viewport frame.
- Record WebM uses browser MediaRecorder and canvas captureStream at 30 fps. Browser support and phone performance vary. The file is WebM preview footage, not the final HyperFrames MP4.
- Shot cues store a duration, movement type and label, and can be copied as a direction sheet. They are not yet automatically translated into a HyperFrames 3D render timeline.

## Requirements and limitations

- Requires internet access to load Three.js modules from jsDelivr.
- Requires a modern browser with WebGL. WebM recording requires MediaRecorder support.
- Large or high-polygon models may exceed Android memory/GPU limits. Use optimized GLB files and keep texture sizes reasonable.
- A GLB/GLTF file is necessary for physically truthful orbit and rotation. This tool does not create a 3D model from the supplied Galaxy reference images.
- No model or video-generation credits are used. This phase does not use a paid AI API.
- Inline module JavaScript syntax has been checked; real Android browser, device-memory, model-loading and capture tests remain outstanding.
