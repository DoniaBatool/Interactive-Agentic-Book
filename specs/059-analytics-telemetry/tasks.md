# Implementation Tasks: Analytics & Telemetry Scaffolding Layer

**Feature**: 059-analytics-telemetry  
**Date**: 2025-01-27  
**Status**: Draft

## Task Groups

### A. Analytics Module Setup Tasks

- [ ] **T001**: Create `backend/app/analytics/__init__.py`
  - Make analytics a package
  - File: `backend/app/analytics/__init__.py`

---

### B. Event Logger Scaffold Tasks

- [ ] **T002**: Create `backend/app/analytics/event_logger.py`
  - Define EventLogger class
  - Add method: `log(event_type: str, payload: dict) -> None`
  - Define event types: "ai_block_used", "chapter_visit", "error_event"
  - TODO: Replace with real tracking later
  - Placeholder: Print/log message (no real persistence)
  - File: `backend/app/analytics/event_logger.py`

---

### C. Analytics Models Tasks

- [ ] **T003**: Create `backend/app/analytics/analytics_models.py`
  - Define AnalyticsEvent class (dataclass or Pydantic model)
  - Fields: event_type (str), payload (dict), timestamp (str)
  - No database storage
  - Placeholder structure only
  - File: `backend/app/analytics/analytics_models.py`

---

### D. Telemetry Router Tasks

- [ ] **T004**: Create `backend/app/analytics/telemetry_router.py`
  - File: `backend/app/analytics/telemetry_router.py`

- [ ] **T005**: Add POST /api/telemetry/log endpoint
  - Accepts event_type, payload
  - Calls EventLogger.log()
  - Returns placeholder JSON: message, event_type, timestamp
  - File: `backend/app/analytics/telemetry_router.py`

- [ ] **T006**: Add GET /api/telemetry/health endpoint
  - Returns placeholder JSON: status, message, events_logged
  - File: `backend/app/analytics/telemetry_router.py`

---

### E. Integration Tasks

- [ ] **T007**: Register telemetry router in main.py
  - Import: `from app.analytics.telemetry_router import router as telemetry_router`
  - Include: `app.include_router(telemetry_router, tags=["telemetry"])`
  - File: `backend/app/main.py`

- [ ] **T008**: Add EventLogger.log() calls to ai_blocks.py
  - Import: `from app.analytics.event_logger import event_logger`
  - Add call in ask_question endpoint: `event_logger.log("ai_block_used", {...})`
  - Add call in explain_like_10 endpoint: `event_logger.log("ai_block_used", {...})`
  - Add call in quiz endpoint: `event_logger.log("ai_block_used", {...})`
  - Add call in diagram endpoint: `event_logger.log("ai_block_used", {...})`
  - All with placeholder payload data
  - TODO comments
  - File: `backend/app/api/ai_blocks.py`

---

### F. Contract Tasks

- [ ] **T009**: Create `specs/059-analytics-telemetry/contracts/telemetry-api.yaml`
  - High-level description of telemetry API
  - Request/response structure
  - No actual tracking schema
  - File: `specs/059-analytics-telemetry/contracts/telemetry-api.yaml`

---

### G. Validation Tasks

- [ ] **T010**: Backend starts without errors
  - Verify: `cd backend && uvicorn app.main:app --reload` starts without errors
  - Check: All imports resolve correctly

- [ ] **T011**: API endpoints return placeholder JSON
  - Test POST /api/telemetry/log with sample event
  - Test GET /api/telemetry/health

---

## Implementation Notes

- All backend functions must have TODO comments explaining expected behavior
- All functions must be placeholder implementations
- No real tracking logic should be implemented
- No real database logic should be implemented
- No real external service integration should be implemented
- All responses are static placeholders
- EventLogger calls should not break existing functionality
