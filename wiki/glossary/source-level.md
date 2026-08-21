---
collection: posts
title: '来源等级'
slug: source-level
status: published
---

# 来源等级

Fluxa WikiCard 用 `sourceLevel` 表示一条信用卡事实的可信度。主站卡片详情会显示对应中文标签。

| 值 | 标签 | 含义 |
| --- | --- | --- |
| `S` | 官方来源 | 直接摘自发卡行产品页或条款，且日期仍有效 |
| `A` | 强来源 | 官方来源 + 至少一次交叉核对 |
| `B` | 已交叉核验 | 两个以上独立来源一致 |
| `C` | 待复核 | 从计算器卡册或公开列表生成，尚未人工核验 |
| `D` | 低置信 | 社区传闻、过期活动或无法复现 |

本仓生成的词条一律从 **C** 起。不要把计算器里的活动叠加默认当成 S。

另见来源 collection 的 `reliabilityLevel`：`primary` / `secondary` / `community` / `unverified`。卡片等级和来源等级可以不同：一篇 S 级卡片仍可附带 community 备注。

[[Category:术语]]
