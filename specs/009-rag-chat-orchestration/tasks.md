---
description: "Tasks for RAG Chat Orchestration"
---

# Tasks: RAG Chat Orchestration

**Input**: spec.md, plan.md  
**Tests**: backend chat flow manual (curl) + `npm test` for frontend unaffected.

## Phase 1: Setup
- [ ] T001 Add settings for CHAT_MODEL (default gpt-4o-mini), RETRIEVAL_TOP_K (default 5), STREAM default False.
- [ ] T002 Create schema file `backend/app/models/schemas/chat.py` for request/response.

## Phase 2: Implementation
- [ ] T010 Add retrieval service `backend/app/services/retrieval.py` (embed question, query Qdrant, respect filters chapter/section, return chunks + scores).
- [ ] T011 Add chat service `backend/app/services/chat.py` (build prompt with context, call OpenAI chat model, streaming optional).
- [ ] T012 Add API route `backend/app/api/chat.py` with POST `/chat` (payload question, filters, stream).
- [ ] T013 Wire router into FastAPI app (update `main.py`).

## Phase 3: Verify
- [ ] T020 Update backend README with `/chat` usage and curl examples.
- [ ] T021 Manual test: ingest (if keys present), then POST `/chat` and verify answer + citations; test stream flag.
- [ ] T022 Run `npm test` to confirm frontend unaffected.

