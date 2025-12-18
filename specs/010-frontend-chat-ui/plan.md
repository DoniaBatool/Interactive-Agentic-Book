# Architecture Plan: Frontend Chat UI (Docusaurus) – Feature 010

## Overview

Goal: Add a reusable RAG chat UI to the Docusaurus frontend that talks to the existing FastAPI `/chat` endpoint (non-stream + SSE streaming) and shows answers with citations, without breaking the docs build.

## High-Level Design

- **Chat Component**: `src/components/RagChat.tsx`
  - Internal state: `messages`, `input`, `loading`, `error`.
  - Message model: `{ id, role: 'user' | 'assistant', content, citations? }`.
  - Props:
    - `initialQuestion?`
    - `chapterFilter?` (string)
    - Later: `sectionFilter?`, `userProfile?`.
- **SSE Streaming**:
  - Use browser `EventSource`-like behavior via `fetch` + `ReadableStream` OR `EventSource` if we adapt API.
  - For now, simplest: use `fetch` with `stream=false` for MVP and wire SSE as progressive enhancement using `fetch` + `ReadableStream` (already supported in modern browsers).
  - NOTE: Backend currently sends proper SSE (`text/event-stream`); we can consume it via `EventSource`:
    - `event: metadata` → set citations for current assistant message.
    - `event: token` → append to assistant message content.
    - `event: done` → finalize.
    - `event: error` → set error state.
- **Integration Points**:
  - A small wrapper like `src/theme/RagChatEntry.tsx` or a custom component imported into MDX pages.
  - For now, start with a **single shared component** used in:
    - `docs` pages via MDX include (e.g. `<RagChat chapter="Course Overview" />`).

## Data Flow

1. User types question and presses Send.
2. Frontend builds payload:
   ```ts
   {
     question,
     filters: chapterFilter ? { chapter: chapterFilter } : undefined,
     stream: USE_STREAMING, // bool
   }
   ```
3. Non-stream:
   - `POST /chat` → `ChatResponse { answer, citations[], stream:false }`.
   - Add user + assistant messages to local `messages` state.
4. Stream:
   - Open `EventSource` to `/chat` with `stream=true` (or use `fetch` with `ReadableStream` if we keep POST body).
   - Handle:
     - `metadata` → set citations on current assistant message.
     - `token` → append `text` chunk to current assistant message.
     - `done` → stop listening.
     - `error` → show error in UI.

## Error Handling Strategy

- Network / 4xx/5xx:
  - Show inline error “Chat service unavailable, please try again.”
  - Log to console for now; structured logs exist on backend.
- Validation:
  - If backend returns `detail`, surface as error bubble.

## Phased Implementation

1. **Phase 1 – Non-stream MVP**
   - Implement `RagChat` with non-stream POST.
   - Integrate into one MDX page (e.g. course overview).
   - Verify build + runtime.
2. **Phase 2 – Streaming**
   - Add `stream=true` path using SSE (`EventSource`) targeting `/chat`.
   - Make streaming opt-in via a prop or feature flag.
3. **Phase 3 – Context filters & polish**
   - Pass `chapter` from page.
   - Improve UI states (loading, disabled input, scroll).

## Dependencies / Config

- Backend base URL:
  - Local dev: `http://127.0.0.1:8000`.
  - Later: environment-based (e.g. `RAG_BACKEND_URL` from `.env`/Docusaurus config).
- No new external frontend libraries required; rely on React + browser APIs.


