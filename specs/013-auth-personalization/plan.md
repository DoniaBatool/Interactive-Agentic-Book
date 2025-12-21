# Architecture Plan: Auth & Personalization – Feature 013

## Overview

Goal: Add user authentication using BetterAuth, collect user background information at signup, and enable content personalization based on user profile.

## High-Level Design

### Authentication Flow

```
┌─────────────────────────────────────────────────────────────┐
│                      User Flow                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────────────────┐  │
│  │  Sign Up │───▶│  Profile │───▶│  Logged In User      │  │
│  │   Form   │    │ Questions│    │  + Personalization   │  │
│  └──────────┘    └──────────┘    └──────────────────────┘  │
│       │                                    │                │
│       │         ┌──────────┐               │                │
│       └────────▶│  Sign In │───────────────┘                │
│                 │   Form   │                                │
│                 └──────────┘                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Database Schema Extension

```
┌─────────────────────────────────────────────────────────────┐
│                     PostgreSQL Database                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────┐       ┌─────────────────────────────┐  │
│  │     users       │       │      user_profiles          │  │
│  ├─────────────────┤       ├─────────────────────────────┤  │
│  │ id (PK)         │◄──────│ user_id (FK)                │  │
│  │ email           │       │ software_level              │  │
│  │ password_hash   │       │ hardware_level              │  │
│  │ name            │       │ technologies (JSON)         │  │
│  │ created_at      │       │ learning_goals              │  │
│  │ updated_at      │       │ created_at                  │  │
│  └─────────────────┘       │ updated_at                  │  │
│         │                  └─────────────────────────────┘  │
│         │                                                    │
│         ▼                                                    │
│  ┌─────────────────┐                                        │
│  │    sessions     │  (existing - add user_id link)         │
│  └─────────────────┘                                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## BetterAuth Integration

### What is BetterAuth?

BetterAuth is a modern authentication library that provides:
- Email/password authentication
- OAuth providers (Google, GitHub, etc.)
- Session management
- TypeScript-first with React hooks
- Self-hosted (no vendor lock-in)

### Integration Approach

**Option A: Full BetterAuth (Frontend + Backend)**
- Use BetterAuth's Next.js/React integration
- BetterAuth handles session management
- Works well with serverless

**Option B: BetterAuth Backend + Custom Frontend** (Chosen)
- Use BetterAuth's core auth functions
- Custom FastAPI endpoints
- Custom React components in Docusaurus
- More control over UI/UX

## Backend Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     FastAPI Backend                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    Auth Router                        │  │
│  │  POST /auth/signup    - Create account + profile      │  │
│  │  POST /auth/signin    - Login, return session token   │  │
│  │  POST /auth/signout   - Clear session                 │  │
│  │  GET  /auth/session   - Get current user              │  │
│  │  GET  /auth/profile   - Get user profile              │  │
│  │  PUT  /auth/profile   - Update profile                │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                 │
│                           ▼                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                   Auth Service                        │  │
│  │  - Password hashing (bcrypt)                         │  │
│  │  - Session token generation (JWT)                    │  │
│  │  - Session validation                                │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                 │
│                           ▼                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                   NeonDB (PostgreSQL)                 │  │
│  │  - users table                                       │  │
│  │  - user_profiles table                               │  │
│  │  - sessions table (updated with user_id)             │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Frontend Components

### Auth Pages (Docusaurus)

```
src/
├── pages/
│   ├── auth/
│   │   ├── signup.tsx      # Sign up with profile questions
│   │   ├── signin.tsx      # Sign in form
│   │   └── profile.tsx     # View/edit profile
│   └── ...
├── components/
│   ├── AuthProvider.tsx    # Context for auth state
│   ├── UserMenu.tsx        # Navbar user menu
│   ├── ProtectedRoute.tsx  # Route guard
│   └── ProfileForm.tsx     # Profile questions form
└── ...
```

### Profile Questions

```typescript
interface UserProfile {
  // Software Experience
  softwareLevel: 'beginner' | 'intermediate' | 'advanced';
  technologies: {
    python: boolean;
    ros2: boolean;
    gazebo: boolean;
    isaac: boolean;
    aiMl: boolean;
    unity: boolean;
  };
  
  // Hardware Experience
  hardwareLevel: 'none' | 'some' | 'extensive';
  hardwareExperience: {
    jetson: boolean;
    realsense: boolean;
    lidar: boolean;
    robots: boolean;
  };
  
  // Goals
  learningGoals: string;
}
```

## Session Management

### JWT Token Structure

```typescript
interface SessionToken {
  userId: number;
  email: string;
  exp: number;      // Expiration timestamp
  iat: number;      // Issued at timestamp
}
```

### Cookie Settings

```python
response.set_cookie(
    key="session_token",
    value=token,
    httponly=True,      # Prevent XSS
    secure=True,        # HTTPS only (production)
    samesite="lax",     # CSRF protection
    max_age=60*60*24*7  # 7 days
)
```

## Phased Implementation

### Phase 1: Backend Auth
1. Add auth dependencies (passlib, python-jose)
2. Create User and UserProfile models
3. Implement auth service (signup, signin, signout)
4. Add auth API endpoints
5. Session token handling

### Phase 2: Frontend Auth
1. Create AuthProvider context
2. Build signup page with profile questions
3. Build signin page
4. Add UserMenu to navbar
5. Protected route wrapper

### Phase 3: Integration
1. Link chat sessions to user accounts
2. Pass user profile to RAG for personalization context
3. Update health endpoint with auth status

## Dependencies

### Backend
- `passlib[bcrypt]>=1.7.4` - Password hashing
- `python-jose[cryptography]>=3.3.0` - JWT tokens

### Frontend
- No new dependencies (use existing React)

## Security Considerations

1. **Password Storage**: bcrypt with salt
2. **Session Tokens**: JWT with short expiry + refresh
3. **CORS**: Strict origin validation
4. **Rate Limiting**: Login attempts limited
5. **HTTPS**: Required for production

