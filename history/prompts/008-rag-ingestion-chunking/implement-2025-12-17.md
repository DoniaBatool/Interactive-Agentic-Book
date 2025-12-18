## Context
- Stage: implement
- Feature: 008-rag-ingestion-chunking
- Prompt: Implement RAG ingestion/chunking with Qdrant wiring.

## Response
- Added ingestion pipeline: chunk markdown, embed via OpenAI, upsert to Qdrant with metadata and idempotent upsert.
- Added helper modules (`services/ingestion.py`, `services/qdrant_client.py`, schemas for chunks).
- Added CLI `backend/scripts/ingest.py`, updated `requirements.txt`, config (collection/model/dim), and README ingestion instructions.
- Tests: `npm test` still passes.

## Tests
- `npm test` ✅

