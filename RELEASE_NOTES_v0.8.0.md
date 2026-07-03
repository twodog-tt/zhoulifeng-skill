# v0.8.0 - Launch Review and Source Verification Workflow

## Release Type

Launch readiness, external review workflow, source verification workflow, and archive packaging release.

## Summary

This release prepares the project for broader public distribution.

v0.8.0 adds launch materials, an external reviewer feedback framework, a source verification workflow for social accounts, and release archive automation.

This release does not claim that external review has already been completed. It prepares the workflow for collecting and recording external review.

## What Changed

### Added

- `launch/` public launch materials:
  - GitHub announcement
  - Chinese X thread draft
  - English X thread draft
  - short post drafts
  - FAQ
- `reviews/external/` external reviewer workflow:
  - reviewer invite
  - feedback form
  - feedback log
  - external review report template
- `references/source-verification/` workflow:
  - account verification checklist
  - social account status registry
  - source verification report template
- release archive automation
- validation scripts:
  - `scripts/external_review_check.py`
  - `scripts/source_verification_check.py`
  - `scripts/launch_materials_check.py`

### Changed

- Expanded README with launch, external review, source verification, and archive pointers.
- Expanded archive workflow documentation.
- Improved packaging safety checks.

## Source Verification Status

The X account `@zlf86` remains marked as:

- status: `unverified`
- used_for: `candidate_voice_calibration`
- can_enter_verified_models: `no`

It must not be used as verified evidence unless independently confirmed in a future release.

## External Review Status

External review framework is prepared.

External review is not yet completed in this release.

No reviewer feedback is fabricated or assumed.

## What This Release Does Not Change

- Does not upgrade candidate models to verified.
- Does not weaken hard safety boundaries.
- Does not change authorization scope.
- Does not make the Skill a real-time official statement generator.
- Does not include private authorization materials.
- Does not include private chats, long transcripts, API keys, tokens, local private paths, or private data.
- Does not verify X `@zlf86`.

## Archive Packaging

The release archive workflow supports:

```bash
python3 scripts/create_release_archive.py --version v0.8.0
```

Generated archives are written to `dist/` and should not be committed to git.

## Validation

The following validation commands pass:

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
python3 scripts/evidence_check.py
python3 scripts/social_speech_check.py
python3 scripts/eval_run_check.py
python3 scripts/demo_check.py
python3 scripts/docs_check.py
python3 scripts/review_check.py
python3 scripts/demo_outputs_check.py
python3 scripts/archive_check.py
python3 scripts/external_review_check.py
python3 scripts/source_verification_check.py
python3 scripts/launch_materials_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

## Recommended Next Step

Proceed to v0.9 with:

- collecting real external reviewer feedback
- updating `reviews/external/feedback-log.csv`
- completing `v0.8-external-review-report.md` or creating a v0.9 review report
- improving launch copy based on reviewer feedback
- optionally adding screenshots and public demo recordings
