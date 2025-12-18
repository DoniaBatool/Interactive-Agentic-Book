# Research Notes – Feature 010: Frontend Chat UI

- Docusaurus 3 uses MDX; React components like `RagChatPanel` can be imported directly into docs pages.
- Streaming with FastAPI + `StreamingResponse` exposes SSE-compatible `text/event-stream` responses, which can be consumed in the browser via:
  - `EventSource` (GET-only, not ideal with JSON POST body).
  - `fetch` + `ReadableStream` (used here) to manually parse SSE frames.
- Frontend keeps state client-side; no persistence yet (to be added when Postgres/auth features are implemented).


