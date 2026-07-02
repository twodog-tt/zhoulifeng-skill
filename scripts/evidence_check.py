#!/usr/bin/env python3
"""Validate references/evidence/zlf-evidence-map.csv."""

from __future__ import annotations

import csv
from pathlib import Path


EXPECTED_FIELDS = [
    "source_id",
    "title",
    "model_ref",
    "evidence_type",
    "timestamp_or_section",
    "summary",
    "confidence",
    "notes",
]

ALLOWED_EVIDENCE_TYPES = {"supporting", "counterexample", "boundary", "unclear"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}


def load_source_ids(root: Path) -> set[str]:
    source_path = root / "references" / "source-index.csv"
    with source_path.open("r", encoding="utf-8-sig", newline="") as handle:
        return {row["id"].strip() for row in csv.DictReader(handle) if row.get("id", "").strip()}


def validate_evidence(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    evidence_path = root / "references" / "evidence" / "zlf-evidence-map.csv"

    if not evidence_path.exists():
        return [f"missing {evidence_path}"], 0

    source_ids = load_source_ids(root)
    row_count = 0

    with evidence_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_FIELDS:
            errors.append(f"unexpected fields: expected {EXPECTED_FIELDS}, got {reader.fieldnames}")
            return errors, 0

        for line_no, row in enumerate(reader, start=2):
            row_count += 1
            source_id = (row.get("source_id") or "").strip()
            if source_id not in source_ids:
                errors.append(f"line {line_no}: unknown source_id {source_id!r}")

            evidence_type = (row.get("evidence_type") or "").strip()
            if evidence_type not in ALLOWED_EVIDENCE_TYPES:
                errors.append(f"line {line_no}: invalid evidence_type {evidence_type!r}")

            confidence = (row.get("confidence") or "").strip()
            if confidence not in ALLOWED_CONFIDENCE:
                errors.append(f"line {line_no}: invalid confidence {confidence!r}")

            for field in EXPECTED_FIELDS:
                if not (row.get(field) or "").strip():
                    errors.append(f"line {line_no}: empty {field}")

    if row_count < 5:
        errors.append(f"expected at least 5 evidence rows, got {row_count}")

    return errors, row_count


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors, row_count = validate_evidence(root)

    if errors:
        print("FAIL: evidence validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: evidence map has {row_count} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
