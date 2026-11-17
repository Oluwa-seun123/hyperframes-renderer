#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

video = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if not video or not video.is_file() or video.stat().st_size == 0:
    raise SystemExit("Usage: python3 scripts/validate_render.py <rendered.mp4>")

cmd = [
    "ffprobe", "-v", "error",
    "-show_entries", "stream=codec_type,codec_name,width,height,r_frame_rate",
    "-show_entries", "format=duration,size",
    "-of", "json", str(video)
]
data = json.loads(subprocess.check_output(cmd, text=True))
streams = [s for s in data.get("streams", []) if s.get("codec_type") == "video"]
if not streams:
    raise SystemExit("FAIL: no video stream found")
stream = streams[0]
duration = float(data.get("format", {}).get("duration", 0))
fps = stream.get("r_frame_rate", "")
checks = {
    "H.264 video": stream.get("codec_name") == "h264",
    "1080x1920": stream.get("width") == 1080 and stream.get("height") == 1920,
    "30 fps": fps in ("30/1", "30000/1001"),
    "30-second runtime": abs(duration - 30.0) <= 0.6,
}
for label, ok in checks.items():
    print(f'{"PASS" if ok else "FAIL"}: {label}')
if not all(checks.values()):
    raise SystemExit(1)
print(f"Validated {video} ({duration:.3f}s, {stream['width']}x{stream['height']}, {fps})")
