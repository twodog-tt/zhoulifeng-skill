#!/usr/bin/env python3
"""Validate release archive automation setup."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def validate_archive_setup(root: Path) -> list[str]:
    errors: list[str] = []

    archive_script = root / "scripts" / "create_release_archive.py"
    if not archive_script.is_file():
        errors.append("scripts/create_release_archive.py is missing")

    workflow_doc = root / "docs" / "ARCHIVE_WORKFLOW.md"
    if not workflow_doc.is_file():
        errors.append("docs/ARCHIVE_WORKFLOW.md is missing")

    gitignore = root / ".gitignore"
    if not gitignore.is_file():
        errors.append(".gitignore is missing")
    else:
        gitignore_lines = {
            line.strip()
            for line in gitignore.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        }
        if "dist/" not in gitignore_lines and "dist" not in gitignore_lines:
            errors.append(".gitignore must include dist/")
        if ".DS_Store" not in gitignore_lines:
            errors.append(".gitignore must include .DS_Store")

    try:
        tracked_dist = subprocess.run(
            ["git", "ls-files", "dist"],
            cwd=root,
            check=True,
            text=True,
            capture_output=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        errors.append(f"could not inspect tracked dist files: {exc}")
    else:
        if tracked_dist:
            errors.append("dist/ should not be tracked by git")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_archive_setup(root)
    if errors:
        print("FAIL: archive setup invalid")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: archive setup is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
