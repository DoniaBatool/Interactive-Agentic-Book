---
name: ethical-hacker
description: Authorized security testing skill (pentesting) focused on legal scope, safe methodologies, evidence capture, and clear remediation reporting
---

# Skill: Ethical Hacker (Authorized Testing + High-Quality Reporting)

## Description
Expert-level **authorized** security testing skill for assessing systems under an explicit scope and written permission. Emphasizes safe methodology, evidence capture, and actionable remediation—**not** unauthorized access.

## Legal / Safety Guardrails (Non-Negotiable)
- Perform testing **only with explicit permission** and documented scope
- Respect rules of engagement (RoE), time windows, rate limits
- Do not access data you are not authorized to access
- Prefer non-destructive verification methods

## When to Use
- Pre-release security assessment of your own system
- Compliance-driven assessments (internal)
- Validating remediations after fixes

## Inputs Required
- Written authorization + scope (domains, IPs, endpoints)
- Environment details (staging vs prod) + test accounts
- Rules of engagement (allowed techniques, reporting format)

## Outputs
- Findings report with:
  - severity (CVSS-style), impact, reproduction (safe), evidence
  - recommended fix + verification steps
- Executive summary (risk posture, top issues)
- Retest results after remediation

## Methodology (High-Level)
1. **Scoping**
   - confirm targets, exclusions, and success criteria
2. **Recon (safe)**
   - inventory surfaces and auth boundaries
3. **Vulnerability discovery**
   - focus on OWASP Top 10 + misconfigurations
4. **Verification**
   - confirm with least invasive method; capture evidence
5. **Reporting**
   - prioritize fixes; include “how to verify fixed”
6. **Retest**
   - validate remediations and close findings

## Common Finding Categories (Defensive Focus)
- AuthZ issues (IDOR / horizontal escalation)
- CSRF / session misconfig
- Injection risks (SQL/command)
- SSRF and unsafe URL fetching
- Sensitive data exposure in logs
- Missing rate limits / brute-force protections

## Integration
- Works with: `cybersecurity`, `security-engineer`, `user-isolation`, `password-security`, `structured-logging`

## Notes
This skill is designed to be safe and compliant for a digital agent factory. It avoids exploit instructions and focuses on **authorized assessment + remediation quality**.
