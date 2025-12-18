---
description: "Tasks for RAG Backend Scaffold"
---

# Tasks: RAG Backend Scaffold

**Input**: spec.md, plan.md  
**Tests**: none required yet; ensure `npm test` still passes and backend health runs locally.

## Phase 1: Setup
- [ ] T001 Create `backend/` layout with `app/`, `api/`, `core/`, `models/schemas/`, `services/`, `tests/`, and `README.md`.
- [ ] T002 Add `backend/requirements.txt` with pinned deps (FastAPI, uvicorn, pydantic-settings, qdrant-client stub, python-dotenv for dev).

## Phase 2: Foundational
- [ ] T010 Add `backend/app/main.py` with FastAPI app and `/health` route returning status ok.
- [ ] T011 Add `backend/app/core/config.py` settings class (env vars: OPENAI_API_KEY, QDRANT_URL, QDRANT_API_KEY, DATABASE_URL, ALLOWED_ORIGINS).
- [ ] T012 Wire CORS placeholder (localhost origins) in main.py.

## Phase 3: Polish
- [ ] T020 Update `backend/README.md` with run instructions and env vars.
- [ ] T021 Verify backend starts: `uvicorn backend.app.main:app --reload` and hit `/health`.
- [ ] T022 Run `npm test` to confirm frontend unaffected.

