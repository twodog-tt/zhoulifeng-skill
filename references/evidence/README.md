# Evidence Notes

This directory stores short, source-linked evidence notes for model review.

Evidence notes must:

- Use source IDs that exist in `references/source-index.csv`.
- Use short summaries, not long transcripts or copied articles.
- Mark uncertain timestamps as `unknown`.
- Identify whether evidence is supporting, counterexample, boundary, or unclear.
- Mark confidence as high, medium, or low.

Run:

```bash
python3 scripts/evidence_check.py
```

Current v0.4 status: initial evidence map prepared. More timestamped review is needed before candidate models can be upgraded.
