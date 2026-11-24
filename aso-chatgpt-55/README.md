# ChatGPT — More Than a Conversation

55-second vertical motion-graphics advert based on the supplied eight-panel storyboard.

- Canvas: 1080 × 1920 (9:16)
- Target duration: 55 seconds
- Frame rate: HyperFrames renderer default
- Composition: HTML/CSS + seekable GSAP root timeline
- Supplied ChatGPT logo retained as a source asset

## Build

```bash
npm run check
npx hyperframes snapshot --at 2,8,13,17,23,32,41,49
npm run render
```

The GitHub Actions workflow runs the check, captures review frames, renders the MP4 and uploads the render artifact.
