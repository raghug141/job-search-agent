@echo off
echo ===================================================================
echo   Job Search Agent - Windows Setup & Test Script
echo ===================================================================
echo.

if not exist venv (
    echo [1/3] Creating virtual environment...
    python -m venv venv
) else (
    echo [1/3] Virtual environment exists.
)

echo.
echo [2/3] Installing dependencies...
call .\venv\Scripts\pip.exe install -r requirements.txt

echo.
echo [3/3] Running test suite...
call .\venv\Scripts\python.exe test_agent.py

echo.
echo Setup and testing finished!
pause
