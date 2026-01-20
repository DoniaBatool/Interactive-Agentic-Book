---
name: api-docs-generator
description: Generate comprehensive OpenAPI documentation and docstrings for all backend endpoints, services, and MCP tools (Phase 3)
---

# Skill: API Docs Generator (OpenAPI + SDK-Ready Docs)

## Description
Expert-level documentation skill that produces **accurate, complete, versioned** API docs for backend services and MCP tools. Outputs include OpenAPI specs, endpoint docs, examples, error models, auth flows, pagination conventions, and client snippets.

## Purpose
- Keep APIs discoverable and safe to change
- Make SDK/client generation reliable
- Reduce integration time + production incidents

## When to Use
- New endpoints added/changed
- Any breaking change or payload shape change
- Before public release / partner integration
- When errors are unclear or inconsistent

## Inputs (you must gather)
- **Runtime contract**: actual request/response bodies (curl/Postman examples)
- **Source of truth**: route handlers + schema models + validators
- **Auth model**: cookies/JWT/API key; required scopes/roles
- **Environments**: base URLs, CORS, rate limits, timeouts

## Outputs (artifacts)
- `openapi.json` / `openapi.yaml` (or generated at `/openapi.json`)
- Endpoint reference pages (README / docs site)
- Examples: success + common errors
- Changelog entry: what changed + migration notes

## Operating Principles
- **Docs must match code**, not intention
- Prefer **explicit** schemas over “any/object”
- Every endpoint must define:
  - status codes
  - error format
  - auth requirements
  - idempotency / retries guidance

## Playbook
1. **Inventory endpoints**
   - List routes, methods, tags, auth guards, dependencies
2. **Normalize conventions**
   - Error envelope: `{ error: { code, message, details? } }`
   - Pagination: `{ items, next_cursor? }`
3. **Document auth**
   - How to obtain session/JWT
   - How to pass credentials (cookie/header)
4. **Add examples**
   - curl for each endpoint
   - realistic request bodies
5. **Validate spec**
   - Ensure no missing schemas
   - Ensure referenced schemas exist
6. **Diff & version**
   - Highlight breaking changes
   - Provide migration notes

## Quality Checklist (must pass)
- [ ] Every endpoint has request/response schemas
- [ ] Every endpoint has at least 1 success example
- [ ] Every endpoint lists error codes + meanings
- [ ] Auth requirements documented (including “public” endpoints)
- [ ] Naming consistent across services (snake/camel)

## Safety & Security Notes
- Never document real secrets, tokens, or internal URLs
- For admin endpoints, clearly mark **RBAC requirements**
- Include rate limiting + abuse prevention guidance when applicable

## Integration With Other Skills
- Pairs with: `api-contract-design`, `pydantic-validation`, `structured-logging`, `production-checklist`
- Enables: client generation + contract tests + monitoring dashboards

