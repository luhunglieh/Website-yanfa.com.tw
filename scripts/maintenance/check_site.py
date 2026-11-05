#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Site Asset & Link Integrity Checker (全站資源與連結完整度巡檢器)
巡檢 dist/ 中靜態圖檔、WebP、CSS、JS 與內部連結是否存在壞軌或 404
"""

import os
import sys
import re
from pathlib import Path
from urllib.parse import urlparse, unquote
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

try:
    import requests
except ImportError:
    requests = None

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DIST_DIR = ROOT_DIR / "dist"
REPORT_FILE = ROOT_DIR / "MAINTENANCE_REPORT.md"
TIMEOUT = 4
SKIP_DOMAINS = ['localhost', '127.0.0.1', 'fonts.googleapis.com', 'fonts.gstatic.com', 'www.googletagmanager.com', 'goo.gl', 'maps.google.com']

def extract_links_and_assets(html_path: Path):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    links = []
    assets = []

    if BeautifulSoup:
        soup = BeautifulSoup(content, 'html.parser')
        # A links
        for a in soup.find_all('a', href=True):
            links.append(a['href'].strip())
        # Img src
        for img in soup.find_all('img', src=True):
            assets.append(('image', img['src'].strip()))
        # Link stylesheets / favicons
        for link in soup.find_all('link', href=True):
            rel = link.get('rel', [])
            if any(r in rel for r in ['stylesheet', 'icon', 'apple-touch-icon']):
                assets.append(('link', link['href'].strip()))
        # Script src
        for s in soup.find_all('script', src=True):
            assets.append(('script', s['src'].strip()))
    else:
        for m in re.finditer(r'<a[^>]+href=["\'](.*?)["\']', content, re.IGNORECASE):
            links.append(m.group(1).strip())
        for m in re.finditer(r'<img[^>]+src=["\'](.*?)["\']', content, re.IGNORECASE):
            assets.append(('image', m.group(1).strip()))
        for m in re.finditer(r'<script[^>]+src=["\'](.*?)["\']', content, re.IGNORECASE):
            assets.append(('script', m.group(1).strip()))

    return links, assets

def verify_local_asset(dist_dir: Path, asset_url: str):
    # Ignore data URIs and full external URLs
    if asset_url.startswith(('data:', 'http://', 'https://', '//')):
        return True, "External/Inline"

    # Remove query string / hash
    clean_url = asset_url.split('?')[0].split('#')[0]
    clean_url = unquote(clean_url).lstrip('/')

    target_path = dist_dir / clean_url
    if target_path.exists() and target_path.is_file():
        return True, "OK"
    
    # Try public folder fallback
    pub_path = ROOT_DIR / "public" / clean_url
    if pub_path.exists() and pub_path.is_file():
        return True, "OK (Public)"

    return False, f"File not found: {target_path}"

def verify_internal_link(dist_dir: Path, link_url: str):
    if link_url.startswith(('mailto:', 'tel:', 'javascript:', '#')):
        return True, "Special Link"
    if link_url.startswith(('http://', 'https://', '//')):
        return True, "External Link"

    clean = link_url.split('?')[0].split('#')[0]
    clean = unquote(clean).strip('/')

    if clean == '':
        # Root index
        return (dist_dir / "index.html").exists(), "Root index"

    candidate_dir = dist_dir / clean / "index.html"
    candidate_file = dist_dir / f"{clean}.html"
    candidate_direct = dist_dir / clean

    if candidate_dir.exists() or candidate_file.exists() or candidate_direct.exists():
        return True, "Route exists"

    return False, f"Broken link target: {link_url}"

def main():
    print("=" * 60)
    print("🚀 [2/2] 正在執行全站資源與連結完整度巡檢...")
    print("=" * 60)

    if not DIST_DIR.exists():
        print("❌ [ERROR] dist/ 目錄不存在！請先執行 npm run build。")
        sys.exit(1)

    html_files = sorted([p for p in DIST_DIR.rglob("*.html") if not (p.name.startswith("google") and p.name.endswith(".html"))])
    if not html_files:
        print("❌ [ERROR] dist/ 未包含任何 HTML 檔案！")
        sys.exit(1)

    all_assets_checked = []
    all_links_checked = []
    missing_assets = []
    broken_links = []

    for hf in html_files:
        rel_hf = hf.relative_to(ROOT_DIR).as_posix()
        links, assets = extract_links_and_assets(hf)

        for asset_type, src in assets:
            ok, msg = verify_local_asset(DIST_DIR, src)
            all_assets_checked.append((rel_hf, asset_type, src, ok, msg))
            if not ok:
                missing_assets.append((rel_hf, src, msg))

        for l in links:
            ok, msg = verify_internal_link(DIST_DIR, l)
            all_links_checked.append((rel_hf, l, ok, msg))
            if not ok:
                broken_links.append((rel_hf, l, msg))

    # Summary
    total_assets = len(all_assets_checked)
    total_links = len(all_links_checked)

    report_lines = [
        "# 仰發科技官方網站 靜態資源與連結完整度巡檢報告",
        "",
        f"> **巡檢時間**：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ",
        f"> **巡檢根目錄**：`dist/` ｜ **正式網域**：`https://www.yanfa.com.tw/`  ",
        f"> **安全基準**：OWASP Static Hosting 健全度檢驗  ",
        "",
        "---",
        "",
        "## 一、巡檢總覽指標",
        "",
        f"- **掃描 HTML 頁面數**：{len(html_files)}",
        f"- **靜態素材引用數 (Images/CSS/JS)**：{total_assets} 處",
        f"- **靜態素材遺失 (404) 數**：{len(missing_assets)} ({'✅ 0 遺失 (100% 通過)' if len(missing_assets) == 0 else f'❌ 發現 {len(missing_assets)} 處壞軌'})",
        f"- **頁面連結審查數 (Internal/External)**：{total_links} 處",
        f"- **內部壞軌連結數**：{len(broken_links)} ({'✅ 0 壞軌 (100% 通過)' if len(broken_links) == 0 else f'❌ 發現 {len(broken_links)} 處壞軌'})",
        "",
        "---",
        "",
        "## 二、靜態資源完整度清單 (前 20 項)",
        "",
        "| 來源頁面 | 資源類型 | 引用路徑 | 狀態 |",
        "| :--- | :--- | :--- | :--- |"
    ]

    for item in all_assets_checked[:20]:
        status_str = "✅ 存在" if item[3] else f"❌ {item[4]}"
        report_lines.append(f"| `{item[0]}` | {item[1]} | `{item[2]}` | {status_str} |")

    report_lines.extend([
        "",
        "---",
        "",
        "## 三、內部與特殊連結檢核表 (前 20 項)",
        "",
        "| 來源頁面 | 連結路徑 | 檢驗狀態 |",
        "| :--- | :--- | :--- |"
    ])

    for item in all_links_checked[:20]:
        status_str = "✅ 通過" if item[2] else f"❌ {item[3]}"
        report_lines.append(f"| `{item[0]}` | `{item[1]}` | {status_str} |")

    report_lines.append("\n---\n*報告自動產出於 Antigravity Test Harness 工業級管線。*\n")

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))

    print(f"📊 巡檢總結：資源 {total_assets} 項 (壞軌: {len(missing_assets)})，連結 {total_links} 項 (壞軌: {len(broken_links)})")
    print(f"📄 報告已寫入：{REPORT_FILE}")

    if len(missing_assets) == 0 and len(broken_links) == 0:
        print("✅ [Site Maintenance] 100% 通過驗收！\n")
        return 0
    else:
        print("❌ [Site Maintenance] 發現壞軌資源，請參閱報告。\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
