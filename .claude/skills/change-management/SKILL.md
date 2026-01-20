---
name: change-management
description: Manage changes to existing features by creating change subfolders with spec, plan, tasks and automatically updating all affected areas of the project (project)
---

# Skill: Change Management (Specs → Plans → Safe Implementation)

## Description
Expert-level skill to manage changes to existing features without breaking the system. It enforces a **spec → plan → tasks → implementation → verification** loop and ensures all affected areas (code, docs, tests, deploy) are updated coherently.

## Why This Matters
- Prevents “quick fixes” from turning into production regressions
- Creates a durable audit trail (what changed and why)
- Keeps multi-service systems consistent (frontend/backend/auth/db)

## When to Use
- Extending an existing feature (auth, chat, translation, theming)
- Refactors that touch multiple modules
- Bug fixes that require behavior changes
- Any change that could affect user experience or data integrity

## Inputs
- Current behavior + desired behavior (before/after)
- Constraints (deadlines, infra limits, backwards compatibility)
- Impacted modules/services

## Outputs
- `spec.md`: user story + acceptance criteria + constraints
- `plan.md`: technical design + rollout plan + risks
- `tasks.md`: implementation checklist (small, verifiable tasks)
- PR with changes + migration notes (if needed)

## Playbook (Modern Agentic Workflow)
1. **Clarify**: reproduce issue / confirm expected outcome
2. **Spec**: write success criteria + non-goals
3. **Plan**: design the smallest safe change set
4. **Execute**: implement in small commits; keep surfaces stable
5. **Verify**: targeted tests + manual smoke checks
6. **Deploy**: staged rollout when possible; monitor; document

## Safety / Quality Gates (P0)
- [ ] Backwards compatible changes (or staged migration plan)
- [ ] Error handling is user-friendly and actionable
- [ ] Observability updated (logs/metrics/health checks)
- [ ] Rollback plan exists (and is realistic)

## Integration
- Strongly pairs with: `production-checklist`, `deployment-automation`, `edge-case-tester`, `structured-logging`