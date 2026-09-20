"""Exercise package completion gates without generating assets."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "plugins/machinebot-ecommerce-studio/skills/machinebot-ecommerce-studio/scripts/validate_package.py"


class PackageGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "source.bin").write_bytes(b"source")
        sh = hashlib.sha256(b"source").hexdigest()
        self.data = {
            "product": {"variant": "blue"},
            "sources": [{"id": "s", "sha256": sh}],
            "assets": [],
            "plans": [{"id": "pkg", "status": "approved", "scope": {"tier": "lite"},
                       "slots": []}],
        }
        counts = {"cutout": 1, "thumbnail": 6, "lifestyle": 4, "benefit": 3, "detail": 6}
        for kind, count in counts.items():
            for index in range(count):
                aid = f"{kind}-{index + 1}"
                path = f"{aid}.bin"
                payload = aid.encode()
                (self.root / path).write_bytes(payload)
                ah = hashlib.sha256(payload).hexdigest()
                self.data["assets"].append({
                    "id": aid, "kind": kind, "path": path, "sha256": ah,
                    "source_ids": ["s"], "source_hashes": {"s": sh}, "variant": "blue",
                    "status": "pass", "review": {"viewed": True, "sha256": ah},
                })
                self.data["plans"][0]["slots"].append({"id": f"slot-{aid}", "kind": kind, "asset_id": aid})

    def tearDown(self):
        self.temp.cleanup()

    def run_check(self, data):
        context = self.root / "context.json"
        context.write_text(json.dumps(data), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(context), "--plan-id", "pkg"],
            capture_output=True, text=True, check=False,
        )

    def add_asset(self, data, kind, index):
        aid = f"{kind}-{index}"
        path = f"{aid}.bin"
        payload = aid.encode()
        (self.root / path).write_bytes(payload)
        ah = hashlib.sha256(payload).hexdigest()
        data["assets"].append({
            "id": aid, "kind": kind, "path": path, "sha256": ah,
            "source_ids": ["s"], "source_hashes": {"s": data["sources"][0]["sha256"]},
            "variant": "blue", "status": "pass", "review": {"viewed": True, "sha256": ah},
        })
        data["plans"][0]["slots"].append({"id": f"slot-{aid}", "kind": kind, "asset_id": aid})

    def test_approved_pass_asset_is_eligible(self):
        result = self.run_check(self.data)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_proposed_plan_and_failed_asset_are_blocked(self):
        changed = copy.deepcopy(self.data)
        changed["plans"][0]["status"] = "proposed"
        changed["assets"][0]["status"] = "failed"
        result = self.run_check(changed)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("plan is not approved", result.stdout)
        self.assertIn("asset not pass", result.stdout)

    def test_same_asset_file_cannot_fill_two_slots(self):
        changed = copy.deepcopy(self.data)
        changed["assets"][1]["path"] = changed["assets"][0]["path"]
        result = self.run_check(changed)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("duplicate asset file in slots", result.stdout)

    def test_unknown_tier_is_blocked(self):
        changed = copy.deepcopy(self.data)
        changed["plans"][0]["scope"]["tier"] = "custom"
        result = self.run_check(changed)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("unsupported package tier", result.stdout)

    def test_lite_cutout_upper_bound_is_two(self):
        changed = copy.deepcopy(self.data)
        self.add_asset(changed, "cutout", 2)
        result = self.run_check(changed)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

        self.add_asset(changed, "cutout", 3)
        result = self.run_check(changed)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("quantity outside full range: cutout=3", result.stdout)

    def test_full_ranges_are_enforced_and_satisfied(self):
        changed = copy.deepcopy(self.data)
        changed["plans"][0]["scope"]["tier"] = "full"
        self.add_asset(changed, "cutout", 2)
        self.add_asset(changed, "lifestyle", 5)
        self.add_asset(changed, "lifestyle", 6)
        self.add_asset(changed, "detail", 7)
        self.add_asset(changed, "detail", 8)
        result = self.run_check(changed)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
