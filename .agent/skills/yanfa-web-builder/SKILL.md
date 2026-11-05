---
name: yanfa-web-builder
description: 仰發科技官方網站建置、Astro 靜態渲染、Tailwind CSS 佈局、AEO 語意與元件化架構規範技能。
---

# Yanfa Web Builder Skill
# 仰發科技官方網站建置與 AEO 運維技能

此技能專為「**仰發科技有限公司官方網站 (Website-yanfa.com.tw)**」量身打造，作為 AI Agent 深度理解全站 Astro 架構、維護前端元件、最佳化搜尋與 AI 答案引擎 (SEO/AEO) 之遵循綱領。

---

## 1. 核心專案規格與嚴格邊界 (Core Specifications & Boundary)

* **公司名稱**：`仰發科技有限公司` (Yanfa Technology Co., Ltd.)
* **正式網域**：`https://www.yanfa.com.tw/`
* **技術架構**：`Astro 4.x + Tailwind CSS 3.x + Node 24 Active LTS`
* **核心精神**：`專業半導體及電子零件代理與經銷商・服務至上`
* **主要業務範疇**：
  * MOSFET（高低壓金氧半場效電晶體）
  * 二極體 (Diode)、電晶體 (BJT)、三極體
  * 第三代半導體 SiC SBD & MOSFET
  * 鋁質電解電容、固態電容、貼片電感
  * LED、保護元件
* **代理原廠**：冠寶科技 (Jackcon)、義發科技 (EMC)、尼克森微電子 (Niko-Sem)、友順科技 (UTC)、佳展科技 (BRT)、德微科技 (Eris)、邁斯半導體 (Matrix)、華太電子 (CTE)、瞻芯電子 (Basic Semiconductor)
* **全球經銷夥伴**：Littelfuse, Nichicon, Nippon Chemi-Con, Panasonic, Toshiba

> [!CAUTION]
> **嚴格商業機密防護邊界**：
> - ❌ 內部產品報價單、客戶毛利與進貨成本絕不上網。
> - ❌ 內部客戶名單、未公開合作廠商簽約備忘錄嚴格禁止進入版本庫。
> - ❌ 不得擅自重構未授權之頁面結構或樣式系統。

---

## 2. 網站拓撲與頁面職責規範 (Website Topology)

```
Website-yanfa.com.tw/
├── src/
│   ├── components/
│   │   ├── Header.astro     # 頂部導覽列：Logo + 桌面導覽 + 手機漢堡選單
│   │   ├── Footer.astro     # 全站頁尾：公司聯絡資訊、交通、版權宣告
│   │   └── BrandCard.astro  # 代理原廠品牌卡片組件
│   ├── layouts/
│   │   └── Layout.astro     # 全域佈局：Frame-Busting、CSP、GA4、AEO Schema.org
│   ├── data/
│   │   ├── site.ts          # 全站基礎設定與導覽路徑
│   │   ├── brands.ts        # 代理品牌資料庫
│   │   └── dealers.ts       # 經銷夥伴資料庫
│   └── pages/
│       ├── index.astro      # 首頁：Hero Banner、服務理念、產品範疇、聯絡資訊
│       ├── brands.astro     # 代理品牌專頁：原廠 Logo、產品特色、原廠介紹
│       └── dealer.astro     # 經銷服務專頁：國際五大品牌經銷優勢、服務承諾
```

## 3. 開發與驗證指令
- 本地開發：`npm run dev` (http://localhost:4321/)
- 生產編譯：`npm run build` (輸出於 `dist/`)
- 全站巡檢：`python scripts/run_all_audits.py`
