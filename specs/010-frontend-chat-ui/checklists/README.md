# Checklists – Feature 010: Frontend Chat UI

## Dev Checklist
- [x] Spec, plan, tasks created in `specs/010-frontend-chat-ui/`.
- [x] Non-stream chat UI implemented and wired to `/chat`.
- [x] Streaming (SSE) path implemented and guarded by `useStreaming` prop.
- [ ] Backend URL configurable for local vs deployed environments.
- [x] Integrated into at least one docs page (`docs/course-overview.md`).

## QA Checklist
- [ ] Ask a simple question and receive an answer with citations.
- [ ] Streaming shows incremental tokens without page reload.
- [ ] Error state when backend is down shows a friendly message.
- [ ] Docs build (`npm run build`) passes without front matter errors.


