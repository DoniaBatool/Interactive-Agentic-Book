# Browser Session Guardian - Windows Audit Script (Defensive)
# Outputs a JSON report to tools/security/reports/browser_audit_latest.json

$ErrorActionPreference = "Continue"

function Ensure-Dir($path) {
  if (-not (Test-Path -LiteralPath $path)) {
    New-Item -ItemType Directory -Path $path | Out-Null
  }
}

function Read-RegistryValue($path, $name) {
  try {
    $item = Get-ItemProperty -Path $path -ErrorAction Stop
    return $item.$name
  } catch {
    return $null
  }
}

function Get-PolicyValues($rootPath) {
  $out = @()
  try {
    if (Test-Path $rootPath) {
      $props = Get-ItemProperty -Path $rootPath
      foreach ($p in $props.PSObject.Properties) {
        if ($p.Name -in @("PSPath","PSParentPath","PSChildName","PSDrive","PSProvider")) { continue }
        $out += [pscustomobject]@{ Name = $p.Name; Value = $p.Value }
      }
    }
  } catch {}
  return $out
}

function Get-ExtensionList($baseDir) {
  $exts = @()
  try {
    if (Test-Path -LiteralPath $baseDir) {
      Get-ChildItem -LiteralPath $baseDir -Directory | ForEach-Object {
        $id = $_.Name
        $versions = @()
        Get-ChildItem -LiteralPath $_.FullName -Directory -ErrorAction SilentlyContinue | ForEach-Object {
          $versions += $_.Name
        }
        $exts += [pscustomobject]@{
          id = $id
          versions = $versions
          path = $_.FullName
          lastWriteTimeUtc = $_.LastWriteTimeUtc
        }
      }
    }
  } catch {}
  return $exts
}

function Get-HostsInfo() {
  $hosts = "$env:WINDIR\System32\drivers\etc\hosts"
  $info = [pscustomobject]@{ path = $hosts; exists = $false; lastWriteTimeUtc = $null; suspiciousLines = @() }
  try {
    if (Test-Path -LiteralPath $hosts) {
      $info.exists = $true
      $fi = Get-Item -LiteralPath $hosts
      $info.lastWriteTimeUtc = $fi.LastWriteTimeUtc
      $lines = Get-Content -LiteralPath $hosts -ErrorAction SilentlyContinue
      $sus = @()
      foreach ($ln in $lines) {
        $t = $ln.Trim()
        if ($t -eq "" -or $t.StartsWith("#")) { continue }
        # Flag non-localhost mappings (review manually)
        if ($t -notmatch "127\.0\.0\.1|0\.0\.0\.0|::1") {
          $sus += $t
        }
      }
      $info.suspiciousLines = $sus
    }
  } catch {}
  return $info
}

function Get-ProxyInfo() {
  $internetSettings = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
  $proxyEnable = Read-RegistryValue $internetSettings "ProxyEnable"
  $proxyServer = Read-RegistryValue $internetSettings "ProxyServer"
  $autoConfigUrl = Read-RegistryValue $internetSettings "AutoConfigURL"

  $winhttp = ""
  try {
    $winhttp = (netsh winhttp show proxy) | Out-String
  } catch {}

  return [pscustomobject]@{
    userProxyEnabled = $proxyEnable
    userProxyServer = $proxyServer
    autoConfigUrl = $autoConfigUrl
    winhttp = $winhttp.Trim()
  }
}

function Get-DnsInfo() {
  $rows = @()
  try {
    $adapters = Get-DnsClientServerAddress -AddressFamily IPv4 -ErrorAction SilentlyContinue
    foreach ($a in $adapters) {
      $rows += [pscustomobject]@{
        interfaceAlias = $a.InterfaceAlias
        serverAddresses = $a.ServerAddresses
      }
    }
  } catch {}
  return $rows
}

function Get-StartupItems() {
  $items = @()
  try {
    Get-CimInstance Win32_StartupCommand -ErrorAction SilentlyContinue | ForEach-Object {
      $items += [pscustomobject]@{
        name = $_.Name
        command = $_.Command
        location = $_.Location
        user = $_.User
      }
    }
  } catch {}
  return $items
}

Ensure-Dir "tools/security/reports"

$chromeDefault = Join-Path $env:LOCALAPPDATA "Google\Chrome\User Data\Default\Extensions"
$edgeDefault   = Join-Path $env:LOCALAPPDATA "Microsoft\Edge\User Data\Default\Extensions"

$chromePolicyHKLM = "HKLM:\SOFTWARE\Policies\Google\Chrome"
$chromePolicyHKCU = "HKCU:\SOFTWARE\Policies\Google\Chrome"
$edgePolicyHKLM   = "HKLM:\SOFTWARE\Policies\Microsoft\Edge"
$edgePolicyHKCU   = "HKCU:\SOFTWARE\Policies\Microsoft\Edge"

$report = [pscustomobject]@{
  generatedAtUtc = (Get-Date).ToUniversalTime().ToString("o")
  machine = $env:COMPUTERNAME
  user = $env:USERNAME
  proxy = (Get-ProxyInfo)
  dns = (Get-DnsInfo)
  hosts = (Get-HostsInfo)
  browser = [pscustomobject]@{
    chrome = [pscustomobject]@{
      extensionsPath = $chromeDefault
      extensions = (Get-ExtensionList $chromeDefault)
      policyHKLM = (Get-PolicyValues $chromePolicyHKLM)
      policyHKCU = (Get-PolicyValues $chromePolicyHKCU)
    }
    edge = [pscustomobject]@{
      extensionsPath = $edgeDefault
      extensions = (Get-ExtensionList $edgeDefault)
      policyHKLM = (Get-PolicyValues $edgePolicyHKLM)
      policyHKCU = (Get-PolicyValues $edgePolicyHKCU)
    }
  }
  startup = (Get-StartupItems)
  redFlags = @()
}

# Simple red-flag heuristics
if ($report.proxy.userProxyEnabled -eq 1 -and $report.proxy.userProxyServer) {
  $report.redFlags += "User proxy is enabled. Verify ProxyServer is expected."
}
if ($report.proxy.autoConfigUrl) {
  $report.redFlags += "AutoConfigURL is set (PAC). Verify it is expected."
}
# WinHTTP parsing: "Direct access (no proxy server)." is OK; otherwise review.
if ($report.proxy.winhttp) {
  # Normalize whitespace/newlines since netsh output varies across hosts/locales.
  $winhttpNorm = ($report.proxy.winhttp -replace "\\s+", " ").Trim()
  if ($winhttpNorm -notlike "*Direct access (no proxy server).*") {
    $report.redFlags += "WinHTTP proxy settings are not 'Direct access'. Review netsh winhttp show proxy output."
  }
}
if ($report.hosts.suspiciousLines.Count -gt 0) {
  $report.redFlags += "Hosts file has non-localhost mappings. Review suspiciousLines."
}
if (($report.browser.chrome.policyHKLM.Count + $report.browser.chrome.policyHKCU.Count) -gt 0) {
  $report.redFlags += "Chrome policies are present. Review for forced extensions or proxy settings."
}
if (($report.browser.edge.policyHKLM.Count + $report.browser.edge.policyHKCU.Count) -gt 0) {
  $report.redFlags += "Edge policies are present. Review for forced extensions or proxy settings."
}

$outPath = "tools/security/reports/browser_audit_latest.json"
$json = $report | ConvertTo-Json -Depth 8
Set-Content -LiteralPath $outPath -Value $json -Encoding UTF8

Write-Host ""
Write-Host "Browser Session Guardian - Audit Complete"
Write-Host ("Report: {0}" -f $outPath)
Write-Host ""

if ($report.redFlags.Count -gt 0) {
  Write-Host "RED FLAGS:"
  $report.redFlags | ForEach-Object { Write-Host ("- " + $_) }
  Write-Host ""
} else {
  Write-Host "No red flags detected by basic heuristics."
  Write-Host ""
}

Write-Host "Next steps (recommended):"
Write-Host "- Run Microsoft Defender Offline Scan (Windows Security)"
Write-Host "- Remove unknown browser extensions; reset browser profile if needed"
Write-Host "- Rotate passwords + enable MFA/security key (especially email + LinkedIn)"

