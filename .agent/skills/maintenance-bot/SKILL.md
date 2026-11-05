---
name: maintenance-bot
description: 仰發科技官方網站自動巡檢技能，掃描內部連結、外部超連結與 WebP/CSS/JS 靜態資源載入完整度。
---

# Maintenance Bot Skill (仰發科技官方網站專屬)

此技能負責全面巡檢仰發科技官方網站的內部連結、圖片資源（WebP）、樣式腳本及外部原廠/夥伴超連結，確保訪客瀏覽體驗順暢、無 404 或死鏈問題。

## 功能特色
- **死鏈偵測**：掃描全站編譯產物 `dist/`，驗證內部導覽與錨點路徑正確性。
- **本地靜態資源檢查**：檢查 `<img>` 的 `src`、`<script>`、`<link>` 是否均正確對應本地實體檔案（WebP 圖檔、CSS、JS）。
- **外部連結檢驗**：發送安全探測檢核原廠官網與合作夥伴連結存活狀態。
- **自動化 Markdown 報告**：產出 `MAINTENANCE_REPORT.md`，統整健康度評分與異常清單。

## 使用方式
於專案根目錄執行：
```bash
python scripts/maintenance/check_site.py
```
