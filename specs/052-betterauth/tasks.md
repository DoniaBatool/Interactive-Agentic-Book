# Implementation Tasks: BetterAuth Authentication Layer

**Feature**: 052-betterauth  
**Date**: 2025-01-27  
**Status**: Draft

## Task Groups

### A. Backend Tasks

- [ ] **T001**: Create `backend/app/auth/__init__.py` to make auth a package
  - File: `backend/app/auth/__init__.py`

- [ ] **T002**: Create `backend/app/auth/betterauth_client.py` with placeholder class + TODO functions
  - Function: `init_client() -> None` (TODO: Initialize BetterAuth client)
  - Function: `get_user(session_token: str) -> Optional[Dict]` (TODO: Retrieve user)
  - Function: `validate_session(session_token: str) -> bool` (TODO: Validate session)
  - All functions return placeholders
  - File: `backend/app/auth/betterauth_client.py`

- [ ] **T003**: Create `backend/app/auth/routes.py` with /auth/signup, login, logout, me endpoints
  - POST `/auth/signup`: Request `{email, password, name?}`, Response `{user, message}` (placeholder)
  - POST `/auth/login`: Request `{email, password}`, Response `{user, session_token}` (placeholder)
  - POST `/auth/logout`: Request `{session_token?}`, Response `{message}` (placeholder)
  - GET `/auth/me`: Headers (session token), Response `{user}` (placeholder)
  - All endpoints return placeholder responses
  - File: `backend/app/auth/routes.py`

- [ ] **T004**: Add router to main FastAPI app
  - Import: `from app.auth.routes import router as auth_router`
  - Include: `app.include_router(auth_router, prefix="/auth", tags=["auth"])`
  - File: `backend/app/main.py`

- [ ] **T005**: Create `backend/app/auth/session_middleware.py` with placeholder logic
  - Function: `extract_session_cookie(request) -> Optional[str]` (TODO: Extract cookie)
  - Function: `validate_session_middleware(request, call_next)` (TODO: Validate session)
  - Placeholder: pass through request unchanged
  - File: `backend/app/auth/session_middleware.py`

- [ ] **T006**: Create `backend/app/auth/decorators.py` with require_auth (placeholder)
  - Decorator: `require_auth(func)` (TODO: Check authentication)
  - Placeholder: Log message, allow access
  - File: `backend/app/auth/decorators.py`

- [ ] **T007**: Update `backend/app/config/settings.py` for new env vars
  - Add: `BETTERAUTH_PUBLIC_KEY: Optional[str] = None`
  - Add: `BETTERAUTH_SECRET_KEY: Optional[str] = None`
  - Add: `BETTERAUTH_ISSUER: Optional[str] = "interactive-agentic-book"`
  - All from environment variables
  - File: `backend/app/config/settings.py`

- [ ] **T008**: Update `.env.example` with BetterAuth env vars
  - Add commented: `# BETTERAUTH_PUBLIC_KEY=`
  - Add commented: `# BETTERAUTH_SECRET_KEY=`
  - Add commented: `# BETTERAUTH_ISSUER=interactive-agentic-book`
  - File: `.env.example`

---

### B. Frontend Tasks

- [ ] **T009**: Create `frontend/src/auth/useAuth.ts` with placeholder methods
  - Function: `login(email: string, password: string) -> Promise<Dict>` (POST /auth/login)
  - Function: `signup(email: string, password: string, name?: string) -> Promise<Dict>` (POST /auth/signup)
  - Function: `logout() -> Promise<void>` (POST /auth/logout)
  - Function: `getSession() -> Promise<Dict | null>` (GET /auth/me)
  - All return placeholder responses
  - File: `frontend/src/auth/useAuth.ts`

- [ ] **T010**: Create `frontend/src/components/auth/LoginForm.tsx`
  - Email input field
  - Password input field
  - "Login" button
  - Error display (placeholder)
  - Loading state (placeholder)
  - Calls `useAuth().login()` on submit
  - Minimal styling
  - File: `frontend/src/components/auth/LoginForm.tsx`

- [ ] **T011**: Create `frontend/src/components/auth/SignupForm.tsx`
  - Email input field
  - Password input field
  - Confirm password field
  - Name input field (optional)
  - "Signup" button
  - Error display (placeholder)
  - Loading state (placeholder)
  - Calls `useAuth().signup()` on submit
  - Minimal styling
  - File: `frontend/src/components/auth/SignupForm.tsx`

- [ ] **T012**: Create `frontend/src/components/auth/ProfileBox.tsx`
  - Display placeholder user information (email, name)
  - "Logout" button
  - Loading state (placeholder)
  - On mount: Call `useAuth().getSession()`
  - On logout: Call `useAuth().logout()`
  - Minimal styling
  - File: `frontend/src/components/auth/ProfileBox.tsx`

---

### C. Contract Tasks

- [ ] **T013**: Create `specs/052-betterauth/contracts/auth-api.yaml` with endpoint schemas
  - POST /auth/signup: Request/response schemas
  - POST /auth/login: Request/response schemas
  - POST /auth/logout: Request/response schemas
  - GET /auth/me: Request/response schemas
  - Error codes and examples
  - File: `specs/052-betterauth/contracts/auth-api.yaml` (already created)

---

### D. Validation Tasks

- [ ] **T014**: Backend must start with uvicorn
  - Verify: `cd backend && uvicorn app.main:app --reload` starts without errors
  - Check: All imports resolve correctly

- [ ] **T015**: Frontend must build without errors
  - Verify: `cd frontend && npm run build` succeeds
  - Check: All components compile

- [ ] **T016**: Auth endpoints must return placeholder responses
  - Test: POST /auth/signup returns `{user, message}`
  - Test: POST /auth/login returns `{user, session_token}`
  - Test: POST /auth/logout returns `{message}`
  - Test: GET /auth/me returns `{user}`

---

## Implementation Notes

- All backend functions must have TODO comments explaining expected behavior
- All frontend components must be minimal, functional placeholders
- No real authentication logic should be implemented
- No password hashing, session management, or crypto operations
- All responses are static placeholders

