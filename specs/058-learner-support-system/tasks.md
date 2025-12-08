# Implementation Tasks: Learner Support System (LSS) — Hints, Summaries & Progress Helper

**Feature**: 058-learner-support-system  
**Date**: 2025-01-27  
**Status**: Draft

## Task Groups

### A. LSS Module Creation Tasks

- [ ] **T001**: Create `backend/app/ai/lss/__init__.py`
  - Make lss a package
  - File: `backend/app/ai/lss/__init__.py`

- [ ] **T002**: Create `backend/app/ai/lss/hints.py`
  - Define HintEngine class
  - Add method: `get_hint(chapter_id: int, section_id: str, user_state: dict) -> str`
  - Define hint types: "concept", "example", "definition"
  - TODO: Use context + runtime later
  - Placeholder: Return placeholder hint string
  - File: `backend/app/ai/lss/hints.py`

- [ ] **T003**: Create `backend/app/ai/lss/summaries.py`
  - Define SummaryEngine class
  - Add method: `summarize_section(chapter_id: int, section_id: str) -> str`
  - Add contract comments: expected summary length (2-3 sentences), metadata fields to use
  - TODO: Use section metadata, RAG pipeline later
  - Placeholder: Return placeholder summary string
  - File: `backend/app/ai/lss/summaries.py`

- [ ] **T004**: Create `backend/app/ai/lss/progress.py`
  - Define ProgressTracker class
  - Add method: `get_section_status(user_id: str, chapter_id: int) -> dict`
  - Add method: `mark_section_complete(user_id: str, chapter_id: int, section_id: str) -> None`
  - TODO: Replace with DB later (stub only)
  - Placeholder: Return placeholder progress data
  - File: `backend/app/ai/lss/progress.py`

---

### B. API Layer Tasks

- [ ] **T005**: Create `backend/app/api/lss.py`
  - File: `backend/app/api/lss.py`

- [ ] **T006**: Add POST /api/lss/hint endpoint
  - Accepts chapter_id, section_id, user_state (optional)
  - Calls HintEngine.get_hint()
  - Returns placeholder JSON: hint, hint_type, chapter_id, section_id
  - File: `backend/app/api/lss.py`

- [ ] **T007**: Add POST /api/lss/summary endpoint
  - Accepts chapter_id, section_id
  - Calls SummaryEngine.summarize_section()
  - Returns placeholder JSON: summary, chapter_id, section_id, summary_length
  - File: `backend/app/api/lss.py`

- [ ] **T008**: Add POST /api/lss/progress/update endpoint
  - Accepts user_id, chapter_id, section_id
  - Calls ProgressTracker.mark_section_complete()
  - Returns placeholder JSON: message, user_id, chapter_id, section_id
  - File: `backend/app/api/lss.py`

- [ ] **T009**: Add GET /api/lss/progress/{user_id}/{chapter_id} endpoint
  - Extracts user_id and chapter_id from path
  - Calls ProgressTracker.get_section_status()
  - Returns placeholder JSON: user_id, chapter_id, sections (list)
  - File: `backend/app/api/lss.py`

---

### C. Integration Tasks

- [ ] **T010**: Register LSS router in main.py
  - Import: `from app.api.lss import router as lss_router`
  - Include: `app.include_router(lss_router, tags=["lss"])`
  - File: `backend/app/main.py`

---

### D. Contract Tasks

- [ ] **T011**: Create `specs/058-learner-support-system/contracts/lss-api.yaml`
  - Describe request/response structure for hints
  - Describe request/response structure for summaries
  - Describe request/response structure for progress
  - No real schemas for AI output
  - File: `specs/058-learner-support-system/contracts/lss-api.yaml`

---

### E. Validation Tasks

- [ ] **T012**: Backend starts without errors
  - Verify: `cd backend && uvicorn app.main:app --reload` starts without errors
  - Check: All imports resolve correctly

- [ ] **T013**: API endpoints return placeholder JSON
  - Test POST /api/lss/hint with sample data
  - Test POST /api/lss/summary with sample data
  - Test POST /api/lss/progress/update with sample data
  - Test GET /api/lss/progress/{user_id}/{chapter_id} with sample data

---

## Implementation Notes

- All backend functions must have TODO comments explaining expected behavior
- All functions must be placeholder implementations
- No real AI logic should be implemented
- No real database logic should be implemented
- No real RAG integration should be implemented
- All responses are static placeholders
- LSS is optional and should not break existing functionality
