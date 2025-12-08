# Feature Specification: Chapter Progress Tracking Layer (Scaffold Only)

**Feature Branch**: `055-progress-tracking`
**Created**: 2025-01-27
**Status**: Draft
**Type**: backend-progress-architecture
**Input**: User description: "Introduce a progress-tracking framework enabling the system to: Mark chapter started, Mark chapter completed, Retrieve progress state for a user. NO real database logic, NO real auth integration. Only scaffolding + TODO markers."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Can Use Progress Tracking Structure (Priority: P1)

As a developer, I need a placeholder progress tracking system with models, service functions, and API endpoints, so I can understand how progress tracking will work in the future, even though the actual persistence logic is not yet implemented.

**Why this priority**: This establishes the foundation for progress tracking. Without proper scaffolding, future progress tracking implementation will require restructuring.

**Independent Test**: Can be fully tested by verifying that progress models exist, service functions exist, API endpoints return placeholder responses, and frontend helpers compile.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/progress/models.py`, **Then** I see ProgressState enum and ProgressRecord dataclass with placeholder structure

2. **Given** the feature is implemented, **When** I check `backend/app/progress/service.py`, **Then** I see functions: `mark_started()`, `mark_completed()`, `get_progress()` with placeholder logic

3. **Given** the feature is implemented, **When** I call POST `/progress/{chapter_id}/start`, **Then** I receive a placeholder success response

4. **Given** the feature is implemented, **When** I call POST `/progress/{chapter_id}/complete`, **Then** I receive a placeholder success response

5. **Given** the feature is implemented, **When** I call GET `/progress/`, **Then** I receive a placeholder progress list

---

### User Story 2 - Frontend Can Track Progress (Priority: P2)

As a frontend developer, I need helper functions to update and retrieve progress, so I can integrate progress tracking into the UI, even though the actual progress data is placeholder.

**Why this priority**: Important for frontend development, but not critical for initial scaffolding. The structure enables incremental implementation.

**Independent Test**: Can be fully tested by verifying that `progressClient.ts` exists with placeholder functions for progress tracking.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `frontend/src/progress/progressClient.ts`, **Then** I see functions: `updateProgress()`, `getProgress()` with placeholder implementations

2. **Given** the feature is implemented, **When** I call `updateProgress(chapterId, state)` in frontend, **Then** it makes a POST request to the backend and receives a placeholder response

---

### Edge Cases

- What happens when user_id is missing or invalid?
  - **Expected**: Service should handle gracefully, return error or use placeholder user_id
- What happens when chapter_id is invalid?
  - **Expected**: Service should return error or handle gracefully
- What happens when progress state is invalid?
  - **Expected**: Service should validate and return error

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Progress State Model (Placeholder)

- **FR-001.1**: System MUST create `backend/app/progress/models.py`:
  - Define `ProgressState` enum:
    - `NOT_STARTED = "not_started"`
    - `IN_PROGRESS = "in_progress"`
    - `COMPLETED = "completed"`
  - Define `ProgressRecord` dataclass:
    ```python
    @dataclass
    class ProgressRecord:
        user_id: str
        chapter_id: int
        state: ProgressState
        updated_at: datetime
    ```
  - TODO: persistence layer integration

#### FR-002: Progress Service Scaffolding

- **FR-002.1**: System MUST create `backend/app/progress/service.py`:
  - Function: `mark_started(user_id: str, chapter_id: int) -> ProgressRecord`:
    - TODO: Mark chapter as started for user
    - Placeholder: return ProgressRecord with IN_PROGRESS state
  - Function: `mark_completed(user_id: str, chapter_id: int) -> ProgressRecord`:
    - TODO: Mark chapter as completed for user
    - Placeholder: return ProgressRecord with COMPLETED state
  - Function: `get_progress(user_id: str) -> List[ProgressRecord]`:
    - TODO: Retrieve all progress records for user
    - Placeholder: return empty list or placeholder records
  - All functions contain placeholder logic + TODO comments

#### FR-003: API Endpoints Scaffold

- **FR-003.1**: System MUST create `backend/app/api/progress.py`:
  - POST `/progress/{chapter_id}/start` endpoint:
    - Read user_id from request.state.user_id (placeholder)
    - Call `service.mark_started(user_id, chapter_id)`
    - Return placeholder success response
  - POST `/progress/{chapter_id}/complete` endpoint:
    - Read user_id from request.state.user_id (placeholder)
    - Call `service.mark_completed(user_id, chapter_id)`
    - Return placeholder success response
  - GET `/progress/` endpoint:
    - Read user_id from request.state.user_id (placeholder)
    - Call `service.get_progress(user_id)`
    - Return placeholder progress list
  - All endpoints use placeholder user_id (no real auth)

#### FR-004: Router Registration

- **FR-004.1**: System MUST update `backend/app/main.py`:
  - Import: `from app.api.progress import router as progress_router`
  - Include: `app.include_router(progress_router, tags=["progress"])`

#### FR-005: Frontend Tracking Helper

- **FR-005.1**: System MUST create `frontend/src/progress/progressClient.ts`:
  - Function: `updateProgress(chapterId: number, state: string) -> Promise<Dict>`:
    - POST to `/progress/{chapterId}/start` or `/progress/{chapterId}/complete`
    - Return placeholder response
  - Function: `getProgress() -> Promise<Dict[]>`:
    - GET `/progress/`
    - Return placeholder progress list
  - All functions are placeholder implementations

#### FR-006: Contract File

- **FR-006.1**: System MUST create `specs/055-progress-tracking/contracts/progress-api.yaml`:
  - Document the three endpoints (start, complete, get)
  - Placeholder request/response schemas
  - No actual persistence schema

#### FR-007: Testing Scaffold

- **FR-007.1**: System MUST create `backend/tests/progress/test_progress.py`:
  - Placeholder test: `test_mark_started_placeholder()`
  - Placeholder test: `test_mark_completed_placeholder()`
  - Placeholder test: `test_get_progress_placeholder()`
  - All tests are placeholders with TODO comments

## Success Criteria

- ✅ All files exist
- ✅ Backend starts without errors
- ✅ API routes compile
- ✅ Frontend builds
- ✅ Contract YAML created
- ✅ spec.md, plan.md, tasks.md created correctly
- ✅ Contract file created
- ✅ Checklist file created
- ✅ Research, data-model, quickstart files created

## Constraints

- **No Real DB Logic**: All persistence must be placeholders only
- **No Real Authentication**: All user_id extraction must be placeholders
- **No Real User Session**: No real session management
- **Scaffolding Only**: This feature creates structure, not functionality
- **No Analytics**: No analytics or dashboard logic

## Dependencies

- Feature 052 (BetterAuth) — for auth structure (optional, not required for scaffolding)
- FastAPI for backend routes
- React/TypeScript for frontend

## Out of Scope

- Real database persistence
- Real authentication integration
- Real user session management
- Analytics and dashboard
- Progress history
- Progress statistics
- Progress sharing

