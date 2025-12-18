## Context
- Stage: implement
- Feature: 010-frontend-chat-ui
- Prompt: Implement the Docusaurus frontend chat UI that connects to the RAG backend, supports streaming, and shows citations, without breaking tests/build.

## Response
- Implemented `src/components/RagChat.tsx` with:
  - Local `messages` state, input handling, and error state.
  - Non-stream POST `/chat` integration and SSE streaming via `fetch` + `ReadableStream`.
  - Incremental token updates and citation display per assistant message.
- Added `src/components/RagChatPanel.tsx` and integrated it into `docs/course-overview.md` under “Chat with the Textbook Assistant”.
- Fixed YAML front matter for `docs/modules/gazebo-unity.md`, `docs/modules/nvidia-isaac.md`, `docs/modules/ros2.md`, and `docs/modules/vla-capstone.md` so `npm run build` passes.
- Added supporting docs in `specs/010-frontend-chat-ui/` (`contracts/`, `checklists/`, `quickstart.md`, `research.md`, `data-model.md`) and a combined setup PHR.

## Tests
- `npm test` ✅ (course structure + typecheck)
- `npm run build` ✅ (Docusaurus static build)


