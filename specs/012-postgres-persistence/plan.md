# Architecture Plan: Postgres Persistence – Feature 012

## Overview

Goal: Add PostgreSQL persistence for chat conversations, allowing users to maintain conversation history across sessions and page navigations.

## High-Level Design

### Database Schema

```
┌─────────────────────────────────────────────────────────────┐
│                     PostgreSQL Database                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────┐       ┌─────────────────────────────┐  │
│  │    sessions     │       │         messages            │  │
│  ├─────────────────┤       ├─────────────────────────────┤  │
│  │ id (PK)         │◄──────│ session_id (FK)             │  │
│  │ session_id      │       │ id (PK)                     │  │
│  │ user_id (null)  │       │ chapter                     │  │
│  │ created_at      │       │ role                        │  │
│  │ updated_at      │       │ content                     │  │
│  └─────────────────┘       │ citations (JSON)            │  │
│                            │ created_at                  │  │
│                            └─────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Backend Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     FastAPI Backend                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │ /chat/agent  │    │ /chat/history│    │ Database     │  │
│  │   endpoint   │───▶│   service    │───▶│  Models      │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│         │                   │                    │          │
│         │                   │                    ▼          │
│         │                   │            ┌──────────────┐  │
│         │                   └───────────▶│  PostgreSQL  │  │
│         │                                └──────────────┘  │
│         ▼                                                   │
│  ┌──────────────┐                                          │
│  │ Save message │                                          │
│  │  to history  │                                          │
│  └──────────────┘                                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

### Saving Messages

```
User sends message
       │
       ▼
POST /chat/agent (with session_id header)
       │
       ▼
Save user message to DB
       │
       ▼
Process with Agent
       │
       ▼
Save assistant message to DB
       │
       ▼
Return response
```

### Loading History

```
Frontend mounts RagChat
       │
       ▼
GET /chat/history?session_id=X&chapter=Y
       │
       ▼
Query messages from DB
       │
       ▼
Return message list
       │
       ▼
Populate chat UI
```

## Session Management

### Anonymous Sessions

1. Frontend generates UUID on first visit
2. Stored in localStorage: `rag-chat-session-id`
3. Sent with every request as header: `X-Session-ID`
4. No expiration (until user clears browser data)

### Future Auth Integration

- When user logs in, link session to user_id
- Merge anonymous sessions with user account
- Query by user_id instead of session_id

## Database Connection

### Configuration

```python
# Environment variable (NeonDB serverless - recommended)
DATABASE_URL=postgresql://user:pass@ep-xxx.aws.neon.tech/neondb?sslmode=require

# For local development (Docker)
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rag_chatbot
```

### NeonDB Serverless (Production)

- **Auto-conversion**: Code automatically converts `postgresql://` to `postgresql+asyncpg://`
- **SSL**: Automatically configured for cloud databases
- **NullPool**: Used for serverless databases (connection pooling handled by NeonDB)
- **Query params**: `sslmode` and `channel_binding` stripped (handled via SSL context)

### Local PostgreSQL (Development)

- Use SQLAlchemy async with asyncpg driver
- Pool size: 5-20 connections
- Connection timeout: 30 seconds

## Phased Implementation

1. **Phase 1 – Database Setup**
   - Add SQLAlchemy and asyncpg dependencies
   - Create database models
   - Set up connection and migrations

2. **Phase 2 – History Service**
   - Implement message CRUD operations
   - Add session management

3. **Phase 3 – API Endpoints**
   - Add `/chat/history` GET endpoint
   - Add `/chat/history` DELETE endpoint
   - Update `/chat/agent` to save messages

4. **Phase 4 – Frontend Integration**
   - Generate/retrieve session ID
   - Load history on mount
   - Send session ID with requests

## Dependencies

- `sqlalchemy[asyncio]>=2.0.0` - Async ORM
- `asyncpg>=0.29.0` - PostgreSQL async driver
- `alembic>=1.13.0` - Database migrations (optional)

## Database Options

### Option 1: NeonDB Serverless (Recommended for Production)

1. Go to https://neon.tech and create free account
2. Create new project
3. Copy connection string from Dashboard
4. Add to `.env`:
   ```
   DATABASE_URL=postgresql://user:pass@ep-xxx.aws.neon.tech/neondb?sslmode=require
   ```

**Benefits:**
- Free tier available
- Serverless (auto-scaling)
- No infrastructure management
- SSL by default

### Option 2: Docker PostgreSQL (Local Development)

```bash
docker run --name rag-postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=rag_chatbot \
  -p 5432:5432 \
  -d postgres:16
```

Add to `.env`:
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rag_chatbot
```

### Option 3: Local PostgreSQL

- Install PostgreSQL locally
- Create database: `createdb rag_chatbot`
- Set DATABASE_URL environment variable

