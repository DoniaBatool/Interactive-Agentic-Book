# Browser Session Guardian (Windows) — Local Audit

This folder contains **defensive** scripts that help you audit common causes of browser/session hijacking on Windows.

## What it checks
- System proxy settings (WinHTTP + user proxy)
- DNS server configuration
- Hosts file changes
- Chrome/Edge forced policies (including forced extension install lists)
- Installed browser extensions (IDs + versions)
- Startup programs (common persistence vector)

## What it does NOT do
- It does **not** remove malware.
- It does **not** bypass security or “hack back”.
- It does **not** steal or read your cookies/session tokens.

## How to run
Open PowerShell (no admin required for most checks) and run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\security\browser_audit.ps1
```

If you have PowerShell 7 installed, this also works:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\tools\security\browser_audit.ps1
```

Outputs:
- `tools/security/reports/browser_audit_latest.json`
- A console summary with red flags.

## Optional: run continuously (while PC is ON)
Install a scheduled task that runs every 15 minutes:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\security\install_guardian_task.ps1
```

If your AV quarantines/blocks that file, use:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\security\install_guardian_task_safe.ps1
```

Or (alternative) use the CMD installer:

```bat
.\tools\security\install_guardian_task.cmd
```

It writes a drift/alert summary here:
- `tools/security/reports/guardian_alert_latest.txt`

**Note**: no script can run when the PC is fully powered off. This can run while ON, and can wake from sleep/hibernate if enabled.

## If your antivirus flags the scripts (RAV/others)
Some endpoint products flag *any* PowerShell that reads `hosts` / registry as “suspicious” (heuristics). These scripts are **defensive** and only **read** configuration + write local JSON reports, but AV may still block/quarantine them.

Recommended safest path:
- Prefer **Microsoft Defender Offline Scan** for cleanup.
- If you don’t explicitly need RAV Endpoint Protection, consider uninstalling it and using Microsoft Defender.

If you choose to keep RAV:
- Only allow/run these scripts **after you personally review them** (they should not modify `hosts`).
- You may need to add a **trusted exclusion** for your guardian folder so RAV doesn’t quarantine `install_guardian_task.ps1` or block scheduled runs.

## Next steps if you see red flags
- Remove unknown browser extensions
- Reset browser settings / create a fresh profile
- Check policies in registry (forced extensions are a big warning sign)
- Run **Microsoft Defender Offline Scan**
- Rotate passwords + enable MFA/security key

