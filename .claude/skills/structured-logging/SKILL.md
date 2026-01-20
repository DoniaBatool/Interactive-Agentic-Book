---
name: structured-logging
description: Setup comprehensive structured logging infrastructure with user context, request IDs, and error tracking (Phase 3)
---

# Skill: Structured Logging (Debuggable Production Systems)

## Description
Expert-level logging skill to make production issues diagnosable quickly: JSON logs, correlation IDs, redaction, event taxonomy, and actionable error context.

## Logging Rules
- Logs must be **machine-parseable** (JSON preferred)
- Include **request_id / session_id** consistently
- Never log secrets/PII; redact tokens and cookies

## Event Taxonomy (recommended)
- `*.start` (request begins)
- `*.done` (success with duration)
- `*.error` (exception with safe message)

## Playbook
1. Add a request ID middleware
2. Log structured events (not free-form strings)
3. Add duration + key dimensions (chapter, mode, status_code)
4. Add error capture with stack traces (server-side only)
5. Add sampling for high-volume logs

## Output Artifacts
- Logging helpers (event logger)
- Redaction utilities
- “How to debug” runbook

## Integration
- Works with: `observability-apm`, `devops-engineer`, `chatbot-endpoint`