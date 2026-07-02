# v0.3.0 Release Notes

## Release Type

Engineering readiness / release validation version.

## What This Release Adds

* Structured fidelity test cases
* Structured safety boundary test cases
* Static fidelity validation runner
* GitHub Actions validation workflow
* Contribution guidelines
* Security policy
* Expanded README release/status sections
* Clear verified / candidate / rejected model distinction

## Current Model Status

Verified:

* 底层现场主义
* 边缘样本优先
* 内容判断四问

Candidate:

* 荒诞现实解构
* 采访中的弱控制
* 流量红线雷达

Rejected / Unsafe:

* 自嘲式冒险人格 as an activatable persona
* 口头禅人格复刻
* 争议站队与封禁原因脑补

## What This Release Is Not

This release is not:

* an official Zhou Lifeng / 峰哥亡命天涯 bot
* an authorized representative of Zhou Lifeng
* a final fidelity-approved personality clone
* a tool for dangerous travel, illegal activity, gray-market access, harassment, privacy exposure, or explicit content
* a long transcript or quote archive

## Validation

The following commands pass locally:

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

## Known Gaps

* Human reviewer evidence audit still required
* Dual Agent fidelity evaluation has not yet been executed
* Candidate models need more A/B-grade source evidence
* More timestamped video evidence and short non-infringing summaries are needed

## Recommended Next Step

Proceed to v0.4:

* run dual Agent fidelity evaluation
* add timestamped evidence notes
* strengthen candidate model evidence
* prepare a public demo prompt set
