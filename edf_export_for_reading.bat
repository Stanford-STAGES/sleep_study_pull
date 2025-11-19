@echo off
REM ==============================================
REM Script Name: edf_export_for_reading.bat
REM Author: Gauri Ganjoo
REM Date: November 19, 2025
REM Description: This script automatically opens Domino, signs into you SHC account, and exports the event data for the studies in the directory you list to the last location Domino remembers exporting event files to with the same options chosen.
REM ==============================================

@echo off
setlocal

rem Path to the folder containing measurement files
set measur_path=\path to sleep studies without vids
rem Path to DOMINO executable
set Domino_exe=C:\SOMNOmedics\SomnoScreen\bin64\SomnoScreen.exe
rem Updated Path to nircmd
set nircmd_path=C:\Users\WKS29464-U\Downloads\nircmd\nircmd.exe
rem Log file path
set log_file=processed_subdirectories.log

rem Ensure nircmd_path exists
if not exist "%nircmd_path%" (
    echo NirCmd path not found! Please check the path to nircmd.exe.
    exit /b 1
)

rem Create or clear the log file
echo Processing Log > "%log_file%"

rem Loop through each file with .dt2, .dtx, or .dat extension
for /r "%measur_path%" %%f in (*.dt2 *.dtx *.dat *.dt3) do (
    echo Processing %%f
    rem Open the measurement file with DOMINO
    start "" "%Domino_exe%" -open:"%%f"
    rem Log the processed file
    echo %%f >> "%log_file%"
    
    rem Wait for 5 seconds (adjust as needed to ensure measurement loads)
    timeout /t 5 /nobreak

    rem Type username
    "%nircmd_path%" sendkey shift down
    "%nircmd_path%" sendkey S press
    "%nircmd_path%" sendkey shift up
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press

    rem Press Tab to move to password field
    "%nircmd_path%" sendkey tab press
    rem Type password
    "%nircmd_path%" sendkey shift down
    "%nircmd_path%" sendkey S press
    "%nircmd_path%" sendkey shift up
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press
    "%nircmd_path%" sendkey x press

    rem Press Enter to log in
    "%nircmd_path%" sendkey enter press

    rem Wait for 45 seconds (adjust as needed to ensure measurement loads)
    timeout /t 45 /nobreak

    rem Simulate Enter key press
    "%nircmd_path%" sendkey enter press

    rem Wait for 30 seconds (adjust as needed to ensure measurement loads)
    timeout /t 30 /nobreak

    rem Focus on the window (if the window title contains part of the measurement name, use wildcard *)
    "%nircmd_path%" win activate title "*SomnoScreen*"
    rem Wait for the window to be in focus
    timeout /t 1 /nobreak

    rem Simulate ALT key press to start the export of Analysis Data
    "%nircmd_path%" sendkey alt down
    "%nircmd_path%" sendkey alt up
    rem Simulate Enter key press
    "%nircmd_path%" sendkey enter press

    rem Wait for 7 seconds (adjust as needed to ensure measurement loads)
    timeout /t 7 /nobreak

    rem Simulate 7x Arrow Down key press
    for /l %%i in (1,1,4) do "%nircmd_path%" sendkey down press

    rem Wait for 10 seconds (adjust as needed to ensure measurement loads)
    timeout /t 10 /nobreak

    rem Simulate 1x Arrow Right key press
    "%nircmd_path%" sendkey right press
    rem Simulate 1x Arrow Down key press
    "%nircmd_path%" sendkey down press
    rem Simulate Enter key press
    "%nircmd_path%" sendkey enter press
    rem Wait for the confirmation window to appear
    timeout /t 2 /nobreak
    rem Confirm the new window with Enter key press
    "%nircmd_path%" sendkey enter press
    rem Wait for the window to be in focus
    timeout /t 110 /nobreak

    rem Simulate Enter key press
    "%nircmd_path%" sendkey enter press
    rem Simulate ALT key press to close the software
    "%nircmd_path%" sendkey alt down
    "%nircmd_path%" sendkey alt up
    rem Simulate Enter key press
    "%nircmd_path%" sendkey enter press
    rem Simulate 1x Arrow up key press
    "%nircmd_path%" sendkey up press
    rem Simulate Enter key press
    "%nircmd_path%" sendkey enter press
    rem Pause before the second Enter (for the next window)
    timeout /t 2 /nobreak
    rem Simulate TAB key press
    for /l %%i in (1,1,3) do "%nircmd_path%" sendkey tab press
    rem Simulate Enter key press
    "%nircmd_path%" sendkey enter press

    rem Wait before processing the next file
    timeout /t 10 /nobreak

    rem Simulate ALT key press to start closing Domino Window
    "%nircmd_path%" sendkey alt down
    "%nircmd_path%" sendkey alt up
    rem Simulate Enter key press
    "%nircmd_path%" sendkey enter press

    rem Wait for 7 seconds (adjust as needed to ensure measurement loads)
    timeout /t 7 /nobreak

    rem Simulate 7x Arrow Down key press
    for /l %%i in (1,1,8) do "%nircmd_path%" sendkey down press

    rem Simulate Enter key press
    "%nircmd_path%" sendkey enter press

    rem Wait for 4 seconds (adjust as needed to ensure measurement loads)
    timeout /t 4 /nobreak

    rem Simulate Enter key press
    "%nircmd_path%" sendkey enter press

    rem Wait for 4 seconds (adjust as needed to ensure measurement loads)
    timeout /t 4 /nobreak
)

endlocal