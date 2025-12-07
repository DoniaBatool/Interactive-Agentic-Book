# Tasks: Chapter 2 — RAG + Embeddings + AI Runtime Integration

**Feature**: 035-ch2-rag-integration | **Branch**: `035-ch2-rag-integration` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for implementing RAG + embedding + runtime integration layer for Chapter 2 (scaffolding only, no real RAG logic).

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), SETUP (Initial setup), VALIDATION (Validation tasks)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before implementing RAG scaffolding for Chapter 2.

- [ ] [T001] [P1] [SETUP] Verify Chapter 2 chunks file exists: Check that `backend/app/content/chapters/chapter_2_chunks.py` exists with placeholder function `get_chapter_chunks()` (from Feature 033)
- [ ] [T002] [P1] [SETUP] Verify Chapter 2 subagents exist: Check that `backend/app/ai/subagents/ch2_ask_agent.py`, `ch2_explain_agent.py`, `ch2_quiz_agent.py`, `ch2_diagram_agent.py` exist (from Feature 034)
- [ ] [P1] [SETUP] Verify runtime engine exists: Check that `backend/app/ai/runtime/engine.py` exists with routing structure (from Feature 005)
- [ ] [T004] [P1] [SETUP] Verify Chapter 2 MDX exists: Check that `frontend/docs/chapters/chapter-2.mdx` exists with content (from Feature 033)
- [ ] [T005] [P1] [SETUP] Verify .env.example exists: Check that `.env.example` file exists in project root
- [ ] [T006] [P1] [SETUP] Verify FastAPI backend is functional: Run `cd backend && python -c "from app.main import app; print('Backend imports OK')"` to confirm server can start without errors

**Success Criteria**:
- All prerequisite files exist
- Backend imports resolve without errors
- No breaking changes to existing functionality

**Dependencies**: Feature 033 (Chapter 2 Content), Feature 034 (Chapter 2 AI Blocks Integration), and Feature 005 (AI Runtime Engine) must be complete

---

## PHASE 1 — Embeddings Layer

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by creating ch2_embedding_client.py with placeholder functions and verifying imports work.

### Create Chapter 2 Embedding Client

- [ ] [T007] [P1] [US1] Create new file `backend/app/ai/embeddings/ch2_embedding_client.py`:
  - Add file header comment: `"""Chapter 2 Embedding Client - Generates embeddings for Mechanical Systems content."""`
  - Add imports: `from typing import List`

- [ ] [T008] [P1] [US1] Add `generate_embedding()` function to `backend/app/ai/embeddings/ch2_embedding_client.py`:
  - Function signature: `def generate_embedding(text: str) -> List[float]:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Select model from ENV (EMBEDDING_MODEL_CH2)`
    - `# TODO: Generate embedding vector`
    - `# TODO: Handle max token size, truncation`
    - `# TODO: Return vector with expected dimensions`
    - `# TODO: Vector dimensional expectations (e.g., 1536 for text-embedding-3-small)`
    - `# TODO: Safety guidelines (max token size, truncation)`
  - Return empty list placeholder: `return []`

- [ ] [T009] [P1] [US1] Add `batch_embed()` function to `backend/app/ai/embeddings/ch2_embedding_client.py`:
  - Function signature: `def batch_embed(chunks: List[str]) -> List[List[float]]:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Process chunks in batches`
    - `# TODO: Use Chapter 2 embedding model (EMBEDDING_MODEL_CH2)`
    - `# TODO: Return list of vectors`
    - `# TODO: Batching plan (e.g., 100 chunks per batch)`
  - Return empty list placeholder: `return []`

- [ ] [T010] [P1] [US1] Verify ch2_embedding_client.py is importable: Run `cd backend && python -c "from app.ai.embeddings.ch2_embedding_client import generate_embedding, batch_embed; print('Import successful')"` - should complete without errors

**Acceptance Test**: Chapter 2 embedding client has generate_embedding() and batch_embed() functions with comprehensive TODO comments, imports work, functions return empty list placeholders

---

## PHASE 2 — Qdrant Store

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by creating ch2_qdrant_store.py with placeholder functions and verifying imports work.

### Create Chapter 2 Qdrant Store

- [ ] [T011] [P1] [US1] Create new file `backend/app/ai/rag/ch2_qdrant_store.py`:
  - Add file header comment: `"""Chapter 2 Qdrant Store - Manages vector database operations for Mechanical Systems content."""`
  - Add imports: `from typing import List, Dict, Any`

- [ ] [T012] [P1] [US1] Add `create_collection()` function to `backend/app/ai/rag/ch2_qdrant_store.py`:
  - Function signature: `def create_collection() -> None:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Create collection "chapter_2" (from QDRANT_COLLECTION_CH2 env var)`
    - `# TODO: Configure vector dimensions`
    - `# TODO: Set distance metric (cosine similarity)`
    - `# TODO: Configure indexing (HNSW)`
    - `# TODO: Collection creation logic`
  - Return None placeholder: `pass`

- [ ] [T013] [P1] [US1] Add `upsert_vectors()` function to `backend/app/ai/rag/ch2_qdrant_store.py`:
  - Function signature: `def upsert_vectors(vectors: List[List[float]], metadata: List[Dict]) -> None:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Upsert vectors to "chapter_2" collection`
    - `# TODO: Include metadata (chapter_id, section_id, position, etc.)`
    - `# TODO: Handle batch upsertion`
    - `# TODO: Vector upsertion logic`
  - Return None placeholder: `pass`

- [ ] [T014] [P1] [US1] Add `similarity_search()` function to `backend/app/ai/rag/ch2_qdrant_store.py`:
  - Function signature: `def similarity_search(query: str, top_k: int = 5) -> List[Dict]:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Embed query using ch2_embedding_client`
    - `# TODO: Search "chapter_2" collection`
    - `# TODO: Return top-k most relevant chunks`
    - `# TODO: Include chunk metadata`
    - `# TODO: Similarity search logic`
  - Return empty list placeholder: `return []`

- [ ] [T015] [P1] [US1] Verify ch2_qdrant_store.py is importable: Run `cd backend && python -c "from app.ai.rag.ch2_qdrant_store import create_collection, upsert_vectors, similarity_search; print('Import successful')"` - should complete without errors

**Acceptance Test**: Chapter 2 Qdrant store has create_collection(), upsert_vectors(), and similarity_search() functions with comprehensive TODO comments, imports work, functions return placeholder values

---

## PHASE 3 — Chunk Source

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by verifying/updating chapter_2_chunks.py with get_chapter_2_chunks() function and verifying imports work.

### Update Chapter 2 Chunks File

- [ ] [T016] [P1] [US1] Verify `get_chapter_chunks()` function exists in `backend/app/content/chapters/chapter_2_chunks.py`:
  - Check function signature: `def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:`
  - Verify function has placeholder return: `return []`

- [ ] [T017] [P1] [US1] Add `get_chapter_2_chunks()` function to `backend/app/content/chapters/chapter_2_chunks.py` (if not exists):
  - Function signature: `def get_chapter_2_chunks() -> List[str]:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Load Chapter 2 content from MDX file`
    - `# TODO: Implement chunking strategy (syntactic, semantic, hybrid)`
    - `# TODO: Extract metadata (section titles, positions, word counts)`
    - `# TODO: Generate unique chunk IDs`
    - `# TODO: Handle special content (glossary, diagrams, AI blocks)`
    - `# TODO: No real chunking logic`
  - Return empty list placeholder: `return []`

- [ ] [T018] [P1] [US1] Verify chapter_2_chunks.py is importable after updates: Run `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks, get_chapter_2_chunks; print('Import successful')"` - should complete without errors

**Acceptance Test**: Chapter 2 chunks file has get_chapter_2_chunks() function with comprehensive TODO comments, imports work, function returns empty list placeholder

---

## PHASE 4 — RAG Pipeline

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by creating ch2_pipeline.py with 5-step flow comments and verifying imports work.

### Create Chapter 2 RAG Pipeline File

- [ ] [T019] [P1] [US1] Create new file `backend/app/ai/rag/ch2_pipeline.py`:
  - Add file header comment: `"""Chapter 2 RAG Pipeline Orchestration - Orchestrates retrieval, embedding, search, and context assembly for Mechanical Systems."""`
  - Add imports: `from typing import Dict, Any, List`

- [ ] [T020] [P1] [US1] Add `run_ch2_rag_pipeline()` function to `backend/app/ai/rag/ch2_pipeline.py`:
  - Function signature: `async def run_ch2_rag_pipeline(query: str, top_k: int = 5) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Function description
    - Args documentation (query, top_k)
    - Returns documentation (context, chunks, query_embedding)
    - Pipeline Steps section with 5 steps:
      1. Load chapter chunks
      2. Embed query
      3. Search Qdrant
      4. Prepare context
      5. Pass into AI runtime

- [ ] [T021] [P1] [US1] Add TODO comments for each pipeline step in `run_ch2_rag_pipeline()` function body in `backend/app/ai/rag/ch2_pipeline.py`:
  - Step 1 TODOs:
    - `# TODO: Step 1: Load chapter chunks`
    - `# TODO:     from app.content.chapters.chapter_2_chunks import get_chapter_2_chunks`
    - `# TODO:     chunks = get_chapter_2_chunks()`
  - Step 2 TODOs:
    - `# TODO: Step 2: Embed query`
    - `# TODO:     from app.ai.embeddings.ch2_embedding_client import generate_embedding`
    - `# TODO:     query_embedding = generate_embedding(query)`
  - Step 3 TODOs:
    - `# TODO: Step 3: Search Qdrant`
    - `# TODO:     from app.ai.rag.ch2_qdrant_store import similarity_search`
    - `# TODO:     results = similarity_search(query, top_k)`
  - Step 4 TODOs:
    - `# TODO: Step 4: Prepare context`
    - `# TODO:     context = assemble_context_string(results)`
  - Step 5 TODOs:
    - `# TODO: Step 5: Pass into AI runtime`
    - `# TODO:     return context dictionary`

- [ ] [T022] [P1] [US1] Add placeholder return to `run_ch2_rag_pipeline()` function in `backend/app/ai/rag/ch2_pipeline.py`:
  - Return empty dict placeholder: `return {"context": "", "chunks": [], "query_embedding": []}`

- [ ] [T023] [P1] [US1] Verify ch2_pipeline.py is importable: Run `cd backend && python -c "from app.ai.rag.ch2_pipeline import run_ch2_rag_pipeline; print('Import successful')"` - should complete without errors

**Acceptance Test**: Chapter 2 RAG pipeline has run_ch2_rag_pipeline() function with 5-step flow comments, comprehensive TODO comments, imports work, function returns empty dict placeholder

---

## PHASE 5 — Runtime Integration

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by updating engine.py with Chapter 2 routing comments and verifying imports work.

### Update Runtime Engine Routing

- [ ] [T024] [P1] [US1] Update `backend/app/ai/runtime/engine.py` to add Chapter 2 routing to ch2_pipeline:
  - Locate existing Chapter 2 routing section (from Feature 034)
  - Add TODO comment: `# TODO: When chapterId=2, call run_ch2_rag_pipeline()`
  - Add TODO comment: `# TODO:     from app.ai.rag.ch2_pipeline import run_ch2_rag_pipeline`
  - Add TODO comment: `# TODO:     context = await run_ch2_rag_pipeline(query, top_k)`
  - Add TODO comment: `# TODO: Pass context to Chapter 2 subagents`
  - Add TODO comment: `# TODO: Routing rules: chapter="2" → use ch2_pipeline`

- [ ] [T025] [P1] [US1] Verify engine.py is importable after updates: Run `cd backend && python -c "from app.ai.runtime.engine import run_ai_block; print('Import successful')"` - should complete without errors

**Acceptance Test**: Runtime engine has Chapter 2 routing comments explaining routing rules, imports work, existing routing remains unchanged

---

## PHASE 6 — Subagents Verification

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by verifying subagent files exist and have placeholder run() signatures.

### Verify Chapter 2 Subagents

- [ ] [T026] [P1] [US1] Verify `backend/app/ai/subagents/ch2_ask_agent.py` exists:
  - Check file exists
  - Check has Ch2AskAgent class with run() method
  - Check has TODO comments

- [ ] [T027] [P1] [US1] Verify `backend/app/ai/subagents/ch2_explain_agent.py` exists:
  - Check file exists
  - Check has Ch2ExplainAgent class with run() method
  - Check has TODO comments

- [ ] [T028] [P1] [US1] Verify `backend/app/ai/subagents/ch2_quiz_agent.py` exists:
  - Check file exists
  - Check has Ch2QuizAgent class with run() method
  - Check has TODO comments

- [ ] [T029] [P1] [US1] Verify `backend/app/ai/subagents/ch2_diagram_agent.py` exists:
  - Check file exists
  - Check has Ch2DiagramAgent class with run() method
  - Check has TODO comments

- [ ] [T030] [P1] [US1] Verify all Chapter 2 subagents are importable: Run `cd backend && python -c "from app.ai.subagents.ch2_ask_agent import Ch2AskAgent; from app.ai.subagents.ch2_explain_agent import Ch2ExplainAgent; from app.ai.subagents.ch2_quiz_agent import Ch2QuizAgent; from app.ai.subagents.ch2_diagram_agent import Ch2DiagramAgent; print('All subagents importable')"` - should complete without errors

**Acceptance Test**: All Chapter 2 subagents exist with placeholder run() signatures and TODO comments, imports work

---

## PHASE 7 — Environment Variables

**User Story**: US2 - System Administrator Configures Chapter 2 RAG Settings

**Test Strategy**: Can be tested by updating .env.example with Chapter 2 variables and verifying format.

### Update Environment Variables

- [ ] [T031] [P1] [US2] Add `EMBEDDING_MODEL_CH2=""` to `.env.example`:
  - Add variable with description: `# Embedding model for Chapter 2 (e.g., "text-embedding-3-small")`
  - Add placeholder value: `EMBEDDING_MODEL_CH2=""`

- [ ] [T032] [P1] [US2] Add `QDRANT_COLLECTION_CH2=""` to `.env.example`:
  - Add variable with description: `# Qdrant collection name for Chapter 2 (e.g., "chapter_2")`
  - Add placeholder value: `QDRANT_COLLECTION_CH2=""`

- [ ] [T033] [P1] [US2] Verify .env.example is readable: Check file exists and variables are properly formatted

**Acceptance Test**: .env.example has EMBEDDING_MODEL_CH2 and QDRANT_COLLECTION_CH2 variables with descriptions and placeholder values

---

## PHASE 8 — Contract File

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by verifying contract file exists and documents RAG flow.

### Verify Contract File

- [ ] [T034] [P1] [US1] Verify `specs/035-ch2-rag-integration/contracts/rag-flow.yaml` exists:
  - Check file exists (already created in spec phase)
  - Verify documents high-level RAG flow
  - Verify documents 5-step pipeline

**Acceptance Test**: Contract file exists and documents RAG flow with high-level description

---

## PHASE 9 — Validation

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by verifying all files exist, imports work, and backend starts.

### Final Validation

- [ ] [T035] [P1] [US1] Verify all files exist:
  - Check: `backend/app/ai/embeddings/ch2_embedding_client.py` (exists)
  - Check: `backend/app/ai/rag/ch2_qdrant_store.py` (exists)
  - Check: `backend/app/ai/rag/ch2_pipeline.py` (exists)
  - Check: `backend/app/content/chapters/chapter_2_chunks.py` (updated)
  - Check: `backend/app/ai/runtime/engine.py` (updated)
  - Check: `.env.example` (updated)

- [ ] [T036] [P1] [US1] Verify backend starts without errors:
  - Run: `cd backend && python -c "from app.main import app; print('Backend starts OK')"`
  - Expected: No import errors or runtime exceptions

- [ ] [T037] [P1] [US1] Verify all imports resolve:
  - Test ch2_embedding_client imports
  - Test ch2_qdrant_store imports
  - Test ch2_pipeline imports
  - Test chapter_2_chunks imports
  - Test engine imports

**Acceptance Test**: All files exist, backend starts without errors, all imports resolve successfully

---

## Summary

**Total Tasks**: 37 tasks across 9 phases
**Estimated Time**: 1-2 hours (scaffolding only, no business logic)
**Complexity**: Low (scaffolding, following existing patterns)

**Success Criteria**:
- ✅ All ch2 pipeline files exist and import correctly
- ✅ No business logic implemented; placeholders only
- ✅ Chapter 2 AI blocks route through ch2_pipeline
- ✅ Embedding, Qdrant, Subagents folders updated
- ✅ .env.example updated with CH2 vars
- ✅ Backend boots without errors
- ✅ Contract file exists and documents RAG flow

**Next Steps**: Proceed to `/sp.implement` to execute all tasks in order.

