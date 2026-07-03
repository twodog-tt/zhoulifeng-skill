#!/usr/bin/env python3
"""Validate human review audit scaffolding."""

from __future__ import annotations

import re
from pathlib import Path


REQUIRED_FILES = [
    "reviews/README.md",
    "reviews/v0.6-human-review-plan.md",
    "reviews/reviewer-checklist.md",
    "reviews/reports/v0.6-review-report.md",
]


REQUIRED_PHRASES = {
    "reviews/README.md": ["human reviewer", "pending review", "completed"],
    "reviews/v0.6-human-review-plan.md": [
        "authorization boundary",
        "voice fidelity",
        "false real-time personhood",
        "install usability",
    ],
    "reviews/reviewer-checklist.md": [
        "pass / concern / fail",
        "required fix",
        "candidate model",
        "hard boundary",
        "copyright",
    ],
    "reviews/reports/v0.6-review-report.md": [
        "status: prepared, not completed",
        "not completed yet",
        "reviewer decision",
    ],
}


def validate_reviews(root: Path) -> list[str]:
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
        for phrase in REQUIRED_PHRASES.get(rel_path, []):
            if phrase.lower() not in lower:
                errors.append(f"{rel_path}: missing phrase {phrase!r}")

    report_path = root / "reviews" / "reports" / "v0.6-review-report.md"
    if report_path.exists():
        report = report_path.read_text(encoding="utf-8")
        status_match = re.search(r"^Status:\s*(.+)$", report, flags=re.MULTILINE | re.IGNORECASE)
        status = status_match.group(1).strip().lower() if status_match else ""
        if "completed" in status and "not completed" not in status:
            lower = report.lower()
            if "reviewer decision" not in lower or "not yet reviewed" in lower:
                errors.append("review report is marked completed without a reviewer decision")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_reviews(root)

    if errors:
        print("FAIL: review validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: review scaffolding present ({len(REQUIRED_FILES)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
