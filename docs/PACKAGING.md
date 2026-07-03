# Packaging

This document describes how to package and release this Skill without leaking private material or weakening safety boundaries.

## Repository Structure

Important public release files:

- `SKILL.md`
- `AUTHORIZATION.md`
- `README.md`
- `CHANGELOG.md`
- `LICENSE`
- `agents/openai.yaml`
- `references/`
- `examples/`
- `tests/`
- `evals/`
- `scripts/`
- `docs/`

## Pre-Release Checklist

Before creating a release:

- Run all validation commands in `docs/INSTALL.md`.
- Confirm `git status --short` is clean or only contains intentionally excluded local files.
- Confirm candidate models remain candidate unless a separate evidence review supports promotion.
- Confirm hard safety boundaries remain unchanged.
- Confirm release notes do not describe the Skill as a real-time official statement generator.
- Confirm no private authorization files are present.
- Confirm no long subtitles, long transcripts, raw interview dumps, or copied articles are included.
- Confirm evaluation artifacts distinguish completed, invalid, placeholder, and pending runs.

## Tag / Release Flow

Use an annotated tag:

```bash
git tag -a vX.Y.Z -m "vX.Y.Z release title"
git push origin vX.Y.Z
```

Create a GitHub Release with a release-notes file:

```bash
gh release create vX.Y.Z \
  --title "vX.Y.Z - Release Title" \
  --notes-file RELEASE_NOTES_vX.Y.Z.md
```

If GitHub CLI is unavailable, create the release manually from the GitHub Releases page.

## Do Not Package

Do not package or commit:

- private authorization contracts
- private chats or private screenshots
- signatures, phone numbers, addresses, or identity documents
- raw long subtitles
- full interview transcripts
- long article copies
- private source files
- privacy data about real interviewees
- doxxing targets or harassment materials
- dangerous travel routes, gray-market contact instructions, platform evasion guides, or explicit content

## Release Language Boundaries

Release notes may say:

- authorized style Skill
- authorized voice evaluation pass
- lower moralizing with hard safety boundaries
- candidate models remain candidate

Release notes must not say:

- final personality clone
- real-time official statement generator
- all candidate models are verified
- dangerous/gray-market/explicit content is allowed
