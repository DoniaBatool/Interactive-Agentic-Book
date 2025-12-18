# RAG Backend Scaffold

FastAPI service for the RAG chatbot. Target: Render (container). Frontend: Vercel (Docusaurus).

## Quickstart
```bash
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
```

Test health:
```bash
curl http://localhost:8000/health
```

## Environment
- `OPENAI_API_KEY`
- `QDRANT_URL`, `QDRANT_API_KEY`
- `QDRANT_COLLECTION` (default: textbook-chunks)
- `EMBEDDING_MODEL` (default: text-embedding-3-small)
- `EMBEDDING_DIM` (default: 1536)
- `RETRIEVAL_TOP_K` (default: 5)
- `CHAT_MODEL` (default: gpt-4o-mini)
- `CHAT_STREAM` (default: False)
- `DATABASE_URL` (optional for now)
- `ALLOWED_ORIGINS` (optional; defaults to http://localhost:3000)

## Structure
```
backend/
  app/
    main.py
    core/config.py
    api/
    models/schemas/
    services/
    tests/
  scripts/ingest.py
```

## Notes
- CORS allows localhost for dev; update before production.
- Future features will add ingestion, chat endpoints, and DB/Qdrant wiring.

## Ingestion
```bash
pip install -r backend/requirements.txt
python backend/scripts/ingest.py --docs-dir docs
# add --dry-run to skip OpenAI/Qdrant calls
```
Env required for real ingestion: `OPENAI_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY` (optional overrides: `QDRANT_COLLECTION`, `EMBEDDING_MODEL`, `EMBEDDING_DIM`).

## Chat API
Start server:
```bash
uvicorn backend.app.main:app --reload
```

Call chat:
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What is Physical AI?","filters":{"chapter":"Course Overview"},"stream":false}'
```
Requires ingestion completed and OpenAI/Qdrant env set.

Streaming (Server-Sent Events):
```bash
curl -N -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"What is Physical AI?","stream":true}'
# SSE events: metadata (citations), token chunks, then done
```

