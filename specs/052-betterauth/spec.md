# Feature Specification: BetterAuth Authentication Layer — Scaffolding & Integration

**Feature Branch**: `052-betterauth`
**Created**: 2025-01-27
**Status**: Draft
**Type**: auth-architecture
**Input**: User description: "Add complete scaffolding for BetterAuth-based authentication across the platform. This feature introduces: Auth client + server scaffolding, Login, signup, logout endpoints (placeholder logic), Session validation middleware, Frontend auth UI placeholders, Config wiring and env vars. No real authentication or crypto logic is implemented."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - User Can Access Authentication UI (Priority: P1)

As a user, I need to see login and signup forms in the frontend, so I can understand how authentication will work in the future, even though the actual authentication logic is not yet implemented.

**Why this priority**: This establishes the foundation for authentication. Without UI scaffolding, future authentication implementation will require frontend restructuring.

**Independent Test**: Can be fully tested by verifying that login and signup forms exist in the frontend, they render correctly, and they make placeholder API calls to backend endpoints.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I navigate to the login page, **Then** I see a LoginForm component with email and password fields

2. **Given** the feature is implemented, **When** I navigate to the signup page, **Then** I see a SignupForm component with email, password, and confirm password fields

3. **Given** the feature is implemented, **When** I submit the login form, **Then** the frontend sends a POST request to `/auth/login` and receives a placeholder response

4. **Given** the feature is implemented, **When** I submit the signup form, **Then** the frontend sends a POST request to `/auth/signup` and receives a placeholder response

---

### User Story 2 - Developer Can Extend Authentication System (Priority: P2)

As a developer, I need a complete scaffolding structure for BetterAuth authentication with clear separation between client, server, routes, middleware, and decorators, so I can implement real authentication logic in future features without restructuring the codebase.

**Why this priority**: Important for maintainability and future development, but not critical for initial scaffolding. The structure enables incremental implementation.

**Independent Test**: Can be fully tested by verifying all required files exist at specified paths, all imports resolve without errors, and the authentication structure is clear and extensible.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/auth/betterauth_client.py`, **Then** I see placeholder functions: `init_client()`, `get_user()`, `validate_session()` with TODO comments

2. **Given** the feature is implemented, **When** I check `backend/app/auth/routes.py`, **Then** I see placeholder endpoints: `/auth/signup`, `/auth/login`, `/auth/logout`, `/auth/me` with placeholder responses

3. **Given** the feature is implemented, **When** I check `backend/app/auth/session_middleware.py`, **Then** I see placeholder middleware with TODO comments for session extraction and validation

4. **Given** the feature is implemented, **When** I check `backend/app/auth/decorators.py`, **Then** I see `require_auth` decorator with placeholder logic

---

### Edge Cases

- What happens when authentication credentials are invalid?
  - **Expected**: Backend should return placeholder error response (no real validation)
- What happens when session is missing or invalid?
  - **Expected**: Middleware should pass through with TODO comment (no real validation)
- What happens when user tries to access protected route without auth?
  - **Expected**: Decorator should log message but allow access (placeholder behavior)

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Backend Setup (Scaffold Only)

- **FR-001.1**: System MUST create `backend/app/auth/betterauth_client.py`:
  - Function: `init_client() -> None`:
    - TODO: Initialize BetterAuth client with config
    - Placeholder: print message or no-op
  - Function: `get_user(session_token: str) -> Optional[Dict]`:
    - TODO: Retrieve user from BetterAuth
    - Placeholder: return None or placeholder user dict
  - Function: `validate_session(session_token: str) -> bool`:
    - TODO: Validate session token
    - Placeholder: return True
  - All functions contain TODO comments only

- **FR-001.2**: System MUST create `backend/app/auth/routes.py`:
  - POST `/auth/signup` endpoint:
    - Request: `{email: str, password: str, name: Optional[str]}`
    - Response: `{user: Dict, message: str}` (placeholder)
    - No real signup logic
  - POST `/auth/login` endpoint:
    - Request: `{email: str, password: str}`
    - Response: `{user: Dict, session_token: str}` (placeholder)
    - No real login logic
  - POST `/auth/logout` endpoint:
    - Request: `{session_token: str}` (optional)
    - Response: `{message: str}` (placeholder)
    - No real logout logic
  - GET `/auth/me` endpoint:
    - Request: Session token from cookie/header
    - Response: `{user: Dict}` (placeholder user profile)
    - No real user retrieval

- **FR-001.3**: System MUST create `backend/app/auth/session_middleware.py`:
  - Function: `extract_session_cookie(request) -> Optional[str]`:
    - TODO: Extract session cookie from request
    - Placeholder: return None
  - Function: `validate_session_middleware(request, call_next)`:
    - TODO: Validate session via betterauth_client
    - TODO: Attach user to request.state if valid
    - Placeholder: pass through request
  - All logic is placeholder with TODO comments

#### FR-002: Frontend Integration (Scaffold)

- **FR-002.1**: System MUST create `frontend/src/auth/useAuth.ts`:
  - Function: `login(email: string, password: string) -> Promise<Dict>`:
    - Placeholder: POST to `/auth/login`
    - Return placeholder response
  - Function: `signup(email: string, password: string, name?: string) -> Promise<Dict>`:
    - Placeholder: POST to `/auth/signup`
    - Return placeholder response
  - Function: `logout() -> Promise<void>`:
    - Placeholder: POST to `/auth/logout`
    - Clear local state (placeholder)
  - Function: `getSession() -> Promise<Dict | null>`:
    - Placeholder: GET `/auth/me`
    - Return placeholder user or null
  - All functions are placeholder implementations

- **FR-002.2**: System MUST create `frontend/src/components/auth/LoginForm.tsx`:
  - Email input field
  - Password input field
  - "Login" button
  - Error display (placeholder)
  - Calls `useAuth().login()` on submit
  - Minimal styling

- **FR-002.3**: System MUST create `frontend/src/components/auth/SignupForm.tsx`:
  - Email input field
  - Password input field
  - Confirm password field
  - Name input field (optional)
  - "Signup" button
  - Error display (placeholder)
  - Calls `useAuth().signup()` on submit
  - Minimal styling

- **FR-002.4**: System MUST create `frontend/src/components/auth/ProfileBox.tsx`:
  - Display placeholder user information
  - "Logout" button
  - Calls `useAuth().logout()` on logout
  - Minimal styling

#### FR-003: Shared API Contract

- **FR-003.1**: System MUST create `specs/052-betterauth/contracts/auth-api.yaml`:
  - Define request/response for:
    - POST `/auth/signup`
    - POST `/auth/login`
    - POST `/auth/logout`
    - GET `/auth/me`
  - Placeholder schemas, no real authentication rules
  - Error response format

#### FR-004: .env + Settings Update

- **FR-004.1**: System MUST update `backend/app/config/settings.py`:
  - Add `BETTERAUTH_PUBLIC_KEY: Optional[str]` (from env)
  - Add `BETTERAUTH_SECRET_KEY: Optional[str]` (from env)
  - Add `BETTERAUTH_ISSUER: Optional[str]` (from env, default: "interactive-agentic-book")
  - All settings are optional (scaffolding only)

- **FR-004.2**: System MUST update `.env.example`:
  - Add `BETTERAUTH_PUBLIC_KEY=` (commented)
  - Add `BETTERAUTH_SECRET_KEY=` (commented)
  - Add `BETTERAUTH_ISSUER=` (commented)

#### FR-005: Protect API Routes (Scaffold)

- **FR-005.1**: System MUST create `backend/app/auth/decorators.py`:
  - Function: `require_auth(func)` decorator:
    - TODO: Check if user is authenticated
    - TODO: Return 401 if not authenticated
    - Placeholder: Log message, allow access
    - No real permission logic

## Success Criteria

- ✅ All file paths exist
- ✅ Backend starts without errors
- ✅ Frontend builds without errors
- ✅ Auth endpoints return placeholder static responses
- ✅ Middleware + decorators exist with TODOs
- ✅ Env vars present in .env.example
- ✅ spec.md, plan.md, tasks.md created correctly
- ✅ Contract file created
- ✅ Checklist file created
- ✅ Research, data-model, quickstart files created

## Constraints

- **No Real Auth Logic**: All authentication, password hashing, session management must be placeholders only
- **Scaffolding Only**: This feature creates structure, not functionality
- **No Database**: No user persistence required
- **No Crypto**: No password hashing, JWT signing, or crypto operations
- **No OAuth/SSO**: Out of scope for this feature

## Dependencies

- FastAPI for backend routes
- React/TypeScript for frontend components
- BetterAuth library structure (scaffolding only, no real library dependency)

## Out of Scope

- Real password hashing
- Session cookies
- OAuth / SSO
- Multi-factor authentication
- JWT signing or verification
- User database persistence
- Real session management
- Password reset functionality

