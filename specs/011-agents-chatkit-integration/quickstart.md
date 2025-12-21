# Quickstart – Feature 011: Agents/ChatKit Integration

## Prerequisites

- Backend running with RAG service
- Qdrant vector database populated
- OpenAI API key configured

## Run Backend

```bash
cd C:\Users\Leo\interactive-agentic-book
venv\Scripts\activate
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Verify health:
```bash
curl http://localhost:8000/health
```

## Run Frontend

```bash
cd C:\Users\Leo\interactive-agentic-book
npm run start
```

## Test Agent Mode

1. Open browser: `http://localhost:3000`
2. Navigate to any chapter page
3. Click the floating chat button (bottom-right)
4. Ask a question: "What is Physical AI?"
5. Observe:
   - Chapter badge shows current chapter
   - Response includes citations from textbook
   - Backend logs show `agent.start` and `agent.done` events

## Test RAG Mode

To test basic RAG mode (without agent):

1. In `FloatingChatButton.tsx`, change `mode="agent"` to `mode="rag"`
2. Restart frontend
3. Ask the same question
4. Compare responses

## Backend Logs

Watch for these log entries:
```
INFO: agent.start - Processing question: "What is Physical AI?"
INFO: agent.tool_call - retrieve_book_context with query: "Physical AI"
INFO: agent.tool_result - Retrieved 5 chunks
INFO: agent.done - Generated answer with 3 citations
```

## Endpoints

| Endpoint | Mode | Description |
|----------|------|-------------|
| `POST /chat` | RAG | Basic retrieval-augmented generation |
| `POST /chat/agent` | Agent | Function calling with tool use |

Both endpoints accept the same request schema and return the same response schema.

