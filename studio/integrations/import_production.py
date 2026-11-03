import argparse
import hashlib
import json
import shutil
from pathlib import Path

EXTENSIONS = {
    "video": {".mp4", ".mov", ".webm"},
    "image": {".png", ".jpg", ".jpeg", ".webp"},
    "audio": {".wav", ".mp3", ".m4a", ".flac", ".ogg"},
}
ROLES = {"scene", "voiceover", "music", "sfx", "product", "logo", "reference"}

def file_hash(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--allow-duplicate-video", action="store_true")
    args = parser.parse_args()
    source = args.source_root.resolve()
    project = args.project_root.resolve()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    assets = manifest.get("assets")
    if not isinstance(assets, list) or not assets:
        parser.error("manifest must contain a non-empty assets list")
    seen_ids, seen_videos, plan = set(), {}, []
    for item in assets:
        asset_id = item.get("id")
        kind, role = item.get("kind"), item.get("role")
        if not asset_id or asset_id in seen_ids:
            parser.error("asset IDs must be present and unique")
        seen_ids.add(asset_id)
        if kind not in EXTENSIONS or role not in ROLES:
            parser.error(f"{asset_id}: unsupported kind or role")
        if role == "voiceover" and kind != "audio":
            parser.error(f"{asset_id}: voiceover must be audio")
        rel = Path(item.get("source", ""))
        if rel.is_absolute() or ".." in rel.parts:
            parser.error(f"{asset_id}: unsafe relative source path")
        path = (source / rel).resolve()
        if source not in path.parents or not path.is_file():
            parser.error(f"{asset_id}: source file missing or outside source root")
        if path.suffix.lower() not in EXTENSIONS[kind]:
            parser.error(f"{asset_id}: file extension does not match kind")
        digest = file_hash(path)
        if kind == "video" and digest in seen_videos and not args.allow_duplicate_video:
            parser.error(f"{asset_id}: duplicate video matches {seen_videos[digest]}")
        if kind == "video":
            seen_videos[digest] = asset_id
        plan.append((item, path, digest))
    target = project / "assets" / "aso-imported"
    target.mkdir(parents=True, exist_ok=True)
    imported = []
    for item, path, digest in plan:
        scene = "".join(c if c.isalnum() or c in "-_" else "-" for c in str(item.get("scene_id") or item["id"]))
        dest = target / f"{scene[:48]}-{path.name}"
        if dest.exists() and file_hash(dest) != digest:
            parser.error(f"refusing to overwrite different file: {dest}")
        if not dest.exists():
            shutil.copy2(path, dest)
        imported.append({
            "id": item["id"], "kind": item["kind"], "role": item["role"],
            "scene_id": item.get("scene_id"), "file": dest.relative_to(project).as_posix(),
            "sha256": digest, "source_tool": item.get("source_tool", "unspecified"),
            "license": item.get("license", "UNSPECIFIED"), "notes": item.get("notes", "")
        })
    result = {"project": manifest.get("project", project.name), "assets": imported}
    (target / "aso-import-manifest.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {len(imported)} assets into {target}")
    print("Duplicate-video check passed.")

if __name__ == "__main__":
    main()
