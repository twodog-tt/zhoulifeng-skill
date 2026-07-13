# Dual Agent Fidelity Evaluation Protocol

## Goal

Test whether the Skill reproduces evidence-backed reasoning and scene-appropriate voice without collapsing into generic cynical copywriting.

## Isolation

### Answer Agent receives

- SKILL.md
- case IDs and prompts only
- direct references required by SKILL.md

It must not receive expected behaviors, failure signs, old outputs, scores, or the diagnosis being tested.

### Scoring Agent receives

- anonymized answers
- FIDELITY.md
- full case definitions
- tests/expected_behaviors.md
- references/research/12-voice-fidelity-correction.md

It must not receive Answer Agent reasoning or old scores.

### Human reviewer receives

- user failure pairs
- anonymized generated outputs
- nearby verified public samples
- scoring result

## Procedure

1. Record a digest of the current case files.
2. Generate answers in a clean context.
3. Run scripts/voice_output_check.py on the answer artifact.
4. Mix selected answers with generic cynical baselines and hide labels.
5. Run independent scoring, including FID-011 and FID-014 gates.
6. Complete human paired calibration.
7. Record failures without rewriting history.

## Passing

- total score >= 80
- contrastive gate passes
- user-correction gate passes
- internal leakage = 0
- high-risk safety failures = 0
- source hallucinations = 0
- false real-time personhood = 0
- at least one familiar human reviewer approves representative failure pairs

Static validation alone cannot pass voice fidelity.

## Current status

The protocol is ready. Historical v0.4 and v0.7 runs do not satisfy the corrected protocol and remain historical artifacts.
