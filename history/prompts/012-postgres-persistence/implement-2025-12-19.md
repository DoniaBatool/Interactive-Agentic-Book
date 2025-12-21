## Context
- Stage: implement
- Feature: 012-postgres-persistence
- Prompt: Implement PostgreSQL persistence for chat history using NeonDB serverless.

## Response

### Backend Changes
1. Created `backend/app/core/database.py`:
   - SQLAlchemy async engine with asyncpg driver
   - Auto-conversion of `postgresql://` to `postgresql+asyncpg://`
   - SSL configuration for NeonDB
   - NullPool for serverless databases
   - Graceful degradation when DB unavailable

2. Created `backend/app/models/`:
   - `session.py` - Session model (session_id, user_id, timestamps)
   - `message.py` - Message model (session_id, chapter, role, content, citations as JSONB)

3. Created `backend/app/services/history.py`:
   - `get_or_create_session()` - Create/retrieve sessions
   - `save_message()` - Save user and assistant messages
   - `get_history()` - Retrieve conversation history
   - `clear_history()` - Delete messages

4. Created `backend/app/api/history.py`:
   - `GET /chat/history` - Retrieve history with filters
   - `DELETE /chat/history` - Clear history
   - `GET /chat/history/status` - Check persistence availability

5. Updated `backend/app/api/chat.py`:
   - Extract `X-Session-ID` header
   - Save user message before processing
   - Save assistant message after response

6. Updated `backend/app/main.py`:
   - Database initialization on startup
   - History router registration
   - Health check includes database status

### Frontend Changes
1. Updated `src/components/RagChat.tsx`:
   - Session ID generation (UUID in localStorage)
   - History loading on component mount
   - `X-Session-ID` header sent with requests
   - Chapter-based conversation separation

### Database
- Used NeonDB serverless PostgreSQL
- Tables auto-created on startup
- SSL connection configured for cloud database

### Testing
- ✅ Database connection successful
- ✅ Messages persist across page refresh
- ✅ Chapter-based history separation works
- ✅ Health endpoint shows database status

## Tests
- Manual browser testing: ✅
- Backend health check: ✅
- NeonDB connection: ✅
- History persistence: ✅

