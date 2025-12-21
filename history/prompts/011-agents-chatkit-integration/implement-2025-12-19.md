## Context
- Stage: implement
- Feature: 011-agents-chatkit-integration
- Prompt: Implement the Agents/ChatKit integration with OpenAI function calling.

## Response

### Backend Changes
1. Created `backend/app/services/agents.py`:
   - OpenAI client with function calling
   - `retrieve_book_context` tool definition
   - `generate_agent_answer()` for non-streaming
   - `stream_agent_answer()` for streaming
   - Structured logging (agent.start, agent.tool_call, agent.done)

2. Updated `backend/app/api/chat.py`:
   - Added `/chat/agent` endpoint
   - Wired to agent service
   - Same request/response schema as `/chat`

3. Updated `backend/app/services/qdrant_client.py`:
   - Added `ensure_payload_indexes()` function
   - Created `chapter` and `section` keyword indexes

### Frontend Changes
1. Updated `src/components/RagChat.tsx`:
   - Added `mode?: 'rag' | 'agent'` prop
   - Routes to appropriate endpoint based on mode

2. Updated `src/components/FloatingChatButton.tsx`:
   - Set `mode="agent"` as default
   - Passes chapter context to agent

### Testing
- Agent correctly identifies when to use RAG tool
- Citations properly extracted from tool results
- Both modes work correctly
- Backend logs show agent decision-making

## Tests
- Manual browser testing: ✅
- Backend health check: ✅
- Agent mode with tool calls: ✅
- RAG mode fallback: ✅

