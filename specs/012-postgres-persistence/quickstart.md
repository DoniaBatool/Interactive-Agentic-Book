# Quickstart – Feature 012: Postgres Persistence

## Prerequisites

- PostgreSQL database (NeonDB recommended, or local)
- Backend running with RAG service
- Frontend running

## Option 1: NeonDB Serverless (Recommended) ⭐

1. Go to https://neon.tech
2. Create free account and new project
3. Copy connection string from Dashboard
4. Add to `.env` file:

```bash
DATABASE_URL=postgresql://neondb_owner:xxx@ep-xxx.aws.neon.tech/neondb?sslmode=require
```

**Note:** Code automatically:
- Converts `postgresql://` to `postgresql+asyncpg://`
- Configures SSL for secure connection
- Uses NullPool for serverless compatibility

## Option 2: Docker PostgreSQL (Local Development)

```bash
# Start PostgreSQL container
docker run --name rag-postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=rag_chatbot \
  -p 5432:5432 \
  -d postgres:16

# Verify it's running
docker ps
```

Add to `.env`:
```bash
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rag_chatbot
```

## Option 3: Supabase (Cloud Alternative)

1. Go to https://supabase.com
2. Create new project
3. Get connection string from Settings → Database
4. Use the connection string as DATABASE_URL

## Environment Setup

Create/update `.env` file in project root:

```bash
# Database (NeonDB example)
DATABASE_URL=postgresql://neondb_owner:xxx@ep-xxx.aws.neon.tech/neondb?sslmode=require

# Existing variables
OPENAI_API_KEY=sk-...
QDRANT_HOST=localhost
QDRANT_PORT=6333
```

## Run Backend

```bash
cd C:\Users\Leo\interactive-agentic-book
venv\Scripts\activate
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will automatically create tables on startup.

## Run Frontend

```bash
cd C:\Users\Leo\interactive-agentic-book
npm run start
```

## Test Persistence

1. Open browser: `http://localhost:3000`
2. Navigate to any chapter
3. Click floating chat button
4. Ask a question
5. **Refresh the page** (F5)
6. Click chat button again
7. Your previous conversation should appear!

## Verify Database

```bash
# Connect to PostgreSQL
psql -U postgres -d rag_chatbot

# Check tables
\dt

# View sessions
SELECT * FROM sessions;

# View messages
SELECT * FROM messages ORDER BY created_at DESC LIMIT 10;
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/chat/history` | GET | Get conversation history |
| `/chat/history` | DELETE | Clear conversation history |

### Get History

```bash
curl "http://localhost:8000/chat/history?session_id=YOUR_SESSION_ID&chapter=Introduction%20to%20Physical%20AI"
```

### Clear History

```bash
curl -X DELETE "http://localhost:8000/chat/history?session_id=YOUR_SESSION_ID"
```

## Troubleshooting

### Connection Refused

- Ensure PostgreSQL is running
- Check DATABASE_URL is correct
- Verify port 5432 is not blocked

### Tables Not Created

- Check backend logs for errors
- Verify DATABASE_URL format
- Ensure database exists

### History Not Loading

- Check browser localStorage for session ID
- Verify API response in Network tab
- Check backend logs for errors

