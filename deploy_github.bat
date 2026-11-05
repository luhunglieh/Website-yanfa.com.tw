@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ========================================================
echo   仰發科技官方網站 - 一鍵推送至 GitHub (Website-yanfa.com.tw)
echo ========================================================
echo.

where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] 系統未安裝或找不到 Git，請先確認 Git 環境變數。
    pause
    exit /b 1
)

echo [0/5] 執行全站線路測試與資安檢驗 (Run All Audits)...
python scripts/run_all_audits.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [BLOCKED] 檢驗未通過！請修正錯誤後再行提交。
    pause
    exit /b 1
)

echo.
echo [1/5] 檢查 Git 工作區狀態...
git status --short

echo.
set "COMMIT_MSG="
set /p COMMIT_MSG="請輸入本次提交摘要（直接按 Enter 則使用自動時間戳記）: "
if "%COMMIT_MSG%"=="" (
    for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss'"`) do set "COMMIT_MSG=update: %%i"
)

echo.
echo [2/5] 加入所有變更檔案至暫存區...
git add -A

echo.
echo [3/5] 建立版本提交 (Commit)...
git commit -m "%COMMIT_MSG%"

echo.
echo [4/5] 正在取得當前分支名稱...
for /f "usebackq delims=" %%b in (`git branch --show-current`) do set "CURRENT_BRANCH=%%b"
if "%CURRENT_BRANCH%"=="" set "CURRENT_BRANCH=master"

echo.
echo [5/5] 推送至 GitHub (origin %CURRENT_BRANCH%)...
git push origin %CURRENT_BRANCH%

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo   推送成功！
    echo   分支名稱: %CURRENT_BRANCH%
    echo   正式站台: https://www.yanfa.com.tw/
    echo ========================================================
) else (
    echo.
    echo [ERROR] 推送失敗，請檢查權限或網路連線。
)
pause
