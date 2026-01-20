@echo off
REM Installs a scheduled task to run Browser Session Guardian every 15 minutes.
REM Use this if AV blocks the PowerShell installer.
REM Note: A fully powered-off PC cannot run tasks. This can run while ON and can wake from sleep/hibernate.

set TASKNAME=BrowserSessionGuardian
set RUNNER=%~dp0guardian_runner.ps1

if not exist "%RUNNER%" (
  echo guardian_runner.ps1 not found at: %RUNNER%
  exit /b 1
)

REM Create or update task: run every 15 minutes.
REM /RU = current user. This will prompt for credentials in some environments.
schtasks /Create /F /TN "%TASKNAME%" /TR "powershell.exe -NoProfile -ExecutionPolicy Bypass -File \"%RUNNER%\"" /SC MINUTE /MO 15 /RU "%USERNAME%"

if errorlevel 1 (
  echo Failed to create scheduled task. Try running Command Prompt as Administrator, or use Task Scheduler GUI.
  exit /b 1
)

echo Installed scheduled task: %TASKNAME%
echo It will run every 15 minutes while the machine is ON (and can wake from sleep if enabled in task settings).
echo Latest alert file: tools\security\reports\guardian_alert_latest.txt
exit /b 0

