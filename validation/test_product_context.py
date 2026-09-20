"""Exercise handoff failures that could propagate a wrong product or unreviewed image."""
import copy
import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("context_check", ROOT / "plugins/machinebot-ecommerce-studio/skills/machinebot-ecommerce-studio/scripts/validate_context.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "source.bin").write_bytes(b"source")
        (self.root / "asset.bin").write_bytes(b"asset")
        sh = hashlib.sha256(b"source").hexdigest()
        ah = hashlib.sha256(b"asset").hexdigest()
        self.data = {"schema_version": 1, "product": {"id": "p", "name": "P", "variant": "blue", "mode": "real"},
                     "identity": {"locked": ["blue"], "unseen": []}, "sources": [{"id": "s", "path": "source.bin", "sha256": sh}],
                     "facts": [{"id": "f", "text": "blue", "basis": "observed", "source_ids": ["s"]}],
                     "assets": [{"id": "a", "path": "asset.bin", "sha256": ah, "source_ids": ["s"], "source_hashes": {"s": sh},
                                 "variant": "blue", "kind": "cutout", "status": "pass", "review": {"viewed": True, "note": "checked", "reviewer": "test", "sha256": ah}}],
                     "plans": [{"id": "p", "status": "approved", "approval_evidence": "test only", "slots": [{"id": "c1", "kind": "cutout", "asset_id": "a"}]}]}

    def tearDown(self):
        self.temp.cleanup()

    def test_valid(self):
        self.assertEqual([], MOD.validate(self.data, self.root))

    def test_failure_boundaries(self):
        mutations = [
            lambda d: d.update(schema_version=2),
            lambda d: d["assets"][0].update(variant="red"),
            lambda d: d["assets"][0].update(status="failed"),
            lambda d: d["assets"][0]["review"].update(viewed=False),
            lambda d: d["assets"][0]["review"].update(sha256="0" * 64),
            lambda d: d["assets"][0]["source_hashes"].update(s="0" * 64),
            lambda d: d["facts"][0].update(source_ids=["missing"]),
            lambda d: d["facts"][0].update(basis="synthetic-spec"),
            lambda d: d["plans"][0].update(approval_evidence=""),
            lambda d: d["plans"][0]["slots"].append({"id": "c2", "kind": "cutout", "asset_id": "a"}),
            lambda d: d["assets"][0].update(path="../outside.bin"),
        ]
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index):
                changed = copy.deepcopy(self.data)
                mutate(changed)
                self.assertTrue(MOD.validate(changed, self.root))

    def test_changed_and_missing_files(self):
        (self.root / "source.bin").write_bytes(b"changed source")
        self.assertTrue(MOD.validate(self.data, self.root))
        (self.root / "source.bin").unlink()
        self.assertTrue(MOD.validate(self.data, self.root))


if __name__ == "__main__":
    unittest.main()
