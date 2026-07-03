# v0.9.0 - External Review Feedback and Launch Copy Polish

## Release Type

External reviewer feedback, launch-copy polish, and public-proof clarity release.

## Summary

This release records the first real external reviewer feedback for the project and addresses the concerns raised before public promotion.

v0.9.0 improves public authorization wording, aligns launch materials, softens evaluation-score framing, adds stronger Level 3 authorized draft samples, and records a reviewer follow-up pass.

This release does not claim that broad external review has been completed.

## What Changed

### Added

- `reviews/external/v0.9-reviewer-packet.md`
- External feedback intake instructions
- First real external feedback record: `EXT-001`
- Reviewer follow-up record: `EXT-001-FUP`
- v0.9 external review report
- Stronger Level 3 authorized draft samples

### Changed

- Clarified public proof status in `AUTHORIZATION.md` and `README.md`
- Clarified that private authorization materials are not included in the repository
- Clarified that public proof is not included at this stage
- Aligned launch version and model-status wording
- Updated launch materials to include v0.7 candidate models
- Softened `100/100` framing as an automated/static evaluation result, not proof of perfect fidelity
- Polished public launch copy to reduce overclaiming

## External Reviewer Feedback

One real external reviewer provided combined content, safety, and open-source documentation feedback.

Initial decision:

- concern
- not a safety hold

Main concerns:

- public authorization proof clarity
- stale launch version/model-status wording
- Level 3 outputs still slightly documentation-like
- `100/100` framing could sound like overclaiming

Fix status:

- addressed

Follow-up decision:

- pass for v0.9.0 release prep
- no public launch blockers found

## What This Release Does Not Claim

- Does not claim broad external review is complete
- Does not claim perfect fidelity
- Does not upgrade candidate models to verified
- Does not verify X `@zlf86`
- Does not make the Skill a real-time official statement generator
- Does not weaken hard safety boundaries
- Does not include private authorization materials

## Model Status

Verified:

- 底层现场主义
- 边缘样本优先
- 内容判断四问

Candidate:

- 荒诞现实解构
- 采访中的弱控制
- 流量红线雷达
- 下三路牵引
- 知识分子外衣 / 俗人落点

Rejected / Unsafe:

- 自嘲式冒险人格 as an activatable persona
- 口头禅人格复刻
- 争议站队与封禁原因脑补
- 粗俗无限制化
- 低俗越界成露骨或人身羞辱

## Source Verification Status

X `@zlf86` remains:

- status: `unverified`
- used_for: `candidate_voice_calibration`
- can_enter_verified_models: `no`

## Safety Boundary Status

Hard safety boundaries remain unchanged.

The Skill still does not allow:

- real-time impersonation
- fabricated private facts
- doxxing or harassment
- privacy exposure
- dangerous travel guidance
- gray-market or illegal guidance
- platform-evasion guidance
- explicit sexual content
- long transcript or subtitle reproduction

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

Proceed to v1.0 planning with:

- broader external reviewer coverage
- optional public proof link if available
- screenshot / demo-run assets
- stable install package
- final pre-1.0 source and candidate-model audit
