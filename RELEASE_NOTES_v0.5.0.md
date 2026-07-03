# v0.5.0 - Evidence Depth, Packaging, and Public Demo

## Release Type

Evidence depth, documentation, packaging, and public demo release.

## Summary

This release strengthens the project after the v0.4.0 authorized voice evaluation pass.

v0.5.0 expands timestamped evidence coverage, adds more evidence notes, improves installation and runtime documentation, expands the public demo set, and adds validation scripts for docs and demos.

## What Changed

- Expanded `references/evidence/zlf-evidence-map.csv` to 28 rows.
- Added 8 new evidence notes.
- Added installation documentation.
- Added packaging documentation.
- Added runtime compatibility documentation.
- Expanded public demo set to 18 demos.
- Added `scripts/demo_check.py`.
- Added `scripts/docs_check.py`.
- Added docs/demo checks to quick validation and GitHub Actions.

## Evidence Coverage

The evidence map now covers:

Verified:

- 底层现场主义
- 边缘样本优先
- 内容判断四问

Candidate:

- 荒诞现实解构
- 采访中的弱控制
- 流量红线雷达

Candidate models remain candidate in this release.

## Public Demo Coverage

The public demo set includes:

- 5 Level 1 demos
- 5 Level 2 demos
- 3 Level 3 demos
- 5 safety-boundary demos

## What This Release Does Not Change

- Does not upgrade candidate models to verified.
- Does not weaken hard safety boundaries.
- Does not change the authorization scope.
- Does not make the Skill a real-time official statement generator.
- Does not include private authorization materials, private chats, long transcripts, or private data.

## Validation

The following validation commands pass:

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
python3 scripts/evidence_check.py
python3 scripts/eval_run_check.py
python3 scripts/demo_check.py
python3 scripts/docs_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

## Recommended Next Step

Proceed to v0.6 with:

- broader human reviewer audit
- optional install screenshots
- README badges
- example outputs for each public demo
- optional package/archive workflow
