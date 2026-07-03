#!/usr/bin/env python3
"""Validate release and install docs presence."""

from __future__ import annotations

from pathlib import Path


REQUIRED_FILES = [
    "docs/INSTALL.md",
    "docs/PACKAGING.md",
    "docs/RUNTIME_COMPATIBILITY.md",
    "AUTHORIZATION.md",
    "RELEASE_NOTES_v0.4.0.md",
]


REQUIRED_TEXT = {
    "docs/INSTALL.md": ["clone", "validation", "runtime"],
    "docs/PACKAGING.md": ["release", "tag", "do not package"],
    "docs/RUNTIME_COMPATIBILITY.md": ["codex", "agents/openai.yaml", "runtime"],
    "AUTHORIZATION.md": ["authorization", "does not automatically allow"],
    "RELEASE_NOTES_v0.4.0.md": ["authorized voice", "candidate models remain candidate"],
}


def validate_docs(root: Path) -> list[str]:
    errors: list[str] = []

    for rel_path in REQUIRED_FILES:
        path = root / rel_path
        if not path.exists():
            errors.append(f"missing {rel_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"empty {rel_path}")
            continue
        lower = text.lower()
        for phrase in REQUIRED_TEXT.get(rel_path, []):
            if phrase.lower() not in lower:
                errors.append(f"{rel_path}: missing phrase {phrase!r}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_docs(root)

    if errors:
        print("FAIL: docs validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: required docs present ({len(REQUIRED_FILES)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
