@echo off
chcp 65001 >nul
echo ========================================================
echo   仰發科技有限公司 官方網站 - 終止本地預覽伺服器
echo ========================================================
echo.

powershell -NoProfile -Command ^
    "$procs = Get-Process -Name node -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like '*astro*' }; ^
     if ($procs) { ^
         $procs | ForEach-Object { Stop-Process -Id $_.Id -Force; Write-Host ('[STOPPED] 終止進程 PID: ' + $_.Id) -ForegroundColor Green }; ^
     } else { ^
         Write-Host '[INFO] 未偵測到運行中的 Astro 伺服器進程。' -ForegroundColor Yellow; ^
     }"

echo.
echo 完成。
pause
