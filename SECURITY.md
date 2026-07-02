# Security Policy

This project is not authorized by 周丽峰 and does not represent him. It is a public-source research Skill for social-observation perspective analysis.

## Reporting Security Issues

If you find a safety issue, open a GitHub issue with:

- The file and line involved.
- The risky prompt or behavior.
- Why it violates the project boundaries.
- A safer alternative, if you have one.

Do not include private information, doxxing material, leaked messages, or dangerous operational details in the report.

## What Counts as a Security Issue

Security issues include:

- Impersonating 周丽峰本人 or generating statements as him.
- Fabricating personal views, private facts, income, location, relationships, or platform inside information.
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

## Preferred Fix Pattern

Fixes should add source-aware boundaries, safer alternatives, and test coverage. If a risky behavior is found in `SKILL.md`, add or update a matching case in `tests/safety_cases.yaml`.
