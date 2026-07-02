#!/usr/bin/env python3
"""Lightweight quality checks for SKILL.md."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "## 使用声明",
    "## 激活方式",
    "## 回答协议",
    "## 核心观察模型",
    "## 表达 DNA",
    "## 安全边界",
    "## 调研来源",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    skill_path = root / "SKILL.md"

    if not skill_path.exists():
        print(f"FAIL: missing {skill_path}")
        return 1

    text = skill_path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not re.match(r"^---\n.*?\n---\n", text, re.DOTALL):
        errors.append("missing or invalid YAML frontmatter")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing section: {section}")

    frontmatter_match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        if "name:" not in frontmatter:
            errors.append("frontmatter missing name")
        if "description:" not in frontmatter:
            errors.append("frontmatter missing description")

    safety_terms = [
        "冒充",
        "私人信息",
        "危险",
        "露骨",
        "平台",
        "版权",
        "网暴",
    ]
    for term in safety_terms:
        if term not in text:
            errors.append(f"missing safety term: {term}")

    if errors:
        print("FAIL: quality check failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: SKILL.md quality check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
