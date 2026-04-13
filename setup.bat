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
echo [2] Installing Core Physics and Hardware Drivers...
call pip install -r requirements.txt
echo.

:: --- 3. NEURAL LLM PROMPT ---
echo ========================================================
echo [OPTIONAL NEURAL CORE] 
echo T.O.M.M.Y natively bypasses your mouse and controls your OS
echo using lightweight, purely local Python geometry math.
echo.
echo However, if you want Tommy to have a high "IQ" 
echo (Read your screen, summarize articles, act as an AI agent), 
echo he requires an absolute heavy-weight local Neural Engine (Ollama).
echo.
echo NOTE: Installing the Neural Engine requires roughly 6-8GB+ 
echo of disk space. Tommy works perfectly fine without it!
echo ========================================================
set /P INSTALL_LLM="Do you want to install the heavy Neural Engine? (Y/N): "

if /I "%INSTALL_LLM%"=="N" goto SKIP_LLM
if /I "%INSTALL_LLM%"=="n" goto SKIP_LLM

echo.
echo [3] Bootstrapping Neural System Architecture...
ollama -v >nul 2>&1
IF %ERRORLEVEL% NEQ 0 goto INSTALL_OLLAMA

:PULL_MODELS
echo [INFO] Injecting Local AI Weights... Do NOT close this window.
echo Pulling Primary Logic Core (llama3)...
call ollama pull deepseek-r1:8b
echo Pulling Screen Vision Core (moondream)...
call ollama pull qwen3-vl:4b
goto FINISH


:INSTALL_OLLAMA
echo [INFO] Ollama is missing. Downloading via Winget...
winget install -e --id Ollama.Ollama --accept-package-agreements --accept-source-agreements
echo.
echo [SYSTEM ALERT] Ollama was just installed! 
echo To ensure the models load correctly, please restart this script or
echo manually run: ollama pull llama3:8b-instruct-q4_K_M
goto FINISH


:SKIP_LLM
echo.
echo [3] Skipping Neural Engine. Tommy will operate in Pure OS-Control Mode!


:FINISH
echo.
echo ========================================================
echo   INSTALLATION COMPLETE.
echo   Remember to add your free Picovoice token to the .env file!
echo   To launch the OS, simply run: python tommy_os.py
echo ========================================================
pause
