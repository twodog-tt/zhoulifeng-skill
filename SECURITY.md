# Security Policy

This project is maintained as an authorized Zhou Lifeng / 峰哥亡命天涯 style Skill. Authorization supports style drafting and content analysis; it does not make model output a verified real-time personal statement from Zhou Lifeng.

## Reporting Security Issues

If you find a safety issue, open a GitHub issue with:

- The file and line involved.
- The risky prompt or behavior.
- Why it violates the project boundaries.
- A safer alternative, if you have one.

Do not include private information, doxxing material, leaked messages, or dangerous operational details in the report.

## What Counts as a Security Issue

Security issues include:

- Presenting generated drafts as Zhou Lifeng's verified real-time personal statements.
- Fabricating personal views, private facts, income, location, relationships, commitments, plans, controversy responses, or platform inside information.
- Revealing or encouraging collection of private information about real people.
- Doxxing, harassment, dogpiling, or targeted humiliation.
- Dangerous travel, border action, gray-market contact, war-zone, or illegal activity guidance.
- Platform ban evasion or moderation bypass instructions.
- Explicit sexual content, especially involving real people or minors.
- Large-scale copyright copying of transcripts, subtitles, articles, or interviews.
- Turning controversy rumors into asserted facts.
- Treating candidate models as verified.

## Scope

We handle safety issues in this repository's Skill instructions, tests, references, and examples. We do not process requests for private information about 周丽峰, interview subjects, contributors, or third parties.

Do not submit private authorization materials, contracts, chat logs, signatures, phone numbers, addresses, or other non-public evidence in security reports.

## Preferred Fix Pattern

Fixes should add source-aware boundaries, safer alternatives, and test coverage. If a risky behavior is found in `SKILL.md`, add or update a matching case in `tests/safety_cases.yaml`.
