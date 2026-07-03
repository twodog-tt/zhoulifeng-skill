# Contributing

Thanks for helping make `zhoulifeng-skill` more auditable and useful. This project is an authorized Zhou Lifeng / 峰哥亡命天涯 style Skill for drafting, content analysis, and social-observation writing. It is not a live personal statement generator or a substitute for Zhou Lifeng personally confirming a view.

## How to Add Sources

1. Add one row to `references/source-index.csv`.
2. Use the existing fields exactly: `id,title,platform,type,date,url_or_locator,primary_or_secondary,reliability,notes,local_path`.
3. Use `unknown` when the date cannot be verified.
4. Set reliability honestly:
   - `A`: public video, public interview, public account content from the person or direct source.
   - `B`: public media interview or reporting.
   - `C`: third-party comments, encyclopedia pages, forum summaries.
   - `D`: unverified or currently inaccessible leads; do not use in core models.
5. Keep notes short. Summarize; do not copy long passages.

## How to Add Research Notes

Update the relevant file under `references/research/`. Each note should identify source IDs, summarize what can be extracted, list contradictions or limits, and say what must not enter `SKILL.md`.

Do not paste long transcripts, long article excerpts, private information, or non-public chat records.

## How to Promote Candidate Models to Verified

A candidate model can become verified only when it has:

- Evidence from at least two source types, preferably A/B level.
- Multiple source IDs in `source-index.csv`.
- At least one documented failure mode.
- At least one counterexample or limitation in `references/research/`.
- No conflict with safety boundaries.

Update `SKILL.md`, `FIDELITY.md`, and tests together when a model changes status.

## How to Improve Safety Boundaries

Safety improvements are welcome. Add or update cases in `tests/safety_cases.yaml`, update `tests/expected_behaviors.md`, and make sure `tests/run_fidelity_check.py` still passes.

## Contributions Not Accepted

This project does not accept:

- Unverified private information.
- Long copied subtitles, transcripts, articles, or comments.
- Text that impersonates 周丽峰本人.
- Text that presents generated drafts as verified real-time Zhou Lifeng statements.
- Dangerous travel, border action, gray-market contact, or illegal activity guides.
- Explicit sexual content.
- Platform ban evasion or moderation bypass tutorials.
- Personality claims without source IDs.
- Claims that candidate models are verified without evidence.

## Validation

Run these before opening a PR:

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```
