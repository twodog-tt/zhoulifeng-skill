# 贡献指南

感谢你愿意帮 `zhoulifeng-skill` 变得更可审计、更好用。

这个项目是一个授权维护的 Zhou Lifeng / 峰哥亡命天涯 style Skill，用于风格草稿、内容分析和社会观察写作。它不是峰哥本人实时声明生成器，也不能替代周丽峰本人亲自确认观点。

## 贡献前先确认

请先记住几条硬规则：

- 不冒充周丽峰本人。
- 不捏造本人观点、行踪、关系、承诺或争议回应。
- 不把 candidate model 写成 verified。
- 不加入私人授权材料、私聊、长字幕、隐私资料。
- 不削弱 hard safety boundaries。
- 不把项目描述成实时本人声明生成器。

## 如何新增来源

1. 在 `references/source-index.csv` 新增一行。
2. 字段必须沿用现有格式：

   ```text
   id,title,platform,type,date,url_or_locator,primary_or_secondary,reliability,notes,local_path
   ```

3. 日期无法确认时写 `unknown`，不要编造。
4. reliability 请诚实标注：
   - `A`：本人公开视频、本人公开访谈、本人账号公开内容等直接来源。
   - `B`：媒体采访、深度报道等二级但较可靠来源。
   - `C`：第三方评论、百科、论坛整理。
   - `D`：传闻、待验证线索，不能进入核心模型。
5. notes 写 1-2 句摘要即可，不要复制长文。

## 如何新增 research note

请更新 `references/research/` 下对应文件。

一条合格 research note 应该说明：

- 使用了哪些 source ID。
- 能支持什么观察。
- 不能支持什么结论。
- 存在哪些反例、限制或争议。
- 哪些内容不应进入 `SKILL.md`。

不要粘贴长访谈、长字幕、长文章摘录、私人信息或非公开聊天记录。

## 如何把 candidate model 提升为 verified

candidate model 只有在证据足够时才能升级。

最低要求：

- 至少两类来源支持，优先 A/B 级来源。
- 多个 `source-index.csv` source ID 可追溯。
- 有明确 failure mode。
- 在 `references/research/` 中写明限制或反例。
- 不与安全边界冲突。

升级模型状态时，必须同步更新：

- `SKILL.md`
- `FIDELITY.md`
- `tests/fidelity_cases.yaml`
- `tests/safety_cases.yaml` 或相关安全说明
- evidence / research 记录

评测通过、demo 很像、外部 reviewer 喜欢，都不能单独把 candidate 升级成 verified。

## 如何改进安全边界

欢迎提交安全边界改进。

常见改法：

- 在 `tests/safety_cases.yaml` 增加或改进测试。
- 在 `tests/expected_behaviors.md` 写清楚好答案和坏答案。
- 在 `SKILL.md` 补充更清晰的拒绝边界。
- 在 examples 中增加安全替代写法。

拒绝风格可以冷一点、短一点、少说教，但不能放松硬安全边界。

## 不接受的贡献

本项目不接受：

- 未证实隐私。
- 私聊、私人授权材料、电话号码、地址、身份证明等非公开材料。
- 长篇搬运字幕、访谈稿、文章、评论。
- 冒充周丽峰本人的文案。
- 把生成内容包装成峰哥刚刚确认的真实声明。
- 危险旅行、边境行动、灰产接触或违法指南。
- 平台封禁规避、审核绕过教程。
- 露骨内容。
- 人肉、网暴、挂人、羞辱真实个人。
- 无来源的人格设定。
- 把 candidate model 强行写成 verified。

## 提交前校验

提交 PR 前请至少运行：

```bash
python3 scripts/source_index_check.py
python3 scripts/quality_check.py
python3 quick_validate.py
python3 tests/run_fidelity_check.py
```

如果改了 docs、demo、review、source verification 或 archive 相关文件，请运行完整校验：

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

## PR 建议

PR 描述里请写清：

- 改了什么。
- 为什么改。
- 影响哪些模型、来源、边界或文档。
- 是否新增来源 ID。
- 是否涉及 candidate / verified 状态。
- 运行了哪些校验。

小改可以直接说明；涉及模型状态、安全边界、授权范围的改动，请尽量给出证据链和测试结果。
