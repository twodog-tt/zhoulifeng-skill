# Launch

This document prepares public launch copy for the repository. It should describe the project as an authorized style Skill and public-source-supported social-observation toolkit, not as a real-time official statement generator.

## One-Line Introduction

An authorized Zhou Lifeng / 峰哥亡命天涯 style Skill for social observation, topic framing, commentary drafts, and safety-bounded voice adaptation.

## Chinese Public Launch Draft

# zhoulifeng-skill：一个已授权的「峰哥亡命天涯」风格 Skill

`zhoulifeng-skill` 是一个面向 Agent / Codex / Claude / Cursor 等 AI runtime 的人物风格 Skill。

它基于公开资料、结构化证据、授权边界和多轮评测，提炼「峰哥亡命天涯 / 周丽峰」式的社会观察、内容判断、冷感表达和荒诞现实拆解方式。

这个项目不是一个简单的“模仿口头禅”工具，也不是把人物做成低质量 bot。它更接近一个可审计、可验证、可安装的人物风格系统。

### 这个项目是什么

这是一个已授权的 Zhou Lifeng / 峰哥亡命天涯 style Skill。

它可以帮助你做：

- 峰哥式社会观察
- 短视频选题拆解
- 授权风格文案草稿
- 冷感、荒诞、现实感评论
- 采访角度生成
- 内容传播判断
- 网红 / 边缘样本 / 社会议题分析

它支持不同强度的口吻模式：

- Level 0：普通分析
- Level 1：峰哥式视角
- Level 2：授权峰哥式口吻草稿
- Level 3：授权第一人称草稿

Level 3 可以写得更像“本人风格草稿”，但仍然会明确区分：这是授权风格草稿，不是峰哥刚刚实时确认的本人声明。

### 这个项目不是什么

它不是：

- 峰哥本人实时发言生成器
- 私人观点伪造器
- 争议回应编造器
- 危险旅行 / 灰产 / 边境行动指南
- 人肉、网暴、隐私曝光工具
- 露骨内容生成器
- 长字幕 / 长访谈搬运仓库

授权让它可以更接近峰哥的语气、节奏、冷感、损劲和荒诞观察，但不允许它虚构私人事实、实时行踪、真实承诺、未证实争议回应或危险操作细节。

### 项目特点

#### 1. 授权口吻模式

项目从早期的 public-source-based perspective skill，升级为 authorized Zhou Lifeng / 峰哥亡命天涯 style Skill。

这意味着它不再只是“从外部观察峰哥”，而是可以在授权边界内生成更接近峰哥表达方式的内容草稿。

#### 2. 低道德说教感 + 高安全硬边界

这个 Skill 不会把所有东西都写成普通 AI 的安全客服腔。

它允许更冷、更损、更现实、更荒诞的表达；允许拆人性、欲望、流量、投机、虚荣和社会缝隙。

但硬边界不变：

- 不冒充实时本人声明
- 不捏造私人事实
- 不人肉、不网暴、不泄露隐私
- 不提供危险、违法、灰产、平台规避指南
- 不生成露骨内容
- 不搬运长篇原文、字幕或访谈稿

#### 3. 有证据地图

仓库包含 `references/evidence/` 和 `source-index.csv`，用于记录模型判断来自哪些公开来源。

目前 evidence map 已扩展到 28 条 evidence rows，覆盖 verified 和 candidate models。

#### 4. 有评测体系

项目包含：

- fidelity cases
- safety cases
- expected behaviors
- dual-Agent evaluation protocol
- scoring agent prompt
- answer agent prompt
- human reviewer checklist
- public demo outputs

v0.4-run-003 已完成真实评测：

- Total score：100/100
- Release recommendation：pass
- High-risk safety failures：0
- Impersonation failures：0
- Dangerous instruction failures：0
- Candidate / verified confusions：0
- Source hallucinations：0
- False real-time personhood failures：0

#### 5. 有安装和运行文档

仓库包含：

- `docs/INSTALL.md`
- `docs/PACKAGING.md`
- `docs/RUNTIME_COMPATIBILITY.md`
- `docs/ARCHIVE_WORKFLOW.md`
- `examples/public-demo.md`
- `examples/public-demo-outputs.md`

你可以把它作为一个 Agent Skill 使用，也可以把它当作一个人物风格蒸馏项目模板来参考。

### 当前模型状态

Verified models：

- 底层现场主义
- 边缘样本优先
- 内容判断四问

Candidate models：

- 荒诞现实解构
- 采访中的弱控制
- 流量红线雷达

Rejected / unsafe patterns：

- 把“自嘲式冒险人格”作为可激活人格
- 口头禅人格复刻
- 争议站队与封禁原因脑补

Candidate models 目前仍保持 candidate，没有为了“更像”而强行升级。

### 适合谁用

适合：

- 想研究人物风格 Skill 的开发者
- 想做授权风格 Agent 的创作者
- 想研究 AI 如何蒸馏人物表达系统的人
- 想做社会观察、短视频选题、内容拆解的人
- 想参考一个带 evidence / eval / safety / review 的开源 Skill 模板的人

不适合：

- 想伪造本人声明的人
- 想做网暴、人肉、隐私曝光的人
- 想获取危险路线、灰产联系、平台规避技巧的人
- 想搬运长字幕、长访谈、原文内容的人
- 想把 Skill 做成无边界人格克隆的人

### 为什么开源

因为人物风格 Skill 不应该只是“像不像”的玄学。

它应该能回答这些问题：

- 这个风格判断有什么证据？
- 哪些模型是 verified，哪些只是 candidate？
- 哪些东西不能模仿？
- 授权允许什么，不允许什么？
- 安全边界在哪里？
- 评测是否真的跑过？
- 失败案例是否被记录？
- 外部用户能不能安装、审计、复现？

这个项目尝试把“人物风格蒸馏”做成一个工程化、可审计、可迭代的开源模板。

### Repo

GitHub：

[https://github.com/twodog-tt/zhoulifeng-skill](https://github.com/twodog-tt/zhoulifeng-skill)

Release：

v0.6.0 - Public Readiness and Reviewer Coverage

如果你对人物 Skill、授权风格 Agent、内容创作者 AI 分身、风格蒸馏评测感兴趣，欢迎 star、fork、review，也欢迎提 issue。

## GitHub Release Notes Draft

`zhoulifeng-skill` is an authorized style Skill for building 峰哥亡命天涯-style social observation and commentary drafts from documented boundaries, public evidence, demo outputs, and evaluation reports.

This release focuses on public usability and auditability: installation docs, runtime compatibility notes, demo prompts, demo outputs, review coverage, safety boundaries, and packaging guidance. It does not turn the Skill into a live official spokesperson, a source of private facts, or a tool for dangerous, illegal, explicit, harassing, or privacy-invasive requests.

Good uses:

- Analyze social topics with a colder, sharper, more reality-facing observation frame.
- Draft authorized voice-style commentary with clear boundaries.
- Review whether a topic is suitable for public, safety-bounded content.
- Test Agent runtimes against fidelity and safety cases.

Not supported:

- Real-time claims about Zhou Lifeng's current views, location, private relationships, commitments, or controversy responses.
- Dangerous travel, illegal border action, gray-market contact, platform evasion, doxxing, harassment, explicit content, or long transcript copying.
- Upgrading candidate models to verified without new evidence.

## X / Twitter Post Draft

v0.7 dev work for `zhoulifeng-skill`: launch assets + packaging automation.

It is an authorized 峰哥亡命天涯 style Skill for social observation and commentary drafts, with hard safety boundaries and explicit verified / candidate / rejected model separation.

Not a real-time official statement generator. Not a dangerous travel or gray-market guide. Not a transcript archive.

Repo:
https://github.com/twodog-tt/zhoulifeng-skill

Latest release:
https://github.com/twodog-tt/zhoulifeng-skill/releases

## Project Positioning

This project sits between voice adaptation, public evidence research, and safety evaluation.

It is designed to help Agents produce authorized 峰哥式 social observation drafts while keeping the following distinctions visible:

- verified models are supported by existing evidence
- candidate models remain tentative
- rejected / unsafe patterns are boundary markers only
- generated outputs are drafts, not live personal statements

The Skill can be sharp, cold, cynical, absurd, and practical. It should not become moralized customer-service prose. It also must not trade that sharper tone for harmful instructions, privacy violations, impersonation, or invented personal facts.

## Good Fit

- Builders testing Agent Skill packaging and validation workflows.
- Reviewers auditing voice fidelity, safety boundaries, and evidence discipline.
- Creators drafting social-observation angles without pretending to speak as the real person in real time.
- Researchers comparing public evidence, demo behavior, and evaluation outputs.

## Not A Good Fit

- Anyone who needs official real-time statements from Zhou Lifeng.
- Anyone asking for private facts, private authorization material, locations, relationships, or non-public commitments.
- Anyone trying to create dangerous travel guides, illegal action plans, gray-market access, platform evasion, harassment, doxxing, or explicit content.
- Anyone looking for full transcripts, copied subtitles, or long quote archives.

## Safety Boundaries

The public positioning should repeat these hard limits:

- Do not impersonate Zhou Lifeng as a real-time personhood claim.
- Do not fabricate private views, private facts, locations, relationships, promises, or controversy responses.
- Do not expose private authorization material.
- Do not provide dangerous travel, illegal border action, gray-market contact, or platform evasion instructions.
- Do not facilitate privacy exposure, doxxing, harassment, or dogpiling.
- Do not generate explicit sexual content.
- Do not copy long transcripts, subtitles, interviews, or other copyrighted source text.
- Do not upgrade candidate models without a separate evidence review.

## Demo Links

- [Public Demo Prompts](../examples/public-demo.md)
- [Public Demo Outputs](../examples/public-demo-outputs.md)
- [v0.4 Fidelity Report](../evals/reports/v0.4-fidelity-report.md)
- [Runtime Compatibility](RUNTIME_COMPATIBILITY.md)
- [Installation](INSTALL.md)

## Release Links

- [GitHub Releases](https://github.com/twodog-tt/zhoulifeng-skill/releases)
- [Latest Release Badge](https://github.com/twodog-tt/zhoulifeng-skill/releases/latest)
- [Repository](https://github.com/twodog-tt/zhoulifeng-skill)

## Language To Avoid

Avoid launch phrasing that says or implies:

- "This is Zhou Lifeng speaking now."
- "This generates his official current position."
- "This fully clones the person."
- "This has distilled the final personality."
- "This can safely guide dangerous fieldwork."
- "Candidate models are now verified."

Use:

- "authorized style Skill"
- "voice-style draft"
- "public-source-supported observation frame"
- "not a real-time official statement generator"
- "hard safety boundaries remain unchanged"
