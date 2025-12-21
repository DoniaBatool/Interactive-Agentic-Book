# Feature Specification: Auth & Personalization (BetterAuth)

**Feature Number**: 013  
**Feature Branch**: `013-auth-personalization`  
**Status**: ✅ Complete & Tested  
**Input**: Hackathon requirements, existing Docusaurus frontend, FastAPI backend.  
**Implementation**: BetterAuth + Content Personalization

## User Scenarios & Testing *(mandatory)*

### User Story 1 – Sign Up with Profile (P1)
As a new user, I can sign up with my email and provide information about my software and hardware background so the content can be personalized for me.

**Acceptance**:
- Sign up form asks for email, password, and profile questions.
- Profile questions include:
  - Software background (Python, ROS, AI/ML experience level)
  - Hardware background (Jetson, RealSense, Robot experience)
  - Learning goals
- User account is created and stored securely.
- User is automatically logged in after signup.

### User Story 2 – Sign In (P1)
As a returning user, I can sign in with my email and password to access my personalized experience.

**Acceptance**:
- Sign in form accepts email and password.
- Successful login redirects to previous page or home.
- Invalid credentials show clear error message.
- Session persists across page refreshes.

### User Story 3 – Session Persistence (P1)
As a logged-in user, my session persists so I don't have to log in repeatedly.

**Acceptance**:
- Session survives page refresh and navigation.
- Session token stored securely (httpOnly cookie).
- User can stay logged in across browser sessions (remember me).

### User Story 4 – Sign Out (P1)
As a logged-in user, I can sign out to end my session.

**Acceptance**:
- Sign out button visible when logged in.
- Clicking sign out clears session and redirects to home.
- Protected actions require re-login after sign out.

### User Story 5 – View/Edit Profile (P2)
As a logged-in user, I can view and update my profile information.

**Acceptance**:
- Profile page shows current information.
- User can update their background/preferences.
- Changes are saved to database.

### User Story 6 – Content Personalization (P1)
As a logged-in user, I can personalize chapter content based on my skill level to get content adapted to my experience.

**Acceptance**:
- Personalization banner appears on all doc pages.
- Shows my current skill level badge.
- "Personalize Content" button adapts content using AI.
- Content becomes more/less detailed based on my level.
- "Restore Original" button reverts to original content.

## Requirements

- **FR-001**: Integrate BetterAuth for authentication:
  - Email/password authentication
  - Session management with secure cookies
  - OAuth providers (optional: GitHub, Google)

- **FR-002**: User profile with background questions:
  - Software experience level (Beginner/Intermediate/Advanced)
  - Hardware experience (None/Some/Extensive)
  - Specific technologies (checkboxes: Python, ROS 2, Gazebo, Isaac, etc.)
  - Learning goals (free text)

- **FR-003**: Frontend auth UI components:
  - Sign up page with profile questions
  - Sign in page
  - User menu (logged in state)
  - Profile page

- **FR-004**: Backend auth endpoints:
  - POST `/auth/signup` - Create account with profile
  - POST `/auth/signin` - Login
  - POST `/auth/signout` - Logout
  - GET `/auth/session` - Get current session
  - GET/PUT `/auth/profile` - View/update profile

- **FR-005**: Content personalization system:
  - AI-powered content adaptation based on user skill level
  - Personalization API endpoint for content modification
  - Frontend component for triggering personalization
  - Restore original content functionality

- **FR-006**: Link chat sessions to user accounts (Future):
  - Associate existing anonymous sessions with user on login
  - Query chat history by user_id when logged in
  - Pass user profile to RAG for personalized responses

## Non-Functional Requirements

- **NFR-001**: Passwords must be hashed securely (bcrypt/argon2).
- **NFR-002**: Session tokens must be httpOnly cookies (XSS protection).
- **NFR-003**: Auth endpoints must be rate-limited.
- **NFR-004**: Profile data stored in same PostgreSQL (NeonDB).

## Success Criteria

- **SC-001**: User can sign up, sign in, and sign out successfully.
- **SC-002**: Profile information is captured and stored.
- **SC-003**: Session persists across page navigation.
- **SC-004**: Content personalization adapts chapters to user skill level.
- **SC-005**: BetterAuth integration provides secure authentication.
- **SC-006**: Dark/light mode compatibility maintained.
- **SC-007**: Mobile-responsive auth pages and components.

