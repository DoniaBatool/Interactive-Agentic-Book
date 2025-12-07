# Quickstart Guide: System Integration Layer — Phase 1

**Feature**: 044-system-integration-phase-1
**Branch**: `044-system-integration-phase-1`
**Estimated Time**: 30-40 minutes (integration scaffolding only, no real logic)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 001 (Base Project Initialization) completed
- [x] Feature 003 (Chapter 1 Content) completed
- [x] Feature 032 (Chapter 2 Content) completed
- [x] Feature 037 (Chapter 3 Content Specification) completed
- [x] Feature 038 (Chapter 3 MDX Implementation) completed
- [x] Feature 005 (AI Runtime Engine) completed
- [x] Feature 013 (Chapter 2 Runtime Engine) completed
- [x] Feature 040 (Chapter 3 RAG + Runtime Integration) completed
- [x] Feature 041 (Chapter 3 Subagents + Skills) completed
- [x] Git branch `044-system-integration-phase-1` checked out
- [x] Read `specs/044-system-integration-phase-1/spec.md`
- [x] Read existing runtime engine code (`backend/app/ai/runtime/engine.py`)

## Implementation Overview

**Total Steps**: 6 phases
**Primary Deliverable**: Unified system integration layer for Chapters 1-3
**Validation**: All modules exist, imports resolve, backend starts without errors

---

## Phase 1: Runtime Router & Registry (10 minutes)

### Step 1.1: Create runtime router

**File**: `backend/app/ai/runtime/router.py`

**Action**: Create file with placeholder route() function:
- Function signature: `def route(chapter_id: int, block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]`
- Placeholder switch logic for chapters 1, 2, 3
- TODO comments for dynamic registry later
- Placeholder return: empty dict

### Step 1.2: Create runtime registry

**File**: `backend/app/ai/runtime/registry.py`

**Action**: Create file with CHAPTER_RUNTIMES dictionary:
- Dictionary with chapters 1, 2, 3
- Placeholder strings for runtime descriptions
- TODO comments for runtime objects in Phase 2

**Validation**: Files exist, imports resolve

---

## Phase 2: API Routing Update (5 minutes)

### Step 2.1: Update ai_blocks.py

**File**: `backend/app/api/ai_blocks.py`

**Action**: Update endpoints to route to central runtime router:
- Import router from `app.ai.runtime.router`
- Update endpoints to call router.route()
- Placeholder flow only (no real logic)
- Ensure existing functionality not broken

**Validation**: Backend starts without errors

---

## Phase 3: Unified RAG & Provider (10 minutes)

### Step 3.1: Create unified RAG layer

**File**: `backend/app/ai/rag/unified_rag.py`

**Action**: Create file with placeholder functions:
- `get_embeddings_for_chapter(chapter_id: int) -> List[List[float]]`
- `retrieve_context(chapter_id: int, query: str) -> Dict[str, Any]`
- TODO comments for Qdrant pipeline connection
- Placeholder returns

### Step 3.2: Update provider base

**File**: `backend/app/ai/providers/base_llm.py`

**Action**: Add get_provider() factory function:
- Function signature: `def get_provider(provider_name: str) -> BaseLLMProvider`
- TODO comments for provider selection
- Placeholder return: None

**Validation**: Files exist, imports resolve

---

## Phase 4: Settings & Metadata (5 minutes)

### Step 4.1: Update settings.py

**File**: `backend/app/config/settings.py`

**Action**: Add default runtime model settings:
- Add PROVIDER_DEFAULTS dictionary (placeholder)
- Add default runtime model settings
- Ensure environment variable fallback works
- No breaking changes to existing settings

### Step 4.2: Create chapter metadata registry

**File**: `backend/app/content/chapters/registry.py`

**Action**: Create file with metadata registration:
- Import chapter metadata modules (chapter_1, chapter_2, chapter_3)
- Create CHAPTER_METADATA_REGISTRY dictionary
- Add get_chapter_metadata(id: int) function (placeholder)
- TODO comments for metadata retrieval

**Validation**: Files exist, imports resolve

---

## Phase 5: Frontend Integration (5 minutes)

### Step 5.1: Create runtime client

**File**: `frontend/src/integration/runtime-client.ts`

**Action**: Create file with placeholder functions:
- `callAIBlock(type: string, payload: any): Promise<any>`
- `callChapterRuntime(id: number, data: any): Promise<any>`
- TODO comments for backend API connection
- Placeholder returns

**Validation**: File exists, TypeScript compiles

---

## Phase 6: Documentation (5 minutes)

### Step 6.1: Create dependency map

**File**: `specs/044-system-integration-phase-1/contracts/dependency-map.md`

**Action**: Create file with dependency documentation:
- Chapter metadata dependencies
- Runtime dependencies
- Subagent/skills dependencies
- RAG dependencies
- Circular import prevention

**Validation**: Documentation complete

---

## Success Criteria

- ✅ All integration modules exist at specified paths
- ✅ Backend starts without import errors
- ✅ All routing placeholders connect correctly
- ✅ Runtime registry properly references chapters 1–3
- ✅ No real logic implemented (scaffolding only)
- ✅ No breaking changes to existing features

---

## Troubleshooting

### Import Errors
- Verify all imports resolve correctly
- Check for circular imports
- Ensure all modules exist

### Backend Startup Errors
- Check for syntax errors
- Verify all placeholder functions have correct signatures
- Ensure no real logic is implemented

### TypeScript Errors
- Verify TypeScript types are correct
- Check for missing imports
- Ensure Promise types are correct

---

## Notes

- This is integration scaffolding only—no real routing logic, RAG operations, provider selection, or API calls
- All functions are placeholders with TODO comments
- No breaking changes to existing functionality
- Ready for Phase 2 (dynamic registry, runtime objects)

