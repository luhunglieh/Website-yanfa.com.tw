#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO & AEO Schema.org Semantic Checker (SEO / AEO 結構化資料審核器)
針對仰發科技官方網站產出之 HTML 進行 SEO 關鍵字、AEO Schema.org、Title、Meta 與圖片 Alt 檢驗
"""

import os
import sys
import re
import subprocess
from pathlib import Path
from datetime import datetime

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DIST_DIR = ROOT_DIR / "dist"
REPORT_FILE = ROOT_DIR / "SEO_REPORT.md"

KEYWORDS_TO_CHECK = [
    '仰發科技',
    '半導體',
    'MOSFET',
    '電晶體',
    '二極體',
    '電解電容',
    '固態電容',
    'SiC',
    '代理',
    '經銷'
]

def ensure_build():
    if not DIST_DIR.exists() or not (DIST_DIR / "index.html").exists():
        print("⚡ [INFO] dist 目錄尚未建立，正在執行 npm run build...")
        subprocess.run(["npm", "run", "build"], cwd=ROOT_DIR, check=True)

def find_html_files():
    html_files = []
    if DIST_DIR.exists():
        for p in DIST_DIR.rglob("*.html"):
            html_files.append(p)
    return sorted(html_files)

def check_seo_on_file(filepath: Path):
    rel_path = filepath.relative_to(ROOT_DIR).as_posix()
    results = {
        'file': rel_path,
        'title': None,
        'description': None,
        'canonical': None,
        'og_title': None,
        'og_desc': None,
        'has_schema': False,
        'schema_types': [],
        'missing_alts': [],
        'keyword_counts': {kw: 0 for kw in KEYWORDS_TO_CHECK}
    }

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if BeautifulSoup:
            soup = BeautifulSoup(content, 'html.parser')
            
            # Title
            title_tag = soup.find('title')
            if title_tag and title_tag.text:
                results['title'] = title_tag.text.strip()
            
            # Description
            desc_tag = soup.find('meta', attrs={'name': 'description'})
            if desc_tag and desc_tag.get('content'):
                results['description'] = desc_tag['content'].strip()

            # Canonical
            canon_tag = soup.find('link', attrs={'rel': 'canonical'})
            if canon_tag and canon_tag.get('href'):
                results['canonical'] = canon_tag['href'].strip()

            # OG Title & Desc
            og_t = soup.find('meta', attrs={'property': 'og:title'})
            if og_t:
                results['og_title'] = og_t.get('content', '').strip()
            og_d = soup.find('meta', attrs={'property': 'og:description'})
            if og_d:
                results['og_desc'] = og_d.get('content', '').strip()

            # Schema.org JSON-LD
            for s in soup.find_all('script', type='application/ld+json'):
                results['has_schema'] = True
                s_text = s.string or ""
                matches = re.findall(r'"@type"\s*:\s*"([^"]+)"', s_text)
                results['schema_types'].extend(matches)

            # Missing Alt
            for img in soup.find_all('img'):
                alt = img.get('alt')
                if alt is None or not str(alt).strip():
                    results['missing_alts'].append(img.get('src', 'unknown'))
        else:
            # Fallback regex
            t_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            results['title'] = t_m.group(1).strip() if t_m else None
            d_m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', content, re.IGNORECASE)
            results['description'] = d_m.group(1).strip() if d_m else None
            if 'application/ld+json' in content:
                results['has_schema'] = True

        # Keyword counts
        for kw in KEYWORDS_TO_CHECK:
            results['keyword_counts'][kw] = len(re.findall(re.escape(kw), content, re.IGNORECASE))

    except Exception as e:
        results['error'] = str(e)

    return results

def main():
    print("=" * 60)
    print("🚀 [1/2] 正在執行 SEO / AEO 結構化資料審核...")
    print("=" * 60)

    ensure_build()
    html_files = find_html_files()

    if not html_files:
        print("❌ [ERROR] 未找到任何 HTML 檔案！")
        sys.exit(1)

    all_results = [check_seo_on_file(f) for f in html_files]

    total_pages = len(all_results)
    pages_with_title = sum(1 for r in all_results if r.get('title'))
    pages_with_desc = sum(1 for r in all_results if r.get('description'))
    pages_with_schema = sum(1 for r in all_results if r.get('has_schema'))
    total_missing_alts = sum(len(r.get('missing_alts', [])) for r in all_results)

    # Output report
    report_lines = [
        "# 仰發科技官方網站 SEO & AEO 全站健康檢測報告",
        "",
        f"> **檢測時間**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ",
        f"> **受測端點**：`https://www.yanfa.com.tw/` ｜ **編譯產物**：`dist/`  ",
        f"> **工程規範**：[HARNESS_ENGINEERING.md](./HARNESS_ENGINEERING.md) ｜ [DEPLOY_SPEC.md](./DEPLOY_SPEC.md)  ",
        "",
        "---",
        "",
        "## 一、檢驗指標統計摘要",
        "",
        f"- **受測 HTML 頁面數**：{total_pages} 頁",
        f"- **Title 標籤具備率**：{pages_with_title}/{total_pages} ({'✅ 100%' if pages_with_title == total_pages else '⚠️ 未達標'})",
        f"- **Meta Description 具備率**：{pages_with_desc}/{total_pages} ({'✅ 100%' if pages_with_desc == total_pages else '⚠️ 未達標'})",
        f"- **AEO Schema.org 語意具備率**：{pages_with_schema}/{total_pages} ({'✅ 100%' if pages_with_schema == total_pages else '⚠️ 未達標'})",
        f"- **圖片無障礙 Alt 缺失數**：{total_missing_alts} 處 ({'✅ 0 缺失' if total_missing_alts == 0 else f'⚠️ 發現 {total_missing_alts} 處缺漏'})",
        "",
        "---",
        "",
        "## 二、各頁面詳細檢驗結果",
        "",
        "| 檔案路徑 | Title 標題 | Meta Description | AEO 結構型別 | Alt 缺失數 |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]

    for r in all_results:
        t_status = f"`{r['title'][:25]}...`" if r.get('title') else "❌ MISSING"
        d_status = "✅ 具備" if r.get('description') else "❌ MISSING"
        schema_types = ", ".join(set(r.get('schema_types', []))) if r.get('schema_types') else ("✅ 具備" if r.get('has_schema') else "❌ MISSING")
        alt_status = f"✅ 0" if len(r.get('missing_alts', [])) == 0 else f"⚠️ {len(r['missing_alts'])}"
        report_lines.append(f"| `{r['file']}` | {t_status} | {d_status} | {schema_types} | {alt_status} |")

    report_lines.extend([
        "",
        "---",
        "",
        "## 三、核心業務關鍵字密度分佈",
        "",
        "| 頁面檔案 | " + " | ".join(KEYWORDS_TO_CHECK) + " |",
        "| :--- | " + " | ".join([":---:"] * len(KEYWORDS_TO_CHECK)) + " |"
    ])

    for r in all_results:
        counts = [str(r['keyword_counts'][kw]) for kw in KEYWORDS_TO_CHECK]
        report_lines.append(f"| `{r['file']}` | " + " | ".join(counts) + " |")

    report_lines.append("\n---\n*報告自動產出於 Antigravity Test Harness 工業級管線。*\n")

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))

    print(f"📊 檢測總結：頁面 {total_pages} 頁，Title: {pages_with_title}/{total_pages}，Desc: {pages_with_desc}/{total_pages}，AEO Schema: {pages_with_schema}/{total_pages}，Alt 缺失: {total_missing_alts}")
    print(f"📄 報告已寫入：{REPORT_FILE}")

    if pages_with_title == total_pages and pages_with_desc == total_pages and pages_with_schema == total_pages and total_missing_alts == 0:
        print("✅ [SEO / AEO] 100% 通過驗收！\n")
        return 0
    else:
        print("⚠️ [SEO / AEO] 發現未達標項目，請參閱報告。\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
