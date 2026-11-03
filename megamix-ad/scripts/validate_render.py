#!/usr/bin/env python3
import json, subprocess, sys
raw=subprocess.check_output(["ffprobe","-v","error","-show_entries","stream=codec_type,width,height,r_frame_rate","-show_entries","format=duration","-of","json",sys.argv[1]],text=True)
data=json.loads(raw)
video=next(s for s in data["streams"] if s["codec_type"]=="video")
duration=float(data["format"]["duration"])
assert (video["width"],video["height"])==(1080,1920), video
assert video["r_frame_rate"]=="30/1", video
assert 58 <= duration <= 62, duration
print("Validated",round(duration,2),"seconds at 1080x1920 / 30fps")
