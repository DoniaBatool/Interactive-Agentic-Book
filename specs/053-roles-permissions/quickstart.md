# Quickstart Guide: User Roles & Permission Scaffolding

**Feature**: 053-roles-permissions
**Branch**: `053-roles-permissions`
**Estimated Time**: 1-2 hours (scaffolding only)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 052 (BetterAuth) completed
- [x] Git branch `053-roles-permissions` checked out
- [x] Read `specs/053-roles-permissions/spec.md`
- [x] Read `specs/053-roles-permissions/plan.md`
- [x] Read `specs/053-roles-permissions/tasks.md`

## Implementation Overview

**Total Steps**: 6 phases
**Primary Deliverable**: Complete RBAC scaffolding with roles, permissions, decorators, middleware, and frontend helpers
**Validation**: All RBAC modules exist, decorators work, middleware attaches roles, frontend helpers compile

---

## Phase 1: Backend Role Definitions (15 minutes)

### Step 1.1: Create Roles File

**File**: `backend/app/auth/roles.py`

**Action**: Create role constants and permission maps:
- `ROLE_ADMIN`, `ROLE_EDUCATOR`, `ROLE_STUDENT`
- Placeholder permissions mapping
- TODO comments

---

## Phase 2: Permission Checking (20 minutes)

### Step 2.1: Create Permissions File

**File**: `backend/app/auth/permissions.py`

**Action**: Create `has_permission()` function:
- Accepts user_role and action
- Returns placeholder True/False
- TODO comments

### Step 2.2: Update Decorators

**File**: `backend/app/auth/decorators.py`

**Action**: Add decorators:
- `require_role(role)` - Placeholder check
- `require_permission(action)` - Placeholder check
- TODO comments

---

## Phase 3: Role Middleware (15 minutes)

### Step 3.1: Create Role Middleware

**File**: `backend/app/auth/role_middleware.py`

**Action**: Create middleware:
- `extract_role_from_request()` - Placeholder
- `attach_role_middleware()` - Attach role to request.state
- TODO comments

---

## Phase 4: Update Auth Routes (10 minutes)

### Step 4.1: Update /auth/me Endpoint

**File**: `backend/app/auth/routes.py`

**Action**: Modify endpoint to return role:
- Extract role from request.state.user_role
- Include role in response
- Default to "student" if not set

---

## Phase 5: Frontend Role Helpers (20 minutes)

### Step 5.1: Create useRole Hook

**File**: `frontend/src/auth/useRole.ts`

**Action**: Create functions:
- `getRole()` - Get user role
- `isAdmin()`, `isEducator()`, `isStudent()` - Role checks
- All placeholders

---

## Phase 6: Configuration (5 minutes)

### Step 6.1: Update Settings

**File**: `backend/app/config/settings.py`

**Action**: Add `DEFAULT_USER_ROLE = "student"`

---

## Validation Checklist

After implementation, verify:

- [ ] roles.py exists with role constants
- [ ] permissions.py exists with has_permission()
- [ ] decorators.py has require_role() and require_permission()
- [ ] role_middleware.py exists
- [ ] /auth/me returns role in response
- [ ] useRole.ts exists with all functions
- [ ] settings.py has DEFAULT_USER_ROLE
- [ ] Backend starts without errors
- [ ] Frontend builds without errors

---

## Next Steps

After completing scaffolding:

1. Test role attachment in middleware
2. Test decorators on sample routes
3. Test frontend role helpers
4. Implement real RBAC logic in future features

---

## Troubleshooting

**Issue**: Import errors
- **Solution**: Check all __init__.py files exist

**Issue**: Role not attached to request
- **Solution**: Verify middleware is added to FastAPI app

**Issue**: Frontend helpers don't work
- **Solution**: Check useRole.ts imports and API calls

