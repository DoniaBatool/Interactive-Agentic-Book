# Feature Specification: RAG Chat Orchestration (API + Retrieval)

**Feature Branch**: `009-rag-chat-orchestration`  
**Created**: 2025-12-17  
**Status**: Draft  
**Input**: Implement chat API with retrieval from Qdrant, OpenAI generation, and citations, to power the textbook chatbot.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask a question (P1)
User sends a question; API returns an answer grounded in the textbook with citations.
**Acceptance**: `/chat` endpoint responds 200 with answer, sources, and metadata.

### User Story 2 - Streaming (P2)
User can receive streamed tokens for the answer.
**Acceptance**: Streaming variant returns incremental chunks.

### User Story 3 - Context filtering (P2)
API can filter context by chapter/section when provided.
**Acceptance**: Query parameters or payload allow optional filters; retrieval honors them.

## Requirements
- **FR-001**: Add `/chat` POST endpoint (JSON) that takes `question`, optional `filters` (chapter/section), optional `stream` flag.
- **FR-002**: Retrieve top-k chunks from Qdrant using embeddings; include metadata in citations.
- **FR-003**: Generate answer via OpenAI chat model (default GPT-4o or 4o-mini) with provided context; return citations.
- **FR-004**: Support streaming responses when requested (server-sent or chunked).
- **FR-005**: Log basic telemetry (latency, retrieved count) for debugging.

## Success Criteria
- **SC-001**: `/chat` returns grounded answers with citations (path/chapter/section) and 200 status.
- **SC-002**: Retrieval respects optional filters and returns configurable top-k.
- **SC-003**: Streaming mode works without errors.
- **SC-004**: README updated with API usage and env notes; `npm test` remains green.

