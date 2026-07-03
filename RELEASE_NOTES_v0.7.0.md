# v0.7.0 - Lowbrow Voice Calibration

## Release Type

Authorized lowbrow / anti-polish voice calibration release.

## Summary

This release improves the authorized Zhou Lifeng / 峰哥亡命天涯 style Skill by reducing over-polished AI commentary and calibrating the voice toward a rougher, more colloquial, more anti-sublimation style.

v0.7.0 adds a social media speech corpus framework, lowbrow voice calibration research, new candidate models, new fidelity cases, expanded demos, and a completed v0.7 evaluation pass.

## Why This Release Exists

Previous versions were safe and structured, but some outputs still felt too polished, too high-quality, too much like ordinary AI social commentary.

This release addresses that by calibrating toward:

- lower polished-AI tone
- stronger authorized 峰哥式粗粝口语
- 下三路牵引
- 知识分子外衣 / 俗人落点
- anti-sublimation endings
- sharper analysis of money, desire, face, traffic, failure, awkward motives, and social embarrassment

## What Changed

### Added

- `references/research/09-social-media-speech-corpus.md`
- `references/research/10-lowbrow-voice-calibration.md`
- `references/evidence/social-speech-map.csv`
- `scripts/social_speech_check.py`
- Lowbrow / anti-polish demo set
- FID-011 to FID-014 fidelity cases
- Over-polished output penalty
- Lowbrow boundary failure checks

### New Candidate Models

- 下三路牵引
- 知识分子外衣 / 俗人落点

These models remain candidate in this release.

## Evaluation Result

v0.7-run-001 completed automated Answer Agent + Scoring Agent evaluation.

- Total score: 100/100
- Release recommendation: pass
- FID-011 to FID-014: pass
- Over-polished failures: 0
- Lowbrow boundary failures: 0
- High-risk safety failures: 0
- Candidate/verified confusions: 0
- Source hallucinations: 0

## Human Review

Lightweight human review completed.

- Reviewer decision: Pass for v0.7.0 release prep
- Release blockers: none found
- FID-011 to FID-014 human review: pass
- Candidate models remain candidate
- Hard safety boundaries remain unchanged

## What This Release Allows

- Rougher authorized style drafts
- Less polished, less generic AI commentary
- More colloquial expression
- More anti-sublimation endings
- More direct analysis of money, desire, face, traffic, failure, and awkward motives
- Stronger Level 2 and Level 3 authorized draft behavior

## What This Release Does Not Allow

- Real-time impersonation of Zhou Lifeng
- Fabricated private facts, locations, relationships, promises, or controversy responses
- Explicit sexual content
- Doxxing, harassment, privacy exposure, or mobbing
- Dangerous travel, gray-market, illegal, border-crossing, or platform-evasion guides
- Long transcript, subtitle, or interview reproduction
- Treating unverified social accounts as verified evidence
- Upgrading candidate models without evidence

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
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

## Known Limits

- New lowbrow models remain candidate.
- X account evidence remains unverified unless independently confirmed.
- This release improves style fidelity but does not remove hard safety boundaries.
- This Skill is still not a real-time official statement generator.

## Recommended Next Step

Proceed to v0.8 with:

- external reviewer feedback
- more verified social speech sources
- optional screenshots / launch assets
- archive packaging automation
- public announcement materials
