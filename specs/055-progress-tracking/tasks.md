# Implementation Tasks: Chapter Progress Tracking Layer (Scaffold Only)

**Feature**: 055-progress-tracking  
**Date**: 2025-01-27  
**Status**: Draft

## Task Groups

### A. Backend Model Tasks

- [ ] **T001**: Create `backend/app/progress/__init__.py` to make progress a package
  - File: `backend/app/progress/__init__.py`

- [ ] **T002**: Create `backend/app/progress/models.py`
  - File: `backend/app/progress/models.py`

- [ ] **T003**: Add ProgressState enum to models.py
  - Enum values: NOT_STARTED, IN_PROGRESS, COMPLETED
  - File: `backend/app/progress/models.py`

- [ ] **T004**: Add ProgressRecord dataclass to models.py
  - Fields: user_id, chapter_id, state, updated_at
  - TODO: persistence layer integration
  - File: `backend/app/progress/models.py`

---

### B. Progress Service Tasks

- [ ] **T005**: Create `backend/app/progress/service.py`
  - File: `backend/app/progress/service.py`

- [ ] **T006**: Add mark_started() placeholder to service.py
  - Function: `mark_started(user_id: str, chapter_id: int) -> ProgressRecord`
  - TODO: Mark chapter as started for user
  - Placeholder: return ProgressRecord with IN_PROGRESS state
  - File: `backend/app/progress/service.py`

- [ ] **T007**: Add mark_completed() placeholder to service.py
  - Function: `mark_completed(user_id: str, chapter_id: int) -> ProgressRecord`
  - TODO: Mark chapter as completed for user
  - Placeholder: return ProgressRecord with COMPLETED state
  - File: `backend/app/progress/service.py`

- [ ] **T008**: Add get_progress() placeholder to service.py
  - Function: `get_progress(user_id: str) -> List[ProgressRecord]`
  - TODO: Retrieve all progress records for user
  - Placeholder: return empty list or placeholder records
  - File: `backend/app/progress/service.py`

---

### C. API Tasks

- [ ] **T009**: Create `backend/app/api/progress.py`
  - File: `backend/app/api/progress.py`

- [ ] **T010**: Add POST /progress/{chapter_id}/start endpoint
  - Read user_id from request.state.user_id (placeholder)
  - Call service.mark_started(user_id, chapter_id)
  - Return placeholder success response
  - File: `backend/app/api/progress.py`

- [ ] **T011**: Add POST /progress/{chapter_id}/complete endpoint
  - Read user_id from request.state.user_id (placeholder)
  - Call service.mark_completed(user_id, chapter_id)
  - Return placeholder success response
  - File: `backend/app/api/progress.py`

- [ ] **T012**: Add GET /progress/ endpoint
  - Read user_id from request.state.user_id (placeholder)
  - Call service.get_progress(user_id)
  - Return placeholder progress list
  - File: `backend/app/api/progress.py`

- [ ] **T013**: Register router in main.py
  - Import: `from app.api.progress import router as progress_router`
  - Include: `app.include_router(progress_router, tags=["progress"])`
  - File: `backend/app/main.py`

---

### D. Frontend Tasks

- [ ] **T014**: Create `frontend/src/progress/progressClient.ts`
  - File: `frontend/src/progress/progressClient.ts`

- [ ] **T015**: Implement updateProgress() placeholder
  - Function: `updateProgress(chapterId: number, state: string) -> Promise<Dict>`
  - POST to `/progress/{chapterId}/start` or `/progress/{chapterId}/complete` based on state
  - Return placeholder response
  - File: `frontend/src/progress/progressClient.ts`

- [ ] **T016**: Implement getProgress() placeholder
  - Function: `getProgress() -> Promise<Dict[]>`
  - GET `/progress/`
  - Return placeholder progress list
  - File: `frontend/src/progress/progressClient.ts`

---

### E. Contract Tasks

- [ ] **T017**: Create `specs/055-progress-tracking/contracts/progress-api.yaml`
  - Document the three endpoints (start, complete, get)
  - Placeholder request/response schemas
  - File: `specs/055-progress-tracking/contracts/progress-api.yaml` (already created)

---

### F. Testing Tasks

- [ ] **T018**: Create `backend/tests/progress/test_progress.py` with placeholders
  - Test: `test_mark_started_placeholder()`
  - Test: `test_mark_completed_placeholder()`
  - Test: `test_get_progress_placeholder()`
  - All with TODO comments
  - File: `backend/tests/progress/test_progress.py`

---

### G. Validation Tasks

- [ ] **T019**: Backend starts without errors
  - Verify: `cd backend && uvicorn app.main:app --reload` starts without errors
  - Check: All imports resolve correctly

- [ ] **T020**: Frontend compiles successfully
  - Verify: `cd frontend && npm run build` succeeds
  - Check: All components compile

---

## Implementation Notes

- All backend functions must have TODO comments explaining expected behavior
- All frontend functions must be placeholder implementations
- No real persistence logic should be implemented
- No real authentication logic should be implemented
- All responses are static placeholders
- User ID extraction is placeholder (no real auth)

