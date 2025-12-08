# Quickstart Guide: Chapter Access Control Scaffolding

**Feature**: 054-chapter-access-control
**Branch**: `054-chapter-access-control`
**Estimated Time**: 1-2 hours (scaffolding only)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 053 (Roles & Permissions) completed
- [x] Feature 052 (BetterAuth) completed
- [x] Backend chapters API exists
- [x] Git branch `054-chapter-access-control` checked out
- [x] Read `specs/054-chapter-access-control/spec.md`
- [x] Read `specs/054-chapter-access-control/plan.md`
- [x] Read `specs/054-chapter-access-control/tasks.md`

## Implementation Overview

**Total Steps**: 6 phases
**Primary Deliverable**: Complete chapter access control scaffolding with access map, checking functions, decorators, API integration, and frontend helpers
**Validation**: All access control modules exist, decorators work, API routes wrapped, frontend helpers compile

---

## Phase 1: Backend Chapter Access Map (15 minutes)

### Step 1.1: Create Chapter Access File

**File**: `backend/app/auth/chapter_access.py`

**Action**: Create CHAPTER_ACCESS_MAP:
- Map chapters 1, 2, 3 to allowed roles
- Default: All roles allowed
- TODO comments

---

## Phase 2: Access Checking Function (15 minutes)

### Step 2.1: Update Permissions File

**File**: `backend/app/auth/permissions.py`

**Action**: Add `can_access_chapter()` function:
- Accepts user_role and chapter_number
- Returns placeholder True/False
- TODO comments

---

## Phase 3: Chapter Access Decorator (15 minutes)

### Step 3.1: Update Decorators

**File**: `backend/app/auth/decorators.py`

**Action**: Add `require_chapter_access()` decorator:
- Accepts chapter_number
- Placeholder check
- TODO comments

---

## Phase 4: API Integration (20 minutes)

### Step 4.1: Update Chapters API

**File**: `backend/app/api/chapters.py`

**Action**: Wrap GET `/chapter/{id}` with decorator:
- Apply `require_chapter_access(id)` decorator
- Placeholder behavior

---

## Phase 5: Frontend Helpers (20 minutes)

### Step 5.1: Create Chapter Access Helpers

**File**: `frontend/src/auth/chapterAccess.ts`

**Action**: Create functions:
- `canViewChapter()` - Check if role can view chapter
- `chaptersAllowed()` - Get allowed chapters for role
- All placeholders

---

## Phase 6: Tests Placeholder (15 minutes)

### Step 6.1: Create Test File

**File**: `backend/tests/auth/test_chapter_access.py`

**Action**: Create placeholder tests:
- test_student_access_placeholder()
- test_educator_access_placeholder()
- test_admin_access_placeholder()

---

## Validation Checklist

After implementation, verify:

- [ ] chapter_access.py exists with CHAPTER_ACCESS_MAP
- [ ] permissions.py has can_access_chapter()
- [ ] decorators.py has require_chapter_access()
- [ ] chapters.py endpoint wrapped with decorator
- [ ] chapterAccess.ts exists with all functions
- [ ] test_chapter_access.py exists
- [ ] Backend starts without errors
- [ ] Frontend builds without errors

---

## Next Steps

After completing scaffolding:

1. Test chapter access checking
2. Test decorator on sample routes
3. Test frontend helpers
4. Implement real access control logic in future features

---

## Troubleshooting

**Issue**: Import errors
- **Solution**: Check all __init__.py files exist

**Issue**: Decorator not working
- **Solution**: Verify decorator is applied correctly

**Issue**: Frontend helpers don't work
- **Solution**: Check chapterAccess.ts imports

