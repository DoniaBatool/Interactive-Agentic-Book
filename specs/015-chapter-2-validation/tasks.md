# Tasks: Chapter 2 Validation, Testing, Build Stability & Integration Checks

**Feature**: 015-chapter-2-validation | **Branch**: `015-chapter-2-validation` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for validating Chapter 2 content, metadata, AI-block integrations, RAG pipeline, embeddings, runtime engine, and build stability. No new features; only validation.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), US3 (User Story 3), SETUP (Initial setup), VALIDATION (Validation tasks)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before running validations.

- [ ] [T001] [P1] [SETUP] Verify Feature 014 is complete: Check that `frontend/docs/chapters/chapter-2.mdx` exists with 7 sections
- [ ] [T002] [P1] [SETUP] Verify Feature 011 is complete: Check that AI-block React components exist in `frontend/src/components/ai/`
- [ ] [T003] [P1] [SETUP] Verify Feature 012 is complete: Check that `backend/app/content/chapters/chapter_2_chunks.py` exists
- [ ] [T004] [P1] [SETUP] Verify Feature 013 is complete: Check that `backend/app/ai/runtime/engine.py` has Chapter 2 routing
- [ ] [T005] [P1] [SETUP] Verify backend directory structure exists: Check that `backend/app/content/chapters/` directory exists
- [ ] [T006] [P1] [SETUP] Verify frontend directory structure exists: Check that `frontend/docs/chapters/` directory exists
- [ ] [T007] [P1] [SETUP] Verify tests directory exists: Check that `tests/` directory exists (create if needed)

**Success Criteria**:
- All prerequisite files and directories exist
- All dependent features (010-014) are complete
- Ready to run validations

**Dependencies**: Feature 010, 011, 012, 013, 014 (all must be complete)

---

## PHASE 1 — MDX VALIDATION

**User Story**: US1 - Developer Validates Chapter 2 Structure

**Test Strategy**: Can be tested by running validation commands and verifying results match expected values.

### Section Count Validation

- [ ] [T008] [P1] [US1] Validate 7 H2 sections in `frontend/docs/chapters/chapter-2.mdx`:
  - Run: `grep -c "^## " frontend/docs/chapters/chapter-2.mdx`
  - Expected: 7
  - Document result in validation report

### AI-Block Placeholder Validation

- [ ] [T009] [P1] [US1] Validate 4 AI-block placeholders in `frontend/docs/chapters/chapter-2.mdx`:
  - Run: `grep -c "chapterId={2}" frontend/docs/chapters/chapter-2.mdx`
  - Expected: 4
  - Verify all have `chapterId={2}`
  - Document result in validation report

### Diagram Placeholder Validation

- [ ] [T010] [P1] [US1] Validate 4 DIAGRAM placeholders in `frontend/docs/chapters/chapter-2.mdx`:
  - Run: `grep -c "<!-- DIAGRAM:" frontend/docs/chapters/chapter-2.mdx`
  - Expected: 4
  - Verify all are kebab-case: `ros2-ecosystem-overview`, `node-communication-architecture`, `topic-pubsub-flow`, `services-actions-comparison`
  - Document result in validation report

### Glossary Term Validation

- [ ] [T011] [P1] [US1] Validate 7 glossary terms in `frontend/docs/chapters/chapter-2.mdx`:
  - Extract glossary section
  - Count placeholder terms: ROS 2, Node, Topic, Service, Action, Package, Launch File
  - Expected: 7 terms
  - Document result in validation report

### Frontmatter Format Validation

- [ ] [T012] [P1] [US1] Validate frontmatter format in `frontend/docs/chapters/chapter-2.mdx`:
  - Check `title: "Chapter 2 — ROS 2 Fundamentals"` exists
  - Check `description: "..."` exists and is non-empty
  - Check `sidebar_position: 2` exists
  - Check `sidebar_label: "Chapter 2: ROS 2 Fundamentals"` exists
  - Check `tags: ["ros2", "robotics", "programming", "beginner"]` exists
  - Document result in validation report

**Phase Completion**: All MDX validations pass, results documented

---

## PHASE 2 — METADATA VALIDATION

**User Story**: US1 - Developer Validates Chapter 2 Structure

**Test Strategy**: Can be tested by importing metadata and comparing with MDX structure.

### Section Count Match Validation

- [ ] [T013] [P1] [US1] Ensure `backend/app/content/chapters/chapter_2.py` section_count matches MDX:
  - Import: `from app.content.chapters.chapter_2 import CHAPTER_METADATA`
  - Compare: `CHAPTER_METADATA["section_count"]` with MDX section count (from Phase 1)
  - Expected: Both equal 7
  - Document result in validation report

### AI Blocks Match Validation

- [ ] [T014] [P1] [US1] Ensure `backend/app/content/chapters/chapter_2.py` ai_blocks[] matches MDX:
  - Extract AI-block types from MDX (from Phase 1)
  - Compare: `CHAPTER_METADATA["ai_blocks"]` with MDX AI-block types
  - Expected: Sets match (4 items: ask-question, generate-diagram, explain-like-i-am-10, interactive-quiz)
  - Document result in validation report

### Diagram Placeholders Match Validation

- [ ] [T015] [P1] [US1] Ensure `backend/app/content/chapters/chapter_2.py` diagram_placeholders[] matches MDX:
  - Extract diagram placeholders from MDX (from Phase 1)
  - Compare: `CHAPTER_METADATA["diagram_placeholders"]` with MDX diagram placeholders
  - Expected: Sets match (4 items: ros2-ecosystem-overview, node-communication-architecture, topic-pubsub-flow, services-actions-comparison)
  - Document result in validation report

### Glossary Terms & Learning Outcomes Validation

- [ ] [T016] [P1] [US1] Validate glossary_terms and learning_outcomes fields in `backend/app/content/chapters/chapter_2.py`:
  - Check `CHAPTER_METADATA["glossary_terms"]` exists and has 7 items
  - Check `CHAPTER_METADATA["learning_outcomes"]` exists and is non-empty
  - Compare glossary_terms with MDX glossary terms (from Phase 1)
  - Expected: Sets match
  - Document result in validation report

**Phase Completion**: All metadata validations pass, results documented

---

## PHASE 3 — CHUNK FILE VALIDATION

**User Story**: US1 - Developer Validates Chapter 2 Structure

**Test Strategy**: Can be tested by importing chunk file and verifying function exists and signature is correct.

### Import Validation

- [ ] [T017] [P1] [US1] Ensure `backend/app/content/chapters/chapter_2_chunks.py` imports correctly:
  - Run: `python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; print('Import successful')"`
  - Expected: No import errors
  - Document result in validation report

### Function Signature Validation

- [ ] [T018] [P1] [US1] Ensure chunk function uses correct signature in `backend/app/content/chapters/chapter_2_chunks.py`:
  - Verify function `get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]` exists
  - Verify return type is `List[Dict[str, Any]]` (placeholder return acceptable)
  - Document result in validation report

### Chunk Placeholder Validation

- [ ] [T019] [P1] [US1] Ensure no invalid characters in chunk placeholders in `backend/app/content/chapters/chapter_2_chunks.py`:
  - Verify function returns list (empty list acceptable for placeholders)
  - Verify no syntax errors in file
  - Document result in validation report

**Phase Completion**: All chunk file validations pass, results documented

---

## PHASE 4 — RAG & EMBEDDING PIPELINE

**User Story**: US1 - Developer Validates Chapter 2 Structure

**Test Strategy**: Can be tested by importing RAG pipeline components and verifying they can import Chapter 2 chunks.

### Qdrant Store Import Validation

- [ ] [T020] [P1] [US1] Validate Qdrant store import works in `backend/app/ai/rag/qdrant_store.py`:
  - Run: `python -c "from app.ai.rag.qdrant_store import create_collection, upsert_vectors; print('Import successful')"`
  - Expected: No import errors
  - Verify collection name "chapter_2" is supported (check comments/TODOs)
  - Document result in validation report

### Embedding Client Placeholder Methods Validation

- [ ] [T021] [P1] [US1] Validate embedding_client placeholder methods exist in `backend/app/ai/embeddings/embedding_client.py`:
  - Run: `python -c "from app.ai.embeddings.embedding_client import generate_embedding, batch_embed; print('Import successful')"`
  - Expected: No import errors
  - Verify methods exist (placeholder acceptable)
  - Document result in validation report

### RAG Pipeline Import Validation

- [ ] [T022] [P1] [US1] Validate RAG pipeline imports chapter 2 chunks in `backend/app/ai/rag/pipeline.py`:
  - Run: `python -c "from app.ai.rag.pipeline import run_rag_pipeline; from app.content.chapters.chapter_2_chunks import get_chapter_chunks; print('Import successful')"`
  - Expected: No import errors
  - Verify pipeline can handle `chapter_id=2` parameter (check comments/TODOs)
  - Document result in validation report

**Phase Completion**: All RAG & embedding pipeline validations pass, results documented

---

## PHASE 5 — AI RUNTIME ROUTING

**User Story**: US1 - Developer Validates Chapter 2 Structure

**Test Strategy**: Can be tested by verifying routing logic and stub responses exist.

### API Routing Validation

- [ ] [T023] [P1] [US1] Validate `backend/app/api/ai_blocks.py` routes correctly:
  - Verify router exists and routes are defined
  - Verify all four AI block types have routes: ask-question, explain-el10, interactive-quiz, generate-diagram
  - Verify routes accept `chapterId` parameter
  - Document result in validation report

### Runtime Engine Stub Logic Validation

- [ ] [T024] [P1] [US1] Validate runtime engine stub logic loads without error in `backend/app/ai/runtime/engine.py`:
  - Run: `python -c "from app.ai.runtime.engine import run_ai_block; print('Import successful')"`
  - Expected: No import errors
  - Verify Chapter 2 routing logic exists (check comments/TODOs)
  - Verify stub responses exist for all four block types
  - Document result in validation report

**Phase Completion**: All AI runtime routing validations pass, results documented

---

## PHASE 6 — TESTING

**User Story**: US3 - QA Engineer Runs Integration Tests

**Test Strategy**: Can be tested by creating test stubs and running them with pytest.

### Test File Creation

- [ ] [T025] [P1] [US3] Create `tests/test_chapter_2_runtime.py`:
  - Create file with module docstring
  - Add imports: `import pytest`, `from app.content.chapters.chapter_2 import CHAPTER_METADATA`
  - Add test for metadata imports
  - Document result in validation report

### Stub Tests for AI Block Endpoints

- [ ] [T026] [P1] [US3] Add stub tests for AI block endpoints in `tests/test_chapter_2_runtime.py`:
  - Add test: `test_ask_question_endpoint_stub()` (TODO placeholder)
  - Add test: `test_explain_el10_endpoint_stub()` (TODO placeholder)
  - Add test: `test_interactive_quiz_endpoint_stub()` (TODO placeholder)
  - Add test: `test_generate_diagram_endpoint_stub()` (TODO placeholder)
  - All tests should have TODO placeholders (no real implementation)
  - Document result in validation report

### Import Stability Tests

- [ ] [T027] [P1] [US3] Add import stability tests in `tests/test_chapter_2_runtime.py`:
  - Add test: `test_import_stability()` that imports all Chapter 2 dependencies
  - Verify all imports succeed: chapter_2, chapter_2_chunks, pipeline, ai_blocks, runtime engine
  - Expected: No import errors
  - Document result in validation report

- [ ] [T028] [P1] [US3] Run test stubs to verify they execute without failure:
  - Run: `pytest tests/test_chapter_2_runtime.py -v`
  - Expected: All tests pass or skip (with TODO markers)
  - Document result in validation report

**Phase Completion**: All test stubs created and run without failure, results documented

---

## PHASE 7 — BUILD STABILITY

**User Story**: US2 - System Administrator Ensures Build Stability

**Test Strategy**: Can be tested by running frontend build and backend boot commands.

### Frontend Build Validation

- [ ] [T029] [P1] [US2] Verify frontend build success:
  - Run: `cd frontend && npm run build`
  - Expected: Build completes successfully with no errors
  - Check for build warnings (document acceptable warnings)
  - Document result in validation report

### Backend Boot Validation

- [ ] [T030] [P1] [US2] Verify backend boots without error:
  - Run: `cd backend && python -m uvicorn app.main:app --reload` (start and stop)
  - Expected: Server starts without import errors or runtime exceptions
  - Check for import errors
  - Check for runtime exceptions
  - Document result in validation report

- [ ] [T031] [P1] [US2] Verify import graph stability:
  - Check for circular dependencies (manual inspection or importlib)
  - Verify all imports resolve correctly
  - Expected: No circular dependencies
  - Document result in validation report

**Phase Completion**: All build stability validations pass, results documented

---

## PHASE 8 — DOCUMENTATION

**User Story**: US1, US2, US3 - All User Stories

**Test Strategy**: Can be tested by verifying validation report is generated with all results.

### Validation Report Generation

- [ ] [T032] [P1] [US1] Generate `specs/015-chapter-2-validation/checklists/validation-report.md`:
  - Update summary section with total validations, passed, failed, warnings
  - Fill in all 7 validation category results (MDX Structure, Metadata Consistency, Chunk File, RAG Pipeline, AI Runtime Routing, API Contract Testing, Build Stability)
  - Add recommendations section (if any failures)
  - Add next steps section
  - Document all validation results from Phases 1-7

### Validation Schema Documentation

- [ ] [T033] [P2] [US1] Verify `specs/015-chapter-2-validation/contracts/validation-schema.md` exists:
  - Check file exists (created in spec phase)
  - Verify all validation categories are documented
  - Verify validation response schemas are documented
  - Document result in validation report

### Research Documentation Update

- [ ] [T034] [P2] [US1] Update `specs/015-chapter-2-validation/research.md` with testing results:
  - Add validation results summary
  - Add any observations from validation process
  - Add recommendations for future improvements
  - Document result in validation report

**Phase Completion**: All documentation tasks complete, validation report generated with all results

---

## Summary

**Total Tasks**: 34 tasks across 8 phases
- Phase 0: Setup & Prerequisites (7 tasks)
- Phase 1: MDX Validation (5 tasks)
- Phase 2: Metadata Validation (4 tasks)
- Phase 3: Chunk File Validation (3 tasks)
- Phase 4: RAG & Embedding Pipeline (3 tasks)
- Phase 5: AI Runtime Routing (2 tasks)
- Phase 6: Testing (4 tasks)
- Phase 7: Build Stability (3 tasks)
- Phase 8: Documentation (3 tasks)

**Estimated Time**: ~1-2 hours (validation execution and report generation)

**Success Criteria**:
- All MDX validations pass (7 sections, 4 diagrams, 4 AI blocks, 7 glossary terms, frontmatter)
- All metadata validations pass (section_count, ai_blocks, diagram_placeholders, glossary_terms, learning_outcomes match)
- Chunk file validation passes (imports, function signature, return type)
- RAG pipeline validation passes (imports, Qdrant collection, embedding methods)
- AI runtime routing validation passes (routing, stub responses)
- Test stubs created and run without failure
- Frontend build succeeds
- Backend boots without errors
- Validation report generated with all results

**Next Step**: Run `/sp.implement` to execute all validation tasks
