# Quickstart: RAG Ingestion & Chunking

1) Set env: OPENAI_API_KEY, QDRANT_URL, QDRANT_API_KEY (optional dry-run if unset).
2) Install deps: `pip install -r backend/requirements.txt`
3) Run ingestion: `python backend/scripts/ingest.py --docs-dir docs`
4) Verify output: chunk/file counts; collection in Qdrant.

