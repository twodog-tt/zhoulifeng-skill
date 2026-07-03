# v0.6.0 - Public Readiness and Reviewer Coverage

## Release Type

Public readiness, reviewer coverage, demo-output, and packaging safety documentation release.

## Summary

This release improves the project's public usability after the v0.5.0 evidence/docs/demo release.

v0.6.0 adds a human reviewer audit system, public demo sample outputs, README badges, screenshot safety guidance, optional archive workflow documentation, and additional validation scripts.

## What Changed

- Added `reviews/` with human review plan, checklist, and v0.6 review report.
- Added `examples/public-demo-outputs.md` with 18 sample outputs.
- Added README badges and improved public entry points.
- Added `docs/SCREENSHOTS.md`.
- Added `docs/ARCHIVE_WORKFLOW.md`.
- Added `scripts/review_check.py`.
- Added `scripts/demo_outputs_check.py`.
- Added review/demo-output checks to quick validation and GitHub Actions.
- Updated install docs with the v0.6 validation commands.

## Review Result

- Lightweight human review: pass for v0.6.0 release prep
- Release blockers: none found
- Candidate models: remain candidate
- Hard safety boundaries: unchanged
- Authorization scope: unchanged

## Demo Output Coverage

The public demo outputs cover:

- Level 1: 峰哥式视角分析
- Level 2: 授权峰哥式口吻草稿
- Level 3: 授权第一人称草稿
- Safety-boundary demos

Level 3 outputs are framed as authorized style drafts, not real-time personal statements.

## What This Release Does Not Change

- Does not make the Skill a real-time official statement generator.
- Does not upgrade candidate models to verified.
- Does not weaken hard safety boundaries.
- Does not include private authorization materials.
- Does not include private chats, long transcripts, API keys, tokens, or private data.
- Does not allow dangerous, illegal, gray-market, doxxing, harassment, explicit, or platform-evasion content.

## Validation

The following validation commands pass:

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
python3 scripts/evidence_check.py
python3 scripts/eval_run_check.py
python3 scripts/demo_check.py
python3 scripts/docs_check.py
python3 scripts/review_check.py
python3 scripts/demo_outputs_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

## Recommended Next Step

Proceed to v0.7 with:

- optional install screenshots
- example output screenshots
- package/archive automation
- broader external reviewer coverage
- public launch materials for GitHub / X
