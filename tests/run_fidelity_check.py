#!/usr/bin/env python3
"""Static fidelity and safety checks for zhoulifeng-skill.

This runner intentionally does not call any external LLM API. The .yaml files
are written as JSON-compatible YAML so the Python standard library can parse
them in CI without extra dependencies.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIDELITY_FIELDS = {
    "id",
    "category",
    "prompt",
    "expected_behavior",
    "failure_signs",
    "score_weight",
    "required_model_refs",
    "forbidden_patterns",
}
SAFETY_FIELDS = {
    "id",
    "prompt",
    "expected_refusal_or_redirection",
    "must_not_include",
    "safer_alternative",
}
ALLOWED_CATEGORIES = {
    "style_analysis",
    "topic_selection",
    "social_observation",
    "controversy_boundary",
    "refusal_boundary",
}


def load_cases(path: Path) -> list[dict[str, Any]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON-compatible YAML: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError(f"{path}: expected a list of cases")
    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"{path}: case #{index} is not an object")
    return data


def require_text(case: dict[str, Any], field: str, errors: list[str]) -> None:
    value = case.get(field)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{case.get('id', '<missing id>')}: {field} must be non-empty text")


def require_list(case: dict[str, Any], field: str, errors: list[str]) -> None:
    value = case.get(field)
    if not isinstance(value, list) or not value:
        errors.append(f"{case.get('id', '<missing id>')}: {field} must be a non-empty list")
        return
    if not all(isinstance(item, str) and item.strip() for item in value):
        errors.append(f"{case.get('id', '<missing id>')}: {field} must contain only non-empty text")


def validate_fidelity_cases(cases: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    total_weight = 0

    for case in cases:
        missing = FIDELITY_FIELDS - set(case)
        if missing:
            errors.append(f"{case.get('id', '<missing id>')}: missing fields {sorted(missing)}")

        require_text(case, "id", errors)
        require_text(case, "category", errors)
        require_text(case, "prompt", errors)
        require_text(case, "expected_behavior", errors)
        require_text(case, "failure_signs", errors)
        require_list(case, "required_model_refs", errors)
        require_list(case, "forbidden_patterns", errors)

        case_id = case.get("id")
        if isinstance(case_id, str):
            if case_id in seen_ids:
                errors.append(f"{case_id}: duplicate id")
            seen_ids.add(case_id)

        category = case.get("category")
        if category not in ALLOWED_CATEGORIES:
            errors.append(f"{case_id}: invalid category {category!r}")

        weight = case.get("score_weight")
        if not isinstance(weight, int) or weight <= 0:
            errors.append(f"{case_id}: score_weight must be a positive integer")
        else:
            total_weight += weight

    if total_weight != 100:
        errors.append(f"fidelity score_weight total must be 100, got {total_weight}")

    return errors


def validate_safety_cases(cases: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()

    for case in cases:
        missing = SAFETY_FIELDS - set(case)
        if missing:
            errors.append(f"{case.get('id', '<missing id>')}: missing fields {sorted(missing)}")

        require_text(case, "id", errors)
        require_text(case, "prompt", errors)
        require_text(case, "expected_refusal_or_redirection", errors)
        require_text(case, "safer_alternative", errors)
        require_list(case, "must_not_include", errors)

        case_id = case.get("id")
        if isinstance(case_id, str):
            if case_id in seen_ids:
                errors.append(f"{case_id}: duplicate id")
            seen_ids.add(case_id)

    return errors


def validate_skill_md() -> list[str]:
    errors: list[str] = []
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")

    for section in ("## Verified Models", "## Candidate Models", "## Rejected / Unsafe Patterns"):
        if section not in text:
            errors.append(f"SKILL.md missing section: {section}")

    required_terms = [
        "不代表",
        "不冒充",
        "危险行动指南",
        "露骨",
        "二创",
        "视角分析",
        "自然输出协议",
        "反模板",
        "混合原因",
        "普通解释句",
    ]
    for term in required_terms:
        if term not in text:
            errors.append(f"SKILL.md missing required safety/evaluation term: {term}")

    if re.search(r"自嘲式冒险人格\s*\n+status:\s*verified", text):
        errors.append("SKILL.md must not mark 自嘲式冒险人格 as verified")

    if len(text.splitlines()) > 500:
        errors.append("SKILL.md must stay at or below 500 lines")

    return errors


def validate_source_count() -> list[str]:
    csv_path = ROOT / "references" / "source-index.csv"
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        count = sum(1 for _ in csv.DictReader(handle))
    if count < 15:
        return [f"source-index.csv must contain at least 15 sources, got {count}"]
    return []


def main() -> int:
    checks: list[tuple[str, list[str]]] = []

    try:
        fidelity_cases = load_cases(ROOT / "tests" / "fidelity_cases.yaml")
        safety_cases = load_cases(ROOT / "tests" / "safety_cases.yaml")
        checks.append(("fidelity cases", validate_fidelity_cases(fidelity_cases)))
        checks.append(("safety cases", validate_safety_cases(safety_cases)))
    except ValueError as exc:
        checks.append(("case loading", [str(exc)]))

    checks.append(("SKILL.md", validate_skill_md()))
    checks.append(("source index count", validate_source_count()))

    failed = False
    for name, errors in checks:
        if errors:
            failed = True
            print(f"FAIL: {name}")
            for error in errors:
                print(f"- {error}")
        else:
            print(f"PASS: {name}")

    if failed:
        return 1

    print("PASS: fidelity static checks complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
