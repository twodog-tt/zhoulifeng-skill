#!/usr/bin/env python3
"""Create a public release archive for the Skill repository."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path


VERSION_RE = re.compile(r"^v\d+\.\d+\.\d+(?:-rc\.\d+)?$")

REQUIRED_FILES = [
    "SKILL.md",
    "AUTHORIZATION.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "references/source-index.csv",
]

REQUIRED_DIRS = [
    "agents",
    "docs",
    "examples",
    "launch",
    "references/evidence",
    "references/research",
    "references/source-verification",
    "reviews",
    "tests",
    "scripts",
]

EXCLUDED_PARTS = {
    ".git",
    ".DS_Store",
    "dist",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
}

SENSITIVE_MARKERS = [
    ".env",
    "api_key",
    "api-key",
    "apikey",
    "credential",
    "credentials",
    "local-only",
    "long-subtitle",
    "long_subtitle",
    "private-auth",
    "private-authorization",
    "private_authorization",
    "private-chat",
    "private_chats",
    "private-material",
    "private_material",
    "private-photo",
    "private_photo",
    "raw-transcript",
    "raw_transcript",
    "raw-subtitle",
    "raw_subtitle",
    "secret",
    "token",
    "private-path",
    "private_path",
    "unauthorized-reference-photo",
    "unauthorized_reference_photo",
]


def is_excluded(path: Path) -> bool:
    parts = set(path.parts)
    if parts & EXCLUDED_PARTS:
        return True
    lowered = str(path).lower()
    return any(marker in lowered for marker in SENSITIVE_MARKERS)


def iter_archive_files(root: Path) -> list[Path]:
    files: list[Path] = []

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            raise FileNotFoundError(f"required file missing: {relative}")
        files.append(path)

    for relative in REQUIRED_DIRS:
        directory = root / relative
        if not directory.is_dir():
            raise FileNotFoundError(f"required directory missing: {relative}")
        for path in sorted(directory.rglob("*")):
            if path.is_file() and not is_excluded(path.relative_to(root)):
                files.append(path)

    return sorted(set(files), key=lambda item: item.relative_to(root).as_posix())


def create_archive(root: Path, version: str, output: Path | None = None) -> Path:
    if not VERSION_RE.match(version):
        raise ValueError("version must look like vX.Y.Z or vX.Y.Z-rc.N")

    archive_path = output or root / "dist" / f"zhoulifeng-skill-{version}.zip"
    archive_path.parent.mkdir(parents=True, exist_ok=True)

    files = iter_archive_files(root)
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            relative = path.relative_to(root)
            archive.write(path, relative.as_posix())

    return archive_path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--version",
        required=True,
        help="release version, for example v1.0.0 or v1.0.0-rc.1",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="optional archive path; defaults to dist/zhoulifeng-skill-vX.Y.Z.zip",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root = Path(__file__).resolve().parents[1]

    try:
        archive_path = create_archive(root, args.version, args.output)
    except (FileNotFoundError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1

    print(f"PASS: created {archive_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
