@echo off
setlocal

REM One-click setup for Windows.
REM - Installs Python deps from requirements.txt

cd /d "%~dp0"

echo === Teaching The Machine: Windows Setup ===
echo.

set "PY=python"
where python >nul 2>nul
if errorlevel 1 (
  where py >nul 2>nul
  if errorlevel 1 (
    echo ERROR: Python was not found in PATH.
    echo Install Python 3.10+ from https://www.python.org/downloads/ and re-run this file.
    echo Make sure to tick "Add python.exe to PATH" in the installer.
    echo.
    pause
    exit /b 1
  )
  set "PY=py -3"
)

echo.
echo Upgrading pip ...
%PY% -m pip install --upgrade pip
if errorlevel 1 (
  echo ERROR: Failed to upgrade pip.
  pause
  exit /b 1
)

echo.
echo Installing dependencies (this can take a while, especially Torch) ...
%PY% -m pip install --user -r requirements.txt
if errorlevel 1 (
  echo.
  echo ERROR: Dependency install failed.
  echo If Torch download fails, retry on a stable connection.
  pause
  exit /b 1
)

echo.
echo DONE.
echo To run scripts:
echo   python yolo_live.py
echo   python yolo_single_image.py
echo   python yolo_train.py
echo   python capture.py
echo.
pause
