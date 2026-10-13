@echo off
title Outreach Tool
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo Python is not installed or not in PATH.
  echo Install it from https://www.python.org/downloads/ and tick "Add Python to PATH".
  pause
  exit /b
)
if not exist ".installed" (
  echo Installing required packages - first time only...
  python -m pip install -r requirements.txt
  if errorlevel 1 ( echo Package install failed. & pause & exit /b )
  echo done> .installed
)
echo Starting Outreach Tool... keep this window open. Close it to stop the tool.
start "" http://127.0.0.1:5000
python app.py
pause
