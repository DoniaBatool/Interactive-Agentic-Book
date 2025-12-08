# Feature Specification: Learner Support System (LSS) — Hints, Summaries & Progress Helper

**Feature Branch**: `058-learner-support-system`
**Created**: 2025-01-27
**Status**: Draft
**Type**: backend-ai-support-layer
**Input**: User description: "Build a backend-only scaffolding system that provides: Context-aware hints, Auto-generated summaries for sections, Simple progress helper endpoints. WITHOUT adding real AI logic. This feature must integrate with Chapter metadata and the existing runtime engine, using only placeholder functions."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learner Can Get Hints (Priority: P1)

As a learner, I need a hints system to get context-aware hints when I'm stuck, so I can understand concepts better, even though the actual hint generation logic is placeholder.

**Why this priority**: This establishes the foundation for learner support. Without proper scaffolding, future hint implementation will require restructuring.

**Independent Test**: Can be fully tested by verifying that hints endpoint exists, HintEngine class exists, and endpoint returns placeholder hints.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I call POST `/api/lss/hint` with chapter_id, section_id, and user_state, **Then** I receive a placeholder hint response

2. **Given** the feature is implemented, **When** I check `backend/app/ai/lss/hints.py`, **Then** I see HintEngine class with get_hint() method and placeholder logic

3. **Given** the feature is implemented, **When** I check the hint response, **Then** I see hint_type field with values: "concept", "example", "definition"

---

### User Story 2 - Learner Can Get Section Summaries (Priority: P1)

As a learner, I need section summaries to quickly understand what a section covers, so I can decide if I need to read it, even though the actual summary generation logic is placeholder.

**Why this priority**: This establishes the foundation for summary generation. Without proper scaffolding, future summary implementation will require restructuring.

**Independent Test**: Can be fully tested by verifying that summary endpoint exists, SummaryEngine class exists, and endpoint returns placeholder summaries.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I call POST `/api/lss/summary` with chapter_id and section_id, **Then** I receive a placeholder summary response

2. **Given** the feature is implemented, **When** I check `backend/app/ai/lss/summaries.py`, **Then** I see SummaryEngine class with summarize_section() method and placeholder logic

---

### User Story 3 - Learner Can Track Progress (Priority: P2)

As a learner, I need progress tracking endpoints to mark sections as complete, so I can track my learning progress, even though the actual progress storage is placeholder.

**Why this priority**: Important for learner experience, but not critical for initial scaffolding. The structure enables incremental implementation.

**Independent Test**: Can be fully tested by verifying that progress endpoints exist, ProgressTracker class exists, and endpoints return placeholder responses.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I call POST `/api/lss/progress/update` with user_id, chapter_id, and section_id, **Then** I receive a placeholder success response

2. **Given** the feature is implemented, **When** I call GET `/api/lss/progress/{user_id}/{chapter_id}`, **Then** I receive a placeholder progress response

---

### Edge Cases

- What happens when chapter_id or section_id is invalid?
  - **Expected**: Return error response (placeholder)
- What happens when user_state is missing?
  - **Expected**: Use default user_state (placeholder)
- What happens when section has no content?
  - **Expected**: Return empty summary or error (placeholder)

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: LSS Module Structure

- **FR-001.1**: System MUST create folder `backend/app/ai/lss/`:
  - Create `__init__.py` to make lss a package
  - Create `hints.py` with HintEngine class
  - Create `summaries.py` with SummaryEngine class
  - Create `progress.py` with ProgressTracker class
  - All files must include placeholder classes, method signatures, and TODO comments

#### FR-002: Hints System Scaffolding

- **FR-002.1**: System MUST create `backend/app/ai/lss/hints.py`:
  - Define `HintEngine` class:
    - Method: `get_hint(chapter_id: int, section_id: str, user_state: dict) -> str`
    - Return placeholder hint string
    - TODO: Use context + runtime later
  - Define allowed hint types: "concept", "example", "definition"
  - All logic is placeholder with TODO comments

#### FR-003: Section Summary Engine

- **FR-003.1**: System MUST create `backend/app/ai/lss/summaries.py`:
  - Define `SummaryEngine` class:
    - Method: `summarize_section(chapter_id: int, section_id: str) -> str`
    - Return placeholder summary string
  - Add contract comments describing:
    - Expected summary length (e.g., 2-3 sentences)
    - What metadata fields should be used (section title, content preview)
  - All logic is placeholder with TODO comments

#### FR-004: Progress Helper Scaffolding

- **FR-004.1**: System MUST create `backend/app/ai/lss/progress.py`:
  - Define `ProgressTracker` class:
    - Method: `get_section_status(user_id: str, chapter_id: int) -> dict`
    - Method: `mark_section_complete(user_id: str, chapter_id: int, section_id: str) -> None`
  - TODO: Replace with DB later (stub only)
  - All logic is placeholder with TODO comments

#### FR-005: LSS Router Layer

- **FR-005.1**: System MUST create `backend/app/api/lss.py`:
  - POST `/api/lss/hint` endpoint:
    - Accepts chapter_id, section_id, user_state
    - Calls HintEngine.get_hint()
    - Returns placeholder JSON
  - POST `/api/lss/summary` endpoint:
    - Accepts chapter_id, section_id
    - Calls SummaryEngine.summarize_section()
    - Returns placeholder JSON
  - POST `/api/lss/progress/update` endpoint:
    - Accepts user_id, chapter_id, section_id
    - Calls ProgressTracker.mark_section_complete()
    - Returns placeholder JSON
  - GET `/api/lss/progress/{user_id}/{chapter_id}` endpoint:
    - Calls ProgressTracker.get_section_status()
    - Returns placeholder JSON
  - All endpoints return placeholder responses

#### FR-006: Router Integration

- **FR-006.1**: System MUST update `backend/app/main.py`:
  - Import: `from app.api.lss import router as lss_router`
  - Include: `app.include_router(lss_router, tags=["lss"])`

#### FR-007: Contract File

- **FR-007.1**: System MUST create `specs/058-learner-support-system/contracts/lss-api.yaml`:
  - Describe request/response structure for hints
  - Describe request/response structure for summaries
  - Describe request/response structure for progress
  - No real schemas for AI output

## Success Criteria

- ✅ All scaffolding files created with method signatures + TODO comments
- ✅ New API endpoints compile and return placeholder JSON
- ✅ No AI logic implemented
- ✅ Backend builds without errors
- ✅ LSS integrates with existing chapter metadata
- ✅ spec.md, plan.md, tasks.md created correctly
- ✅ Contract file created
- ✅ Checklist file created
- ✅ Research, data-model, quickstart files created

## Constraints

- **No Real AI Logic**: All implementations must be placeholders only
- **Backend Only**: No frontend components required
- **Scaffolding Only**: This feature creates structure, not functionality
- **No Database**: No real progress storage
- **No RAG Integration**: No real RAG calls

## Dependencies

- Feature 044 (System Integration Phase 1) — for runtime structure
- Feature 045 (System Integration Phase 2) — for RAG pipeline structure
- Chapter metadata — must exist
- Runtime engine — must exist

## Out of Scope

- Real AI logic for hints
- Real AI logic for summaries
- Real database for progress
- Real RAG integration
- Frontend components
- Real context-aware hint generation
