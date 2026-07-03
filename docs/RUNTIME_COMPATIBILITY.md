# Runtime Compatibility

This Skill is designed to be portable across Agent runtimes, but exact behavior depends on how a runtime discovers skills, reads resources, and exposes tools.

## Codex

Codex-style runtimes should load `SKILL.md` as the primary instruction file and can read supporting files as needed:

- `AUTHORIZATION.md`
- `references/source-index.csv`
- `references/evidence/zlf-evidence-map.csv`
- `references/research/`
- `tests/expected_behaviors.md`
- `examples/public-demo.md`

The validation scripts are plain Python and do not require network access.

## Claude / Cursor / Other Agent Runtimes

Other runtimes may support similar Markdown skill folders, but compatibility is not guaranteed.

Common portable parts:

- Markdown instructions in `SKILL.md`
- public-source research notes
- evidence map CSV
- demo prompts
- safety and fidelity cases
- release and install docs

Potential runtime-specific parts:

- skill discovery location
- YAML frontmatter interpretation
- how bundled references are loaded
- how examples are surfaced to the model
- whether scripts can be executed
- whether `agents/openai.yaml` is recognized

## OpenAI Agents-Style Metadata

The repository includes:

```text
agents/openai.yaml
```

This file provides OpenAI-style metadata for skill lists and chips where supported. Runtimes that do not understand this file can ignore it and read `SKILL.md` directly.

## What Is Runtime-Independent

These behaviors are enforced by the public repo content and validation suite:

- non-impersonation boundary
- no false real-time personhood
- no private fact fabrication
- candidate / verified / rejected model distinction
- no dangerous travel, gray-market, platform evasion, doxxing, harassment, explicit content, or long transcript copying
- evidence rows must reference source IDs from `references/source-index.csv`

## What Requires Runtime Support

Some behaviors depend on host runtime conventions:

- automatic skill triggering from the `description`
- access to bundled references during generation
- executing local validation scripts
- rendering demos or examples in UI
- honoring `agents/openai.yaml`

When in doubt, treat this repository as a Markdown-first Skill and manually provide `SKILL.md` plus relevant references to the Agent runtime.
