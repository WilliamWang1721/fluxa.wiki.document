#!/usr/bin/env python3
"""Generate Fluxa WikiCard markdown entries from the Payload starter data files.

This is a staging wiki: article bodies live here as Markdown + wiki syntax so they
can later be imported into payload-website-starter collections (cards, banks,
reward-programs, sources, pages, posts).
"""

from __future__ import annotations

import re
import shutil
from collections import defaultdict
from datetime import date
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
PAYLOAD = Path(os.environ.get("PAYLOAD_STARTER", "/tmp/payload-website-starter"))
TODAY = date.today().isoformat()

COUNTRY_LABELS = {
    "AE": "阿联酋",
    "AU": "澳大利亚",
    "BM": "百慕大",
    "CN": "中国内地",
    "EG": "埃及",
    "EXPAT_JE": "HSBC Expat / 泽西离岸",
    "HK": "香港",
    "ID": "印度尼西亚",
    "IM_GG_JE": "海峡群岛及马恩岛",
    "IN": "印度",
    "LK": "斯里兰卡",
    "MO": "澳门",
    "MT": "马耳他",
    "MX": "墨西哥",
    "MY": "马来西亚",
    "PH": "菲律宾",
    "QA": "卡塔尔",
    "SG": "新加坡",
    "TR": "土耳其",
    "TW": "台湾",
    "UK": "英国",
    "UY": "乌拉圭",
    "US": "美国",
    "VN": "越南",
    "GLOBAL": "全球",
}

REGION_FROM_COUNTRY = {
    "CN": "CN",
    "HK": "HK",
    "MO": "HK",
    "SG": "SG",
    "US": "US",
}

ISSUER_BANKS = {
    "HSBC Hong Kong": {
        "slug": "hsbc-hong-kong",
        "title": "汇丰香港",
        "region": "HK",
        "website": "https://www.hsbc.com.hk/credit-cards/products/",
        "aliases": ["HSBC HK", "汇丰香港", "HSBC"],
    },
    "Hang Seng Bank": {
        "slug": "hang-seng",
        "title": "恒生银行",
        "region": "HK",
        "website": "https://www.hangseng.com/en-hk/personal/cards/",
        "aliases": ["恒生银行", "Hang Seng"],
    },
    "CCB (Asia)": {
        "slug": "ccb-asia",
        "title": "建行亚洲",
        "region": "HK",
        "website": "https://www.asia.ccb.com/",
        "aliases": ["建行亚洲", "China Construction Bank (Asia)"],
    },
    "CMB Wing Lung Bank": {
        "slug": "cmb-wing-lung",
        "title": "招商永隆银行",
        "region": "HK",
        "website": "https://www.cmbwinglungbank.com/",
        "aliases": ["招商永隆银行"],
    },
    "BOC Hong Kong": {
        "slug": "boc-hong-kong",
        "title": "中银香港",
        "region": "HK",
        "website": "https://www.bochk.com/",
        "aliases": ["中银香港", "Bank of China (Hong Kong)"],
    },
    "Bank of East Asia": {
        "slug": "bank-of-east-asia",
        "title": "东亚银行",
        "region": "HK",
        "website": "https://www.hkbea.com/",
        "aliases": ["东亚银行"],
    },
    "Standard Chartered Hong Kong": {
        "slug": "standard-chartered-hong-kong",
        "title": "渣打香港",
        "region": "HK",
        "website": "https://www.sc.com/hk/",
        "aliases": ["渣打香港", "Standard Chartered"],
    },
    "ICBC (Asia)": {
        "slug": "icbc-asia",
        "title": "工银亚洲",
        "region": "HK",
        "website": "https://www.icbcasia.com/",
        "aliases": ["工银亚洲", "ICBC Asia"],
    },
    "American Express Hong Kong": {
        "slug": "american-express",
        "title": "美国运通",
        "region": "HK",
        "website": "https://www.americanexpress.com/hk/",
        "aliases": ["美国运通", "American Express"],
    },
    "Fubon Bank Hong Kong": {
        "slug": "fubon",
        "title": "富邦银行",
        "region": "HK",
        "website": "https://www.fubonbank.com.hk/",
        "aliases": ["富邦银行", "Fubon Bank"],
    },
    "China CITIC Bank International": {
        "slug": "citic-international",
        "title": "中信银行国际",
        "region": "HK",
        "website": "https://www.cncbinternational.com/",
        "aliases": ["中信银行国际", "CNCBI"],
    },
}

REWARD_PROGRAMS = {
    "hsbc-hong-kong": {
        "slug": "hsbc-rewardcash",
        "title": "汇丰 RewardCash",
        "currencyName": "RewardCash",
        "summary": "汇丰香港信用卡的核心积分货币，可用于兑换里数、签账回赠和合作伙伴礼遇。",
    },
    "hang-seng": {
        "slug": "hang-seng-points",
        "title": "恒生积分",
        "currencyName": "Cash Dollars / 积分",
        "summary": "恒生银行信用卡积分，可兑换商户礼遇、里数和现金回赠。",
    },
    "ccb-asia": {
        "slug": "ccb-asia-points",
        "title": "建行亚洲积分",
        "currencyName": "积分",
        "summary": "建行亚洲信用卡积分礼遇，覆盖本地消费与精选商户兑换。",
    },
    "cmb-wing-lung": {
        "slug": "cmb-wing-lung-bonus-points",
        "title": "招商永隆 Bonus Point",
        "currencyName": "Bonus Points",
        "summary": "招商永隆银行信用卡 Bonus Point Program，基本积分为 HKD 1 = 1 point，可兑换 Asia Miles 等礼遇。",
    },
    "boc-hong-kong": {
        "slug": "boc-hong-kong-points",
        "title": "中银香港积分",
        "currencyName": "积分",
        "summary": "中银香港信用卡积分，可用于兑换礼品、里数和合作伙伴礼遇。",
    },
    "bank-of-east-asia": {
        "slug": "bea-rewards",
        "title": "东亚银行奖赏",
        "currencyName": "奖赏",
        "summary": "东亚银行信用卡奖赏计划，覆盖本地签账、指定商户和精选兑换。",
    },
    "standard-chartered-hong-kong": {
        "slug": "standard-chartered-rewards",
        "title": "渣打奖励",
        "currencyName": "奖励",
        "summary": "渣打香港信用卡奖励计划，覆盖现金回赠、里数和精选礼遇。",
    },
    "icbc-asia": {
        "slug": "icbc-asia-rewards",
        "title": "工银亚洲奖赏",
        "currencyName": "奖赏",
        "summary": "工银亚洲信用卡奖赏，覆盖本地消费、银联场景和精选商户。",
    },
    "american-express": {
        "slug": "amex-membership-rewards-hk",
        "title": "美国运通 Membership Rewards",
        "currencyName": "Membership Rewards",
        "summary": "美国运通香港 Membership Rewards 积分，可兑换航空里数、酒店积分和精选礼遇。",
    },
    "fubon": {
        "slug": "fubon-rewards",
        "title": "富邦银行奖赏",
        "currencyName": "奖赏",
        "summary": "富邦银行香港信用卡奖赏计划，覆盖本地签账与指定商户回赠。",
    },
    "citic-international": {
        "slug": "citic-international-rewards",
        "title": "中信银行国际奖赏",
        "currencyName": "奖赏",
        "summary": "中信银行国际信用卡奖赏，覆盖本地消费、外币签账和精选兑换。",
    },
}

NATIVE_CARDS = [
    {
        "calculatorId": "hsbcAdvanceVisaPlatinum",
        "slug": "hsbc-advance-visa-platinum-card",
        "title": "汇丰 Advance Visa 白金卡",
        "shortName": "Advance Visa 白金卡",
        "issuer": "HSBC Hong Kong",
        "country": "HK",
        "summary": "基础 RewardCash、最红自主 / Rewards of Your Choice 与 FTF 计算。",
        "tags": ["RC", "FTF 1.95%", "Rewards of Your Choice"],
        "conversionRuleId": "standardRewardCash",
        "unionPay": False,
    },
    {
        "calculatorId": "hsbcEasyVisaPlatinum",
        "slug": "hsbc-easy-credit-card-visa-platinum-card",
        "title": "汇丰 easy 信用卡 / 汇丰 Visa 白金卡",
        "shortName": "easy / Visa 白金卡",
        "issuer": "HSBC Hong Kong",
        "country": "HK",
        "summary": "基础 RewardCash、MoneyBack 联动消费、Rewards of Your Choice 与 FTF 计算。",
        "tags": ["RC", "Visa Platinum", "FTF 1.95%"],
        "conversionRuleId": "standardRewardCash",
        "unionPay": False,
    },
    {
        "calculatorId": "hsbcEveryMile",
        "slug": "hsbc-everymile-credit-card",
        "title": "汇丰 EveryMile 信用卡",
        "shortName": "EveryMile",
        "issuer": "HSBC Hong Kong",
        "country": "HK",
        "summary": "基础 RewardCash、EveryMile 兑换价值口径与 FTF 计算。",
        "tags": ["RC", "里数兑换", "FTF 1.95%"],
        "conversionRuleId": "everyMile",
        "unionPay": False,
    },
    {
        "calculatorId": "hsbcPremierMasterCard",
        "slug": "hsbc-premier-mastercard",
        "title": "汇丰卓越理财 Mastercard",
        "shortName": "Premier Mastercard",
        "issuer": "HSBC Hong Kong",
        "country": "HK",
        "summary": "基础 RewardCash、Premier Rewards of Your Choice 与 FTF 计算。",
        "tags": ["RC", "Premier", "FTF 1.95%"],
        "conversionRuleId": "premierMasterCard",
        "unionPay": False,
    },
    {
        "calculatorId": "hsbcPulseUnionPayDiamond",
        "slug": "hsbc-pulse-unionpay-dual-currency-diamond-credit-card",
        "title": "汇丰 Pulse 银联双币钻石信用卡",
        "shortName": "Pulse 银联钻石",
        "issuer": "HSBC Hong Kong",
        "country": "HK",
        "summary": "内地/澳门 QR/AP、内地餐饮、赏世界、Travel Guru 与迎新活动组合计算。",
        "tags": ["RC", "银联双币", "活动叠加"],
        "conversionRuleId": "unionPayDualCurrency",
        "unionPay": True,
    },
    {
        "calculatorId": "hsbcRed",
        "slug": "hsbc-red-credit-card",
        "title": "汇丰 Red 信用卡",
        "shortName": "Red",
        "issuer": "HSBC Hong Kong",
        "country": "HK",
        "summary": "香港指定商户 8%、网上签账 4% 与基础 RewardCash 分段计算。",
        "tags": ["RC", "网上 4%", "指定商户 8%"],
        "conversionRuleId": "standardRewardCash",
        "unionPay": False,
    },
    {
        "calculatorId": "hsbcUnionPayDualCurrency",
        "slug": "hsbc-unionpay-dual-currency-credit-card",
        "title": "汇丰银联双币信用卡",
        "shortName": "银联双币",
        "issuer": "HSBC Hong Kong",
        "country": "HK",
        "summary": "基础 RewardCash、银联双币外币/内地场景与 FTF 计算。",
        "tags": ["RC", "银联双币", "CNY/HKD"],
        "conversionRuleId": "unionPayDualCurrency",
        "unionPay": True,
    },
    {
        "calculatorId": "hsbcVisaGold",
        "slug": "hsbc-visa-gold-card",
        "title": "汇丰 Visa 金卡",
        "shortName": "Visa 金卡",
        "issuer": "HSBC Hong Kong",
        "country": "HK",
        "summary": "基础 RewardCash、Rewards of Your Choice 与 FTF 计算。",
        "tags": ["RC", "Visa Gold", "FTF 1.95%"],
        "conversionRuleId": "standardRewardCash",
        "unionPay": False,
    },
    {
        "calculatorId": "hsbcVisaGoldStudent",
        "slug": "hsbc-visa-gold-card-for-students",
        "title": "汇丰学生 Visa 金卡",
        "shortName": "学生 Visa 金卡",
        "issuer": "HSBC Hong Kong",
        "country": "HK",
        "summary": "基础 RewardCash、学费缴付场景与 FTF 计算。",
        "tags": ["RC", "学生卡", "学费"],
        "conversionRuleId": "standardRewardCash",
        "unionPay": False,
    },
    {
        "calculatorId": "hsbcVisaSignature",
        "slug": "hsbc-visa-signature-card",
        "title": "汇丰 Visa Signature 卡",
        "shortName": "Visa Signature",
        "issuer": "HSBC Hong Kong",
        "country": "HK",
        "summary": "Visa Signature 奖赏、最红自主奖赏与非港币 FTF 扣费计算。",
        "tags": ["RC", "最高约 3.6%", "最红自主"],
        "conversionRuleId": "standardRewardCash",
        "unionPay": False,
    },
    {
        "calculatorId": "hangSengEnjoyVisaPlatinum",
        "slug": "hang-seng-enjoy-visa-platinum-card",
        "title": "Hang Seng enJoy Visa Platinum Card",
        "shortName": "enJoy Visa Platinum",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "指定 yuu 商户最高 4X yuu Points，按现金价值计算。",
        "tags": ["yuu", "Visa Platinum", "指定商户"],
        "unionPay": False,
    },
    {
        "calculatorId": "hangSengGoldClassicCreditCard",
        "slug": "hang-seng-gold-classic-credit-card",
        "title": "Hang Seng Gold / Classic Credit Card",
        "shortName": "Gold / Classic",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "按恒生 EveryDay Rewards 基本 Cash Dollars 口径计算。",
        "tags": ["Cash Dollars", "EveryDay Rewards"],
        "unionPay": False,
    },
    {
        "calculatorId": "hangSengMmpowerWorldMastercard",
        "slug": "hang-seng-mmpower-world-mastercard",
        "title": "Hang Seng MMPOWER World Mastercard",
        "shortName": "MMPOWER",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "指定商户 / 网上娱乐 / 网上服饰最高 8%，其他网购 5%，外币 4%。",
        "tags": ["+FUN Dollars", "最高 8%", "Mastercard"],
        "unionPay": False,
    },
    {
        "calculatorId": "hangSengMujiCard",
        "slug": "hang-seng-muji-card",
        "title": "Hang Seng MUJI Card",
        "shortName": "MUJI Card",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "MUJI 联营卡按恒生 EveryDay Rewards 基本 Cash Dollars 口径计算。",
        "tags": ["Cash Dollars", "MUJI"],
        "unionPay": False,
    },
    {
        "calculatorId": "hangSengPlatinum",
        "slug": "hang-seng-platinum-card",
        "title": "Hang Seng Platinum Card",
        "shortName": "Platinum",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "按恒生 EveryDay Rewards 基本 Cash Dollars 口径计算。",
        "tags": ["Cash Dollars", "Platinum"],
        "unionPay": False,
    },
    {
        "calculatorId": "hangSengPrestigeWorldMastercard",
        "slug": "hang-seng-prestige-world-mastercard",
        "title": "Hang Seng Prestige World Mastercard",
        "shortName": "Prestige World",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "Prestige World Mastercard 按基本 Cash Dollars 口径计算，专项活动需另行核对。",
        "tags": ["Cash Dollars", "Prestige", "Mastercard"],
        "unionPay": False,
    },
    {
        "calculatorId": "hangSengRenminbiCreditCard",
        "slug": "hang-seng-renminbi-credit-card",
        "title": "Hang Seng Renminbi Credit Card",
        "shortName": "人民币卡",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "人民币信用卡按 RMB250 赚 $1 Cash Dollars 的基本口径计算。",
        "tags": ["Cash Dollars", "RMB", "人民币"],
        "unionPay": True,
    },
    {
        "calculatorId": "hangSengTravelPlusVisaSignature",
        "slug": "hang-seng-travel-plus-visa-signature-card",
        "title": "Hang Seng Travel+ Visa Signature Card",
        "shortName": "Travel+",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "指定外币最高 7%，其他外币 / 本地餐饮最高 5%，每月额外奖赏 cap $500。",
        "tags": ["Travel+", "Visa Signature", "外币"],
        "unionPay": False,
    },
    {
        "calculatorId": "hangSengUnionPayCreditCard",
        "slug": "hang-seng-unionpay-credit-card",
        "title": "Hang Seng UnionPay Credit Card",
        "shortName": "UnionPay",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "银联信用卡按恒生 EveryDay Rewards 基本 Cash Dollars 口径计算。",
        "tags": ["Cash Dollars", "UnionPay"],
        "unionPay": True,
    },
    {
        "calculatorId": "hangSengUniversityCollege",
        "slug": "hang-seng-university-college-cards",
        "title": "Hang Seng University / College Cards",
        "shortName": "大学 / 大专卡",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "大学 / 大专联营卡教育支出按 2.4% Cash Dollars 口径计算。",
        "tags": ["教育", "学生卡", "Cash Dollars"],
        "unionPay": False,
    },
    {
        "calculatorId": "hangSengVisaInfinite",
        "slug": "hang-seng-visa-infinite-card",
        "title": "Hang Seng Visa Infinite Card",
        "shortName": "Visa Infinite",
        "issuer": "Hang Seng Bank",
        "country": "HK",
        "summary": "Visa Infinite 按基本 Cash Dollars 口径计算，历史限时倍数活动不作为当前默认规则。",
        "tags": ["Visa Infinite", "Cash Dollars"],
        "unionPay": False,
    },
    {
        "calculatorId": "ccbAsiaAiaVisa",
        "slug": "ccb-asia-aia-visa-credit-card",
        "title": "建行亚洲 AIA Visa 信用卡",
        "shortName": "AIA Visa",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "AIA 联营 Visa 卡按建行亚洲基本奖赏现金价值计算。",
        "tags": ["CCB Asia", "Visa", "AIA"],
        "unionPay": False,
    },
    {
        "calculatorId": "ccbAsiaEyeCreditCard",
        "slug": "ccb-asia-eye-credit-card",
        "title": "建行亚洲 eye 信用卡",
        "shortName": "eye",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "eye 信用卡网上及本地消费按基本奖赏与指定类别官方口径计算。",
        "tags": ["CCB Asia", "eye", "网上签账"],
        "unionPay": False,
    },
    {
        "calculatorId": "ccbAsiaGbaVirtualUnionPay",
        "slug": "ccb-asia-gba-virtual-unionpay-credit-card",
        "title": "建行亚洲大湾区虚拟银联信用卡",
        "shortName": "大湾区虚拟银联",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "大湾区虚拟银联卡按银联 / 内地消费与基本奖赏官方口径计算。",
        "tags": ["CCB Asia", "虚拟卡", "UnionPay"],
        "unionPay": True,
    },
    {
        "calculatorId": "ccbAsiaIndustryUnionPayDualCurrency",
        "slug": "ccb-asia-industry-unionpay-dual-currency-credit-card",
        "title": "建行亚洲建造业银联双币信用卡",
        "shortName": "建造业银联双币",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "建造业银联双币卡按银联 / 内地消费与基本奖赏官方口径计算。",
        "tags": ["CCB Asia", "UnionPay", "双币"],
        "unionPay": True,
    },
    {
        "calculatorId": "ccbAsiaOctopusMotoristUnionPayDiamond",
        "slug": "ccb-asia-octopus-motorist-unionpay-diamond-credit-card",
        "title": "八达通车生活银联钻石信用卡",
        "shortName": "八达通车生活钻石",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "八达通车生活银联钻石卡按基本奖赏现金价值计算。",
        "tags": ["CCB Asia", "UnionPay Diamond", "八达通"],
        "unionPay": True,
    },
    {
        "calculatorId": "ccbAsiaOctopusUnionPayDualCurrency",
        "slug": "ccb-asia-octopus-unionpay-dual-currency-credit-card",
        "title": "建行亚洲八达通银联双币信用卡",
        "shortName": "八达通银联双币",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "八达通银联双币卡按银联 / 内地消费与基本奖赏官方口径计算。",
        "tags": ["CCB Asia", "UnionPay", "八达通"],
        "unionPay": True,
    },
    {
        "calculatorId": "ccbAsiaPlatinum",
        "slug": "ccb-asia-platinum-credit-card",
        "title": "建行亚洲白金信用卡",
        "shortName": "白金卡",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "白金信用卡按建行亚洲基本奖赏现金价值计算。",
        "tags": ["CCB Asia", "Platinum"],
        "unionPay": False,
    },
    {
        "calculatorId": "ccbAsiaPuiChingUnionPayDualCurrency",
        "slug": "ccb-asia-pui-ching-unionpay-dual-currency-credit-card",
        "title": "建行亚洲培正银联双币信用卡",
        "shortName": "培正银联双币",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "培正银联双币卡按银联 / 内地消费与基本奖赏官方口径计算。",
        "tags": ["CCB Asia", "UnionPay", "联营卡"],
        "unionPay": True,
    },
    {
        "calculatorId": "ccbAsiaTravoMastercard",
        "slug": "ccb-asia-travo-mastercard",
        "title": "建行亚洲 TRAVO Mastercard",
        "shortName": "TRAVO Mastercard",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "TRAVO Mastercard 旅游及本地消费按基本奖赏与指定类别官方口径计算。",
        "tags": ["CCB Asia", "TRAVO", "Mastercard"],
        "unionPay": False,
    },
    {
        "calculatorId": "ccbAsiaTravoWorldMastercard",
        "slug": "ccb-asia-travo-world-mastercard",
        "title": "建行亚洲 TRAVO World Mastercard",
        "shortName": "TRAVO World",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "TRAVO World Mastercard 旅游及海外消费按基本奖赏与指定类别官方口径计算。",
        "tags": ["CCB Asia", "TRAVO", "World Mastercard"],
        "unionPay": False,
    },
    {
        "calculatorId": "ccbAsiaUnionPayDiamondPrestige",
        "slug": "ccb-asia-unionpay-diamond-prestige-credit-card",
        "title": "建行亚洲银联钻石 Prestige 信用卡",
        "shortName": "银联钻石 Prestige",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "银联钻石 Prestige 卡按银联 / 内地消费与基本奖赏官方口径计算。",
        "tags": ["CCB Asia", "UnionPay Diamond", "Prestige"],
        "unionPay": True,
    },
    {
        "calculatorId": "ccbAsiaUnionPayDualCurrency",
        "slug": "ccb-asia-unionpay-dual-currency-credit-card",
        "title": "建行亚洲银联双币信用卡",
        "shortName": "银联双币",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "银联双币信用卡按银联 / 内地消费与基本奖赏官方口径计算。",
        "tags": ["CCB Asia", "UnionPay", "双币"],
        "unionPay": True,
    },
    {
        "calculatorId": "ccbAsiaVisaInfinite",
        "slug": "ccb-asia-visa-infinite-credit-card",
        "title": "建行亚洲 Visa Infinite 信用卡",
        "shortName": "Visa Infinite",
        "issuer": "CCB (Asia)",
        "country": "HK",
        "summary": "Visa Infinite 卡按基本奖赏、海外签账及 FTF 官方口径计算。",
        "tags": ["CCB Asia", "Visa Infinite"],
        "unionPay": False,
    },
]


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def yaml_list(values: list[str], indent: int = 2) -> str:
    if not values:
        return " []"
    pad = " " * indent
    return "\n" + "\n".join(f"{pad}- {yaml_quote(v)}" for v in values)


def wikilink(slug: str, title: str, kind: str) -> str:
    rel = {
        "cards": f"../cards/{slug}.md",
        "banks": f"../banks/{slug}.md",
        "reward-programs": f"../reward-programs/{slug}.md",
        "sources": f"../sources/{slug}.md",
        "pages": f"../pages/{slug}.md",
        "posts": f"../posts/{slug}.md",
        "glossary": f"../glossary/{slug}.md",
        "categories": f"../categories/{slug}.md",
    }[kind]
    return f"[[{kind}:{slug}|{title}]]({rel})"


def wikilink_from(slug: str, title: str, kind: str, here: str) -> str:
    prefix = "../" if here != kind else "./"
    if here == "root":
        prefix = f"{kind}/"
        return f"[[{kind}:{slug}|{title}]]({prefix}{slug}.md)"
    rel = f"{prefix}{slug}.md" if here == kind else f"../{kind}/{slug}.md"
    return f"[[{kind}:{slug}|{title}]]({rel})"


def hsbc_market_bank(country: str) -> dict:
    labels = {
        "AE": ("hsbc-united-arab-emirates", "汇丰阿联酋"),
        "AU": ("hsbc-australia", "汇丰澳大利亚"),
        "BM": ("hsbc-bermuda", "汇丰百慕大"),
        "CN": ("hsbc-china", "汇丰中国"),
        "EG": ("hsbc-egypt", "汇丰埃及"),
        "EXPAT_JE": ("hsbc-expat", "汇丰 Expat"),
        "HK": ("hsbc-hong-kong", "汇丰香港"),
        "ID": ("hsbc-indonesia", "汇丰印度尼西亚"),
        "IM_GG_JE": ("hsbc-channel-islands-isle-of-man", "汇丰海峡群岛及马恩岛"),
        "IN": ("hsbc-india", "汇丰印度"),
        "LK": ("hsbc-sri-lanka", "汇丰斯里兰卡"),
        "MO": ("hsbc-macau", "汇丰澳门"),
        "MT": ("hsbc-malta", "汇丰马耳他"),
        "MX": ("hsbc-mexico", "汇丰墨西哥"),
        "MY": ("hsbc-malaysia", "汇丰马来西亚"),
        "PH": ("hsbc-philippines", "汇丰菲律宾"),
        "QA": ("hsbc-qatar", "汇丰卡塔尔"),
        "SG": ("hsbc-singapore", "汇丰新加坡"),
        "TR": ("hsbc-turkiye", "汇丰土耳其"),
        "TW": ("hsbc-taiwan", "汇丰台湾"),
        "UK": ("hsbc-united-kingdom", "汇丰英国"),
        "UY": ("hsbc-uruguay", "汇丰乌拉圭"),
        "US": ("hsbc-united-states", "汇丰美国"),
        "VN": ("hsbc-vietnam", "汇丰越南"),
    }
    slug, title = labels[country]
    websites = {
        "AE": "https://www.hsbc.ae/credit-cards/products/",
        "AU": "https://www.hsbc.com.au/credit-cards/products/",
        "BM": "https://www.hsbc.bm/credit-cards/products/",
        "CN": "https://www.hsbc.com.cn/credit-cards/products/",
        "EG": "https://www.hsbc.com.eg/credit-cards/products/",
        "EXPAT_JE": "https://www.expat.hsbc.com/credit-cards/products/",
        "HK": "https://www.hsbc.com.hk/credit-cards/products/",
        "ID": "https://www.hsbc.co.id/credit-cards/products/",
        "IM_GG_JE": "https://ciiom.hsbc.com/credit-cards/products/",
        "IN": "https://www.hsbc.co.in/credit-cards/products/",
        "LK": "https://www.hsbc.lk/credit-cards/products/",
        "MO": "https://www.hsbc.com.mo/credit-cards/products/",
        "MT": "https://www.hsbc.com.mt/credit-cards/products/",
        "MX": "https://www.hsbc.com.mx/tarjetas-de-credito/productos/",
        "MY": "https://www.hsbc.com.my/credit-cards/products/",
        "PH": "https://www.hsbc.com.ph/credit-cards/products/",
        "QA": "https://www.hsbc.com.qa/credit-cards/products/",
        "SG": "https://www.hsbc.com.sg/credit-cards/products/",
        "TR": "https://www.hsbc.com.tr/en/credit-cards-and-loans/credit-cards/",
        "TW": "https://www.hsbc.com.tw/credit-cards/products/",
        "UK": "https://www.hsbc.co.uk/credit-cards/products/",
        "US": "https://www.us.hsbc.com/credit-cards/products/",
        "UY": "https://www.hsbc.com.uy/tarjetas/credito/",
        "VN": "https://www.hsbc.com.vn/credit-cards/products/",
    }
    return {
        "slug": slug,
        "title": title,
        "region": REGION_FROM_COUNTRY.get(country, "GLOBAL"),
        "website": websites[country],
        "country": country,
    }


def parse_additional_cards(text: str) -> list[dict]:
    start = text.index("export const additionalHongKongRebateCards = [")
    end = text.index("export const additionalHongKongRebateCalculatorCardIds")
    body = text[start:end]
    cards = []
    for block in re.split(r"\n  \{\n", body)[1:]:
        def g(key: str, default: str = "") -> str:
            m = re.search(rf"{key}:\s*'([^']*)'", block)
            return m.group(1) if m else default

        def gbool(key: str) -> bool:
            m = re.search(rf"{key}: (true|false)", block)
            return m.group(1) == "true" if m else False

        tags_m = re.search(r"tags: \[([^\]]*)\]", block)
        tags = []
        if tags_m:
            tags = [t.strip().strip("'") for t in tags_m.group(1).split(",") if t.strip()]
        items = []
        for im in re.finditer(
            r"label: '([^']+)'.*?rateText: '([^']+)'",
            block,
            re.S,
        ):
            items.append({"label": im.group(1), "rateText": im.group(2)})
        cards.append(
            {
                "calculatorId": g("calculatorId"),
                "issuer": g("issuer"),
                "shortName": g("shortName"),
                "slug": g("slug"),
                "summary": g("summary"),
                "title": g("title"),
                "unionPay": gbool("unionPay"),
                "tags": tags,
                "termsURL": g("termsURL"),
                "rateText": g("rateText"),
                "rewardUnitLabel": g("rewardUnitLabel"),
                "baseLabel": g("baseLabel"),
                "items": items[:8],
                "country": "HK",
            }
        )
    return [c for c in cards if c["slug"] and c["title"]]


def parse_global_hsbc_cards(text: str) -> list[dict]:
    cards = []
    pattern = re.compile(
        r"card\(\s*'([^']+)',\s*'([^']+)',\s*'([^']+)',\s*'([^']+)',\s*'([^']+)',\s*'([^']+)'(?:,\s*'([^']*)')?,?\s*\)",
        re.S,
    )
    for m in pattern.finditer(text):
        country, market, slug, title, short_name, official, status = m.groups()
        status = status or "官方产品页列出，未见停售标记"
        cards.append(
            {
                "calculatorId": "globalHsbc" + "".join(
                    part[:1].upper() + part[1:] for part in slug.replace("hsbc-", "").split("-")
                ),
                "issuer": f"HSBC {country}",
                "shortName": short_name,
                "slug": slug,
                "summary": f"{market} HSBC 官方信用卡产品。官方名称：{official}。状态：{status}。",
                "title": title,
                "unionPay": "unionpay" in slug or "银联" in title,
                "tags": ["HSBC", country, short_name, status],
                "termsURL": hsbc_market_bank(country)["website"],
                "officialName": official,
                "statusNote": status,
                "market": market,
                "country": country,
                "items": [],
                "rateText": "",
                "rewardUnitLabel": "",
                "baseLabel": "",
            }
        )
    return cards


def ensure_bank(banks: dict[str, dict], card: dict) -> dict:
    issuer = card["issuer"]
    if issuer in ISSUER_BANKS:
        info = ISSUER_BANKS[issuer]
        banks.setdefault(info["slug"], {**info, "issuerKey": issuer})
        return banks[info["slug"]]
    if issuer.startswith("HSBC "):
        info = hsbc_market_bank(card["country"])
        banks.setdefault(info["slug"], info)
        return banks[info["slug"]]
    raise KeyError(issuer)


def yaml_dump_card(card: dict, bank: dict, program: dict | None, related: list[dict], source_slug: str | None) -> str:
    tags = card.get("tags") or []
    related_slugs = [c["slug"] for c in related]
    front = [
        "---",
        "collection: cards",
        f"title: {yaml_quote(card['title'])}",
        f"shortName: {yaml_quote(card.get('shortName') or '')}",
        f"slug: {card['slug']}",
        f"country: {card['country']}",
        f"bank: {bank['slug']}",
        f"rewardProgram: {program['slug'] if program else ''}",
        f"sourceLevel: C",
        "status: stub",
        "_status: draft",
        "lastVerifiedAt: null",
        f"unionPay: {'true' if card.get('unionPay') else 'false'}",
        "rebateCalculator:",
        f"  enabled: true",
        f"  calculatorId: {card.get('calculatorId') or ''}",
        f"  issuer: {yaml_quote(card['issuer'])}",
        "conversionCalculator:",
        f"  enabled: {'true' if card.get('conversionRuleId') else 'false'}",
        f"  ruleId: {card.get('conversionRuleId') or 'null'}",
        f"tags:{yaml_list(tags)}",
        f"relatedCards:{yaml_list(related_slugs)}",
        f"sources:{yaml_list([source_slug] if source_slug else [])}",
        "origin: payload-website-starter",
        f"generatedAt: {TODAY}",
        "---",
        "",
    ]
    return "\n".join(front)


def card_body(card: dict, bank: dict, program: dict | None, related: list[dict], source: dict | None) -> str:
    country_label = COUNTRY_LABELS.get(card["country"], card["country"])
    bank_link = wikilink(bank["slug"], bank["title"], "banks")
    program_link = (
        wikilink(program["slug"], program["title"], "reward-programs") if program else "待补"
    )
    infobox_rows = [
        ("官方名称", card["title"]),
        ("简称", card.get("shortName") or "—"),
        ("市场", country_label),
        ("发卡银行", bank_link),
        ("积分体系", program_link),
        ("来源等级", "[[glossary:source-level|C · 待复核]](../glossary/source-level.md)"),
        ("词条状态", "Stub / 待迁入 Payload"),
        ("银联双币", "是" if card.get("unionPay") else "否"),
    ]
    if card.get("rateText"):
        infobox_rows.append(("基本回赠", card["rateText"]))
    if card.get("rewardUnitLabel"):
        infobox_rows.append(("奖赏单位", card["rewardUnitLabel"]))
    if card.get("calculatorId"):
        infobox_rows.append(("计算器插件", f"`{card['calculatorId']}`"))
    if card.get("conversionRuleId"):
        infobox_rows.append(("兑换规则", f"`{card['conversionRuleId']}`"))
    if card.get("officialName"):
        infobox_rows.append(("英文官方名", card["officialName"]))
    if card.get("statusNote"):
        infobox_rows.append(("产品状态", card["statusNote"]))

    table = ["| 字段 | 值 |", "| --- | --- |"]
    table.extend(f"| {k} | {v} |" for k, v in infobox_rows)

    rules = ""
    if card.get("items"):
        lines = ["", "## 已收录回赠口径", "", "以下规则摘自主仓库计算器数据，**不是**数据库正文，迁移后仍需对照官方条款核验。", ""]
        lines.append("| 项目 | 口径 |")
        lines.append("| --- | --- |")
        seen = set()
        for item in card["items"]:
            key = (item["label"], item["rateText"])
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"| {item['label']} | {item['rateText']} |")
        rules = "\n".join(lines) + "\n"

    related_md = "暂无同银行相关词条。"
    if related:
        related_md = "\n".join(
            f"- {wikilink(c['slug'], c['title'], 'cards')}" for c in related
        )

    source_md = "尚未挂接核验来源。"
    if source:
        source_md = (
            f"- {wikilink(source['slug'], source['title'], 'sources')} — {source['url']}"
        )

    tags = card.get("tags") or []
    cats = [
        "[[Category:信用卡]]",
        f"[[Category:{country_label}信用卡]]",
        f"[[Category:{bank['title']}]]",
    ]
    if card.get("unionPay"):
        cats.append("[[Category:银联]]")
    for tag in tags[:4]:
        cats.append(f"[[Category:{tag}]]")

    lead = card.get("summary") or "这个卡片词条正在逐步补全。"
    return f"""{{{{Infobox card}}}}

# {card['title']}

> {lead}

{chr(10).join(table)}

## 概述

**{card['title']}** 是 {bank_link} 在{country_label}市场发行的信用卡词条。本页是 Fluxa WikiCard 的 Git 暂存稿：主站 [fluxa.wiki](https://fluxa.wiki) 的正文目前写在 Payload 数据库里，等 `payload-website-starter` 代码稳定后再迁回 Cards collection。

- 发卡银行：{bank_link}
- 积分体系：{program_link}
- 编辑约定：卡片维基摘要和正文不写进前端源码，见 [[pages:how-to-contribute|词条编写约定]](../pages/how-to-contribute.md)

## 积分与回赠

本词条的奖赏单位关联 {program_link}。计算器规则仍保留在主仓库源码中；本 Wiki 只记录可迁移的词条事实和官方来源。

{rules}
## 计算器接入

| 类型 | 是否接入 | 标识 |
| --- | --- | --- |
| 返利计算器 | 是 | `{card.get('calculatorId') or '—'}` |
| 兑换计算器 | {'是' if card.get('conversionRuleId') else '否'} | `{card.get('conversionRuleId') or '—'}` |

实际估算请以 [fluxa.wiki 返利计算器](https://fluxa.wiki/rebate-calculator) 和官方条款为准。未核验活动、过期优惠或商户分类差异都可能导致实际到账与估算不同。详见 [[pages:terms|使用条款]](../pages/terms.md)。

## 信息来源

{source_md}

来源等级当前为 **C（待复核）**。等级说明见 [[glossary:source-level|来源等级]](../glossary/source-level.md)。

## 相关词条

{related_md}

## 迁移备注

- Payload collection：`cards`
- slug：`{card['slug']}`
- 关系字段：`bank` → `{bank['slug']}`；`rewardProgram` → `{program['slug'] if program else ''}`
- `_status` 建议先以 `draft` 导入，核验后再 publish

{chr(10).join(cats)}
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def index_page(kind: str, title: str, intro: str, items: list[tuple[str, str, str]]) -> str:
    groups: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for heading, slug, label in items:
        groups[heading].append((slug, label))
    parts = [
        "---",
        f"collection: pages",
        f"title: {yaml_quote(title)}",
        f"slug: {kind}-index",
        "status: published",
        "---",
        "",
        f"# {title}",
        "",
        intro,
        "",
    ]
    for heading in sorted(groups):
        parts.append(f"## {heading}")
        parts.append("")
        for slug, label in sorted(groups[heading], key=lambda x: x[1]):
            parts.append(f"- {wikilink_from(slug, label, kind, kind)}")
        parts.append("")
    parts.append("[[Category:索引]]")
    return "\n".join(parts) + "\n"


def bank_page(bank: dict, cards: list[dict], program: dict | None) -> str:
    region = bank.get("region", "HK")
    program_link = (
        wikilink(program["slug"], program["title"], "reward-programs") if program else "待建"
    )
    card_links = "\n".join(
        f"- {wikilink(c['slug'], c['title'], 'cards')}"
        for c in sorted(cards, key=lambda x: x["title"])
    )
    aliases = bank.get("aliases") or []
    return f"""---
collection: banks
title: {yaml_quote(bank['title'])}
slug: {bank['slug']}
region: {region}
website: {yaml_quote(bank.get('website') or '')}
status: stub
generatedAt: {TODAY}
---

{{{{Infobox bank}}}}

# {bank['title']}

**{bank['title']}** 是 Fluxa WikiCard 的银行词条。卡片必须通过 `bank` 关系挂到本页，前台筛选和详情页都读这个关系，不要再靠标题模糊匹配。

| 字段 | 值 |
| --- | --- |
| 地区 | {region} · {COUNTRY_LABELS.get(region, region)} |
| 官网 | {bank.get('website') or '—'} |
| 积分体系 | {program_link} |
| 词条数 | {len(cards)} |

## 收录信用卡

{card_links or '暂无卡片。'}

## 别名

用于主仓库把计算器 issuer 字符串对齐到银行关系：

{chr(10).join(f'- `{a}`' for a in aliases) or '- 无'}

## 迁移备注

- Payload collection：`banks`
- slug：`{bank['slug']}`

[[Category:银行]]
[[Category:{COUNTRY_LABELS.get(region, region)}]]
"""


def program_page(program: dict, bank: dict, cards: list[dict]) -> str:
    card_links = "\n".join(
        f"- {wikilink(c['slug'], c['title'], 'cards')}"
        for c in sorted(cards, key=lambda x: x["title"])
    )
    return f"""---
collection: reward-programs
title: {yaml_quote(program['title'])}
slug: {program['slug']}
bank: {bank['slug']}
region: {bank.get('region', 'HK')}
currencyName: {yaml_quote(program['currencyName'])}
status: stub
generatedAt: {TODAY}
---

{{{{Infobox reward program}}}}

# {program['title']}

{program['summary']}

| 字段 | 值 |
| --- | --- |
| 所属银行 | {wikilink(bank['slug'], bank['title'], 'banks')} |
| 积分货币 | {program['currencyName']} |
| 地区 | {bank.get('region', 'HK')} |

## 使用该体系的信用卡

{card_links or '暂无卡片。'}

## 迁移备注

- Payload collection：`reward-programs`
- 关系字段：`bank` → `{bank['slug']}`
- `transferPartners` 尚未从数据库导出，迁入时留空即可

[[Category:积分体系]]
[[Category:{bank['title']}]]
"""


def source_page(source: dict, cards: list[dict]) -> str:
    card_links = "\n".join(
        f"- {wikilink(c['slug'], c['title'], 'cards')}"
        for c in sorted(cards, key=lambda x: x["title"])
    )
    return f"""---
collection: sources
title: {yaml_quote(source['title'])}
slug: {source['slug']}
url: {yaml_quote(source['url'])}
sourceType: {source['sourceType']}
publisher: {yaml_quote(source['publisher'])}
reliabilityLevel: secondary
status: stub
generatedAt: {TODAY}
---

# {source['title']}

这是卡片词条挂接的核验来源。主仓库约定：核验来源写在数据库里，再挂到对应卡片上。

| 字段 | 值 |
| --- | --- |
| URL | {source['url']} |
| 类型 | {source['sourceType']} |
| 发布方 | {source['publisher']} |
| 可信等级 | secondary（待复核） |

## 关联信用卡

{card_links or '暂无卡片。'}

[[Category:来源]]
"""


def main() -> None:
    if not PAYLOAD.exists():
        raise SystemExit(
            f"Payload starter not found at {PAYLOAD}. "
            "Clone payload-website-starter and set PAYLOAD_STARTER."
        )
    for name in ["cards", "banks", "reward-programs", "sources", "categories"]:
        path = WIKI / name
        if path.exists():
            shutil.rmtree(path)
    additional = parse_additional_cards(
        (PAYLOAD / "src/data/additionalHongKongRebateCards.ts").read_text(encoding="utf-8")
    )
    global_cards = parse_global_hsbc_cards(
        (PAYLOAD / "src/data/globalHsbcCards.ts").read_text(encoding="utf-8")
    )

    all_cards: list[dict] = []
    seen_slugs: set[str] = set()
    for card in NATIVE_CARDS + additional + global_cards:
        if card["slug"] in seen_slugs:
            continue
        seen_slugs.add(card["slug"])
        all_cards.append(card)

    banks: dict[str, dict] = {}
    for info in ISSUER_BANKS.values():
        banks[info["slug"]] = {**info}
    for card in all_cards:
        ensure_bank(banks, card)

    programs: dict[str, dict] = {}
    for bank_slug, prog in REWARD_PROGRAMS.items():
        programs[prog["slug"]] = {**prog, "bank": bank_slug}
    for bank in banks.values():
        if bank["slug"] not in REWARD_PROGRAMS:
            slug = f"{bank['slug']}-rewards"
            programs[slug] = {
                "slug": slug,
                "title": f"{bank['title']}奖赏",
                "currencyName": "奖赏",
                "summary": f"{bank['title']}信用卡奖赏计划，细则以当地官方产品页为准。",
                "bank": bank["slug"],
            }
            REWARD_PROGRAMS[bank["slug"]] = programs[slug]

    cards_by_bank: dict[str, list[dict]] = defaultdict(list)
    sources: dict[str, dict] = {}
    source_cards: dict[str, list[dict]] = defaultdict(list)

    enriched = []
    for card in all_cards:
        bank = ensure_bank(banks, card)
        prog_meta = REWARD_PROGRAMS.get(bank["slug"])
        program = programs.get(prog_meta["slug"]) if prog_meta else None
        source = None
        if card.get("termsURL"):
            src_slug = re.sub(r"[^a-z0-9]+", "-", f"{bank['slug']}-official-terms").strip("-")
            if card["termsURL"] not in {s["url"] for s in sources.values()}:
                source = {
                    "slug": src_slug[:80],
                    "title": f"{bank['title']} 官方产品 / 条款",
                    "url": card["termsURL"],
                    "sourceType": "terms",
                    "publisher": bank["title"],
                }
                # Unique slug if same bank has multiple official URLs
                if src_slug in sources and sources[src_slug]["url"] != card["termsURL"]:
                    src_slug = f"{src_slug}-{len(sources)}"
                    source["slug"] = src_slug
                sources[src_slug] = source
            else:
                source = next(s for s in sources.values() if s["url"] == card["termsURL"])
            source_cards[source["slug"]].append(card)
        card["_bank"] = bank
        card["_program"] = program
        card["_source"] = source
        cards_by_bank[bank["slug"]].append(card)
        enriched.append(card)

    for path in [
        WIKI / "cards",
        WIKI / "banks",
        WIKI / "reward-programs",
        WIKI / "sources",
        WIKI / "categories",
    ]:
        path.mkdir(parents=True, exist_ok=True)

    for card in enriched:
        bank = card["_bank"]
        related = [
            c
            for c in cards_by_bank[bank["slug"]]
            if c["slug"] != card["slug"]
        ][:8]
        source = card["_source"]
        text = yaml_dump_card(
            card, bank, card["_program"], related, source["slug"] if source else None
        ) + card_body(card, bank, card["_program"], related, source)
        write(WIKI / "cards" / f"{card['slug']}.md", text)

    for bank in banks.values():
        prog_meta = REWARD_PROGRAMS.get(bank["slug"])
        program = programs.get(prog_meta["slug"]) if prog_meta else None
        write(
            WIKI / "banks" / f"{bank['slug']}.md",
            bank_page(bank, cards_by_bank.get(bank["slug"], []), program),
        )

    cards_by_program: dict[str, list[dict]] = defaultdict(list)
    for card in enriched:
        if card["_program"]:
            cards_by_program[card["_program"]["slug"]].append(card)
    for program in programs.values():
        bank = banks[program["bank"]]
        write(
            WIKI / "reward-programs" / f"{program['slug']}.md",
            program_page(program, bank, cards_by_program.get(program["slug"], [])),
        )

    for source in sources.values():
        write(
            WIKI / "sources" / f"{source['slug']}.md",
            source_page(source, source_cards[source["slug"]]),
        )

    write(
        WIKI / "cards" / "_index.md",
        index_page(
            "cards",
            "信用卡词条",
            "按银行浏览 Fluxa WikiCard 暂存信用卡词条。正文目前是 stub，等主仓库 Payload 数据迁入后再替换摘要与 Lexical 正文。",
            [(c["_bank"]["title"], c["slug"], c["title"]) for c in enriched],
        ),
    )
    write(
        WIKI / "banks" / "_index.md",
        index_page(
            "banks",
            "银行词条",
            "浏览发卡机构。卡片必须挂到银行词条上，不要把银行名单写进前端源码。",
            [(b.get("region", "HK"), b["slug"], b["title"]) for b in banks.values()],
        ),
    )
    write(
        WIKI / "reward-programs" / "_index.md",
        index_page(
            "reward-programs",
            "积分体系词条",
            "积分体系、转点伙伴和发卡行礼遇会在这里持续整理。",
            [
                (programs[p]["title"] if False else banks[prog["bank"]]["title"], prog["slug"], prog["title"])
                for prog in programs.values()
            ],
        ),
    )
    write(
        WIKI / "sources" / "_index.md",
        index_page(
            "sources",
            "核验来源",
            "从主仓库计算器 `termsURL` 抽出的条款来源。可信等级默认为 secondary，迁入数据库后需人工复核。",
            [("条款", s["slug"], s["title"]) for s in sources.values()],
        ),
    )

    cat_cards = defaultdict(list)
    for card in enriched:
        cat_cards["信用卡"].append(card)
        cat_cards[f"{COUNTRY_LABELS.get(card['country'], card['country'])}信用卡"].append(card)
        cat_cards[card["_bank"]["title"]].append(card)
        if card.get("unionPay"):
            cat_cards["银联"].append(card)
    for name, cards in cat_cards.items():
        slug = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", name.lower()).strip("-")
        links = "\n".join(
            f"- {wikilink(c['slug'], c['title'], 'cards')}"
            for c in sorted(cards, key=lambda x: x["title"])
        )
        write(
            WIKI / "categories" / f"{slug}.md",
            f"""---
collection: categories
title: {yaml_quote(name)}
slug: {slug}
---

# 分类：{name}

本分类下共 {len(cards)} 个信用卡词条。

{links}

[[Category:分类]]
""",
        )

    summary = WIKI / "_generated-stats.md"
    write(
        summary,
        f"""# 生成统计

- 生成日期：{TODAY}
- 信用卡词条：{len(enriched)}
- 银行词条：{len(banks)}
- 积分体系：{len(programs)}
- 来源词条：{len(sources)}
- 分类页：{len(cat_cards)}

数据来源：`payload-website-starter` 的计算器卡册与 `globalHsbcCards` / `additionalHongKongRebateCards`。数据库里的 Lexical 正文、摘要覆盖和对比参数值**没有**导出。
""",
    )
    print(f"cards={len(enriched)} banks={len(banks)} programs={len(programs)} sources={len(sources)}")


if __name__ == "__main__":
    main()
