# Phase 16 — Real GLB Inspection & Validation

- Phone-friendly browser utility to load a self-contained GLB locally.
- Three.js preview with orbit/zoom, auto-frame and reset camera.
- Reports actual mesh count, triangle count, material count, unique material texture maps, animation clips, bounding dimensions and file size.
- Exports an inspection JSON file for project handoff.
- File is not uploaded; loading stays in the browser.

## Galaxy S26 Ultra model supplied for testing

The uploaded ZIP was structurally inspected. It contains a GLB 2.0 file (5,773,756 bytes; archive entry `source/Untitled.glb`) with 35 meshes, 35 nodes, 32 materials, 26 texture references, 11 embedded image entries and 0 animation clips. Its GLB header length matches the actual file length. Textures are embedded in the GLB, making it a suitable single-file test input for the Phase 6 and Phase 8 loaders.


This is a technical file check only. Visual inspection in the browser is still needed to verify model accuracy, orientation, Cobalt Violet, camera islands, screen, proportions and side details. The model is not yet committed to the repository; the user-provided ZIP is the test asset in this conversation.


## Limitations

- Technical metadata is not a product authenticity score.
- GLB under the Phase 8 exporter 100 MB limit is recommended.
- Browser WebGL and network access to Three.js are required.
- Mobile memory/GPU capability varies; no Android device test is claimed.
