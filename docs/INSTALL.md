# Install

This document explains how to install and validate the authorized Zhou Lifeng / 峰哥亡命天涯 style Skill in a local Agent runtime.

## Clone Install

Clone the repository into a local skill directory:

```bash
git clone git@github.com:twodog-tt/zhoulifeng-skill.git ~/.codex/skills/zhoulifeng-skill
```

For HTTPS:

```bash
git clone https://github.com/twodog-tt/zhoulifeng-skill.git ~/.codex/skills/zhoulifeng-skill
```

## Codex / Agents Usage

For Codex-style runtimes, place the repository in a directory that the runtime scans for skills. The required entry point is:

```text
SKILL.md
```

The Skill also includes supporting resources:

- `AUTHORIZATION.md`
- `references/source-index.csv`
- `references/evidence/zlf-evidence-map.csv`
- `references/research/`
- `tests/`
- `evals/`
- `agents/openai.yaml`

## Copy To A Runtime Directory

If the runtime does not support direct Git installs, copy the repository folder into the runtime's skill directory:

```bash
mkdir -p ~/.codex/skills
cp -R /path/to/zhoulifeng-skill ~/.codex/skills/zhoulifeng-skill
```

Avoid copying private authorization materials, private chats, screenshots, raw subtitles, or non-public source files into the public skill folder.

## Local Validation

Run the full local validation suite:

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
python3 scripts/evidence_check.py
python3 scripts/eval_run_check.py
python3 scripts/demo_check.py
python3 scripts/docs_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

The checks do not call external LLM APIs. They validate structure, source references, evidence rows, evaluation run artifacts, demo coverage, and required docs.

## Runtime Compatibility Note

Different Agent runtimes may interpret skill metadata, tool access, and bundled resources differently. This repository is designed as a Markdown-first Skill, but full behavior depends on the host runtime.

See `docs/RUNTIME_COMPATIBILITY.md` for details.
