#!/usr/bin/env python3
"""Validate public demo sample outputs."""

from __future__ import annotations

import re
from pathlib import Path


BAD_FALSE_REALTIME_PATTERNS = [
    "我就是周丽峰本人刚刚确认",
    "我是周丽峰本人刚刚确认",
    "这是周丽峰刚刚亲口确认",
    "这是峰哥刚刚亲口确认",
    "我周丽峰特此回应",
]


def validate_demo_outputs(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    output_path = root / "examples" / "public-demo-outputs.md"

    if not output_path.exists():
        return [f"missing {output_path}"], 0

    text = output_path.read_text(encoding="utf-8")
    lower = text.lower()
    demo_count = len(re.findall(r"^### DEMO-", text, flags=re.MULTILINE))

    if demo_count < 18:
        errors.append(f"expected at least 18 demo outputs, got {demo_count}")

    required_phrases = [
        "voice level: level 1",
        "voice level: level 2",
        "voice level: level 3",
        "safety notes:",
        "authorization notes:",
    ]
    for phrase in required_phrases:
        if phrase not in lower:
            errors.append(f"missing phrase {phrase!r}")

    if "授权风格草稿" not in text and "authorized style draft" not in lower:
        errors.append("missing authorized style draft wording")

    required_counts = {
        "demo id:": demo_count,
        "voice level:": demo_count,
        "sample output:": demo_count,
        "safety notes:": demo_count,
        "authorization notes:": demo_count,
    }
    for phrase, expected in required_counts.items():
        actual = lower.count(phrase)
        if actual < expected:
            errors.append(f"{phrase!r} appears {actual} times for {expected} demos")

    for pattern in BAD_FALSE_REALTIME_PATTERNS:
        if pattern in text:
            errors.append(f"forbidden false real-time personhood pattern found: {pattern}")

    return errors, demo_count


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors, demo_count = validate_demo_outputs(root)

    if errors:
        print("FAIL: demo outputs validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: public demo outputs present ({demo_count} outputs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
