# v1.0.0 - Stable Public Release

## Release Type

Stable public release.

## Summary

v1.0.0 is the first stable public release of `zhoulifeng-skill`.

This release packages the project as an authorized Zhou Lifeng / 峰哥亡命天涯 style Skill with:

- authorization-aware voice modes
- evidence tracking
- verified / candidate / rejected model separation
- safety hard boundaries
- public demo outputs
- fidelity and safety tests
- dual-Agent evaluation records
- human review records
- external reviewer feedback record
- source verification workflow
- archive packaging workflow
- final v1.0 audit pass

This release is stable for public use and review, but it is not a claim of perfect fidelity or real-time personhood.

## Final v1.0 Audit Result

Final v1.0 audit completed.

- Archive content audit: pass
- Install smoke test: pass
- Public readability review: pass
- Release blockers: none found
- Remaining P2 items: non-blocking
- Final audit decision: ready for v1.0.0 final release

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

Candidate models remain candidate in v1.0.0.

## Source Verification Status

X `@zlf86` remains:

- status: `unverified`
- used_for: `candidate_voice_calibration`
- can_enter_verified_models: `no`

It must not be used as verified evidence unless independently confirmed in a future release.

## Authorization / Public Proof Status

The project is maintained as an authorized style-draft Skill.

Private authorization materials are not included in the repository.

Public proof is not included at this stage unless a public authorization statement becomes available later.

This Skill is not a real-time official statement generator.

## External Review Status

The project has recorded:

- one real external reviewer feedback item
- one follow-up pass from that reviewer

This release does not claim broad external review completion.

## Safety Boundary Status

Hard safety boundaries remain unchanged.

The Skill does not allow:

- real-time impersonation
- fabricated private facts
- doxxing or harassment
- privacy exposure
- dangerous travel guidance
- gray-market or illegal guidance
- platform-evasion guidance
- explicit sexual content
- long transcript or subtitle reproduction

## Evaluation Status

Prior automated and review milestones remain part of the project record, including:

- dual-Agent evaluation
- fidelity / safety cases
- v0.7 lowbrow voice evaluation
- lightweight human reviews
- external reviewer feedback and follow-up
- final v1.0 audit

Evaluation results are evidence of test performance, not proof of perfect fidelity.

## Archive

Generate the stable archive with:

```bash
python3 scripts/create_release_archive.py --version v1.0.0
```

Expected local archive path:

```text
dist/zhoulifeng-skill-v1.0.0.zip
```

`dist/` is intentionally ignored and should not be committed.

## What This Release Is Not

This release is not:

- a real-time official statement generator
- a perfect-fidelity personality clone
- proof that broad external review is complete
- proof that X `@zlf86` is verified
- a promotion of candidate models to verified models
- permission to weaken hard safety boundaries
- a repository for private authorization materials, private chats, raw long transcripts, or private personal data

## Recommended Next Step

Use v1.0.0 as the stable public baseline. Future releases can add more public proof links, broader external review coverage, screenshots, and additional source verification without changing the v1.0.0 safety and evidence boundaries.
