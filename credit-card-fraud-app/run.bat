@echo off
echo ========================================
echo Credit Card Fraud Detection Web App
echo ========================================
echo.

REM Check if virtual environment exists
if exist venv (
    echo Activating virtual environment...
    call venv\Scripts\activate
) else (
    echo No virtual environment found.
    echo Running with system Python...
)

echo.
echo Starting Flask application...
echo.
echo The application will be available at:
echo http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py

pause
