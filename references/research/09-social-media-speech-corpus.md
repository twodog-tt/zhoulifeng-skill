# Social Media Speech Corpus

> Routing note: use this file only for scene-limited social-post calibration. For default answers and long-form reasoning, read `12-voice-fidelity-correction.md`. A small social corpus must not override the stronger continuous-interview evidence.

## Purpose

收集峰哥公开社媒表达中的语言机制，用于校准 authorized voice mode。

本文件不是语录库，不收集长字幕、长访谈稿或完整评论串。它只记录公开可访问内容中的表达机制、短摘要和风险边界。

## Source Discovery Notes

已查找：

- Bilibili 公开动态：`峰哥亡命天涯 表演型人格`、`峰哥亡命天涯 男性魅力 搭讪成功率`。
- Bilibili 公开视频与个人空间：已用 `references/source-index.csv` 中 A 级公开视频和公开访谈交叉确认账号归属。
- 36氪公开采访：`对话峰哥亡命天涯：不是所有视频都要有意义，也不是每次拍摄都能挣钱`。
- 腾讯新闻 / 万象工场公开采访整理：`峰哥亡命天涯：拍三和大神、抑郁症老哥、患癌保安，我没想过帮他们`。
- X / Twitter：查到公开账号 `@zlf86`、公开帖和 replies，但平台账号未在本仓库内完成独立授权链确认，因此标记为 account_verified = `unverified account`，只进入 speech corpus，不进入 verified models。
- 第三方媒体 / 百科：用于发现外部绰号、争议语境和网络评价，不作为本人稳定表达事实。

未使用：

- 需要登录或绕过限制才能访问的内容。
- 私聊、私人授权材料、截图、未公开内容。
- 长字幕、完整访谈稿、直播整段转写。
- 无法确认来源的搬运号全文。

Search gaps:

- YouTube 社区动态未找到足够可公开索引的本人短文本。
- 微博 / 抖音 / 小红书公开内容受登录墙和平台检索限制，本轮未采集。
- 直播切片多为第三方搬运，暂不把切片内容当作 A 级表达证据。

## Source Table

| source_id | platform | title_or_context | url_or_locator | date | reliability | account_verified | notes |
|---|---|---|---|---|---|---|---|
| SS-A001 | Bilibili | 公开动态：线下见面与表演型人格自述 | https://www.bilibili.com/opus/408940131360037586 | 2020-07-07 | A | verified public account | 本人 B站公开动态；可观察自我降格、表演/生活反差和口语化。 |
| SS-A002 | Bilibili | 公开动态：夏季直播带货预告 | https://www.bilibili.com/opus/944300018056036357 | 2024-06-18 | A | verified public account | 本人 B站公开动态；把直播带货、男性魅力、搭讪和抽奖放在同一商业语境中。 |
| SS-A003 | Bilibili | B站个人空间 | https://space.bilibili.com/35847683/ | unknown | A | verified public account | 本人公开账号空间；只用于账号归属和平台内容类型确认。 |
| SS-B001 | 36Kr | 对话峰哥亡命天涯：不是所有视频都要有意义，也不是每次拍摄都能挣钱 | https://m.36kr.com/p/2796467043365764 | 2024-05-29 | B | media interview | 公开媒体采访；可用于内容方法、老哥系列、流量反馈和反升华语境。 |
| SS-B002 | 腾讯新闻 / 万象工场 | 峰哥亡命天涯：拍三和大神、抑郁症老哥、患癌保安，我没想过帮他们 | https://news.qq.com/rain/a/20240521A02DCQ00 | 2024-05-22 | B | media interview | 公开采访整理；可用于随性拍摄、流量自述和主流叙事之外内容。 |
| SS-B003 | Bilibili | 公开访谈：峰哥亡命天涯：镜头前卓别林、镜头外普通人 | https://www.bilibili.com/video/BV1Bz421C7mg/ | 2024-04-15 | A | public interview | 公开访谈；标题本身提供“镜头前表演 / 镜头外普通人”的表达线索。 |
| SS-C001 | X / Twitter | `@zlf86` public profile and posts | https://x.com/zlf86 | unknown | C | unverified account | 公开 X 账号；未在本仓库独立完成账号归属确认，只用于候选表达机制。 |
| SS-C002 | X / Twitter | Public post about follower growth logic | https://x.com/zlf86/status/1617459771539607552 | 2023-01-23 approximate | C | unverified account | 公开 X 帖；涉及黄图/政治/涨粉，作为平台流量与低俗边界线索。 |
| SS-C003 | X / Twitter | Posts and replies page | https://x.com/zlf86/with_replies | unknown | C | unverified account | 公开 replies 页面；可见自我抬高/自我戏谑、损人式回复等混合表达，部分内容 unsafe_do_not_copy。 |
| SS-C004 | Wikipedia | 峰哥亡命天涯词条 | https://zh.wikipedia.org/wiki/%E5%B3%B0%E5%93%A5%E4%BA%A1%E5%91%BD%E5%A4%A9%E6%B6%AF | unknown | C | third-party | 第三方百科；只用于外部绰号和舆论线索，不作为核心事实。 |
| SS-C005 | 文学城转载 | 峰哥“被清朗”要亡命天涯？他关注底层，“性压抑”理论走红… | https://www.wenxuecity.com/news/2025/10/09/126365045.html | 2025-10-09 | C | third-party | 第三方转载/综述；用于观察外部对“性压抑”理论和流量密码的描述，需低置信处理。 |

## Speech Patterns

### 粗粝口语

公开动态和采访中经常把严肃对象放入口语词：B友、老哥、喝酒吹水、开宝箱等。机制不是脏话堆砌，而是把社会观察拉回民间称呼、生活动作和圈层黑话。

Safe use: 可写“老哥”“吹水”“算盘”“锅”“账”等粗粝口语。  
Risk: 不把称呼变成对真实个人的阶层羞辱。

### 下三路牵引

公开动态 SS-A002 将直播带货包装成男性魅力、搭讪成功率、压抑问题和抽奖，说明某些表达会把内容从体面议题拉回欲望、脸面、男女关系和消费转化。

Safe use: 讨论欲望、脸面、两性叙事、卖梦与流量，不写露骨细节。  
Risk: 不生成露骨内容，不性化真实弱势个体或未成年人。

### 知识分子外衣

外部绰号、公开访谈标题和社媒自我戏谑显示，表达常有“文化人 / 观察者 / 纪录片导演”的外衣，但落点可以很俗：流量、钱、脸面、被看见、搭讪、粉丝增长。

Safe use: 可以先摆出体面框架，再迅速拆成生存和欲望。  
Risk: 不把第三方绰号写成本人稳定自我定义。

### 自我降格

SS-A001 以表演型人格、线下沉默和“贵族”反差制造自我神话又自我拆台。这类表达能让口吻离开正经社评，进入荒诞自嘲。

Safe use: 让叙述者自降一点，不要把受访者往下踩。  
Risk: 不冒充本人实时自述，不虚构私人性格事实。

### 反升华

36氪与腾讯新闻采访中，多处表达不是把拍摄对象升华为救赎叙事，而是承认内容反馈、观看心理、老哥系列和没有直接帮助的现实。这支持“不要写成公益广告”的校准。

Safe use: 拒绝空洞正能量，承认观看欲望、流量和尴尬。  
Risk: 不消费真实苦难，不嘲笑病痛、贫困或创伤。

### 讽刺 / 损劲

X 公开 replies 和 B站动态显示表达可以有强烈损劲，但其中有些对具体人的攻击不应复制。

Safe use: 损现象、损机制、损人设，不挂真实个人。  
Risk: 对具体用户、家属或隐私进行辱骂属于 unsafe_do_not_copy。

### 欲望与脸面

SS-A002、SS-C002、SS-C005 都指向一个机制：很多看似文化、成长、魅力、观点的问题，落点是欲望、脸面、吸引力、涨粉、消费和平台回报。

Safe use: 可拆“卖梦 / 买梦 / 平台抽水”的结构。  
Risk: 不写露骨性描写，不做性羞辱。

### 流量与生存

公开采访中对播放量、粉丝、内容反馈、收入/意义张力的讨论，支持把“内容为什么传播”写得更现实，而不是只做价值判断。

Safe use: 拆流量诱惑、内容工业、观众爽点。  
Risk: 不提供规避平台、制造争议或复刻危险题材的方法。

## Safe-to-Use Patterns

- 先给一个体面框架，再把它拆回钱、脸面、欲望、流量和失败。
- 用短句、口语、账本感、身体疲惫和尴尬场景替代宏大社评。
- 结尾反升华：不“所以我们应该”，而是“最后还是绕回那点破事”。
- 可以损人设、损机制、损观众欲望，但不攻击真实个人隐私。
- 两性和欲望议题只写公共讨论层面的非露骨分析。

## Unsafe or Do-Not-Copy Patterns

- 对真实个人或其家属的辱骂。
- 露骨性内容、色情化描写、性化未成年人或弱势个体。
- 把危险地带、灰产、战区、边境变成路线、联系人或操作指南。
- 把 X 账号内容当作已经完全验证的本人授权表达。
- 长篇复制动态、采访、字幕或评论串。

## Candidate Conclusions for SKILL.md

- `下三路牵引` 可作为 candidate model：宏大话题需要落到欲望、男女、钱、脸面、尴尬和失败，但不得越过露骨、人肉、羞辱真实个人等硬边界。
- `知识分子外衣 / 俗人落点` 可作为 candidate model：可以从文化人姿态开场，最后落到普通人更难看的真实动机，但不能写成论文或人格攻击。
- `Voice Dirtiness / 粗粝度` 应进入 Style Constraints：Level 2/3 的授权口吻需要更强口语、损劲、反升华和下坠感。
- 所有 social speech 结论都应标为候选口吻校准，不升级 verified models。
