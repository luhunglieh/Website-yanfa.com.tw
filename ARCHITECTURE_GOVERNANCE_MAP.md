# 仰發科技專案架構、規範、雙平台安全邊界與檔案分層治理總簿 (`ARCHITECTURE_GOVERNANCE_MAP.md`)

> **文件位階**：專案最高全域導覽母檔 (Project Master Architecture & File Governance Map)  
> **適用標準**：Google Antigravity 2.0 原生客製化規範 + `GEMINI.md` 階層規範 + `.agent/skills/` 漸進式揭露  
> **發布端點**：GitHub (Private Security Zone) ＋ Cloudflare Pages / Edge CDN (`https://www.yanfa.com.tw/`)  
> **連動母檔**：[GEMINI.md](./GEMINI.md) ｜ [DEPLOY_SPEC.md](./DEPLOY_SPEC.md) ｜ [HARNESS_ENGINEERING.md](./HARNESS_ENGINEERING.md) ｜ [PROJECT_MASTER_DOCUMENT.md](./PROJECT_MASTER_DOCUMENT.md)  
> **最後更新**：2026-11-05

---

## 一、架構理念：資深 IT 與工程素養防禦縱深

本專案為 **仰發科技有限公司官方網站 (Website-yanfa.com.tw)**，專案主持與維運系統負責人為資深 IT 專家，全專案徹底杜絕業餘開發行為，以嚴格的六層架構（L0 至 L5）落實「小心翼翼、零機密洩漏、守護技術聲譽、雙平台權責分離」之專業精神。

```mermaid
flowchart TD
    subgraph L0["L0：本機全域層 (Machine Global) • 永遠常駐 (~220 Tokens)"]
        G0["C:/Users/User/.gemini/GEMINI.md<br/>個人溝通鐵律：繁體中文、直接給代碼、重視架構、無空話"]
    end

    subgraph L1["L1：專案常駐規則與雙平台防護層 (Workspace Always-On) • 啟動載入 (< 2,500 Tokens)"]
        G1["GEMINI.md (專案常駐)<br/>1. 網站代碼全面凍結紅線<br/>2. 商業機密防護邊界<br/>3. GitHub (Private) vs Edge CDN 雙平台權責<br/>4. 核心熱區行號索引 (Hot-Zone Line Index)"]
        G2[".geminiignore<br/>屏蔽 dist/、.astro/、node_modules/<br/>防止龐大編譯產物與依賴套件雙重檢索消耗 Token"]
        G3["ARCHITECTURE_GOVERNANCE_MAP.md (本檔)<br/>全專案檔案地圖、六層治理與標準維護 SOP"]
        G4["TOKEN_OPTIMIZATION_GLOBAL.md<br/>Token 審計與精簡數據、架構變更紀錄總簿"]
    end

    subgraph L2["L2：Antigravity 2.0 漸進式技能模組層 (Progressive Disclosure) • 平時 0 Token，按需調用"]
        S1[".agent/skills/node24-security-baseline/SKILL.md<br/>Node 24 Active LTS 資安基準、不可變 SHA、node_modules 清消"]
        S2[".agent/skills/yanfa-web-builder/SKILL.md<br/>Astro 靜態渲染、Tailwind 佈局、AEO 結構化標準規範"]
        S3[".agent/skills/seo-checker/SKILL.md<br/>SEO 關鍵字、AEO Schema.org 語意檢核、無障礙 Alt 掃描"]
        S4[".agent/skills/maintenance-bot/SKILL.md<br/>全站資源巡檢、WebP 圖片存在性、死鏈與壞軌檢測"]
    end

    subgraph L3["L3：領域業務與工程白皮書庫 (Domain Specs & Runbooks) • 平時 0 Token，由 L2 按需導航"]
        D1["PROJECT_MASTER_DOCUMENT.md (PRD 業務總體規格母檔)<br/>仰發科技企業定位、主被動元件代理經銷清單、AEO 關鍵字字典"]
        D2["DEPLOY_SPEC.md (雙平台部署與資安架構白皮書)<br/>GitHub Private 備份機制與 Cloudflare Pages / Edge 邊緣發布規範"]
        D3["HARNESS_ENGINEERING.md (測試線路與檢驗工程手冊)<br/>run_all_audits.py 整合測試線路、自癒程序與合格代碼判定"]
    end

    subgraph L4["L4：生產代碼與可執行腳本庫 (Production Code & Scripts) • 依 L1 行號索引微創編輯 (≤80行)"]
        C1["正式頁面 (Astro HTML5)<br/>src/pages/index.astro, brands.astro, dealer.astro"]
        C2["全域佈局與共用組件<br/>src/layouts/Layout.astro, src/components/{Header,Footer,BrandCard}.astro"]
        C3["資料中心 (Data Models)<br/>src/data/{site,brands,dealers}.ts"]
        C4["自動化腳本產線 (scripts/)<br/>scripts/run_all_audits.py, scripts/{seo,maintenance}/, enforce-node24.mjs"]
    end

    subgraph L5["L5：對話串跨進程記憶層 (Cross-Thread Memory)"]
        M1["CONVERSATION_MEMORY.md<br/>跨對話串進度交接母檔、凍結狀態鎖、巡檢 100% 紀錄"]
        M2["對話 Log 隱私隔離<br/>.gitignore 徹底阻絕 brain/、logs/、*.jsonl 上傳 Git"]
    end

    L0 --> L1
    L1 --> L2
    L2 --> L3
    L2 --> L4
    L1 --> L4
    L4 --> L5
```

---

## 二、全專案檔案矩陣與職責清冊

### 1. 規則、部署與工程規範 (Rules & Deployment)
| 檔案路徑 | 層級 | Antigravity 載入行為 | 主要職責 |
| :--- | :--- | :--- | :--- |
| `C:\Users\User\.gemini\GEMINI.md` | **L0** | 永遠全域載入 | 個人對話習慣：繁體中文、專家溝通、直接代碼。 |
| [GEMINI.md](./GEMINI.md) | **L1** | **專案常駐載入** | 專案總體規則：代碼凍結、商業機密防火牆、熱區行號索引。 |
| [.geminiignore](./.geminiignore) | **L1** | 搜尋引擎前置過濾 | 隔離 `dist/`、`.astro/`、`node_modules/`，杜絕 Token 浪費。 |
| [ARCHITECTURE_GOVERNANCE_MAP.md](./ARCHITECTURE_GOVERNANCE_MAP.md) | **L1** | 專案導覽母檔 | 全案件檔案地圖、六層架構圖、職責矩陣與標準維護程序。 |
| [TOKEN_OPTIMIZATION_GLOBAL.md](./TOKEN_OPTIMIZATION_GLOBAL.md) | **L1** | 治理日誌 | 記錄專案架構盤點、Token 精簡數據與歷次架構升級紀錄。 |
| [DEPLOY_SPEC.md](./DEPLOY_SPEC.md) | **L3** | 部署白皮書 | GitHub Private 與 Cloudflare Pages / Edge 雙平台職責分離與安全配置。 |
| [HARNESS_ENGINEERING.md](./HARNESS_ENGINEERING.md) | **L3** | 測試工程手冊 | 自動化測試線路、SEO/AEO 檢驗標準、資安標頭防線。 |

---

### 2. 漸進式技能層 (Progressive Disclosure Skills)
位於 `.agent/skills/`，平時僅注入 `name` 與 `description`（零 Token 負擔），依需求自動展開：

| 技能目錄 | 觸發時機 | 關聯腳本與目標 |
| :--- | :--- | :--- |
| `node24-security-baseline` | CI/CD 修改、套件安裝、版本審查 | `scripts/enforce-node24.mjs` 強制 Node 24 執行期與清消 |
| `yanfa-web-builder` | 網站頁面維護、Astro 元件調整、AEO 優化 | `PROJECT_MASTER_DOCUMENT.md`、`src/` 程式庫 |
| `seo-checker` | 檢核產業關鍵字、AEO Schema.org 語意 | `scripts/seo/check_seo.py` 產出 `SEO_REPORT.md` |
| `maintenance-bot` | 檢核內部壞軌、圖檔遺失、外部連結 | `scripts/maintenance/check_site.py` 產出 `MAINTENANCE_REPORT.md` |

---

### 3. 業務資料與生產代碼 (Domain Data & Production Code)
| 檔案路徑 | 層級 | 說明 |
| :--- | :--- | :--- |
| [PROJECT_MASTER_DOCUMENT.md](./PROJECT_MASTER_DOCUMENT.md) | **L3** | **專案最高業務規格書**：仰發科技公司定位、代理品牌陣容、經銷服務項目、AEO 關鍵字字典。 |
| `src/data/site.ts` | **L4** | 公司名稱、地址、電話、統編與全域導覽連結設定。 |
| `src/data/brands.ts` | **L4** | 9 大代理品牌資料庫（冠寶、義發、尼克森、友順、佳展、德微、邁斯、華太、瞻芯）。 |
| `src/data/dealers.ts` | **L4** | 5 大國際經銷夥伴資料庫（Littelfuse、Nichicon、Nippon Chemi-Con、Panasonic、Toshiba）。 |
| `src/layouts/Layout.astro` | **L4** | 核心佈局，內建 Anti-Clickjacking Frame-Busting、CSP 安全標頭、GA4 與 Schema.org JSON-LD。 |
| `src/pages/*.astro` | **L4** | 正式發布頁面（首頁、代理品牌、經銷服務）。 |
| `scripts/run_all_audits.py` | **L4** | 一鍵整合全站檢測流水線（Node 24、Astro Build、SEO/AEO、資源巡檢）。 |

---

### 4. 自動化維運工具 (Maintenance Tooling)
| 批次檔路徑 | 作用 |
| :--- | :--- |
| `backup.bat` | 建立專案 Git Bundle 鏡像與源碼壓縮包至 `..\Website-yanfa-Backups`。 |
| `deploy_github.bat` | 一鍵執行前置測試、Git Add、Commit 與 Push。 |
| `preview.bat` | 啟動本機 Astro 開發預覽伺服器 (`http://localhost:4321/`)。 |
| `stop.bat` | 終止運行中之 Astro/Node 本地預覽進程。 |

---

## 三、標準變更與維護 SOP

1. **規格先行 (Spec-First)**：
   - 任何產品型錄更新、代理品牌異動，必須先於 `PROJECT_MASTER_DOCUMENT.md` 定案確認，方可異動 `src/data/` 或頁面。
2. **切片微創 (Micro-Slice Edit)**：
   - 先查閱 `GEMINI.md` 之行號索引，以 `read_file(StartLine, EndLine)` 讀取指定行區間（≤ 80 行），使用 `edit_file` 精準置換。
3. **推前必檢 (Audit-Before-Push)**：
   - 每次提交前必須執行 `python scripts/run_all_audits.py`，保持全站 0 壞軌、0 遺失、SEO 100% 通過。
