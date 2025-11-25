@echo off
REM Interactive Data Display - Local Server Startup Script for Windows

echo ==========================================
echo 🚀 Interactive Data Display Server
echo ==========================================
echo.

REM Check if Flask is installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo ⚠️  Flask is not installed!
    echo.
    echo Installing Flask...
    pip install Flask
    echo.
)

REM Start the server
echo Starting server...
echo.
python app.py

pause
