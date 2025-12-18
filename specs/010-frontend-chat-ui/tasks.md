---
description: "Tasks for Frontend Chat UI (Docusaurus) – Feature 010"
---

# Tasks: Frontend Chat UI (Docusaurus)

**Input**: spec.md, plan.md  
**Tests**: manual browser test + `npm test` & `npm run build` must stay green.

## Phase 1: Non-stream MVP
- [x] T010-001 Create `src/components/RagChat.tsx` with:
  - Local `messages` state (`role`, `content`, `citations?`).
  - Input box + send button.
  - Simple non-stream `POST /chat` call (backend URL configurable).
- [ ] T010-002 Add basic styling/layout (panel or card) that works inside a docs page.
- [ ] T010-003 Expose a simple prop API:
  - `chapterFilter?: string`
  - `backendUrl?: string` (default to `http://127.0.0.1:8000` for now).

## Phase 2: Docs integration
- [x] T010-010 Add a small wrapper (e.g. `src/components/RagChatPanel.tsx`) for embedding in MDX.
- [x] T010-011 Integrate chat panel into at least one MDX page (e.g. course overview) with a chapter filter.
- [ ] T010-012 Verify `npm test` and `npm run build` succeed after integration.

## Phase 3: Streaming & polish
- [x] T010-020 Add optional streaming support:
  - When `useStreaming` prop is true, call `/chat` with `stream=true` and consume SSE events.
  - Update assistant message content incrementally from `token` events.
  - Attach citations from `metadata` event once.
- [ ] T010-021 Add UX polish:
  - Loading spinner / state while waiting.
  - Disable send while a request is in-flight (or support cancel).
  - Auto-scroll to bottom on new messages.
- [ ] T010-022 Error handling:
  - Show inline error message in chat on network/HTTP errors.
  - Do not crash the page if backend is unreachable.


