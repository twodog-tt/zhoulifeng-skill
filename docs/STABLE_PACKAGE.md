# Stable Package

## Package Goal

The release archive is an installable package, not a complete research dump.

It should contain the Skill, public docs, examples, evidence summaries, research notes, tests, and validation scripts needed for public installation and audit. It must not include private authorization materials, private chats, raw long transcripts, local-only files, tokens, API keys, or private data.

## Build

```bash
python3 scripts/create_release_archive.py --version v1.0.0-rc.1
```

Expected output:

```text
dist/zhoulifeng-skill-v1.0.0-rc.1.zip
```

`dist/` is ignored by git and should not be committed.

## Inspect

Before attaching an archive to any release, inspect it locally:

```bash
python3 scripts/archive_check.py
unzip -l dist/zhoulifeng-skill-v1.0.0-rc.1.zip | less
```

Confirm the archive includes:

- `SKILL.md`
- `AUTHORIZATION.md`
- `README.md`
- `LICENSE`
- `CHANGELOG.md`
- `agents/`
- `docs/`
- `examples/`
- `launch/`
- `references/evidence/`
- `references/research/`
- `references/source-verification/`
- `reviews/`
- `tests/`
- `scripts/`

Confirm the archive excludes:

- `.git`
- `.DS_Store`
- `dist/`
- private authorization materials
- private chats
- raw transcripts or long subtitles
- tokens / API keys / credentials
- private paths
- local cache files
- unauthorized reference photos

## Release Use

For v1.0-rc.1, a generated archive may be used for inspection and install testing. It should not be treated as the final v1.0 package until the final pre-v1.0 audit is complete.

candidate models remain candidate. hard safety boundaries remain unchanged. This package is not a real-time official statement generator.
