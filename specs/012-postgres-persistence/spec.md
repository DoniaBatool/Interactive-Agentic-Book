# Feature Specification: Postgres Persistence – Chat History

**Feature Number**: 012  
**Feature Branch**: `012-postgres-persistence`  
**Status**: In Progress  
**Input**: Existing RAG chatbot with Agent integration (Feature 011).

## User Scenarios & Testing *(mandatory)*

### User Story 1 – Persistent Chat History (P1)
As a learner, my chat conversations are saved so I can continue where I left off after refreshing the page or returning later.

**Acceptance**:
- Chat messages persist across page refreshes.
- Returning to the same chapter shows previous conversation.
- Messages are stored with timestamps and context.

### User Story 2 – Session-based Conversations (P1)
As a learner, my chat sessions are organized by chapter context so each chapter has its own conversation thread.

**Acceptance**:
- Each chapter maintains a separate conversation history.
- Navigating between chapters shows the relevant conversation.
- Session ID is generated per browser session.

### User Story 3 – Anonymous Sessions (P2)
As an anonymous user (not logged in), my conversations are tied to my browser session.

**Acceptance**:
- Session ID is stored in browser localStorage.
- Sessions persist until explicitly cleared or expired.
- Future auth integration can link sessions to user accounts.

### User Story 4 – API for Chat History (P2)
As a developer, I can retrieve and manage chat history through API endpoints.

**Acceptance**:
- `GET /chat/history` returns conversation history.
- `DELETE /chat/history` clears conversation history.
- History is filtered by session and optional chapter.

## Requirements

- **FR-001**: Set up PostgreSQL database connection:
  - Use SQLAlchemy as ORM.
  - Configure via environment variables (DATABASE_URL).
  - Support both local development and production deployments.

- **FR-002**: Create database schema:
  - `sessions` table: session_id, created_at, user_id (nullable for future auth).
  - `messages` table: id, session_id, chapter, role, content, citations, created_at.
  - Proper indexes for efficient queries.

- **FR-003**: Implement message persistence:
  - Save user messages and assistant responses to database.
  - Include citations as JSON field.
  - Store chapter context with each message.

- **FR-004**: Add history API endpoints:
  - `GET /chat/history?session_id=X&chapter=Y` - Retrieve history.
  - `DELETE /chat/history?session_id=X` - Clear history.

- **FR-005**: Update frontend to use persistence:
  - Generate/retrieve session ID from localStorage.
  - Load previous messages on component mount.
  - Send session_id with chat requests.

## Non-Functional Requirements

- **NFR-001**: Database operations should not significantly increase response latency (<100ms overhead).
- **NFR-002**: Support graceful degradation if database is unavailable.
- **NFR-003**: Message storage should handle large conversations (1000+ messages per session).

## Success Criteria

- **SC-001**: Chat history persists across page refreshes.
- **SC-002**: Multiple chapters maintain separate conversation threads.
- **SC-003**: API endpoints for history management work correctly.
- **SC-004**: System works with anonymous sessions (no auth required).

