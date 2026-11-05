#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unified Site Audit Runner (仰發科技全站綜合健康巡檢器)
整合 Node 24 資安基線、Astro 編譯驗證、SEO/AEO 檢測與全站連結/靜態資源完整度巡檢
"""

import sys
import subprocess
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent

def run_command(cmd, name: str) -> bool:
    print("=" * 60)
    print(f"🚀 開始執行：{name}")
    print(f"指令：{' '.join(cmd) if isinstance(cmd, list) else cmd}")
    print("=" * 60)
    try:
        res = subprocess.run(cmd, cwd=ROOT_DIR, shell=(isinstance(cmd, str) or sys.platform == 'win32'))
        return res.returncode == 0
    except Exception as e:
        print(f"❌ 執行失敗: {e}")
        return False

def main():
    print("\n🔍 仰發科技有限公司官方網站 (Website-yanfa.com.tw) 全站自動巡檢系統")
    print(f"專案根目錄：{ROOT_DIR}\n")

    # 1. Node 24 Security Baseline
    node24_ok = run_command(["node", "scripts/enforce-node24.mjs"], "1. Node 24 Active LTS 資安基準與 node_modules 清消")
    print("\n")

    # 2. Astro Production Build
    build_ok = run_command("npm run build", "2. Astro 生產環境靜態編譯驗證")
    print("\n")

    # 3. SEO & AEO Check
    seo_script = ROOT_DIR / "scripts" / "seo" / "check_seo.py"
    seo_ok = run_command([sys.executable, str(seo_script)], "3. SEO 關鍵字與 AEO 結構化資料審核")
    print("\n")

    # 4. Site Maintenance & Resource Integrity Check
    site_script = ROOT_DIR / "scripts" / "maintenance" / "check_site.py"
    site_ok = run_command([sys.executable, str(site_script)], "4. 全站連結與靜態資源完整度巡檢")

    print("\n" + "=" * 60)
    print("📋 仰發科技官方網站 全站巡檢最終執行摘要報告")
    print("=" * 60)
    print(f"• 1. Node 24 資安基線檢測 : {'✅ 100% 通過 (All Passed)' if node24_ok else '❌ 發現安全性錯誤'}")
    print(f"• 2. Astro 靜態編譯檢測   : {'✅ 100% 通過 (All Passed)' if build_ok else '❌ 編譯失敗'}")
    print(f"• 3. SEO / AEO 結構審核   : {'✅ 100% 通過 (All Passed)' if seo_ok else '❌ 發現警告或錯誤'}")
    print(f"• 4. 網站靜態資源巡檢     : {'✅ 100% 通過 (All Passed)' if site_ok else '❌ 發現壞軌或遺失檔案'}")
    print(f"• 報告輸出路徑           : SEO_REPORT.md ｜ MAINTENANCE_REPORT.md")
    print("=" * 60)

    if node24_ok and build_ok and seo_ok and site_ok:
        print("🎉 恭喜！全站程式碼、Node 24 資安基準、SEO 語意與素材資源皆處於頂級健康安全狀態！\n")
        sys.exit(0)
    else:
        print("⚠️ 巡檢發現未達標項目，請參閱上方日誌與報告進行修正。\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
