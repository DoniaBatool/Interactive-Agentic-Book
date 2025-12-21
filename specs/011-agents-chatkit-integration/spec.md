# Feature Specification: Agents/ChatKit Integration – RAG Textbook Assistant

**Feature Number**: 011  
**Feature Branch**: `011-agents-chatkit-integration`  
**Status**: ✅ Complete  
**Input**: Existing RAG backend (`/chat` API) and Frontend Chat UI (Feature 010).

## User Scenarios & Testing *(mandatory)*

### User Story 1 – Intelligent Tool Use (P1)
As a learner, when I ask a question, the AI agent intelligently decides whether to retrieve textbook context or answer directly from its knowledge.

**Acceptance**:
- Simple greetings ("Hi", "Hello") are answered directly without RAG retrieval.
- Subject-specific questions ("What is Physical AI?") trigger the `retrieve_book_context` tool.
- Backend logs show `agent.start` and `agent.done` events with tool call details.

### User Story 2 – Chapter-Aware Context (P1)
As a learner on a specific chapter page, the agent receives my current chapter context and prioritizes relevant content.

**Acceptance**:
- The `chapterFilter` from frontend is passed to the agent's system prompt.
- Retrieved chunks prioritize the current chapter when available.
- Citations in responses reference the appropriate chapter.

### User Story 3 – Seamless Mode Switching (P2)
As a developer, I can switch between basic RAG mode and Agent mode using a simple prop.

**Acceptance**:
- `mode="rag"` uses the `/chat` endpoint (basic RAG).
- `mode="agent"` uses the `/chat/agent` endpoint (Agents with function calling).
- Both modes return the same response schema for frontend compatibility.

### User Story 4 – Function Calling Flow (P1)
As an AI agent, I can call the `retrieve_book_context` tool to get relevant textbook content.

**Acceptance**:
- OpenAI function calling is properly configured with tool schema.
- Tool execution retrieves top-k chunks from Qdrant.
- Tool results are incorporated into the final response.

## Requirements

- **FR-001**: Create `backend/app/services/agents.py` with:
  - OpenAI client integration with function calling.
  - `retrieve_book_context` tool definition and implementation.
  - System prompt that describes the agent's role as a textbook assistant.
  - Support for both streaming and non-streaming responses.

- **FR-002**: Add `/chat/agent` API endpoint:
  - Accept same request schema as `/chat`.
  - Use agent-based flow with function calling.
  - Return same response schema (answer + citations).

- **FR-003**: Update frontend `RagChat` component:
  - Add `mode` prop with values `'rag'` | `'agent'`.
  - Route requests to appropriate endpoint based on mode.
  - Default `FloatingChatButton` to use `mode="agent"`.

- **FR-004**: Structured logging and telemetry:
  - Log `agent.start` when agent processing begins.
  - Log tool calls with parameters and results.
  - Log `agent.done` with final response details.

## Non-Functional Requirements

- **NFR-001**: Agent response latency should be within 2x of basic RAG (acceptable for function calling overhead).
- **NFR-002**: Function calling must handle edge cases (no relevant context found, tool errors).
- **NFR-003**: Backward compatibility – existing `/chat` endpoint continues to work.

## Success Criteria

- **SC-001**: Agent correctly identifies when to use the RAG tool vs. direct answers.
- **SC-002**: Citations are properly extracted from tool results and included in response.
- **SC-003**: Frontend seamlessly switches between RAG and Agent modes.
- **SC-004**: Backend logs provide clear visibility into agent decision-making.

