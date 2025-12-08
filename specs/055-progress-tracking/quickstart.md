# Quickstart Guide: Chapter Progress Tracking Layer

**Feature**: 055-progress-tracking
**Branch**: `055-progress-tracking`
**Estimated Time**: 1-2 hours (scaffolding only)

## Prerequisites

Before starting implementation, ensure you have:

- [x] FastAPI backend structure exists
- [x] React/TypeScript frontend structure exists
- [x] Git branch `055-progress-tracking` checked out
- [x] Read `specs/055-progress-tracking/spec.md`
- [x] Read `specs/055-progress-tracking/plan.md`
- [x] Read `specs/055-progress-tracking/tasks.md`

## Implementation Overview

**Total Steps**: 6 phases
**Primary Deliverable**: Complete progress tracking scaffolding with models, service, API endpoints, and frontend helpers
**Validation**: All progress modules exist, API endpoints return placeholders, frontend helpers compile

---

## Phase 1: Backend Models (15 minutes)

### Step 1.1: Create Progress Models

**File**: `backend/app/progress/models.py`

**Action**: Create:
- ProgressState enum (NOT_STARTED, IN_PROGRESS, COMPLETED)
- ProgressRecord dataclass
- TODO comments for persistence

---

## Phase 2: Progress Service (20 minutes)

### Step 2.1: Create Progress Service

**File**: `backend/app/progress/service.py`

**Action**: Create functions:
- `mark_started()` - Placeholder
- `mark_completed()` - Placeholder
- `get_progress()` - Placeholder
- All with TODO comments

---

## Phase 3: API Endpoints (25 minutes)

### Step 3.1: Create Progress API

**File**: `backend/app/api/progress.py`

**Action**: Create endpoints:
- POST `/progress/{chapter_id}/start`
- POST `/progress/{chapter_id}/complete`
- GET `/progress/`
- All return placeholders

### Step 3.2: Register Router

**File**: `backend/app/main.py`

**Action**: Include progress router

---

## Phase 4: Frontend Helper (20 minutes)

### Step 4.1: Create Progress Client

**File**: `frontend/src/progress/progressClient.ts`

**Action**: Create functions:
- `updateProgress()` - POST to backend
- `getProgress()` - GET from backend
- All placeholders

---

## Phase 5: Tests Placeholder (15 minutes)

### Step 5.1: Create Test File

**File**: `backend/tests/progress/test_progress.py`

**Action**: Create placeholder tests:
- test_mark_started_placeholder()
- test_mark_completed_placeholder()
- test_get_progress_placeholder()

---

## Phase 6: Contract (10 minutes)

### Step 6.1: Create Contract File

**File**: `specs/055-progress-tracking/contracts/progress-api.yaml`

**Action**: Document all 3 endpoints

---

## Validation Checklist

After implementation, verify:

- [ ] models.py exists with enum and dataclass
- [ ] service.py exists with all functions
- [ ] progress.py exists with all endpoints
- [ ] main.py includes progress router
- [ ] progressClient.ts exists with all functions
- [ ] test_progress.py exists
- [ ] Backend starts without errors
- [ ] Frontend builds without errors

---

## Next Steps

After completing scaffolding:

1. Test progress endpoints with sample data
2. Test frontend helpers
3. Verify service functions work
4. Implement real persistence logic in future features

---

## Troubleshooting

**Issue**: Import errors
- **Solution**: Check all __init__.py files exist

**Issue**: Router not found
- **Solution**: Verify router is registered in main.py

**Issue**: Frontend helpers don't work
- **Solution**: Check progressClient.ts imports and API calls

