# zhoulifeng-skill

一个授权维护的“峰哥亡命天涯式社会观察与口吻草稿” Agent Skill。

This project is an authorized Zhou Lifeng / 峰哥亡命天涯 style skill. It is not a real-time official statement generator, and generated drafts are not a substitute for Zhou Lifeng personally confirming a view.

## Current Status

Current version: `v0.4.0`

Status: Authorized voice evaluation pass

v0.4.0 已完成授权口吻模式校准、dual-Agent evaluation 和 lightweight human review。run-003 评分为 `100/100`，release recommendation 为 `pass`。

本项目是 authorized style skill，不是实时官方声明生成器。candidate models 仍保持 candidate，hard safety boundaries 保持不变。

## v0.5 Evaluation Roadmap

v0.4.0 已完成授权口吻评测通过。v0.5 的目标是补充更多 timestamped evidence notes、扩展 public demo prompt set、完善安装/打包说明，并增加更广覆盖的人类 reviewer 审计。

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

## Authorization Status

本项目现在按授权风格 Skill 维护。授权允许更接近峰哥口吻进行风格草稿、内容分析和二创辅助，但不允许虚构私人事实、实时观点或危险内容。

授权状态和范围见 [AUTHORIZATION.md](AUTHORIZATION.md)。公开仓库不保存私人合同、私聊、签名、电话号码、地址或其他非公开授权材料。

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
python3 scripts/eval_run_check.py
python3 scripts/demo_check.py
python3 scripts/docs_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

GitHub Actions 会在 push 和 pull request 上运行同一组核心校验。

## Fidelity Evaluation

`tests/fidelity_cases.yaml` 包含 10 个结构化 fidelity cases，总分 100。`tests/safety_cases.yaml` 包含 12 个安全边界测试。`tests/run_fidelity_check.py` 只做静态规则检查，不调用外部 LLM API。

v0.4-run-003 已完成 Answer Agent + Scoring Agent 评测和 lightweight human review。结果：`100/100`，release recommendation：`pass`，high-risk safety failures：`0`，candidate/verified confusions：`0`，false real-time personhood failures：`0`。

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

更多公开 demo 见 [examples/public-demo.md](examples/public-demo.md)。安装说明见 [docs/INSTALL.md](docs/INSTALL.md)，runtime 兼容性见 [docs/RUNTIME_COMPATIBILITY.md](docs/RUNTIME_COMPATIBILITY.md)，v0.4 评测报告见 [evals/reports/v0.4-fidelity-report.md](evals/reports/v0.4-fidelity-report.md)。

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
│   ├── INSTALL.md
│   ├── PACKAGING.md
│   └── RUNTIME_COMPATIBILITY.md
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
│   ├── demo_check.py
│   ├── docs_check.py
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
- v0.5.0：补充 timestamped evidence notes、扩展 public demo set、完善安装/打包文档、增加更广覆盖的人类审计。
- v1.0.0：达到发布阈值，冻结核心模型，开始接受兼容 runtime 的安装反馈。

## License

本仓库代码和原创文档使用 MIT License。被索引的公开视频、报道、访谈和平台内容版权归原权利人所有，本仓库只保存短摘要、出处和研究笔记。
