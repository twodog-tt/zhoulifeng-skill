#!/usr/bin/env python3
"""Validate social account source verification status."""

from __future__ import annotations

import csv
from pathlib import Path


FIELDS = [
    "account_id",
    "platform",
    "handle",
    "url",
    "status",
    "verification_basis",
    "used_for",
    "can_enter_verified_models",
    "notes",
]

ALLOWED_STATUS = {"verified", "likely", "unverified", "rejected"}
ALLOWED_USED_FOR = {
    "verified_model_evidence",
    "candidate_voice_calibration",
    "search_lead_only",
    "not_used",
}


def validate_source_verification(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    base = root / "references" / "source-verification"

    required_files = [
        base / "README.md",
        base / "account-verification-checklist.md",
        base / "social-account-status.csv",
        base / "reports" / "v0.8-source-verification-report.md",
    ]
    for path in required_files:
        if not path.exists():
            errors.append(f"missing {path.relative_to(root)}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty {path.relative_to(root)}")

    status_path = base / "social-account-status.csv"
    if not status_path.exists():
        return errors, 0

    with status_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            errors.append(f"social-account-status.csv fields mismatch: {reader.fieldnames}")
            return errors, 0
        rows = list(reader)

    if not rows:
        errors.append("social-account-status.csv must contain at least one account row")

    seen_ids: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        account_id = row.get("account_id", "").strip()
        if not account_id:
            errors.append(f"line {line_number}: missing account_id")
        elif account_id in seen_ids:
            errors.append(f"line {line_number}: duplicate account_id {account_id}")
        seen_ids.add(account_id)

        status = row.get("status", "").strip()
        used_for = row.get("used_for", "").strip()
        can_enter = row.get("can_enter_verified_models", "").strip().lower()

        if status not in ALLOWED_STATUS:
            errors.append(f"{account_id}: invalid status {status!r}")
        if used_for not in ALLOWED_USED_FOR:
            errors.append(f"{account_id}: invalid used_for {used_for!r}")
        if can_enter not in {"yes", "no"}:
            errors.append(f"{account_id}: can_enter_verified_models must be yes/no")
        if status != "verified" and can_enter == "yes":
            errors.append(f"{account_id}: non-verified account cannot enter verified models")
        if used_for == "verified_model_evidence" and status != "verified":
            errors.append(f"{account_id}: verified_model_evidence requires verified status")

    return errors, len(rows)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors, row_count = validate_source_verification(root)
    if errors:
        print("FAIL: source verification validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: source verification has {row_count} account rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
