# Archive Workflow

This optional workflow describes how a future release archive could be produced. It is not currently required for releases.

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
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

Confirm:

- `git status --short` is clean.
- Candidate models remain candidate unless a separate evidence review explicitly supports promotion.
- Hard safety boundaries remain unchanged.
- No private authorization material is present.

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
- private authorization materials
- private chats or screenshots
- raw long subtitles
- full transcript dumps
- token / API key / credential files
- non-public materials
- local caches such as `__pycache__`
- files containing private data about real interviewees

## Example Command

Example only; review before using:

```bash
git archive --format=zip --output=zhoulifeng-skill-vX.Y.Z.zip HEAD
```

Do not create an archive from a dirty working tree.
