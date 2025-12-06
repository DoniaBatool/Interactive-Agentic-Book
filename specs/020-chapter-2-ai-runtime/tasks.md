# Tasks: AI Runtime Engine Extension for Chapter 2

**Feature**: 020-chapter-2-ai-runtime | **Branch**: `020-chapter-2-ai-runtime` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for extending the AI Runtime Engine to support Chapter 2 content (scaffolding only, no real AI logic).

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

**Purpose**: Verify dependencies and prerequisites before implementing Chapter 2 runtime engine extension scaffolding.

- [ ] [T001] [P1] [SETUP] Verify Feature 005 is complete: Check that `backend/app/ai/runtime/engine.py` exists with runtime engine structure
- [ ] [T002] [P1] [SETUP] Verify Feature 012 is complete: Check that `backend/app/content/chapters/chapter_2_chunks.py` exists with `get_chapter_chunks()` function
- [ ] [T003] [P1] [SETUP] Verify Feature 013 is complete: Check that Chapter 2 subagents exist in `backend/app/ai/subagents/` (ch2_*.py files)
- [ ] [T004] [P1] [SETUP] Verify collections directory doesn't exist: Check that `backend/app/ai/rag/collections/` directory doesn't exist (to be created)
- [ ] [T005] [P1] [SETUP] Verify embedding client exists: Check that `backend/app/ai/embeddings/embedding_client.py` exists
- [ ] [T006] [P1] [SETUP] Verify skills exist: Check that `backend/app/ai/skills/retrieval_skill.py` and `prompt_builder_skill.py` exist
- [ ] [T007] [P1] [SETUP] Verify ChatKit exists: Check that `backend/app/ai/chatkit/session_manager.py` exists
- [ ] [T008] [P1] [SETUP] Verify settings exists: Check that `backend/app/config/settings.py` exists
- [ ] [T009] [P1] [SETUP] Verify .env.example exists: Check that `.env.example` file exists in project root
- [ ] [T010] [P1] [SETUP] Verify backend imports work: Run `cd backend && python -c "from app.main import app; print('Backend imports OK')"` - should complete without errors

**Success Criteria**:
- All prerequisite files exist
- Backend imports resolve without errors
- Ready to implement scaffolding

**Dependencies**: Feature 005 (AI Runtime Engine), Feature 012 (Chapter 2 RAG), Feature 013 (Chapter 2 Runtime Engine)

---

## PHASE A — RAG Infrastructure Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by creating RAG collection module and verifying imports work.

### Create Collections Directory

- [ ] [T011] [P1] [US1] Create `backend/app/ai/rag/collections/` directory:
  - Run: `New-Item -ItemType Directory -Path "backend\app\ai\rag\collections" -Force` (PowerShell)
  - Expected: Directory created successfully
  - Acceptance test: Directory exists at specified path

### Create Collections __init__.py

- [ ] [T012] [P1] [US1] Create `backend/app/ai/rag/collections/__init__.py`:
  - Add module docstring: `"""RAG collection modules for chapter-specific collections."""`
  - Add TODO comment: `# TODO: Import collection modules when implemented`
  - Add empty `__all__` list (commented out)
  - Expected content: Module initialization with docstring and TODO
  - Dependencies: None
  - Acceptance test: File exists and imports without errors

### Create ch2_collection.py

- [ ] [T013] [P1] [US1] Create `backend/app/ai/rag/collections/ch2_collection.py`:
  - Add module docstring: `"""RAG collection operations for Chapter 2."""`
  - Add constant: `CH2_COLLECTION_NAME = "chapter_2"`
  - Add function stub: `def create_collection() -> None:` with TODO comment
  - Add function stub: `def upsert_vectors(chunks: List[str], embeddings: List[List[float]]) -> None:` with TODO comment
  - Add function stub: `def search(query_embedding: List[float], top_k: int) -> List[Dict[str, Any]]:` with TODO comment
  - Expected content: Module with constant and 3 function stubs, all with TODO comments
  - Dependencies: `typing` module (List, Dict, Any)
  - Acceptance test: File exists, imports without errors, constant and functions are accessible

**Phase Completion**: RAG collection module created with TODO stubs, imports work

---

## PHASE B — Embedding Pipeline Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by updating embedding client and verifying imports work.

### Extend generate_embedding Function

- [ ] [T014] [P1] [US1] Update `backend/app/ai/embeddings/embedding_client.py` function `generate_embedding()`:
  - Add `chapter_id: int = 1` parameter to function signature
  - Add TODO comment: `# TODO: Add chapter_id parameter support for Chapter 2`
  - Add TODO comment: `# TODO: Use CH2_EMBEDDING_MODEL when chapter_id=2`
  - Expected content: Function signature updated with chapter_id parameter, TODO comments added
  - Dependencies: Existing `generate_embedding()` function from Feature 005
  - Acceptance test: Function signature updated, imports work, no syntax errors

### Add batch_embed_ch2 Function

- [ ] [T015] [P1] [US1] Add `batch_embed_ch2()` function to `backend/app/ai/embeddings/embedding_client.py`:
  - Add function stub: `def batch_embed_ch2(chunks: List[str]) -> List[List[float]]:`
  - Add docstring with input/output description
  - Add TODO comment: `# TODO: Implement batch embedding for Chapter 2 chunks`
  - Add TODO comment: `# TODO: Use CH2_EMBEDDING_MODEL for Chapter 2`
  - Add placeholder return: `return []`
  - Expected content: New function with TODO comments and placeholder return
  - Dependencies: `typing` module (List)
  - Acceptance test: Function exists, imports work, function is callable

**Phase Completion**: Embedding client extended with chapter=2 support, imports work

---

## PHASE C — Chapter Knowledge Source Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by verifying chapter_2_chunks.py exists and has correct structure.

### Verify chapter_2_chunks.py Exists

- [ ] [T016] [P1] [US1] Verify `backend/app/content/chapters/chapter_2_chunks.py` exists:
  - Run: `Test-Path backend/app/content/chapters/chapter_2_chunks.py` (PowerShell)
  - Expected: File exists
  - Dependencies: Feature 012 (Chapter 2 RAG)
  - Acceptance test: File exists at specified path

### Verify get_chapter_chunks Function

- [ ] [T017] [P1] [US1] Verify `get_chapter_chunks()` function exists in `backend/app/content/chapters/chapter_2_chunks.py`:
  - Check function signature: `def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:`
  - Check function is importable: `from app.content.chapters.chapter_2_chunks import get_chapter_chunks`
  - Expected content: Function exists with correct signature
  - Dependencies: Feature 012 (Chapter 2 RAG)
  - Acceptance test: Function exists, imports without errors, function is callable

### Add TODO Comments if Needed

- [ ] [T018] [P2] [US1] Add TODO comments to `backend/app/content/chapters/chapter_2_chunks.py` if function is placeholder:
  - Check if function returns empty list or placeholder
  - Add TODO comment: `# TODO: Implement chunking from Chapter 2 MDX content` (if not already present)
  - Expected content: TODO comments present if function is placeholder
  - Dependencies: Feature 012 (Chapter 2 RAG)
  - Acceptance test: TODO comments present if needed

**Phase Completion**: Chapter 2 knowledge source verified, ready for RAG integration

---

## PHASE D — Runtime Engine Extension Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by updating runtime engine and verifying imports work.

### Add Chapter 2 Routing Logic

- [ ] [T019] [P1] [US1] Update `backend/app/ai/runtime/engine.py` function `run_ai_block()`:
  - Add TODO comment block: `# TODO: Chapter 2 routing`
  - Add code: `chapter_id = request_data.get("chapterId", 1)`
  - Add conditional: `if chapter_id == 2:`
  - Add TODO: `#     # TODO: Check ENABLE_CHAPTER_2_RUNTIME flag`
  - Add TODO: `#     # TODO: Route to CH2 RAG via ch2_collection.py`
  - Add TODO: `#     # TODO: Call CH2 subagents`
  - Expected content: Chapter 2 routing logic with TODO comments
  - Dependencies: Existing `run_ai_block()` function from Feature 005
  - Acceptance test: Code added, imports work, no syntax errors

### Add Chapter 2 Handler Functions

- [ ] [T020] [P1] [US1] Add placeholder handler functions to `backend/app/ai/runtime/engine.py`:
  - Add function stub: `async def handle_ch2_ask_question(request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:` with TODO comment
  - Add function stub: `async def handle_ch2_explain_el10(request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:` with TODO comment
  - Add function stub: `async def handle_ch2_quiz(request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:` with TODO comment
  - Add function stub: `async def handle_ch2_diagram(request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:` with TODO comment
  - Expected content: 4 handler function stubs with TODO comments
  - Dependencies: `typing` module (Dict, Any)
  - Acceptance test: Functions exist, imports work, functions are callable

### Add Chapter 2 RAG Integration Comments

- [ ] [T021] [P1] [US1] Add Chapter 2 RAG integration comments to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Import ch2_collection for Chapter 2 RAG operations`
  - Add TODO comment: `# TODO: from app.ai.rag.collections.ch2_collection import CH2_COLLECTION_NAME, search`
  - Add TODO comment: `# TODO: Use CH2_COLLECTION_NAME when chapter_id=2`
  - Expected content: TODO comments for Chapter 2 RAG integration
  - Dependencies: ch2_collection.py (from Phase A)
  - Acceptance test: Comments added, no syntax errors

### Verify Engine Imports

- [ ] [T022] [P1] [US1] Verify `backend/app/ai/runtime/engine.py` imports correctly:
  - Run: `cd backend && python -c "from app.ai.runtime.engine import run_ai_block; print('Import successful')"`
  - Expected: Import succeeds without errors
  - Dependencies: All updated code in engine.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: Runtime engine extended with Chapter 2 routing, imports work

---

## PHASE E — Subagent Tasks (CH2)

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by verifying subagents exist or creating them with TODO stubs.

### Verify ch2_ask_question_agent.py

- [ ] [T023] [P1] [US1] Verify or create `backend/app/ai/subagents/ch2_ask_question_agent.py`:
  - Check if file exists (from Feature 013)
  - If exists: Verify function `ch2_ask_question_agent()` exists with input/output schema placeholders
  - If missing: Create file with function stub, input schema placeholder, output schema placeholder, TODO: orchestrate provider + RAG
  - Expected content: File exists with function stub and TODO comments
  - Dependencies: Feature 013 (may have created this file)
  - Acceptance test: File exists, function exists, imports work

### Verify ch2_el10_agent.py

- [ ] [T024] [P1] [US1] Verify or create `backend/app/ai/subagents/ch2_el10_agent.py`:
  - Check if file exists (from Feature 013)
  - If exists: Verify function `ch2_el10_agent()` exists with input/output schema placeholders
  - If missing: Create file with function stub, input schema placeholder, output schema placeholder, TODO: orchestrate provider + RAG
  - Expected content: File exists with function stub and TODO comments
  - Dependencies: Feature 013 (may have created this file)
  - Acceptance test: File exists, function exists, imports work

### Verify ch2_quiz_agent.py

- [ ] [T025] [P1] [US1] Verify or create `backend/app/ai/subagents/ch2_quiz_agent.py`:
  - Check if file exists (from Feature 013)
  - If exists: Verify function `ch2_quiz_agent()` exists with input/output schema placeholders
  - If missing: Create file with function stub, input schema placeholder, output schema placeholder, TODO: orchestrate provider + RAG
  - Expected content: File exists with function stub and TODO comments
  - Dependencies: Feature 013 (may have created this file)
  - Acceptance test: File exists, function exists, imports work

### Verify ch2_diagram_agent.py

- [ ] [T026] [P1] [US1] Verify or create `backend/app/ai/subagents/ch2_diagram_agent.py`:
  - Check if file exists (from Feature 013)
  - If exists: Verify function `ch2_diagram_agent()` exists with input/output schema placeholders
  - If missing: Create file with function stub, input schema placeholder, output schema placeholder, TODO: orchestrate provider + RAG
  - Expected content: File exists with function stub and TODO comments
  - Dependencies: Feature 013 (may have created this file)
  - Acceptance test: File exists, function exists, imports work

### Verify All Subagents Import

- [ ] [T027] [P1] [US1] Verify all Chapter 2 subagents import correctly:
  - Run: `cd backend && python -c "from app.ai.subagents.ch2_ask_question_agent import ch2_ask_question_agent; from app.ai.subagents.ch2_el10_agent import ch2_el10_agent; from app.ai.subagents.ch2_quiz_agent import ch2_quiz_agent; from app.ai.subagents.ch2_diagram_agent import ch2_diagram_agent; print('All imports successful')"`
  - Expected: All imports succeed without errors
  - Dependencies: All 4 subagent files exist
  - Acceptance test: All imports work, no syntax errors

**Phase Completion**: All Chapter 2 subagents exist with TODO stubs, imports work

---

## PHASE F — Skills Extension Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by updating skills files and verifying imports work.

### Extend retrieval_skill.py

- [ ] [T028] [P1] [US1] Update `backend/app/ai/skills/retrieval_skill.py` function `retrieve_content()`:
  - Add TODO comment: `# TODO: support CH2 collection name`
  - Add TODO comment: `# TODO: If chapter_id == 2, use CH2_COLLECTION_NAME from ch2_collection.py`
  - Add TODO comment: `# TODO: from app.ai.rag.collections.ch2_collection import CH2_COLLECTION_NAME`
  - Add TODO comment: `# TODO: Call RAG pipeline with Chapter 2 collection`
  - Expected content: TODO comments added for CH2 collection name support
  - Dependencies: Existing `retrieve_content()` function from Feature 005, ch2_collection.py (from Phase A)
  - Acceptance test: Comments added, imports work, no syntax errors

### Extend prompt_builder_skill.py

- [ ] [T029] [P1] [US1] Update `backend/app/ai/skills/prompt_builder_skill.py` function `build_prompt()`:
  - Add TODO comment: `# TODO: templates for CH2`
  - Add TODO comment: `# TODO: If chapter_id == 2, use ROS 2 prompt templates`
  - Add TODO comment: `# TODO: Include ROS 2 concepts, analogies, examples in prompts`
  - Add TODO comment: `# TODO: Format context with ROS 2-specific instructions`
  - Expected content: TODO comments added for CH2 templates
  - Dependencies: Existing `build_prompt()` function from Feature 005
  - Acceptance test: Comments added, imports work, no syntax errors

### Verify Skills Import

- [ ] [T030] [P1] [US1] Verify skills import correctly:
  - Run: `cd backend && python -c "from app.ai.skills.retrieval_skill import retrieve_content; from app.ai.skills.prompt_builder_skill import build_prompt; print('Import successful')"`
  - Expected: Imports succeed without errors
  - Dependencies: Updated skills files
  - Acceptance test: Imports work, no syntax errors

**Phase Completion**: Skills extended with CH2 TODOs, imports work

---

## PHASE G — ChatKit Extension Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by updating session manager and verifying imports work.

### Extend session_manager.py

- [ ] [T031] [P1] [US1] Update `backend/app/ai/chatkit/session_manager.py`:
  - Add TODO comment: `# TODO: Extend session_manager to track chapterId=2`
  - Add TODO comment to `create_session()` function: `# TODO: Support chapterId=2, track Chapter 2 sessions separately`
  - Add TODO comment: `# TODO: attach CH2 memory nodes`
  - Add TODO comment to `attach_memory_nodes()` function: `# TODO: If chapter_id == 2, attach CH2 memory nodes`
  - Expected content: TODO comments added for Chapter 2 session tracking
  - Dependencies: Existing `session_manager.py` from Feature 005
  - Acceptance test: Comments added, imports work, no syntax errors

### Verify ChatKit Import

- [ ] [T032] [P1] [US1] Verify ChatKit imports correctly:
  - Run: `cd backend && python -c "from app.ai.chatkit.session_manager import SessionManager; print('Import successful')"`
  - Expected: Import succeeds without errors
  - Dependencies: Updated session_manager.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: ChatKit extended with Chapter 2 TODOs, imports work

---

## PHASE H — Config + ENV Tasks

**User Story**: US2 - System Administrator Configures Chapter 2 Runtime Settings

**Test Strategy**: Can be tested by updating settings.py and .env.example and verifying backend can read them.

### Update settings.py

- [ ] [T033] [P1] [US2] Update `backend/app/config/settings.py` Settings class:
  - Add setting: `QDRANT_COLLECTION_CH2: Optional[str] = None`
  - Add setting: `CH2_EMBEDDING_MODEL: Optional[str] = None`
  - Add setting: `CH2_LLM_MODEL: Optional[str] = None`
  - Expected content: 3 new settings added to Settings class, all optional (default to None)
  - Dependencies: Existing Settings class from Feature 005
  - Acceptance test: Settings added, backend imports work, settings are accessible

### Update .env.example

- [ ] [T034] [P1] [US2] Update `.env.example` file:
  - Add variable: `QDRANT_COLLECTION_CH2="chapter_2"` with comment: `# Qdrant collection name for Chapter 2 RAG operations`
  - Add variable: `CH2_EMBEDDING_MODEL="text-embedding-3-small"` with comment: `# Embedding model for Chapter 2 (e.g., "text-embedding-3-small")`
  - Add variable: `CH2_LLM_MODEL="gpt-4o-mini"` with comment: `# LLM model for Chapter 2 (e.g., "gpt-4o-mini")`
  - Expected content: 3 new environment variables with descriptions
  - Dependencies: Existing .env.example file
  - Acceptance test: Variables added, file is readable, format is correct

### Verify Settings Load

- [ ] [T035] [P1] [US2] Verify settings load correctly:
  - Run: `cd backend && python -c "from app.config.settings import settings; print(f'QDRANT_COLLECTION_CH2: {settings.QDRANT_COLLECTION_CH2}'); print(f'CH2_EMBEDDING_MODEL: {settings.CH2_EMBEDDING_MODEL}'); print(f'CH2_LLM_MODEL: {settings.CH2_LLM_MODEL}'); print('Settings load OK')"`
  - Expected: Settings load without errors (values may be None)
  - Dependencies: Updated settings.py
  - Acceptance test: Settings load, no errors, values accessible

**Phase Completion**: Configuration updated with Chapter 2 settings, settings load correctly

---

## PHASE I — API Routing Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by verifying ai_blocks.py routes chapterId=2 correctly.

### Verify ai_blocks.py Routes Chapter 2

- [ ] [T036] [P1] [US1] Verify `backend/app/api/ai_blocks.py` routes chapterId=2 correctly:
  - Check module docstring mentions Chapter 2 support
  - Check all endpoints accept `chapterId` parameter
  - Check all endpoints call `run_ai_block(block_type, request_data)` with chapterId included
  - Expected content: API routes chapterId=2 to runtime engine
  - Dependencies: Existing ai_blocks.py from Feature 005
  - Acceptance test: API routes correctly, no special handling needed

### Add Chapter 2 Routing Comment

- [ ] [T037] [P1] [US1] Add Chapter 2 routing comment to `backend/app/api/ai_blocks.py`:
  - Add comment: `# TODO: For chapterId=2, all block types route to run_ai_block(block_type, chapter_id=2)`
  - Add comment: `# Runtime engine will handle Chapter 2 routing internally`
  - Expected content: Comments added documenting Chapter 2 routing
  - Dependencies: Existing ai_blocks.py
  - Acceptance test: Comments added, no syntax errors

### Verify API Imports

- [ ] [T038] [P1] [US1] Verify `backend/app/api/ai_blocks.py` imports correctly:
  - Run: `cd backend && python -c "from app.api.ai_blocks import router; print('Import successful')"`
  - Expected: Import succeeds without errors
  - Dependencies: Updated ai_blocks.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: API routing verified, Chapter 2 routes correctly to runtime engine

---

## PHASE J — Validation Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by verifying all files exist, imports work, and backend starts.

### Verify All Files Exist

- [ ] [T039] [P1] [US1] Verify all new files exist:
  - Check `backend/app/ai/rag/collections/ch2_collection.py` exists
  - Check `backend/app/ai/rag/collections/__init__.py` exists
  - Check all 4 Chapter 2 subagent files exist
  - Expected: All files exist at specified paths
  - Dependencies: All previous phases
  - Acceptance test: All files exist

### Verify All Imports Resolve

- [ ] [T040] [P1] [US1] Verify all imports resolve without errors:
  - Test ch2_collection.py import: `from app.ai.rag.collections.ch2_collection import CH2_COLLECTION_NAME`
  - Test embedding_client.py import: `from app.ai.embeddings.embedding_client import generate_embedding, batch_embed_ch2`
  - Test runtime engine import: `from app.ai.runtime.engine import run_ai_block`
  - Test subagents import: All 4 ch2_* subagents
  - Test skills import: `from app.ai.skills.retrieval_skill import retrieve_content`
  - Test ChatKit import: `from app.ai.chatkit.session_manager import SessionManager`
  - Test settings import: `from app.config.settings import settings`
  - Expected: All imports succeed without errors
  - Dependencies: All updated files
  - Acceptance test: All imports work, no circular dependencies

### Verify Backend Starts

- [ ] [T041] [P1] [US1] Verify backend starts successfully:
  - Run: `cd backend && python -c "from app.main import app; print('Backend starts OK')"`
  - Expected: Backend starts without import errors or runtime exceptions
  - Dependencies: All updated files
  - Acceptance test: Backend starts, no errors

### Verify No Breaking Changes

- [ ] [T042] [P1] [US1] Verify no breaking changes to Chapter 1 functionality:
  - Test Chapter 1 imports still work: `from app.ai.runtime.engine import run_ai_block`
  - Test Chapter 1 subagents still work: `from app.ai.subagents.ask_question_agent import ask_question_agent`
  - Expected: Chapter 1 functionality remains unchanged
  - Dependencies: All updated files
  - Acceptance test: Chapter 1 imports work, no breaking changes

**Phase Completion**: All validations pass, backend starts, no breaking changes

---

## PHASE K — Contract + Checklist Generation Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by verifying contract files exist from spec phase.

### Verify Contract Files Exist

- [ ] [T043] [P1] [US1] Verify contract files exist from spec phase:
  - Check `specs/020-chapter-2-ai-runtime/contracts/runtime-extension.yaml` exists
  - Check `specs/020-chapter-2-ai-runtime/checklists/requirements.md` exists
  - Expected: Contract files exist from spec phase
  - Dependencies: Feature 020 spec phase
  - Acceptance test: Contract files exist

### Verify Checklist Files Exist

- [ ] [T044] [P1] [US1] Verify checklist files exist from spec phase:
  - Check `specs/020-chapter-2-ai-runtime/checklists/requirements.md` exists
  - Expected: Checklist files exist from spec phase
  - Dependencies: Feature 020 spec phase
  - Acceptance test: Checklist files exist

**Phase Completion**: Contract and checklist files verified (already created in spec phase)

---

## Summary

**Total Tasks**: 44 tasks across 11 phases

**Phases**:
1. Phase 0: Setup & Prerequisites (10 tasks)
2. Phase A: RAG Infrastructure Tasks (3 tasks)
3. Phase B: Embedding Pipeline Tasks (2 tasks)
4. Phase C: Chapter Knowledge Source Tasks (3 tasks)
5. Phase D: Runtime Engine Extension Tasks (4 tasks)
6. Phase E: Subagent Tasks (CH2) (5 tasks)
7. Phase F: Skills Extension Tasks (3 tasks)
8. Phase G: ChatKit Extension Tasks (2 tasks)
9. Phase H: Config + ENV Tasks (3 tasks)
10. Phase I: API Routing Tasks (3 tasks)
11. Phase J: Validation Tasks (4 tasks)
12. Phase K: Contract + Checklist Generation Tasks (2 tasks)

**Priority Distribution**:
- P1 (Critical): 44 tasks
- P2 (Important): 0 tasks
- P3 (Nice-to-have): 0 tasks

**Dependencies**:
- Feature 005 (AI Runtime Engine) - must be complete
- Feature 012 (Chapter 2 RAG) - must be complete
- Feature 013 (Chapter 2 Runtime Engine) - may have created subagents (verify)

**Success Criteria**:
- All P1 tasks completed
- All files exist at specified paths
- All imports resolve without errors
- Backend starts successfully
- No breaking changes to Chapter 1 functionality
- All TODO placeholders are descriptive and actionable

---

Tasks complete — ready for /sp.implement.
