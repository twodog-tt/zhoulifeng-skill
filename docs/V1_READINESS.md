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

No known blocker for `v1.0.0-rc.1` tag prep.

## v1.0-rc.1 Readiness

ready for final review before rc tag

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
- archive generation: fixed locally for `v1.0.0-rc.1`
- README / AUTHORIZATION / launch audit: fixed for rc.1 readiness
- source verification and candidate model status audit: fixed
- safety-boundary audit: fixed
- final v1.0 release notes: downgraded to P2 with reason; they belong to actual v1.0 release prep
- final regression run: deferred with reason and no release blocker; no core Skill/model/safety evaluator changes were made
