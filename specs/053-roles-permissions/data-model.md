# Data Model: User Roles & Permission Scaffolding

**Feature**: 053-roles-permissions
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for RBAC system

## Entity Definitions

### 1. Role (Primary Entity)

**Description**: Represents a user role in the system

**Storage**: Static constants (not persisted in scaffolding)

**Structure**:
```python
Role = str  # "admin" | "educator" | "student"

# Constants
ROLE_ADMIN = "admin"
ROLE_EDUCATOR = "educator"
ROLE_STUDENT = "student"
```

**Role Definitions**:
- `admin`: Administrator with full system access
- `educator`: Educator with content management access
- `student`: Student with read-only access

---

### 2. Permission (Primary Entity)

**Description**: Represents a permission action in the system

**Storage**: Static permission maps (not persisted in scaffolding)

**Structure**:
```python
Permission = str  # Format: "{action}:{resource}"

# Examples
"read:chapters"
"write:content"
"read:analytics"
"manage:students"
```

**Permission Format**:
- Action: `read`, `write`, `manage`, `delete`
- Resource: `chapters`, `content`, `analytics`, `students`

---

### 3. Permission Map (Configuration Entity)

**Description**: Maps roles to their permissions

**Storage**: Static dictionary in `backend/app/auth/roles.py`

**Structure**:
```python
permissions = {
    "admin": ["*"],  # All permissions
    "educator": [
        "read:chapters",
        "write:content",
        "read:analytics",
        "manage:students"
    ],
    "student": [
        "read:chapters",
        "read:content",
        "read:own_progress"
    ]
}
```

---

### 4. User with Role (Extended Entity)

**Description**: User entity extended with role information

**Storage**: Transient (in request.state during request)

**Structure**:
```python
UserWithRole = {
    "id": str,
    "email": str,
    "name": str,
    "role": str,  # "admin" | "educator" | "student"
    "created_at": datetime
}
```

**Example**:
```python
{
    "id": "user_123",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "student",
    "created_at": "2025-01-27T00:00:00Z"
}
```

---

## Relationships

### Role → Permissions
- One role has many permissions
- Permissions are defined in permission map
- Admin role has all permissions ("*")

### User → Role
- One user has one role
- Role is attached to request.state.user_role
- Default role: "student"

### Request → Role
- One request has one role (via middleware)
- Role attached to request.state.user_role
- Extracted from session/token (placeholder)

---

## Data Flow

### Role Attachment Flow
```
Request arrives
  → role_middleware extracts role (placeholder)
  → Attach to request.state.user_role
  → Route handler can access role
```

### Permission Check Flow
```
Route handler
  → require_permission("write:content") decorator
  → Check request.state.user_role
  → Check permissions map
  → Allow or deny (placeholder: always allow)
```

### Role Check Flow
```
Route handler
  → require_role("admin") decorator
  → Check request.state.user_role
  → Allow or deny (placeholder: always allow)
```

---

## Notes

- All data structures are static (not persisted)
- Roles are constants, not database entities
- Permissions are defined in code, not database
- Future: Database-backed roles and permissions
- Future: Dynamic permission assignment
- Future: Role hierarchies

