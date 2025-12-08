# Feature Specification: Chapter Access Control Scaffolding (RBAC-based Chapter Permissions)

**Feature Branch**: `054-chapter-access-control`
**Created**: 2025-01-27
**Status**: Draft
**Type**: backend-authorization-architecture
**Input**: User description: "Add a scaffolding layer that controls which user roles can access specific chapters. This feature introduces: Chapter → Role access map, Permission check placeholder for chapter access, Backend API wrapper enforcing placeholder access, Frontend helpers for showing/hiding chapters. No real RBAC validation. No real auth. Only placeholder structure."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Can Use Chapter Access Control Structure (Priority: P1)

As a developer, I need a placeholder chapter access control system with chapter-to-role mapping and access checking functions, so I can understand how chapter-level access control will work in the future, even though the actual access control logic is not yet implemented.

**Why this priority**: This establishes the foundation for chapter-level access control. Without proper scaffolding, future access control implementation will require restructuring.

**Independent Test**: Can be fully tested by verifying that chapter access map exists, access checking functions exist, decorators work, and API routes are wrapped with placeholder logic.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/auth/chapter_access.py`, **Then** I see `CHAPTER_ACCESS_MAP` with chapters 1, 2, 3 mapped to allowed roles

2. **Given** the feature is implemented, **When** I check `backend/app/auth/permissions.py`, **Then** I see `can_access_chapter()` function that returns placeholder True/False

3. **Given** the feature is implemented, **When** I check `backend/app/auth/decorators.py`, **Then** I see `require_chapter_access()` decorator with placeholder logic

4. **Given** the feature is implemented, **When** I check `backend/app/api/chapters.py`, **Then** I see GET `/chapter/{id}` endpoint wrapped with `require_chapter_access(id)` decorator

5. **Given** the feature is implemented, **When** I check `frontend/src/auth/chapterAccess.ts`, **Then** I see `canViewChapter()` and `chaptersAllowed()` functions with placeholder implementations

---

### User Story 2 - Frontend Can Check Chapter Access (Priority: P2)

As a frontend developer, I need helper functions to check chapter access based on user roles, so I can conditionally show/hide chapters in the UI, even though the actual access control is placeholder.

**Why this priority**: Important for frontend development, but not critical for initial scaffolding. The structure enables incremental implementation.

**Independent Test**: Can be fully tested by verifying that `chapterAccess.ts` exists with placeholder functions for chapter access checking.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I call `canViewChapter(role, chapterNumber)` in frontend, **Then** it returns a placeholder boolean value

2. **Given** the feature is implemented, **When** I call `chaptersAllowed(role)` in frontend, **Then** it returns a list of allowed chapter numbers (placeholder)

---

### Edge Cases

- What happens when a chapter ID doesn't exist in the access map?
  - **Expected**: Default to allowing all roles (or return False)
- What happens when a user role is not in the allowed roles list?
  - **Expected**: Function should return False (placeholder)
- What happens when chapter access check is called with invalid chapter number?
  - **Expected**: Function should return False or handle gracefully

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Backend Chapter Access Map

- **FR-001.1**: System MUST create `backend/app/auth/chapter_access.py`:
  - Define `CHAPTER_ACCESS_MAP: Dict[int, List[str]]`:
    - Key: chapter number (1, 2, 3, ...)
    - Value: List of allowed roles (["admin", "educator", "student"])
  - Default: All roles allowed for all chapters (placeholder)
  - Example:
    ```python
    CHAPTER_ACCESS_MAP = {
        1: ["admin", "educator", "student"],
        2: ["admin", "educator", "student"],
        3: ["admin", "educator", "student"]
    }
    ```
  - TODO markers for real policy logic

#### FR-002: Access Checking Function

- **FR-002.1**: System MUST update `backend/app/auth/permissions.py`:
  - Add function: `can_access_chapter(user_role: str, chapter_number: int) -> bool`:
    - TODO: Check if user_role is in allowed roles for chapter_number
    - Placeholder: return True for all (or based on CHAPTER_ACCESS_MAP)
    - TODO comments explaining expected logic

#### FR-003: Decorator for Chapter Protection

- **FR-003.1**: System MUST update `backend/app/auth/decorators.py`:
  - Add decorator: `require_chapter_access(chapter_number: int)`:
    - TODO: Check if user can access chapter
    - TODO: Read request.state.user_role
    - TODO: Call can_access_chapter()
    - Placeholder enforcement: pass-through with TODO
    - TODO comments only

#### FR-004: API Integration (Scaffold Only)

- **FR-004.1**: System MUST update `backend/app/api/chapters.py`:
  - Wrap GET `/chapter/{id}` endpoint with `require_chapter_access(id)` decorator
  - Placeholder behavior only
  - No real enforcement

#### FR-005: Frontend Awareness Layer

- **FR-005.1**: System MUST create `frontend/src/auth/chapterAccess.ts`:
  - Function: `canViewChapter(role: string, chapterNumber: number) -> boolean`:
    - Placeholder: Check if role can access chapter
    - Return placeholder boolean
  - Function: `chaptersAllowed(role: string) -> number[]`:
    - Placeholder: Return list of allowed chapter numbers for role
    - Return placeholder list

#### FR-006: Contract File

- **FR-006.1**: System MUST create `specs/054-chapter-access-control/contracts/chapter-access.yaml`:
  - High-level description of access rules
  - Chapter → Role mapping structure
  - No actual enforcement schema

#### FR-007: Tests Placeholder

- **FR-007.1**: System MUST create `backend/tests/auth/test_chapter_access.py`:
  - Placeholder test: `test_student_access_placeholder()`
  - Placeholder test: `test_educator_access_placeholder()`
  - Placeholder test: `test_admin_access_placeholder()`
  - All tests are placeholders with TODO comments

## Success Criteria

- ✅ Chapter access map exists
- ✅ Decorators exist and import correctly
- ✅ Chapters API is wrapped with placeholder logic
- ✅ Frontend helpers compile
- ✅ Contract YAML created
- ✅ Backend starts without errors
- ✅ spec.md, plan.md, tasks.md created correctly
- ✅ Contract file created
- ✅ Checklist file created
- ✅ Research, data-model, quickstart files created

## Constraints

- **No Real RBAC Enforcement**: All access checks must be placeholders only
- **Scaffolding Only**: This feature creates structure, not functionality
- **No Database**: No access control persistence required
- **No Real Validation**: No real access enforcement logic

## Dependencies

- Feature 053 (Roles & Permissions) — for role structure
- Feature 052 (BetterAuth) — for auth structure
- Backend chapters API — must exist

## Out of Scope

- Real RBAC enforcement
- Real authorization middleware
- Database-driven permissions
- SSO, OAuth, JWT permission tokens
- Dynamic access control assignment
- Time-based access control
- Chapter subscription model

