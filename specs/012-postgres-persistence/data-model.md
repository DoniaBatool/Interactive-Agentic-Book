# Data Model – Feature 012: Postgres Persistence

## Database Schema

### Sessions Table

```sql
CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(36) UNIQUE NOT NULL,
    user_id INTEGER NULL,  -- For future auth integration
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_sessions_session_id ON sessions(session_id);
CREATE INDEX idx_sessions_user_id ON sessions(user_id);
```

### Messages Table

```sql
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(36) NOT NULL REFERENCES sessions(session_id),
    chapter VARCHAR(255) NULL,
    role VARCHAR(20) NOT NULL,  -- 'user' or 'assistant'
    content TEXT NOT NULL,
    citations JSONB NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_messages_session_id ON messages(session_id);
CREATE INDEX idx_messages_session_chapter ON messages(session_id, chapter);
CREATE INDEX idx_messages_created_at ON messages(created_at);
```

## SQLAlchemy Models

### Session Model

```python
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(36), unique=True, nullable=False, index=True)
    user_id = Column(Integer, nullable=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    messages = relationship("Message", back_populates="session")
```

### Message Model

```python
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(36), ForeignKey("sessions.session_id"), nullable=False, index=True)
    chapter = Column(String(255), nullable=True)
    role = Column(String(20), nullable=False)  # 'user' or 'assistant'
    content = Column(Text, nullable=False)
    citations = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    session = relationship("Session", back_populates="messages")
```

## API Schemas

### MessageHistory Response

```python
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MessageHistoryItem(BaseModel):
    id: int
    role: str
    content: str
    citations: Optional[List[dict]] = None
    created_at: datetime

    class Config:
        from_attributes = True

class HistoryResponse(BaseModel):
    session_id: str
    chapter: Optional[str] = None
    messages: List[MessageHistoryItem]
    total: int
```

### History Request Parameters

```python
class HistoryParams(BaseModel):
    session_id: str
    chapter: Optional[str] = None
    limit: int = 100
    offset: int = 0
```

## Frontend Storage

### localStorage Schema

```typescript
// Key: 'rag-chat-session-id'
// Value: UUID string (e.g., "550e8400-e29b-41d4-a716-446655440000")

interface StoredSession {
  sessionId: string;
  createdAt: string;
}
```

### Request Headers

```typescript
// Added to all chat requests
headers: {
  'Content-Type': 'application/json',
  'X-Session-ID': sessionId,
}
```

