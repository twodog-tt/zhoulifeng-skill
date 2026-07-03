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


def validate_evidence_map(skill_dir: Path) -> tuple[bool, str]:
    scripts_dir = skill_dir / "scripts"
    sys.path.insert(0, str(scripts_dir))
    try:
        from evidence_check import validate_evidence
    except Exception as exc:  # pragma: no cover - defensive CLI guard
        return False, f"could not import evidence_check: {exc}"

    errors, row_count = validate_evidence(skill_dir)
    if errors:
        return False, "evidence map invalid: " + "; ".join(errors)
    return True, f"Evidence map is valid with {row_count} rows."


def validate_eval_runs(skill_dir: Path) -> tuple[bool, str]:
    scripts_dir = skill_dir / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    try:
        from eval_run_check import validate_eval_runs as run_validator
    except Exception as exc:  # pragma: no cover - defensive CLI guard
        return False, f"could not import eval_run_check: {exc}"

    errors, run_count, row_count = run_validator(skill_dir)
    if errors:
        return False, "eval runs invalid: " + "; ".join(errors)
    return True, f"Eval runs are valid with {run_count} run directory and {row_count} case rows."


def validate_demo_set(skill_dir: Path) -> tuple[bool, str]:
    scripts_dir = skill_dir / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    try:
        from demo_check import validate_demo
    except Exception as exc:  # pragma: no cover - defensive CLI guard
        return False, f"could not import demo_check: {exc}"

    errors, counts = validate_demo(skill_dir)
    if errors:
        return False, "demo set invalid: " + "; ".join(errors)
    return (
        True,
        "Demo set is valid with "
        f"{counts['level_1']} Level 1, "
        f"{counts['level_2']} Level 2, "
        f"{counts['level_3']} Level 3, and "
        f"{counts['safety_boundary']} safety-boundary demos.",
    )


def validate_docs_set(skill_dir: Path) -> tuple[bool, str]:
    scripts_dir = skill_dir / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    try:
        from docs_check import validate_docs
    except Exception as exc:  # pragma: no cover - defensive CLI guard
        return False, f"could not import docs_check: {exc}"

    errors = validate_docs(skill_dir)
    if errors:
        return False, "docs invalid: " + "; ".join(errors)
    return True, "Docs are valid."


def validate_review_set(skill_dir: Path) -> tuple[bool, str]:
    scripts_dir = skill_dir / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    try:
        from review_check import validate_reviews
    except Exception as exc:  # pragma: no cover - defensive CLI guard
        return False, f"could not import review_check: {exc}"

    errors = validate_reviews(skill_dir)
    if errors:
        return False, "reviews invalid: " + "; ".join(errors)
    return True, "Review scaffolding is valid."


def validate_demo_outputs_set(skill_dir: Path) -> tuple[bool, str]:
    scripts_dir = skill_dir / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    try:
        from demo_outputs_check import validate_demo_outputs
    except Exception as exc:  # pragma: no cover - defensive CLI guard
        return False, f"could not import demo_outputs_check: {exc}"

    errors, demo_count = validate_demo_outputs(skill_dir)
    if errors:
        return False, "demo outputs invalid: " + "; ".join(errors)
    return True, f"Demo outputs are valid with {demo_count} outputs."


def validate_archive_set(skill_dir: Path) -> tuple[bool, str]:
    scripts_dir = skill_dir / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    try:
        from archive_check import validate_archive_setup
    except Exception as exc:  # pragma: no cover - defensive CLI guard
        return False, f"could not import archive_check: {exc}"

    errors = validate_archive_setup(skill_dir)
    if errors:
        return False, "archive setup invalid: " + "; ".join(errors)
    return True, "Archive setup is valid."


def main() -> int:
    skill_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
    valid, message = validate_skill(skill_dir)
    print(message)
    if not valid:
        return 1

    evidence_valid, evidence_message = validate_evidence_map(skill_dir)
    print(evidence_message)
    if not evidence_valid:
        return 1

    eval_valid, eval_message = validate_eval_runs(skill_dir)
    print(eval_message)
    if not eval_valid:
        return 1

    demo_valid, demo_message = validate_demo_set(skill_dir)
    print(demo_message)
    if not demo_valid:
        return 1

    docs_valid, docs_message = validate_docs_set(skill_dir)
    print(docs_message)
    if not docs_valid:
        return 1

    review_valid, review_message = validate_review_set(skill_dir)
    print(review_message)
    if not review_valid:
        return 1

    outputs_valid, outputs_message = validate_demo_outputs_set(skill_dir)
    print(outputs_message)
    if not outputs_valid:
        return 1

    archive_valid, archive_message = validate_archive_set(skill_dir)
    print(archive_message)
    return 0 if archive_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
