# Feature Specification: Frontend Chat UI (Docusaurus) – RAG Textbook Assistant

**Feature Number**: 010  
**Feature Branch**: `010-frontend-chat-ui`  
**Status**: Draft  
**Input**: Existing RAG backend (`/chat` API with streaming + citations) and Docusaurus book.

## User Scenarios & Testing *(mandatory)*

### User Story 1 – Ask a question from the book (P1)
As a learner reading the textbook, I can open a chat panel, ask a question about the current chapter, and see an answer with cited sources from the book.

**Acceptance**:
- From any chapter page, a visible “Ask the AI” button or panel opens the chat UI.
- I can type a question and submit.
- The UI shows the assistant’s answer and a list of source snippets/links (path + chapter + section).

### User Story 2 – Streaming experience (P2)
As a learner, I see the answer stream in token-by-token (or chunk-by-chunk) so I don’t have to wait for the full response.

**Acceptance**:
- When streaming is enabled, the answer area progressively fills as tokens arrive from `/chat` with `stream=true`.
- If streaming fails, the UI falls back gracefully with an error message.

### User Story 3 – Context awareness by chapter (P2)
As a learner, when I ask questions from a specific chapter page, the assistant automatically prefers that chapter as context.

**Acceptance**:
- Chat requests from a chapter route pass an appropriate `filters.chapter` (e.g. page metadata/slug → chapter label).
- When filters are active, citations mostly reference that chapter (assuming content exists).

### User Story 4 – Error & empty-state handling (P2)
As a learner, if something goes wrong (backend down, invalid response), I see a clear message and can retry.

**Acceptance**:
- If the `/chat` call fails (network or 4xx/5xx), the UI shows a friendly error in the chat timeline.
- The UI does not crash the page; I can retry another question.

## Requirements

- **FR-001**: Add a reusable chat UI component in the Docusaurus frontend (e.g. `src/components/RagChat.tsx`) that:
  - Renders a chat history (user + assistant turns).
  - Has an input box with send button and “Enter to send”.
  - Displays citations for each assistant message (list of sources from backend).
- **FR-002**: Integrate with backend `/chat`:
  - Non-stream mode: simple POST and render full answer + citations.
  - Stream mode (`stream=true`): consume SSE events (`metadata`, `token`, `done`, `error`) and update UI incrementally.
- **FR-003**: Wire chat UI into textbook pages:
  - Add a chat entry point on chapter pages (e.g. floating button or sidebar panel).
  - Pass chapter context (and later section) as `filters` where possible.
- **FR-004**: Basic UX polish:
  - Loading state while answer is being generated.
  - Disabled input while a request is in-flight (or support cancel).
  - Scroll-to-bottom behavior when new messages appear.

## Non-Functional Requirements

- **NFR-001**: The chat UI must not break static build (`npm run build`) or tests (`npm test`).
- **NFR-002**: Handle missing backend gracefully (e.g. when running docs only) with a clear message.
- **NFR-003**: Keep dependencies minimal; prefer using existing Docusaurus/React stack and browser `EventSource` for SSE.

## Success Criteria

- **SC-001**: From a Docusaurus chapter page, a learner can ask a question and receive an answer with citations via the RAG backend.
- **SC-002**: Streaming mode works in at least one modern browser (Chrome) and passes manual smoke test.
- **SC-003**: Chat UI integration does not break existing docs navigation, build, or tests.
- **SC-004**: Code is organized and documented so that later features (auth, personalization, Urdu toggle) can hook into the same chat UI without major refactors.


