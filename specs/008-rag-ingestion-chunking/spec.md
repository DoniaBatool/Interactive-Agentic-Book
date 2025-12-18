# Feature Specification: RAG Ingestion & Chunking (Qdrant Wiring)

**Feature Branch**: `008-rag-ingestion-chunking`  
**Created**: 2025-12-17  
**Status**: Draft  
**Input**: Implement ingestion of textbook content into Qdrant with embeddings, readying the RAG stack for chat.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ingest content (P1)
Developer can run an ingestion command to read docs, chunk content, embed, and upsert to Qdrant.
**Acceptance**: Command succeeds given valid env (OpenAI, Qdrant); reports counts.

### User Story 2 - Re-run safely (P1)
Ingestion can be re-run idempotently (same collection, upsert replaces/updates).
**Acceptance**: Re-running does not error; upserts without duplicates.

### User Story 3 - Observe status (P2)
Developer sees basic logging/metrics (files processed, chunks stored).
**Acceptance**: Output includes file count, chunk count, collection name.

## Requirements
- **FR-001**: Provide an ingestion entrypoint (CLI/script) that reads Markdown/MDX docs from `docs/` (default) and ingests into Qdrant.
- **FR-002**: Chunk content with metadata (chapter, relative path, section heading if available).
- **FR-003**: Embed using OpenAI embeddings (model configurable; default `text-embedding-3-small`) and upsert to Qdrant collection (configurable; default `textbook-chunks`).
- **FR-004**: Support idempotent reruns (upsert) and configurable vector size (default 1536).
- **FR-005**: Document required env vars and usage in backend README.

## Success Criteria
- **SC-001**: Ingestion script runs locally with valid env; writes to configured Qdrant collection.
- **SC-002**: Chunks carry metadata: `path`, `chapter`, `source`, and `section` when available.
- **SC-003**: Re-running ingestion completes without duplicate errors (upsert behavior).
- **SC-004**: README updated with ingestion instructions and env variables.

