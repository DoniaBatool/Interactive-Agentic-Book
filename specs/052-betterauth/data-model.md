# Data Model: BetterAuth Authentication Layer

**Feature**: 052-betterauth
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for authentication system

## Entity Definitions

### 1. User (Primary Entity)

**Description**: Represents a user account in the system

**Storage**: Future database (not implemented in scaffolding)

**Structure**:
```python
User = {
    "id": str,              # Unique user ID
    "email": str,           # User's email address
    "name": Optional[str],  # User's full name
    "role": str,            # User role (student, educator, admin)
    "created_at": datetime, # Account creation timestamp
    "updated_at": datetime  # Last update timestamp
}
```

**Placeholder Example**:
```python
{
    "id": "user_123",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "student",
    "created_at": "2025-01-27T00:00:00Z",
    "updated_at": "2025-01-27T00:00:00Z"
}
```

---

### 2. Session (Primary Entity)

**Description**: Represents an active user session

**Storage**: Future database or cache (not implemented in scaffolding)

**Structure**:
```python
Session = {
    "token": str,           # Session token
    "user_id": str,         # Associated user ID
    "expires_at": datetime, # Session expiration
    "created_at": datetime  # Session creation timestamp
}
```

**Placeholder Example**:
```python
{
    "token": "placeholder_session_token_123",
    "user_id": "user_123",
    "expires_at": "2025-01-28T00:00:00Z",
    "created_at": "2025-01-27T00:00:00Z"
}
```

---

### 3. Signup Request (Data Transfer Object)

**Description**: Request for user registration

**Structure**:
```python
SignupRequest = {
    "email": str,           # Required, valid email format
    "password": str,        # Required, min 8 chars
    "name": Optional[str]   # Optional, max 100 chars
}
```

**Validation Rules**:
- Email: Valid email format
- Password: Min 8 characters, max 128 characters
- Name: Optional, max 100 characters

---

### 4. Login Request (Data Transfer Object)

**Description**: Request for user authentication

**Structure**:
```python
LoginRequest = {
    "email": str,    # Required, valid email format
    "password": str   # Required
}
```

**Validation Rules**:
- Email: Valid email format
- Password: Required

---

### 5. Auth Response (Data Transfer Object)

**Description**: Response from authentication endpoints

**Structure** (varies by endpoint):

**Signup Response**:
```python
{
    "user": User,
    "message": str  # "User created successfully (placeholder)"
}
```

**Login Response**:
```python
{
    "user": User,
    "session_token": str  # Placeholder session token
}
```

**Logout Response**:
```python
{
    "message": str  # "Logged out successfully (placeholder)"
}
```

**Me Response**:
```python
{
    "user": User
}
```

---

## Relationships

### User → Session
- One user can have multiple sessions
- One session belongs to one user
- Sessions expire after timeout

### Request → Response
- One signup request produces one signup response
- One login request produces one login response
- One logout request produces one logout response

---

## Data Flow

### Signup Flow
```
Frontend SignupForm
  → POST /auth/signup
    → Backend validates request
    → Backend creates placeholder user
    → Backend returns user + message
```

### Login Flow
```
Frontend LoginForm
  → POST /auth/login
    → Backend validates credentials (placeholder)
    → Backend creates placeholder session
    → Backend returns user + session_token
```

### Logout Flow
```
Frontend ProfileBox
  → POST /auth/logout
    → Backend invalidates session (placeholder)
    → Backend returns message
```

### Session Validation Flow
```
Request with session token
  → Middleware extracts token
  → Middleware validates token (placeholder)
  → Middleware attaches user to request.state
  → Route handler processes request
```

---

## Notes

- All data structures are placeholders
- No real persistence in scaffolding
- No real validation in scaffolding
- Future: Real database integration
- Future: Real session management
- Future: Real password hashing

