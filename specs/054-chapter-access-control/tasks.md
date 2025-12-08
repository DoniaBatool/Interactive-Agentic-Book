# Implementation Tasks: Chapter Access Control Scaffolding

**Feature**: 054-chapter-access-control  
**Date**: 2025-01-27  
**Status**: Draft

## Task Groups

### A. Backend Tasks

- [ ] **T001**: Create `backend/app/auth/chapter_access.py` with CHAPTER_ACCESS_MAP
  - Define: `CHAPTER_ACCESS_MAP: Dict[int, List[str]]`
  - Map chapters 1, 2, 3 to allowed roles
  - Default: All roles allowed for all chapters
  - TODO comments for real policy logic
  - File: `backend/app/auth/chapter_access.py`

- [ ] **T002**: Add `can_access_chapter()` to `backend/app/auth/permissions.py`
  - Function: `can_access_chapter(user_role: str, chapter_number: int) -> bool`
  - TODO: Check if user_role is in allowed roles for chapter_number
  - Placeholder: return True for all (or based on CHAPTER_ACCESS_MAP)
  - TODO comments explaining expected logic
  - File: `backend/app/auth/permissions.py` (update existing)

- [ ] **T003**: Add `require_chapter_access()` decorator to `backend/app/auth/decorators.py`
  - Decorator: `require_chapter_access(chapter_number: int)`
  - TODO: Check if user can access chapter
  - TODO: Read request.state.user_role
  - TODO: Call can_access_chapter()
  - Placeholder enforcement: pass-through with TODO
  - TODO comments only
  - File: `backend/app/auth/decorators.py` (update existing)

- [ ] **T004**: Modify `backend/app/api/chapters.py` to use decorator
  - Wrap GET `/chapter/{id}` endpoint with `require_chapter_access(id)` decorator
  - Placeholder behavior only
  - File: `backend/app/api/chapters.py` (update existing)

- [ ] **T005**: Ensure imports resolve
  - Check all imports work correctly
  - Verify no circular imports

---

### B. Frontend Tasks

- [ ] **T006**: Create `frontend/src/auth/chapterAccess.ts`
  - File: `frontend/src/auth/chapterAccess.ts`

- [ ] **T007**: Implement `canViewChapter()` placeholder
  - Function: `canViewChapter(role: string, chapterNumber: number) -> boolean`
  - Placeholder: Check if role can access chapter
  - Return placeholder boolean
  - File: `frontend/src/auth/chapterAccess.ts`

- [ ] **T008**: Implement `chaptersAllowed()` placeholder
  - Function: `chaptersAllowed(role: string) -> number[]`
  - Placeholder: Return list of allowed chapter numbers for role
  - Return placeholder list (e.g., [1, 2, 3])
  - File: `frontend/src/auth/chapterAccess.ts`

---

### C. Contract Tasks

- [ ] **T009**: Create `specs/054-chapter-access-control/contracts/chapter-access.yaml`
  - High-level description of access rules
  - Chapter → Role mapping structure
  - No actual enforcement schema
  - File: `specs/054-chapter-access-control/contracts/chapter-access.yaml` (already created)

---

### D. Testing Scaffold

- [ ] **T010**: Create `backend/tests/auth/test_chapter_access.py` with placeholder tests
  - Test: `test_student_access_placeholder()`
  - Test: `test_educator_access_placeholder()`
  - Test: `test_admin_access_placeholder()`
  - All with TODO comments
  - File: `backend/tests/auth/test_chapter_access.py`

---

### E. Validation Tasks

- [ ] **T011**: Backend compiles with no runtime errors
  - Verify: `cd backend && uvicorn app.main:app --reload` starts without errors
  - Check: All imports resolve correctly

- [ ] **T012**: Frontend builds without errors
  - Verify: `cd frontend && npm run build` succeeds
  - Check: All components compile

---

## Implementation Notes

- All backend functions must have TODO comments explaining expected behavior
- All frontend functions must be placeholder implementations
- No real access control enforcement logic should be implemented
- All responses are static placeholders
- Decorator is optional (can be applied to routes incrementally)

