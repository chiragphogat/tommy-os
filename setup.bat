@echo off
setlocal
color 0A

:: Navigate precisely to the folder where setup.bat is located
cd /d "%~dp0"

echo ========================================================
echo   T.O.M.M.Y OS - AUTOMATED DEPLOYMENT PROTOCOL
echo ========================================================
echo.

:: --- 1. PYTHON CHECK & INSTALL ---
echo [1] Checking architecture for Python 3.10+...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 goto INSTALL_PYTHON
echo Python visually verified.
echo.
goto SETUP_VENV

:INSTALL_PYTHON
echo [WARNING] Python not found. Initiating automated Winget payload...
winget install -e --id Python.Python.3.11 --accept-package-agreements --accept-source-agreements
echo.
echo [SYSTEM ALERT] Python was just installed! 
echo Because the Windows path was updated, you MUST close this black window 
echo and re-open setup.bat to continue!
pause
exit /b

:SETUP_VENV
:: --- 2. VIRTUAL ENVIRONMENT ARCHITECTURE ---
echo [2] Initializing Virtual Environment...
IF NOT EXIST "venv\" (
    echo Creating new venv container...
    python -m venv venv
)
echo Activating Virtual Environment...
call venv\Scripts\activate.bat
echo.

:: --- 3. PYTHON DRIVER INSTALLATION ---
echo [3] Installing Core Physics and Hardware Drivers into venv...
call pip install -r requirements.txt
echo.

:: --- 4. DETERMINISTIC NLP MODEL ---
echo ========================================================
echo [4] Downloading Deterministic NLP Model (spaCy)
echo T.O.M.M.Y natively bypasses your mouse and controls your OS
echo using lightweight, purely local Python geometry math.
echo Downloading English core model for syntax routing...
echo ========================================================
call python -m spacy download en_core_web_sm
echo.

:FINISH
echo.
echo ========================================================
echo   INSTALLATION COMPLETE.
echo   Remember to add your free Picovoice token to the .env file!
echo   Launching PowerShell Terminal in T.O.M.M.Y. Environment...
echo ========================================================

:: Spawn a native PowerShell instance, bypass execution policies to allow activate.ps1, and stay open
start powershell -NoExit -ExecutionPolicy Bypass -Command "& { cd '%~dp0'; .\venv\Scripts\Activate.ps1; Clear-Host; Write-Host -ForegroundColor Green '========================================================'; Write-Host -ForegroundColor Green ' T.O.M.M.Y. VIRTUAL ENVIRONMENT ACTIVATED.'; Write-Host -ForegroundColor Green ' Press ENTER to launch the OS!'; Write-Host -ForegroundColor Green '========================================================'; [Microsoft.PowerShell.PSConsoleReadLine]::Insert('python tommy_os.py') }"

exit /b
