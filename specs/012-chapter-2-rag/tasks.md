# Tasks: Chapter 2 — RAG Chunking, Embeddings & Qdrant Collection Setup

**Feature**: 012-chapter-2-rag | **Branch**: `012-chapter-2-rag` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for building RAG foundations for Chapter 2 (scaffolding only, no real RAG logic).

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), SETUP (Initial setup), POLISH (Final touches)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before implementing RAG scaffolding for Chapter 2.

- [ ] [T001] [P1] [SETUP] Verify Chapter 2 chunks file exists: Check that `backend/app/content/chapters/chapter_2_chunks.py` exists with placeholder function `get_chapter_chunks()` (from Feature 011)
- [ ] [T002] [P1] [SETUP] Verify embedding client exists: Check that `backend/app/ai/embeddings/embedding_client.py` exists with placeholder functions `generate_embedding()` and `batch_embed()` (from Feature 005)
- [ ] [T003] [P1] [SETUP] Verify Qdrant store exists: Check that `backend/app/ai/rag/qdrant_store.py` exists with placeholder functions `create_collection()`, `upsert_vectors()`, and `similarity_search()` (from Feature 005)
- [ ] [T004] [P1] [SETUP] Verify RAG pipeline exists: Check that `backend/app/ai/rag/pipeline.py` exists with placeholder function `run_rag_pipeline()` (from Feature 005)
- [ ] [T005] [P1] [SETUP] Verify runtime engine exists: Check that `backend/app/ai/runtime/engine.py` exists with Chapter 2 knowledge source mapping (from Feature 011)
- [ ] [T006] [P1] [SETUP] Verify FastAPI backend is functional: Run `cd backend && python -c "from app.main import app; print('Backend imports OK')"` to confirm server can start without errors
- [ ] [T007] [P1] [SETUP] Verify .env.example exists: Check that `.env.example` file exists in project root

**Success Criteria**:
- All prerequisite files exist
- Backend imports resolve without errors
- No breaking changes to existing functionality

**Dependencies**: Feature 005 (AI Runtime Engine) and Feature 011 (Chapter 2 AI Blocks) must be complete

---

## PHASE 1 — Chunking Scaffolding

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by updating chapter_2_chunks.py with TODO comments and verifying imports still work.

### Update Chapter 2 Chunks File

- [ ] [T008] [P1] [US1] Update `backend/app/content/chapters/chapter_2_chunks.py` function docstring with comprehensive chunking TODO comments:
  - Add TODO: `# TODO: Implement chunking from Chapter 2 MDX content`
  - Add TODO: `# TODO: Load Chapter 2 content from frontend/docs/chapters/chapter-2.mdx`
  - Add TODO: `# TODO: Implement chunking strategy:`
  - Add TODO: `#   - Max token size constraints (e.g., 512 tokens per chunk)`
  - Add TODO: `#   - Semantic segmentation by section`
  - Add TODO: `#   - Heading-aware slicing (respect H2 boundaries)`
  - Add TODO: `#   - Overlapping window strategy (e.g., 50 tokens overlap)`
  - Add TODO: `# TODO: Extract metadata (section titles, positions, word counts)`
  - Add TODO: `# TODO: Generate unique chunk IDs (format: "ch2-s{section}-c{chunk}")`
  - Add TODO: `# TODO: Handle special content (glossary, diagrams, AI blocks)`
  - Add TODO: `# TODO: Cache chunks for performance`
  - Add TODO: `# TODO: Include ROS 2-specific metadata (concepts: nodes, topics, services, actions)`

- [ ] [T009] [P1] [US1] Verify chapter_2_chunks.py is importable after updates: Run `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; print('Import successful')"` - should complete without errors

- [ ] [T010] [P1] [US1] Verify function returns placeholder: Run `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; chunks = get_chapter_chunks(2); assert chunks == [], 'Should return empty list'; print('Placeholder return verified')"` - should complete without errors

**Acceptance Test**: Chapter 2 chunks file has comprehensive TODO comments for chunking rules, imports work, function returns empty list placeholder

---

## PHASE 2 — Embeddings Scaffold

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by verifying embedding_client.py has placeholder functions with TODO comments.

### Verify and Update Embedding Client

- [ ] [T011] [P1] [US1] Verify `generate_embedding()` function exists in `backend/app/ai/embeddings/embedding_client.py`:
  - Function signature: `def generate_embedding(text: str) -> List[float]:`
  - Has TODO comments for future implementation
  - Returns empty list placeholder: `return []`

- [ ] [T012] [P1] [US1] Add Chapter 2-specific TODO comments to `generate_embedding()` docstring in `backend/app/ai/embeddings/embedding_client.py`:
  - Add TODO: `# TODO: Use settings.embedding_model for model selection (default: "text-embedding-3-small")`
  - Add TODO: `# TODO: Return 1536-dimensional vector for text-embedding-3-small`
  - Add TODO: `# TODO: Handle max token size (8191 for text-embedding-3-small)`
  - Add TODO: `# TODO: Truncate text if exceeds max tokens`

- [ ] [T013] [P1] [US1] Verify `batch_embed()` function exists in `backend/app/ai/embeddings/embedding_client.py`:
  - Function signature: `def batch_embed(chunks: List[str]) -> List[List[float]]:`
  - Has TODO comments for future implementation
  - Returns empty list placeholder: `return []`

- [ ] [T014] [P1] [US1] Add Chapter 2-specific TODO comments to `batch_embed()` docstring in `backend/app/ai/embeddings/embedding_client.py`:
  - Add TODO: `# TODO: Handle large batches (split if needed, e.g., 100 chunks per batch)`
  - Add TODO: `# TODO: Add progress tracking for large batches`
  - Add TODO: `# TODO: Return list of 1536-dimensional vectors`

- [ ] [T015] [P1] [US1] Verify embedding_client.py is importable: Run `cd backend && python -c "from app.ai.embeddings.embedding_client import generate_embedding, batch_embed; print('Import successful')"` - should complete without errors

**Acceptance Test**: Embedding client has placeholder functions with comprehensive TODO comments, imports work, functions return empty list placeholders

---

## PHASE 3 — Qdrant Scaffold

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by verifying qdrant_store.py has placeholder functions with Chapter 2 collection TODOs.

### Verify and Update Qdrant Store

- [ ] [T016] [P1] [US1] Verify `create_collection()` function exists in `backend/app/ai/rag/qdrant_store.py`:
  - Function signature: `def create_collection(collection_name: str) -> bool:`
  - Has TODO comments for future implementation
  - Returns False placeholder: `return False`

- [ ] [T017] [P1] [US1] Add Chapter 2 collection-specific TODO comments to `create_collection()` docstring in `backend/app/ai/rag/qdrant_store.py`:
  - Add TODO: `# TODO: For Chapter 2: collection_name = "chapter_2" (from QDRANT_COLLECTION_CH2 env var)`
  - Add TODO: `# TODO: Configure collection with appropriate vector size (1536 for text-embedding-3-small)`
  - Add TODO: `# TODO: Set distance metric to Cosine similarity`
  - Add TODO: `# TODO: Configure HNSW index (m, ef_construct parameters)`

- [ ] [T018] [P1] [US1] Verify `upsert_vectors()` function exists in `backend/app/ai/rag/qdrant_store.py`:
  - Function signature: `def upsert_vectors(collection_name: str, vectors: List[Dict[str, Any]]) -> bool:`
  - Has TODO comments for future implementation
  - Returns False placeholder: `return False`

- [ ] [T019] [P1] [US1] Add Chapter 2 collection-specific TODO comments to `upsert_vectors()` docstring in `backend/app/ai/rag/qdrant_store.py`:
  - Add TODO: `# TODO: For Chapter 2: collection_name = "chapter_2"`
  - Add TODO: `# TODO: Vector structure: {id, vector (1536 dims), payload (metadata)}`
  - Add TODO: `# TODO: Payload metadata: {text, chapter_id, section_id, position, word_count, metadata}`

- [ ] [T020] [P1] [US1] Verify `similarity_search()` function exists in `backend/app/ai/rag/qdrant_store.py`:
  - Function signature: `def similarity_search(collection_name: str, query: str, top_k: int = 5) -> List[Dict[str, Any]]:`
  - Has TODO comments for future implementation
  - Returns empty list placeholder: `return []`

- [ ] [T021] [P1] [US1] Add Chapter 2 collection-specific TODO comments to `similarity_search()` docstring in `backend/app/ai/rag/qdrant_store.py`:
  - Add TODO: `# TODO: For Chapter 2: collection_name = "chapter_2"`
  - Add TODO: `# TODO: Return top_k results sorted by similarity score`

- [ ] [T022] [P1] [US1] Verify qdrant_store.py is importable: Run `cd backend && python -c "from app.ai.rag.qdrant_store import create_collection, upsert_vectors, similarity_search; print('Import successful')"` - should complete without errors

**Acceptance Test**: Qdrant store has placeholder functions with Chapter 2 collection-specific TODO comments, imports work, functions return placeholder values

---

## PHASE 4 — RAG Pipeline Integration

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by updating pipeline.py with Chapter 2 flow comments and verifying imports still work.

### Update RAG Pipeline with Chapter 2 Flow

- [ ] [T023] [P1] [US1] Add Chapter 2-specific flow comments to `run_rag_pipeline()` function in `backend/app/ai/rag/pipeline.py`:
  - Add comment block: `# TODO: Chapter 2 specific flow (when chapter_id=2):`
  - Add comment: `#   - Step 1: Call get_chapter_chunks(chapter_id=2) to retrieve Chapter 2 chunks`
  - Add comment: `#   - Step 2: Call generate_embedding(query) to embed user query`
  - Add comment: `#   - Step 3: Call similarity_search(collection="chapter_2", query_embedding, top_k) to find relevant chunks`
  - Add comment: `#   - Step 4: Assemble retrieved chunks into context string with metadata`
  - Add comment: `#   - Step 5: Return context to runtime engine for LLM prompts`

- [ ] [T024] [P1] [US1] Add placeholder code comments in `run_rag_pipeline()` function body in `backend/app/ai/rag/pipeline.py`:
  - Add commented code: `# if chapter_id == 2:`
  - Add commented code: `#     from app.content.chapters.chapter_2_chunks import get_chapter_chunks`
  - Add commented code: `#     chunks = get_chapter_chunks(chapter_id=2)`
  - Add commented code: `# query_embedding = generate_embedding(query)`
  - Add commented code: `# if chapter_id == 2:`
  - Add commented code: `#     results = similarity_search(collection_name="chapter_2", query_embedding, top_k)`
  - Add commented code: `# context = assemble_context(results, max_chunks=RAG_MAX_CONTEXT)`
  - Add commented code: `# return {"context": context, "chunks": results, "query_embedding": query_embedding}`

- [ ] [T025] [P1] [US1] Add additional TODO comments to `run_rag_pipeline()` docstring in `backend/app/ai/rag/pipeline.py`:
  - Add TODO: `# TODO: Filter chunks by section_id when sectionId provided in request`
  - Add TODO: `# TODO: Limit context size (use RAG_MAX_CONTEXT env var, default: 4 chunks)`

- [ ] [T026] [P1] [US1] Verify pipeline.py is importable after updates: Run `cd backend && python -c "from app.ai.rag.pipeline import run_rag_pipeline; print('Import successful')"` - should complete without errors

**Acceptance Test**: RAG pipeline has Chapter 2 flow comments, placeholder code comments, and additional TODOs, imports work

---

## PHASE 5 — Runtime Engine Integration

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Can be tested by adding RAG integration comments to engine.py and verifying imports still work.

### Update Runtime Engine with RAG Integration Comments

- [ ] [T027] [P1] [US1] Verify Chapter 2 knowledge source mapping exists in `backend/app/ai/runtime/engine.py`:
  - Check that `knowledge_sources` dictionary contains: `2: "chapter_2_chunks"`
  - Check that TODO comment block for Chapter 2 RAG Integration exists

- [ ] [T028] [P1] [US1] Add RAG pipeline integration comments to `backend/app/ai/runtime/engine.py` after existing Chapter 2 TODO block:
  - Add comment block: `# RAG Pipeline Integration Flow:`
  - Add comment: `#   1. Runtime engine calls run_rag_pipeline(query, chapter_id=2, top_k=5)`
  - Add comment: `#   2. RAG pipeline returns context: {context: str, chunks: List, query_embedding: List}`
  - Add comment: `#   3. Runtime engine passes context to subagent along with request_data`
  - Add comment: `#   4. Subagent uses context in LLM prompt for generating response`
  - Add comment: `#   5. LLM provider generates response with ROS 2 context`

- [ ] [T029] [P1] [US1] Add placeholder code comments in `run_ai_block()` function in `backend/app/ai/runtime/engine.py` (if not already present):
  - Add commented code: `# context = await run_rag_pipeline(query, chapter_id)`
  - Add commented code: `# if chapter_id == 2:`
  - Add commented code: `#     from app.content.chapters.chapter_2_chunks import get_chapter_chunks`
  - Add commented code: `#     chunks = get_chapter_chunks(chapter_id=2)`
  - Add commented code: `#     # Use chunks for RAG retrieval`
  - Add commented code: `#     # Pass to subagent with Chapter 2 context`

- [ ] [T030] [P1] [US1] Verify runtime engine is importable after updates: Run `cd backend && python -c "from app.ai.runtime.engine import run_ai_block, knowledge_sources; assert 2 in knowledge_sources; print('Import successful')"` - should complete without errors

**Acceptance Test**: Runtime engine has RAG integration comments, Chapter 2 mapping verified, imports work

---

## PHASE 6 — Environment Updates

**User Story**: US2 - System Administrator Configures Chapter 2 RAG Settings

**Test Strategy**: Can be tested by updating .env.example and verifying variables are documented.

### Update Environment Variables

- [ ] [T031] [P2] [US2] Add Chapter 2 RAG environment variables to `.env.example`:
  - Add comment: `# Chapter 2 RAG Configuration`
  - Add variable: `QDRANT_COLLECTION_CH2="chapter_2"` with description: `# Qdrant collection name for Chapter 2`
  - Add variable: `EMBEDDING_MODEL="text-embedding-3-small"` with description: `# Embedding model name (OpenAI)`
  - Add variable: `RAG_MAX_CONTEXT=4` with description: `# Maximum number of chunks in context`

- [ ] [T032] [P2] [US2] Verify .env.example file is readable: Check that file exists and new variables are properly formatted

- [ ] [T033] [P3] [US2] (Optional) Verify settings.py can read new env vars: Check that `backend/app/config/settings.py` uses environment variables (no changes needed if it already reads from os.environ)

**Acceptance Test**: .env.example has 3 new environment variables with clear descriptions, file is properly formatted

---

## PHASE 7 — Contracts

**User Story**: US1 - Developer Sets Up Chapter 2 RAG Infrastructure

**Test Strategy**: Contracts already created in specification phase, verify they exist.

### Verify Contract Files

- [ ] [T034] [P1] [US1] Verify `specs/012-chapter-2-rag/contracts/rag-pipeline.yaml` exists:
  - Check that file contains RAG pipeline contract
  - Check that 5-step pipeline flow is documented
  - Check that Chapter 2-specific considerations are included

- [ ] [T035] [P1] [US1] Verify `specs/012-chapter-2-rag/contracts/ch2-schema.yaml` exists:
  - Check that file contains Chapter 2 schema contract
  - Check that chunk schema, vector schema, and metadata schema are documented
  - Check that Qdrant collection schema for Chapter 2 is included

**Acceptance Test**: Both contract files exist and contain required documentation (already created in spec phase)

---

## Phase 8: Validation & Testing

**Purpose**: Final validation to ensure all scaffolding is in place and backend starts successfully.

### Backend Validation

- [ ] [T036] [P1] [POLISH] Verify all imports resolve: Run `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; from app.ai.embeddings.embedding_client import generate_embedding, batch_embed; from app.ai.rag.qdrant_store import create_collection, upsert_vectors, similarity_search; from app.ai.rag.pipeline import run_rag_pipeline; from app.ai.runtime.engine import run_ai_block; print('All imports successful')"` - should complete without errors

- [ ] [T037] [P1] [POLISH] Verify backend starts successfully: Run `cd backend && python -c "from app.main import app; print('Backend startup OK')"` - should complete without errors

- [ ] [T038] [P1] [POLISH] Verify no syntax errors: Run `cd backend && python -m py_compile app/content/chapters/chapter_2_chunks.py app/ai/embeddings/embedding_client.py app/ai/rag/qdrant_store.py app/ai/rag/pipeline.py app/ai/runtime/engine.py` - should complete without errors

### File Existence Validation

- [ ] [T039] [P1] [POLISH] Verify all updated files exist:
  - `backend/app/content/chapters/chapter_2_chunks.py` (updated with TODOs)
  - `backend/app/ai/embeddings/embedding_client.py` (updated with TODOs)
  - `backend/app/ai/rag/qdrant_store.py` (updated with TODOs)
  - `backend/app/ai/rag/pipeline.py` (updated with Chapter 2 flow)
  - `backend/app/ai/runtime/engine.py` (updated with RAG integration comments)
  - `.env.example` (updated with 3 new env vars)

### TODO Validation

- [ ] [T040] [P1] [POLISH] Verify all functions have TODO comments:
  - `get_chapter_chunks()` has chunking TODO comments
  - `generate_embedding()` has embedding TODO comments
  - `batch_embed()` has batching TODO comments
  - `create_collection()` has Chapter 2 collection TODO comments
  - `upsert_vectors()` has Chapter 2 vector TODO comments
  - `similarity_search()` has Chapter 2 search TODO comments
  - `run_rag_pipeline()` has Chapter 2 flow comments
  - `run_ai_block()` has RAG integration comments

**Acceptance Test**: 
- All imports resolve without errors
- Backend starts successfully
- All files exist and are updated
- All functions have appropriate TODO comments
- No real RAG logic implemented (only placeholders)

---

## Summary

**Total Tasks**: 40 tasks across 8 phases
- Phase 0 (Setup): 7 tasks
- Phase 1 (Chunking): 3 tasks
- Phase 2 (Embeddings): 5 tasks
- Phase 3 (Qdrant): 7 tasks
- Phase 4 (Pipeline): 4 tasks
- Phase 5 (Runtime): 4 tasks
- Phase 6 (Environment): 3 tasks
- Phase 7 (Contracts): 2 tasks (already done)
- Phase 8 (Validation): 5 tasks

**Estimated Effort**: ~2-3 hours (mostly adding TODO comments and verifying imports)

**Dependencies**: Feature 005 (AI Runtime Engine) and Feature 011 (Chapter 2 AI Blocks) must be complete

**Next Step**: Run `/sp.implement` to execute these tasks
