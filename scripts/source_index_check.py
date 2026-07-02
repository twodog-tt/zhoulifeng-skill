#!/usr/bin/env python3
"""Validate references/source-index.csv."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


EXPECTED_FIELDS = [
    "id",
    "title",
    "platform",
    "type",
    "date",
    "url_or_locator",
    "primary_or_secondary",
    "reliability",
    "notes",
    "local_path",
]

ALLOWED_RELIABILITY = {"A", "B", "C", "D"}
ALLOWED_PRIMARY = {"primary", "secondary"}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    csv_path = root / "references" / "source-index.csv"

    if not csv_path.exists():
        print(f"FAIL: missing {csv_path}")
        return 1

    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_FIELDS:
            print("FAIL: unexpected CSV fields")
            print(f"expected: {EXPECTED_FIELDS}")
            print(f"actual:   {reader.fieldnames}")
            return 1

        errors: list[str] = []
        seen_ids: set[str] = set()
        row_count = 0

        for line_no, row in enumerate(reader, start=2):
            row_count += 1
            source_id = (row.get("id") or "").strip()
            if not source_id:
                errors.append(f"line {line_no}: empty id")
            elif source_id in seen_ids:
                errors.append(f"line {line_no}: duplicate id {source_id}")
            else:
                seen_ids.add(source_id)

            reliability = (row.get("reliability") or "").strip()
            if reliability not in ALLOWED_RELIABILITY:
                errors.append(
                    f"line {line_no}: invalid reliability {reliability!r}; "
                    f"expected one of {sorted(ALLOWED_RELIABILITY)}"
                )

            primary = (row.get("primary_or_secondary") or "").strip()
            if primary not in ALLOWED_PRIMARY:
                errors.append(
                    f"line {line_no}: invalid primary_or_secondary {primary!r}; "
                    f"expected one of {sorted(ALLOWED_PRIMARY)}"
                )

            for field in ("title", "platform", "type", "url_or_locator", "notes"):
                if not (row.get(field) or "").strip():
                    errors.append(f"line {line_no}: empty {field}")

        if row_count == 0:
            errors.append("source-index.csv has no source rows")

    if errors:
        print("FAIL: source index validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: source index has {row_count} source rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
