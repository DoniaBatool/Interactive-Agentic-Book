# Implementation Plan: Chapter Access Control Scaffolding (RBAC-based Chapter Permissions)

**Branch**: `054-chapter-access-control` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature implements complete scaffolding for chapter-level access control based on RBAC. It introduces chapter-to-role access map, permission check placeholder for chapter access, backend API wrapper enforcing placeholder access, and frontend helpers for showing/hiding chapters. **All implementations are scaffolding only—no real RBAC validation, no real auth enforcement.**

**Primary Deliverable**: Complete chapter access control scaffolding structure
**Validation**: All access control modules exist, decorators work, API routes wrapped, frontend helpers compile

---

## 1. Backend Architecture

### 1.1 Chapter Access Map

**File**: `backend/app/auth/chapter_access.py`

**Purpose**: Define chapter-to-role access mapping

**Structure**:
```python
CHAPTER_ACCESS_MAP: Dict[int, List[str]] = {
    1: ["admin", "educator", "student"],
    2: ["admin", "educator", "student"],
    3: ["admin", "educator", "student"]
}
```

**Default**: All roles allowed for all chapters (placeholder)

**Integration**: Used by permissions.py for access checking

---

### 1.2 Access Checking Function

**File**: `backend/app/auth/permissions.py` (update existing)

**Purpose**: Add chapter access checking function

**Function**:
- `can_access_chapter(user_role: str, chapter_number: int) -> bool`:
  - TODO: Check if user_role is in allowed roles for chapter_number
  - Placeholder: return True for all (or based on CHAPTER_ACCESS_MAP)
  - TODO comments explaining expected logic

**Integration**: Used by decorators

---

### 1.3 Chapter Access Decorator

**File**: `backend/app/auth/decorators.py` (update existing)

**Purpose**: Add decorator for chapter access protection

**Decorator**:
- `require_chapter_access(chapter_number: int)`:
  - TODO: Check if user can access chapter
  - TODO: Read request.state.user_role
  - TODO: Call can_access_chapter()
  - Placeholder enforcement: pass-through with TODO
  - TODO comments only

**Integration**: Applied to chapter endpoints

---

### 1.4 API Integration

**File**: `backend/app/api/chapters.py` (update existing)

**Purpose**: Wrap chapter endpoint with access control

**Changes**:
- Wrap GET `/chapter/{id}` endpoint with `require_chapter_access(id)` decorator
- Placeholder behavior only
- No real enforcement

---

### 1.5 Test Placeholders

**File**: `backend/tests/auth/test_chapter_access.py` (new)

**Purpose**: Placeholder tests for chapter access

**Tests**:
- `test_student_access_placeholder()`
- `test_educator_access_placeholder()`
- `test_admin_access_placeholder()`
- All with TODO comments

---

## 2. Frontend Architecture

### 2.1 Chapter Access Helpers

**File**: `frontend/src/auth/chapterAccess.ts`

**Purpose**: Helper functions for chapter access checking

**Functions**:
- `canViewChapter(role: string, chapterNumber: number) -> boolean`:
  - Placeholder: Check if role can access chapter
  - Return placeholder boolean
- `chaptersAllowed(role: string) -> number[]`:
  - Placeholder: Return list of allowed chapter numbers for role
  - Return placeholder list

**Integration**: Used by frontend components for conditional rendering

---

## 3. Directory Structure

```
backend/app/auth/
├── chapter_access.py        # Chapter access map (new)
└── permissions.py           # Updated with can_access_chapter()

backend/app/api/
└── chapters.py              # Updated with decorator

backend/tests/auth/
└── test_chapter_access.py   # Placeholder tests (new)

frontend/src/auth/
└── chapterAccess.ts         # Chapter access helpers (new)

specs/054-chapter-access-control/contracts/
└── chapter-access.yaml      # Access control contract (already created)
```

---

## 4. Constraints

- **NO Real RBAC Enforcement**: All access checks must be placeholders
- **NO Database**: No access control persistence required
- **NO Real Validation**: No real access enforcement logic
- **Scaffolding Only**: This feature creates structure, not functionality

---

## 5. Acceptance Criteria Mapping

| Acceptance Criteria | Implementation Location |
|---------------------|------------------------|
| Chapter access map exists | chapter_access.py created |
| Decorators exist and import correctly | decorators.py updated |
| Chapters API is wrapped | chapters.py updated |
| Frontend helpers compile | chapterAccess.ts created |
| Contract YAML created | chapter-access.yaml already created |
| Backend starts without errors | All imports resolve correctly |

---

## 6. Risk Analysis

**Risk 1**: Import errors if auth module structure incorrect
- **Mitigation**: Ensure all `__init__.py` files exist, test imports

**Risk 2**: Decorator may interfere with existing routes
- **Mitigation**: Decorator is optional, can be applied incrementally

**Risk 3**: Access map may not be complete
- **Mitigation**: Default to all roles allowed, easy to extend

---

## 7. Future Enhancements

- Real access enforcement
- Database-backed access control
- Dynamic access assignment
- Time-based access
- Chapter subscription model
- User-specific overrides

