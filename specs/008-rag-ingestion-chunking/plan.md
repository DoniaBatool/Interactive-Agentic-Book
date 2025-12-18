# Implementation Plan: RAG Ingestion & Chunking (Qdrant Wiring)

**Branch**: `008-rag-ingestion-chunking` | **Date**: 2025-12-17 | **Spec**: `specs/008-rag-ingestion-chunking/spec.md`

## Summary
Add ingestion pipeline to read docs content, chunk, embed with OpenAI, and upsert into Qdrant. Provide a CLI/entry script, configurable env vars, and metadata for chapters/sections. Keep idempotent upsert behavior. Target backend on Render; Qdrant Cloud and OpenAI keys via env.

## Technical Context
**Language**: Python 3.11+  
**Framework**: FastAPI backend; ingestion as script/CLI  
**Deps**: openai (client), qdrant-client, pydantic-settings, tiktoken (optional chunking assist)  
**Config**: env vars for OPENAI_API_KEY, QDRANT_URL, QDRANT_API_KEY, QDRANT_COLLECTION (default `textbook-chunks`), EMBEDDING_MODEL (default `text-embedding-3-small`), EMBEDDING_DIM (default 1536)  
**Input**: Markdown/MDX under `docs/`  
**Output**: Qdrant collection with chunk vectors + metadata

## Constitution Check
- Spec and plan before implementation.  
- Tests: ensure frontend `npm test` still green; add minimal ingestion dry-run guard.  
- Docs: Update backend README with ingestion usage/env.

## Project Structure (this feature)
```
backend/
  app/
    services/ingestion.py
    services/qdrant_client.py
    models/schemas/chunk.py
  scripts/ingest.py (optional entry)
```

## Implementation Notes
- Chunk by paragraphs with max token/char length; fallback to simple splitting if tiktoken unavailable.
- Include metadata: path, chapter (from filename), section (best-effort heading extraction).
- Upsert to Qdrant; create collection if missing with given dim.
- Log counts (files, chunks) for visibility.

