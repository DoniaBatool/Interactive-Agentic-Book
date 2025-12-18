# Implementation Plan: RAG Chat Orchestration (API + Retrieval)

**Branch**: `009-rag-chat-orchestration` | **Date**: 2025-12-17 | **Spec**: `specs/009-rag-chat-orchestration/spec.md`

## Summary
Build `/chat` API on FastAPI backend to retrieve chunks from Qdrant, generate answers with OpenAI, and return citations. Support optional filters (chapter/section) and streaming responses. Keep defaults minimal; target backend on Render later, frontend on Vercel.

## Technical Context
**Backend**: FastAPI (existing `backend/`)  
**Deps**: openai client (already added), qdrant-client (already added)  
**Retrieval**: Qdrant search by embeddings, top-k configurable (default 5)  
**Generation**: OpenAI chat model (default gpt-4o or 4o-mini)  
**Responses**: JSON with `answer`, `citations` (metadata), optional streaming  
**Config**: TOP_K, CHAT_MODEL, STREAM default; filter by chapter/section in payload  
**Frontend**: Will consume this endpoint later (separate feature)

## Constitution Check
- Spec/plan present.  
- Tests: ensure `npm test` still passes; add minimal backend test or manual curl.  
- Docs: Update backend README with `/chat` usage.

## Project Structure (this feature)
```
backend/app/api/chat.py
backend/app/services/retrieval.py
backend/app/services/chat.py
backend/app/models/schemas/chat.py
backend/app/core/config.py (add chat/retrieval settings)
```

## Implementation Notes
- Add settings: CHAT_MODEL (default gpt-4o-mini), RETRIEVAL_TOP_K (default 5), STREAM default False.
- Retrieval uses embedding model from previous feature.
- Return citations with path/chapter/section; include scores.
- Streaming: use async generator / EventSourceResponse or chunked response; keep simple chunked text.

