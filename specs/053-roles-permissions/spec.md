# Feature Specification: User Roles & Permission Scaffolding (RBAC v0)

**Feature Branch**: `053-roles-permissions`
**Created**: 2025-01-27
**Status**: Draft
**Type**: auth-architecture
**Input**: User description: "Add a placeholder RBAC (role-based access control) framework to the backend. This feature introduces: Static role definitions (admin, educator, student), Permission map structure, Decorator-based permission checks (scaffold only), Middleware placeholder for role injection, Frontend helper for role-awareness. No real validation, no secure RBAC logic, only scaffolding."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Can Use Role-Based Access Control Structure (Priority: P1)

As a developer, I need a placeholder RBAC framework with role definitions, permission maps, and decorators, so I can understand how role-based access control will work in the future, even though the actual RBAC logic is not yet implemented.

**Why this priority**: This establishes the foundation for role-based access control. Without proper scaffolding, future RBAC implementation will require restructuring.

**Independent Test**: Can be fully tested by verifying that role definitions exist, permission maps are structured, decorators exist, and middleware can inject roles into requests.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/auth/roles.py`, **Then** I see role constants (ROLE_ADMIN, ROLE_EDUCATOR, ROLE_STUDENT) and placeholder permission maps

2. **Given** the feature is implemented, **When** I check `backend/app/auth/permissions.py`, **Then** I see `has_permission()` function that returns placeholder True/False

3. **Given** the feature is implemented, **When** I check `backend/app/auth/decorators.py`, **Then** I see `require_role()` and `require_permission()` decorators with placeholder logic

4. **Given** the feature is implemented, **When** I check `backend/app/auth/role_middleware.py`, **Then** I see middleware that attaches placeholder role to request.state.user_role

5. **Given** the feature is implemented, **When** I call GET `/auth/me`, **Then** I receive a response with `{user: {role: "<placeholder>"}}`

---

### User Story 2 - Frontend Can Check User Roles (Priority: P2)

As a frontend developer, I need helper functions to check user roles, so I can conditionally render UI elements based on user roles, even though the actual role data is placeholder.

**Why this priority**: Important for frontend development, but not critical for initial scaffolding. The structure enables incremental implementation.

**Independent Test**: Can be fully tested by verifying that `useRole.ts` exists with placeholder functions for role checking.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `frontend/src/auth/useRole.ts`, **Then** I see functions: `getRole()`, `isAdmin()`, `isEducator()`, `isStudent()` with placeholder implementations

2. **Given** the feature is implemented, **When** I call `isAdmin()` in frontend, **Then** it returns a placeholder boolean value

---

### Edge Cases

- What happens when a user has no role assigned?
  - **Expected**: Default role should be used (e.g., ROLE_STUDENT)
- What happens when a permission check is called with invalid role?
  - **Expected**: Function should return False (placeholder)
- What happens when middleware cannot extract role?
  - **Expected**: Middleware should attach default role or None

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Backend Role Definitions

- **FR-001.1**: System MUST create `backend/app/auth/roles.py`:
  - Define role constants:
    - `ROLE_ADMIN = "admin"`
    - `ROLE_EDUCATOR = "educator"`
    - `ROLE_STUDENT = "student"`
  - Define placeholder permissions mapping:
    ```python
    permissions = {
        "admin": ["*"],  # All permissions
        "educator": ["read:chapters", "write:content", "read:analytics"],
        "student": ["read:chapters", "read:content"]
    }
    ```
  - TODO markers for real logic

#### FR-002: Permission Checking System (Scaffold)

- **FR-002.1**: System MUST create or update `backend/app/auth/permissions.py`:
  - Function: `has_permission(user_role: str, action: str) -> bool`:
    - TODO: Check if user_role has permission for action
    - Placeholder: return True for admin, False for others (or based on permissions map)
    - TODO comments explaining expected logic

- **FR-002.2**: System MUST update `backend/app/auth/decorators.py`:
  - Add decorator: `require_role(role: str)`:
    - TODO: Check if request.state.user_role matches required role
    - Placeholder: Log message, allow access
  - Add decorator: `require_permission(action: str)`:
    - TODO: Check if user has permission for action
    - Placeholder: Log message, allow access
  - Both decorators contain TODO comments only

#### FR-003: Middleware to Attach Role to Request

- **FR-003.1**: System MUST create `backend/app/auth/role_middleware.py`:
  - Function: `extract_role_from_request(request) -> Optional[str]`:
    - TODO: Extract role from placeholder source (session, token, etc.)
    - Placeholder: return default role or None
  - Function: `attach_role_middleware(request, call_next)`:
    - TODO: Extract role and attach to request.state.user_role
    - Placeholder: Attach default role (e.g., "student")
  - All logic is placeholder with TODO comments

#### FR-004: Update Auth Routes to Demonstrate Role Use

- **FR-004.1**: System MUST update `backend/app/auth/routes.py`:
  - Modify GET `/auth/me` endpoint:
    - Return `{user: {role: "<placeholder>"}}` in response
    - Role should come from request.state.user_role (if set) or default

#### FR-005: API Contract

- **FR-005.1**: System MUST create `specs/053-roles-permissions/contracts/rbac.yaml`:
  - Document the role model (admin, educator, student)
  - Document how permissions are structured
  - Document decorator usage
  - No real enforcement logic

#### FR-006: Frontend Role Awareness

- **FR-006.1**: System MUST create `frontend/src/auth/useRole.ts`:
  - Function: `getRole() -> Promise<string | null>`:
    - Placeholder: GET `/auth/me` and extract role
    - Return placeholder role or null
  - Function: `isAdmin() -> Promise<boolean>`:
    - Placeholder: Check if role is admin
  - Function: `isEducator() -> Promise<boolean>`:
    - Placeholder: Check if role is educator
  - Function: `isStudent() -> Promise<boolean>`:
    - Placeholder: Check if role is student
  - All functions are placeholder implementations

#### FR-007: .env + config

- **FR-007.1**: System MUST update `backend/app/config/settings.py`:
  - Add `DEFAULT_USER_ROLE: str = "student"` (placeholder default role)
  - No new env vars required

## Success Criteria

- ✅ All RBAC modules exist exactly as described
- ✅ No endpoint breaks due to missing imports
- ✅ role_middleware runs but contains only placeholder logic
- ✅ Frontend compiles successfully
- ✅ specs/rbac.yaml exists
- ✅ Backend starts without errors
- ✅ spec.md, plan.md, tasks.md created correctly
- ✅ Contract file created
- ✅ Checklist file created
- ✅ Research, data-model, quickstart files created

## Constraints

- **No Real RBAC Enforcement**: All permission checks must be placeholders only
- **Scaffolding Only**: This feature creates structure, not functionality
- **No Database**: No role persistence required
- **No Real Validation**: No real permission enforcement logic

## Dependencies

- Feature 052 (BetterAuth) — for auth structure
- FastAPI for backend decorators
- React/TypeScript for frontend

## Out of Scope

- Real RBAC enforcement
- Database-backed permission storage
- OAuth scopes
- User-specific overrides
- Dynamic permission assignment
- Permission inheritance
- Role hierarchies

