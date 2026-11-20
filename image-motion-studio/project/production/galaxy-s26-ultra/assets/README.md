# Galaxy S26 Ultra production asset

Place the authentic Samsung GLB supplied for this project at:

`assets/galaxy-s26-ultra.glb`

The expected full repository path is:

`image-motion-studio/project/production/galaxy-s26-ultra/assets/galaxy-s26-ultra.glb`

Keep the GLB's embedded textures inside the GLB (GLB 2.0). The dedicated GitHub Actions workflow validates the binary header, stages the model beside the HyperFrames composition, runs `hyperframes check`, renders the animation frame-by-frame, runs FFmpeg media QC, and packages MP4 + ZIP delivery.

Do not replace the real model with a still image or a CSS phone mock-up. The composition uses Three.js to render and rotate the supplied mesh while GSAP animates the camera, model pose, lights, typography, graphic rings, light sweeps, callouts and transitions.

The model is intentionally not committed in this source change: it is a user-supplied binary asset. The render workflow stops with an explicit missing-asset error until the GLB is uploaded at the path above.
