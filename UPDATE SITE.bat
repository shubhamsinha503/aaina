@echo off
title Rebuild aaina.space upload file
cd /d "%~dp0"
echo.
echo   Rebuilding the upload file from your site folder...
python "tools\make_zip.py"
if errorlevel 1 (
  echo.
  echo   Something went wrong. Is Python installed?
)
echo   Opening the folder for you...
explorer "%~dp0"
echo.
pause
