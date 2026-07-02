#!/usr/bin/env python3
"""Repo-local skill validator with no third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


MAX_SKILL_NAME_LENGTH = 64


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML frontmatter")

    frontmatter: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []

    for raw_line in match.group(1).splitlines():
        if raw_line.startswith("  ") and current_key:
            current_lines.append(raw_line.strip())
            continue
        if current_key:
            frontmatter[current_key] = "\n".join(current_lines).strip()
            current_key = None
            current_lines = []

        key_match = re.match(r"^([a-zA-Z0-9_-]+):(?:\s*(.*))?$", raw_line)
        if not key_match:
            raise ValueError(f"invalid frontmatter line: {raw_line!r}")
        key, value = key_match.groups()
        if value == "|":
            current_key = key
            current_lines = []
        else:
            frontmatter[key] = (value or "").strip().strip('"')

    if current_key:
        frontmatter[current_key] = "\n".join(current_lines).strip()

    return frontmatter


def validate_skill(skill_dir: Path) -> tuple[bool, str]:
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.exists():
        return False, "SKILL.md not found"

    try:
        frontmatter = parse_frontmatter(skill_path.read_text(encoding="utf-8"))
    except ValueError as exc:
        return False, str(exc)

    allowed_keys = {"name", "description"}
    unexpected = set(frontmatter) - allowed_keys
    if unexpected:
        return False, f"unexpected frontmatter keys: {sorted(unexpected)}"

    name = frontmatter.get("name", "").strip()
    description = frontmatter.get("description", "").strip()
    if not name:
        return False, "missing name"
    if not description:
        return False, "missing description"
    if not re.match(r"^[a-z0-9-]+$", name):
        return False, f"name must be hyphen-case: {name}"
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, f"name has invalid hyphen placement: {name}"
    if len(name) > MAX_SKILL_NAME_LENGTH:
        return False, f"name too long: {len(name)} characters"
    if "<" in description or ">" in description:
        return False, "description cannot contain angle brackets"
    if len(description) > 1024:
        return False, f"description too long: {len(description)} characters"

    return True, "Skill is valid!"


def main() -> int:
    skill_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
    valid, message = validate_skill(skill_dir)
    print(message)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
