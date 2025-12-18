# Implementation Plan: RAG Backend Scaffold

**Branch**: `007-rag-backend-scaffold` | **Date**: 2025-12-17 | **Spec**: `specs/007-rag-backend-scaffold/spec.md`

## Summary
Create a FastAPI backend scaffold in `backend/` for the RAG chatbot. Include health route, env-driven settings, dependency pins, and a directory layout ready for ingestion/chat/auth. Target Render for deployment; Neon Postgres and Qdrant Cloud will be integrated in later features.

## Technical Context
**Language**: Python 3.11+  
**Framework**: FastAPI + uvicorn  
**Deps**: pydantic-settings, qdrant-client (stub for later), httpx (optional), python-dotenv (dev)  
**Structure**: `backend/app/{main.py, api/, core/config.py, models/schemas/, services/, tests/}`  
**Config**: Env vars for OPENAI_API_KEY, QDRANT_URL/API_KEY, DATABASE_URL, ALLOWED_ORIGINS  
**Run**: `uvicorn backend.app.main:app --reload` (local)  
**Deploy**: Render (container) in later step

## Constitution Check
- Spec + plan present before implementation.  
- Tests: none required yet, but `npm test` should remain green; backend scaffold should run without breaking frontend.  
- Docs-first: README for backend run/deploy instructions.

## Project Structure (this feature)
```
backend/
  README.md
  requirements.txt
  app/
    __init__.py
    main.py
    api/
    core/
      __init__.py
      config.py
    models/
      __init__.py
      schemas/
        __init__.py
    services/
    tests/
```

## Implementation Notes
- Keep config minimal; allow missing non-critical keys but validate types.
- CORS placeholder; allow localhost for now.
- No ingestion/chat logic yet—stub only.

