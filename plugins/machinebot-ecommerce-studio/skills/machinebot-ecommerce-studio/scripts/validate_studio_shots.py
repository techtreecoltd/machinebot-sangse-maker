"""Read-only technical checks for white-background studio product shots."""
import sys
from pathlib import Path

from PIL import Image


def validate(folder):
    root = Path(folder).resolve()
    if not root.is_dir():
        return [f"missing folder: {root}"]
    files = sorted(path for path in root.iterdir() if path.suffix.lower() in {".png", ".jpg", ".jpeg"})
    if not files:
        return ["no studio image files"]

    errors = []
    for path in files:
        try:
            with Image.open(path) as image:
                rgba = image.convert("RGBA")
                width, height = rgba.size
                if width < 1000 or height < 1000:
                    errors.append(f"{path.name}: too small {width}x{height}")
                alpha = rgba.getchannel("A")
                if alpha.getextrema() != (255, 255):
                    errors.append(f"{path.name}: background is not fully opaque")
                pixels = rgba.load()
                corners = [pixels[0, 0], pixels[width - 1, 0], pixels[0, height - 1], pixels[width - 1, height - 1]]
                if any(min(pixel[:3]) < 235 for pixel in corners):
                    errors.append(f"{path.name}: corner is not white studio background")
        except OSError as exc:
            errors.append(f"{path.name}: unreadable image ({exc})")
    return errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: validate_studio_shots.py <folder>")
        sys.exit(2)
    problems = validate(sys.argv[1])
    if problems:
        print("\n".join(f"FAIL: {problem}" for problem in problems))
        sys.exit(1)
    print("PASS: studio images are opaque, high-resolution and white-background compatible; visual identity still requires direct review")
