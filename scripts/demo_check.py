#!/usr/bin/env python3
"""Validate public demo coverage."""

from __future__ import annotations

import re
from pathlib import Path


def validate_demo(root: Path) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    demo_path = root / "examples" / "public-demo.md"
    counts = {
        "level_1": 0,
        "level_2": 0,
        "level_3": 0,
        "safety_boundary": 0,
    }

    if not demo_path.exists():
        return [f"missing {demo_path}"], counts

    text = demo_path.read_text(encoding="utf-8")
    lower = text.lower()

    required_phrases = [
        "## public demo set",
        "expected behavior",
        "why this is safe",
        "what not to do",
    ]
    for phrase in required_phrases:
        if phrase not in lower:
            errors.append(f"missing phrase {phrase!r}")

    counts["level_1"] = len(re.findall(r"^### Level 1 Demo", text, flags=re.MULTILINE))
    counts["level_2"] = len(re.findall(r"^### Level 2 Demo", text, flags=re.MULTILINE))
    counts["level_3"] = len(re.findall(r"^### Level 3 Demo", text, flags=re.MULTILINE))
    counts["safety_boundary"] = len(re.findall(r"^### Safety-boundary Demo", text, flags=re.MULTILINE))

    minimums = {
        "level_1": 5,
        "level_2": 5,
        "level_3": 3,
        "safety_boundary": 5,
    }
    for key, expected in minimums.items():
        if counts[key] < expected:
            errors.append(f"expected at least {expected} {key} demos, got {counts[key]}")

    total_demos = sum(counts.values())
    expected_behavior_count = lower.count("expected behavior")
    what_not_count = lower.count("what not to do")
    why_safe_count = lower.count("why this is safe")
    if expected_behavior_count < total_demos:
        errors.append(f"expected behavior appears {expected_behavior_count} times for {total_demos} demos")
    if what_not_count < total_demos:
        errors.append(f"what not to do appears {what_not_count} times for {total_demos} demos")
    if why_safe_count < total_demos:
        errors.append(f"why this is safe appears {why_safe_count} times for {total_demos} demos")

    return errors, counts


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors, counts = validate_demo(root)

    if errors:
        print("FAIL: demo validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "OK: public demos "
        f"level_1={counts['level_1']} "
        f"level_2={counts['level_2']} "
        f"level_3={counts['level_3']} "
        f"safety_boundary={counts['safety_boundary']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
