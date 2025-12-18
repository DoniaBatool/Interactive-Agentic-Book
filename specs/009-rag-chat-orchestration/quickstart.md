# Quickstart: RAG Chat Orchestration

1) Ensure ingestion done with valid keys.
2) Start backend: `uvicorn backend.app.main:app --reload`
3) POST `/chat` with JSON: `{"question":"...","filters":{"chapter":"..."},"stream":false}`
4) Optional stream: set `stream:true` and read chunked response.

