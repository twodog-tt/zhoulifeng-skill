# v0.4 Run 001

## Status

Not completed yet. Awaiting external Answer Agent and Scoring Agent outputs.

## Inputs

* `SKILL.md`
* `FIDELITY.md`
* `tests/fidelity_cases.yaml`
* `tests/safety_cases.yaml`
* `tests/expected_behaviors.md`
* `evals/dual-agent-protocol.md`

## Required Procedure

1. Open a fresh Agent session as Answer Agent.
2. Give it `evals/evaluator-prompts/answer-agent.md`.
3. Provide the test cases.
4. Save its output into `answer-agent-output.md`.
5. Open a separate fresh Agent session as Scoring Agent.
6. Give it `evals/evaluator-prompts/scoring-agent.md`.
7. Provide the Answer Agent output and scoring files.
8. Save scoring result into `scoring-agent-output.md`.
9. Ask a human reviewer to fill `human-review-notes.md`.
10. Summarize results into `case-summary.csv`.

## Notes

Do not mark this run completed until the Answer Agent output, Scoring Agent output, and human review notes are filled from actual evaluation work.
