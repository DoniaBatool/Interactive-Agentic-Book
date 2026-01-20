---
name: mcp-tool-builder
description: Build MCP (Model Context Protocol) tools with proper contracts, validation, and integration with AI agents (project)
---

# Skill: MCP Tool Builder (Safe, Typed, Observable Tools)

## Description
Expert-level skill to design and implement MCP tools that are **safe**, **typed**, and **easy to debug**. Focuses on schemas, guardrails, timeouts, idempotency, and clear outputs.

## When to Use
- Adding a new MCP tool
- Tools are flaky, slow, or hard to understand
- Need safer tool execution (prevent destructive ops)

## Tool Design Rules
- Validate inputs strictly (types + constraints)
- Prefer **read-only** tools by default
- Every tool must have:
  - clear purpose
  - failure modes
  - safe defaults
  - deterministic output shape

## Playbook
1. Define schema (inputs/outputs) and examples
2. Add safety rails (allowlist paths/domains, dry-run)
3. Add timeouts + retries (only when safe)
4. Add logging with correlation IDs
5. Write tests or reproducible examples

## Output Artifacts
- Tool spec + examples
- Implementation with validation + error mapping
- Docs for usage patterns

## Integration
- Works with: `api-docs-generator`, `structured-logging`, `change-management`