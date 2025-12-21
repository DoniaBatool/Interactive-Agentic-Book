# Research Notes – Feature 012: Postgres Persistence

## SQLAlchemy 2.0 Async

- SQLAlchemy 2.0 introduces native async support with `create_async_engine`.
- Requires `asyncpg` driver for PostgreSQL.
- Session management via `async_sessionmaker`.

### Basic Setup

```python
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(
    "postgresql+asyncpg://user:pass@localhost/db",
    pool_size=5,
    max_overflow=10,
)

async_session = async_sessionmaker(engine, expire_on_commit=False)
```

## FastAPI Dependency Injection

- Use `Depends()` to inject database sessions into endpoints.
- Proper session lifecycle management (create, use, close).

```python
async def get_db():
    async with async_session() as session:
        yield session

@app.get("/items")
async def get_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item))
    return result.scalars().all()
```

## Session Management Strategies

### Option 1: UUID in localStorage (Chosen)
- Generate UUID client-side
- Store in localStorage
- Send with every request
- Pros: Simple, works for anonymous users
- Cons: Tied to browser/device

### Option 2: JWT Tokens
- Server generates session token
- Stored in httpOnly cookie
- Pros: More secure, cross-tab sync
- Cons: More complex, needs backend session store

### Option 3: Database Sessions with Expiry
- Server creates session record
- Return session ID to client
- Expire after inactivity
- Pros: Full control
- Cons: More complexity

## PostgreSQL JSON/JSONB

- Use JSONB for citations storage
- Allows efficient querying of JSON fields
- SQLAlchemy supports via `JSONB` type

```python
from sqlalchemy.dialects.postgresql import JSONB

class Message(Base):
    citations = Column(JSONB, nullable=True)
```

## Connection Pooling

### PgBouncer vs SQLAlchemy Pool

- SQLAlchemy has built-in connection pooling
- For serverless/high-scale, consider PgBouncer
- For this project, SQLAlchemy pool is sufficient

### Pool Configuration

```python
engine = create_async_engine(
    DATABASE_URL,
    pool_size=5,          # Number of permanent connections
    max_overflow=10,       # Additional connections under load
    pool_timeout=30,       # Wait time for connection
    pool_recycle=1800,     # Recycle connections after 30 min
)
```

## Migration Strategy

### Option 1: Auto-create (Chosen for MVP)
- Use `Base.metadata.create_all()` on startup
- Simple, works for development
- Not recommended for production

### Option 2: Alembic Migrations
- Proper version-controlled migrations
- Required for production
- Can be added later

## Cloud PostgreSQL Options

- **NeonDB** (Recommended): Serverless PostgreSQL, free tier, auto-scaling ⭐
- **Supabase**: Free tier, hosted PostgreSQL
- **Railway**: Simple deployment, $5/month
- **Render**: Free tier with limitations

## NeonDB Implementation Notes

### URL Conversion
```python
# NeonDB provides: postgresql://user:pass@host/db?sslmode=require
# asyncpg requires: postgresql+asyncpg://user:pass@host/db (with SSL context)
```

### SSL Configuration for NeonDB
```python
import ssl
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
connect_args = {"ssl": ssl_context}
```

### Connection Pooling
- NeonDB manages connection pooling server-side
- Use `NullPool` in SQLAlchemy for serverless databases
- Avoid `pool_size` settings with serverless DBs

## Security Considerations

- Sanitize session IDs (UUID format validation)
- Rate limiting on history endpoints
- Don't store sensitive data in messages
- Consider message retention policy

