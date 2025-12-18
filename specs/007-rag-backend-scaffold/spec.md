# Feature Specification: RAG Backend Scaffold

**Feature Branch**: `007-rag-backend-scaffold`  
**Created**: 2025-12-17  
**Status**: Draft  
**Input**: Build the initial backend scaffold for the RAG chatbot (FastAPI service to run on Render) to support content ingestion and chat API in later features.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Health & readiness (P1)
A developer can deploy and ping the backend to verify it’s alive.
**Acceptance**: `/health` returns 200 with status payload.

### User Story 2 - Config bootstrap (P1)
Service loads required settings (OpenAI key, Qdrant, Postgres, CORS) from env with sensible defaults for local dev.
**Acceptance**: Settings object validates env vars; server starts with missing non-critical keys gated off.

### User Story 3 - Project structure ready (P1)
Service has a clean layout for future RAG features (ingestion, chat, auth).
**Acceptance**: Directories for `api`, `core/config`, `services`, `models/schemas`, `tests`, and a `README` describing run/build steps.

## Requirements
- **FR-001**: Create a `backend/` service with FastAPI entrypoint and `/health` route.
- **FR-002**: Provide configuration loading (env-based) for OpenAI key, Qdrant URL/key, Postgres URL, allowed origins.
- **FR-003**: Add basic run instructions and dependencies (requirements.txt) suitable for Render deploy.
- **FR-004**: Establish folder structure for upcoming features (ingestion, chat, auth).

## Success Criteria
- **SC-001**: `uvicorn backend.app.main:app` runs locally; `/health` returns 200 with `{"status":"ok"}`.
- **SC-002**: Settings class validates env; missing non-critical values are handled gracefully.
- **SC-003**: README documents local run and env vars; deps pinned in requirements.txt.
- **SC-004**: Tests (if present) pass or are stubbed; repo remains buildable (`npm test` unaffected).

