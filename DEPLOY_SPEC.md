# 雙平台架構佈署與全維度資安白皮書 (`DEPLOY_SPEC.md`)

> **文件位階**：專案生產環境部署與資安架構最高規範 (L3 Domain Spec)  
> **適用架構**：GitHub (Private Code Repository) ＋ Cloudflare Pages / Edge CDN (Global Edge Distribution)  
> **發布端點**：`https://www.yanfa.com.tw/`  
> **最後更新**：2026-11-05

---

## 一、架構設計理念：資深 IT 的雙平台職責分離 (Separation of Concerns)

身為資深 IT 專家主持的企業官方網站，發布機制絕不採用業餘的「單一公開倉庫裸奔」模式，而是落實業界標準的**「雙平台職責分離」**與**「外網零原始碼暴露」**：

```mermaid
flowchart TD
    subgraph PrivateZone["【本機與 GitHub 私有安全區 (Private Security Zone)】"]
        Local["本機開發環境<br/>(Website-yanfa.com.tw)"]
        GitRepo["GitHub Private Repo<br/>(內部核心保險箱)"]
        PrivateData["未公開機密：<br/>• 內部產品報價單與毛利數據<br/>• 未公開客戶名單與合約<br/>• AI 提示規則與治理地圖<br/>• 完整 Git Commit 歷程"]
        
        Local -->|1. git push (安全認證)| GitRepo
        GitRepo --- PrivateData
    end

    subgraph BuildPipeline["【雲端獨立建置管線 (Isolated Build Sandbox)】"]
        Webhook["Cloudflare / GitHub CI<br/>(Webhook 即時感應)"]
        AstroBuild["Node 24 Active LTS<br/>• 執行 scripts/enforce-node24.mjs<br/>• npm run build (Astro 靜態編譯)"]
        SiteOutput["產出純靜態目錄：dist/<br/>(僅包含 HTML5, CSS, WebP, JSON-LD)"]
        
        GitRepo -->|2. Webhook 觸發拉取| Webhook
        Webhook --> AstroBuild
        AstroBuild --> SiteOutput
    end

    subgraph PublicZone["【全球公開邊緣節點 (Global Edge Distribution)】"]
        EdgeCDN["Cloudflare Global CDN<br/>• 台北 / 全球 Anycast 節點<br/>• 免費無限流量 & DDoS 防護<br/>• 啟用 HTTP/3 & TLS 1.3"]
        Visitor["全世界公眾訪客<br/>https://www.yanfa.com.tw/"]
        
        SiteOutput -->|3. 發布純 dist/| EdgeCDN
        EdgeCDN --> Visitor
    end
```

---

## 二、平台職責邊界矩陣 (Responsibility Boundary Matrix)

| 治理維度 | GitHub (私有端) | Cloudflare Pages / Edge CDN (公開端) |
| :--- | :--- | :--- |
| **可見性 (Visibility)** | **100% Private (僅負責人帳號授權可見)** | **100% Public (全球公眾存取)** |
| **核心職責** | 完整原始碼管理、版本歷史追蹤、雲端災難備份、內部行政與巡檢腳本存放。 | 靜態 HTML/CSS/WebP 渲染、全球 CDN 快取、DDoS 阻斷、SSL 憑證簽發。 |
| **外網暴露檔案** | **0 (外網無法直連任何 Git 檔案)** | **僅限 `dist/` 目錄下的純靜態編譯產物**。 |
| **敏感資產保護** | 透過 `.gitignore` 阻絕底層對話 Log（`*.jsonl`）、Token 統計簿與本機暫存。 | 內部腳本（`scripts/`）、規格文件、規則（`GEMINI.md`）完全不發布。 |
| **自訂網域彈性** | 不適用。 | 綁定正式網域 `www.yanfa.com.tw`，提供自動 HSTS 與現代 TLS 加密。 |

---

## 三、建置與部署標準規範 (Build & Deploy Specs)

### 1. Cloudflare Pages 專案配置標準
- **Project name**：`website-yanfa-com-tw`
- **Production branch**：`master` (或 `main`)
- **Framework preset**：`Astro`
- **Build command**：`npm run build`
- **Build output directory**：`dist`
- **Root directory**：`/`
- **Environment variables**：
  - `NODE_VERSION` = `24.0.0`
  - `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24` = `true`

### 2. GitHub Actions CI/CD 最小權限與不可變 SHA 規範
如採用 GitHub Pages 或 GitHub Actions 進行中轉發布，必須遵循 `.agent/skills/node24-security-baseline` 規範：
- 鎖定不可變 40 位元 Commit SHA。
- 嚴格落實最小權限：`build` 僅限 `contents: read`，`deploy` 僅限 `pages: write` 與 `id-token: write`。

---

## 四、資安防禦縱深與安全標頭規範 (Security Headers)

全站於 `src/layouts/Layout.astro` 與 `_headers` 實施 OWASP 等級資安強化：

1. **Anti-Clickjacking 防點擊劫持 (Frame-Busting)**：
   ```html
   <style id="anti-clickjack" is:inline>body{display:none !important;}</style>
   <script is:inline>
     if (self === top) {
       var antiClickjack = document.getElementById('anti-clickjack');
       if (antiClickjack) antiClickjack.parentNode.removeChild(antiClickjack);
     } else {
       top.location = self.location;
     }
   </script>
   ```

2. **嚴格內容安全策略 (Content-Security-Policy)**：
   ```http
   Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' data: https://fonts.gstatic.com; img-src 'self' data: https://www.googletagmanager.com https://*.google-analytics.com; connect-src 'self' https://*.google-analytics.com https://analytics.google.com https://stats.g.doubleclick.net; frame-src 'none'; object-src 'none'; base-uri 'self'; form-action 'self';
   ```

3. **MIME 嗅探防禦**：`X-Content-Type-Options: nosniff`。
4. **推薦來源保護**：`Referrer-Policy: strict-origin-when-cross-origin`。
5. **瀏覽器特徵權限限制**：`Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()`。
6. **強制安全傳輸 (HSTS)**：`Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`。
