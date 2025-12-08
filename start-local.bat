@echo off
REM Quick Start Script for Local Testing
REM This script starts both backend and frontend servers

echo ========================================
echo   AI Robotics Textbook - Local Testing
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.11+ and try again
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js is not installed or not in PATH
    echo Please install Node.js 18+ and try again
    pause
    exit /b 1
)

echo [1/4] Checking dependencies...
echo.

REM Check backend dependencies
if not exist "backend\requirements.txt" (
    echo [WARNING] backend\requirements.txt not found
) else (
    echo [INFO] Backend requirements.txt found
)

REM Check frontend dependencies
if not exist "frontend\node_modules" (
    echo [WARNING] Frontend node_modules not found
    echo [INFO] Run 'npm install' in frontend directory first
) else (
    echo [INFO] Frontend dependencies found
)

echo.
echo [2/4] Starting Backend Server...
echo [INFO] Backend will run on: http://localhost:8000
echo [INFO] API Docs will be at: http://localhost:8000/docs
echo.

REM Start backend in new window
start "Backend Server" cmd /k "cd backend && python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

REM Wait a bit for backend to start
timeout /t 3 /nobreak >nul

echo [3/4] Starting Frontend Server...
echo [INFO] Frontend will run on: http://localhost:3000
echo.

REM Start frontend in new window
start "Frontend Server" cmd /k "cd frontend && npm start"

echo.
echo [4/4] Setup Complete!
echo.
echo ========================================
echo   Services Starting...
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo Frontend: http://localhost:3000
echo.
echo Two new windows have opened:
echo   - Backend Server (Terminal 1)
echo   - Frontend Server (Terminal 2)
echo.
echo Wait for both servers to start, then:
echo   1. Open http://localhost:3000 in your browser
echo   2. Navigate to Chapter 1 to test features
echo   3. Check http://localhost:8000/docs for API testing
echo.
echo Press any key to close this window...
pause >nul

