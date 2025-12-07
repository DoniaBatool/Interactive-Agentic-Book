# Tasks: Chapter 3 — RAG + Embedding Preparation Layer

**Feature**: 029-ch3-rag-prep | **Branch**: `029-ch3-rag-prep` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for building RAG foundations for Chapter 3 (scaffolding only, no real RAG logic).

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

**Purpose**: Verify dependencies and prerequisites before implementing RAG scaffolding for Chapter 3.

- [ ] [T001] [P1] [SETUP] Verify Chapter 3 chunks file exists: Check that `backend/app/content/chapters/chapter_3_chunks.py` exists with placeholder function `get_chapter_chunks()` (from Feature 028)
- [ ] [T002] [P1] [SETUP] Verify embedding client exists: Check that `backend/app/ai/embeddings/embedding_client.py` exists with placeholder functions (from Feature 005)
- [ ] [T003] [P1] [SETUP] Verify Qdrant store exists: Check that `backend/app/ai/rag/qdrant_store.py` exists with placeholder functions `create_collection()`, `upsert_vectors()`, and `similarity_search()` (from Feature 005)
- [ ] [T004] [P1] [SETUP] Verify Chapter 3 MDX exists: Check that `frontend/docs/chapters/chapter-3.mdx` exists with content and AI blocks (from Feature 028)
- [ ] [T005] [P1] [SETUP] Verify settings.py exists: Check that `backend/app/config/settings.py` exists with Settings class (from Feature 005)
- [ ] [T006] [P1] [SETUP] Verify FastAPI backend is functional: Run `cd backend && python -c "from app.main import app; print('Backend imports OK')"` to confirm server can start without errors
- [ ] [T007] [P1] [SETUP] Verify .env.example exists or create it: Check that `.env.example` file exists in project root, create if missing

**Success Criteria**:
- All prerequisite files exist
- Backend imports resolve without errors
- No breaking changes to existing functionality

**Dependencies**: Feature 028 (Chapter 3 AI Blocks Integration) and Feature 005 (AI Runtime Engine) must be complete

---

## PHASE 1 — Chunking Scaffolding

**User Story**: US1 - Developer Sets Up Chapter 3 RAG Infrastructure

**Test Strategy**: Can be tested by updating chapter_3_chunks.py with CH3_CHUNKS constant and TODO comments and verifying imports still work.

### Update Chapter 3 Chunks File

- [ ] [T008] [P1] [US1] Add placeholder constant `CH3_CHUNKS = []` to `backend/app/content/chapters/chapter_3_chunks.py`:
  - Add constant at module level: `CH3_CHUNKS = []  # TODO: Populate with Chapter 3 chunks`
  - Add comment explaining placeholder nature

- [ ] [T009] [P1] [US1] Update `get_chapter_chunks()` function in `backend/app/content/chapters/chapter_3_chunks.py` to return CH3_CHUNKS:
  - Change return statement from `return []` to `return CH3_CHUNKS`
  - Update docstring to reference CH3_CHUNKS constant

- [ ] [T010] [P1] [US1] Update `get_chapter_chunks()` function docstring in `backend/app/content/chapters/chapter_3_chunks.py` with comprehensive chunking TODO comments:
  - Add TODO: `# TODO: Implement chunking from Chapter 3 MDX content`
  - Add TODO: `# TODO: Load Chapter 3 content from frontend/docs/chapters/chapter-3.mdx`
  - Add TODO: `# TODO: Implement chunking strategy:`
  - Add TODO: `#   - Respect chunk markers (CHUNK: START / CHUNK: END)`
  - Add TODO: `#   - Respect RAG-CHUNK markers (<!-- RAG-CHUNK: start --> / <!-- RAG-CHUNK: end -->)`
  - Add TODO: `#   - Section-based logical chunks (each H2 section is a natural chunk boundary)`
  - Add TODO: `#   - Semantic segmentation by section`
  - Add TODO: `#   - Heading-aware slicing (respect H2 boundaries)`
  - Add TODO: `#   - Max token size constraints (e.g., 512 tokens per chunk)`
  - Add TODO: `#   - Overlapping window strategy (e.g., 50 tokens overlap)`
  - Add TODO: `# TODO: Extract metadata (section titles, positions, word counts)`
  - Add TODO: `# TODO: Generate unique chunk IDs (format: "ch3-s{section}-c{chunk}")`
  - Add TODO: `# TODO: Handle special content (glossary, diagrams, AI blocks)`
  - Add TODO: `# TODO: Include Physical AI-specific metadata (concepts: perception, sensors, vision, signal processing)`
  - Add TODO: `# TODO: Include chunk marker metadata (chunk_markers: bool flag)`

- [ ] [T011] [P1] [US1] Verify chapter_3_chunks.py is importable after updates: Run `cd backend && python -c "from app.content.chapters.chapter_3_chunks import get_chapter_chunks, CH3_CHUNKS; print('Import successful')"` - should complete without errors

- [ ] [T012] [P1] [US1] Verify function returns placeholder: Run `cd backend && python -c "from app.content.chapters.chapter_3_chunks import get_chapter_chunks, CH3_CHUNKS; chunks = get_chapter_chunks(3); assert chunks == CH3_CHUNKS == [], 'Should return empty list'; print('Placeholder return verified')"` - should complete without errors

**Acceptance Test**: Chapter 3 chunks file has CH3_CHUNKS constant, comprehensive TODO comments for chunking rules (including RAG-CHUNK markers), imports work, function returns empty list placeholder

---

## PHASE 2 — Embeddings Scaffold

**User Story**: US1 - Developer Sets Up Chapter 3 RAG Infrastructure

**Test Strategy**: Can be tested by adding Chapter 3 embedding functions to embedding_client.py and verifying imports work.

### Add Chapter 3 Embedding Functions

- [ ] [T013] [P1] [US1] Add `embed_chapter3_chunks()` function to `backend/app/ai/embeddings/embedding_client.py`:
  - Function signature: `def embed_chapter3_chunks(chunks: List[str]) -> List[List[float]]:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Implement batch embedding for Chapter 3 chunks`
    - `# TODO: Use CH3_EMBEDDING_MODEL for Chapter 3`
    - `# TODO: Use settings.ch3_embedding_model for model selection`
    - `# TODO: Use batch API endpoint for efficiency`
    - `# TODO: Handle large batches (split if needed, e.g., 100 chunks per batch)`
    - `# TODO: Add progress tracking for large batches`
    - `# TODO: Add error handling for partial failures`
    - `# TODO: Return list of 1536-dimensional vectors`
  - Return empty list placeholder: `return []`

- [ ] [T014] [P1] [US1] Add `normalize_chapter3_embeddings()` function to `backend/app/ai/embeddings/embedding_client.py`:
  - Function signature: `def normalize_chapter3_embeddings(embeddings: List[List[float]]) -> List[List[float]]:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Implement normalization for Chapter 3 embeddings`
    - `# TODO: Optional L2 normalization`
    - `# TODO: Return normalized embeddings`
    - `# TODO: Handle empty embeddings list`
    - `# TODO: Add error handling for invalid embeddings`
  - Return empty list placeholder: `return []`

- [ ] [T015] [P1] [US1] Verify embedding_client.py is importable after updates: Run `cd backend && python -c "from app.ai.embeddings.embedding_client import embed_chapter3_chunks, normalize_chapter3_embeddings; print('Import successful')"` - should complete without errors

**Acceptance Test**: Embedding client has embed_chapter3_chunks() and normalize_chapter3_embeddings() functions with comprehensive TODO comments, imports work, functions return empty list placeholders

---

## PHASE 3 — Qdrant Scaffold

**User Story**: US1 - Developer Sets Up Chapter 3 RAG Infrastructure

**Test Strategy**: Can be tested by adding Chapter 3 TODOs and similarity_search_ch3() function to qdrant_store.py and verifying imports work.

### Update Qdrant Store with Chapter 3 Support

- [ ] [T016] [P1] [US1] Add Chapter 3 collection-specific TODO comments to `create_collection()` docstring in `backend/app/ai/rag/qdrant_store.py`:
  - Add TODO: `# TODO: For Chapter 3: collection_name = "chapter3" (from QDRANT_COLLECTION_CH3 env var)`
  - Add TODO: `# TODO: Configure collection with appropriate vector size (1536 for text-embedding-3-small)`
  - Add TODO: `# TODO: Set distance metric to Cosine similarity`
  - Add TODO: `# TODO: Configure HNSW index (m, ef_construct parameters)`

- [ ] [T017] [P1] [US1] Add Chapter 3 collection-specific TODO comments to `upsert_vectors()` docstring in `backend/app/ai/rag/qdrant_store.py`:
  - Add TODO: `# TODO: For Chapter 3: collection_name = "chapter3"`
  - Add TODO: `# TODO: Vector structure: {id, vector (1536 dims), payload (metadata)}`
  - Add TODO: `# TODO: Payload metadata: {text, chapter_id: 3, section_id, position, word_count, metadata}`
  - Add TODO: `# TODO: Metadata.concepts: Physical AI concepts (e.g., ["perception", "sensors", "vision", "signal-processing"])`

- [ ] [T018] [P1] [US1] Add `similarity_search_ch3()` function to `backend/app/ai/rag/qdrant_store.py`:
  - Function signature: `def similarity_search_ch3(query: str, top_k: int = 5) -> List[Dict[str, Any]]:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Implement similarity search for Chapter 3`
    - `# TODO: Use collection "chapter3" (from QDRANT_COLLECTION_CH3 env var)`
    - `# TODO: Embed query using generate_embedding(query, chapter_id=3)`
    - `# TODO: Perform vector search in Qdrant`
    - `# TODO: Return top-k most relevant chunks`
    - `# TODO: Add error handling for search failures`
    - `# TODO: Add result validation and filtering`
  - Return empty list placeholder: `return []`

- [ ] [T019] [P1] [US1] Verify qdrant_store.py is importable after updates: Run `cd backend && python -c "from app.ai.rag.qdrant_store import create_collection, upsert_vectors, similarity_search_ch3; print('Import successful')"` - should complete without errors

**Acceptance Test**: Qdrant store has Chapter 3 collection-specific TODO comments, similarity_search_ch3() function with comprehensive TODOs, imports work, function returns empty list placeholder

---

## PHASE 4 — RAG Pipeline Integration

**User Story**: US1 - Developer Sets Up Chapter 3 RAG Infrastructure

**Test Strategy**: Can be tested by creating ch3_pipeline.py with 5-step flow comments and verifying imports work.

### Create Chapter 3 RAG Pipeline File

- [ ] [T020] [P1] [US1] Create new file `backend/app/ai/rag/ch3_pipeline.py`:
  - Add file header comment: `"""Chapter 3 RAG Pipeline Orchestration"""`
  - Add imports: `from typing import Dict, Any, List`

- [ ] [T021] [P1] [US1] Add `run_ch3_rag_pipeline()` function to `backend/app/ai/rag/ch3_pipeline.py`:
  - Function signature: `async def run_ch3_rag_pipeline(query: str, top_k: int = 5) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Function description
    - Args documentation (query, top_k)
    - Returns documentation (context, chunks, query_embedding)
    - Pipeline Steps section with 5 steps:
      1. Retrieve chunks (call get_chapter_chunks(chapter_id=3))
      2. Embed query (call generate_embedding(query, chapter_id=3))
      3. Perform search (call similarity_search_ch3(query, top_k))
      4. Construct retrieval context (assemble retrieved chunks into context string)
      5. Return placeholder response (return context dictionary)

- [ ] [T022] [P1] [US1] Add TODO comments for each pipeline step in `run_ch3_rag_pipeline()` function body in `backend/app/ai/rag/ch3_pipeline.py`:
  - Step 1 TODOs:
    - `# TODO: Step 1 - Retrieve Chapter 3 chunks`
    - `# TODO:     from app.content.chapters.chapter_3_chunks import get_chapter_chunks`
    - `# TODO:     chunks = get_chapter_chunks(chapter_id=3)`
    - `# TODO:     Validate chunks are available`
  - Step 2 TODOs:
    - `# TODO: Step 2 - Embed user query`
    - `# TODO:     from app.ai.embeddings.embedding_client import generate_embedding`
    - `# TODO:     query_embedding = generate_embedding(query, chapter_id=3)`
    - `# TODO:     Validate embedding is generated`
  - Step 3 TODOs:
    - `# TODO: Step 3 - Perform similarity search`
    - `# TODO:     from app.ai.rag.qdrant_store import similarity_search_ch3`
    - `# TODO:     results = similarity_search_ch3(query, top_k)`
    - `# TODO:     Validate results are returned`
  - Step 4 TODOs:
    - `# TODO: Step 4 - Construct retrieval context`
    - `# TODO:     context = assemble_context_string(results)`
    - `# TODO:     Include section headers for context`
    - `# TODO:     Limit context size (max chunks from config)`
    - `# TODO:     Include chunk metadata`
  - Step 5 TODOs:
    - `# TODO: Step 5 - Return response`
    - `# TODO:     return {"context": context, "chunks": results, "query_embedding": query_embedding}`
  - Additional TODOs:
    - `# TODO: Add error handling for each step`
    - `# TODO: Add logging for pipeline execution`
    - `# TODO: Filter chunks by section_id when sectionId provided in request`
    - `# TODO: Limit context size (use configurable max chunks)`

- [ ] [T023] [P1] [US1] Add placeholder code comments in `run_ch3_rag_pipeline()` function body in `backend/app/ai/rag/ch3_pipeline.py`:
  - Add commented code: `# Step 1: Retrieve chunks (TODO)`
  - Add commented code: `# chunks = get_chapter_chunks(chapter_id=3)`
  - Add commented code: `# Step 2: Embed query (TODO)`
  - Add commented code: `# query_embedding = generate_embedding(query, chapter_id=3)`
  - Add commented code: `# Step 3: Perform search (TODO)`
  - Add commented code: `# results = similarity_search_ch3(query, top_k)`
  - Add commented code: `# Step 4: Construct context (TODO)`
  - Add commented code: `# context = assemble_context_string(results)`
  - Add commented code: `# Step 5: Return response (TODO)`
  - Add commented code: `# return {"context": context, "chunks": results, "query_embedding": query_embedding}`

- [ ] [T024] [P1] [US1] Add placeholder return statement to `run_ch3_rag_pipeline()` function in `backend/app/ai/rag/ch3_pipeline.py`:
  - Return: `return {"context": "", "chunks": [], "query_embedding": []}`

- [ ] [T025] [P1] [US1] Verify ch3_pipeline.py is importable: Run `cd backend && python -c "from app.ai.rag.ch3_pipeline import run_ch3_rag_pipeline; print('Import successful')"` - should complete without errors

**Acceptance Test**: Chapter 3 RAG pipeline file exists with run_ch3_rag_pipeline() function, 5-step flow comments, placeholder code comments, placeholder return, imports work

---

## PHASE 5 — MDX RAG Markers

**User Story**: US1 - Developer Sets Up Chapter 3 RAG Infrastructure

**Test Strategy**: Can be tested by adding RAG-CHUNK markers to chapter-3.mdx and verifying MDX build passes.

### Add RAG-CHUNK Markers to Chapter 3 MDX

- [ ] [T026] [P1] [US1] Add `<!-- RAG-CHUNK: start -->` marker before each section in `frontend/docs/chapters/chapter-3.mdx`:
  - Add marker before "What Is Perception in Physical AI?" section
  - Add marker before "Types of Sensors in Robotics" section
  - Add marker before "Computer Vision & Depth Perception" section
  - Add marker before "Signal Processing Basics for AI" section
  - Add marker before "Feature Extraction & Interpretation" section
  - Add marker before "Learning Objectives" section
  - Add marker before "Glossary" section

- [ ] [T027] [P1] [US1] Add `<!-- RAG-CHUNK: end -->` marker after each section in `frontend/docs/chapters/chapter-3.mdx`:
  - Add marker after "What Is Perception in Physical AI?" section (after `<!-- CHUNK: END -->`)
  - Add marker after "Types of Sensors in Robotics" section (after `<!-- CHUNK: END -->`)
  - Add marker after "Computer Vision & Depth Perception" section (after `<!-- CHUNK: END -->`)
  - Add marker after "Signal Processing Basics for AI" section (after `<!-- CHUNK: END -->`)
  - Add marker after "Feature Extraction & Interpretation" section (after `<!-- CHUNK: END -->`)
  - Add marker after "Learning Objectives" section (after `<!-- CHUNK: END -->`)
  - Add marker after "Glossary" section (after `<!-- CHUNK: END -->`)

- [ ] [T028] [P1] [US1] Verify RAG-CHUNK markers are properly placed: Check that markers wrap section content including AI blocks and diagrams, and don't interfere with existing CHUNK markers

- [ ] [T029] [P2] [US1] (Optional) Verify MDX build passes: Run `cd frontend && npm run build` to confirm MDX builds successfully with RAG-CHUNK markers

**Acceptance Test**: Chapter 3 MDX contains RAG-CHUNK markers around all 7 sections, markers are properly placed, MDX build passes (optional)

---

## PHASE 6 — Settings & Environment Updates

**User Story**: US2 - System Administrator Configures Chapter 3 RAG Settings

**Test Strategy**: Can be tested by updating settings.py and .env.example and verifying variables are documented.

### Update Settings Configuration

- [ ] [T030] [P1] [US2] Add Chapter 3 RAG configuration fields to `backend/app/config/settings.py`:
  - Add comment: `# === Chapter 3 Runtime Configuration ===`
  - Add field: `qdrant_collection_ch3: Optional[str] = None  # Qdrant collection name for Chapter 3 RAG operations`
  - Add field: `ch3_embedding_model: Optional[str] = None  # Embedding model for Chapter 3 (e.g., "text-embedding-3-small")`

- [ ] [T031] [P1] [US2] Verify settings.py is importable after updates: Run `cd backend && python -c "from app.config.settings import settings; print('Settings import successful')"` - should complete without errors

### Update Environment Variables

- [ ] [T032] [P2] [US2] Add Chapter 3 RAG environment variables to `.env.example` (create if doesn't exist):
  - Add comment: `# Chapter 3 RAG Configuration`
  - Add variable: `QDRANT_COLLECTION_CH3="chapter3"` with description: `# Qdrant collection name for Chapter 3`
  - Add variable: `EMBEDDING_MODEL_CH3="text-embedding-3-small"` with description: `# Embedding model for Chapter 3 (OpenAI)`

- [ ] [T033] [P2] [US2] Verify .env.example file is readable: Check that file exists and new variables are properly formatted

**Acceptance Test**: Settings file has qdrant_collection_ch3 and ch3_embedding_model fields, .env.example has 2 new environment variables with clear descriptions, files are properly formatted

---

## PHASE 7 — Contracts

**User Story**: US1 - Developer Sets Up Chapter 3 RAG Infrastructure

**Test Strategy**: Contracts already created in specification phase, verify they exist.

### Verify Contract Files

- [ ] [T034] [P1] [US1] Verify `specs/029-ch3-rag-prep/contracts/ch3-rag-definition.yaml` exists:
  - Check that file contains RAG pipeline contract
  - Check that 5-step pipeline flow is documented
  - Check that Chapter 3-specific considerations are included
  - Check that chunk structure, embedding format, Qdrant collection schema are documented

**Acceptance Test**: Contract file exists and contains required documentation (already created in spec phase)

---

## Phase 8: Validation & Testing

**Purpose**: Final validation to ensure all scaffolding is in place and backend starts successfully.

### Backend Validation

- [ ] [T035] [P1] [POLISH] Verify all imports resolve: Run `cd backend && python -c "from app.content.chapters.chapter_3_chunks import get_chapter_chunks, CH3_CHUNKS; from app.ai.embeddings.embedding_client import embed_chapter3_chunks, normalize_chapter3_embeddings; from app.ai.rag.qdrant_store import similarity_search_ch3; from app.ai.rag.ch3_pipeline import run_ch3_rag_pipeline; from app.config.settings import settings; print('All imports successful')"` - should complete without errors

- [ ] [T036] [P1] [POLISH] Verify backend starts successfully: Run `cd backend && python -c "from app.main import app; print('Backend startup OK')"` - should complete without errors

- [ ] [T037] [P1] [POLISH] Verify no syntax errors: Run `cd backend && python -m py_compile app/content/chapters/chapter_3_chunks.py app/ai/embeddings/embedding_client.py app/ai/rag/qdrant_store.py app/ai/rag/ch3_pipeline.py app/config/settings.py` - should complete without errors

### File Existence Validation

- [ ] [T038] [P1] [POLISH] Verify all updated files exist:
  - `backend/app/content/chapters/chapter_3_chunks.py` (updated with CH3_CHUNKS and TODOs)
  - `backend/app/ai/embeddings/embedding_client.py` (updated with Chapter 3 functions)
  - `backend/app/ai/rag/qdrant_store.py` (updated with Chapter 3 TODOs and similarity_search_ch3())
  - `backend/app/ai/rag/ch3_pipeline.py` (NEW FILE with 5-step pipeline)
  - `backend/app/config/settings.py` (updated with Chapter 3 config fields)
  - `frontend/docs/chapters/chapter-3.mdx` (updated with RAG-CHUNK markers)
  - `.env.example` (updated with 2 new env vars)

### TODO Validation

- [ ] [T039] [P1] [POLISH] Verify all functions have TODO comments:
  - `get_chapter_chunks()` has chunking TODO comments (including RAG-CHUNK markers)
  - `embed_chapter3_chunks()` has embedding TODO comments
  - `normalize_chapter3_embeddings()` has normalization TODO comments
  - `create_collection()` has Chapter 3 collection TODO comments
  - `upsert_vectors()` has Chapter 3 vector TODO comments
  - `similarity_search_ch3()` has Chapter 3 search TODO comments
  - `run_ch3_rag_pipeline()` has 5-step pipeline TODO comments

**Acceptance Test**: 
- All imports resolve without errors
- Backend starts successfully
- All files exist and are updated/created
- All functions have appropriate TODO comments
- No real RAG logic implemented (only placeholders)
- MDX contains RAG-CHUNK markers

---

## Summary

**Total Tasks**: 39 tasks across 8 phases
- Phase 0 (Setup): 7 tasks
- Phase 1 (Chunking): 5 tasks
- Phase 2 (Embeddings): 3 tasks
- Phase 3 (Qdrant): 4 tasks
- Phase 4 (Pipeline): 6 tasks
- Phase 5 (MDX Markers): 4 tasks
- Phase 6 (Settings/Environment): 4 tasks
- Phase 7 (Contracts): 1 task (already done)
- Phase 8 (Validation): 5 tasks

**Estimated Effort**: ~2-3 hours (mostly adding TODO comments, creating new file, and verifying imports)

**Dependencies**: Feature 028 (Chapter 3 AI Blocks Integration) and Feature 005 (AI Runtime Engine) must be complete

**Next Step**: Run `/sp.implement` to execute these tasks

