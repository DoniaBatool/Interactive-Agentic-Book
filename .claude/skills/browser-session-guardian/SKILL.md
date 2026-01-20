---
name: browser-session-guardian
description: Defensive local security agent for detecting common browser/session hijack risk factors (proxy/DNS/hosts/forced extensions) and guiding safe remediation
---

# Skill: Browser Session Guardian (Defensive, Local Audit + Remediation Guidance)

## Description
An expert-level **defensive** skill to help protect browsers and web sessions from hijacking by:
- auditing common compromise signals (proxy/DNS/hosts/policies/extensions/startup),
- producing a clear risk report,
- guiding safe remediation steps and account hardening.

This skill **does not** perform unauthorized access, exploit steps, or credential theft.

## Reality Check (Important)
Session hijacking usually succeeds because of one of these:
- malware/stealer on the device,
- malicious extensions,
- phishing/credential reuse,
- insecure networks + missing MFA,
- compromised email (account recovery channel).

An “agent” can’t magically make sessions unhackable, but it *can*:
- detect suspicious configuration drift,
- reduce attack surface,
- enforce good hygiene,
- alert you early.

## When to Use
- You suspect your browser sessions are getting hijacked
- Account got compromised (LinkedIn/Google/etc.)
- You want a weekly/monthly security audit checklist

## Inputs (you must provide)
- OS: Windows version
- Browser(s): Chrome / Edge (profile count if multiple)
- Confirmation: you own the device and have permission to run audits
- Optional: the affected account(s) (e.g., LinkedIn) so the remediation steps are tailored

## Outputs
- A local audit report (JSON + summary)
- A prioritized action plan (P0/P1/P2)
- Account-hardening checklist (MFA, sessions revoke, password rotation)

## Guardrails (Non‑Negotiable)
- No instructions for stealing sessions/cookies or bypassing security.
- No automation that requires storing passwords in plaintext.
- Prefer “report-only” by default; changes are explicit and reviewed.

## Playbook
1. **Stabilize accounts**
   - Sign out of all sessions, rotate passwords, enable MFA/security keys.
2. **Device audit (local)**
   - Proxy/DNS/hosts, forced policies, extensions, startup items.
3. **Remediate**
   - Remove suspicious extensions/policies, reset browser profiles if needed.
4. **Harden**
   - Separate browser profiles, reduce extensions, turn on OS security features.
5. **Monitor**
   - Run audits on a schedule; alert on drift.

## Recommended Tooling (Safe)
- Windows Security / Defender (including Offline Scan)
- Browser extension audit and policy review
- Password manager + unique passwords
- MFA with authenticator app or hardware key

## Integration
- Pairs with: `cybersecurity`, `security-engineer`, `password-security`
- Useful for: personal security workflows and enterprise hardening checklists

