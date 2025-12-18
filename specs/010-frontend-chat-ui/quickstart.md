# Quickstart – Feature 010: Frontend Chat UI

## Run Backend (RAG)

```bash
cd /mnt/c/Users/Leo/interactive-agentic-book
python3 -m uvicorn backend.app.main:app --reload
```

Ensure health:

```bash
curl -s http://127.0.0.1:8000/health
```

## Ingest Docs

```bash
PYTHONPATH=. python3 backend/scripts/ingest.py --docs-dir docs
```

## Run Docusaurus Dev Server

```bash
cd /mnt/c/Users/Leo/interactive-agentic-book
npm run start
```

Then open the **Course Overview** page and use the **Chat with the Textbook Assistant** panel.


