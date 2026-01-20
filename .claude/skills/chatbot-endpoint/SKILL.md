---
name: chatbot-endpoint
description: Create stateless chat endpoint with conversation history management and AI agent integration (project)
---

# Skill: Chatbot Endpoint (Fast, Reliable, Observable Chat APIs)

## Description
Expert-level skill for implementing **chat endpoints** (standard + agent/tool mode) with correct streaming semantics, timeouts, retries, and production telemetry.

## When to Use
- Adding `/chat` or `/chat/agent` endpoints
- Fixing timeouts / cold-start behavior
- Implementing SSE streaming responses

## Inputs
- Backend framework (FastAPI/Express)
- Model provider (OpenAI) + tool calling requirements
- Persistence requirements (history, user profile)

## Outputs
- Stable API contract (request/response schemas)
- Streaming (SSE) + non-streaming modes
- Health + telemetry events (start/done/error)

## Playbook
1. **Define contract**
   - Request: `question`, `filters`, `stream`, `mode`, `session_id`
   - Response: `answer`, `citations`, `stream`
2. **Time budgets**
   - Client timeout + server timeout + upstream timeout
3. **Streaming**
   - Send `metadata` event first, then `token`, then `done`
4. **Errors**
   - Map upstream errors to user-safe messages
   - Log internal details with request IDs
5. **Observability**
   - Structured logs: `chat.start`, `chat.done`, `chat.error`

## Quality Checklist
- [ ] Handles Render/Vercel cold starts gracefully
- [ ] Validates input size and rejects abuse
- [ ] Never leaks secrets/system prompts
- [ ] Returns citations when RAG used

## Integration
- Pairs with: `structured-logging`, `observability-apm`, `pydantic-validation`, `security-engineer`