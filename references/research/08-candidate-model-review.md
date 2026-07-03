# Candidate Model Review

本文件审查 v0.5 阶段仍为 candidate 的模型。默认不升级，除非 evidence map 中的 A/B 级证据足以证明稳定机制、可复现表达方式和反例边界。

## Review Inputs

- `references/evidence/zlf-evidence-map.csv`
- `references/evidence/notes/`
- `references/source-index.csv`
- `SKILL.md`

## 荒诞现实解构

### Current Status

candidate

### Supporting Evidence

- `ZLF-A003`：病痛和出租屋题材具有现实反差，但 evidence row 标为 `unclear`，主要强化边界而非稳定表达机制。
- `ZLF-A007`：从网管到高收入再到虚无的经历跨度提供强反差题材线索，evidence row 标为 `supporting / medium`。
- `ZLF-A010`：战争和平民题材具有强现实张力，但当前主要支持底层现场主义和危险题材边界。
- `ZLF-A011`：公开访谈标题中的镜头形象与普通人反差提供线索，evidence row 标为 `unclear / low`。
- `ZLF-B001`：媒体采访标题和摘要提示内容意义、收益和生产张力，可作为外部线索。

### Missing Evidence

- 缺少可复核的短片段摘要和时间点来证明稳定句式、节奏、冷幽默和荒诞机制。
- 缺少多个不同题材中的相同表达机制对照。
- 缺少明确反例，说明哪些公开视频只做纪实观察而不使用荒诞解构。
- 缺少本人公开解释“为什么这样处理反差”的直接材料。

### Counterexamples / Limitations

- 病痛、战争、贫困和孤独可以有现实反差，但不能被自动写成笑点。
- 题材本身荒诞不等于表达机制稳定。
- 不能依赖“看起来像峰哥”或授权口吻通过来升级模型。
- 授权只改变可用口吻强度，不改变证据等级。

### Upgrade Criteria

- 至少 3 条 A/B 级来源有短摘要或 timestamp，能显示相似的荒诞表达机制。
- 至少覆盖 2 种以上题材类型，例如底层劳动、城市空间、危险题材、访谈长文。
- 至少 1 个反例说明边界：哪些题材应保持克制，不进入荒诞化。
- 结论必须能回到 `zlf-evidence-map.csv` 的 evidence rows。

### v0.5 Decision

remain candidate

理由：v0.5 新增 evidence rows 增强了题材反差证据，但仍缺少逐段表达机制和反例对照，不足以升级为 verified。

## 采访中的弱控制

### Current Status

candidate

### Supporting Evidence

- `ZLF-A005`：人物关系链和访谈样本提示受访者经历可能承担叙事推进，evidence row 标为 `unclear / medium`。
- `ZLF-A006`：以“保安老刘的一天”观察日常节奏，支持人物和日常推进，但不是逐段问答证据。
- `ZLF-A011`：公开访谈可为镜头前后关系和表达方式提供线索，evidence row 标为 `unclear / medium`。
- `ZLF-A013`：乌克兰前线访谈材料可能呈现经历解释和叙事节奏，evidence row 标为 `unclear / low`。

### Missing Evidence

- 缺少逐段问答分析，无法确认创作者是否持续少下结论、让受访者自我呈现。
- 缺少对不同采访对象的对照，无法证明这是稳定方法而非单个题材自然形成。
- 缺少保护性提问案例，尤其是病痛、创伤、危险经历、灰色题材中的边界处理。
- 缺少弱控制失效或不适用场景的反例。

### Counterexamples / Limitations

- 出现人物讲述不等于采访方法已验证。
- 创伤、隐私、未成年人、违法风险、危险行动题材不能弱控制到失去保护。
- 采访中的弱控制不是放弃事实核查，也不是不设边界。
- 授权口吻更强不代表可以替受访者编经历。

### Upgrade Criteria

- 至少 3 条 A/B 级采访或人物叙事来源有逐段短摘要。
- 至少 2 种人物类型或题材类型能显示相同采访机制。
- 至少 1 个保护性边界案例和 1 个不适用场景。
- 每条结论能回到 evidence map 的 `source_id` 和 `timestamp_or_section`。

### v0.5 Decision

remain candidate

理由：v0.5 增加了 A005、A011、A013 的候选线索，但多数证据仍是标题/题材级或未逐段化，不能证明稳定采访方法。

## 流量红线雷达

### Current Status

candidate

### Supporting Evidence

- `ZLF-A008`：妙瓦底相关高风险题材支持传播张力和安全红线研究，evidence row 标为 `boundary / medium`。
- `ZLF-A009`：乌克兰险些被绑架叙事支持危险现场边界研究，evidence row 标为 `boundary / medium`。
- `ZLF-A010`：战区平民题材同时具有传播张力和高安全风险，evidence row 标为 `boundary / medium`。
- `ZLF-A013`：乌克兰前线访谈材料支持危险经历公开叙述边界和安全降级要求，evidence row 标为 `boundary / medium`。
- `ZLF-B001`：媒体采访可支持内容意义、收益和传播张力线索，但 evidence row 仍为 `unclear / low`。

### Missing Evidence

- 缺少可访问的 A/B 级平台动作证据。
- 缺少本人关于平台红线、内容限度和风险判断的稳定自述。
- 缺少被主动放弃、远程替代或安全降级的具体选题案例。
- 缺少平台外部动作与内容判断之间的可验证关联。

### Counterexamples / Limitations

- 高风险题材存在不等于鼓励高风险行动。
- 高传播张力不等于可以推断平台内部判断。
- 当前证据不能支持封禁原因、规避规则策略或对抗平台审核。
- `ZLF-D001` 仍是 D 级待验证线索，不进入核心模型。

### Upgrade Criteria

- 至少 3 条 A/B 级来源能显示明确的内容风险判断，而非仅仅出现高风险题材。
- 至少 1 条可靠来源显示安全降级、放弃实地行动或公开解释平台尺度。
- 至少 1 个反例说明“有流量但不应做/不能做”的边界。
- 不依赖 C/D 来源和推测平台内部原因。

### v0.5 Decision

remain candidate

理由：v0.5 增强了危险题材边界证据，但仍缺少平台动作、本人稳定自述和安全降级案例，不得升级为 verified。

## Overall v0.5 Decision

三个 candidate models 均保持 candidate：

- 荒诞现实解构：remain candidate
- 采访中的弱控制：remain candidate
- 流量红线雷达：remain candidate

本轮只增强证据深度和审计可追溯性，不改变 `SKILL.md` 的核心模型状态。
