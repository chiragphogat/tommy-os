@echo off
setlocal
color 0A
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
goto INSTALL_REQUIREMENTS

:INSTALL_PYTHON
echo [WARNING] Python not found. Initiating automated Winget payload...
winget install -e --id Python.Python.3.11 --accept-package-agreements --accept-source-agreements
echo.
echo [SYSTEM ALERT] Python was just installed! 
echo Because the Windows path was updated, you MUST close this black window 
echo and re-open setup.bat to continue!
pause
exit /b


:INSTALL_REQUIREMENTS
:: --- 2. PYTHON DRIVER INSTALLATION ---
echo [2] Setting up Virtual Environment and Installing Core Drivers...
if not exist venv\Scripts\activate.bat (
    echo Creating virtual environment 'venv'...
    call python -m venv venv
)
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
call pip install -r requirements.txt
echo.

:: --- 3. DETERMINISTIC NLP MODEL ---
echo ========================================================
echo [3] Downloading Deterministic NLP Model (spaCy)
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
echo   To launch the OS, first activate the environment: venv\Scripts\activate
echo   Then simply run: python tommy_os.py
echo ========================================================
pause
