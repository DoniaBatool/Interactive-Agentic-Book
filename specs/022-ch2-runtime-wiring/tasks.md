# Tasks: Chapter 2 — RAG Pipeline Wiring, Runtime Routing & AI Block Integration

**Feature**: 022-ch2-runtime-wiring | **Branch**: `022-ch2-runtime-wiring` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for wiring Chapter 2 into the AI Runtime Engine (scaffolding only, no real RAG, routing, or AI logic).

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

**Purpose**: Verify dependencies and prerequisites before implementing Chapter 2 runtime wiring scaffolding.

- [ ] [T001] [P1] [SETUP] Verify Feature 005 is complete: Check that `backend/app/ai/runtime/engine.py` exists with `run_ai_block()` function
- [ ] [T002] [P1] [SETUP] Verify Feature 012 is complete: Check that `backend/app/ai/rag/collections/ch2_collection.py` exists with `CH2_COLLECTION_NAME` constant
- [ ] [T003] [P1] [SETUP] Verify Feature 013 is complete: Check that Chapter 2 subagents exist (`ch2_ask_question_agent.py`, `ch2_explain_el10_agent.py`, `ch2_quiz_agent.py`, `ch2_diagram_agent.py`)
- [ ] [T004] [P1] [SETUP] Verify Feature 020 is complete: Check that Chapter 2 AI Runtime Extension scaffolding exists
- [ ] [T005] [P1] [SETUP] Verify Feature 021 is complete: Check that `backend/app/content/chapters/chapter_2_chunks.py` exists with `get_chapter_chunks()` function
- [ ] [T006] [P1] [SETUP] Verify contract file exists: Check that `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml` exists (from spec phase)
- [ ] [T007] [P1] [SETUP] Verify backend imports work: Run `cd backend && python -c "from app.ai.runtime.engine import run_ai_block; print('Import successful')"` - should complete without errors
- [ ] [T008] [P1] [SETUP] Verify backend starts: Run `cd backend && python -c "from app.main import app; print('Backend starts OK')"` - should complete without errors

**Success Criteria**:
- All prerequisite files exist
- Backend imports resolve without errors
- Backend starts without errors
- Ready to implement scaffolding

**Dependencies**: Feature 005 (AI Runtime Engine), Feature 012 (Chapter 2 RAG Collection), Feature 013 (Chapter 2 Subagents), Feature 020 (Chapter 2 AI Runtime Extension), Feature 021 (Chapter 2 RAG Preparation)

---

## PHASE A — BACKEND: RAG Pipeline

**User Story**: US1 - Developer Wires Chapter 2 into Runtime Engine

**Test Strategy**: Can be tested by verifying function stubs exist and imports resolve successfully.

### Add Chapter 2 Collection Name Constant

- [ ] [T009] [P1] [US1] Add `CHAPTER_2_COLLECTION_NAME` constant to `backend/app/ai/rag/pipeline.py`:
  - Location: Top of file, after imports, before function definitions
  - Option 1: Import from ch2_collection.py: `from app.ai.rag.collections.ch2_collection import CH2_COLLECTION_NAME`
  - Option 2: Define locally: `CHAPTER_2_COLLECTION_NAME = "chapter_2"  # From QDRANT_COLLECTION_CH2 env var`
  - Expected content: Constant defined or imported
  - Dependencies: Feature 012 (Chapter 2 RAG Collection)
  - Acceptance test: Constant exists, can be referenced in functions

### Add Embed Chapter 2 Function Stub

- [ ] [T010] [P1] [US1] Add `embed_chapter_2()` function stub to `backend/app/ai/rag/pipeline.py`:
  - Location: After `run_rag_pipeline()` function
  - Function signature: `async def embed_chapter_2() -> None:`
  - Docstring: Describe embedding batch for Chapter 2 chunks
  - TODO comments: Implement embedding batch processing, implement Qdrant upsert operations, use batch_embed_ch2() from embedding_client.py
  - Expected content: Function stub with TODO comments, no implementation
  - Dependencies: Feature 012 (Chapter 2 RAG Collection)
  - Acceptance test: Function exists, imports resolve, no syntax errors

### Add Retrieve Chapter 2 Relevant Chunks Function Stub

- [ ] [T011] [P1] [US1] Add `retrieve_chapter_2_relevant_chunks()` function stub to `backend/app/ai/rag/pipeline.py`:
  - Location: After `embed_chapter_2()` function
  - Function signature: `async def retrieve_chapter_2_relevant_chunks(query: str, top_k: int = 5) -> List[Dict[str, Any]]:`
  - Docstring: Describe semantic search for Chapter 2
  - TODO comments: Implement query embedding, implement Qdrant similarity search, use search() from ch2_collection.py
  - Expected content: Function stub with TODO comments, returns empty list
  - Dependencies: Feature 012 (Chapter 2 RAG Collection)
  - Acceptance test: Function exists, imports resolve, no syntax errors

### Add Build Context for Chapter 2 Function Stub

- [ ] [T012] [P1] [US1] Add `build_context_for_ch2()` function stub to `backend/app/ai/rag/pipeline.py`:
  - Location: After `retrieve_chapter_2_relevant_chunks()` function
  - Function signature: `async def build_context_for_ch2(query: str) -> Dict[str, Any]:`
  - Docstring: Describe context assembly for Chapter 2
  - TODO comments: Implement context assembly, implement context formatting, include chunk metadata
  - Expected content: Function stub with TODO comments, returns empty context dictionary
  - Dependencies: Feature 012 (Chapter 2 RAG Collection)
  - Acceptance test: Function exists, imports resolve, no syntax errors

### Validate RAG Pipeline Imports

- [ ] [T013] [P1] [VALIDATION] Validate RAG pipeline imports in `backend/app/ai/rag/pipeline.py`:
  - Run: `cd backend && python -c "from app.ai.rag.pipeline import embed_chapter_2, retrieve_chapter_2_relevant_chunks, build_context_for_ch2; print('Imports successful')"`
  - Expected: All three functions import successfully
  - Dependencies: Tasks T009-T012
  - Acceptance test: All imports resolve without errors

---

## PHASE B — BACKEND: Runtime Engine

**User Story**: US1 - Developer Wires Chapter 2 into Runtime Engine

**Test Strategy**: Can be tested by verifying chapter_id=2 handling path exists and imports resolve successfully.

### Update Engine with Chapter 2 Routing

- [ ] [T014] [P1] [US1] Update `backend/app/ai/runtime/engine.py` with chapter_id=2 handling path:
  - Location: Inside `run_ai_block()` function, after chapter_id extraction
  - Add: `if chapter_id == 2:` branch (if not already exists)
  - Expected content: chapter_id=2 branch exists with pass statement
  - Dependencies: Feature 005 (AI Runtime Engine)
  - Acceptance test: chapter_id=2 branch exists in run_ai_block() function

### Add TODO: Call Chapter 2 RAG Pipeline

- [ ] [T015] [P1] [US1] Add TODO comments for calling Chapter 2 RAG pipeline in `backend/app/ai/runtime/engine.py`:
  - Location: Inside chapter_id=2 branch in `run_ai_block()` function
  - TODO comments:
    - Import build_context_for_ch2 from pipeline
    - Extract query from request_data
    - Call build_context_for_ch2(query) to get context
    - Use context for subagent processing
  - Expected content: TODO comments describing RAG pipeline call
  - Dependencies: Task T012 (build_context_for_ch2 function)
  - Acceptance test: TODO comments exist, clearly describe RAG pipeline integration

### Add TODO: Provider Selection

- [ ] [T016] [P1] [US1] Add TODO comments for provider selection for Chapter 2 in `backend/app/ai/runtime/engine.py`:
  - Location: Inside chapter_id=2 branch in `run_ai_block()` function
  - TODO comments:
    - Select LLM provider based on CH2_LLM_MODEL setting
    - Import settings from app.config.settings
    - Use provider for Chapter 2 LLM calls
  - Expected content: TODO comments describing provider selection
  - Dependencies: Feature 020 (Chapter 2 AI Runtime Extension - settings)
  - Acceptance test: TODO comments exist, clearly describe provider selection

### Add TODO: Context Generation

- [ ] [T017] [P1] [US1] Add TODO comments for context merging/generation for Chapter 2 in `backend/app/ai/runtime/engine.py`:
  - Location: Inside chapter_id=2 branch in `run_ai_block()` function
  - TODO comments:
    - Merge RAG context with request_data for subagent processing
    - Combine context dictionary with request payload
    - Pass merged context to Chapter 2 subagent
  - Expected content: TODO comments describing context merging
  - Dependencies: Task T015 (RAG pipeline call)
  - Acceptance test: TODO comments exist, clearly describe context merging

---

## PHASE C — BACKEND: AI Block Routing

**User Story**: US2 - System Integrates Chapter 2 AI Blocks

**Test Strategy**: Can be tested by verifying all endpoints can accept chapterId=2 and route to runtime engine.

### Modify AI Blocks to Support Chapter 2

- [ ] [T018] [P1] [US2] Modify `backend/app/api/ai_blocks.py` to support chapter_id=2:
  - Verify all 4 endpoints (ask-question, explain-like-10, quiz, diagram) accept chapterId parameter
  - Verify all endpoints route to runtime engine with chapterId in request_data
  - Expected content: All endpoints support chapterId parameter
  - Dependencies: Feature 005 (AI Runtime Engine)
  - Acceptance test: All endpoints can accept chapterId=2, route to runtime engine

### Add Chapter ID=2 Support

- [ ] [T019] [P1] [US2] Add chapter_id=2 support verification in `backend/app/api/ai_blocks.py`:
  - Verify AskQuestionRequest has optional chapterId parameter
  - Verify ExplainLike10Request has optional chapterId parameter
  - Verify QuizRequest has required chapterId parameter
  - Verify DiagramRequest has optional chapterId parameter
  - Expected content: All request models support chapterId
  - Dependencies: Feature 005 (AI Runtime Engine)
  - Acceptance test: All request models include chapterId parameter

### Add TODO: Load Chapter 2 Context

- [ ] [T020] [P1] [US2] Add TODO comments for loading Chapter 2 context in `backend/app/api/ai_blocks.py`:
  - Location: In each of the 4 endpoint functions (ask_question, explain_like_10, quiz, diagram)
  - TODO comments:
    - Load Chapter 2 context if chapterId=2
    - Import build_context_for_ch2 from pipeline
    - Call build_context_for_ch2 with appropriate query
    - Pass context to runtime engine
  - Expected content: TODO comments in all 4 endpoints
  - Dependencies: Task T012 (build_context_for_ch2 function)
  - Acceptance test: TODO comments exist in all 4 endpoints

---

## PHASE D — BACKEND: Subagents

**User Story**: US1 - Developer Wires Chapter 2 into Runtime Engine

**Test Strategy**: Can be tested by verifying all subagents have Chapter 2 handling path TODO comments.

### Add Chapter 2 TODO Branch in Ask Question Agent

- [ ] [T021] [P1] [US1] Add Chapter 2 handling path TODO comments to `backend/app/ai/subagents/ask_question_agent.py`:
  - Location: Inside ask_question_agent() function, add chapter_id=2 branch
  - TODO comments:
    - Chapter 2 handling path
    - Process Chapter 2 requests with ROS 2 context
    - Use Chapter 2 RAG context in prompts
    - Format Chapter 2 responses
    - Include ROS 2-specific knowledge (nodes, topics, services, actions)
  - Expected content: chapter_id=2 branch with TODO comments
  - Dependencies: Feature 013 (Chapter 2 Subagents)
  - Acceptance test: chapter_id=2 branch exists with TODO comments

### Add Chapter 2 TODO Branch in Explain EL10 Agent

- [ ] [T022] [P1] [US1] Add Chapter 2 handling path TODO comments to `backend/app/ai/subagents/explain_el10_agent.py`:
  - Location: Inside explain_el10_agent() function, add chapter_id=2 branch
  - TODO comments:
    - Chapter 2 handling path
    - Process Chapter 2 requests with ROS 2 context
    - Use Chapter 2 RAG context in prompts
    - Format Chapter 2 responses
    - Include ROS 2-specific analogies (post office, restaurant, phone calls)
  - Expected content: chapter_id=2 branch with TODO comments
  - Dependencies: Feature 013 (Chapter 2 Subagents)
  - Acceptance test: chapter_id=2 branch exists with TODO comments

### Add Chapter 2 TODO Branch in Quiz Agent

- [ ] [T023] [P1] [US1] Add Chapter 2 handling path TODO comments to `backend/app/ai/subagents/quiz_agent.py`:
  - Location: Inside quiz_agent() function, add chapter_id=2 branch
  - TODO comments:
    - Chapter 2 handling path
    - Process Chapter 2 requests with ROS 2 context
    - Use Chapter 2 RAG context in prompts
    - Format Chapter 2 responses
    - Generate ROS 2-specific quiz questions (nodes, topics, services, actions)
  - Expected content: chapter_id=2 branch with TODO comments
  - Dependencies: Feature 013 (Chapter 2 Subagents)
  - Acceptance test: chapter_id=2 branch exists with TODO comments

### Add Chapter 2 TODO Branch in Diagram Agent

- [ ] [T024] [P1] [US1] Add Chapter 2 handling path TODO comments to `backend/app/ai/subagents/diagram_agent.py`:
  - Location: Inside diagram_agent() function, add chapter_id=2 branch
  - TODO comments:
    - Chapter 2 handling path
    - Process Chapter 2 requests with ROS 2 context
    - Use Chapter 2 RAG context in prompts
    - Format Chapter 2 responses
    - Generate ROS 2-specific diagrams (node communication, topic pubsub, services/actions)
  - Expected content: chapter_id=2 branch with TODO comments
  - Dependencies: Feature 013 (Chapter 2 Subagents)
  - Acceptance test: chapter_id=2 branch exists with TODO comments

---

## PHASE E — BACKEND: Knowledge Source Module

**User Story**: US1 - Developer Wires Chapter 2 into Runtime Engine

**Test Strategy**: Can be tested by verifying structural metadata placeholders exist and imports resolve successfully.

### Update Chapter 2 Chunks with Structural TODOs

- [ ] [T025] [P1] [US1] Update `backend/app/content/chapters/chapter_2_chunks.py` with structural TODO comments:
  - Location: Top of file, after imports, before function definitions
  - Add structural metadata placeholders:
    - `chunk_count: int = 0  # TODO: Calculate chunk count from MDX content`
    - `expected_section_map: Dict[str, List[int]] = {}  # TODO: Build section map from MDX structure`
    - `embedding_ready: bool = False  # TODO: Set based on chunk availability`
  - Expected content: Three structural metadata placeholders with TODO comments
  - Dependencies: Feature 021 (Chapter 2 RAG Preparation)
  - Acceptance test: Structural metadata placeholders exist with TODO comments

### Add TODO for Chunk Count

- [ ] [T026] [P1] [US1] Add TODO comment for chunk_count in `backend/app/content/chapters/chapter_2_chunks.py`:
  - Location: After chunk_count placeholder
  - TODO comment: Calculate chunk count from MDX content, expected ~6-8 chunks based on chunk markers
  - Expected content: Descriptive TODO comment for chunk_count
  - Dependencies: Feature 021 (Chapter 2 RAG Preparation - chunk markers)
  - Acceptance test: TODO comment exists, clearly describes chunk count calculation

### Add TODO for Section Map

- [ ] [T027] [P1] [US1] Add TODO comment for expected_section_map in `backend/app/content/chapters/chapter_2_chunks.py`:
  - Location: After expected_section_map placeholder
  - TODO comment: Build section map from MDX structure, map section IDs to chunk ranges
  - Expected structure example in comment:
    ```python
    # {
    #     "introduction-to-ros2": [0, 1],
    #     "nodes-and-node-communication": [2, 3],
    #     ...
    # }
    ```
  - Expected content: Descriptive TODO comment with structure example
  - Dependencies: Feature 021 (Chapter 2 RAG Preparation - chunk markers)
  - Acceptance test: TODO comment exists with structure example

### Add TODO for Embedding Ready Flag

- [ ] [T028] [P1] [US1] Add TODO comment for embedding_ready flag in `backend/app/content/chapters/chapter_2_chunks.py`:
  - Location: After embedding_ready placeholder
  - TODO comment: Set based on chunk availability, set to True when chunks are extracted and ready for embedding
  - Expected content: Descriptive TODO comment for embedding_ready flag
  - Dependencies: Feature 021 (Chapter 2 RAG Preparation)
  - Acceptance test: TODO comment exists, clearly describes embedding readiness

---

## PHASE F — CONTRACTS

**User Story**: US1 - Developer Wires Chapter 2 into Runtime Engine

**Test Strategy**: Can be tested by verifying contract file exists and contains all required documentation.

### Verify Runtime Wiring Contract Exists

- [ ] [T029] [P1] [US1] Verify `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml` exists:
  - Check file exists at specified path
  - Expected: Contract file exists (created in spec phase)
  - Dependencies: Feature 022 spec phase
  - Acceptance test: Contract file exists and is readable

### Verify Flow Diagram Documentation

- [ ] [T030] [P1] [US1] Verify flow diagram documentation in `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml`:
  - Check Chapter Selection Flow Contract exists
  - Check flow diagram documents: API → Runtime Engine → RAG → Subagent → Response
  - Expected: Flow diagram documented in contract
  - Dependencies: Task T029 (contract file exists)
  - Acceptance test: Flow diagram documentation exists in contract

### Verify RAG → LLM Routing Rules Documentation

- [ ] [T031] [P1] [US1] Verify RAG → LLM routing rules documentation in `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml`:
  - Check RAG Pipeline Integration Contract exists
  - Check API-Level Routing Contract exists
  - Check Context-Building Contract exists
  - Check routing rules document: query → RAG pipeline → context → LLM → response
  - Expected: Routing rules documented in contract
  - Dependencies: Task T029 (contract file exists)
  - Acceptance test: Routing rules documentation exists in contract

---

## PHASE G — VALIDATION

**User Story**: VALIDATION - Ensure scaffolding is correct

**Test Strategy**: Can be tested by verifying backend starts, imports resolve, and no business logic is implemented.

### Validate Backend Starts Without Errors

- [ ] [T032] [P1] [VALIDATION] Validate backend starts without errors:
  - Run: `cd backend && python -c "from app.main import app; print('Backend starts OK')"`
  - Expected: Backend starts successfully, no import errors, no runtime exceptions
  - Dependencies: All previous tasks (T009-T031)
  - Acceptance test: Backend starts without errors

### Validate All Imports Resolve

- [ ] [T033] [P1] [VALIDATION] Validate all imports resolve successfully:
  - Test RAG pipeline imports: `python -c "from app.ai.rag.pipeline import embed_chapter_2, retrieve_chapter_2_relevant_chunks, build_context_for_ch2"`
  - Test runtime engine imports: `python -c "from app.ai.runtime.engine import run_ai_block"`
  - Test API endpoints imports: `python -c "from app.api.ai_blocks import router"`
  - Test subagent imports: `python -c "from app.ai.subagents.ask_question_agent import ask_question_agent"`
  - Test knowledge source imports: `python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks"`
  - Expected: All imports resolve without errors
  - Dependencies: All previous tasks (T009-T031)
  - Acceptance test: All imports resolve successfully

### Validate No Business Logic Implemented

- [ ] [T034] [P1] [VALIDATION] Validate no business logic is implemented (only scaffolding):
  - Review all modified files for TODO comments
  - Verify no actual RAG implementation (only function stubs)
  - Verify no actual routing implementation (only TODO comments)
  - Verify no actual subagent logic implementation (only TODO comments)
  - Expected: Only TODO comments and function stubs exist, no business logic
  - Dependencies: All previous tasks (T009-T031)
  - Acceptance test: No business logic implemented, only scaffolding

### Validate Runtime Engine Aware of Chapter 2

- [ ] [T035] [P1] [VALIDATION] Validate runtime engine is "aware" of Chapter 2:
  - Check `backend/app/ai/runtime/engine.py` for chapter_id=2 handling path
  - Verify TODO comments exist for Chapter 2 operations
  - Verify chapter_id=2 branch exists in `run_ai_block()` function
  - Expected: Runtime engine contains chapter_id=2 handling path with TODO comments
  - Dependencies: Tasks T014-T017 (runtime engine updates)
  - Acceptance test: Runtime engine contains chapter_id=2 handling path

---

## Summary

**Total Tasks**: 35 tasks across 7 phases

**Phase Breakdown**:
- Phase 0: Setup & Prerequisites (8 tasks)
- Phase A: BACKEND — RAG Pipeline (5 tasks)
- Phase B: BACKEND — Runtime Engine (4 tasks)
- Phase C: BACKEND — AI Block Routing (3 tasks)
- Phase D: BACKEND — Subagents (4 tasks)
- Phase E: BACKEND — Knowledge Source Module (4 tasks)
- Phase F: CONTRACTS (3 tasks)
- Phase G: VALIDATION (4 tasks)

**Priority Distribution**:
- P1 (Critical): 35 tasks
- P2 (Important): 0 tasks
- P3 (Nice-to-have): 0 tasks

**Dependencies**:
- Feature 005 (AI Runtime Engine): Required for runtime engine updates
- Feature 012 (Chapter 2 RAG Collection): Required for RAG pipeline updates
- Feature 013 (Chapter 2 Subagents): Required for subagent updates
- Feature 020 (Chapter 2 AI Runtime Extension): Required for settings and scaffolding
- Feature 021 (Chapter 2 RAG Preparation): Required for knowledge source updates

**Success Criteria**:
- All 35 tasks completed
- Backend starts without errors
- All imports resolve successfully
- Runtime engine aware of Chapter 2
- No business logic implemented (only scaffolding)

**Next Steps**: Run `/sp.implement` to implement scaffolding
