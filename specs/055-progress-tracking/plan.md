# Implementation Plan: Chapter Progress Tracking Layer (Scaffold Only)

**Branch**: `055-progress-tracking` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature implements complete scaffolding for chapter progress tracking. It introduces progress state model, service functions for marking progress, API endpoints for progress operations, and frontend helpers for progress tracking. **All implementations are scaffolding only—no real database logic, no real auth integration.**

**Primary Deliverable**: Complete progress tracking scaffolding structure
**Validation**: All progress modules exist, API endpoints return placeholders, frontend helpers compile

---

## 1. Data Flow

### 1.1 Progress Update Flow

```
Frontend Component
  → progressClient.updateProgress(chapterId, state)
  → POST /progress/{chapter_id}/start or /complete
  → Backend extracts user_id from request.state (placeholder)
  → Service function (mark_started or mark_completed)
  → Return ProgressRecord (placeholder)
```

### 1.2 Progress Retrieval Flow

```
Frontend Component
  → progressClient.getProgress()
  → GET /progress/
  → Backend extracts user_id from request.state (placeholder)
  → Service function (get_progress)
  → Return list of ProgressRecords (placeholder)
```

---

## 2. Model Design

### 2.1 ProgressState Enum

**File**: `backend/app/progress/models.py`

**Structure**:
```python
from enum import Enum

class ProgressState(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
```

**Purpose**: Type-safe progress state values

---

### 2.2 ProgressRecord Dataclass

**File**: `backend/app/progress/models.py`

**Structure**:
```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProgressRecord:
    user_id: str
    chapter_id: int
    state: ProgressState
    updated_at: datetime
```

**Purpose**: Structured progress record representation

**Future DB Integration**: TODO comments for database model mapping

---

## 3. Service Layer Design

### 3.1 Progress Service

**File**: `backend/app/progress/service.py`

**Functions**:

1. **mark_started(user_id: str, chapter_id: int) -> ProgressRecord**:
   - TODO: Create or update progress record with IN_PROGRESS state
   - TODO: Persist to database
   - Placeholder: Return ProgressRecord with IN_PROGRESS state

2. **mark_completed(user_id: str, chapter_id: int) -> ProgressRecord**:
   - TODO: Update progress record with COMPLETED state
   - TODO: Persist to database
   - Placeholder: Return ProgressRecord with COMPLETED state

3. **get_progress(user_id: str) -> List[ProgressRecord]**:
   - TODO: Retrieve all progress records for user from database
   - Placeholder: Return empty list or placeholder records

**TODOs**: Database logic, validation, error handling

---

## 4. API Design

### 4.1 Progress Endpoints

**File**: `backend/app/api/progress.py`

**Endpoints**:

1. **POST `/progress/{chapter_id}/start`**:
   - Extract user_id from request.state.user_id (placeholder)
   - Call `service.mark_started(user_id, chapter_id)`
   - Return ProgressRecord response

2. **POST `/progress/{chapter_id}/complete`**:
   - Extract user_id from request.state.user_id (placeholder)
   - Call `service.mark_completed(user_id, chapter_id)`
   - Return ProgressRecord response

3. **GET `/progress/`**:
   - Extract user_id from request.state.user_id (placeholder)
   - Call `service.get_progress(user_id)`
   - Return list of ProgressRecords

**Placeholder Responses**: All endpoints return static placeholder data

---

## 5. Frontend Integration Plan

### 5.1 Progress Client

**File**: `frontend/src/progress/progressClient.ts`

**Functions**:
- `updateProgress(chapterId: number, state: string) -> Promise<Dict>`:
  - POST to `/progress/{chapterId}/start` or `/complete` based on state
  - Return placeholder response
- `getProgress() -> Promise<Dict[]>`:
  - GET `/progress/`
  - Return placeholder progress list

**Usage Patterns**: Called from chapter viewer components, progress dashboard (future)

---

## 6. File Structure Plan

```
backend/app/progress/
├── __init__.py
├── models.py          # ProgressState enum, ProgressRecord dataclass
└── service.py         # Progress service functions

backend/app/api/
└── progress.py        # Progress API endpoints

backend/tests/progress/
└── test_progress.py   # Placeholder tests

frontend/src/progress/
└── progressClient.ts   # Progress client functions

specs/055-progress-tracking/contracts/
└── progress-api.yaml   # API contract (already created)
```

---

## 7. Constraints & Future Work

### Constraints
- **NO Real DB Logic**: All persistence must be placeholders
- **NO Real Auth**: All user_id extraction must be placeholders
- **NO Real Session**: No real session management
- **Scaffolding Only**: Structure, not functionality

### Future Work
- Real database persistence (PostgreSQL, MongoDB, etc.)
- Real authentication integration
- Progress history tracking
- Progress analytics
- Progress dashboard
- Progress sharing

---

## 8. Acceptance Criteria Mapping

| Acceptance Criteria | Implementation Location |
|---------------------|------------------------|
| All files exist | All files created with placeholder logic |
| Backend starts without errors | All imports resolve correctly |
| API routes compile | All endpoints return placeholders |
| Frontend builds | progressClient.ts compiles |
| Contract YAML created | progress-api.yaml already created |

---

## 9. Risk Analysis

**Risk 1**: Import errors if progress module structure incorrect
- **Mitigation**: Ensure all `__init__.py` files exist, test imports

**Risk 2**: Service functions may not handle edge cases
- **Mitigation**: Add TODO comments for validation, use placeholder defaults

**Risk 3**: Frontend helpers may not integrate with UI
- **Mitigation**: Create standalone helpers, integration in future features

---

## 10. Future Enhancements

- Real database persistence
- Real authentication integration
- Progress history
- Progress statistics
- Progress visualization
- Progress dashboard
- Progress sharing

