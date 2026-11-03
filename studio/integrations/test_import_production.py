import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().with_name("import_production.py")


class ImporterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "exports"
        self.project = self.root / "project"
        self.source.mkdir()
        self.project.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def run_import(self, assets, allow_duplicates=False):
        manifest = self.root / "manifest.json"
        manifest.write_text(json.dumps({"project": "test", "assets": assets}), encoding="utf-8")
        command = [
            sys.executable, str(SCRIPT), "--manifest", str(manifest),
            "--source-root", str(self.source), "--project-root", str(self.project),
        ]
        if allow_duplicates:
            command.append("--allow-duplicate-video")
        return subprocess.run(command, text=True, capture_output=True)

    def asset(self, asset_id, source, kind="video", role="scene"):
        return {"id": asset_id, "source": source, "kind": kind, "role": role}

    def test_imports_video_and_writes_hash_manifest(self):
        media = self.source / "scene.mp4"
        media.write_bytes(b"unique video bytes")
        result = self.run_import([self.asset("scene-01", "scene.mp4")])
        self.assertEqual(result.returncode, 0, result.stderr)
        imported = self.project / "assets/aso-imported/aso-import-manifest.json"
        data = json.loads(imported.read_text(encoding="utf-8"))
        self.assertEqual(len(data["assets"]), 1)
        self.assertEqual(data["assets"][0]["sha256"], hashlib.sha256(b"unique video bytes").hexdigest())

    def test_rejects_identical_video_files(self):
        (self.source / "a.mp4").write_bytes(b"same")
        (self.source / "b.mp4").write_bytes(b"same")
        result = self.run_import([
            self.asset("a", "a.mp4"), self.asset("b", "b.mp4")
        ])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate video", result.stderr)

    def test_allows_duplicate_video_only_with_explicit_flag(self):
        (self.source / "a.mp4").write_bytes(b"same")
        (self.source / "b.mp4").write_bytes(b"same")
        result = self.run_import([
            self.asset("a", "a.mp4"), self.asset("b", "b.mp4")
        ], allow_duplicates=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_path_traversal(self):
        outside = self.root / "outside.mp4"
        outside.write_bytes(b"not allowed")
        result = self.run_import([self.asset("escape", "../outside.mp4")])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsafe relative source path", result.stderr)

    def test_rejects_extension_kind_mismatch(self):
        (self.source / "voice.wav").write_bytes(b"audio")
        result = self.run_import([self.asset("bad", "voice.wav", "video")])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("extension does not match kind", result.stderr)

    def test_voiceover_must_be_audio(self):
        (self.source / "scene.mp4").write_bytes(b"video")
        result = self.run_import([self.asset("bad", "scene.mp4", "video", "voiceover")])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("voiceover must be audio", result.stderr)


if __name__ == "__main__":
    unittest.main()
