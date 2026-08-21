---
collection: banks
title: 'HSBC'
slug: hsbc
kind: group
region: GLOBAL
website: 'https://www.hsbc.com/'
status: published
origin: manual
---

{{Infobox bank}}

# HSBC

**HSBC** 是 Fluxa WikiCard 的银行集团词条。本页不直接挂信用卡；各市场发卡机构是子行，卡片通过 `bank` 关系挂到对应子行。检索路径是「集团 → 子行 → 信用卡」。

| 字段 | 值 |
| --- | --- |
| 类型 | 集团 |
| 地区 | GLOBAL · 全球 |
| 官网 | https://www.hsbc.com/ |
| 积分体系 | 各市场子行各自挂体系，集团页不挂 |
| 子行数 | 24 |
| 词条数 | 0（信用卡挂在子行） |

## 子行

下列页面都是本仓已经存在的 `hsbc-*` 词条（`kind: subsidiary`，`parent: hsbc`）。没有对应文件的市场不收录。

### CN

- [[banks:hsbc-china|HSBC CN]](./hsbc-china.md)

### GLOBAL

- [[banks:hsbc-expat|HSBC Expat]](./hsbc-expat.md)
- [[banks:hsbc-uruguay|HSBC UY]](./hsbc-uruguay.md)
- [[banks:hsbc-qatar|HSBC QA]](./hsbc-qatar.md)
- [[banks:hsbc-india|HSBC IN]](./hsbc-india.md)
- [[banks:hsbc-indonesia|HSBC ID]](./hsbc-indonesia.md)
- [[banks:hsbc-taiwan|HSBC TW]](./hsbc-taiwan.md)
- [[banks:hsbc-turkiye|HSBC TR]](./hsbc-turkiye.md)
- [[banks:hsbc-egypt|HSBC EG]](./hsbc-egypt.md)
- [[banks:hsbc-mexico|HSBC MX]](./hsbc-mexico.md)
- [[banks:hsbc-sri-lanka|HSBC LK]](./hsbc-sri-lanka.md)
- [[banks:hsbc-channel-islands-isle-of-man|HSBC CIIOM]](./hsbc-channel-islands-isle-of-man.md)
- [[banks:hsbc-australia|HSBC AU]](./hsbc-australia.md)
- [[banks:hsbc-bermuda|HSBC BM]](./hsbc-bermuda.md)
- [[banks:hsbc-united-kingdom|HSBC UK]](./hsbc-united-kingdom.md)
- [[banks:hsbc-philippines|HSBC PH]](./hsbc-philippines.md)
- [[banks:hsbc-vietnam|HSBC VN]](./hsbc-vietnam.md)
- [[banks:hsbc-united-arab-emirates|HSBC AE]](./hsbc-united-arab-emirates.md)
- [[banks:hsbc-malaysia|HSBC MY]](./hsbc-malaysia.md)
- [[banks:hsbc-malta|HSBC MT]](./hsbc-malta.md)

### HK

- [[banks:hsbc-macau|HSBC MO]](./hsbc-macau.md)
- [[banks:hsbc-hong-kong|HSBC HK]](./hsbc-hong-kong.md)

### SG

- [[banks:hsbc-singapore|HSBC SG]](./hsbc-singapore.md)

### US

- [[banks:hsbc-united-states|HSBC US]](./hsbc-united-states.md)

## 客户经理等级

[[products:hsbc-premier|HSBC Premier]](../products/hsbc-premier.md) 是集团统一的客户经理等级词条。

## 收录信用卡

集团词条不直接收录信用卡。要找卡，先进入上表对应市场子行。

## 别名

用于主仓库把计算器 issuer 字符串对齐到银行关系。裸 `HSBC` / `汇丰` 只指向本集团页，不指向 [[banks:hsbc-hong-kong|HSBC HK]](./hsbc-hong-kong.md)：

- `HSBC`
- `汇丰`

## 迁移备注

- Payload collection：`banks`
- slug：`hsbc`
- kind：`group`
- parent：（集团不填）
- 子行 frontmatter 写 `parent: hsbc`（slug 字符串）；Payload `Banks.parent` 为 relationship → `banks`

[[Category:银行]]
[[Category:全球]]
[[Category:汇丰]]
