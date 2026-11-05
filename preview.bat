@echo off
chcp 65001 >nul
echo ========================================================
echo   仰發科技有限公司 官方網站 - 本地預覽啟動器 (Astro)
echo ========================================================
echo.

where npm >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [INFO] 正在啟動 Astro 開發預覽伺服器 (http://localhost:4321/)...
    start http://localhost:4321/
    npm run dev
) else (
    echo [ERROR] 系統未安裝或找不到 npm。
)
pause
