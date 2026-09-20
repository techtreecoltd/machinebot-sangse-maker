"""Validate the source, build a new immutable release ZIP, then validate its extraction."""
import hashlib
import json
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "plugins/machinebot-ecommerce-studio"


def validate(folder):
    skill_root = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills/.system"
    commands = [[sys.executable, str(skill_root / "skill-creator/scripts/quick_validate.py"), str(p.parent)]
                for p in sorted(folder.glob("skills/*/SKILL.md"))]
    commands.append([sys.executable, str(skill_root / "plugin-creator/scripts/validate_plugin.py"), str(folder)])
    receipts = []
    for command in commands:
        run = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONUTF8": "1"})
        receipts.append({"command": command, "exit_code": run.returncode, "stdout": run.stdout, "stderr": run.stderr})
        if run.returncode:
            raise RuntimeError(json.dumps(receipts, ensure_ascii=False))
    for path in folder.rglob("*.md"):
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8-sig")):
            target = link.split("#")[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not (path.parent / target).exists():
                raise RuntimeError(f"Broken link: {path}: {link}")
    return receipts


def main():
    version = json.loads((SOURCE / ".codex-plugin/plugin.json").read_text(encoding="utf-8-sig"))["version"]
    archive = ROOT / f"dist/machinebot-ecommerce-studio-{version}.zip"
    extraction = ROOT / f"validation/package-check-{version}"
    if archive.exists() or extraction.exists():
        raise RuntimeError("Release/extraction already exists; choose a new version rather than overwrite it")
    for path in [ROOT / "README.md", SOURCE / "README.md", ROOT / "YOUTUBE_RELEASE_GUIDE.md", ROOT / "CHANGELOG.md"]:
        if version not in path.read_text(encoding="utf-8-sig"):
            raise RuntimeError(f"Version missing: {path}")
    receipts = validate(SOURCE)
    files = sorted(p for p in SOURCE.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc")
    with zipfile.ZipFile(archive, "x", zipfile.ZIP_DEFLATED) as z:
        for path in files:
            z.write(path, (Path(SOURCE.name) / path.relative_to(SOURCE)).as_posix())
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:
            raise RuntimeError("ZIP CRC failed")
        z.extractall(extraction)
    extracted = extraction / SOURCE.name
    receipts += validate(extracted)
    for path in files:
        if path.read_bytes() != (extracted / path.relative_to(SOURCE)).read_bytes():
            raise RuntimeError(f"Source/archive mismatch: {path}")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".zip.sha256").write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    report = {"version": version, "archive": archive.relative_to(ROOT).as_posix(), "sha256": digest,
              "file_count": len(files), "skills": len(list(SOURCE.glob("skills/*/SKILL.md"))), "source_extraction_equal": True,
              "checks": receipts}
    (ROOT / f"validation/package-{version}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS {version}: {report['skills']} skills, {len(files)} files, source/extraction validators + links + byte equality + CRC; SHA256 {digest}")


if __name__ == "__main__":
    main()
