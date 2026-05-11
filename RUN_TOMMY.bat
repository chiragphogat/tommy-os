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
echo T.O.M.M.Y. is starting. This system is locked for persistence.
echo To safely unmount the OS, press (Ctrl+C) in this terminal.
echo.

python tommy_os.py

echo.
echo [OS] System safely unmounted.
echo Press any key to close this terminal.
pause >nul
exit /b
