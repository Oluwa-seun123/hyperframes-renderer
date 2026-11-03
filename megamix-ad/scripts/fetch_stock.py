#!/usr/bin/env python3
from pathlib import Path
import csv, re, requests

root = Path(__file__).resolve().parents[1]
assets = root / "assets"
assets.mkdir(exist_ok=True)
sources = [
    ("yoghurt-preparation", "https://mixkit.co/free-stock-video/preparing-yogurt-2685/"),
    ("yoghurt-fruit-bowl", "https://mixkit.co/free-stock-video/preparing-a-bowl-with-yogurt-and-fruit-43925/"),
]
manifest = []
for name, page in sources:
    html = requests.get(page, headers={"User-Agent":"Mozilla/5.0"}, timeout=45)
    html.raise_for_status()
    # Find an MP4 URL embedded in the Mixkit clip page.
    matches = re.findall(r'https?://[^\s"<>]+?\.mp4(?:\?[^\s"<>]*)?', html.text, flags=re.I)
    if not matches:
        raise SystemExit("Mixkit did not expose a direct MP4 for " + page + "; stopping rather than substituting footage.")
    url = matches[0].replace("&amp;", "&")
    target = assets / (name + ".mp4")
    with requests.get(url, headers={"User-Agent":"Mozilla/5.0"}, stream=True, timeout=90) as media:
        media.raise_for_status()
        with target.open("wb") as output:
            for chunk in media.iter_content(1024 * 1024):
                if chunk:
                    output.write(chunk)
    if target.stat().st_size < 100000:
        raise SystemExit("Invalid or incomplete stock file: " + str(target))
    manifest.append([name, page, url, "Mixkit Stock Video Free License; confirm page badge before use"])
with (assets / "licence-manifest.csv").open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["asset", "source_page", "download_url", "licence"])
    writer.writerows(manifest)
print("Downloaded stock footage and wrote the licence manifest.")
