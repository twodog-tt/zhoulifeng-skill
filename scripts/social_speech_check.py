#!/usr/bin/env python3
"""Validate social speech corpus rows."""

from __future__ import annotations

import csv
from pathlib import Path


FIELDS = [
    "id",
    "source_id",
    "platform",
    "date_or_unknown",
    "speech_pattern",
    "excerpt_or_summary",
    "quote_length",
    "risk_level",
    "confidence",
    "notes",
]

ALLOWED_PATTERNS = {
    "rough_colloquial",
    "lowbrow_drift",
    "pseudo_intellectual_pose",
    "anti_sublimation",
    "self_degradation",
    "desire_money_face",
    "traffic_survival",
    "vulgar_but_non_explicit",
    "unsafe_do_not_copy",
    "premise_resistance",
    "qualified_reasoning",
    "plain_explanation",
    "mixed_motives",
    "self_limitation",
    "direct_verification",
}

ALLOWED_RISK_LEVELS = {"safe", "sensitive", "unsafe_do_not_copy"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
MAX_QUOTE_LENGTH = 80


def validate_social_speech(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    path = root / "references" / "evidence" / "social-speech-map.csv"

    if not path.exists():
        return [f"missing {path}"], 0

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            return [f"unexpected fields: expected {FIELDS}, got {reader.fieldnames}"], 0
        rows = list(reader)

    if len(rows) < 15:
        errors.append(f"expected at least 15 social speech rows, got {len(rows)}")

    seen_ids: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        row_id = row.get("id", "").strip()
        if not row_id:
            errors.append(f"line {line_number}: empty id")
        elif row_id in seen_ids:
            errors.append(f"line {line_number}: duplicate id {row_id}")
        seen_ids.add(row_id)

        for field in FIELDS:
            if not row.get(field, "").strip():
                errors.append(f"{row_id or line_number}: empty {field}")

        pattern = row.get("speech_pattern", "").strip()
        if pattern not in ALLOWED_PATTERNS:
            errors.append(f"{row_id}: invalid speech_pattern {pattern!r}")

        risk_level = row.get("risk_level", "").strip()
        if risk_level not in ALLOWED_RISK_LEVELS:
            errors.append(f"{row_id}: invalid risk_level {risk_level!r}")

        confidence = row.get("confidence", "").strip()
        if confidence not in ALLOWED_CONFIDENCE:
            errors.append(f"{row_id}: invalid confidence {confidence!r}")

        quote_length = row.get("quote_length", "").strip()
        if quote_length != "summary":
            try:
                length = int(quote_length)
            except ValueError:
                errors.append(f"{row_id}: quote_length must be 'summary' or an integer")
            else:
                if length < 0 or length > MAX_QUOTE_LENGTH:
                    errors.append(
                        f"{row_id}: quote_length must be 0-{MAX_QUOTE_LENGTH}, got {length}"
                    )

        if risk_level == "unsafe_do_not_copy" and "unsafe" not in pattern:
            errors.append(f"{row_id}: unsafe risk rows should use unsafe_do_not_copy pattern")

    return errors, len(rows)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors, row_count = validate_social_speech(root)
    if errors:
        print("FAIL: social speech map validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: social speech map has {row_count} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
