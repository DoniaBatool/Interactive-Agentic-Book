# Tasks: Chapter 3 — RAG Pipeline + Embeddings + AI Runtime Integration

**Feature**: 040-ch3-rag-runtime | **Branch**: `040-ch3-rag-runtime` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating Chapter 3 RAG + runtime scaffolding. All tasks are placeholder-only—no real logic implemented.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category`: CHUNKS (Chunks source), EMBEDDINGS (Embeddings layer), QDRANT (Qdrant storage), PIPELINE (RAG pipeline), RUNTIME (Runtime engine), API (API layer), CONFIG (Config layer), VALIDATION (Validation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prepare for implementation.

- [ ] [T001] [P1] [SETUP] Verify Feature 037 (Chapter 3 Content Specification) is complete: Check that specification exists
- [ ] [T002] [P1] [SETUP] Verify Feature 038 (Chapter 3 MDX Implementation) is complete: Check that chapter-3.mdx exists
- [ ] [T003] [P1] [SETUP] Verify Feature 039 (Chapter 3 AI Blocks Integration) is complete: Check that AI blocks are integrated
- [ ] [T004] [P1] [SETUP] Verify Feature 035 (Chapter 2 RAG Integration) is complete: Check that reference pattern exists
- [ ] [T005] [P1] [SETUP] Verify backend structure exists: Check that backend/app/ directory structure is ready

**Success Criteria**:
- All prerequisite features complete
- Backend structure ready
- Reference pattern available

**Dependencies**: Feature 037, Feature 038, Feature 039, Feature 035 must be complete

---

## PHASE 1 — CHAPTER 3 CHUNKS

**User Story**: US1 - Developer Implements Chapter 3 RAG Scaffolding

**Test Strategy**: Can be tested by verifying chapter_3_chunks.py exists with placeholder functions.

### Create chapter_3_chunks.py

- [ ] [T006] [P1] [CHUNKS] Create `backend/app/content/chapters/chapter_3_chunks.py`: Create new file

- [ ] [T007] [P1] [CHUNKS] Add module docstring to `backend/app/content/chapters/chapter_3_chunks.py`:
  - Add docstring explaining purpose (Chapter 3 content chunks for RAG pipeline)

- [ ] [T008] [P1] [CHUNKS] Add get_chapter_chunks() function to `backend/app/content/chapters/chapter_3_chunks.py`:
  - Function signature: `get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]`
  - Add TODO markers: "# TODO: extract real chunks after content stabilizes"
  - Add TODO markers for chunking implementation
  - Return empty list placeholder: `return []`

- [ ] [T009] [P1] [CHUNKS] Add get_chapter_3_chunks() function to `backend/app/content/chapters/chapter_3_chunks.py`:
  - Function signature: `get_chapter_3_chunks() -> List[str]`
  - Add TODO markers for chunking implementation
  - Return empty list placeholder: `return []`

**Acceptance Test**: chapter_3_chunks.py exists, functions have correct signatures, TODO markers present, imports resolve

---

## PHASE 2 — EMBEDDINGS

**User Story**: US1 - Developer Implements Chapter 3 RAG Scaffolding

**Test Strategy**: Can be tested by verifying embedding_client.py has Chapter 3 TODO comments.

### Update embedding_client.py

- [ ] [T010] [P1] [EMBEDDINGS] Open `backend/app/ai/embeddings/embedding_client.py`: Open file in editor

- [ ] [T011] [P1] [EMBEDDINGS] Add Chapter 3 TODO comments to generate_embedding() in `backend/app/ai/embeddings/embedding_client.py`:
  - Add TODO: "# TODO: Add chapter_id=3 support for Chapter 3"
  - Add TODO: "# TODO: Use CH3_EMBEDDING_MODEL when chapter_id=3"
  - No real logic changes (placeholder only)

**Acceptance Test**: embedding_client.py updated, Chapter 3 TODO comments added, no syntax errors

---

## PHASE 3 — QDRANT COLLECTION

**User Story**: US1 - Developer Implements Chapter 3 RAG Scaffolding

**Test Strategy**: Can be tested by verifying qdrant_store.py has Chapter 3 TODO comments.

### Update qdrant_store.py

- [ ] [T012] [P1] [QDRANT] Open `backend/app/ai/rag/qdrant_store.py`: Open file in editor

- [ ] [T013] [P1] [QDRANT] Add Chapter 3 TODO comment to create_collection() in `backend/app/ai/rag/qdrant_store.py`:
  - Add TODO: "# TODO: For Chapter 3: collection_name = 'chapter_3'"
  - No real logic changes (placeholder only)

- [ ] [T014] [P1] [QDRANT] Add Chapter 3 TODO comment to upsert_vectors() in `backend/app/ai/rag/qdrant_store.py`:
  - Add TODO: "# TODO: For Chapter 3: collection_name = 'chapter_3'"
  - No real logic changes (placeholder only)

**Acceptance Test**: qdrant_store.py updated, Chapter 3 TODO comments added, no syntax errors

---

## PHASE 4 — RAG PIPELINE

**User Story**: US1 - Developer Implements Chapter 3 RAG Scaffolding

**Test Strategy**: Can be tested by verifying pipeline.py has Chapter 3 branch with placeholder flow.

### Update pipeline.py

- [ ] [T015] [P1] [PIPELINE] Open `backend/app/ai/rag/pipeline.py`: Open file in editor

- [ ] [T016] [P1] [PIPELINE] Add Chapter 3 branch to run_rag_pipeline() in `backend/app/ai/rag/pipeline.py`:
  - Add `if chapter_id == 3:` branch
  - Add placeholder flow comments:
    - "# TODO: Step 1: Call get_chapter_chunks(chapter_id=3)"
    - "# TODO: Step 2: Call generate_embedding(query, chapter_id=3)"
    - "# TODO: Step 3: Call similarity_search(collection='chapter_3', query_embedding, top_k)"
    - "# TODO: Step 4: Assemble retrieved chunks into context string"
  - No real logic (placeholder only)

**Acceptance Test**: pipeline.py updated, Chapter 3 branch added, placeholder flow comments present, no syntax errors

---

## PHASE 5 — RUNTIME ENGINE

**User Story**: US1, US2 - Developer Implements Chapter 3 RAG Scaffolding, System Routes Chapter 3 Requests

**Test Strategy**: Can be tested by verifying engine.py has Chapter 3 routing logic.

### Update engine.py

- [ ] [T017] [P1] [RUNTIME] Open `backend/app/ai/runtime/engine.py`: Open file in editor

- [ ] [T018] [P1] [RUNTIME] Add Chapter 3 routing logic to run_ai_block() in `backend/app/ai/runtime/engine.py`:
  - Add `if request_data.get("chapterId") == 3:` branch
  - Add placeholder routing comments:
    - "# TODO: Route to Chapter 3 RAG pipeline"
    - "# TODO: Call Chapter 3 subagents (ch3_ask_agent, ch3_explain_agent, ch3_quiz_agent, ch3_diagram_agent)"
  - No real logic (placeholder only)

**Acceptance Test**: engine.py updated, Chapter 3 routing added, placeholder comments present, no syntax errors

---

## PHASE 6 — API LAYER

**User Story**: US2 - System Routes Chapter 3 AI Block Requests

**Test Strategy**: Can be tested by verifying ai_blocks.py supports chapterId=3.

### Verify ai_blocks.py

- [ ] [T019] [P2] [API] Open `backend/app/api/ai_blocks.py`: Open file in editor

- [ ] [T020] [P2] [API] Verify all endpoints support chapterId=3 in `backend/app/api/ai_blocks.py`:
  - Verify ask-question endpoint accepts chapterId parameter
  - Verify explain-like-10 endpoint accepts chapterId parameter
  - Verify quiz endpoint accepts chapterId parameter
  - Verify diagram endpoint accepts chapterId parameter
  - Add TODO comments if needed

**Acceptance Test**: ai_blocks.py verified, all endpoints support chapterId=3, routing handled by runtime engine

---

## PHASE 7 — CONFIG

**User Story**: US1 - Developer Implements Chapter 3 RAG Scaffolding

**Test Strategy**: Can be tested by verifying settings.py has Chapter 3 config and .env.example is updated.

### Update settings.py and .env.example

- [ ] [T021] [P1] [CONFIG] Verify settings.py has Chapter 3 config: Check that QDRANT_COLLECTION_CH3, CH3_EMBEDDING_MODEL, CH3_LLM_MODEL exist

- [ ] [T022] [P1] [CONFIG] Update `.env.example` with Chapter 3 env vars:
  - Add `QDRANT_COLLECTION_CH3=chapter_3` with description
  - Add `CH3_EMBEDDING_MODEL=` with description (if not present)
  - Add `CH3_LLM_MODEL=` with description (if not present)

**Acceptance Test**: settings.py verified, .env.example updated with Chapter 3 env vars

---

## PHASE 8 — VALIDATION

**User Story**: US1, US2 - Structure and Routing Validation

**Test Strategy**: Can be tested by running backend startup, import tests, and API tests.

### Backend Startup Validation

- [ ] [T023] [P1] [VALIDATION] Run backend startup test: Run `uvicorn app.main:app --reload` in backend directory
- [ ] [T024] [P1] [VALIDATION] Verify backend starts without errors: Check startup logs for errors
- [ ] [T025] [P1] [VALIDATION] Fix any startup errors: Resolve import errors or syntax errors

### Import Validation

- [ ] [T026] [P1] [VALIDATION] Test chapter_3_chunks import: Run `python -c "from app.content.chapters.chapter_3_chunks import get_chapter_chunks; print('Import successful')"`
- [ ] [T027] [P1] [VALIDATION] Test pipeline import: Run `python -c "from app.ai.rag.pipeline import run_rag_pipeline; print('Import successful')"`
- [ ] [T028] [P1] [VALIDATION] Verify all imports resolve: Check for missing module errors

### API Validation

- [ ] [T029] [P2] [VALIDATION] Test API call with chapterId=3: Make POST request to `/api/ai/ask-question` with `{"question": "test", "chapterId": 3}`
- [ ] [T030] [P2] [VALIDATION] Verify API routes to Chapter 3 placeholder logic: Check response (should be placeholder, no errors)

**Acceptance Test**: All validation checks pass (backend starts, imports resolve, API routes correctly)

---

## Summary

**Total Tasks**: 30 tasks across 8 phases
**Estimated Time**: 45-60 minutes (scaffolding only, no real AI logic)
**Complexity**: Low (following existing patterns, placeholder implementation)

**Success Criteria**:
- ✅ Backend runs without errors
- ✅ All Chapter 3 scaffolding files exist
- ✅ No real AI calls or embeddings
- ✅ ai_blocks API recognizes chapterId=3
- ✅ Runtime engine routes to chapter 3 stub
- ✅ Pipeline imports chapter_3_chunks successfully

**Next Steps**: Proceed to `/sp.implement` to execute all tasks in order.

