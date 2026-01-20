# Uninstalls the Browser Session Guardian scheduled task (Windows)

$ErrorActionPreference = "Stop"
$taskName = "BrowserSessionGuardian"

try {
  Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction Stop | Out-Null
  Write-Host "Removed scheduled task: $taskName"
} catch {
  Write-Host "Task not found or could not be removed: $taskName"
}

