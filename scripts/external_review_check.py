#!/usr/bin/env python3
"""Validate external reviewer feedback scaffolding."""

from __future__ import annotations

import csv
import re
from pathlib import Path


REQUIRED_FILES = [
    "reviews/external/README.md",
    "reviews/external/reviewer-invite.md",
    "reviews/external/feedback-form.md",
    "reviews/external/feedback-log.csv",
    "reviews/external/reports/v0.8-external-review-report.md",
]

FEEDBACK_FIELDS = [
    "id",
    "date_or_unknown",
    "reviewer_type",
    "scope",
    "voice_fidelity_score",
    "lowbrow_score",
    "safety_score",
    "usability_score",
    "evidence_score",
    "decision",
    "summary",
    "action_required",
    "status",
]

ALLOWED_DECISIONS = {"pass", "concern", "hold"}


def validate_external_review(root: Path) -> list[str]:
    errors: list[str] = []

    for rel_path in REQUIRED_FILES:
        path = root / rel_path
        if not path.exists():
            errors.append(f"missing {rel_path}")
            continue
        if not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty {rel_path}")

    log_path = root / "reviews" / "external" / "feedback-log.csv"
    if log_path.exists():
        with log_path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != FEEDBACK_FIELDS:
                errors.append(f"feedback-log.csv fields mismatch: {reader.fieldnames}")
            else:
                for line_number, row in enumerate(reader, start=2):
                    if not row.get("id", "").strip():
                        errors.append(f"feedback-log.csv line {line_number}: missing id")
                    decision = row.get("decision", "").strip()
                    if decision and decision not in ALLOWED_DECISIONS:
                        errors.append(
                            f"feedback-log.csv line {line_number}: invalid decision {decision!r}"
                        )
                    for score_field in [
                        "voice_fidelity_score",
                        "lowbrow_score",
                        "safety_score",
                        "usability_score",
                        "evidence_score",
                    ]:
                        value = row.get(score_field, "").strip()
                        if value and value not in {"1", "2", "3", "4", "5"}:
                            errors.append(
                                f"feedback-log.csv line {line_number}: invalid {score_field} {value!r}"
                            )

    report_path = root / "reviews" / "external" / "reports" / "v0.8-external-review-report.md"
    if report_path.exists():
        report = report_path.read_text(encoding="utf-8")
        status_match = re.search(r"^Status:\s*(.+)$", report, flags=re.MULTILINE | re.IGNORECASE)
        status = status_match.group(1).strip().lower() if status_match else ""
        if not status:
            errors.append("v0.8 external review report missing Status")
        if status == "completed" and "reviewer decision" not in report.lower():
            errors.append("completed external review report must include reviewer decision")
        if status == "completed" and "not completed" in report.lower():
            errors.append("external review report has contradictory completion wording")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_external_review(root)
    if errors:
        print("FAIL: external review validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: external review scaffolding is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
