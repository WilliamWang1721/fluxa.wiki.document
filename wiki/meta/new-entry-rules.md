---
collection: pages
title: '词条新建规则'
slug: new-entry-rules
status: published
---

# 词条新建规则

本页是 **往本仓库新增或完善词条时必须遵守的规则**。编辑入口在仓库根目录 [README.md](../../README.md)。语法细节见 [[meta:syntax|Wiki 语法]](syntax.md)，字段含义见 [[meta:payload-mapping|Payload 字段对照]](payload-mapping.md)。

可复制的空白稿在 [`wiki/_templates/`](../_templates/)。

## 1. 先判断写哪一种词条

| 你要写的内容 | 写到 | Payload | 文件 |
| --- | --- | --- | --- |
| 一张具体的信用卡 / 签账卡 | 信用卡 | `cards` | `wiki/cards/{slug}.md` |
| 一家发卡机构、银行集团或市场子行 | 银行 | `banks` | `wiki/banks/{slug}.md` |
| RewardCash、Cash Dollars、Membership Rewards 等 | 积分体系 | `reward-programs` | `wiki/reward-programs/{slug}.md` |
| 官方产品页、条款、公告 URL | 来源 | `sources` | `wiki/sources/{slug}.md` |
| 关于、政策、编写约定 | 指南页 | `pages` | `wiki/pages/{slug}.md` |
| 攻略、说明文 | 文章 | `posts` | `wiki/posts/{slug}.md` |
| 一个概念（FTF、来源等级） | 术语 | （暂用 posts 口径） | `wiki/glossary/{slug}.md` |
| 一组同类词条的集合 | 分类 | `categories` | `wiki/categories/{name}.md` |

**一张卡不是一篇攻略。** 玩法、对比、怎么选卡写 `posts`；卡面事实写 `cards`。

**不要**把银行名单、卡片列表写进 React / 计算器 TypeScript。本仓和日后的 Payload 关系才是名单来源。

## 2. 新建顺序（有依赖，不可跳）

```
银行 banks
  → 积分体系 reward-programs（挂到银行）
    → 来源 sources（官方 URL）
      → 信用卡 cards（挂银行 + 积分体系 + 来源）
        → 回写索引、分类、relatedCards
```

- 银行已存在：从「来源 / 信用卡」开始。
- 若发卡机构属于集团：先建集团词条（`kind: group`），再建子行（`kind: subsidiary`，`parent` 指向集团 slug）。卡片挂子行，不挂集团。
- 积分计划是新的（例如新开的联名里数计划）：先建 `reward-programs`，再写卡。
- 指南、术语、政策没有这个依赖，可单独新增。

## 3. 所有词条都适用的硬规则

1. **一个 slug 一篇文件。** 文件名必须是 `{slug}.md`，且与 YAML 里的 `slug` 完全一致。
2. **slug 只用小写 ASCII 和短横线。** `hsbc-red-credit-card` 正确；`HSBC Red`、`汇丰-red`、`hsbc_red` 错误。
3. **标题只出现一次。** 正文第一个 `#` 标题等于 YAML `title`（不要再套一层不同的名字）。
4. **中文或含冒号的 YAML 值用单引号。** `title: '汇丰 Red 信用卡'`。
5. **关系字段只写 slug，不写中文名。** `bank: hsbc-hong-kong`，不是 `bank: 汇丰香港`。子行的 `parent: hsbc` 同样只写集团 slug。
6. **内部链接写两遍：** Wiki 链（给以后导入）+ Markdown 相对路径（给 GitHub 预览）。
7. **新建默认是未核验稿。** 信用卡：`sourceLevel: C`，`_status: draft`，`status: stub` 或 `drafting`。
8. **数字必须能点到来源。** 没有 URL 就不要写具体费率、倍数、迎新额。
9. **禁止**把 token、账号、未公开活动内部备忘写进词条。
10. **禁止**为了「刷新列表」再跑 `scripts/generate_wiki.py`。该脚本会删掉 `wiki/cards`、`banks`、`reward-programs`、`sources`、`categories` 后重生成，手写内容会丢。

### Slug 怎么取

| 类型 | 规则 | 好例子 | 坏例子 |
| --- | --- | --- | --- |
| 信用卡 | `{机构}-{产品}`，机构与银行 slug 前缀一致 | `hsbc-red-credit-card` | `red`、`汇丰red` |
| 银行（独立） | 机构常用英文名；单市场可带地区 | `hang-seng`、`bank-of-east-asia` | 用集团 slug 当某一市场的发卡行 |
| 银行（集团） | 品牌英文短名，不写市场 | `hsbc` | `hsbc-group`、`HSBC` |
| 银行（子行） | `{集团slug}-{市场}` | `hsbc-hong-kong`、`hsbc-china` | `hsbc`（分不清市场；集团页才用这个 slug） |
| 积分体系 | `{银行slug}-{货币名}` | `hsbc-rewardcash` | `rc`、`points` |
| 来源 | `{银行slug}-official-terms`；一张卡独有条款则 `{卡slug}-terms` | `hang-seng-official-terms` | `source-1` |
| 其它 | 英文短横线，与主站 URL 一致 | `how-to-contribute` | `如何编写` |

先在 GitHub 搜索 slug，确认文件还不存在，再新建。

### 链接写法（强制）

```md
[[banks:hsbc-hong-kong|汇丰香港]](../banks/hsbc-hong-kong.md)
[[cards:hsbc-red-credit-card|汇丰 Red 信用卡]](./hsbc-red-credit-card.md)
[[glossary:source-level|来源等级]](../glossary/source-level.md)
```

同目录用 `./`，跨目录用 `../{collection}/`。不要只写 `[[汇丰香港]]` 而不给 Markdown 链接——GitHub 点不开。

## 4. 信用卡 `cards`

**何时新建：** 主站或本仓还没有这张卡，或计算器里已有但 Wiki 漏了。

**何时改旧稿：** `wiki/cards/` 里已有 stub（当前绝大多数是这种情况）——不要另开一篇，直接改原文件。

### 必填 frontmatter

| 字段 | 规则 |
| --- | --- |
| `collection` | 必须 `cards` |
| `title` | 对外官方名，可中英混合 |
| `shortName` | 卡册 / 对比表用的短名，尽量短 |
| `slug` | 与文件名一致 |
| `country` | 市场代码，见下表 |
| `bank` | 已存在的银行 slug |
| `rewardProgram` | 已存在的积分体系 slug；确实没有则先去建 |
| `sourceLevel` | 新建用 `C` |
| `_status` | 新建用 `draft` |
| `status` | `stub`（骨架）/ `drafting`（正在补正文）/ `verified`（已对照官方核验） |
| `unionPay` | 有银联双币账户则为 `true` |
| `rebateCalculator.enabled` | 主仓库还没有插件就 `false` |
| `rebateCalculator.calculatorId` | 必须与主仓库选项完全一致；没有则留空并 `enabled: false` |
| `conversionCalculator.enabled` / `ruleId` | 同理；没有则 `false` / `null` |
| `tags` | 3～6 个短标签，便于检索 |
| `relatedCards` | 同银行其它卡 slug，建议 3～8 个 |
| `sources` | 至少一个条款 / 官方产品页 slug |

`country` 取值（与主仓库 `cardCountryOptions` 一致）：

`HK` `MO` `CN` `TW` `SG` `MY` `PH` `ID` `VN` `IN` `LK` `AU` `US` `UK` `AE` `QA` `EG` `TR` `MT` `MX` `BM` `UY` `IM_GG_JE` `EXPAT_JE`

银行 `region` 只有：`HK` `CN` `SG` `US` `GLOBAL`。澳门卡的 `country` 是 `MO`，银行 `region` 仍常用 `HK`。

### 正文结构（按这个顺序）

1. `{{Infobox card}}`
2. `# {title}`
3. `>` 摘要（对应 Payload `summary`，2～4 句，不写未核验倍数）
4. 信息框表格：官方名称、简称、市场、发卡银行、积分体系、来源等级、银联、计算器
5. `## 概述`
6. `## 积分与回赠`（有官方口径再写表；没有就写「待核验」）
7. `## 计算器接入`
8. `## 信息来源`
9. `## 相关词条`
10. `## 迁移备注`（collection + slug + 关系）
11. `[[Category:...]]` 至少：`信用卡`、`{市场}信用卡`、`{银行中文名}`；银联卡再加 `银联`

复制模板：[`wiki/_templates/card.md`](../_templates/card.md)

### 写完必须回写

- [ ] `wiki/banks/{bank}.md` 的「收录信用卡」
- [ ] `wiki/reward-programs/{program}.md` 的「使用该体系的信用卡」
- [ ] `wiki/cards/_index.md` 对应银行小节
- [ ] `wiki/sources/{source}.md` 的「关联信用卡」
- [ ] 同银行 1～2 篇旧卡的 `relatedCards`（可选但推荐）
- [ ] 分类页 `wiki/categories/`；没有就新建分类页

## 5. 银行 `banks`

**何时新建：** 出现本仓没有的发卡机构。一张新卡挂到已有银行时，**不要**新建银行。若该行属于某集团：先有集团词条，再写子行；信用卡仍挂子行，不挂集团页。

### 必填

| 字段 | 规则 |
| --- | --- |
| `collection` | `banks` |
| `title` | 对外中文名，如 `汇丰香港`；集团可用 `汇丰 / HSBC` |
| `slug` | 文件名。集团用不带市场的品牌短名；子行 `{集团slug}-{市场}` |
| `region` | `HK` `CN` `SG` `US` `GLOBAL` 之一；集团常用 `GLOBAL` |
| `website` | 信用卡产品列表页，优先官方；集团用集团官网 |

### 选填（集团 / 子行；独立银行不要填）

| 字段 | 规则 |
| --- | --- |
| `kind` | 集团 `group`；子行 `subsidiary`。独立银行**省略**，缺省即普通银行，旧词条不用改。取值只有这两个。 |
| `parent` | **仅子行。** 值为集团 slug，如 `parent: hsbc`。字段名必须是 `parent`，不要用 `group`。集团页和独立银行都不要填。导入 Payload 时变成 relationship → `banks`。 |

独立银行（不属于任何集团）保持合法：不写 `kind` / `parent` 即可。不要强迫每家银行都填集团。

正文用 `{{Infobox bank}}`。

- **独立银行 / 子行：** 必须有「收录信用卡」（新银行可先空列表）和「别名」（主仓库 issuer 字符串，如 `Hang Seng Bank`）。子行信息框加「所属集团」链接。
- **集团：** 必须有「子行」列表（只挂本仓已有页面，不编造市场）。集团页不直接挂信用卡。
- **别名：** 裸品牌名（`HSBC` / `汇丰`）只写在集团页。子行用带地区的写法（`HSBC HK`），避免和集团抢同一个 issuer 字符串。

分类：`[[Category:银行]]` 和地区分类；集团与子行可再加集团分类（如 `[[Category:汇丰]]`）。

回写：`wiki/banks/_index.md`——集团要出现在「按集团」节并展开子行；独立银行仍按地区列出。若该行同时会发卡，接着建积分体系。

模板：[`wiki/_templates/bank.md`](../_templates/bank.md)

## 6. 积分体系 `reward-programs`

**何时新建：** 该行出现新的积分货币或独立计划（例如新的航司联名里数池）。同一行多张卡共用一个体系时，**共用一篇**，不要每张卡一个体系。

### 必填

| 字段 | 规则 |
| --- | --- |
| `bank` | 所属银行 slug |
| `region` | 与银行一致 |
| `currencyName` | 对外单位名，如 `RewardCash`、`Cash Dollars` |
| 首段 | 简介，对应 Payload `summary` |

转点伙伴写在 `## 转点伙伴` 表（`伙伴 / 比例 / 来源`）。没有核验过就不要编造比例。

回写：`wiki/reward-programs/_index.md`，以及银行页信息框里的「积分体系」链接。

模板：[`wiki/_templates/reward-program.md`](../_templates/reward-program.md)

## 7. 来源 `sources`

**何时新建：** 有新的可引用 URL。同一 URL 只建一篇来源，多张卡共用。

### 必填

| 字段 | 允许值 |
| --- | --- |
| `url` | 完整 `https://` 链接，不要短链 |
| `sourceType` | `official` `terms` `news` `community` `internal` |
| `publisher` | 发布方，通常是银行中文名 |
| `reliabilityLevel` | `primary` 官方现页；`secondary` 条款摘要/转载；`community` 论坛；`unverified` 来路不明 |

卡片上的 `sourceLevel` 和来源上的 `reliabilityLevel` 不是一回事：一张 `C` 级卡也可以先挂 `primary` 来源，等有人对照条款后再把卡升到 `A`/`S`。

回写：被引用卡片 frontmatter 的 `sources` 列表，以及来源页「关联信用卡」。

模板：[`wiki/_templates/source.md`](../_templates/source.md)

## 8. 指南页 / 文章 / 术语 / 分类

| 类型 | 目录 | `collection` | 注意 |
| --- | --- | --- | --- |
| 指南、政策 | `wiki/pages/` | `pages` | 政策页 `status: published`；写完加入 `wiki/pages/_index.md` 和 `_Sidebar.md` |
| 说明/攻略 | `wiki/posts/` | `posts` | 不要把单卡事实只写在攻略里而不写卡片词条 |
| 术语 | `wiki/glossary/` | `posts` | slug 用英文；加入 `wiki/glossary/_index.md` |
| 分类 | `wiki/categories/` | `categories` | 文件名可以是中文，与 `[[Category:名称]]` 一致 |

指南模板：[`wiki/_templates/page.md`](../_templates/page.md)

## 9. 完善已有 stub（比新建更常见）

当前 `wiki/cards/` 里大部分是生成稿。编辑它们时：

1. 不要改 `slug`、`bank`、文件名（改了等于拆词条，导入会重复）。
2. 把 `status` 从 `stub` 改为 `drafting`，开始补摘要和来源。
3. 对照官方条款后：填写 `lastVerifiedAt: YYYY-MM-DD`，按 [[glossary:source-level|来源等级]](../glossary/source-level.md) 升级，必要时把 `_status` 改为 `published`。
4. 用官方摘要替换生成器那句「按计算器口径收录……」，但**不要删** frontmatter 里的 `calculatorId`。
5. 信息框表格和 YAML 必须一起改，避免一个写 Red、一个还写旧名。

## 10. 文风

- 先事实，后玩法。玩法放到 `posts` 或概述末段，并标明「非官方」。
- 不写「值得申请」「神卡」这类评价。
- 限时活动：写活动名 + 结束条件 + 来源；**不要**写进默认回赠口径表。
- `title` 用官方对外名，`shortName` 用口语短名。
- 费用、FTF、迎新一律写「以官方价目表为准」，有数字就挂来源。

## 11. 提交前清单

- [ ] 文件名 = `slug` + `.md`
- [ ] 依赖的银行 / 积分体系 / 来源文件已存在
- [ ] 每条 `[[collection:slug|标题]]` 都带可点的 `(相对路径)`
- [ ] 信用卡已回写银行页、积分体系页、`cards/_index.md`、来源页、分类
- [ ] 没有把未核验倍数写进默认口径
- [ ] 没有运行 `generate_wiki.py`
- [ ] commit 说明写清：`Add card: {slug}` 或 `Fill stub: {slug}`

## 12. 最小实例：新增一张已有银行的香港卡

假设要为恒生补一张本仓没有的卡，银行 `hang-seng` 和积分 `hang-seng-points` 已存在。

1. 复制 [`wiki/_templates/card.md`](../_templates/card.md) → `wiki/cards/hang-seng-example-card.md`
2. 若条款 URL 是新的：复制 [`wiki/_templates/source.md`](../_templates/source.md) → `wiki/sources/hang-seng-example-card-terms.md`
3. 填卡的 YAML：`bank: hang-seng`，`rewardProgram: hang-seng-points`，`country: HK`
4. 在 `wiki/banks/hang-seng.md`、`wiki/reward-programs/hang-seng-points.md`、`wiki/cards/_index.md` 的「恒生银行」节各加一行链接
5. 在 `wiki/categories/恒生银行.md` 和 `wiki/categories/香港信用卡.md` 加一行
6. 提交

[[Category:元文档]]
[[Category:指南]]
