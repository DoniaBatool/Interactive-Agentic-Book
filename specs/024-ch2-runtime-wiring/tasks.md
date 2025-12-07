# Tasks: Chapter 2 — Backend Runtime Wiring for AI Blocks

**Feature**: 024-ch2-runtime-wiring | **Branch**: `024-ch2-runtime-wiring` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for wiring Chapter 2 into backend runtime system by updating API layer, extending runtime engine, creating chunks file, creating subagent scaffolds, and extending skills layer (scaffolding only, no real AI logic).

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), SETUP (Initial setup), VALIDATION (Testing/validation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before wiring Chapter 2 into backend runtime.

- [ ] [T001] [P1] [SETUP] Verify AI Runtime Engine exists: Check that `backend/app/ai/runtime/engine.py` exists and is importable
- [ ] [T002] [P1] [SETUP] Verify API layer exists: Check that `backend/app/api/ai_blocks.py` exists and routes to runtime engine
- [ ] [T003] [P1] [SETUP] Verify Chapter 1 chunks structure exists: Check that `backend/app/content/chapters/chapter_1_chunks.py` exists (for reference structure)
- [ ] [T004] [P1] [SETUP] Verify existing subagents exist: Check that subagent files exist in `backend/app/ai/subagents/` (for reference structure)
- [ ] [T005] [P1] [SETUP] Verify skills layer exists: Check that `backend/app/ai/skills/retrieval_skill.py`, `prompt_builder_skill.py`, `formatting_skill.py` exist
- [ ] [T006] [P1] [SETUP] Verify backend starts successfully: Run `cd backend && uvicorn app.main:app` to confirm server starts without errors

**Success Criteria**:
- All required files and directories exist
- Backend starts without errors
- All imports resolve correctly

**Dependencies**: Feature 006 (AI Runtime Engine) must be complete

---

## PHASE 1 — API Layer

**User Story**: US2 - System Routes Chapter 2 AI Block Requests

**Test Strategy**: Can be tested by verifying API endpoints route chapterId=2 to runtime engine and contain routing comments.

### API Layer Updates

- [ ] [T007] [P1] [US2] Update `backend/app/api/ai_blocks.py` to pass chapterId=2 to run_ai_block:
  - Verify all 4 endpoints (ask-question, explain-like-10, quiz, diagram) accept chapterId parameter
  - Ensure chapterId=2 is passed to `run_ai_block(block_type, request_data)` where request_data includes chapterId=2
  - Verify routing is generic (not hardcoded to chapterId=1)

- [ ] [T008] [P1] [US2] Add routing comments for all 4 CH2 endpoints in `backend/app/api/ai_blocks.py`:
  - Add comment in ask-question endpoint: `# TODO: Chapter 2 runtime call`
  - Add comment in explain-like-10 endpoint: `# TODO: Chapter 2 runtime call`
  - Add comment in quiz endpoint: `# TODO: Chapter 2 runtime call`
  - Add comment in diagram endpoint: `# TODO: Chapter 2 runtime call`

**Acceptance Test**: All 4 endpoints route chapterId=2 to runtime engine, routing comments are present

---

## PHASE 2 — Runtime Engine

**User Story**: US1 - Developer Wires Chapter 2 into Backend Runtime

**Test Strategy**: Can be tested by verifying runtime engine has Chapter 2 routing placeholders and TODO markers.

### Runtime Engine Updates

- [ ] [T009] [P1] [US1] Update `backend/app/ai/runtime/engine.py` with CH2 placeholder routing:
  - Verify/add `if chapter_id == 2:` block in `run_ai_block()` function
  - Add placeholder routing comments describing expected flow
  - Ensure Chapter 2 routing path exists (may already exist from Feature 022)

- [ ] [T010] [P1] [US1] Add TODO markers for each runtime stage in `backend/app/ai/runtime/engine.py`:
  - Add TODO for RAG stage: `# TODO: Load Chapter 2 RAG context`
  - Add TODO for LLM stage: `# TODO: Select LLM provider for Chapter 2`
  - Add TODO for format stage: `# TODO: Format response for Chapter 2`
  - Document expected flow: `request → rag_pipeline → provider → formatter → response`

**Acceptance Test**: Runtime engine has Chapter 2 routing path with TODO markers for all runtime stages

---

## PHASE 3 — Chapter Content Source

**User Story**: US1 - Developer Wires Chapter 2 into Backend Runtime

**Test Strategy**: Can be tested by creating chunks file and verifying it's importable.

### Chapter 2 Chunks File

- [ ] [T011] [P1] [US1] Create `backend/app/content/chapters/chapter_2_chunks.py`:
  - Add module docstring: "Chapter 2 Content Chunks - Provides chapter content chunks for RAG pipeline"
  - Import statement: `from typing import List, Dict, Any`
  - Function definition: `def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:`
  - Function docstring explaining return structure (id, text, chapter_id, section_id, position, word_count, metadata)
  - TODO comments explaining future chunking implementation:
    - `# TODO: Implement chunking from Chapter 2 MDX content`
    - `# TODO: Load Chapter 2 content from frontend/docs/chapters/chapter-2.mdx`
    - `# TODO: Implement chunking strategy (same as Chapter 1)`
    - `# TODO: Extract metadata (section titles, positions, word counts)`
    - `# TODO: Generate unique chunk IDs (format: "ch2-s{section}-c{chunk}")`
    - `# TODO: Handle special content (glossary, diagrams, AI blocks)`
    - `# TODO: Cache chunks for performance`
    - `# TODO: Include ROS 2-specific metadata (concepts: nodes, topics, services, actions)`
  - Placeholder return: `return []  # Placeholder return - no real chunking implementation`

- [ ] [T012] [P1] [US1] Verify chapter_2_chunks.py is importable: Run `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; print('Import successful')"` - should complete without errors

- [ ] [T013] [P2] [US1] Verify chapter_2_chunks.py structure matches chapter_1_chunks.py:
  - Compare function signatures
  - Compare return type structure
  - Ensure parity in structure (same fields, same types)

**Acceptance Test**: chapter_2_chunks.py exists, is importable, and has placeholder function matching chapter_1_chunks structure

---

## PHASE 4 — Subagents

**User Story**: US1 - Developer Wires Chapter 2 into Backend Runtime

**Test Strategy**: Can be tested by creating subagent files and verifying they're importable.

### Subagent Scaffold Files

- [ ] [T014] [P1] [US1] Create `backend/app/ai/subagents/ch2_ask_question_agent.py`:
  - Add module docstring: "Chapter 2 Ask Question Agent"
  - Add TODO comment: `# TODO: blueprint for Chapter 2 version of the agent`
  - Add minimal docstring explaining purpose: "Placeholder for Chapter 2 ask question agent logic"

- [ ] [T015] [P1] [US1] Create `backend/app/ai/subagents/ch2_explain_el10_agent.py`:
  - Add module docstring: "Chapter 2 Explain Like I'm 10 Agent"
  - Add TODO comment: `# TODO: blueprint for Chapter 2 version of the agent`
  - Add minimal docstring explaining purpose: "Placeholder for Chapter 2 explain like 10 agent logic"

- [ ] [T016] [P1] [US1] Create `backend/app/ai/subagents/ch2_quiz_agent.py`:
  - Add module docstring: "Chapter 2 Quiz Agent"
  - Add TODO comment: `# TODO: blueprint for Chapter 2 version of the agent`
  - Add minimal docstring explaining purpose: "Placeholder for Chapter 2 quiz agent logic"

- [ ] [T017] [P1] [US1] Create `backend/app/ai/subagents/ch2_diagram_agent.py`:
  - Add module docstring: "Chapter 2 Diagram Agent"
  - Add TODO comment: `# TODO: blueprint for Chapter 2 version of the agent`
  - Add minimal docstring explaining purpose: "Placeholder for Chapter 2 diagram agent logic"

- [ ] [T018] [P1] [US1] Verify all 4 subagent files are importable: Run `cd backend && python -c "from app.ai.subagents.ch2_ask_question_agent import *; print('Import successful')"` for each file - should complete without errors

**Acceptance Test**: All 4 subagent files exist, are importable, and contain TODO placeholders

---

## PHASE 5 — Skills Layer

**User Story**: US1 - Developer Wires Chapter 2 into Backend Runtime

**Test Strategy**: Can be tested by updating skills files and verifying they still import correctly.

### Skills Layer Extensions

- [ ] [T019] [P1] [US1] Update `backend/app/ai/skills/retrieval_skill.py` with CH2 placeholder:
  - Add placeholder routing comment: `# TODO: Chapter 2 placeholder routing`
  - Add conditional comment: `# if chapterId == 2: # TODO`
  - Add comment: `# TODO: Add Chapter 2 handling path`
  - Keep logic empty (no implementation)

- [ ] [T020] [P1] [US1] Update `backend/app/ai/skills/prompt_builder_skill.py` with CH2 placeholder:
  - Add placeholder routing comment: `# TODO: Chapter 2 placeholder routing`
  - Add conditional comment: `# if chapterId == 2: # TODO`
  - Add comment: `# TODO: Add Chapter 2 handling path`
  - Keep logic empty (no implementation)

- [ ] [T021] [P1] [US1] Update `backend/app/ai/skills/formatting_skill.py` with CH2 placeholder:
  - Add placeholder routing comment: `# TODO: Chapter 2 placeholder routing`
  - Add conditional comment: `# if chapterId == 2: # TODO`
  - Add comment: `# TODO: Add Chapter 2 handling path`
  - Keep logic empty (no implementation)

- [ ] [T022] [P1] [US1] Verify skills files still import correctly: Run `cd backend && python -c "from app.ai.skills.retrieval_skill import *; print('Import successful')"` for each file - should complete without errors

**Acceptance Test**: All 3 skills files have Chapter 2 placeholder routing comments and still import correctly

---

## PHASE 6 — Contracts

**User Story**: US1 - Developer Wires Chapter 2 into Backend Runtime

**Test Strategy**: Can be tested by verifying contract file exists and documents flow sequence.

### Contract Documentation

- [ ] [T023] [P1] [US1] Verify `specs/024-ch2-runtime-wiring/contracts/runtime-flow.yaml` exists (already created in spec phase)

- [ ] [T024] [P1] [US1] Verify contract documents expected flow sequence:
  - API → Runtime Engine → Chapter 2 Subagent → Skills → Response
  - Document request flow: `request → rag_pipeline → provider → formatter → response`
  - Document Chapter 2-specific routing patterns

**Acceptance Test**: Contract file exists and documents expected runtime flow for Chapter 2

---

## PHASE 7 — Validation

**User Story**: US1 - Developer Wires Chapter 2 into Backend Runtime

**Test Strategy**: Can be tested by running backend import checks and startup tests.

### Backend Validation

- [ ] [T025] [P1] [VALIDATION] Run backend import check: Test all new modules are importable:
  - `from app.content.chapters.chapter_2_chunks import get_chapter_chunks`
  - `from app.ai.subagents.ch2_ask_question_agent import *`
  - `from app.ai.subagents.ch2_explain_el10_agent import *`
  - `from app.ai.subagents.ch2_quiz_agent import *`
  - `from app.ai.subagents.ch2_diagram_agent import *`
  - All imports should complete without errors

- [ ] [T026] [P1] [VALIDATION] Ensure uvicorn starts successfully: Run `cd backend && uvicorn app.main:app` - should start without import errors or runtime exceptions

- [ ] [T027] [P1] [VALIDATION] Verify no syntax errors: Check all new files for Python syntax errors - should have none

- [ ] [T028] [P1] [VALIDATION] Verify no circular imports: Check for circular import errors - should have none

**Acceptance Test**: 
- Backend starts successfully
- All new modules import correctly
- No syntax or import errors

---

## Task Summary

**Total Tasks**: 28 tasks
- **Phase 0 (Setup)**: 6 tasks
- **Phase 1 (API Layer)**: 2 tasks
- **Phase 2 (Runtime Engine)**: 2 tasks
- **Phase 3 (Chapter Content Source)**: 3 tasks
- **Phase 4 (Subagents)**: 5 tasks
- **Phase 5 (Skills Layer)**: 4 tasks
- **Phase 6 (Contracts)**: 2 tasks
- **Phase 7 (Validation)**: 4 tasks

**Priority Breakdown**:
- **P1 (Critical)**: 26 tasks
- **P2 (Important)**: 2 tasks
- **P3 (Nice-to-have)**: 0 tasks

**Estimated Time**: 45-60 minutes (scaffolding only, no backend logic)

---

## Dependencies

- **Dependency 1**: Feature 006 (AI Runtime Engine) - Required for runtime engine infrastructure
- **Dependency 2**: Feature 023 (Chapter 2 AI Block MDX Integration) - Required for frontend AI blocks
- **Dependency 3**: Chapter 1 chunks structure - Required as reference for chapter_2_chunks.py structure
- **Dependency 4**: Existing subagents - Required as reference for subagent structure
- **Dependency 5**: Skills layer - Required for skills extension

---

## Success Criteria

- ✅ API layer routes chapterId=2 to runtime engine
- ✅ Runtime engine has Chapter 2 routing placeholders
- ✅ chapter_2_chunks.py exists and is importable
- ✅ All 4 subagent files exist and are importable
- ✅ Skills layer has Chapter 2 placeholder routing
- ✅ Contract file documents runtime flow
- ✅ Backend starts without errors
- ✅ All imports resolve correctly

---

## Notes

- All tasks are scaffolding only (no real AI logic)
- All subagent files are empty scaffolds with TODO comments
- Skills extensions are comment-only (no logic)
- Backend must start and all modules must import correctly
- Follow Chapter 1 patterns for consistency

