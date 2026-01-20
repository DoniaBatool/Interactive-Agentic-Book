---
name: cybersecurity
description: Defensive cybersecurity skill for securing applications, infrastructure, and AI systems with practical controls, monitoring, and incident readiness
---

# Skill: Cybersecurity (Defensive, Practical, Production-Ready)

## Description
Expert-level defensive cybersecurity skill that hardens systems across app, infra, and AI surfaces. Focuses on **prevention**, **detection**, and **response** using measurable controls and production-friendly workflows.

## What This Skill Does
- Security posture reviews (app + cloud + supply chain)
- Threat modeling and control mapping
- Secure-by-default configuration (secrets, headers, authz)
- Monitoring/alerting recommendations + incident runbooks

## Hard Rules
- No secrets in logs, docs, or examples
- Least privilege everywhere (users, services, CI tokens)
- Prefer defense-in-depth over single “magic” control

## Core Domains (Coverage)
### Application Security
- OWASP Top 10: XSS, CSRF, SSRF, IDOR, injection, auth bypass
- Input validation, output encoding, file upload controls

### Infrastructure & Cloud
- Environment isolation (dev/staging/prod)
- Network controls (ingress allowlists where possible)
- Secure defaults for containers and runtime

### Supply Chain
- Dependency vulnerability scanning
- Lockfiles + pinned versions
- Secret scanning in CI

### AI / RAG / Agents
- Prompt injection mitigation (treat tool outputs as untrusted)
- Data exfiltration prevention (no secret/tool leakage)
- RAG ingestion trust boundaries (who can write to vector DB)

## Playbook
1. **Map assets + trust boundaries**
2. **Identify high-risk entry points**
3. **Apply baseline controls**
   - authz, validation, rate limits, logging redaction, headers
4. **Add detection**
   - structured logs, anomaly alerts, audit events
5. **Prepare response**
   - runbook + severity levels + rollback plan

## Output Artifacts
- Security checklist applied to the repo
- Threat model notes (assets, entry points, mitigations)
- CI security gates (deps/secret scan)
- Incident runbook (triage → contain → recover → postmortem)

## Integration
- Works with: `security-engineer`, `devops-engineer`, `structured-logging`, `production-checklist`, `user-isolation`
