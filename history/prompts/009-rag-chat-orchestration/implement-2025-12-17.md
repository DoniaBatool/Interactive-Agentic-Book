## Context
- Stage: implement
- Feature: 009-rag-chat-orchestration
- Prompt: Implement RAG chat orchestration (API + retrieval).

## Response
- Added chat API `/chat` with request schemas, retrieval via Qdrant, OpenAI generation, citations.
- Added settings for chat model, top-k, stream; retrieval and chat services; router wiring; README updates.
- Tests: `npm test` (frontend) still passing.

## Tests
- `npm test` ✅

