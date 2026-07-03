#!/usr/bin/env python3
"""Validate v1.0 planning and release-candidate documentation."""

from __future__ import annotations

from pathlib import Path


REQUIRED_FILES = [
    "docs/V1_PLAN.md",
    "docs/V1_RELEASE_CRITERIA.md",
    "docs/V1_GAP_ANALYSIS.md",
    "docs/V1_CHECKLIST.md",
    "docs/V1_TASKS.md",
    "docs/V1_READINESS.md",
    "docs/STABLE_PACKAGE.md",
    "reviews/pre-v1.0-audit.md",
    "references/research/11-pre-v1-model-and-source-audit.md",
]

REQUIRED_PHRASES = [
    "candidate models remain candidate",
    "hard safety boundaries",
    "not a real-time official statement generator",
    "X `@zlf86` remains unverified",
    "public proof status",
]


def validate_v1_plan(root: Path) -> list[str]:
    errors: list[str] = []
    combined_parts: list[str] = []

    for rel_path in REQUIRED_FILES:
        path = root / rel_path
        if not path.exists():
            errors.append(f"missing {rel_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"empty {rel_path}")
            continue
        combined_parts.append(text)

    combined = "\n".join(combined_parts)
    lower = combined.lower()
    for phrase in REQUIRED_PHRASES:
        if phrase.lower() not in lower:
            errors.append(f"v1 planning docs missing required phrase {phrase!r}")

    changelog = root / "CHANGELOG.md"
    if not changelog.exists():
        errors.append("missing CHANGELOG.md")
    elif "## [1.0.0] - planning" not in changelog.read_text(encoding="utf-8"):
        errors.append("CHANGELOG.md missing [1.0.0] - planning")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_v1_plan(root)
    if errors:
        print("FAIL: v1.0 planning validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: v1.0 planning docs are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
