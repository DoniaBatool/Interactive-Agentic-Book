# Browser Session Guardian Runner (Defensive)
# - Runs browser_audit.ps1
# - Compares against previous report (local only)
# - Writes a small alert summary when drift is detected

$ErrorActionPreference = "Continue"

function Ensure-Dir($path) {
  if (-not (Test-Path -LiteralPath $path)) {
    New-Item -ItemType Directory -Path $path | Out-Null
  }
}

function Load-Json($path) {
  try {
    if (Test-Path -LiteralPath $path) {
      return (Get-Content -LiteralPath $path -Raw | ConvertFrom-Json)
    }
  } catch {}
  return $null
}

function Normalize-Extensions($exts) {
  $out = @()
  if ($null -eq $exts) { return $out }
  if ($exts -is [System.Array]) { $arr = $exts } else { $arr = @($exts) }
  foreach ($e in $arr) {
    $name = $null
    try {
      if ($e.manifests -and $e.manifests.Count -gt 0) { $name = $e.manifests[0].name }
    } catch {}
    $namePart = ""
    if ($name) { $namePart = $name }
    $out += ("{0}::{1}" -f $e.id, $namePart)
  }
  return ($out | Sort-Object -Unique)
}

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$reportsDir = Join-Path $here "reports"
Ensure-Dir $reportsDir

$latestPath = Join-Path $reportsDir "browser_audit_latest.json"
$prevPath   = Join-Path $reportsDir "browser_audit_prev.json"
$alertPath  = Join-Path $reportsDir "guardian_alert_latest.txt"

# Run audit quietly
& (Join-Path $here "browser_audit.ps1") -Quiet | Out-Null

$cur = Load-Json $latestPath
$prev = Load-Json $prevPath

if ($null -eq $cur) {
  "Guardian: failed to read latest audit report." | Set-Content -LiteralPath $alertPath -Encoding UTF8
  exit 0
}

$alerts = @()

if ($prev) {
  # DNS drift
  try {
    $curDns = ($cur.dns | ForEach-Object { ($_.interfaceAlias + "=" + ($_.serverAddresses -join ",")) }) | Sort-Object
    $prevDns = ($prev.dns | ForEach-Object { ($_.interfaceAlias + "=" + ($_.serverAddresses -join ",")) }) | Sort-Object
    if (($curDns -join "|") -ne ($prevDns -join "|")) {
      $alerts += "DNS settings changed since last run."
    }
  } catch {}

  # Hosts drift
  try {
    $curHosts = @($cur.hosts.suspiciousLines) -join "|"
    $prevHosts = @($prev.hosts.suspiciousLines) -join "|"
    if ($curHosts -ne $prevHosts) {
      $alerts += "Hosts mappings changed since last run."
    }
  } catch {}

  # Extension drift
  try {
    $curChrome = Normalize-Extensions $cur.browser.chrome.extensions
    $prevChrome = Normalize-Extensions $prev.browser.chrome.extensions
    if (($curChrome -join "|") -ne ($prevChrome -join "|")) {
      $alerts += "Chrome extensions changed since last run."
    }
  } catch {}

  try {
    $curEdge = Normalize-Extensions $cur.browser.edge.extensions
    $prevEdge = Normalize-Extensions $prev.browser.edge.extensions
    if (($curEdge -join "|") -ne ($prevEdge -join "|")) {
      $alerts += "Edge extensions changed since last run."
    }
  } catch {}

  # Startup drift (names+commands)
  try {
    $curStartup = ($cur.startup | ForEach-Object { ($_.name + "=" + $_.command) }) | Sort-Object
    $prevStartup = ($prev.startup | ForEach-Object { ($_.name + "=" + $_.command) }) | Sort-Object
    if (($curStartup -join "|") -ne ($prevStartup -join "|")) {
      $alerts += "Startup programs changed since last run."
    }
  } catch {}
}

# Always surface red flags from the audit
try {
  foreach ($rf in @($cur.redFlags)) {
    if ($rf) { $alerts += ("RED FLAG: " + $rf) }
  }
} catch {}

if ($alerts.Count -eq 0) {
  $alerts = @("No changes detected.")
}

$content = @()
$content += ("Guardian run (UTC): {0}" -f (Get-Date).ToUniversalTime().ToString("o"))
$content += ("Report: {0}" -f $latestPath)
$content += ""
$content += ($alerts | Sort-Object -Unique)

$content -join "`r`n" | Set-Content -LiteralPath $alertPath -Encoding UTF8

# Save current report as previous baseline (local only)
Copy-Item -LiteralPath $latestPath -Destination $prevPath -Force

