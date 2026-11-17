#!/usr/bin/env python3
"""Validate the photoreal asset manifest without requiring assets to exist yet."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "assets" / "photoreal-assets.json"

def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    scenes = data.get("scenes", [])
    if len(scenes) != 6:
        raise SystemExit(f"Expected 6 scene entries, found {len(scenes)}")
    expected_starts = [0, 5, 10, 15, 20, 25]
    missing = []
    for i, scene in enumerate(scenes):
        if scene.get("start") != expected_starts[i] or scene.get("duration") != 5:
            raise SystemExit(f"Invalid timing for {scene.get('id')}: expected {expected_starts[i]}s + 5s")
        for field in ("still", "motion"):
            rel = scene.get(field)
            if not rel:
                raise SystemExit(f"{scene.get('id')} is missing {field} path")
            path = (ROOT / "assets" / rel).resolve()
            if ROOT.resolve() not in path.parents:
                raise SystemExit(f"Asset path escapes project: {rel}")
            if not path.is_file():
                missing.append(rel)
    product = data.get("productReferences", {})
    if not product.get("sourcePage") or not product.get("requiredViews"):
        raise SystemExit("Official product reference source and required views must be declared")
    print(f"Manifest valid: {len(scenes)} scenes, 30 seconds, {data['master']['width']}x{data['master']['height']} @ {data['master']['fps']} fps.")
    if missing:
        print(f"Photoreal assets not supplied yet ({len(missing)} files):")
        for item in missing:
            print(f"  - {item}")
        print("This is an expected pre-production state; add approved files before final render.")
    else:
        print("All declared scene stills and motion plates are present.")
    if product.get("status") != "approved":
        print("Product gate remains OPEN: download official Cobalt Violet references and review usage terms.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
