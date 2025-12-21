---
description: "Tasks for Auth & Personalization – Feature 013"
---

# Tasks: Auth & Personalization (BetterAuth)

**Input**: spec.md, plan.md  
**Tests**: Manual testing + API endpoint tests.

## Phase 1: Backend Auth Setup (FastAPI - DEPRECATED)
- [x] T013-001 Add auth dependencies to `requirements.txt`:
  - `passlib[bcrypt]>=1.7.4`
  - `python-jose[cryptography]>=3.3.0`

- [x] T013-002 Create User model in `backend/app/models/user.py`:
  - id, email, password_hash, name, created_at, updated_at
  - Unique constraint on email

- [x] T013-003 Create UserProfile model in `backend/app/models/user_profile.py`:
  - user_id (FK), software_level, hardware_level
  - technologies (JSONB), learning_goals
  - created_at, updated_at

- [x] T013-004 Update database init to create new tables

## Phase 2: Auth Service (FastAPI - DEPRECATED)
- [x] T013-010 Create `backend/app/services/auth.py`:
  - `hash_password(password)` - bcrypt hashing
  - `verify_password(password, hash)` - verify password
  - `create_session_token(user_id)` - generate JWT
  - `verify_session_token(token)` - validate JWT
  - `get_user_id_from_token(token)` - get user from token

- [x] T013-011 Create `backend/app/services/user.py`:
  - `create_user(email, password, name, profile)` - signup
  - `get_user_by_email(email)` - for login
  - `get_user_by_id(id)` - for session
  - `update_profile(user_id, profile)` - update profile

## Phase 3: BetterAuth Migration
- [x] T013-060 Setup BetterAuth server (`auth-server/`):
  - Create package.json with BetterAuth dependencies
  - Create `src/auth.ts` with BetterAuth config
  - Create `src/index.ts` Express server
  - Configure user fields (name, softwareLevel, hardwareLevel, technologies, learningGoals)

- [x] T013-061 Update frontend AuthContext for BetterAuth:
  - Update API endpoints to `/api/auth/*`
  - Update request/response handling
  - Add `refreshSession()` method

- [x] T013-062 Create auth-server README with setup instructions

## Phase 4: Frontend Auth Pages
- [x] T013-030 Create `src/context/AuthContext.tsx`:
  - AuthProvider with user state
  - Login/logout functions
  - Session check on mount

- [x] T013-031 Create `src/pages/auth/signup.tsx`:
  - Email, password, name fields
  - Profile questions (software/hardware level)
  - Technologies checkboxes
  - Learning goals textarea
  - Password show/hide toggle

- [x] T013-032 Create `src/pages/auth/signin.tsx`:
  - Email and password fields
  - Remember me checkbox
  - Password show/hide toggle

- [x] T013-033 Create `src/components/UserMenu.tsx`:
  - Show user name when logged in
  - Sign out button
  - Profile link

- [x] T013-034 Add UserMenu to navbar (swizzled Navbar/Content)

## Phase 5: Personalization Feature
- [x] T013-070 Create `backend/app/api/personalize.py`:
  - POST `/personalize/content` endpoint
  - Accept content, user level, chapter title
  - Use OpenAI to adapt content
  - Return personalized markdown

- [x] T013-071 Create `src/components/PersonalizeContent.tsx`:
  - Display personalization banner on doc pages
  - Show user level badge
  - Personalize button to adapt content
  - Restore original button

- [x] T013-072 Swizzle DocItem/Content to include PersonalizeContent:
  - Create `src/theme/DocItem/Content/index.tsx`
  - Wrap original content with personalization component

- [x] T013-073 Add personalization CSS styles:
  - `.personalize-container` styles
  - Dark/light mode support
  - Loading spinner animation

- [x] T013-074 Register personalize router in `main.py`

## Phase 6: Integration
- [x] T013-040 Sessions table already has user_id column (nullable FK)

- [x] T013-041 Update chat endpoint for personalized responses:
  - Extract user profile from BetterAuth session cookie
  - Pass user context (skill level, technologies) to RAG agent
  - Agent adapts responses based on user's experience level
  - System message includes user profile for personalization

- [x] T013-042 Create profile page:
  - `src/pages/auth/profile.tsx`
  - View and edit profile

- [x] T013-043 Create PersonalizeButton component:
  - `src/components/PersonalizeButton.tsx`
  - Shows user level, links to profile

## Phase 7: Testing & Documentation
- [x] T013-050 Manual testing:
  - Test signup flow with profile ✅
  - Test signin/signout ✅
  - Test session persistence ✅
  - Test profile update ✅
  - Test personalization feature ✅

- [x] T013-051 Update documentation:
  - Add auth setup to quickstart ✅
  - Update STATUS.md ✅
  - Add BetterAuth setup instructions ✅

---

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend (:3000)                         │
│                         Docusaurus                              │
├─────────────────────────────────────────────────────────────────┤
│  AuthContext  │  PersonalizeContent  │  RagChat  │  UserMenu    │
└───────┬───────────────────┬─────────────────┬───────────────────┘
        │                   │                 │
        ▼                   ▼                 ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ BetterAuth    │   │   FastAPI     │   │   FastAPI     │
│   Server      │   │  /personalize │   │    /chat      │
│   (:8001)     │   │   (:8000)     │   │   (:8000)     │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────────────────────────────────────────────────────┐
│                       PostgreSQL                               │
│              users │ user_profiles │ sessions │ messages       │
└───────────────────────────────────────────────────────────────┘
```
