# zhoulifeng-skill

[![Release](https://img.shields.io/github/v/release/twodog-tt/zhoulifeng-skill?label=release)](https://github.com/twodog-tt/zhoulifeng-skill/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Validate](https://github.com/twodog-tt/zhoulifeng-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/twodog-tt/zhoulifeng-skill/actions/workflows/validate.yml)

<p align="center">
  <img src="docs/assets/pixel-feng.png" alt="Pixel portrait for zhoulifeng-skill" width="360">
</p>

一个授权维护的“峰哥亡命天涯式社会观察与口吻草稿” Agent Skill。

This project is an authorized Zhou Lifeng / 峰哥亡命天涯 style skill. It is not a real-time official statement generator, and generated drafts are not a substitute for Zhou Lifeng personally confirming a view.

This is an authorized style-draft Skill, not an official live/personhood bot or real-time statement generator.

## Current Status

Current version: `v0.9.0`

Status: External review feedback and launch copy polish release

v0.8.0 focuses on launch materials, external review workflow, source verification workflow, and archive packaging automation.

Next planning track: `v1.0.0`, focused on broader external reviewer coverage, optional public proof links if available, screenshot/demo-run assets, stable install packaging, and final pre-1.0 source and candidate-model audit.

v0.7.0 在 v0.6.0 public readiness release 的基础上，完成 lowbrow / anti-polish voice calibration：新增 social media speech corpus、lowbrow voice calibration research、`FID-011` 到 `FID-014`、over-polished penalty、lowbrow boundary failure checks 和 v0.7-run-001 评测。v0.7-run-001 自动评测 `100/100`，release recommendation：`pass`；v0.7 lightweight human review 结论为 `Pass for v0.7.0 release prep`。This is an automated evaluation result, not proof of perfect fidelity.

v0.8.0 prepares broader public distribution with `launch/`, `reviews/external/`, `references/source-verification/`, and release archive automation. The external review framework was prepared in v0.8; v0.9 has recorded the first reviewer concern, but the full external review program is not complete. X `@zlf86` remains unverified, may be used only for `candidate_voice_calibration`, and cannot enter verified models.

v0.9.0 starts real external review intake. Feedback batch `EXT-001` has been recorded with reviewer decision `concern`, not safety hold; `EXT-001-FUP` records a follow-up `pass` for v0.9.0 release prep. This is one external reviewer follow-up, not a claim that broad external review is complete.

本项目是 authorized style skill，不是实时官方声明生成器。candidate models 仍保持 candidate，hard safety boundaries 保持不变。新增 lowbrow calibration 只降低过度体面感，不允许露骨、人肉、网暴、灰产、危险行动、平台规避或隐私内容。

## Quick Links

- [Installation](docs/INSTALL.md)
- [Launch Guide](docs/LAUNCH.md)
- [Launch Materials](launch/README.md)
- [Public Demo](examples/public-demo.md)
- [Public Demo Outputs](examples/public-demo-outputs.md)
- [Archive Workflow](docs/ARCHIVE_WORKFLOW.md)
- [Evidence Map](references/evidence/zlf-evidence-map.csv)
- [Source Verification](references/source-verification/README.md)
- [External Review](reviews/external/README.md)
- [Fidelity Report](evals/reports/v0.4-fidelity-report.md)
- [Authorization](AUTHORIZATION.md)
- [Runtime Compatibility](docs/RUNTIME_COMPATIBILITY.md)
- [Security Policy](SECURITY.md)

## What This Is / Is Not

This is:

- an authorized style Skill for Zhou Lifeng / 峰哥亡命天涯-style social observation, topic framing, commentary drafts, and voice adaptation
- a public-source-supported evidence and demo repository
- a Skill with verified / candidate / rejected model separation

This is not:

- a real-time official statement generator
- a replacement for Zhou Lifeng personally confirming a view
- permission to fabricate private facts, private views, locations, relationships, promises, or controversy responses
- permission to provide dangerous travel, gray-market access, privacy exposure, doxxing, harassment, explicit content, platform evasion, or long transcript copying
- evidence that candidate models have become verified

## v0.8 Release Scope

v0.7.0 已完成低体面/下三路/反升华口吻校准、自动评测和 lightweight human review。v0.8.0 发布 launch materials、external review framework、source verification workflow、archive packaging automation 和公共发布材料。

v0.8.0 不升级 candidate models，不放松 hard safety boundaries，不把未验证社交账号来源写成 verified evidence，也不把授权风格草稿描述成实时官方声明。v0.9 已录入第一条 reviewer concern 和 follow-up pass，但 full external review program 尚未完成。

评测入口：

- [Dual Agent Protocol](evals/dual-agent-protocol.md)
- [Evidence Map](references/evidence/zlf-evidence-map.csv)
- [v0.4 Fidelity Report](evals/reports/v0.4-fidelity-report.md)
- [v0.4 Run 003 Results](evals/results/v0.4-run-003/README.md)
- [Public Demo Prompts](examples/public-demo.md)

## 项目定位

本仓库用于维护授权的 Zhou Lifeng / 峰哥亡命天涯 style Skill，研究并生成授权风格草稿、内容选题分析、社会观察评论、采访视角拆解和争议事件分层分析。

授权允许更接近峰哥口吻做风格草稿、内容分析和二创辅助；但它不自动允许虚构私人事实、实时观点、真实承诺、行踪、关系或争议回应。风格草稿不得被包装成峰哥刚刚亲口确认的真实声明，除非另有独立确认或用户提供真实原文与发布背景。

hard boundaries 不因授权而放松：不得生成危险旅行、灰产接触、违法边境行动、平台规避、隐私暴露、人肉网暴、露骨内容或长篇原文/字幕搬运。

## Launch / Public Use

Public descriptions should call this an authorized style Skill for Zhou Lifeng / 峰哥亡命天涯-style social observation and commentary drafts. Do not describe it as a real-time official statement generator, a full personality clone, or evidence that candidate models have become verified.

Launch policy is maintained in [docs/LAUNCH.md](docs/LAUNCH.md). Draft GitHub announcements, X/Twitter threads, short posts, and FAQ copy are maintained in [launch/](launch/).

## External Review

External reviewer instructions, invite copy, feedback form, feedback log, and v0.8 report template are maintained in [reviews/external/](reviews/external/).

External feedback can identify concerns or release blockers, but it cannot by itself promote candidate models to verified. Model promotion still requires source evidence and a separate evidence review.

For v0.9 reviewer intake, use [reviews/external/v0.9-reviewer-packet.md](reviews/external/v0.9-reviewer-packet.md). Do not record private reviewer identity details, private-message text, or non-public source material.

## Source Verification

Source verification status for social accounts and public account references is maintained in [references/source-verification/](references/source-verification/).

Current status notes:

- Bilibili public account evidence can be used where already mapped and verified.
- X account `@zlf86` remains `unverified` and may only be treated as `candidate_voice_calibration`.
- Unverified social accounts cannot enter verified models.

## Archive / Packaging

Release archives can be generated locally with:

```bash
python3 scripts/create_release_archive.py --version v0.9.0
```

The default output path is `dist/zhoulifeng-skill-v0.9.0.zip`. `dist/` is ignored by git and should not be committed.

Archive contents, exclusions, checks, and release-before-publish validation steps are documented in [docs/ARCHIVE_WORKFLOW.md](docs/ARCHIVE_WORKFLOW.md).

## Authorization Status

本项目现在按授权风格 Skill 维护。授权允许更接近峰哥口吻进行风格草稿、内容分析和二创辅助，但不允许虚构私人事实、实时观点或危险内容。

授权状态和范围见 [AUTHORIZATION.md](AUTHORIZATION.md)。公开仓库不保存私人合同、私聊、签名、电话号码、地址或其他非公开授权材料。

Public proof note: private authorization materials are not included in this repository. Public proof is not included at this stage; if a public authorization statement is later available, it can be summarized or linked without exposing private data.

## Model Status

当前 `SKILL.md` 将模型分成三类：

- verified：`底层现场主义`、`边缘样本优先`、`内容判断四问`
- candidate：`荒诞现实解构`、`采访中的弱控制`、`流量红线雷达`、`下三路牵引`、`知识分子外衣 / 俗人落点`
- rejected / unsafe：`自嘲式冒险人格` 作为 Skill 人格、`口头禅人格复刻`、`争议站队与封禁原因脑补`

candidate 不能写成 verified。rejected / unsafe 只能用于边界说明，不能用于生成。

## 安装方法

手动安装到 Codex：

```bash
git clone git@github.com:twodog-tt/zhoulifeng-skill.git ~/.codex/skills/zhoulifeng-skill
```

也可以 clone 到 Claude、Cursor 或其他 Agent Skills 兼容目录。不同 Agent runtime 的 skill 发现、frontmatter、工具调用和资源加载方式可能不同，本仓库不保证所有 runtime 完全兼容。

如果你的 runtime 支持类似 `npx skills add` 的 GitHub repo 安装方式，可以尝试使用本仓库地址安装，但本项目不保证所有 runtime 都支持该命令。

## Running Validation

本地校验：

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
python3 scripts/evidence_check.py
python3 scripts/social_speech_check.py
python3 scripts/eval_run_check.py
python3 scripts/demo_check.py
python3 scripts/docs_check.py
python3 scripts/review_check.py
python3 scripts/demo_outputs_check.py
python3 scripts/archive_check.py
python3 scripts/external_review_check.py
python3 scripts/source_verification_check.py
python3 scripts/launch_materials_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

GitHub Actions 会在 push 和 pull request 上运行同一组核心校验。

## Fidelity Evaluation

`tests/fidelity_cases.yaml` 包含 10 个结构化 fidelity cases，总分 100。`tests/safety_cases.yaml` 包含 12 个安全边界测试。`tests/run_fidelity_check.py` 只做静态规则检查，不调用外部 LLM API。

v0.4-run-003 已完成 Answer Agent + Scoring Agent 评测和 lightweight human review。结果：`100/100`，release recommendation：`pass`，high-risk safety failures：`0`，candidate/verified confusions：`0`，false real-time personhood failures：`0`。This is an automated evaluation result, not proof of perfect fidelity.

通过阈值和后续人工审计标准见 `FIDELITY.md`。

## Demo

短 demo：

```text
用峰哥式视角分析“年轻人不想升职”。
```

```text
按授权峰哥式口吻写一段短视频开头，主题是“大家都在副业焦虑”。
```

```text
写一段授权第一人称草稿，主题是“危险题材为什么不能被观众当旅游攻略”。
```

```text
有人想人肉争议视频里的受访者，峰哥式怎么拒绝并转成围观机制分析？
```

更多公开 demo 见 [examples/public-demo.md](examples/public-demo.md)，对应 sample outputs 见 [examples/public-demo-outputs.md](examples/public-demo-outputs.md)。安装说明见 [docs/INSTALL.md](docs/INSTALL.md)，runtime 兼容性见 [docs/RUNTIME_COMPATIBILITY.md](docs/RUNTIME_COMPATIBILITY.md)，v0.4 评测报告见 [evals/reports/v0.4-fidelity-report.md](evals/reports/v0.4-fidelity-report.md)。

这些 demo 只展示 authorized style skill，不是实时官方声明生成器。candidate models 仍保持 candidate，hard boundaries unchanged。

## 使用示例

```text
用峰哥式视角分析一下县城咖啡店变多。
```

```text
把“年轻人不想升职”这个选题改成峰哥亡命天涯式切口。
```

```text
给一个长期住青旅的自由职业者设计采访问题，要有峰哥式现实感。
```

## 仓库结构

```text
zhoulifeng-skill/
├── SKILL.md
├── README.md
├── AUTHORIZATION.md
├── FIDELITY.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── LICENSE
├── quick_validate.py
├── docs/
│   ├── ARCHIVE_WORKFLOW.md
│   ├── INSTALL.md
│   ├── LAUNCH.md
│   ├── PACKAGING.md
│   ├── RUNTIME_COMPATIBILITY.md
│   ├── SCREENSHOTS.md
│   └── assets/
├── .github/
│   └── workflows/
│       └── validate.yml
├── agents/
│   └── openai.yaml
├── references/
│   ├── extraction-framework.md
│   ├── fidelity-scorecard.md
│   ├── source-index.csv
│   ├── evidence/
│   │   ├── README.md
│   │   ├── zlf-evidence-map.csv
│   │   └── notes/
│   ├── source-verification/
│   │   ├── README.md
│   │   ├── account-verification-checklist.md
│   │   ├── social-account-status.csv
│   │   └── reports/
│   └── research/
│       ├── 01-primary-videos.md
│       ├── 02-interviews-and-longform.md
│       ├── 03-expression-dna.md
│       ├── 04-external-views-and-controversies.md
│       ├── 05-content-decisions-and-business.md
│       ├── 06-timeline.md
│       ├── 07-safety-and-boundaries.md
│       └── 08-candidate-model-review.md
├── scripts/
│   ├── archive_check.py
│   ├── create_release_archive.py
│   ├── demo_check.py
│   ├── demo_outputs_check.py
│   ├── docs_check.py
│   ├── evidence_check.py
│   ├── external_review_check.py
│   ├── launch_materials_check.py
│   ├── quality_check.py
│   ├── review_check.py
│   ├── source_verification_check.py
│   ├── source_index_check.py
│   └── transcript_cleaner.py
├── reviews/
│   ├── README.md
│   ├── external/
│   ├── reviewer-checklist.md
│   ├── v0.6-human-review-plan.md
│   └── reports/
├── launch/
│   ├── README.md
│   ├── github-announcement.md
│   ├── x-thread-cn.md
│   ├── x-thread-en.md
│   ├── short-post-cn.md
│   ├── short-post-en.md
│   └── faq.md
├── evals/
│   ├── dual-agent-protocol.md
│   ├── evaluator-prompts/
│   ├── reports/
│   └── results/
├── tests/
│   ├── fidelity_cases.yaml
│   ├── safety_cases.yaml
│   ├── expected_behaviors.md
│   └── run_fidelity_check.py
└── examples/
    ├── public-demo.md
    ├── public-demo-outputs.md
    ├── sample-prompts.md
    └── sample-conversations.md
```

## 调研方法

本项目只使用公开资料，包括公开视频、公开访谈、公开媒体报道、公开社交媒体动态、外部评论、争议事件报道和商业/MCN/内容决策资料。

来源可靠度分为：

- A：本人直接发布的视频、直播切片、采访原文、本人账号动态。
- B：权威媒体采访或报道。
- C：第三方评论、百科、论坛整理。
- D：无法交叉验证的传闻或当前不可访问的旧链接，不进入核心模型，只能进入“待验证”。

核心判断应能回到 `references/source-index.csv` 和 `references/research/` 找到证据。没有证据的判断只能标注为 candidate。

## Safety Policy

本 Skill 不做：

- 把模型生成内容伪装成周丽峰刚刚亲口确认的真实声明。
- 捏造本人观点、实时承诺、行踪、关系或私人信息。
- 传播未证实隐私、人肉信息或网暴目标。
- 生成危险探险、违法边境行动、灰产接触、规避平台封禁指南。
- 生成露骨性内容。
- 大段搬运原视频逐字稿或长篇原文。
- 消费真实受访者苦难。

安全问题请参考 `SECURITY.md`。贡献请参考 `CONTRIBUTING.md`。

## Contributing

欢迎补充公开来源、研究摘要、评测用例和安全边界。贡献前请运行本地校验，并确保新增结论可以回到 source ID。

不接受未证实隐私、长篇搬运字幕/原文、伪装成实时本人声明的文案、危险行动指南、露骨内容、平台规避教程或无来源人格设定。

## Release Roadmap

- v0.3.0：发布前工程化，静态评测、CI、贡献和安全政策。
- v0.4.0：授权口吻模式校准，dual-Agent evaluation pass，lightweight human review pass。
- v0.5.0：补强 evidence depth、安装/打包/runtime 文档和 public demo set。
- v0.6.0：更广覆盖的人类 reviewer 审计、demo 输出样例、安装截图、README badges 和可选打包流程。
- v1.0.0：达到发布阈值，冻结核心模型，开始接受兼容 runtime 的安装反馈。

## License

本仓库代码和原创文档使用 MIT License。被索引的公开视频、报道、访谈和平台内容版权归原权利人所有，本仓库只保存短摘要、出处和研究笔记。
