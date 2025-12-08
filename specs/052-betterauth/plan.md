# Implementation Plan: BetterAuth Authentication Layer — Scaffolding & Integration

**Branch**: `052-betterauth` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature implements complete scaffolding for BetterAuth-based authentication across the platform. It introduces auth client + server scaffolding, login/signup/logout endpoints (placeholder logic), session validation middleware, frontend auth UI placeholders, and config wiring. **All implementations are scaffolding only—no real authentication, password hashing, or crypto logic.**

**Primary Deliverable**: Complete authentication scaffolding structure
**Validation**: All scaffolded files exist, imports work, frontend components render, backend endpoints return placeholders

---

## 1. Backend Architecture

### 1.1 BetterAuth Client Wrapper

**File**: `backend/app/auth/betterauth_client.py`

**Purpose**: Placeholder wrapper for BetterAuth client initialization and operations

**Functions**:
- `init_client() -> None`:
  - TODO: Initialize BetterAuth client with config
  - Placeholder: print message or no-op
- `get_user(session_token: str) -> Optional[Dict]`:
  - TODO: Retrieve user from BetterAuth
  - Placeholder: return None or placeholder user dict
- `validate_session(session_token: str) -> bool`:
  - TODO: Validate session token via BetterAuth
  - Placeholder: return True

**Integration**: Used by routes and middleware (placeholder calls)

---

### 1.2 Auth Routes

**File**: `backend/app/auth/routes.py`

**Purpose**: FastAPI router with authentication endpoints

**Endpoints**:

1. **POST `/auth/signup`**:
   - Request: `{email: str, password: str, name: Optional[str]}`
   - Response: `{user: Dict, message: str}` (placeholder)
   - No real signup logic

2. **POST `/auth/login`**:
   - Request: `{email: str, password: str}`
   - Response: `{user: Dict, session_token: str}` (placeholder)
   - No real login logic

3. **POST `/auth/logout`**:
   - Request: `{session_token: Optional[str]}`
   - Response: `{message: str}` (placeholder)
   - No real logout logic

4. **GET `/auth/me`**:
   - Headers: Session token from cookie/header (optional)
   - Response: `{user: Dict}` (placeholder user profile)
   - No real user retrieval

**Router Registration**: Include in `backend/app/main.py`

---

### 1.3 Session Middleware

**File**: `backend/app/auth/session_middleware.py`

**Purpose**: Placeholder middleware for session extraction and validation

**Functions**:
- `extract_session_cookie(request) -> Optional[str]`:
  - TODO: Extract session cookie from request
  - Placeholder: return None
- `validate_session_middleware(request, call_next)`:
  - TODO: Validate session via betterauth_client
  - TODO: Attach user to request.state if valid
  - Placeholder: pass through request unchanged

**Integration**: Add to FastAPI app middleware stack (optional for scaffolding)

---

### 1.4 Auth Decorators

**File**: `backend/app/auth/decorators.py`

**Purpose**: Decorator for route protection (placeholder)

**Decorator**:
- `require_auth(func)`:
  - TODO: Check if user is authenticated via request.state
  - TODO: Return 401 if not authenticated
  - Placeholder: Log message, allow access

**Usage**: Can be applied to routes (placeholder behavior)

---

### 1.5 FastAPI App Integration

**File**: `backend/app/main.py`

**Changes**:
- Import auth router: `from app.auth.routes import router as auth_router`
- Include router: `app.include_router(auth_router, prefix="/auth", tags=["auth"])`
- Optional: Add session middleware to middleware stack

---

## 2. Frontend Architecture

### 2.1 useAuth Hook

**File**: `frontend/src/auth/useAuth.ts`

**Purpose**: React hook for authentication operations

**Functions**:
- `login(email: string, password: string) -> Promise<Dict>`:
  - POST to `/auth/login`
  - Return placeholder response
- `signup(email: string, password: string, name?: string) -> Promise<Dict>`:
  - POST to `/auth/signup`
  - Return placeholder response
- `logout() -> Promise<void>`:
  - POST to `/auth/logout`
  - Clear local state (placeholder)
- `getSession() -> Promise<Dict | null>`:
  - GET `/auth/me`
  - Return placeholder user or null

**State Management**: Local state (placeholder, no persistence)

---

### 2.2 Login Form Component

**File**: `frontend/src/components/auth/LoginForm.tsx`

**Props**: None (self-contained)

**UI Elements**:
- Email input field
- Password input field
- "Login" button
- Error display (placeholder)
- Loading state (placeholder)

**Behavior**:
- On submit: Call `useAuth().login()`
- Display placeholder response
- Handle errors (placeholder)

**Styling**: Minimal, functional only

---

### 2.3 Signup Form Component

**File**: `frontend/src/components/auth/SignupForm.tsx`

**Props**: None (self-contained)

**UI Elements**:
- Email input field
- Password input field
- Confirm password field
- Name input field (optional)
- "Signup" button
- Error display (placeholder)
- Loading state (placeholder)

**Behavior**:
- On submit: Call `useAuth().signup()`
- Display placeholder response
- Handle errors (placeholder)

**Styling**: Minimal, functional only

---

### 2.4 Profile Box Component

**File**: `frontend/src/components/auth/ProfileBox.tsx`

**Props**: None (fetches user via `getSession()`)

**UI Elements**:
- Display placeholder user information (email, name)
- "Logout" button
- Loading state (placeholder)

**Behavior**:
- On mount: Call `useAuth().getSession()`
- On logout: Call `useAuth().logout()`
- Display placeholder user data

**Styling**: Minimal, functional only

---

## 3. Directory Structure

```
backend/app/auth/
├── __init__.py
├── betterauth_client.py      # Client wrapper (placeholder)
├── routes.py                 # Auth endpoints
├── session_middleware.py     # Session middleware (placeholder)
└── decorators.py             # Auth decorators (placeholder)

frontend/src/auth/
└── useAuth.ts                # Auth hook

frontend/src/components/auth/
├── LoginForm.tsx
├── SignupForm.tsx
└── ProfileBox.tsx

specs/052-betterauth/contracts/
└── auth-api.yaml             # API contract
```

---

## 4. API Contract Design

**File**: `specs/052-betterauth/contracts/auth-api.yaml`

**Endpoints**:
- POST `/auth/signup`: User registration (placeholder)
- POST `/auth/login`: User authentication (placeholder)
- POST `/auth/logout`: Session termination (placeholder)
- GET `/auth/me`: Current user profile (placeholder)

**Request/Response Schemas**: Defined in contract file
**Error Codes**: Defined in contract file
**Placeholder Examples**: Included in contract file

---

## 5. Configuration Layer

### 5.1 Settings Update

**File**: `backend/app/config/settings.py`

**Additions**:
```python
BETTERAUTH_PUBLIC_KEY: Optional[str] = None  # From env
BETTERAUTH_SECRET_KEY: Optional[str] = None  # From env
BETTERAUTH_ISSUER: Optional[str] = "interactive-agentic-book"  # From env, default
```

**Source**: Environment variables (all optional for scaffolding)

---

### 5.2 Environment Variables

**File**: `.env.example`

**Additions**:
```bash
# BetterAuth Configuration (optional for scaffolding)
# BETTERAUTH_PUBLIC_KEY=
# BETTERAUTH_SECRET_KEY=
# BETTERAUTH_ISSUER=interactive-agentic-book
```

---

## 6. Constraints

- **NO Real Auth Logic**: All authentication, password hashing, session management must be placeholders
- **NO Crypto**: No password hashing, JWT signing, or crypto operations
- **NO Database**: No user persistence required
- **NO OAuth/SSO**: Out of scope
- **Scaffolding Only**: This feature creates structure, not functionality

---

## 7. Acceptance Criteria Mapping

| Acceptance Criteria | Implementation Location |
|---------------------|------------------------|
| All file paths exist | All files created with placeholder logic |
| Backend starts without errors | All imports resolve correctly |
| Frontend builds without errors | All components compile |
| Auth endpoints return placeholder responses | All endpoints return static placeholders |
| Middleware + decorators exist with TODOs | All files created with TODO comments |
| Env vars present in .env.example | Settings and .env.example updated |

---

## 8. Risk Analysis

**Risk 1**: Import errors if auth module structure incorrect
- **Mitigation**: Ensure all `__init__.py` files exist, test imports

**Risk 2**: Frontend components may not integrate with routing
- **Mitigation**: Create standalone components, integration in future features

**Risk 3**: Middleware may interfere with existing routes
- **Mitigation**: Make middleware optional, add as separate step

---

## 9. Future Enhancements

- Real password hashing (bcrypt, argon2)
- Real session management (cookies, JWT)
- Real user database persistence
- OAuth/SSO integration
- Multi-factor authentication
- Password reset flow
- Email verification

