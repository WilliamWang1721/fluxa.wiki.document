---
collection: banks
title: '银行中文名'
slug: replace-bank-slug
region: HK
# 集团：kind: group（不要写 parent）
# 子行：kind: subsidiary 且 parent: replace-group-slug
# 独立银行：不要写 kind / parent，缺省即普通银行
website: 'https://example.com/'
status: stub
origin: manual
---

{{Infobox bank}}

# 银行中文名

**银行中文名** 是 Fluxa WikiCard 的银行词条。信用卡必须通过 `bank` 关系挂到本页，不要靠标题模糊匹配。

| 字段 | 值 |
| --- | --- |
| 地区 | HK · 香港 |
| 类型 | 独立银行 |
| 所属集团 | （独立银行与集团页留空；子行写 [[banks:replace-group-slug|集团名]](./replace-group-slug.md)） |
| 官网 | https://example.com/ |
| 积分体系 | [[reward-programs:replace-program-slug|积分体系名]](../reward-programs/replace-program-slug.md) |
| 词条数 | 0 |

独立银行可删「类型 / 所属集团」两行。集团页把类型改成「集团」，并改「收录信用卡」为「子行」列表。子行把类型改成「子行」，所属集团必须可点。

## 收录信用卡

- （新建银行时可先留空，有卡之后按标题排序追加）

## 别名

主仓库计算器 `issuer` 可能出现的写法：

- `English Issuer Name`
- `银行中文名`

裸品牌名（如 `HSBC` / `汇丰`）只写在集团页。子行用带地区的别名（如 `HSBC HK`）。

## 迁移备注

- Payload collection：`banks`
- slug：`replace-bank-slug`
- 集团：YAML `kind: group`；Payload `kind` 为 select
- 子行：YAML `kind: subsidiary`，`parent: {集团slug}`；Payload `parent` 为 relationship → `banks`
- 独立银行：不写 `kind` / `parent`

[[Category:银行]]
[[Category:香港]]
