# Implementation Plan: User Roles & Permission Scaffolding (RBAC v0)

**Branch**: `053-roles-permissions` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature implements complete scaffolding for role-based access control (RBAC) framework. It introduces static role definitions (admin, educator, student), permission map structure, decorator-based permission checks (scaffold only), middleware placeholder for role injection, and frontend helper for role-awareness. **All implementations are scaffolding only—no real validation, no secure RBAC logic.**

**Primary Deliverable**: Complete RBAC scaffolding structure
**Validation**: All RBAC modules exist, decorators work, middleware attaches roles, frontend helpers compile

---

## 1. Backend Architecture

### 1.1 Role Definitions

**File**: `backend/app/auth/roles.py`

**Purpose**: Define role constants and placeholder permission maps

**Structure**:
```python
ROLE_ADMIN = "admin"
ROLE_EDUCATOR = "educator"
ROLE_STUDENT = "student"

permissions = {
    "admin": ["*"],  # All permissions
    "educator": ["read:chapters", "write:content", "read:analytics", "manage:students"],
    "student": ["read:chapters", "read:content", "read:own_progress"]
}
```

**Integration**: Used by permissions.py and decorators

---

### 1.2 Permission Checking System

**File**: `backend/app/auth/permissions.py`

**Purpose**: Placeholder permission checking logic

**Function**:
- `has_permission(user_role: str, action: str) -> bool`:
  - TODO: Check if user_role has permission for action
  - Placeholder: return True for admin, check permissions map for others
  - TODO comments explaining expected logic

**Integration**: Used by decorators

---

### 1.3 Auth Decorators Update

**File**: `backend/app/auth/decorators.py` (update existing)

**Purpose**: Add role and permission decorators

**Decorators**:
- `require_role(role: str)`:
  - TODO: Check if request.state.user_role matches required role
  - Placeholder: Log message, allow access
- `require_permission(action: str)`:
  - TODO: Check if user has permission for action
  - Placeholder: Log message, allow access

**Integration**: Can be applied to routes

---

### 1.4 Role Middleware

**File**: `backend/app/auth/role_middleware.py`

**Purpose**: Attach role to request state

**Functions**:
- `extract_role_from_request(request) -> Optional[str]`:
  - TODO: Extract role from placeholder source (session, token, etc.)
  - Placeholder: return default role or None
- `attach_role_middleware(request, call_next)`:
  - TODO: Extract role and attach to request.state.user_role
  - Placeholder: Attach default role (e.g., "student")

**Integration**: Add to FastAPI app middleware stack (optional for scaffolding)

---

### 1.5 Auth Routes Update

**File**: `backend/app/auth/routes.py` (update existing)

**Purpose**: Demonstrate role usage in /auth/me endpoint

**Changes**:
- Modify GET `/auth/me` endpoint:
  - Extract role from request.state.user_role (if set)
  - Include role in response: `{user: {role: "<placeholder>"}}`
  - Default to "student" if role not set

---

### 1.6 Settings Update

**File**: `backend/app/config/settings.py` (update existing)

**Purpose**: Add default user role setting

**Changes**:
- Add: `DEFAULT_USER_ROLE: str = "student"`

---

## 2. Frontend Architecture

### 2.1 useRole Hook

**File**: `frontend/src/auth/useRole.ts`

**Purpose**: React hook for role checking

**Functions**:
- `getRole() -> Promise<string | null>`:
  - GET `/auth/me` and extract role
  - Return placeholder role or null
- `isAdmin() -> Promise<boolean>`:
  - Check if role is "admin"
- `isEducator() -> Promise<boolean>`:
  - Check if role is "educator"
- `isStudent() -> Promise<boolean>`:
  - Check if role is "student"

**Integration**: Used by frontend components for conditional rendering

---

## 3. Directory Structure

```
backend/app/auth/
├── roles.py                 # Role constants and permission maps (new)
├── permissions.py           # Permission checking (new)
├── role_middleware.py       # Role attachment middleware (new)
└── decorators.py            # Updated with require_role and require_permission

frontend/src/auth/
└── useRole.ts               # Role helper functions (new)

specs/053-roles-permissions/contracts/
└── rbac.yaml                # RBAC contract (already created)
```

---

## 4. API Contract Design

**File**: `specs/053-roles-permissions/contracts/rbac.yaml` (already created)

**Content**:
- Role model (admin, educator, student)
- Permission structure
- Decorator usage
- Middleware integration
- API response format

---

## 5. Constraints

- **NO Real RBAC Enforcement**: All permission checks must be placeholders
- **NO Database**: No role persistence required
- **NO Real Validation**: No real permission enforcement logic
- **Scaffolding Only**: This feature creates structure, not functionality

---

## 6. Acceptance Criteria Mapping

| Acceptance Criteria | Implementation Location |
|---------------------|------------------------|
| All RBAC modules exist | All files created with placeholder logic |
| No endpoint breaks | All imports resolve correctly |
| role_middleware runs | Middleware created with placeholder logic |
| Frontend compiles | useRole.ts created with placeholder functions |
| specs/rbac.yaml exists | Contract file already created |

---

## 7. Risk Analysis

**Risk 1**: Import errors if auth module structure incorrect
- **Mitigation**: Ensure all `__init__.py` files exist, test imports

**Risk 2**: Decorators may interfere with existing routes
- **Mitigation**: Decorators are optional, can be applied incrementally

**Risk 3**: Middleware may not attach role correctly
- **Mitigation**: Use placeholder default role, test middleware attachment

---

## 8. Future Enhancements

- Real RBAC enforcement
- Database-backed role storage
- Dynamic permission assignment
- Role hierarchies
- Permission inheritance
- User-specific overrides

