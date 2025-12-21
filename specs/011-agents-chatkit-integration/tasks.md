---
description: "Tasks for Agents/ChatKit Integration – Feature 011"
---

# Tasks: Agents/ChatKit Integration

**Input**: spec.md, plan.md  
**Tests**: Backend unit tests + manual browser testing.

## Phase 1: Agent Service
- [x] T011-001 Create `backend/app/services/agents.py` with:
  - OpenAI client initialization with function calling
  - System prompt for textbook assistant role
  - `retrieve_book_context` tool definition (JSON schema)
  - `generate_agent_answer()` function for non-streaming
  - `stream_agent_answer()` function for streaming (optional)

- [x] T011-002 Implement tool execution:
  - Parse tool_call from OpenAI response
  - Execute RAG retrieval via existing `rag.py` service
  - Format tool result for OpenAI consumption
  - Handle tool execution errors gracefully

- [x] T011-003 Add structured logging:
  - Log `agent.start` with question and context
  - Log `agent.tool_call` with tool name and parameters
  - Log `agent.tool_result` with chunk count
  - Log `agent.done` with response summary

## Phase 2: API Endpoint
- [x] T011-010 Add `/chat/agent` endpoint in `backend/app/api/chat.py`:
  - Accept `ChatRequest` schema (same as `/chat`)
  - Call `generate_agent_answer()` from agents service
  - Return `ChatResponse` schema (answer + citations)

- [x] T011-011 Wire streaming support (optional):
  - Accept `stream=true` parameter
  - Return SSE stream via `stream_agent_answer()`

- [x] T011-012 Add Qdrant payload indexes:
  - Create `chapter` keyword index for filtering
  - Create `section` keyword index for filtering
  - Ensure indexes exist on startup

## Phase 3: Frontend Integration
- [x] T011-020 Update `RagChat.tsx`:
  - Add `mode?: 'rag' | 'agent'` prop
  - Route to `/chat` for `mode="rag"`
  - Route to `/chat/agent` for `mode="agent"`
  - Default to `mode="rag"` for backward compatibility

- [x] T011-021 Update `FloatingChatButton.tsx`:
  - Set `mode="agent"` as default for floating chat
  - Pass chapter context to agent endpoint

- [x] T011-022 Test both modes:
  - Verify RAG mode still works via `/chat`
  - Verify Agent mode works via `/chat/agent`
  - Check that citations appear correctly in both modes

## Phase 4: Documentation & Status
- [x] T011-030 Create STATUS.md with implementation summary
- [x] T011-031 Update remaining features list
- [x] T011-032 Complete spec folder documentation

