# Quickstart Guide: Learner Support System (LSS)

**Feature**: 058-learner-support-system
**Branch**: `058-learner-support-system`
**Estimated Time**: 2-3 hours (scaffolding only)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 044 (System Integration Phase 1) completed
- [x] Feature 045 (System Integration Phase 2) completed
- [x] Chapter metadata exists
- [x] Git branch `058-learner-support-system` checked out
- [x] Read `specs/058-learner-support-system/spec.md`
- [x] Read `specs/058-learner-support-system/plan.md`
- [x] Read `specs/058-learner-support-system/tasks.md`

## Implementation Overview

**Total Steps**: 6 phases
**Primary Deliverable**: Complete LSS scaffolding with hints, summaries, progress helper, and API endpoints
**Validation**: All LSS modules exist, API endpoints return placeholders, backend starts

---

## Phase 1: LSS Module Structure (20 minutes)

### Step 1.1: Create LSS Package

**File**: `backend/app/ai/lss/__init__.py`

**Action**: Create package init file

---

## Phase 2: Hints System (25 minutes)

### Step 2.1: Create Hints Engine

**File**: `backend/app/ai/lss/hints.py`

**Action**: Create HintEngine class:
- get_hint() method
- Hint types: "concept", "example", "definition"
- TODO comments

---

## Phase 3: Summary Engine (25 minutes)

### Step 3.1: Create Summary Engine

**File**: `backend/app/ai/lss/summaries.py`

**Action**: Create SummaryEngine class:
- summarize_section() method
- Contract comments (summary length, metadata fields)
- TODO comments

---

## Phase 4: Progress Helper (25 minutes)

### Step 4.1: Create Progress Tracker

**File**: `backend/app/ai/lss/progress.py`

**Action**: Create ProgressTracker class:
- get_section_status() method
- mark_section_complete() method
- TODO comments

---

## Phase 5: LSS API (30 minutes)

### Step 5.1: Create LSS Router

**File**: `backend/app/api/lss.py`

**Action**: Create 4 endpoints:
- POST /api/lss/hint
- POST /api/lss/summary
- POST /api/lss/progress/update
- GET /api/lss/progress/{user_id}/{chapter_id}
- All return placeholders

### Step 5.2: Register Router

**File**: `backend/app/main.py`

**Action**: Include LSS router

---

## Phase 6: Contract (15 minutes)

### Step 6.1: Create Contract File

**File**: `specs/058-learner-support-system/contracts/lss-api.yaml`

**Action**: Document all 4 endpoints

---

## Validation Checklist

After implementation, verify:

- [ ] lss/__init__.py exists
- [ ] hints.py exists with HintEngine class
- [ ] summaries.py exists with SummaryEngine class
- [ ] progress.py exists with ProgressTracker class
- [ ] lss.py exists with all 4 endpoints
- [ ] main.py includes LSS router
- [ ] Backend starts without errors

---

## Next Steps

After completing scaffolding:

1. Test LSS endpoints with sample data
2. Test hint generation (placeholder)
3. Test summary generation (placeholder)
4. Test progress tracking (placeholder)
5. Implement real AI logic in future features

---

## Troubleshooting

**Issue**: Import errors
- **Solution**: Check all __init__.py files exist

**Issue**: Router not found
- **Solution**: Verify router is registered in main.py

**Issue**: Endpoint not working
- **Solution**: Check endpoint paths and request/response models
