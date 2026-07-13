#!/usr/bin/env python3
"""Flag formulaic or evaluation-leaking Zhou Lifeng style outputs.

This is a regression lint, not a semantic fidelity scorer. It can inspect plain
text, answer-agent artifacts, or public demo files.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


LEAKAGE_MARKERS = {
    "models_used",
    "evidence_notes",
    "candidate_model_notes",
    "lowbrow_notes",
    "这是候选视角，不是验证结论",
}

FORMULA_MARKERS = {
    "说白了",
    "荒诞",
    "体面",
    "账本",
    "流量",
    "脸面",
    "抽水",
    "工资条",
    "卷帘门",
    "灯箱",
    "临时文件",
}

FORMULA_PATTERNS = {
    "you_think_but": re.compile(r"你以为.{0,30}(?:其实|实际上)"),
    "mouth_body": re.compile(r"嘴上.{0,30}身体"),
    "front_back": re.compile(r".{0,20}(?:台前|前台).{0,40}(?:后台|后厨)"),
}

ANSWER_LINE = re.compile(r"(?:^|\n)\s*(?:-\s*)?(?:answer|sample output):\s*(.+)")


def extract_answers(text: str) -> list[str]:
    answers = [match.strip() for match in ANSWER_LINE.findall(text)]
    if answers:
        return answers
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    return paragraphs or [text.strip()]


def check_answers(answers: list[str]) -> list[str]:
    errors: list[str] = []
    corpus_counts: Counter[str] = Counter()

    for index, answer in enumerate(answers, start=1):
        leaks = sorted(marker for marker in LEAKAGE_MARKERS if marker in answer)
        if leaks:
            errors.append(f"answer {index}: internal evaluation leakage: {', '.join(leaks)}")

        markers = sorted(marker for marker in FORMULA_MARKERS if marker in answer)
        for marker in markers:
            corpus_counts[marker] += 1
        if len(markers) >= 4:
            errors.append(
                f"answer {index}: formula marker saturation ({len(markers)}): "
                + ", ".join(markers)
            )

        matched_patterns = [
            name for name, pattern in FORMULA_PATTERNS.items() if pattern.search(answer)
        ]
        if len(matched_patterns) >= 2:
            errors.append(
                f"answer {index}: repeated rhetorical templates: "
                + ", ".join(matched_patterns)
            )

    if len(answers) >= 5:
        threshold = max(3, (len(answers) + 2) // 3)
        for marker, count in corpus_counts.most_common():
            if count >= threshold:
                errors.append(
                    f"corpus: marker {marker!r} appears in {count}/{len(answers)} answers"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()

    failed = False
    for path in args.paths:
        if not path.exists():
            print(f"FAIL: missing {path}")
            failed = True
            continue

        answers = extract_answers(path.read_text(encoding="utf-8"))
        errors = check_answers(answers)
        if errors:
            failed = True
            print(f"FAIL: {path} ({len(answers)} answer blocks)")
            for error in errors:
                print(f"- {error}")
        else:
            print(f"PASS: {path} ({len(answers)} answer blocks)")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
