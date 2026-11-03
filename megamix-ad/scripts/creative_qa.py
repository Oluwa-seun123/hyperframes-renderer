#!/usr/bin/env python3
"""Creative-structure checks for the Megamix composition.

These checks do not judge artistic quality. They prevent a known failure mode:
reusing one or two source clips across many scenes and passing the render anyway.
"""
import re
import sys
from collections import Counter
from pathlib import Path

project = Path(__file__).resolve().parents[1]
html_path = project / "index.html"
html = html_path.read_text(encoding="utf-8")
sources = re.findall(r'<video\b[^>]*?\bsrc=["\']([^"\']+)["\']', html, re.I)
if not sources:
    raise SystemExit("Creative QA failed: no video scenes found.")

counts = Counter(sources)
duplicates = {src: count for src, count in counts.items() if count > 1}
if duplicates:
    detail = ", ".join(f"{src} used {count} times" for src, count in sorted(duplicates.items()))
    raise SystemExit("Creative QA failed: repeated footage sources: " + detail)

if len(sources) < 3:
    raise SystemExit(f"Creative QA failed: expected at least 3 distinct video scenes; found {len(sources)}.")

required_packshots = ("megamix-range.jpg", "megamix-greek.jpg", "megamix-logo.jpg")
for filename in required_packshots:
    if filename not in html:
        raise SystemExit(f"Creative QA failed: composition does not reference required brand asset {filename}.")

print(f"Creative structure passed: {len(sources)} distinct video sources; no repeated clip paths.")
print("Brand asset references present. File existence is checked by the render workflow.")
