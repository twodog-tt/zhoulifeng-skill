# zhoulifeng-skill

一个基于公开资料提炼的“峰哥亡命天涯式社会观察” Agent Skill。

## 项目定位

本仓库用于研究周丽峰 / 峰哥亡命天涯公开内容中的观察视角、内容判断方式、表达 DNA、话题边界和反模式。它面向二创写作、内容选题分析、社会观察评论、采访视角拆解和争议事件分层分析。

这不是周丽峰本人项目，不是授权项目，不代表本人观点，也不用于生成本人声明。

## 安装方法

手动安装到 Codex：

```bash
git clone git@github.com:twodog-tt/zhoulifeng-skill.git ~/.codex/skills/zhoulifeng-skill
```

也可以 clone 到 Claude、Cursor 或其他 Agent Skills 兼容目录。不同 runtime 的 skill 发现机制不同，请按对应工具文档放置。

如果你的 runtime 支持类似 `npx skills add` 的 GitHub repo 安装方式，可以尝试使用本仓库地址安装，但本项目不保证所有 runtime 都支持该命令。

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
├── LICENSE
├── agents/
│   └── openai.yaml
├── references/
│   ├── extraction-framework.md
│   ├── fidelity-scorecard.md
│   ├── source-index.csv
│   └── research/
│       ├── 01-primary-videos.md
│       ├── 02-interviews-and-longform.md
│       ├── 03-expression-dna.md
│       ├── 04-external-views-and-controversies.md
│       ├── 05-content-decisions-and-business.md
│       ├── 06-timeline.md
│       └── 07-safety-and-boundaries.md
├── scripts/
│   ├── quality_check.py
│   ├── source_index_check.py
│   └── transcript_cleaner.py
└── examples/
    ├── sample-prompts.md
    └── sample-conversations.md
```

## 调研方法

本项目只使用公开资料，包括公开视频、公开访谈、公开媒体报道、公开社交媒体动态、外部评论、争议事件报道和商业/MCN/内容决策资料。

来源可靠度分为：

- A：本人直接发布的视频、直播切片、采访原文、本人账号动态。
- B：权威媒体采访或报道。
- C：第三方评论、百科、论坛整理。
- D：无法交叉验证的传闻，不进入核心模型，只能进入“待验证”。

核心判断应能回到 `references/source-index.csv` 和 `references/research/` 找到证据。没有证据的判断只能标注为“候选”。

## 安全边界

本 Skill 不做：

- 冒充周丽峰本人。
- 捏造本人观点或私人信息。
- 传播未证实隐私、人肉信息或网暴目标。
- 生成危险探险、违法边境行动、灰产接触、规避平台封禁指南。
- 生成露骨性内容。
- 大段搬运原视频逐字稿或长篇原文。
- 消费真实受访者苦难。

## 贡献指南

欢迎补充公开来源和研究摘要。贡献时请：

1. 先把来源加入 `references/source-index.csv`。
2. 在对应 `references/research/*.md` 中写摘要、可提取模式、反例和不应进入 Skill 的内容。
3. 不提交长篇逐字稿、未授权搬运、私人信息或未经证实的传闻。
4. 运行校验：

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
```

## License

本仓库代码和原创文档使用 MIT License。被索引的公开视频、报道、访谈和平台内容版权归原权利人所有，本仓库只保存短摘要、出处和研究笔记。
