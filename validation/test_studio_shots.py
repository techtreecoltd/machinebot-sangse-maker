import importlib.util
import tempfile
import unittest
from pathlib import Path

from PIL import Image


SCRIPT = Path(__file__).parents[1] / "plugins" / "machinebot-ecommerce-studio" / "skills" / "machinebot-ecommerce-studio" / "scripts" / "validate_studio_shots.py"
SPEC = importlib.util.spec_from_file_location("validate_studio_shots", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class StudioShotValidationTests(unittest.TestCase):
    def test_opaque_white_studio_shot_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "studio.png"
            Image.new("RGB", (1000, 1000), (250, 250, 250)).save(path)
            self.assertEqual([], MODULE.validate(temp))

    def test_transparent_cutout_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "cutout.png"
            Image.new("RGBA", (1000, 1000), (40, 60, 80, 0)).save(path)
            errors = MODULE.validate(temp)
            self.assertTrue(any("not fully opaque" in error for error in errors))

    def test_non_white_background_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "dark.png"
            Image.new("RGB", (1000, 1000), (80, 80, 80)).save(path)
            errors = MODULE.validate(temp)
            self.assertTrue(any("not white studio background" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
