# Research Notes: RAG Backend Scaffold

Targets: FastAPI service on Render; Qdrant Cloud + Neon Postgres later.
- Use FastAPI + uvicorn as base.
- Config via pydantic settings; allow missing non-critical keys initially.
- Prepare for CORS (frontend on Vercel; localhost for dev).
- Keep deps minimal; add qdrant-client stub now for later integration.

