# Data Model: Chapter Access Control Scaffolding

**Feature**: 054-chapter-access-control
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for chapter access control system

## Entity Definitions

### 1. Chapter Access Map (Configuration Entity)

**Description**: Maps chapters to allowed roles

**Storage**: Static dictionary in `backend/app/auth/chapter_access.py`

**Structure**:
```python
CHAPTER_ACCESS_MAP: Dict[int, List[str]] = {
    1: ["admin", "educator", "student"],
    2: ["admin", "educator", "student"],
    3: ["admin", "educator", "student"]
}
```

**Format**:
- Key: Chapter number (int)
- Value: List of allowed roles (List[str])

**Default**: All roles allowed for all chapters

---

### 2. Chapter Access Check (Processing Entity)

**Description**: Result of chapter access check

**Storage**: In-memory during processing

**Structure**:
```python
AccessCheckResult = {
    "chapter_number": int,
    "user_role": str,
    "allowed": bool,
    "reason": Optional[str]  # Why access allowed/denied
}
```

**Example**:
```python
{
    "chapter_number": 1,
    "user_role": "student",
    "allowed": True,
    "reason": "Role in allowed list"
}
```

---

## Relationships

### Chapter → Roles
- One chapter has many allowed roles
- Roles are defined in access map
- Default: All roles allowed

### User Role → Chapter Access
- One role can access multiple chapters
- Access determined by access map
- Can be checked via can_access_chapter()

### Request → Chapter Access
- One request checks one chapter access
- Access checked via decorator
- Result attached to request (future)

---

## Data Flow

### Access Check Flow
```
Request to GET /chapter/{id}
  → require_chapter_access(id) decorator
  → Extract user_role from request.state
  → Call can_access_chapter(user_role, id)
  → Check CHAPTER_ACCESS_MAP
  → Allow or deny (placeholder: always allow)
```

### Frontend Check Flow
```
Frontend component
  → Call canViewChapter(role, chapterNumber)
  → Check access map (placeholder)
  → Return boolean
  → Conditionally render chapter
```

---

## Notes

- All data structures are static (not persisted)
- Access map is defined in code, not database
- Future: Database-backed access control
- Future: Dynamic access assignment
- Future: User-specific overrides

