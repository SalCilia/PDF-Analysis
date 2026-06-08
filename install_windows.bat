@echo off
REM Financial Holdings Report Generator - Windows Setup Script
REM This script downloads and installs the application

echo.
echo ================================================================================
echo  Financial Holdings Report Generator - Windows Installation
echo ================================================================================
echo.

REM Get the target directory
set TARGET_DIR=C:\Users\%USERNAME%\financial data extraction

echo Creating installation directory...
if not exist "%TARGET_DIR%" (
    mkdir "%TARGET_DIR%"
    echo. Directory created: %TARGET_DIR%
) else (
    echo. Directory already exists: %TARGET_DIR%
)

echo.
echo Changing to installation directory...
cd /d "%TARGET_DIR%"

echo.
echo Downloading application from GitHub...
echo.

REM Clone the repository
git clone https://github.com/SalCilia/pdf-analysis.git .

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✓ Repository cloned successfully!
) else (
    echo.
    echo ✗ Failed to clone repository
    echo. Make sure Git is installed: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo.
echo ================================================================================
echo  Installation Complete!
echo ================================================================================
echo.
echo Installation directory: %TARGET_DIR%
echo.
echo Next steps:
echo   1. Open Command Prompt (cmd.exe)
echo   2. Navigate to: %TARGET_DIR%
echo   3. Run: pip install -r requirements.txt
echo   4. Run: python test_environment.py
echo   5. Run: python demo_mode.py
echo   6. Place your POW Funds PDF in Downloads folder
echo   7. Run: python financial_report_generator_auto.py
echo.
echo Documentation:
echo   - README.md - Overview and features
echo   - SETUP_GUIDE.md - Detailed setup instructions
echo   - QUICK_REFERENCE.md - Quick start guide
echo   - BUILD_REPORT.md - Build verification
echo.
echo ================================================================================
echo.
pause
