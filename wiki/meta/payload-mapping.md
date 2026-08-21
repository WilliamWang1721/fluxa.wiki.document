---
collection: pages
title: 'Payload 字段对照'
slug: payload-mapping
status: published
---

# Payload 字段对照

目标主仓库：`WilliamWang1721/payload-website-starter`（Fluxa WikiCard）。生产域名：`https://fluxa.wiki`。

## Collection 对照

| 本仓目录 | Payload `slug` | 后台分组 |
| --- | --- | --- |
| `wiki/cards/` | `cards` | 玩卡百科 |
| `wiki/banks/` | `banks` | 玩卡百科 |
| `wiki/reward-programs/` | `reward-programs` | 玩卡百科 |
| `wiki/sources/` | `sources` | 玩卡百科 |
| `wiki/pages/` | `pages` | 页面 |
| `wiki/posts/` | `posts` | 文章 |
| `wiki/categories/` | `categories` | 分类 |
| （暂无） | `change-requests` | 玩卡百科 |
| （暂无） | `compare-parameters` / `card-parameter-values` | 玩卡百科 |

## 信用卡 `cards`

| Frontmatter | Payload 字段 | 说明 |
| --- | --- | --- |
| `title` | `title` | 信用卡名称 |
| `shortName` | `shortName` | 卡册简称 |
| `slug` | `slug` | URL |
| `country` | `country` | 市场，见 `cardCountryOptions` |
| `bank` | `bank` | relationship → `banks` |
| `rewardProgram` | `rewardProgram` | relationship → `reward-programs` |
| `issuance` | `issuance` | `issuing` 正在发行 / `discontinued` 已停发 / `legacy` 存量；未知则省略 |
| `sourceLevel` | `sourceLevel` | `S/A/B/C/D` |
| `_status` | `_status` | `draft` / `published` |
| `lastVerifiedAt` | `lastVerifiedAt` | 最后核验时间 |
| `rebateCalculator.*` | `rebateCalculator` | 返利计算器插件 |
| `conversionCalculator.*` | `conversionCalculator` | 兑换规则 |
| `tags` | `rebateCalculator.tags` | JSON 标签 |
| `relatedCards` | `relatedCards` | 相关信用卡 slugs |
| `sources` | `sources` | 来源 slugs |
| 正文 Markdown | `content` | Lexical richText |
| 首段引用 | `summary` | textarea 摘要 |

## 银行 `banks`

主仓库 `src/collections/Banks.ts` 与本仓 **同名、同语义**。集团 / 子行检索两边一起改。

| Frontmatter | Payload 字段 | 说明 |
| --- | --- | --- |
| `title` | `title` | 对外名称 |
| `slug` | `slug` | URL；集团用品牌短名（如 `hsbc`），子行带市场（如 `hsbc-hong-kong`） |
| `region` | `region`（`US/CN/HK/SG/GLOBAL`） | 集团常用 `GLOBAL` |
| `website` | `website` | 官网；集团用集团站，子行用当地信用卡列表 |
| `kind` | `kind`（select：`group` / `subsidiary`） | **独立银行省略**，缺省即普通 bank，保持兼容。不要发明第三种取值。 |
| `parent` | `parent`（relationship → `banks`） | **仅子行填写。** 本仓写集团 slug 字符串（如 `parent: hsbc`）；Payload 存指向集团文档的 relationship，语义相同。字段名必须是 `parent`，不要用 `group`。集团页和独立银行都不要填。 |

信用卡仍然挂在市场子行（或独立银行）上，不要把 `cards.bank` 指到 `kind: group` 的集团页。

## 积分体系 `reward-programs`

| Frontmatter | Payload 字段 |
| --- | --- |
| `title` | `title` |
| `slug` | `slug` |
| `bank` | `bank` |
| `region` | `region` |
| `currencyName` | `currencyName` |
| 首段 | `summary` |
| （未导出） | `transferPartners` |

## 来源 `sources`

| Frontmatter | Payload 字段 |
| --- | --- |
| `title` | `title` |
| `url` | `url` |
| `sourceType` | `sourceType` |
| `publisher` | `publisher` |
| `reliabilityLevel` | `reliabilityLevel` |
| 关联卡片列表 | `relatedCards` |

## 导入顺序

1. `banks`（先导入 `kind: group` 的集团，再导入带 `parent` 的子行，以便解析 relationship）
2. `reward-programs`（依赖银行）
3. `sources`
4. `cards`（依赖银行、积分体系、来源；`bank` 指向子行或独立银行，不要指向集团）
5. 回写 `cards.relatedCards` 和 `sources.relatedCards`
6. `pages` / `posts` / `categories`

导入后不要把计算器规则从 TypeScript 删掉，直到 Admin 里的 `rebateCalculator.calculatorId` 全部对得上。

[[Category:元文档]]
