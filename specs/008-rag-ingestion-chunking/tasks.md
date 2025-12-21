---
description: "Tasks for RAG Ingestion & Chunking"
---

# Tasks: RAG Ingestion & Chunking

**Input**: spec.md, plan.md  
**Tests**: run ingestion locally; ensure `npm test` stays green.

## Phase 1: Setup
- [x] T001 Add/verify backend deps: openai, qdrant-client, tiktoken (optional), update requirements.txt.
- [x] T002 Create skeleton files: `backend/app/services/ingestion.py`, `backend/app/services/qdrant_client.py`, `backend/app/models/schemas/chunk.py`, optional `backend/scripts/ingest.py`.

## Phase 2: Implementation
- [x] T010 Implement settings additions (collection name, embedding model/dim).
- [x] T011 Implement Qdrant helper (create collection if missing, upsert).
- [x] T012 Implement chunking (read docs/, split into chunks, add metadata path/chapter/section).
- [x] T013 Implement embedding + upsert pipeline (OpenAI embeddings → Qdrant upsert, idempotent).

## Phase 3: Verify
- [x] T020 Add README ingestion section (env, run command, expected output).
- [x] T021 Run ingestion locally (with real keys or dry-run if keys absent) and report counts.
- [x] T022 Run `npm test` to confirm frontend unaffected.

