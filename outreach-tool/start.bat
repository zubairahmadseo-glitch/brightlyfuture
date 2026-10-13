@echo off
title Outreach Tool
cd /d "%~dp0"
set PY=
py -3 --version >nul 2>nul && set PY=py -3
if not defined PY ( python --version >nul 2>nul && set PY=python )
if not defined PY (
  echo Python is not installed.
  echo 1. Download it from https://www.python.org/downloads/
  echo 2. During install, tick "Add python.exe to PATH".
  echo 3. Then double-click start.bat again.
  start "" https://www.python.org/downloads/
  pause
  exit /b
)
if not exist ".installed" (
  echo Installing required packages - first time only...
  %PY% -m pip install -r requirements.txt
  if errorlevel 1 ( echo Package install failed. & pause & exit /b )
  echo done> .installed
)
echo Starting Outreach Tool... keep this window open. Close it to stop the tool.
start "" http://127.0.0.1:5000
%PY% app.py
pause
