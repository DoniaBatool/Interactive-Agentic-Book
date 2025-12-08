# Task List: Real-Time AI Interaction Layer — Streaming

**Feature**: 050-live-ai-interaction
**Created**: 2025-01-27
**Status**: Draft

## Task Groups

### 1. Backend Streaming Core Tasks

- [ ] **T050-001** (P1) - Create `backend/app/ai/streaming/__init__.py`
  - Create package initialization file
  - File: `backend/app/ai/streaming/__init__.py`

- [ ] **T050-002** (P1) - Create `backend/app/ai/streaming/stream_manager.py`
  - Implement StreamManager class (placeholder)
  - Add TODO: Manage Server-Sent Events (SSE) or WebSockets
  - Add TODO: Attach to runtime engine pipeline
  - Add TODO: Handle streaming token generation
  - File: `backend/app/ai/streaming/stream_manager.py`

- [ ] **T050-003** (P1) - Update `backend/app/ai/runtime/engine.py`
  - Add TODO comment: "If streaming mode enabled, yield tokens"
  - Add placeholder for streaming hook
  - File: `backend/app/ai/runtime/engine.py`

### 2. Backend API Tasks

- [ ] **T050-010** (P1) - Create `backend/app/api/streaming.py`
  - Create FastAPI router
  - Implement GET /api/stream/ai-block/{block_type} endpoint (placeholder)
  - Return mocked streaming chunks in SSE format
  - Add TODO comments for real implementation
  - File: `backend/app/api/streaming.py`

- [ ] **T050-011** (P1) - Integrate streaming router into main FastAPI router
  - Import streaming router
  - Include router in main app
  - File: `backend/app/main.py` or router file

### 3. Frontend Streaming Client Tasks

- [ ] **T050-020** (P1) - Create `frontend/src/ai/streamClient.ts`
  - Implement SSE connector (placeholder)
  - Implement WebSocket connector (placeholder, optional)
  - Implement event handlers for chunk, error, complete
  - Add TODO comments for real implementation
  - File: `frontend/src/ai/streamClient.ts`

- [ ] **T050-021** (P1) - Create `frontend/src/ai/streamHooks.ts`
  - Implement useAIStreaming() React hook (placeholder)
  - Implement useAIBlockStreaming(blockType) React hook (placeholder)
  - Add TODO comments for real implementation
  - File: `frontend/src/ai/streamHooks.ts`

### 4. Frontend Component Update Tasks

- [ ] **T050-030** (P1) - Update `frontend/src/components/AskQuestionBlock.tsx`
  - Add placeholder streaming UI
  - Add TODO comments for streaming output
  - File: `frontend/src/components/AskQuestionBlock.tsx` (or appropriate path)

- [ ] **T050-031** (P1) - Update `frontend/src/components/ExplainELI10Block.tsx`
  - Add placeholder streaming UI
  - Add TODO comments for streaming output
  - File: `frontend/src/components/ExplainELI10Block.tsx` (or appropriate path)

- [ ] **T050-032** (P1) - Update `frontend/src/components/QuizBlock.tsx`
  - Add placeholder streaming UI
  - Add TODO comments for streaming output
  - File: `frontend/src/components/QuizBlock.tsx` (or appropriate path)

- [ ] **T050-033** (P1) - Update `frontend/src/components/DiagramBlock.tsx`
  - Add placeholder streaming UI
  - Add TODO comments for streaming output
  - File: `frontend/src/components/DiagramBlock.tsx` (or appropriate path)

### 5. Configuration Tasks

- [ ] **T050-040** (P1) - Update `backend/app/config/settings.py`
  - Add AI_STREAMING_ENABLED: bool = False
  - Add STREAMING_BACKEND: str = "sse"
  - File: `backend/app/config/settings.py`

- [ ] **T050-041** (P2) - Update `.env.example`
  - Add AI_STREAMING_ENABLED=false
  - Add STREAMING_BACKEND=sse
  - File: `.env.example`

### 6. Contract Tasks

- [ ] **T050-050** (P1) - Create `specs/050-live-ai-interaction/contracts/stream-schema.yaml`
  - Define streaming chunk schema
  - Define SSE/WebSocket compatibility expectations
  - Define event types
  - File: `specs/050-live-ai-interaction/contracts/stream-schema.yaml`

---

## Implementation Notes

### Scaffolding Only
- All tasks create scaffolding/placeholders only
- No real streaming logic implementation
- TODO comments indicate future implementation

### Priority Levels
- **P1**: Critical for feature completion
- **P2**: Optional enhancements (.env.example)

### File Paths
- All file paths are relative to project root
- Use exact paths as specified

### Testing
- Manual testing recommended after each task group
- Verify streaming endpoints return mocked chunks
- Verify frontend components compile

---

## Acceptance Criteria Checklist

- [ ] Streaming backend infrastructure created
- [ ] Streaming API endpoints created (mocked responses)
- [ ] Frontend streaming client created
- [ ] Frontend streaming hooks created
- [ ] AI Block components updated with streaming placeholders
- [ ] Configuration variables added
- [ ] Contracts created
- [ ] Project starts without errors
- [ ] Streaming endpoints return mocked chunked responses
- [ ] Frontend components compile and contain streaming hooks

