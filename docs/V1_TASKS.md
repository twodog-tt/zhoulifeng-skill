# v1.0 Task Plan

## P0

None known at this planning checkpoint.

If a safety, authorization, impersonation, privacy, dangerous-content, or private-material leak issue appears, it becomes P0 and blocks v1.0 until fixed.

## P1

None remaining for `v1.0.0-rc.1` tag prep.

Resolved in rc.1 readiness cleanup:

- Confirm v0.9.0 release status: fixed.
- Record reviewer follow-up if not yet committed: fixed.
- Finalize release criteria: fixed.
- Run final validation: fixed locally.
- Generate and inspect archive: fixed for rc.1 local package; `dist/` remains untracked.
- Final README / AUTHORIZATION / launch audit: fixed for rc.1 readiness.
- Create final v1.0 regression run if needed: not required for rc.1 because core Skill, model status, and safety boundaries were not changed.
- Confirm candidate models remain candidate: fixed.
- Confirm X `@zlf86` remains unverified unless independently confirmed: fixed.
- Confirm hard safety boundaries remain unchanged: fixed.

Downgraded to P2:

- Prepare `RELEASE_NOTES_v1.0.0.md`: defer to actual v1.0 release prep so the notes can reflect final rc findings.

## P2

- Add install screenshots.
- Add validation screenshots.
- Add demo screenshots.
- Collect more external reviewer feedback.
- Improve launch posts.
- Add GitHub Discussions launch post.
- Attach inspected stable package archive to the release if desired.
- Prepare `RELEASE_NOTES_v1.0.0.md` during actual v1.0 release prep.
