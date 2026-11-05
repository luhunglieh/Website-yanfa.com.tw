@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ^
    "$ts = Get-Date -Format 'yyyyMMdd_HHmmss'; ^
     $backupDir = '..\Website-yanfa-Backups'; ^
     if (!(Test-Path $backupDir)) { New-Item -ItemType Directory -Path $backupDir | Out-Null }; ^
     Write-Host '[1/2] 正在建立 Git 鏡像備份 (.bundle)...' -ForegroundColor Cyan; ^
     git bundle create \"$backupDir\Website-yanfa_$ts.bundle\" --all; ^
     Write-Host \"      -> 已建立: $backupDir\Website-yanfa_$ts.bundle\" -ForegroundColor Green; ^
     Write-Host '[2/2] 正在建立純源碼壓縮包 (.zip)...' -ForegroundColor Cyan; ^
     $exclude = @('dist', '.astro', 'node_modules', '.git', 'logs', 'brain', 'scratch'); ^
     $files = Get-ChildItem -Path '.' -Exclude $exclude | Select-Object -ExpandProperty FullName; ^
     Compress-Archive -Path $files -DestinationPath \"$backupDir\Website-yanfa_src_$ts.zip\" -Force; ^
     Write-Host \"      -> 已建立: $backupDir\Website-yanfa_src_$ts.zip\" -ForegroundColor Green; ^
     Write-Host '========================================================' -ForegroundColor Yellow; ^
     Write-Host '  備份完成！儲存目錄: ..\Website-yanfa-Backups' -ForegroundColor Yellow; ^
     Write-Host '========================================================' -ForegroundColor Yellow;"
pause
