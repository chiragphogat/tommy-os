@echo off
setlocal
color 0A
cd /d "%~dp0"

echo ========================================================
echo   T.O.M.M.Y. OS - ARCHITECT LAUNCHER
echo ========================================================
echo.

:: Check if venv exists
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo [ERROR] T.O.M.M.Y. core environment not found.
    echo Please run setup.bat first to install the system!
    echo.
    pause
    exit /b
)

echo [OS] Activating Virtual Environment...
call venv\Scripts\activate.bat

echo [OS] Igniting Master Kernel...
echo T.O.M.M.Y. is starting. You can close the system using the 
echo SHUTDOWN button on the HUD overlay once it appears.
echo.

python tommy_os.py

echo.
echo [OS] System safely unmounted.
echo Press any key to close this terminal.
pause >nul
exit /b
