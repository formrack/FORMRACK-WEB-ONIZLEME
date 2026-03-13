@echo off
REM Formrack 3D Model Viewer - Quick Start
REM Windows PowerShell Script

title Formrack Server
color 0A

cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                                                            ║
echo ║          🚀 FORMRACK 3D MODEL VIEWER                      ║
echo ║          Professional 3D Product Preview System            ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ❌ ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/
    echo ⚠️  Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo ✅ Python found!
echo.
echo Starting Formrack 3D Model Server...
echo.
timeout /t 2 /nobreak

REM Start Python server
python server.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ Server failed to start!
    echo.
    pause
    exit /b 1
)
