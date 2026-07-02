# zhoulifeng-skill

一个基于公开资料提炼的“峰哥亡命天涯式社会观察” Agent Skill。

This project is a public-source-based perspective skill, not an official or authorized Zhou Lifeng bot.

## Current Status

Current version: `v0.3.0`

Status: Engineering readiness / release validation ready

v0.3 重点是发布前工程化：新增 fidelity/safety 测试用例、静态评测脚本、贡献指南、安全政策和 GitHub Actions 校验。它没有继续强化“人格扮演”，而是把重点放在可审计、可测试、可安装、可贡献。

## v0.4 Evaluation Roadmap

v0.3.0 已完成工程化校验。v0.4 的目标是 dual Agent fidelity evaluation、timestamped evidence notes 和公开 demo prompt set。当前 verified / candidate / rejected 状态保持不变，本项目仍不是本人 bot。

v0.4 入口：

- [Dual Agent Protocol](evals/dual-agent-protocol.md)
- [Evidence Map](references/evidence/zlf-evidence-map.csv)
- [Public Demo Prompts](examples/public-demo.md)

## 项目定位

本仓库用于研究周丽峰 / 峰哥亡命天涯公开内容中的观察视角、内容判断方式、表达 DNA、话题边界和反模式。它面向二创写作、内容选题分析、社会观察评论、采访视角拆解和争议事件分层分析。

这不是周丽峰本人项目，不是授权项目，不代表本人观点，也不用于生成本人声明。

## Model Status

当前 `SKILL.md` 将模型分成三类：

- verified：`底层现场主义`、`边缘样本优先`、`内容判断四问`
- candidate：`荒诞现实解构`、`采访中的弱控制`、`流量红线雷达`
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
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

GitHub Actions 会在 push 和 pull request 上运行同一组核心校验。

## Fidelity Evaluation

`tests/fidelity_cases.yaml` 包含 10 个结构化 fidelity cases，总分 100。`tests/safety_cases.yaml` 包含 12 个安全边界测试。`tests/run_fidelity_check.py` 只做静态规则检查，不调用外部 LLM API。

正式发布前仍需要人工双 Agent 检查和人类 reviewer 检查。通过阈值见 `FIDELITY.md`。

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
├── FIDELITY.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── LICENSE
├── quick_validate.py
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
│   ├── evidence_check.py
│   ├── quality_check.py
│   ├── source_index_check.py
│   └── transcript_cleaner.py
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

- 冒充周丽峰本人。
- 捏造本人观点或私人信息。
- 传播未证实隐私、人肉信息或网暴目标。
- 生成危险探险、违法边境行动、灰产接触、规避平台封禁指南。
- 生成露骨性内容。
- 大段搬运原视频逐字稿或长篇原文。
- 消费真实受访者苦难。

安全问题请参考 `SECURITY.md`。贡献请参考 `CONTRIBUTING.md`。

## Contributing

欢迎补充公开来源、研究摘要、评测用例和安全边界。贡献前请运行本地校验，并确保新增结论可以回到 source ID。

不接受未证实隐私、长篇搬运字幕/原文、冒充本人文案、危险行动指南、露骨内容、平台规避教程或无来源人格设定。

## Release Roadmap

- v0.3.0：发布前工程化，静态评测、CI、贡献和安全政策。
- v0.4.0：执行 dual Agent fidelity evaluation，补充 timestamped evidence notes，完善 candidate model 的逐段证据。
- v0.5.0：完成双 Agent fidelity evaluation 和人工 reviewer 审计。
- v1.0.0：达到发布阈值，冻结核心模型，开始接受兼容 runtime 的安装反馈。

## License

本仓库代码和原创文档使用 MIT License。被索引的公开视频、报道、访谈和平台内容版权归原权利人所有，本仓库只保存短摘要、出处和研究笔记。
