---
name: seo-checker
description: 仰發科技官方網站 SEO 關鍵字、AEO Schema.org 結構化資料、Meta 標籤與圖片無障礙 Alt 巡檢技能。
---

# SEO & AEO Checker Skill (仰發科技官方網站專屬)

此技能專為「**仰發科技有限公司官方網站 (Website-yanfa.com.tw)**」設計，負責檢驗全站頁面 SEO 體質與 AEO (AI 答案引擎) 結構化語意標記，確保各大搜尋引擎與 AI 爬蟲能精準擷取半導體與電子零件代理經銷權威內容。

## 功能特色
- **Meta 標籤檢查**：驗證每頁 `<title>`、`<meta name="description">`、`<link rel="canonical">` 是否齊備且合宜。
- **AEO Schema.org 偵測**：自動偵測頁面是否注入 JSON-LD 結構化資料（如 `Organization`、`WebSite`、`ContactPoint`、`PostalAddress`）。
- **無障礙與 SEO Alt 掃描**：揪出所有未設定 `alt` 屬性或屬性空白之 `<img>` 標籤，確保 100% 覆蓋。
- **半導體產業關鍵字覆蓋密度分析**：統計核心關鍵詞（包含：`仰發科技`、`半導體`、`MOSFET`、`電晶體`、`二極體`、`電解電容`、`固態電容`、`SiC`、`代理`、`經銷`）於全站頁面之出現頻率。
- **自動產出報告**：自動產生 Markdown 格式報告 `SEO_REPORT.md`。

## 檢查涵蓋頁面
1. `src/pages/index.astro`（首頁 - 關於仰發、服務理念、產品範疇）
2. `src/pages/brands.astro`（代理品牌 - 冠寶、義發、尼克森、友順、佳展、德微、邁斯、華太、瞻芯）
3. `src/pages/dealer.astro`（經銷服務 - Littelfuse、Nichicon、Nippon Chemi-Con、Panasonic、Toshiba）

## 使用方式
於專案根目錄執行：
```bash
python scripts/seo/check_seo.py
```
