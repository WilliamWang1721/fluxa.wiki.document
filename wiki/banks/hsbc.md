---
collection: banks
title: '汇丰 / HSBC'
slug: hsbc
kind: group
region: GLOBAL
website: 'https://www.hsbc.com/'
status: published
origin: manual
---

{{Infobox bank}}

# 汇丰 / HSBC

**汇丰 / HSBC** 是 Fluxa WikiCard 的银行集团词条。本页不直接挂信用卡；各市场发卡机构是子行，卡片通过 `bank` 关系挂到对应子行。检索路径是「集团 → 子行 → 信用卡」。

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

- [[banks:hsbc-china|汇丰中国]](./hsbc-china.md)

### GLOBAL

- [[banks:hsbc-expat|汇丰 Expat]](./hsbc-expat.md)
- [[banks:hsbc-uruguay|汇丰乌拉圭]](./hsbc-uruguay.md)
- [[banks:hsbc-qatar|汇丰卡塔尔]](./hsbc-qatar.md)
- [[banks:hsbc-india|汇丰印度]](./hsbc-india.md)
- [[banks:hsbc-indonesia|汇丰印度尼西亚]](./hsbc-indonesia.md)
- [[banks:hsbc-taiwan|汇丰台湾]](./hsbc-taiwan.md)
- [[banks:hsbc-turkiye|汇丰土耳其]](./hsbc-turkiye.md)
- [[banks:hsbc-egypt|汇丰埃及]](./hsbc-egypt.md)
- [[banks:hsbc-mexico|汇丰墨西哥]](./hsbc-mexico.md)
- [[banks:hsbc-sri-lanka|汇丰斯里兰卡]](./hsbc-sri-lanka.md)
- [[banks:hsbc-channel-islands-isle-of-man|汇丰海峡群岛及马恩岛]](./hsbc-channel-islands-isle-of-man.md)
- [[banks:hsbc-australia|汇丰澳大利亚]](./hsbc-australia.md)
- [[banks:hsbc-bermuda|汇丰百慕大]](./hsbc-bermuda.md)
- [[banks:hsbc-united-kingdom|汇丰英国]](./hsbc-united-kingdom.md)
- [[banks:hsbc-philippines|汇丰菲律宾]](./hsbc-philippines.md)
- [[banks:hsbc-vietnam|汇丰越南]](./hsbc-vietnam.md)
- [[banks:hsbc-united-arab-emirates|汇丰阿联酋]](./hsbc-united-arab-emirates.md)
- [[banks:hsbc-malaysia|汇丰马来西亚]](./hsbc-malaysia.md)
- [[banks:hsbc-malta|汇丰马耳他]](./hsbc-malta.md)

### HK

- [[banks:hsbc-macau|汇丰澳门]](./hsbc-macau.md)
- [[banks:hsbc-hong-kong|汇丰香港]](./hsbc-hong-kong.md)

### SG

- [[banks:hsbc-singapore|汇丰新加坡]](./hsbc-singapore.md)

### US

- [[banks:hsbc-united-states|汇丰美国]](./hsbc-united-states.md)

## 收录信用卡

集团词条不直接收录信用卡。要找卡，先进入上表对应市场子行。

## 别名

用于主仓库把计算器 issuer 字符串对齐到银行关系。裸 `HSBC` / `汇丰` 只指向本集团页，不指向汇丰香港：

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
