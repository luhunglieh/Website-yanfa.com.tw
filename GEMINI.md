# Project Global Rules & Architecture Index (`Website-yanfa.com.tw`)

> **Antigravity 2.0 Native Always-On Workspace Rule (`GEMINI.md`)**  
> Master Architecture Map: [ARCHITECTURE_GOVERNANCE_MAP.md](./ARCHITECTURE_GOVERNANCE_MAP.md) | Token Audit & Change Log: [TOKEN_OPTIMIZATION_GLOBAL.md](./TOKEN_OPTIMIZATION_GLOBAL.md)  
> Master Project Spec: [PROJECT_MASTER_DOCUMENT.md](./PROJECT_MASTER_DOCUMENT.md) | Cross-Thread Memory: [CONVERSATION_MEMORY.md](./CONVERSATION_MEMORY.md)  
> Deployment & Security Blueprint: [DEPLOY_SPEC.md](./DEPLOY_SPEC.md) | Test Harness Engineering: [HARNESS_ENGINEERING.md](./HARNESS_ENGINEERING.md)  

---

## 1. 最高指導原則：資深 IT 工程素養與絕對資安紀律

> [!CAUTION]
> **「小心翼翼、零容忍資安洩漏、守護技術聲譽」**  
> 專案負責人為資深 IT 專家（CIO/資深系統架構師），公開發布之企業專案代表極高專業水準，絕不可表現出業餘或欠缺資安思維之行為。  
> 所有架構決策、權限邊界、代碼撰寫與外網暴露面，均須落實國防級防禦縱深（Defense-in-Depth）。

### 1.1 核心架構職責切割（GitHub vs Cloudflare Pages / Edge CDN）
- **GitHub 職責（私有保險箱）**：
  - **屬性**：**嚴格設為 Private Repository**。
  - **任務**：唯一的核心原始碼存放、Git 分支版控、全歷史備份、開發與自動化檢測腳本、商業合作數據存放地。
  - **嚴格防線**：透過 `.gitignore` 嚴格阻絕對話軌跡（`*.jsonl`）、Token 統計簿、本機日誌與快取。
- **Cloudflare Pages / Edge CDN 職責（全球公開展示櫃檯）**：
  - **屬性**：**公開 CDN 邊緣分發 (`https://www.yanfa.com.tw/`)**。
  - **任務**：拉取 Private Repo 中 Astro 原始碼，於獨立雲端容器執行 `npm run build`，**僅將純靜態產物 `dist/` 發布至外網**。
  - **隔離保證**：所有 Python 巡檢腳本、內部名冊與報價、AI 治理規格、批次檔均留在建置層外，**外網 0 機密暴露**。

---

## 2. Top-to-Bottom (L0 -> L5) 六層檔案治理層級

嚴格遵循 Antigravity 2.0 階層規範，絕不在層級外建立散亂檔案：

| Layer | Scope | Path / Location | Antigravity 2.0 Loading Behavior | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **L0** | **Machine Global** | `C:\Users\User\.gemini\GEMINI.md` | **Always-On (Global)** | 繁體中文、直接代碼、不說空話、專家視角、重視工程論證。 |
| **L1** | **Workspace Always-On Rules & Protection** | `./GEMINI.md` (本檔)<br>`./.geminiignore`<br>`./ARCHITECTURE_GOVERNANCE_MAP.md` | **Always-On (Workspace)**<br>(共享 20K Tokens 預算) | 專案紅線、雙平台安全邊界、低 Token 切片編輯守則、核心行號熱區索引。 |
| **L2** | **Progressive Disclosure Skills** | `.agent/skills/<skill-name>/SKILL.md`<br>1. `node24-security-baseline`<br>2. `yanfa-web-builder`<br>3. `seo-checker`<br>4. `maintenance-bot` | **On-Demand (0 Idle Tokens)**<br>(靜態時僅載入名稱與描述) | 模組化任務調度：<br>• Node 24 資安基準與依賴清消<br>• Astro + Tailwind 元件建置<br>• SEO/AEO 關鍵字語意審核<br>• 資源與連結健康巡檢 |
| **L3** | **Domain Specs & Engineering Runbooks** | `./PROJECT_MASTER_DOCUMENT.md`<br>`./DEPLOY_SPEC.md`<br>`./HARNESS_ENGINEERING.md` | **Read-On-Demand via L2 Links**<br>(0 Idle Tokens) | PRD 業務總規、雙平台部署架構、靜態網頁驗證線、半導體經銷規格。 |
| **L4** | **Source Code & Executable Scripts** | `./src/pages/*.astro`<br>`./src/layouts/`, `./src/components/`<br>`./src/data/*.ts`<br>`./scripts/run_all_audits.py`<br>`./scripts/{seo,maintenance}/` | **Targeted Slice Read Only**<br>(`read_file` ≤ 80 lines + `edit_file`) | 生產代碼、Astro 模板、自動化巡檢腳本與資料庫。透過行號索引精準微創。 |
| **L5** | **Conversation Memory & Cross-Thread Ledger** | `./CONVERSATION_MEMORY.md`<br>`<appDataDir>\brain\<conv-id>\{task,walkthrough}.md` | **Conversation-Scoped** | 跨對話串進度交接母檔、凍結狀態鎖。禁止將對話軌跡（`*.jsonl`）上傳至 Git。 |

---

## 3. 絕對安全防護紅線（資深架構師級守則）

1. **正式網站代碼全面凍結原則 (`Website Codebase Frozen Lock`)**：
   - 全站 3 大頁面（首頁、代理品牌、經銷服務）、CSS 樣式表、Header 導覽與 Footer 頁尾均已通過驗證並上線。
   - **零未授權重構**：嚴禁擅自調整 HTML/Astro 結構、Tailwind 樣式或修改導覽連結，所有修改須有使用者明確指令。
2. **商業機密防護邊界 (`Business Confidential Boundary`)**：
   - 產品內部報價、進貨成本、原廠代理合約未公開細節、經銷商返利機制均屬商業機密。
   - **嚴禁登載於公開網頁、嚴禁推入外網部署產物**。
3. **對話日誌與 Token 檔案完全隔離 (`Conversation Log Privacy Gate`)**：
   - `brain/`、`logs/`、`*.jsonl`、`transcript*.jsonl`、`CONVERSATION_MEMORY.md` 必須被 `.gitignore` 徹底遮蔽，絕不進入 Git。
4. **先改規格文件、後改程式碼鐵律 (`Spec-First Iron Law`)**：
   - 任何產品型號增減、代理品牌更新、經銷夥伴異動，必須先於 `PROJECT_MASTER_DOCUMENT.md` 定案確認，方可異動 `src/data/*.ts` 或頁面。
5. **部署標準化驗證 (`Audit-Before-Push Law`)**：
   - 每次 Commit 與 Push 前必須執行 `python scripts/run_all_audits.py`，確保 Node 24 基準、Astro 編譯、SEO/AEO 結構化資料、資源與連結 100% 通過。
6. **Node 24 Active LTS 資安基準 (`Node 24 Mandatory Security`)**：
   - 全面棄用已 EOL 之 Node 18 與 Node 20，CI/CD 與本機全面綁定 Node 24。

---

## 4. 核心程式碼熱區行號索引 (Codebase Hot-Zone Line Index)

進行任何代碼微調，必須先查閱此行號表，使用 `read_file(StartLine, EndLine)` 切片（≤ 80 行），並以 `edit_file` 精準置換：

### 4.1 核心設定與全域佈局
- **`astro.config.mjs`** (15 行):
  - `L5 - L8`: 網域宣告 (`site: "https://www.yanfa.com.tw"`)、路徑 base 與 Tailwind 整合
  - `L9 - L14`: 開發工具列關閉與 build format (`directory`)
- **`src/layouts/Layout.astro`** (125 行):
  - `L22 - L28`: HTML5 根宣告、語系 (`zh-TW`)、標題、描述、Canonical URL
  - `L30 - L35`: 現代 Favicon 與 Apple Touch Icons
  - `L37 - L42`: Open Graph 社交中繼標籤 (og:title, og:desc, og:url, og:site_name)
  - `L44 - L47`: CSP 企業級內容安全策略、Nosniff、Referrer-Policy
  - `L49 - L57`: OWASP Anti-Clickjacking Frame-Busting 防點擊劫持防線
  - `L59 - L98`: AEO Schema.org 語意標記 (`Organization`, `WebSite`, `ContactPoint`)
  - `L100 - L103`: Google Fonts 預先連線 (Noto Sans TC, Roboto)
  - `L105 - L116`: Google Analytics 4 (GA4: `G-TQDJH1PPH4`)

### 4.2 資料庫驅動核心 (Data Models)
- **`src/data/site.ts`** (31 行):
  - `L15 - L31`: 全站全域參數（公司名稱、電話、傳真、Email、地址、Google Maps 連結、導覽列選單）
- **`src/data/brands.ts`** (92 行):
  - `L1 - L92`: 9 大代理品牌資料庫（冠寶 Jackcon、義發 EMC、尼克森 Niko-Sem、友順 UTC、佳展 BRT、德微 Eris、邁斯 Matrix、華太 CTE、瞻芯 Basic Semiconductor）
- **`src/data/dealers.ts`** (56 行):
  - `L1 - L56`: 5 大國際經銷夥伴資料庫（Littelfuse、Nichicon、Nippon Chemi-Con、Panasonic、Toshiba）

### 4.3 共用組件 (Components)
- **`src/components/Header.astro`** (130 行):
  - `L15 - L45`: 頂部導覽 Header、品牌 Logo、桌機版導覽選單
  - `L46 - L70`: 行動裝置漢堡選單按鈕與下拉選單容器
  - `L71 - L130`: 漢堡選單展開/收合互動 JavaScript
- **`src/components/Footer.astro`** (112 行):
  - `L15 - L50`: 品牌簡介、快速導覽連結
  - `L51 - L85`: 公司詳細聯絡資訊、地址、電話、傳真、Email
  - `L86 - L112`: 底部草地裝飾圖 (`footer-grass-v2.webp`) 與版權宣告
- **`src/components/BrandCard.astro`** (51 行):
  - `L1 - L51`: 原廠品牌卡片組件、Logo 渲染、代理產品範疇標籤與介紹

### 4.4 正式發布頁面 (Pages)
- **`src/pages/index.astro`** (206 行):
  - `L16 - L52`: Hero Banner（服務 / 您的需求最優先）、代理與經銷雙 CTA 按鈕
  - `L54 - L110`: 關於仰發科技、企業核心宗旨、專業代理服務
  - `L112 - L175`: 核心產品類別卡片（MOSFET、電晶體、二極體、電容、LED、SiC）
  - `L176 - L206`: 底部行動呼籲 (CTA) 與專屬聯絡諮詢按鈕
- **`src/pages/brands.astro`** (70 行):
  - `L10 - L35`: 代理品牌頁面 Hero Banner、原廠授權代理定位
  - `L36 - L70`: 9 大代理品牌網格佈局渲染 (`brands.map(brand => <BrandCard />)`)
- **`src/pages/dealer.astro`** (61 行):
  - `L10 - L30`: 經銷服務頁面 Hero Banner、全球供應鏈整合優勢
  - `L31 - L61`: 國際五大經銷夥伴品牌卡片、原廠品質保證說明
