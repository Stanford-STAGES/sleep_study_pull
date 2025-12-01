@echo off
REM ==============================================
REM Script Name: copying_without_vids.bat
REM Author: Gauri Ganjoo
REM Date: November 19, 2025
REM Description: This script saves copies of sleep studies without their videos.
REM ==============================================

@echo off
setlocal enabledelayedexpansion

set "source= path\to\source\directory"
set "destination=path\to\destination\directory"

for /d %%D in ("%source%\*") do (
    set "dirname=%%~nxD"
    robocopy "%%D" "%destination%\!dirname!" /E /XD "video"
)

endlocal
