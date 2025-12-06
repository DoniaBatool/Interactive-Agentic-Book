# Tasks: Chapter 2 — RAG Chunking, Embedding Prep & Knowledge Source Scaffolding

**Feature**: 021-ch2-rag-prep | **Branch**: `021-ch2-rag-prep` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for establishing the RAG preparation layer for Chapter 2 (scaffolding only, no real chunking or RAG logic).

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

**Purpose**: Verify dependencies and prerequisites before implementing Chapter 2 RAG preparation scaffolding.

- [ ] [T001] [P1] [SETUP] Verify Feature 005 is complete: Check that `backend/app/ai/rag/pipeline.py` exists with RAG pipeline structure
- [ ] [T002] [P1] [SETUP] Verify Feature 012 is complete: Check that `backend/app/content/chapters/chapter_2_chunks.py` exists with `get_chapter_chunks()` function
- [ ] [T003] [P1] [SETUP] Verify Feature 014 is complete: Check that `frontend/docs/chapters/chapter-2.mdx` exists with 7 H2 sections
- [ ] [T004] [P1] [SETUP] Verify Feature 020 is complete: Check that `backend/app/ai/rag/collections/ch2_collection.py` exists with CH2_COLLECTION_NAME
- [ ] [T005] [P1] [SETUP] Verify metadata file exists: Check that `backend/app/content/chapters/chapter_2.py` exists with CHAPTER_METADATA
- [ ] [T006] [P1] [SETUP] Verify contract file exists: Check that `specs/021-ch2-rag-prep/contracts/rag-prep-schema.md` exists (from spec phase)
- [ ] [T007] [P1] [SETUP] Verify frontend builds: Run `cd frontend && npm run build` - should complete without errors (or at least MDX compiles)
- [ ] [T008] [P1] [SETUP] Verify backend imports work: Run `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; print('Import successful')"` - should complete without errors

**Success Criteria**:
- All prerequisite files exist
- Frontend MDX compiles without errors
- Backend imports resolve without errors
- Ready to implement scaffolding

**Dependencies**: Feature 005 (AI Runtime Engine), Feature 012 (Chapter 2 RAG), Feature 014 (Chapter 2 Content), Feature 020 (Chapter 2 AI Runtime)

---

## PHASE A — FRONTEND: MDX Chunking

**User Story**: US1 - Content Developer Prepares Chapter 2 for RAG

**Test Strategy**: Can be tested by adding chunk markers and verifying MDX builds successfully.

### Open and Prepare MDX File

- [ ] [T009] [P1] [US1] Open `frontend/docs/chapters/chapter-2.mdx`:
  - Verify file exists and is readable
  - Expected: File exists at specified path
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: File exists and can be opened

### Insert Chunk Marker for Section 1

- [ ] [T010] [P1] [US1] Insert `<!-- CHUNK: 1 -->` in `frontend/docs/chapters/chapter-2.mdx`:
  - Location: Before content placeholder in "Introduction to ROS 2" section
  - Format: `<!-- CHUNK: 1 -->`
  - Placement: After H2 heading, before content placeholder comment
  - Expected content: Chunk marker inserted before content placeholder
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: Chunk marker exists, follows regex pattern `<!-- CHUNK: [0-9]+ -->`

### Insert Chunk Marker for Section 2

- [ ] [T011] [P1] [US1] Insert `<!-- CHUNK: 2 -->` in `frontend/docs/chapters/chapter-2.mdx`:
  - Location: Before content placeholder in "Nodes and Node Communication" section
  - Format: `<!-- CHUNK: 2 -->`
  - Placement: After H2 heading, before content placeholder comment
  - Expected content: Chunk marker inserted before content placeholder
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: Chunk marker exists, follows regex pattern

### Insert Chunk Marker for Section 3

- [ ] [T012] [P1] [US1] Insert `<!-- CHUNK: 3 -->` in `frontend/docs/chapters/chapter-2.mdx`:
  - Location: Before content placeholder in "Topics and Messages" section
  - Format: `<!-- CHUNK: 3 -->`
  - Placement: After H2 heading, before content placeholder comment
  - Expected content: Chunk marker inserted before content placeholder
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: Chunk marker exists, follows regex pattern

### Insert Chunk Marker for Section 4

- [ ] [T013] [P1] [US1] Insert `<!-- CHUNK: 4 -->` in `frontend/docs/chapters/chapter-2.mdx`:
  - Location: Before content placeholder in "Services and Actions" section
  - Format: `<!-- CHUNK: 4 -->`
  - Placement: After H2 heading, before content placeholder comment
  - Expected content: Chunk marker inserted before content placeholder
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: Chunk marker exists, follows regex pattern

### Insert Chunk Marker for Section 5

- [ ] [T014] [P1] [US1] Insert `<!-- CHUNK: 5 -->` in `frontend/docs/chapters/chapter-2.mdx`:
  - Location: Before content placeholder in "ROS 2 Packages" section
  - Format: `<!-- CHUNK: 5 -->`
  - Placement: After H2 heading, before content placeholder comment
  - Expected content: Chunk marker inserted before content placeholder
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: Chunk marker exists, follows regex pattern

### Insert Chunk Marker for Section 6

- [ ] [T015] [P1] [US1] Insert `<!-- CHUNK: 6 -->` in `frontend/docs/chapters/chapter-2.mdx`:
  - Location: Before content placeholder in "Launch Files and Workflows" section
  - Format: `<!-- CHUNK: 6 -->`
  - Placement: After H2 heading, before content placeholder comment
  - Expected content: Chunk marker inserted before content placeholder
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: Chunk marker exists, follows regex pattern

### Insert Chunk Marker for Section 7

- [ ] [T016] [P1] [US1] Insert `<!-- CHUNK: 7 -->` in `frontend/docs/chapters/chapter-2.mdx`:
  - Location: Before content placeholder in "Glossary" section
  - Format: `<!-- CHUNK: 7 -->`
  - Placement: After H2 heading, before content placeholder comment
  - Expected content: Chunk marker inserted before content placeholder
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: Chunk marker exists, follows regex pattern

### Verify Diagram Markers Preserved

- [ ] [T017] [P1] [US1] Verify diagram markers remain intact in `frontend/docs/chapters/chapter-2.mdx`:
  - Check `<!-- DIAGRAM: ros2-ecosystem-overview -->` exists
  - Check `<!-- DIAGRAM: node-communication-architecture -->` exists
  - Check `<!-- DIAGRAM: topic-pubsub-flow -->` exists
  - Check `<!-- DIAGRAM: services-actions-comparison -->` exists
  - Expected: All 4 diagram markers exist and unchanged
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: All diagram markers preserved

### Verify AI-Block Components Preserved

- [ ] [T018] [P1] [US1] Verify AI-block components remain intact in `frontend/docs/chapters/chapter-2.mdx`:
  - Check `<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />` exists
  - Check `<GenerateDiagramBlock diagramType="node-communication-architecture" chapterId={2} />` exists
  - Check `<ExplainLike10Block concept="topics" chapterId={2} />` exists
  - Check `<InteractiveQuizBlock chapterId={2} numQuestions={5} />` exists
  - Expected: All 4 AI-block components exist and unchanged
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: All AI-block components preserved

### Verify Section Count Matches Metadata

- [ ] [T019] [P1] [US1] Verify section count matches metadata in `frontend/docs/chapters/chapter-2.mdx`:
  - Count H2 sections: Should be exactly 7
  - Compare with `backend/app/content/chapters/chapter_2.py` CHAPTER_METADATA["section_count"]
  - Expected: Exactly 7 H2 sections match metadata
  - Dependencies: Feature 014 (Chapter 2 Content)
  - Acceptance test: Section count matches metadata (7 sections)

### Validate MDX Build

- [ ] [T020] [P1] [US1] Validate MDX builds successfully:
  - Run: `cd frontend && npm run build`
  - Expected: Build completes without errors (or at least MDX compiles)
  - Dependencies: All chunk markers added
  - Acceptance test: MDX builds successfully, no compilation errors

**Phase Completion**: All chunk markers added (7 markers), diagram and AI-block markers preserved, MDX builds successfully

---

## PHASE B — BACKEND: Chunk Module

**User Story**: US1 - Content Developer Prepares Chapter 2 for RAG

**Test Strategy**: Can be tested by updating chunk file and verifying imports work.

### Verify Chunk File Exists

- [ ] [T021] [P1] [US1] Verify `backend/app/content/chapters/chapter_2_chunks.py` exists:
  - Check file exists at specified path
  - Expected: File exists (from Feature 012)
  - Dependencies: Feature 012 (Chapter 2 RAG)
  - Acceptance test: File exists at specified path

### Verify Function Signature

- [ ] [T022] [P1] [US1] Verify `get_chapter_chunks()` function exists in `backend/app/content/chapters/chapter_2_chunks.py`:
  - Check function signature: `def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:`
  - Check function is importable
  - Expected: Function exists with correct signature
  - Dependencies: Feature 012 (Chapter 2 RAG)
  - Acceptance test: Function exists, imports without errors

### Add Chunk Size Rules TODO Comments

- [ ] [T023] [P1] [US1] Add chunk size rules TODO comments to `backend/app/content/chapters/chapter_2_chunks.py`:
  - Add TODO comment: `# TODO: Chunk size rules: 120-220 words per chunk`
  - Add TODO comment: `# TODO: Minimum: 50 words (to maintain semantic meaning)`
  - Add TODO comment: `# TODO: Maximum: 300 words (to avoid token limits)`
  - Add TODO comment: `# TODO: Token limit: 512 tokens per chunk (for text-embedding-3-small)`
  - Add TODO comment: `# TODO: Implement chunk size validation`
  - Expected content: TODO comments added for chunk size rules
  - Dependencies: Existing `chapter_2_chunks.py` file
  - Acceptance test: Comments added, imports work, no syntax errors

### Add Semantic Grouping TODO Comments

- [ ] [T024] [P1] [US1] Add semantic grouping TODO comments to `backend/app/content/chapters/chapter_2_chunks.py`:
  - Add TODO comment: `# TODO: Semantic grouping: Group by topic, not paragraph count`
  - Add TODO comment: `# TODO: Respect H2 section boundaries`
  - Add TODO comment: `# TODO: Preserve concept units (don't split related ideas)`
  - Add TODO comment: `# TODO: Group paragraphs by semantic topic`
  - Expected content: TODO comments added for semantic grouping
  - Dependencies: Existing `chapter_2_chunks.py` file
  - Acceptance test: Comments added, imports work, no syntax errors

### Add Glossary Handling TODO Comments

- [ ] [T025] [P1] [US1] Add glossary handling TODO comments to `backend/app/content/chapters/chapter_2_chunks.py`:
  - Add TODO comment: `# TODO: Glossary handling: Group as single chunks, don't break entries`
  - Add TODO comment: `# TODO: Group glossary entries as single chunks`
  - Add TODO comment: `# TODO: Don't split glossary entries across chunks`
  - Expected content: TODO comments added for glossary handling
  - Dependencies: Existing `chapter_2_chunks.py` file
  - Acceptance test: Comments added, imports work, no syntax errors

### Add Diagram Linking TODO Comments

- [ ] [T026] [P1] [US1] Add diagram linking TODO comments to `backend/app/content/chapters/chapter_2_chunks.py`:
  - Add TODO comment: `# TODO: Diagram linking: Link explanations with adjacent text`
  - Add TODO comment: `# TODO: Link diagram explanations with adjacent text`
  - Add TODO comment: `# TODO: Include diagram context in chunks`
  - Expected content: TODO comments added for diagram linking
  - Dependencies: Existing `chapter_2_chunks.py` file
  - Acceptance test: Comments added, imports work, no syntax errors

### Add Embedding Guidelines TODO Comments

- [ ] [T027] [P1] [US1] Add embedding guidelines TODO comments to `backend/app/content/chapters/chapter_2_chunks.py`:
  - Add TODO comment: `# TODO: Embedding guidelines: Prepare chunks for embedding generation`
  - Add TODO comment: `# TODO: Prepare chunks for embedding generation`
  - Add TODO comment: `# TODO: Include metadata for embedding context`
  - Expected content: TODO comments added for embedding guidelines
  - Dependencies: Existing `chapter_2_chunks.py` file
  - Acceptance test: Comments added, imports work, no syntax errors

### Add Retrieval Linking TODO Comments

- [ ] [T028] [P1] [US1] Add retrieval linking TODO comments to `backend/app/content/chapters/chapter_2_chunks.py`:
  - Add TODO comment: `# TODO: Retrieval linking: Prepare chunks for RAG ingestion`
  - Add TODO comment: `# TODO: Prepare chunks for RAG ingestion`
  - Add TODO comment: `# TODO: Include section context for retrieval`
  - Expected content: TODO comments added for retrieval linking
  - Dependencies: Existing `chapter_2_chunks.py` file
  - Acceptance test: Comments added, imports work, no syntax errors

### Add Chunk Marker Usage TODO Comments

- [ ] [T029] [P1] [US1] Add chunk marker usage TODO comments to `backend/app/content/chapters/chapter_2_chunks.py`:
  - Add TODO comment: `# TODO: Chunk marker usage: Use chunk markers (<!-- CHUNK: x -->) to identify boundaries`
  - Add TODO comment: `# TODO: Extract chunks using chunk markers`
  - Add TODO comment: `# TODO: Maintain chunk order`
  - Expected content: TODO comments added for chunk marker usage
  - Dependencies: Existing `chapter_2_chunks.py` file
  - Acceptance test: Comments added, imports work, no syntax errors

### Enhance Function Docstring

- [ ] [T030] [P1] [US1] Enhance function docstring in `backend/app/content/chapters/chapter_2_chunks.py`:
  - Update docstring to include chunking strategy documentation
  - Add section: "Chunking Strategy (TODO):"
  - Include: Chunk size rules, semantic grouping, special content handling, chunk marker usage, embedding guidelines, retrieval linking
  - Expected content: Enhanced docstring with comprehensive chunking strategy
  - Dependencies: Existing `chapter_2_chunks.py` file
  - Acceptance test: Docstring enhanced, imports work, no syntax errors

### Verify Chunk File Imports

- [ ] [T031] [P1] [US1] Verify `backend/app/content/chapters/chapter_2_chunks.py` imports correctly:
  - Run: `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; print('Import successful')"`
  - Expected: Import succeeds without errors
  - Dependencies: All updated code in chapter_2_chunks.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: Chunk file enhanced with comprehensive TODO comments, imports work

---

## PHASE C — CONTRACTS

**User Story**: US1 - Content Developer Prepares Chapter 2 for RAG

**Test Strategy**: Can be tested by verifying contract file exists and is complete.

### Verify Contract File Exists

- [ ] [T032] [P1] [US1] Verify `specs/021-ch2-rag-prep/contracts/rag-prep-schema.md` exists:
  - Check file exists at specified path
  - Expected: File exists (from spec phase)
  - Dependencies: Feature 021 spec phase
  - Acceptance test: File exists at specified path

### Verify Marker Format Documentation

- [ ] [T033] [P1] [US1] Verify marker format documentation in `specs/021-ch2-rag-prep/contracts/rag-prep-schema.md`:
  - Check chunk marker contract section exists
  - Check format documented: `<!-- CHUNK: x -->`
  - Check regex pattern documented: `<!-- CHUNK: [0-9]+ -->`
  - Expected: Marker format fully documented
  - Dependencies: Contract file from spec phase
  - Acceptance test: Marker format documented, regex pattern included

### Verify Embedding Boundaries Documentation

- [ ] [T034] [P1] [US1] Verify embedding boundaries documentation in `specs/021-ch2-rag-prep/contracts/rag-prep-schema.md`:
  - Check embedding boundaries section exists
  - Check chunk size rules documented: 120-220 words
  - Check semantic boundaries documented
  - Expected: Embedding boundaries fully documented
  - Dependencies: Contract file from spec phase
  - Acceptance test: Embedding boundaries documented, chunk size rules included

### Verify Retrieval Rules Documentation

- [ ] [T035] [P1] [US1] Verify retrieval rules documentation in `specs/021-ch2-rag-prep/contracts/rag-prep-schema.md`:
  - Check retrieval context rules section exists
  - Check context assembly documented
  - Check metadata inclusion documented
  - Expected: Retrieval rules fully documented
  - Dependencies: Contract file from spec phase
  - Acceptance test: Retrieval rules documented, context assembly included

### Verify Semantic Grouping Rules Documentation

- [ ] [T036] [P1] [US1] Verify semantic grouping rules documentation in `specs/021-ch2-rag-prep/contracts/rag-prep-schema.md`:
  - Check semantic boundaries section exists
  - Check grouping strategy documented: Group by topic, not paragraph count
  - Check boundary rules documented
  - Expected: Semantic grouping rules fully documented
  - Dependencies: Contract file from spec phase
  - Acceptance test: Semantic grouping rules documented, grouping strategy included

**Phase Completion**: Contract file verified, all sections documented

---

## PHASE D — RAG Pipeline Hooks

**User Story**: US1 - Content Developer Prepares Chapter 2 for RAG

**Test Strategy**: Can be tested by updating pipeline file and verifying imports work.

### Verify Pipeline File Exists

- [ ] [T037] [P1] [US1] Verify `backend/app/ai/rag/pipeline.py` exists:
  - Check file exists at specified path
  - Expected: File exists (from Feature 005)
  - Dependencies: Feature 005 (AI Runtime Engine)
  - Acceptance test: File exists at specified path

### Add Chapter 2 Collection Registration TODO

- [ ] [T038] [P1] [US1] Add Chapter 2 collection registration TODO to `backend/app/ai/rag/pipeline.py`:
  - Add TODO comment: `# TODO: Register Chapter 2 collection name`
  - Add TODO comment: `# TODO: Use CH2_COLLECTION_NAME from ch2_collection.py`
  - Add TODO comment: `# TODO: Collection name: "chapter_2" (from QDRANT_COLLECTION_CH2 env var)`
  - Add TODO comment: `# TODO: from app.ai.rag.collections.ch2_collection import CH2_COLLECTION_NAME`
  - Add TODO comment: `# TODO: Register collection name when chapter_id=2`
  - Expected content: TODO comments added for collection registration
  - Dependencies: Existing `pipeline.py` file, Feature 020 (ch2_collection.py)
  - Acceptance test: Comments added, imports work, no syntax errors

### Add Chapter 2 Embedding Batch TODO

- [ ] [T039] [P1] [US1] Add Chapter 2 embedding batch TODO to `backend/app/ai/rag/pipeline.py`:
  - Add TODO comment: `# TODO: Prepare chapter-specific embedding batch for Chapter 2`
  - Add TODO comment: `# TODO: Use batch_embed_ch2() from embedding_client.py`
  - Add TODO comment: `# TODO: Process chunks in batches (e.g., 100 chunks per batch)`
  - Add TODO comment: `# TODO: Use CH2_EMBEDDING_MODEL for Chapter 2 embeddings`
  - Add TODO comment: `# TODO: from app.ai.embeddings.embedding_client import batch_embed_ch2`
  - Add TODO comment: `# TODO: Prepare embedding batch when chapter_id=2`
  - Expected content: TODO comments added for embedding batch
  - Dependencies: Existing `pipeline.py` file, Feature 020 (embedding_client.py)
  - Acceptance test: Comments added, imports work, no syntax errors

### Add Chapter 2 Retrieval Context Builder TODO

- [ ] [T040] [P1] [US1] Add Chapter 2 retrieval context builder TODO to `backend/app/ai/rag/pipeline.py`:
  - Add TODO comment: `# TODO: Placeholder search function for Chapter 2`
  - Add TODO comment: `# TODO: Use search() from ch2_collection.py`
  - Add TODO comment: `# TODO: Perform semantic search in "chapter_2" collection`
  - Add TODO comment: `# TODO: Return top-k most relevant chunks`
  - Add TODO comment: `# TODO: from app.ai.rag.collections.ch2_collection import search`
  - Add TODO comment: `# TODO: Build retrieval context from search results`
  - Add TODO comment: `# TODO: Assemble context string with chunk metadata`
  - Expected content: TODO comments added for retrieval context builder
  - Dependencies: Existing `pipeline.py` file, Feature 020 (ch2_collection.py)
  - Acceptance test: Comments added, imports work, no syntax errors

### Verify Pipeline File Imports

- [ ] [T041] [P1] [US1] Verify `backend/app/ai/rag/pipeline.py` imports correctly:
  - Run: `cd backend && python -c "from app.ai.rag.pipeline import run_rag_pipeline; print('Import successful')"`
  - Expected: Import succeeds without errors
  - Dependencies: All updated code in pipeline.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: RAG pipeline hooks added, imports work

---

## PHASE E — VALIDATION

**User Story**: US2 - System Administrator Validates RAG Preparation

**Test Strategy**: Can be tested by running validation checks on all files.

### Confirm MDX Compiles

- [ ] [T042] [P1] [US2] Confirm MDX compiles successfully:
  - Run: `cd frontend && npm run build`
  - Expected: Build completes without errors (or at least MDX compiles)
  - Dependencies: All chunk markers added
  - Acceptance test: MDX builds successfully, no compilation errors

### Confirm Python Imports Clean

- [ ] [T043] [P1] [US2] Confirm Python imports clean:
  - Test chunk file import: `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; print('Import successful')"`
  - Test pipeline import: `cd backend && python -c "from app.ai.rag.pipeline import run_rag_pipeline; print('Import successful')"`
  - Expected: All imports succeed without errors
  - Dependencies: All updated files
  - Acceptance test: All imports work, no syntax errors

### Confirm Marker Regex Passes

- [ ] [T044] [P1] [US2] Confirm marker regex passes:
  - Extract all chunk markers from `frontend/docs/chapters/chapter-2.mdx`
  - Validate each marker matches regex: `<!-- CHUNK: [0-9]+ -->`
  - Count markers: Should be 7 markers
  - Expected: All markers match regex pattern, count is 7
  - Dependencies: All chunk markers added
  - Acceptance test: All markers match regex, count is correct

### Confirm Folder Structure Exists

- [ ] [T045] [P1] [US2] Confirm folder structure exists:
  - Check `specs/021-ch2-rag-prep/` directory exists
  - Check `specs/021-ch2-rag-prep/contracts/` directory exists
  - Check `specs/021-ch2-rag-prep/checklists/` directory exists
  - Check `history/prompts/021-ch2-rag-prep/` directory exists
  - Expected: All required directories exist
  - Dependencies: Spec and plan phases
  - Acceptance test: All directories exist

### Verify Section Count Validation

- [ ] [T046] [P1] [US2] Verify section count validation:
  - Count H2 sections in `frontend/docs/chapters/chapter-2.mdx`: Should be 7
  - Compare with `backend/app/content/chapters/chapter_2.py` CHAPTER_METADATA["section_count"]
  - Expected: Section count matches metadata (7 sections)
  - Dependencies: MDX file, metadata file
  - Acceptance test: Section count matches metadata

### Verify Chunk Marker Count

- [ ] [T047] [P1] [US2] Verify chunk marker count:
  - Count chunk markers in `frontend/docs/chapters/chapter-2.mdx`: Should be 7
  - Expected: Exactly 7 chunk markers (one per section)
  - Dependencies: All chunk markers added
  - Acceptance test: Chunk marker count is 7

### Verify Backend Starts

- [ ] [T048] [P1] [US2] Verify backend starts successfully:
  - Run: `cd backend && python -c "from app.main import app; print('Backend starts OK')"`
  - Expected: Backend starts without import errors or runtime exceptions
  - Dependencies: All updated files
  - Acceptance test: Backend starts, no errors

**Phase Completion**: All validations pass, MDX builds, imports work, markers valid

---

## Summary

**Total Tasks**: 48 tasks across 5 phases

**Phases**:
1. Phase 0: Setup & Prerequisites (8 tasks)
2. Phase A: FRONTEND — MDX Chunking (12 tasks)
3. Phase B: BACKEND — Chunk Module (11 tasks)
4. Phase C: CONTRACTS (5 tasks)
5. Phase D: RAG Pipeline Hooks (5 tasks)
6. Phase E: VALIDATION (7 tasks)

**Priority Distribution**:
- P1 (Critical): 48 tasks
- P2 (Important): 0 tasks
- P3 (Nice-to-have): 0 tasks

**Dependencies**:
- Feature 005 (AI Runtime Engine) - must be complete
- Feature 012 (Chapter 2 RAG) - must be complete
- Feature 014 (Chapter 2 Content) - must be complete
- Feature 020 (Chapter 2 AI Runtime) - must be complete

**Success Criteria**:
- All P1 tasks completed
- MDX file contains 7 chunk markers (one per section)
- Chunk markers follow regex pattern `<!-- CHUNK: [0-9]+ -->`
- Chunk file enhanced with comprehensive TODO comments
- RAG pipeline updated with TODO hooks for Chapter 2
- MDX builds successfully
- All files import cleanly
- Section count matches metadata (7 sections)
- No business logic implemented (scaffolding only)

---

Tasks complete — ready for /sp.implement.
