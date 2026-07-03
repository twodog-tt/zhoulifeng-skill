# v1.0 Readiness

## Goal

v1.0 代表稳定公开版，而不是最终人格完成版。

Stable public release means the Skill is installable, auditable, and clear about its authorization, evidence, model status, and safety boundaries.

## v1.0 Must Have

- Clear authorization wording
- Public proof status clearly stated
- Candidate / verified model separation
- Source verification status clear
- Hard safety boundaries unchanged
- Install docs usable
- Archive script usable
- Public demo outputs reviewed
- External review feedback recorded
- No private materials in repo
- No unsupported model upgrades

## v1.0 Must Not Claim

- Perfect fidelity
- Broad external review completion unless actually done
- Real-time official statement generation
- Verified status for unverified social accounts
- Permission for doxxing, gray-market, dangerous, explicit, or platform-evasion content

## Current Blockers

No known blocker for `v1.0.0` stable public release.

## v1.0.0 Release Status

ready for stable public release

P0: 0
P1: 0
P2: 7 optional items remain and are non-blocking.

Release notes: `RELEASE_NOTES_v1.0.0.md`

## v1.0-rc.1 Readiness

completed

P0: 0
P1: 0
P2: 7 optional items remain and are not rc.1 release blockers.

## Current Constraints

- candidate models remain candidate
- hard safety boundaries remain unchanged
- X `@zlf86` remains unverified and cannot enter verified models
- public proof status is documented, but public proof is not included at this stage
- broad external review is not claimed complete
- archive generated locally but `dist/` is not committed

## P1 Handling Summary

- final validation: fixed locally
- archive generation: fixed locally for `v1.0.0`
- README / AUTHORIZATION / launch audit: fixed for rc.1 readiness
- source verification and candidate model status audit: fixed
- safety-boundary audit: fixed
- final v1.0 release notes: fixed in `RELEASE_NOTES_v1.0.0.md`
- final regression run: deferred with reason and no release blocker; no core Skill/model/safety evaluator changes were made

## Final v1.0 Audit

Status: completed

Result: ready for v1.0.0 final prep

Release blockers: none found

Summary:

- archive content audit passed
- install smoke test from extracted archive passed
- public readability review passed
- P0: 0
- P1: 0
- P2: 7, all non-blocking
- candidate models remain candidate
- X `@zlf86` remains unverified
- hard safety boundaries remain unchanged
- broad external review is not claimed complete
- public proof is not included at this stage

## Stable Release Notes

v1.0.0 is a stable public release baseline, not a claim of perfect fidelity or broad external review completion.

- candidate models remain candidate
- X `@zlf86` remains unverified
- hard safety boundaries remain unchanged
- public proof is not included at this stage
- private authorization materials remain excluded from the public repository and archive
