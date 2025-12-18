# Contracts – Feature 010: Frontend Chat UI

- **Backend contract**: `POST /chat`
  - Request: `{ question: string; filters?: { chapter?: string; section?: string }; stream?: boolean }`
  - Non-stream response: `{ answer: string; citations: { path: string; chapter: string; section?: string | null; score?: number | null }[]; stream: false }`
  - Streaming (SSE) events:
    - `event: metadata` – `data: { citations: Citation[]; stream: true }`
    - `event: token` – `data: { text: string }`
    - `event: done` – `data: { duration_ms: number }`
    - `event: error` – `data: { message: string }`

- **Frontend contract**:
  - `RagChat` props: `{ backendUrl?: string; chapterFilter?: string; useStreaming?: boolean }`
  - `RagChatPanel` props: `{ chapter?: string }`


