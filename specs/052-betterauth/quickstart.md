# Quickstart Guide: BetterAuth Authentication Layer

**Feature**: 052-betterauth
**Branch**: `052-betterauth`
**Estimated Time**: 2-3 hours (scaffolding only)

## Prerequisites

Before starting implementation, ensure you have:

- [x] FastAPI backend structure exists
- [x] React/TypeScript frontend structure exists
- [x] Git branch `052-betterauth` checked out
- [x] Read `specs/052-betterauth/spec.md`
- [x] Read `specs/052-betterauth/plan.md`
- [x] Read `specs/052-betterauth/tasks.md`

## Implementation Overview

**Total Steps**: 5 phases
**Primary Deliverable**: Complete scaffolding for BetterAuth authentication with backend routes, middleware, decorators, frontend components, and configuration
**Validation**: All auth endpoints return placeholder responses, frontend components render, middleware and decorators exist

---

## Phase 1: Backend Auth Client (20 minutes)

### Step 1.1: Create BetterAuth Client

**File**: `backend/app/auth/betterauth_client.py`

**Action**: Create placeholder functions:
- `init_client()` - TODO: Initialize BetterAuth client
- `get_user(session_token)` - TODO: Get user from BetterAuth
- `validate_session(session_token)` - TODO: Validate session
- All return placeholders

---

## Phase 2: Backend Routes (30 minutes)

### Step 2.1: Create Auth Routes

**File**: `backend/app/auth/routes.py`

**Action**: Create FastAPI router with:
- POST `/auth/signup` - Placeholder signup
- POST `/auth/login` - Placeholder login
- POST `/auth/logout` - Placeholder logout
- GET `/auth/me` - Placeholder user profile

### Step 2.2: Register Router

**File**: `backend/app/main.py`

**Action**: Include auth router

---

## Phase 3: Middleware & Decorators (25 minutes)

### Step 3.1: Create Session Middleware

**File**: `backend/app/auth/session_middleware.py`

**Action**: Create middleware with:
- `extract_session_cookie()` - TODO: Extract cookie
- `validate_session_middleware()` - TODO: Validate session
- Placeholder pass-through logic

### Step 3.2: Create Auth Decorator

**File**: `backend/app/auth/decorators.py`

**Action**: Create `require_auth` decorator:
- TODO: Check authentication
- Placeholder: Log message, allow access

---

## Phase 4: Frontend Components (40 minutes)

### Step 4.1: Create useAuth Hook

**File**: `frontend/src/auth/useAuth.ts`

**Action**: Create hook with:
- `login()` - POST to `/auth/login`
- `signup()` - POST to `/auth/signup`
- `logout()` - POST to `/auth/logout`
- `getSession()` - GET `/auth/me`
- All return placeholders

### Step 4.2: Create Login Form

**File**: `frontend/src/components/auth/LoginForm.tsx`

**Action**: Create component with:
- Email input
- Password input
- Login button
- Error display
- Calls `useAuth().login()`

### Step 4.3: Create Signup Form

**File**: `frontend/src/components/auth/SignupForm.tsx`

**Action**: Create component with:
- Email input
- Password input
- Confirm password input
- Name input (optional)
- Signup button
- Calls `useAuth().signup()`

### Step 4.4: Create Profile Box

**File**: `frontend/src/components/auth/ProfileBox.tsx`

**Action**: Create component with:
- Display placeholder user
- Logout button
- Calls `useAuth().logout()`

---

## Phase 5: Configuration (15 minutes)

### Step 5.1: Update Settings

**File**: `backend/app/config/settings.py`

**Action**: Add:
- `BETTERAUTH_PUBLIC_KEY`
- `BETTERAUTH_SECRET_KEY`
- `BETTERAUTH_ISSUER`

### Step 5.2: Update .env.example

**File**: `.env.example`

**Action**: Add commented environment variables

---

## Validation Checklist

After implementation, verify:

- [ ] betterauth_client.py exists with placeholder functions
- [ ] routes.py exists with all 4 endpoints
- [ ] session_middleware.py exists
- [ ] decorators.py exists with require_auth
- [ ] useAuth.ts exists with all functions
- [ ] LoginForm.tsx exists and renders
- [ ] SignupForm.tsx exists and renders
- [ ] ProfileBox.tsx exists and renders
- [ ] settings.py updated with env vars
- [ ] .env.example updated
- [ ] Backend starts without errors
- [ ] Frontend builds without errors
- [ ] Auth endpoints return placeholder responses

---

## Next Steps

After completing scaffolding:

1. Test auth endpoints with sample requests
2. Test frontend components
3. Verify middleware and decorators exist
4. Implement real authentication logic in future features

---

## Troubleshooting

**Issue**: Import errors
- **Solution**: Check all __init__.py files exist in auth directory

**Issue**: Router not found
- **Solution**: Verify router is registered in main.py

**Issue**: Frontend components don't render
- **Solution**: Check component imports and React setup

