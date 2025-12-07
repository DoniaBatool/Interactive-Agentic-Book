# Tasks: System Integration Layer — Phase 1

**Feature**: 044-system-integration-phase-1 | **Branch**: `044-system-integration-phase-1` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating System Integration Layer (Phase 1) scaffolding. All tasks are placeholder-only—no real routing logic, RAG operations, provider selection, or API calls.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category`: ROUTER (Runtime router), REGISTRY (Runtime registry), PROVIDER (Provider selector), RAG (RAG integration), METADATA (Metadata integration), FRONTEND (Frontend client), VALIDATION (Validation), DOCS (Documentation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prepare for implementation.

- [ ] [T001] [P1] [SETUP] Verify Feature 001 (Base Project Initialization) is complete: Check that base project structure exists
- [ ] [T002] [P1] [SETUP] Verify Feature 003 (Chapter 1 Content) is complete: Check that chapter_1.py exists
- [ ] [T003] [P1] [SETUP] Verify Feature 032 (Chapter 2 Content) is complete: Check that chapter_2.py exists
- [ ] [T004] [P1] [SETUP] Verify Feature 037-038 (Chapter 3 Content) is complete: Check that chapter_3.py exists
- [ ] [T005] [P1] [SETUP] Verify Feature 005 (AI Runtime Engine) is complete: Check that engine.py exists
- [ ] [T006] [P1] [SETUP] Verify Feature 013 (Chapter 2 Runtime Engine) is complete: Check that Chapter 2 routing exists
- [ ] [T007] [P1] [SETUP] Verify Feature 040-041 (Chapter 3 RAG + Runtime Integration) is complete: Check that Chapter 3 routing exists

**Success Criteria**:
- All prerequisite features complete
- All required modules exist

**Dependencies**: Feature 001, 003, 032, 037-038, 005, 013, 040-041 must be complete

---

## PHASE 1 — RUNTIME ROUTER TASKS

**User Story**: US1 - System Integrates All Chapters

**Test Strategy**: Can be tested by verifying router.py exists with placeholder switch logic.

### Create Runtime Router

- [ ] [T008] [P1] [ROUTER] Create `backend/app/ai/runtime/router.py`: Create new file

- [ ] [T009] [P1] [ROUTER] Add route() function to `backend/app/ai/runtime/router.py`:
  - Function signature: `def route(chapter_id: int, block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]`
  - Import Dict, Any from typing
  - Placeholder switch logic for chapters 1, 2, 3
  - TODO comments for dynamic registry later
  - Placeholder return: empty dict

- [ ] [T010] [P1] [ROUTER] Add switch logic for Chapter 1 to `backend/app/ai/runtime/router.py`:
  - if chapter_id == 1: route to Chapter 1 runtime
  - TODO comment: Call runtime engine with chapter_id=1
  - Placeholder return: empty dict

- [ ] [T011] [P1] [ROUTER] Add switch logic for Chapter 2 to `backend/app/ai/runtime/router.py`:
  - elif chapter_id == 2: route to Chapter 2 runtime
  - TODO comment: Call runtime engine with chapter_id=2
  - Placeholder return: empty dict

- [ ] [T012] [P1] [ROUTER] Add switch logic for Chapter 3 to `backend/app/ai/runtime/router.py`:
  - elif chapter_id == 3: route to Chapter 3 runtime
  - TODO comment: Call runtime engine with chapter_id=3
  - Placeholder return: empty dict

- [ ] [T013] [P1] [ROUTER] Add default case to `backend/app/ai/runtime/router.py`:
  - else: handle unknown chapter
  - TODO comment: Return error or placeholder response
  - Placeholder return: empty dict

**Acceptance Test**: router.py exists, route() function has correct signature, switch logic for chapters 1-3

---

## PHASE 2 — REGISTRY TASKS

**User Story**: US1 - System Integrates All Chapters

**Test Strategy**: Can be tested by verifying registry.py exists with CHAPTER_RUNTIMES dictionary.

### Create Runtime Registry

- [ ] [T014] [P1] [REGISTRY] Create `backend/app/ai/runtime/registry.py`: Create new file

- [ ] [T015] [P1] [REGISTRY] Add CHAPTER_RUNTIMES dictionary to `backend/app/ai/runtime/registry.py`:
  - Dictionary with chapters 1, 2, 3
  - Structure: `CHAPTER_RUNTIMES = {1: "engine for Chapter 1", 2: "engine for Chapter 2", 3: "engine for Chapter 3"}`
  - Placeholder strings for runtime descriptions
  - TODO comments for runtime objects in Phase 2

**Acceptance Test**: registry.py exists, CHAPTER_RUNTIMES dictionary contains chapters 1-3

---

## PHASE 3 — PROVIDER SELECTOR TASKS

**User Story**: US1 - System Integrates All Chapters

**Test Strategy**: Can be tested by verifying base_llm.py updated with get_provider() factory function.

### Update Provider Base

- [ ] [T016] [P1] [PROVIDER] Update `backend/app/ai/providers/base_llm.py`:
  - Add get_provider() factory function
  - Function signature: `def get_provider(provider_name: str) -> BaseLLMProvider`
  - Import BaseLLMProvider from current module
  - TODO comments for provider selection logic
  - Placeholder return: None

- [ ] [T017] [P1] [PROVIDER] Add provider selection logic to `backend/app/ai/providers/base_llm.py`:
  - if provider_name == "openai": TODO return OpenAIProvider()
  - elif provider_name == "gemini": TODO return GeminiProvider()
  - else: TODO return DefaultProvider()
  - Placeholder return: None

**Acceptance Test**: base_llm.py updated, get_provider() function exists with correct signature

---

## PHASE 4 — RAG INTEGRATION TASKS

**User Story**: US1 - System Integrates All Chapters

**Test Strategy**: Can be tested by verifying unified_rag.py exists with placeholder functions.

### Create Unified RAG Layer

- [ ] [T018] [P1] [RAG] Create `backend/app/ai/rag/unified_rag.py`: Create new file

- [ ] [T019] [P1] [RAG] Add get_embeddings_for_chapter() function to `backend/app/ai/rag/unified_rag.py`:
  - Function signature: `def get_embeddings_for_chapter(chapter_id: int) -> List[List[float]]`
  - Import List from typing
  - TODO comments for Qdrant pipeline connection
  - Placeholder return: empty list

- [ ] [T020] [P1] [RAG] Add retrieve_context() function to `backend/app/ai/rag/unified_rag.py`:
  - Function signature: `def retrieve_context(chapter_id: int, query: str) -> Dict[str, Any]`
  - Import Dict, Any from typing
  - TODO comments for Qdrant pipeline connection
  - Placeholder return: empty dict

**Acceptance Test**: unified_rag.py exists, both functions have correct signatures

---

## PHASE 5 — METADATA INTEGRATION TASKS

**User Story**: US1 - System Integrates All Chapters

**Test Strategy**: Can be tested by verifying chapters/registry.py exists with metadata registration.

### Create Chapter Metadata Registry

- [ ] [T021] [P1] [METADATA] Create `backend/app/content/chapters/registry.py`: Create new file

- [ ] [T022] [P1] [METADATA] Import chapter metadata modules to `backend/app/content/chapters/registry.py`:
  - Import chapter_1 from app.content.chapters.chapter_1
  - Import chapter_2 from app.content.chapters.chapter_2
  - Import chapter_3 from app.content.chapters.chapter_3

- [ ] [T023] [P1] [METADATA] Add CHAPTER_METADATA_REGISTRY dictionary to `backend/app/content/chapters/registry.py`:
  - Dictionary with chapters 1, 2, 3
  - Structure: `CHAPTER_METADATA_REGISTRY = {1: chapter_1.CHAPTER_METADATA, 2: chapter_2.CHAPTER_METADATA, 3: chapter_3.CHAPTER_METADATA}`

- [ ] [T024] [P1] [METADATA] Add get_chapter_metadata() function to `backend/app/content/chapters/registry.py`:
  - Function signature: `def get_chapter_metadata(id: int) -> Dict[str, Any]`
  - Import Dict, Any from typing
  - TODO comments for metadata retrieval
  - Placeholder return: empty dict or registry lookup

**Acceptance Test**: registry.py exists, CHAPTER_METADATA_REGISTRY contains chapters 1-3, get_chapter_metadata() function exists

---

## PHASE 6 — FRONTEND RUNTIME CLIENT TASKS

**User Story**: US1 - System Integrates All Chapters

**Test Strategy**: Can be tested by verifying runtime-client.ts exists with placeholder functions.

### Create Frontend Runtime Client

- [ ] [T025] [P1] [FRONTEND] Create `frontend/src/integration/runtime-client.ts`: Create new file

- [ ] [T026] [P1] [FRONTEND] Add callAIBlock() function to `frontend/src/integration/runtime-client.ts`:
  - Function signature: `export async function callAIBlock(type: string, payload: any): Promise<any>`
  - TODO comments for backend API connection
  - Placeholder return: Promise.resolve({})

- [ ] [T027] [P1] [FRONTEND] Add callChapterRuntime() function to `frontend/src/integration/runtime-client.ts`:
  - Function signature: `export async function callChapterRuntime(id: number, data: any): Promise<any>`
  - TODO comments for backend API connection
  - Placeholder return: Promise.resolve({})

**Acceptance Test**: runtime-client.ts exists, both functions have correct signatures, TypeScript compiles

---

## PHASE 7 — API ROUTING UPDATE TASKS

**User Story**: US1 - System Integrates All Chapters

**Test Strategy**: Can be tested by verifying ai_blocks.py updated to route to central runtime router.

### Update AI Blocks API

- [ ] [T028] [P1] [ROUTER] Update `backend/app/api/ai_blocks.py`:
  - Import route from app.ai.runtime.router
  - Update ask_question endpoint to call router.route()
  - Placeholder flow only (no real logic)
  - Ensure existing functionality not broken

- [ ] [T029] [P1] [ROUTER] Update explain_like_10 endpoint in `backend/app/api/ai_blocks.py`:
  - Call router.route() with chapter_id and block_type
  - Placeholder flow only (no real logic)
  - Ensure existing functionality not broken

- [ ] [T030] [P1] [ROUTER] Update quiz endpoint in `backend/app/api/ai_blocks.py`:
  - Call router.route() with chapter_id and block_type
  - Placeholder flow only (no real logic)
  - Ensure existing functionality not broken

- [ ] [T031] [P1] [ROUTER] Update diagram endpoint in `backend/app/api/ai_blocks.py`:
  - Call router.route() with chapter_id and block_type
  - Placeholder flow only (no real logic)
  - Ensure existing functionality not broken

**Acceptance Test**: ai_blocks.py updated, all endpoints route to router, backend starts without errors

---

## PHASE 8 — SETTINGS LAYER TASKS

**User Story**: US1 - System Integrates All Chapters

**Test Strategy**: Can be tested by verifying settings.py updated with default runtime model settings.

### Update Settings

- [ ] [T032] [P1] [SETTINGS] Update `backend/app/config/settings.py`:
  - Add PROVIDER_DEFAULTS dictionary (placeholder)
  - Add default runtime model settings
  - Ensure environment variable fallback works
  - No breaking changes to existing settings

**Acceptance Test**: settings.py updated, PROVIDER_DEFAULTS dictionary exists, no breaking changes

---

## PHASE 9 — VALIDATION TASKS

**User Story**: US1, US2 - System Integration Validation

**Test Strategy**: Can be tested by verifying backend starts without import errors and all modules exist.

### Validate Integration

- [ ] [T033] [P1] [VALIDATION] Validate backend starts without import errors: Run backend startup test
- [ ] [T034] [P1] [VALIDATION] Validate all integration modules exist: Check file existence
- [ ] [T035] [P1] [VALIDATION] Validate no circular imports: Check import graph
- [ ] [T036] [P1] [VALIDATION] Validate routing placeholders connect: Check function calls
- [ ] [T037] [P1] [VALIDATION] Validate runtime registry references chapters 1-3: Check registry dictionary
- [ ] [T038] [P1] [VALIDATION] Validate no breaking changes: Test existing features

**Acceptance Test**: All validation checks pass

---

## PHASE 10 — DOCUMENTATION TASKS

**User Story**: US2 - Developer Understands System Dependencies

**Test Strategy**: Can be tested by verifying dependency-map.md exists with complete documentation.

### Create Dependency Map

- [ ] [T039] [P1] [DOCS] Verify `specs/044-system-integration-phase-1/contracts/dependency-map.md` exists: Check file exists (already created in spec phase)

**Acceptance Test**: dependency-map.md exists with complete dependency documentation

---

## Summary

**Total Tasks**: 39 tasks across 10 phases
**Estimated Time**: 30-40 minutes (integration scaffolding only, no real logic)
**Complexity**: Medium (multiple integration points, dependency management)

**Success Criteria**:
- ✅ All integration modules exist at specified paths
- ✅ Backend starts without import errors
- ✅ All routing placeholders connect correctly
- ✅ Runtime registry properly references chapters 1–3
- ✅ No real logic implemented (scaffolding only)
- ✅ No breaking changes to existing features

**Next Steps**: Proceed to `/sp.implement` to execute all tasks in order.

