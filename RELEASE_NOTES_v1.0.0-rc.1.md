# v1.0.0-rc.1 - Pre-1.0 Readiness Candidate

## Release Type

Release candidate.

## Summary

This release candidate prepares `zhoulifeng-skill` for a future v1.0 stable release.

v1.0.0-rc.1 focuses on pre-v1.0 readiness, release criteria, gap analysis, stable archive packaging, model/source audit, and public-readiness checks.

This is not the final v1.0 release.

## Current Readiness Status

- P0 gaps: 0
- P1 gaps: 0
- P2 gaps: 7
- P2 gaps are documented as non-blocking public-assets or release-workflow tasks.
- Recommendation: ready for release-candidate testing / final review before v1.0.

## What Changed Since v0.9.0

- Added v1.0 planning and readiness documentation.
- Added v1.0 release criteria.
- Added v1.0 gap analysis.
- Added v1.0 checklist and task tracking.
- Added pre-v1.0 audit checklist.
- Added pre-v1.0 model and source audit.
- Added stable package documentation.
- Added public assets checklist.
- Resolved P1 release-readiness gaps.
- Confirmed archive generation for `v1.0.0-rc.1`.

## Archive

A local release archive can be generated with:

```bash
python3 scripts/create_release_archive.py --version v1.0.0-rc.1
```

Expected local archive path:

```text
dist/zhoulifeng-skill-v1.0.0-rc.1.zip
```

`dist/` is intentionally ignored and should not be committed.

## Model Status

Verified models:

- 底层现场主义
- 边缘样本优先
- 内容判断四问

Candidate models:

- 荒诞现实解构
- 采访中的弱控制
- 流量红线雷达
- 下三路牵引
- 知识分子外衣 / 俗人落点

Rejected / unsafe patterns:

- 把“自嘲式冒险人格”作为可激活人格
- 口头禅人格复刻
- 争议站队与封禁原因脑补

No candidate models are upgraded by this release candidate.

## Source Verification Status

- X @zlf86 remains unverified.
- X @zlf86 can only be used for candidate voice calibration.
- X @zlf86 does not support verified model upgrades without independent confirmation.

## What This Release Candidate Does Not Claim

- It is not the final v1.0 release.
- It does not claim perfect fidelity.
- It does not claim broad external review completion.
- It does not upgrade candidate models.
- It does not verify X @zlf86.
- It does not weaken hard safety boundaries.
- It does not modify authorization scope.
- It is not a real-time official statement generator.
- It does not add private authorization materials, private chats, raw transcripts, long subtitles, or private personal data.

## Validation

The release-candidate preparation checks pass locally:

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
python3 scripts/v1_plan_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

## Recommended Next Step

Use this release candidate for installation testing, archive inspection, and final public-readiness review before deciding whether to prepare v1.0.0 final.
