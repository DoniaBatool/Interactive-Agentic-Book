# Installs a scheduled task to run Browser Session Guardian periodically (Windows)
# Note: A PC that is fully powered off cannot run tasks. This can run while the PC is ON,
# and can be configured to wake from sleep/hibernate.

$ErrorActionPreference = "Stop"

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$runner = Join-Path $here "guardian_runner.ps1"

if (-not (Test-Path -LiteralPath $runner)) {
  throw "guardian_runner.ps1 not found at: $runner"
}

$taskName = "BrowserSessionGuardian"

$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument ("-NoProfile -ExecutionPolicy Bypass -File `"{0}`"" -f $runner)

# Run every 15 minutes, starting 1 minute from now.
$start = (Get-Date).AddMinutes(1)
$trigger = New-ScheduledTaskTrigger -Once -At $start
$trigger.RepetitionInterval = (New-TimeSpan -Minutes 15)
$trigger.RepetitionDuration = ([TimeSpan]::MaxValue)

$settings = New-ScheduledTaskSettingsSet `
  -StartWhenAvailable `
  -AllowStartIfOnBatteries `
  -DontStopIfGoingOnBatteries `
  -MultipleInstances IgnoreNew `
  -ExecutionTimeLimit (New-TimeSpan -Minutes 10) `
  -WakeToRun

# Run as current user without prompting for password (S4U).
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType S4U -RunLevel Limited

$task = New-ScheduledTask -Action $action -Trigger $trigger -Settings $settings -Principal $principal

Register-ScheduledTask -TaskName $taskName -InputObject $task -Force | Out-Null

Write-Host "Installed scheduled task: $taskName"
Write-Host "It will run every 15 minutes while the machine is ON (and can wake from sleep)."
Write-Host "Latest alert file: tools/security/reports/guardian_alert_latest.txt"

