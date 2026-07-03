# zhoulifeng-skill

[![Release](https://img.shields.io/github/v/release/twodog-tt/zhoulifeng-skill?label=release)](https://github.com/twodog-tt/zhoulifeng-skill/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Validate](https://github.com/twodog-tt/zhoulifeng-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/twodog-tt/zhoulifeng-skill/actions/workflows/validate.yml)

<p align="center">
  <img src="docs/assets/pixel-feng.png" alt="zhoulifeng-skill 像素头像" width="360">
</p>

一个授权维护的「峰哥亡命天涯 / 周丽峰」风格 Agent Skill，用来生成社会观察、内容选题分析、授权口吻草稿和争议事件分层分析。

它不是峰哥本人实时发言生成器，也不是官方在线人格 bot。模型输出不能替代周丽峰本人亲自确认的观点、承诺、行踪或争议回应。

## 当前状态

- 当前版本：`v1.0.0`
- 状态：稳定公开版
- GitHub Release：[`v1.0.0 - Stable Public Release`](https://github.com/twodog-tt/zhoulifeng-skill/releases/tag/v1.0.0)
- 最终 v1.0 审计：通过
- P0 / P1 / P2：`0 / 0 / 7`，剩余 P2 都是非阻塞的公开资产或发布流程优化

v1.0.0 是本项目第一个稳定公开版本。它包含证据索引、verified / candidate / rejected 模型分层、安全硬边界、公开 demo、自动校验、双 Agent 评测记录、人类审核记录、外部 reviewer 反馈记录、来源验证流程、打包流程和 final v1.0 audit。

这代表项目已经适合公开安装、审计和试用；但它不代表「完美还原」，不代表 broad external review 已经完成，也不代表可以生成实时本人声明。

## 快速入口

- [安装说明](docs/INSTALL.md)
- [公开发布说明](docs/LAUNCH.md)
- [发布素材](launch/README.md)
- [公开 Demo](examples/public-demo.md)
- [Demo 输出](examples/public-demo-outputs.md)
- [打包流程](docs/ARCHIVE_WORKFLOW.md)
- [证据地图](references/evidence/zlf-evidence-map.csv)
- [来源验证](references/source-verification/README.md)
- [外部评审](reviews/external/README.md)
- [最终 v1.0 审计](reviews/final-v1.0-audit.md)
- [v1.0.0 Release Notes](RELEASE_NOTES_v1.0.0.md)
- [授权说明](AUTHORIZATION.md)
- [运行环境兼容性](docs/RUNTIME_COMPATIBILITY.md)
- [安全政策](SECURITY.md)

## 这个项目是什么

这是一个授权风格 Skill，用公开资料、结构化证据和评测记录维护「峰哥亡命天涯 / 周丽峰」式社会观察能力。

它可以帮助你做：

- 峰哥式社会观察
- 短视频选题拆解
- 授权风格文案草稿
- 冷感、荒诞、现实感评论
- 采访角度生成
- 内容传播判断
- 网红、边缘样本、社会议题分析

它更像一个可审计的人物风格系统，不是简单复刻口头禅的玩具。

## 这个项目不是什么

它不是：

- 峰哥本人实时发言生成器
- 官方在线人格 bot
- 私人观点伪造器
- 争议回应编造器
- 危险旅行、灰产、边境行动指南
- 人肉、网暴、隐私曝光工具
- 露骨内容生成器
- 长字幕、长访谈、原文搬运仓库

授权允许更接近峰哥的语气、节奏、冷感、损劲和荒诞观察，但不允许虚构私人事实、实时行踪、真实承诺、未证实争议回应或危险操作细节。

## 核心边界

本项目的目标是「低道德说教感 + 高安全硬边界」。

允许：

- 更冷、更损、更现实的表达
- 指出人性里的贪、怂、装、骗、欲望、虚荣和流量算计
- 用不体面但不违法的方式拆解社会现象
- 在授权范围内生成更像峰哥口吻的草稿

禁止：

- 冒充周丽峰本人实时发言
- 捏造本人观点、行踪、关系、承诺或争议回应
- 传播隐私、传闻、人肉材料或网暴目标
- 提供危险旅行、边境行动、灰产、违法或平台规避指南
- 生成露骨内容
- 大段搬运原文、字幕、访谈稿
- 把真实受访者的苦难当作笑料消费

## 模型状态

`SKILL.md` 将模型分成三类。

verified：

- `底层现场主义`
- `边缘样本优先`
- `内容判断四问`

candidate：

- `荒诞现实解构`
- `采访中的弱控制`
- `流量红线雷达`
- `下三路牵引`
- `知识分子外衣 / 俗人落点`

rejected / unsafe：

- 把「自嘲式冒险人格」作为可激活人格
- 口头禅人格复刻
- 争议站队与封禁原因脑补
- 粗俗无限制化
- 低俗越界成露骨或人身羞辱

candidate 不能写成 verified。授权、评测通过或 demo 好看，都不能自动把 candidate 升级成 verified。

## 来源与授权状态

本项目按授权风格 Skill 维护。授权允许做风格草稿、内容分析和二创辅助，但不自动允许虚构私人事实、实时观点、真实承诺、行踪、关系或争议回应。

公开仓库不保存私人合同、私聊、签名、电话号码、地址或其他非公开授权材料。

当前公开证明状态：

- 私人授权材料不进入仓库。
- public proof 当前未包含在仓库里。
- 如果后续有公开授权声明，可以只链接或摘要，不暴露私人材料。

来源验证状态：

- Bilibili 等已记录公开来源可按 evidence map 使用。
- X `@zlf86` 当前仍是 `unverified`。
- X `@zlf86` 只能用于 `candidate_voice_calibration`，不能进入 verified models。

## 安装方法

安装到 Codex：

```bash
git clone git@github.com:twodog-tt/zhoulifeng-skill.git ~/.codex/skills/zhoulifeng-skill
```

也可以 clone 到 Claude、Cursor 或其他 Agent Skills 兼容目录。不同 runtime 的 skill 发现、frontmatter、工具调用和资源加载方式可能不同，本仓库不保证所有 runtime 完全兼容。

## 使用示例

```text
用峰哥式视角分析一下县城咖啡店变多。
```

```text
把「年轻人不想升职」这个选题改成峰哥亡命天涯式切口。
```

```text
给一个长期住青旅的自由职业者设计采访问题，要有峰哥式现实感。
```

```text
有人想人肉争议视频里的受访者，峰哥式怎么拒绝并转成围观机制分析？
```

更多公开 demo 见 [examples/public-demo.md](examples/public-demo.md)，对应输出见 [examples/public-demo-outputs.md](examples/public-demo-outputs.md)。

## 本地校验

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
python3 scripts/v1_plan_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

GitHub Actions 会在 push 和 pull request 上运行核心校验。

## 评测记录

项目包含：

- fidelity cases
- safety cases
- expected behaviors
- dual-Agent evaluation protocol
- scoring agent prompt
- answer agent prompt
- human reviewer checklist
- public demo outputs

已记录的重要评测：

- `v0.4-run-003`：授权 voice mode 双 Agent 评测通过，`100/100`
- `v0.7-run-001`：低体面 / 反 polished AI 口吻校准评测通过，`100/100`
- final v1.0 audit：archive content audit、install smoke test、public readability review 均通过

这些评测说明项目在测试面上表现合格，不等于完美保真。

## 打包

生成 v1.0.0 稳定包：

```bash
python3 scripts/create_release_archive.py --version v1.0.0
```

默认输出：

```text
dist/zhoulifeng-skill-v1.0.0.zip
```

`dist/` 被 `.gitignore` 忽略，不应提交。打包内容、排除项和发布前检查见 [docs/ARCHIVE_WORKFLOW.md](docs/ARCHIVE_WORKFLOW.md)。

## 贡献

贡献说明见 [CONTRIBUTING.md](CONTRIBUTING.md)。

原则很简单：

- 新增结论必须能回到公开来源。
- candidate 不得硬升 verified。
- 不加入私人材料、私聊、长字幕、隐私资料。
- 不削弱安全硬边界。
- 不把项目写成实时本人声明生成器。

## 安全

安全政策见 [SECURITY.md](SECURITY.md)。

如果发现冒充本人、隐私泄露、危险指南、灰产教程、露骨内容、平台规避、版权搬运或 candidate/verified 混淆，请开 issue 说明风险和更安全的替代方向。

## License

本项目使用 MIT License。英文法律正文见 [LICENSE](LICENSE)，其中附有中文参考译文。
