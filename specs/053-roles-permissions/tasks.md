# Implementation Tasks: User Roles & Permission Scaffolding

**Feature**: 053-roles-permissions  
**Date**: 2025-01-27  
**Status**: Draft

## Task Groups

### A. Backend Tasks

- [ ] **T001**: Create `backend/app/auth/roles.py` with role constants + placeholder permissions
  - Define: `ROLE_ADMIN = "admin"`, `ROLE_EDUCATOR = "educator"`, `ROLE_STUDENT = "student"`
  - Create placeholder permissions mapping dictionary
  - TODO comments for real logic
  - File: `backend/app/auth/roles.py`

- [ ] **T002**: Create `backend/app/auth/permissions.py` with has_permission() placeholder
  - Function: `has_permission(user_role: str, action: str) -> bool`
  - TODO: Check if user_role has permission for action
  - Placeholder: return True for admin, False for others (or based on permissions map)
  - TODO comments explaining expected logic
  - File: `backend/app/auth/permissions.py`

- [ ] **T003**: Update `backend/app/auth/decorators.py` with require_role + require_permission decorators
  - Add decorator: `require_role(role: str)`
    - TODO: Check if request.state.user_role matches required role
    - Placeholder: Log message, allow access
  - Add decorator: `require_permission(action: str)`
    - TODO: Check if user has permission for action
    - Placeholder: Log message, allow access
  - Both with TODO comments
  - File: `backend/app/auth/decorators.py` (update existing)

- [ ] **T004**: Create `backend/app/auth/role_middleware.py` to attach placeholder role to request.state
  - Function: `extract_role_from_request(request) -> Optional[str]`
    - TODO: Extract role from placeholder source
    - Placeholder: return default role or None
  - Function: `attach_role_middleware(request, call_next)`
    - TODO: Extract role and attach to request.state.user_role
    - Placeholder: Attach default role (e.g., "student")
  - All logic is placeholder with TODO comments
  - File: `backend/app/auth/role_middleware.py`

- [ ] **T005**: Modify `backend/app/auth/routes.py` to return role in /auth/me
  - Update GET `/auth/me` endpoint
  - Extract role from request.state.user_role (if set)
  - Include role in response: `{user: {role: "<placeholder>"}}`
  - Default to "student" if role not set
  - File: `backend/app/auth/routes.py` (update existing)

- [ ] **T006**: Update `backend/app/config/settings.py` with DEFAULT_USER_ROLE
  - Add: `DEFAULT_USER_ROLE: str = "student"`
  - File: `backend/app/config/settings.py` (update existing)

---

### B. Frontend Tasks

- [ ] **T007**: Create `frontend/src/auth/useRole.ts`
  - File: `frontend/src/auth/useRole.ts`

- [ ] **T008**: Implement placeholder functions: getRole(), isAdmin(), isEducator(), isStudent()
  - Function: `getRole() -> Promise<string | null>` (GET /auth/me and extract role)
  - Function: `isAdmin() -> Promise<boolean>` (check if role is "admin")
  - Function: `isEducator() -> Promise<boolean>` (check if role is "educator")
  - Function: `isStudent() -> Promise<boolean>` (check if role is "student")
  - All return placeholder values
  - File: `frontend/src/auth/useRole.ts`

---

### C. Contract Tasks

- [ ] **T009**: Create `specs/053-roles-permissions/contracts/rbac.yaml`
  - Document the role model
  - Document how permissions are structured
  - Document decorator usage
  - File: `specs/053-roles-permissions/contracts/rbac.yaml` (already created)

---

### D. Validation Tasks

- [ ] **T010**: Ensure backend runs without errors
  - Verify: `cd backend && uvicorn app.main:app --reload` starts without errors
  - Check: All imports resolve correctly

- [ ] **T011**: Ensure frontend builds without errors
  - Verify: `cd frontend && npm run build` succeeds
  - Check: All components compile

---

## Implementation Notes

- All backend functions must have TODO comments explaining expected behavior
- All frontend functions must be placeholder implementations
- No real RBAC enforcement logic should be implemented
- All responses are static placeholders
- Role middleware is optional (can be added to app later)

