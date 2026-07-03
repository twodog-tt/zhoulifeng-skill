# v0.4 Run 001

## Status

Partially completed.

Scoring Agent output was provided and recorded, but the Answer Agent output is still missing. The Scoring Agent evaluated the missing Answer Agent output as all cases failed with `0/100`.

This run does not constitute a valid fidelity pass.

## Inputs

* `SKILL.md`
* `FIDELITY.md`
* `tests/fidelity_cases.yaml`
* `tests/safety_cases.yaml`
* `tests/expected_behaviors.md`
* `evals/dual-agent-protocol.md`

## Current Artifact Status

* `answer-agent-output.md`: missing actual Answer Agent output
* `scoring-agent-output.md`: recorded from external Scoring Agent output
* `human-review-notes.md`: no human reviewer content provided
* `case-summary.csv`: updated from Scoring Agent output
* `improvement-actions.md`: updated from Scoring Agent output

## Required Procedure To Complete Run

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
