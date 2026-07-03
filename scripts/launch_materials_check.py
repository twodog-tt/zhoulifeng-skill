#!/usr/bin/env python3
"""Validate public launch materials."""

from __future__ import annotations

from pathlib import Path


REQUIRED_FILES = [
    "launch/README.md",
    "launch/github-announcement.md",
    "launch/x-thread-cn.md",
    "launch/x-thread-en.md",
    "launch/short-post-cn.md",
    "launch/short-post-en.md",
    "launch/faq.md",
]

REQUIRED_PHRASES = [
    "authorized style skill",
    "not a real-time official statement generator",
    "candidate models remain candidate",
    "hard safety boundaries",
]

FORBIDDEN_PATTERNS = [
    "无边界数字分身",
    "实时本人声明",
    "可做人肉",
    "可以做人肉",
    "可做灰产",
    "可以做灰产",
    "可做危险指南",
    "可以做危险指南",
    "可做露骨内容",
    "可以做露骨内容",
    "boundary-free digital twin",
]


def validate_launch_materials(root: Path) -> list[str]:
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
        if phrase not in lower:
            errors.append(f"launch materials missing required phrase {phrase!r}")

    for pattern in FORBIDDEN_PATTERNS:
        if pattern.lower() in lower:
            errors.append(f"launch materials contain forbidden pattern {pattern!r}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_launch_materials(root)
    if errors:
        print("FAIL: launch materials validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: launch materials are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
