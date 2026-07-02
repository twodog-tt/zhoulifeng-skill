#!/usr/bin/env python3
"""Clean txt/srt/vtt transcript files without rewriting meaning."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TIMESTAMP_RE = re.compile(
    r"^\s*(?:\d{1,2}:)?\d{1,2}:\d{2}[,.]\d{1,3}\s*-->\s*"
    r"(?:\d{1,2}:)?\d{1,2}:\d{2}[,.]\d{1,3}.*$"
)
INLINE_TIMESTAMP_RE = re.compile(r"<\d{2}:\d{2}:\d{2}\.\d{3}>")
TAG_RE = re.compile(r"<[^>]+>")


def normalize_line(raw_line: str) -> str:
    line = raw_line.strip()
    line = INLINE_TIMESTAMP_RE.sub("", line)
    line = TAG_RE.sub("", line)
    return line.strip()


def clean_transcript(text: str) -> str:
    cleaned: list[str] = []
    previous_content = ""
    previous_blank = False

    for raw_line in text.splitlines():
        stripped = raw_line.strip()

        if not stripped:
            if cleaned and not previous_blank:
                cleaned.append("")
            previous_blank = True
            continue

        if stripped.upper() == "WEBVTT":
            continue
        if stripped.startswith("NOTE"):
            continue
        if stripped.isdigit():
            continue
        if TIMESTAMP_RE.match(stripped):
            continue

        line = normalize_line(stripped)
        if not line:
            continue

        if line == previous_content:
            continue

        cleaned.append(line)
        previous_content = line
        previous_blank = False

    while cleaned and cleaned[-1] == "":
        cleaned.pop()

    return "\n".join(cleaned) + ("\n" if cleaned else "")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Clean txt/srt/vtt transcripts by removing timestamps, duplicate blank lines, and consecutive duplicate captions."
    )
    parser.add_argument("input", help="Input .txt, .srt, or .vtt transcript")
    parser.add_argument(
        "output",
        nargs="?",
        help="Output .txt path. Defaults to stdout when omitted.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"FAIL: input file not found: {input_path}", file=sys.stderr)
        return 1

    text = input_path.read_text(encoding="utf-8-sig")
    output = clean_transcript(text)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
