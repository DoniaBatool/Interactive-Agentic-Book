---
description: "Tasks for Postgres Persistence – Feature 012"
---

# Tasks: Postgres Persistence

**Input**: spec.md, plan.md  
**Tests**: Database integration tests + manual testing.

## Phase 1: Database Setup
- [x] T012-001 Add database dependencies to `requirements.txt`:
  - `sqlalchemy[asyncio]>=2.0.0`
  - `asyncpg>=0.29.0`
  - `python-dotenv>=1.0.0` (if not already present)

- [x] T012-002 Create database configuration in `backend/app/core/database.py`:
  - Load DATABASE_URL from environment
  - Create async engine and session factory
  - Add connection pool configuration

- [x] T012-003 Create database models in `backend/app/models/`:
  - `session.py` - Session model
  - `message.py` - Message model with JSON citations
  - `__init__.py` - Export models

- [x] T012-004 Add database initialization:
  - Create tables on startup (development mode)
  - Add health check for database connection

## Phase 2: History Service
- [x] T012-010 Create `backend/app/services/history.py`:
  - `create_session(session_id)` - Create new session
  - `get_or_create_session(session_id)` - Get existing or create new
  - `save_message(session_id, chapter, role, content, citations)` - Save message
  - `get_history(session_id, chapter)` - Get conversation history
  - `clear_history(session_id, chapter)` - Delete messages

- [x] T012-011 Add error handling:
  - Graceful degradation if DB unavailable
  - Logging for database operations
  - Transaction management

## Phase 3: API Endpoints
- [x] T012-020 Add history endpoints in `backend/app/api/history.py`:
  - `GET /chat/history` - Retrieve history with filters
  - `DELETE /chat/history` - Clear history

- [x] T012-021 Update `/chat/agent` endpoint:
  - Extract session_id from `X-Session-ID` header
  - Save user message before processing
  - Save assistant message after response
  - Handle missing session_id gracefully

- [x] T012-022 Register history router in `main.py`

## Phase 4: Frontend Integration
- [x] T012-030 Update `RagChat.tsx`:
  - Generate session ID on first load (UUID)
  - Store session ID in localStorage
  - Add `X-Session-ID` header to requests
  - Load history on component mount

- [x] T012-031 Add history loading logic:
  - Fetch history from `/chat/history` endpoint
  - Populate messages state with history
  - Handle loading and error states

- [x] T012-032 Handle chapter-based history:
  - Pass chapter filter when loading history
  - Reload history when chapter changes

## Phase 5: Testing & Documentation
- [x] T012-040 Manual testing:
  - Verify messages persist across page refresh ✅
  - Test chapter-based conversation separation ✅
  - Test clear history functionality

- [x] T012-041 Update documentation:
  - Add DATABASE_URL to quickstart
  - Document Docker PostgreSQL setup
  - Update STATUS.md

