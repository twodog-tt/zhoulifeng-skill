#!/usr/bin/env python3
"""Validate v0.4 evaluation run artifacts."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any


REQUIRED_RUN_FILES = [
    "README.md",
    "answer-agent-output.md",
    "scoring-agent-output.md",
    "human-review-notes.md",
    "case-summary.csv",
    "improvement-actions.md",
]

LATEST_RUN_REQUIRED_FILES = [
    "README.md",
    "answer-agent-input-pack.md",
    "answer-agent-output.md",
    "scoring-agent-input-pack.md",
    "scoring-agent-output.md",
    "human-review-notes.md",
    "case-summary.csv",
    "improvement-actions.md",
]

CASE_SUMMARY_FIELDS = [
    "case_id",
    "category",
    "score_weight",
    "answer_status",
    "score",
    "pass_status",
    "safety_failure",
    "impersonation_risk",
    "candidate_verified_confusion",
    "unsupported_claim",
    "notes",
    "action_required",
]


def load_case_ids(path: Path) -> set[str]:
    data: Any = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{path}: expected a list")
    case_ids = {item.get("id") for item in data if isinstance(item, dict)}
    return {case_id for case_id in case_ids if isinstance(case_id, str) and case_id}


def run_sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"run-(\d+)$", path.name)
    if match:
        return int(match.group(1)), path.name
    return -1, path.name


def validate_eval_runs(root: Path) -> tuple[list[str], int, int]:
    errors: list[str] = []
    results_dir = root / "evals" / "results"

    if not results_dir.exists():
        return [f"missing {results_dir}"], 0, 0

    run_dirs = sorted((path for path in results_dir.iterdir() if path.is_dir()), key=run_sort_key)
    if not run_dirs:
        return ["evals/results must contain at least one run directory"], 0, 0

    latest_run_dir = run_dirs[-1]
    current_case_ids = load_case_ids(root / "tests" / "fidelity_cases.yaml")
    current_case_ids |= load_case_ids(root / "tests" / "safety_cases.yaml")

    total_rows = 0
    for run_dir in run_dirs:
        for filename in REQUIRED_RUN_FILES:
            if not (run_dir / filename).exists():
                errors.append(f"{run_dir.name}: missing {filename}")

        if run_dir == latest_run_dir:
            for filename in LATEST_RUN_REQUIRED_FILES:
                if not (run_dir / filename).exists():
                    errors.append(f"{run_dir.name}: latest run missing {filename}")

        summary_path = run_dir / "case-summary.csv"
        if not summary_path.exists():
            continue

        with summary_path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != CASE_SUMMARY_FIELDS:
                errors.append(
                    f"{run_dir.name}: unexpected case-summary fields: "
                    f"expected {CASE_SUMMARY_FIELDS}, got {reader.fieldnames}"
                )
                continue

            rows = list(reader)
            total_rows += len(rows)
            seen_case_ids = {row.get("case_id", "").strip() for row in rows}
            unknown_current_ids = seen_case_ids - current_case_ids
            if unknown_current_ids:
                errors.append(
                    f"{run_dir.name}: case-summary has IDs not found in current tests "
                    f"{sorted(unknown_current_ids)}"
                )

            for line_offset, row in enumerate(rows, start=2):
                case_id = row.get("case_id", "").strip()
                if not case_id:
                    errors.append(f"{run_dir.name}: line {line_offset}: empty case_id")
                if not row.get("answer_status", "").strip():
                    errors.append(f"{run_dir.name}: line {line_offset}: empty answer_status")
                if not row.get("pass_status", "").strip():
                    errors.append(f"{run_dir.name}: line {line_offset}: empty pass_status")

    return errors, len(run_dirs), total_rows


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors, run_count, row_count = validate_eval_runs(root)

    if errors:
        print("FAIL: eval run validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: eval results contain {run_count} run directories and {row_count} case rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
