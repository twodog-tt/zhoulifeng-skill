# Archive Workflow

This workflow describes how to create a local release archive for public packaging review.

The archive is a convenience artifact, not a substitute for GitHub releases, validation logs, or human review.

## Pre-Archive Checks

Before creating an archive:

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
python3 scripts/evidence_check.py
python3 scripts/eval_run_check.py
python3 scripts/demo_check.py
python3 scripts/docs_check.py
python3 scripts/review_check.py
python3 scripts/demo_outputs_check.py
python3 scripts/archive_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

Confirm:

- `git status --short` is clean.
- Candidate models remain candidate unless a separate evidence review explicitly supports promotion.
- Hard safety boundaries remain unchanged.
- No private authorization material is present.

## Create Archive

Run:

```bash
python3 scripts/create_release_archive.py --version v0.7.0
```

By default, the archive is written to:

```text
dist/zhoulifeng-skill-v0.7.0.zip
```

`dist/` is ignored by git and should not be committed.

Use a different output path only when you have a specific local packaging workflow:

```bash
python3 scripts/create_release_archive.py --version v0.7.0 --output /tmp/zhoulifeng-skill-v0.7.0.zip
```

## Archive Checks

Run:

```bash
python3 scripts/archive_check.py
```

The checker verifies:

- `scripts/create_release_archive.py` exists.
- `docs/ARCHIVE_WORKFLOW.md` exists.
- `.gitignore` contains `dist/`.
- `.gitignore` contains `.DS_Store`.
- `dist/` is not tracked by git.

## Archive Contents

An archive should include:

- `SKILL.md`
- `AUTHORIZATION.md`
- `README.md`
- `LICENSE`
- `CHANGELOG.md`
- `docs/`
- `examples/`
- `references/evidence/`
- `references/source-index.csv`
- `references/research/`
- `tests/`
- `scripts/`
- `agents/openai.yaml`

## Exclusions

Exclude:

- `.git`
- `.DS_Store`
- `dist/`
- private authorization materials
- private chats or screenshots
- raw long subtitles
- full transcript dumps
- token / API key / credential files
- non-public materials
- local caches such as `__pycache__`
- files containing private data about real interviewees

Do not upload an archive if it includes:

- tokens, API keys, secrets, credentials, or `.env` files
- private authorization screenshots, contracts, chats, or account information
- raw transcripts, full subtitle exports, or long copied source text
- private paths or local machine-only files
- unsafe demo material that teaches dangerous travel, gray-market access, platform evasion, harassment, doxxing, or explicit content

## Release Requirement

Before attaching or publishing any archive, rerun the full validation suite:

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
python3 scripts/evidence_check.py
python3 scripts/eval_run_check.py
python3 scripts/demo_check.py
python3 scripts/docs_check.py
python3 scripts/review_check.py
python3 scripts/demo_outputs_check.py
python3 scripts/archive_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

Do not create an archive from a dirty working tree. Do not use a generated archive to imply that candidate models became verified or that hard safety boundaries were relaxed.
