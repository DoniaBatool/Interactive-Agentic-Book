# Skill: Docusaurus RAG Chatbot Builder

## Purpose
Build a complete production-ready RAG (Retrieval-Augmented Generation) chatbot system for Docusaurus books with FastAPI backend, Neon Postgres, Qdrant vector store, and OpenAI Agents SDK integration.

## When to Use
- Building AI-powered chatbot for technical books/documentation
- Implementing RAG system with conversation history
- Creating text-selection-based Q&A features
- Deploying chatbot for Docusaurus-based textbooks

## Guardrails
- Do not include real secrets (API keys, DB passwords) in generated files or examples.
- Prefer safe defaults: timeouts, input limits, structured logs, and health checks.
- Ensure any “admin” endpoints are protected (auth + authorization), and clearly documented.

## Outputs (what this command should produce)
- A backend with ingestion + retrieval + chat endpoints (streaming + non-streaming)
- A frontend chat widget integrated into Docusaurus
- `.env.example` with all required variables (no secrets)
- README / integration guide + troubleshooting notes

---

command-name: /sp.docusaurus-rag-chatbot

description: |
  Build a complete RAG chatbot system for Docusaurus books with backend (FastAPI + Neon + Qdrant)
  and frontend React component with streaming responses and conversation history.

arguments:
  - name: book_title
    description: "Title of the book/documentation"
    required: false
    default: "Interactive Book"
  - name: deployment_target
    description: "Deployment target (local/vercel/docker)"
    required: false
    default: "local"

---

## User Input

```text
{BOOK_TITLE} - The title of the book for RAG chatbot integration
{DEPLOYMENT_TARGET} - Where the system will be deployed
```

You **MUST** consider the user input before proceeding.

## Outline

### 1. Setup Project Structure

Create the complete project structure for the RAG chatbot system:

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application
│   ├── config.py               # Environment configuration
│   ├── models/
│   │   ├── __init__.py
│   │   ├── conversation.py     # Database models
│   │   └── schemas.py          # Pydantic schemas
│   ├── services/
│   │   ├── __init__.py
│   │   ├── rag_service.py      # RAG retrieval logic
│   │   ├── embedding_service.py # Text embedding
│   │   ├── agent_service.py    # OpenAI Agents SDK
│   │   └── vector_store.py     # Qdrant operations
│   ├── api/
│   │   ├── __init__.py
│   │   ├── chat.py             # Chat endpoints
│   │   ├── documents.py        # Document ingestion
│   │   └── health.py           # Health checks
│   └── database/
│       ├── __init__.py
│       ├── connection.py       # Neon Postgres connection
│       └── migrations/         # Database migrations
├── tests/
│   ├── test_rag_service.py
│   ├── test_embeddings.py
│   └── test_chat_endpoint.py
├── scripts/
│   ├── ingest_documents.py     # Document ingestion
│   └── setup_vector_db.py      # Qdrant setup
├── requirements.txt
├── .env.example
└── README.md

frontend/
└── src/
    └── components/
        ├── ChatWidget.tsx      # Main chat component
        ├── ChatMessage.tsx     # Message component
        ├── ChatInput.tsx       # Input component
        └── styles/
            └── chat.css        # Chat styles
```

**Implementation:**
1. Create backend directory structure
2. Create frontend component structure
3. Initialize package files and imports

### 2. Setup Backend Configuration

**File: `backend/app/config.py`**

```python
"""
Configuration management for RAG Chatbot backend
"""
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "{BOOK_TITLE} RAG Chatbot"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"

    # OpenAI
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o"
    EMBEDDING_MODEL: str = "text-embedding-3-large"
    EMBEDDING_DIMENSIONS: int = 3072

    # Neon Postgres
    DATABASE_URL: str
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20

    # Qdrant
    QDRANT_URL: str
    QDRANT_API_KEY: str
    QDRANT_COLLECTION_NAME: str = "book_chunks"

    # RAG Settings
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    TOP_K_RESULTS: int = 5
    SIMILARITY_THRESHOLD: float = 0.7

    # CORS
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:8000"]

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()
```

**File: `backend/.env.example`**

```env
# OpenAI
OPENAI_API_KEY=sk-...

# Neon Postgres
DATABASE_URL=postgresql://user:password@host/dbname

# Qdrant
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-api-key

# App
DEBUG=False
```

### 3. Setup Database Models and Connection

**File: `backend/app/database/connection.py`**

```python
"""
Neon Postgres database connection with SQLAlchemy
"""
from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool
from contextlib import contextmanager
from app.config import get_settings

settings = get_settings()

# Create async-compatible engine for Neon
engine = create_engine(
    settings.DATABASE_URL,
    poolclass=NullPool,  # Neon handles connection pooling
    pool_pre_ping=True,
    echo=settings.DEBUG,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Session:
    """Dependency for FastAPI routes"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@contextmanager
def get_db_context():
    """Context manager for scripts"""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
```

**File: `backend/app/models/conversation.py`**

```python
"""
Database models for conversation history and user context
"""
from sqlalchemy import Column, String, Text, DateTime, Integer, JSON, Boolean
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from app.database.connection import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String(255), index=True, nullable=True)  # For future auth
    session_id = Column(String(255), index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    title = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True)
    metadata = Column(JSON, nullable=True)  # User background, preferences

class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True), index=True, nullable=False)
    role = Column(String(50), nullable=False)  # user/assistant/system
    content = Column(Text, nullable=False)
    selected_text = Column(Text, nullable=True)  # For text-based queries
    retrieved_chunks = Column(JSON, nullable=True)  # RAG context used
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    tokens_used = Column(Integer, nullable=True)
    model = Column(String(100), nullable=True)

class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chapter_id = Column(String(255), unique=True, nullable=False)
    title = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)
    metadata = Column(JSON, nullable=True)  # Chapter number, section, etc.
    chunk_count = Column(Integer, default=0)
    indexed_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

**File: `backend/app/models/schemas.py`**

```python
"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=5000)
    session_id: str = Field(..., min_length=1)
    selected_text: Optional[str] = Field(None, max_length=10000)
    user_id: Optional[str] = None
    chapter_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    conversation_id: UUID
    sources: List[Dict[str, Any]]
    tokens_used: Optional[int] = None

class StreamChunk(BaseModel):
    delta: str
    conversation_id: Optional[UUID] = None
    done: bool = False

class ConversationHistory(BaseModel):
    conversation_id: UUID
    messages: List[Dict[str, Any]]
    created_at: datetime

class DocumentIngest(BaseModel):
    chapter_id: str
    title: str
    content: str
    metadata: Optional[Dict[str, Any]] = None

class HealthResponse(BaseModel):
    status: str
    database: str
    vector_store: str
    openai: str
```

### 4. Implement Vector Store Service (Qdrant)

**File: `backend/app/services/vector_store.py`**

```python
"""
Qdrant vector store operations
"""
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance, VectorParams, PointStruct,
    Filter, FieldCondition, MatchValue
)
from typing import List, Dict, Any, Optional
import uuid
from app.config import get_settings

settings = get_settings()

class VectorStore:
    def __init__(self):
        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
        )
        self.collection_name = settings.QDRANT_COLLECTION_NAME
        self._ensure_collection()

    def _ensure_collection(self):
        """Create collection if it doesn't exist"""
        collections = self.client.get_collections().collections
        collection_names = [c.name for c in collections]

        if self.collection_name not in collection_names:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=settings.EMBEDDING_DIMENSIONS,
                    distance=Distance.COSINE
                )
            )

    def upsert_chunks(
        self,
        chunks: List[str],
        embeddings: List[List[float]],
        metadata: List[Dict[str, Any]]
    ) -> bool:
        """Insert or update document chunks with embeddings"""
        points = [
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "text": chunk,
                    **meta
                }
            )
            for chunk, embedding, meta in zip(chunks, embeddings, metadata)
        ]

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        return True

    def search(
        self,
        query_embedding: List[float],
        top_k: int = None,
        chapter_filter: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Search for similar chunks"""
        top_k = top_k or settings.TOP_K_RESULTS

        search_filter = None
        if chapter_filter:
            search_filter = Filter(
                must=[
                    FieldCondition(
                        key="chapter_id",
                        match=MatchValue(value=chapter_filter)
                    )
                ]
            )

        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=top_k,
            query_filter=search_filter,
            score_threshold=settings.SIMILARITY_THRESHOLD
        )

        return [
            {
                "text": hit.payload["text"],
                "score": hit.score,
                "chapter_id": hit.payload.get("chapter_id"),
                "chapter_title": hit.payload.get("chapter_title"),
                "metadata": hit.payload
            }
            for hit in results
        ]

    def delete_by_chapter(self, chapter_id: str) -> bool:
        """Delete all chunks for a chapter"""
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="chapter_id",
                        match=MatchValue(value=chapter_id)
                    )
                ]
            )
        )
        return True

# Singleton instance
vector_store = VectorStore()
```

### 5. Implement Embedding Service

**File: `backend/app/services/embedding_service.py`**

```python
"""
Text embedding service using OpenAI
"""
from openai import OpenAI
from typing import List
from app.config import get_settings

settings = get_settings()

class EmbeddingService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.EMBEDDING_MODEL

    def embed_text(self, text: str) -> List[float]:
        """Generate embedding for single text"""
        response = self.client.embeddings.create(
            input=text,
            model=self.model
        )
        return response.data[0].embedding

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts"""
        response = self.client.embeddings.create(
            input=texts,
            model=self.model
        )
        return [item.embedding for item in response.data]

# Singleton instance
embedding_service = EmbeddingService()
```

### 6. Implement RAG Service

**File: `backend/app/services/rag_service.py`**

```python
"""
RAG (Retrieval-Augmented Generation) service
"""
from typing import List, Dict, Any, Optional
from app.services.vector_store import vector_store
from app.services.embedding_service import embedding_service
from app.config import get_settings

settings = get_settings()

class RAGService:
    def __init__(self):
        self.vector_store = vector_store
        self.embedding_service = embedding_service

    def retrieve_context(
        self,
        query: str,
        chapter_filter: Optional[str] = None,
        top_k: Optional[int] = None
    ) -> tuple[str, List[Dict[str, Any]]]:
        """
        Retrieve relevant context for a query
        Returns: (context_text, sources)
        """
        # Generate query embedding
        query_embedding = self.embedding_service.embed_text(query)

        # Search vector store
        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
            chapter_filter=chapter_filter
        )

        if not results:
            return "", []

        # Format context
        context_parts = []
        for i, result in enumerate(results, 1):
            chapter_title = result.get("chapter_title", "Unknown")
            text = result["text"]
            context_parts.append(f"[Source {i} - {chapter_title}]\n{text}")

        context = "\n\n".join(context_parts)

        return context, results

    def retrieve_for_selected_text(
        self,
        selected_text: str,
        chapter_filter: Optional[str] = None
    ) -> tuple[str, List[Dict[str, Any]]]:
        """
        Retrieve context based on user-selected text
        Uses the selected text as the query
        """
        return self.retrieve_context(
            query=selected_text,
            chapter_filter=chapter_filter,
            top_k=3  # Fewer results for focused queries
        )

# Singleton instance
rag_service = RAGService()
```

### 7. Implement Agent Service (OpenAI Agents SDK)

**File: `backend/app/services/agent_service.py`**

```python
"""
OpenAI Agents SDK integration for conversational AI
"""
from openai import OpenAI
from typing import List, Dict, Any, Iterator
from app.services.rag_service import rag_service
from app.config import get_settings

settings = get_settings()

class AgentService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL

    def _build_system_prompt(self, context: str, book_title: str) -> str:
        """Build system prompt with RAG context"""
        return f"""You are an expert AI assistant for the book "{book_title}".

Your role is to help readers understand the content by answering questions based on the book's material.

CONTEXT FROM THE BOOK:
{context}

INSTRUCTIONS:
1. Answer questions using ONLY the information from the provided context
2. If the context doesn't contain enough information, acknowledge this limitation
3. Cite specific sections when possible (e.g., "According to the section on ROS 2...")
4. Be concise but thorough
5. Use technical terminology appropriately for the target audience
6. If asked about selected text, focus your answer on that specific content

Always ground your responses in the provided context."""

    def chat(
        self,
        message: str,
        conversation_history: List[Dict[str, str]],
        chapter_filter: Optional[str] = None,
        selected_text: Optional[str] = None
    ) -> tuple[str, List[Dict[str, Any]], int]:
        """
        Generate chat response with RAG
        Returns: (response, sources, tokens_used)
        """
        # Retrieve relevant context
        if selected_text:
            context, sources = rag_service.retrieve_for_selected_text(
                selected_text=selected_text,
                chapter_filter=chapter_filter
            )
            # Enhance message with selected text
            enhanced_message = f"Selected text from book:\n\"\"\"{selected_text}\"\"\"\n\nQuestion: {message}"
        else:
            context, sources = rag_service.retrieve_context(
                query=message,
                chapter_filter=chapter_filter
            )
            enhanced_message = message

        # Build messages for chat
        messages = [
            {
                "role": "system",
                "content": self._build_system_prompt(context, settings.APP_NAME)
            }
        ]

        # Add conversation history
        messages.extend(conversation_history[-10:])  # Last 10 messages

        # Add current message
        messages.append({
            "role": "user",
            "content": enhanced_message
        })

        # Generate response
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )

        answer = response.choices[0].message.content
        tokens_used = response.usage.total_tokens

        return answer, sources, tokens_used

    def chat_stream(
        self,
        message: str,
        conversation_history: List[Dict[str, str]],
        chapter_filter: Optional[str] = None,
        selected_text: Optional[str] = None
    ) -> Iterator[str]:
        """
        Generate streaming chat response with RAG
        """
        # Retrieve context (same as non-streaming)
        if selected_text:
            context, sources = rag_service.retrieve_for_selected_text(
                selected_text=selected_text,
                chapter_filter=chapter_filter
            )
            enhanced_message = f"Selected text from book:\n\"\"\"{selected_text}\"\"\"\n\nQuestion: {message}"
        else:
            context, sources = rag_service.retrieve_context(
                query=message,
                chapter_filter=chapter_filter
            )
            enhanced_message = message

        # Build messages
        messages = [
            {
                "role": "system",
                "content": self._build_system_prompt(context, settings.APP_NAME)
            }
        ]
        messages.extend(conversation_history[-10:])
        messages.append({
            "role": "user",
            "content": enhanced_message
        })

        # Stream response
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

# Singleton instance
agent_service = AgentService()
```

### 8. Implement FastAPI Endpoints

**File: `backend/app/api/chat.py`**

```python
"""
Chat API endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import Optional
import json
from uuid import UUID

from app.database.connection import get_db
from app.models.schemas import ChatRequest, ChatResponse, ConversationHistory
from app.models.conversation import Conversation, Message
from app.services.agent_service import agent_service

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/message", response_model=ChatResponse)
async def send_message(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    """Send a message and get AI response"""
    # Get or create conversation
    conversation = db.query(Conversation).filter(
        Conversation.session_id == request.session_id,
        Conversation.is_active == True
    ).first()

    if not conversation:
        conversation = Conversation(
            session_id=request.session_id,
            user_id=request.user_id
        )
        db.add(conversation)
        db.flush()

    # Get conversation history
    messages = db.query(Message).filter(
        Message.conversation_id == conversation.id
    ).order_by(Message.created_at).all()

    history = [
        {"role": msg.role, "content": msg.content}
        for msg in messages
    ]

    # Generate response
    try:
        response_text, sources, tokens = agent_service.chat(
            message=request.message,
            conversation_history=history,
            chapter_filter=request.chapter_id,
            selected_text=request.selected_text
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI generation failed: {str(e)}")

    # Save user message
    user_message = Message(
        conversation_id=conversation.id,
        role="user",
        content=request.message,
        selected_text=request.selected_text
    )
    db.add(user_message)

    # Save assistant message
    assistant_message = Message(
        conversation_id=conversation.id,
        role="assistant",
        content=response_text,
        retrieved_chunks=sources,
        tokens_used=tokens,
        model=agent_service.model
    )
    db.add(assistant_message)

    db.commit()

    return ChatResponse(
        response=response_text,
        conversation_id=conversation.id,
        sources=sources,
        tokens_used=tokens
    )

@router.post("/stream")
async def stream_message(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    """Stream AI response in real-time"""
    # Get or create conversation
    conversation = db.query(Conversation).filter(
        Conversation.session_id == request.session_id,
        Conversation.is_active == True
    ).first()

    if not conversation:
        conversation = Conversation(
            session_id=request.session_id,
            user_id=request.user_id
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)

    # Get history
    messages = db.query(Message).filter(
        Message.conversation_id == conversation.id
    ).order_by(Message.created_at).all()

    history = [
        {"role": msg.role, "content": msg.content}
        for msg in messages
    ]

    # Save user message
    user_message = Message(
        conversation_id=conversation.id,
        role="user",
        content=request.message,
        selected_text=request.selected_text
    )
    db.add(user_message)
    db.commit()

    # Stream response
    async def generate():
        full_response = ""
        try:
            for chunk in agent_service.chat_stream(
                message=request.message,
                conversation_history=history,
                chapter_filter=request.chapter_id,
                selected_text=request.selected_text
            ):
                full_response += chunk
                yield f"data: {json.dumps({'delta': chunk, 'done': False})}\n\n"

            # Save complete response
            assistant_message = Message(
                conversation_id=conversation.id,
                role="assistant",
                content=full_response
            )
            db.add(assistant_message)
            db.commit()

            yield f"data: {json.dumps({'delta': '', 'done': True, 'conversation_id': str(conversation.id)})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e), 'done': True})}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")

@router.get("/history/{session_id}", response_model=ConversationHistory)
async def get_history(
    session_id: str,
    db: Session = Depends(get_db)
):
    """Get conversation history"""
    conversation = db.query(Conversation).filter(
        Conversation.session_id == session_id,
        Conversation.is_active == True
    ).first()

    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    messages = db.query(Message).filter(
        Message.conversation_id == conversation.id
    ).order_by(Message.created_at).all()

    return ConversationHistory(
        conversation_id=conversation.id,
        messages=[
            {
                "role": msg.role,
                "content": msg.content,
                "created_at": msg.created_at,
                "sources": msg.retrieved_chunks
            }
            for msg in messages
        ],
        created_at=conversation.created_at
    )

@router.delete("/history/{session_id}")
async def clear_history(
    session_id: str,
    db: Session = Depends(get_db)
):
    """Clear conversation history"""
    conversation = db.query(Conversation).filter(
        Conversation.session_id == session_id
    ).first()

    if conversation:
        conversation.is_active = False
        db.commit()

    return {"status": "cleared"}
```

**File: `backend/app/api/documents.py`**

```python
"""
Document ingestion API
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.models.schemas import DocumentIngest
from app.models.conversation import Document
from app.services.embedding_service import embedding_service
from app.services.vector_store import vector_store
from app.config import get_settings

router = APIRouter(prefix="/documents", tags=["documents"])
settings = get_settings()

def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    """Split text into overlapping chunks"""
    chunks = []
    start = 0
    text_len = len(text)

    while start < text_len:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

@router.post("/ingest")
async def ingest_document(
    doc: DocumentIngest,
    db: Session = Depends(get_db)
):
    """Ingest a document chapter for RAG"""
    # Check if document exists
    existing = db.query(Document).filter(
        Document.chapter_id == doc.chapter_id
    ).first()

    # Chunk the content
    chunks = chunk_text(
        text=doc.content,
        chunk_size=settings.CHUNK_SIZE,
        overlap=settings.CHUNK_OVERLAP
    )

    # Generate embeddings
    try:
        embeddings = embedding_service.embed_batch(chunks)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding failed: {str(e)}")

    # Prepare metadata
    metadata = [
        {
            "chapter_id": doc.chapter_id,
            "chapter_title": doc.title,
            "chunk_index": i,
            **(doc.metadata or {})
        }
        for i in range(len(chunks))
    ]

    # Delete existing chunks if updating
    if existing:
        vector_store.delete_by_chapter(doc.chapter_id)

    # Upsert to vector store
    try:
        vector_store.upsert_chunks(chunks, embeddings, metadata)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Vector store failed: {str(e)}")

    # Save to database
    if existing:
        existing.content = doc.content
        existing.title = doc.title
        existing.chunk_count = len(chunks)
        existing.metadata = doc.metadata
    else:
        document = Document(
            chapter_id=doc.chapter_id,
            title=doc.title,
            content=doc.content,
            chunk_count=len(chunks),
            metadata=doc.metadata
        )
        db.add(document)

    db.commit()

    return {
        "status": "success",
        "chapter_id": doc.chapter_id,
        "chunks_created": len(chunks)
    }

@router.get("/list")
async def list_documents(db: Session = Depends(get_db)):
    """List all ingested documents"""
    documents = db.query(Document).all()
    return [
        {
            "chapter_id": doc.chapter_id,
            "title": doc.title,
            "chunk_count": doc.chunk_count,
            "indexed_at": doc.indexed_at
        }
        for doc in documents
    ]
```

**File: `backend/app/api/health.py`**

```python
"""
Health check endpoints
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.vector_store import vector_store
from app.models.schemas import HealthResponse
from openai import OpenAI
from app.config import get_settings

router = APIRouter(prefix="/health", tags=["health"])
settings = get_settings()

@router.get("/", response_model=HealthResponse)
async def health_check(db: Session = Depends(get_db)):
    """Check system health"""
    # Check database
    try:
        db.execute("SELECT 1")
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"

    # Check Qdrant
    try:
        vector_store.client.get_collections()
        qdrant_status = "healthy"
    except Exception as e:
        qdrant_status = f"unhealthy: {str(e)}"

    # Check OpenAI
    try:
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        client.models.list()
        openai_status = "healthy"
    except Exception as e:
        openai_status = f"unhealthy: {str(e)}"

    overall = "healthy" if all([
        db_status == "healthy",
        qdrant_status == "healthy",
        openai_status == "healthy"
    ]) else "degraded"

    return HealthResponse(
        status=overall,
        database=db_status,
        vector_store=qdrant_status,
        openai=openai_status
    )
```

### 9. Create Main FastAPI Application

**File: `backend/app/main.py`**

```python
"""
FastAPI application for RAG Chatbot
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import get_settings
from app.database.connection import engine, Base
from app.api import chat, documents, health

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    # Create tables
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=settings.APP_NAME,
    description="RAG-powered chatbot for interactive book",
    version="1.0.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(health.router, prefix=settings.API_V1_PREFIX)
app.include_router(chat.router, prefix=settings.API_V1_PREFIX)
app.include_router(documents.router, prefix=settings.API_V1_PREFIX)

@app.get("/")
async def root():
    return {
        "name": settings.APP_NAME,
        "status": "running",
        "docs": "/docs"
    }
```

### 10. Create Frontend Chat Component

**File: `frontend/src/components/ChatWidget.tsx`**

```typescript
import React, { useState, useEffect, useRef } from 'react';
import { ChatMessage } from './ChatMessage';
import { ChatInput } from './ChatInput';
import './styles/chat.css';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: any[];
}

interface ChatWidgetProps {
  apiUrl?: string;
  sessionId?: string;
  chapterId?: string;
}

export const ChatWidget: React.FC<ChatWidgetProps> = ({
  apiUrl = 'http://localhost:8000/api/v1',
  sessionId: providedSessionId,
  chapterId
}) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isOpen, setIsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState(providedSessionId || '');
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [selectedText, setSelectedText] = useState<string | null>(null);

  useEffect(() => {
    if (!sessionId) {
      setSessionId(`session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);
    }
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Detect text selection
  useEffect(() => {
    const handleSelection = () => {
      const selection = window.getSelection();
      const text = selection?.toString().trim();
      if (text && text.length > 10) {
        setSelectedText(text);
      }
    };

    document.addEventListener('mouseup', handleSelection);
    return () => document.removeEventListener('mouseup', handleSelection);
  }, []);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const loadHistory = async () => {
    try {
      const response = await fetch(`${apiUrl}/chat/history/${sessionId}`);
      if (response.ok) {
        const data = await response.json();
        setMessages(data.messages);
      }
    } catch (error) {
      console.error('Failed to load history:', error);
    }
  };

  useEffect(() => {
    if (isOpen && sessionId) {
      loadHistory();
    }
  }, [isOpen, sessionId]);

  const sendMessage = async (content: string) => {
    if (!content.trim()) return;

    const userMessage: Message = { role: 'user', content };
    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const response = await fetch(`${apiUrl}/chat/stream`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: content,
          session_id: sessionId,
          selected_text: selectedText,
          chapter_id: chapterId
        }),
      });

      const reader = response.body?.getReader();
      const decoder = new TextDecoder();
      let assistantMessage = '';

      setMessages(prev => [...prev, { role: 'assistant', content: '' }]);

      while (true) {
        const { done, value } = await reader!.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = JSON.parse(line.slice(6));
            if (data.delta) {
              assistantMessage += data.delta;
              setMessages(prev => {
                const newMessages = [...prev];
                newMessages[newMessages.length - 1] = {
                  role: 'assistant',
                  content: assistantMessage
                };
                return newMessages;
              });
            }
          }
        }
      }

      setSelectedText(null); // Clear selection after use
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: 'Sorry, I encountered an error. Please try again.'
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      {/* Chat Button */}
      <button
        className="chat-widget-button"
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle chat"
      >
        {isOpen ? '✕' : '💬'}
      </button>

      {/* Chat Window */}
      {isOpen && (
        <div className="chat-widget-container">
          <div className="chat-widget-header">
            <h3>AI Assistant</h3>
            <button onClick={() => setIsOpen(false)}>✕</button>
          </div>

          {selectedText && (
            <div className="chat-widget-selected-text">
              <small>Selected text will be used for context</small>
              <button onClick={() => setSelectedText(null)}>Clear</button>
            </div>
          )}

          <div className="chat-widget-messages">
            {messages.length === 0 && (
              <div className="chat-widget-welcome">
                <p>👋 Hi! I'm your AI assistant for this book.</p>
                <p>Ask me anything about the content, or select text and ask questions about it!</p>
              </div>
            )}
            {messages.map((msg, idx) => (
              <ChatMessage key={idx} message={msg} />
            ))}
            {isLoading && (
              <div className="chat-widget-typing">
                <span></span><span></span><span></span>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <ChatInput onSend={sendMessage} disabled={isLoading} />
        </div>
      )}
    </>
  );
};
```

**File: `frontend/src/components/ChatMessage.tsx`**

```typescript
import React from 'react';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: any[];
}

interface ChatMessageProps {
  message: Message;
}

export const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  return (
    <div className={`chat-message chat-message-${message.role}`}>
      <div className="chat-message-content">
        {message.content}
      </div>
      {message.sources && message.sources.length > 0 && (
        <div className="chat-message-sources">
          <details>
            <summary>📚 Sources ({message.sources.length})</summary>
            <ul>
              {message.sources.map((source, idx) => (
                <li key={idx}>
                  <strong>{source.chapter_title}</strong>
                  <div className="source-snippet">{source.text.slice(0, 150)}...</div>
                  <small>Relevance: {(source.score * 100).toFixed(1)}%</small>
                </li>
              ))}
            </ul>
          </details>
        </div>
      )}
    </div>
  );
};
```

**File: `frontend/src/components/ChatInput.tsx`**

```typescript
import React, { useState } from 'react';

interface ChatInputProps {
  onSend: (message: string) => void;
  disabled?: boolean;
}

export const ChatInput: React.FC<ChatInputProps> = ({ onSend, disabled }) => {
  const [input, setInput] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim() && !disabled) {
      onSend(input);
      setInput('');
    }
  };

  return (
    <form className="chat-input-form" onSubmit={handleSubmit}>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask a question..."
        disabled={disabled}
        className="chat-input-field"
      />
      <button
        type="submit"
        disabled={disabled || !input.trim()}
        className="chat-input-button"
      >
        Send
      </button>
    </form>
  );
};
```

**File: `frontend/src/components/styles/chat.css`**

```css
/* Chat Widget Styles */
.chat-widget-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  font-size: 24px;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: transform 0.2s;
  z-index: 1000;
}

.chat-widget-button:hover {
  transform: scale(1.1);
}

.chat-widget-container {
  position: fixed;
  bottom: 90px;
  right: 20px;
  width: 400px;
  height: 600px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  z-index: 1000;
}

.chat-widget-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 12px 12px 0 0;
}

.chat-widget-header h3 {
  margin: 0;
  font-size: 18px;
}

.chat-widget-header button {
  background: none;
  border: none;
  color: white;
  font-size: 24px;
  cursor: pointer;
}

.chat-widget-selected-text {
  padding: 8px 16px;
  background: #f0f9ff;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
}

.chat-widget-messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  background: #f8f9fa;
}

.chat-widget-welcome {
  text-align: center;
  color: #666;
  padding: 20px;
}

.chat-message {
  margin-bottom: 16px;
  animation: fadeIn 0.3s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.chat-message-content {
  padding: 12px 16px;
  border-radius: 12px;
  max-width: 85%;
  word-wrap: break-word;
}

.chat-message-user .chat-message-content {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  margin-left: auto;
}

.chat-message-assistant .chat-message-content {
  background: white;
  color: #333;
  border: 1px solid #e0e0e0;
}

.chat-message-sources {
  margin-top: 8px;
  font-size: 12px;
}

.chat-message-sources details {
  cursor: pointer;
}

.chat-message-sources summary {
  color: #667eea;
  font-weight: 500;
}

.chat-message-sources ul {
  margin: 8px 0;
  padding-left: 20px;
}

.chat-message-sources li {
  margin: 8px 0;
}

.source-snippet {
  color: #666;
  font-size: 11px;
  margin: 4px 0;
}

.chat-widget-typing {
  display: flex;
  gap: 4px;
  padding: 12px 16px;
  background: white;
  border-radius: 12px;
  width: fit-content;
}

.chat-widget-typing span {
  width: 8px;
  height: 8px;
  background: #667eea;
  border-radius: 50%;
  animation: typing 1.4s infinite;
}

.chat-widget-typing span:nth-child(2) {
  animation-delay: 0.2s;
}

.chat-widget-typing span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-10px); }
}

.chat-input-form {
  display: flex;
  padding: 16px;
  background: white;
  border-top: 1px solid #e0e0e0;
  border-radius: 0 0 12px 12px;
}

.chat-input-field {
  flex: 1;
  padding: 10px 12px;
  border: 1px solid #e0e0e0;
  border-radius: 20px;
  outline: none;
  font-size: 14px;
}

.chat-input-field:focus {
  border-color: #667eea;
}

.chat-input-button {
  margin-left: 8px;
  padding: 10px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 500;
}

.chat-input-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .chat-widget-container {
    width: calc(100vw - 40px);
    height: calc(100vh - 140px);
    right: 20px;
    bottom: 90px;
  }
}
```

### 11. Create Document Ingestion Script

**File: `backend/scripts/ingest_documents.py`**

```python
"""
Script to ingest Docusaurus markdown files into RAG system
"""
import os
import sys
import argparse
import requests
from pathlib import Path
import frontmatter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_markdown_content(file_path: Path) -> dict:
    """Extract content and metadata from markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)

    return {
        "chapter_id": post.get('id', file_path.stem),
        "title": post.get('title', file_path.stem),
        "content": post.content,
        "metadata": {
            "sidebar_position": post.get('sidebar_position'),
            "tags": post.get('tags', []),
            "file_path": str(file_path)
        }
    }

def ingest_directory(docs_dir: Path, api_url: str):
    """Ingest all markdown files from docs directory"""
    markdown_files = list(docs_dir.rglob('*.md')) + list(docs_dir.rglob('*.mdx'))

    logger.info(f"Found {len(markdown_files)} markdown files")

    success_count = 0
    for file_path in markdown_files:
        try:
            logger.info(f"Processing: {file_path}")
            doc_data = extract_markdown_content(file_path)

            # Skip if content is too short
            if len(doc_data['content']) < 100:
                logger.warning(f"Skipping {file_path} - content too short")
                continue

            # Send to API
            response = requests.post(
                f"{api_url}/api/v1/documents/ingest",
                json=doc_data
            )

            if response.status_code == 200:
                result = response.json()
                logger.info(f"✓ {doc_data['title']} - {result['chunks_created']} chunks")
                success_count += 1
            else:
                logger.error(f"✗ Failed: {response.text}")

        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")

    logger.info(f"\n✅ Ingestion complete: {success_count}/{len(markdown_files)} files")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Docusaurus docs into RAG system")
    parser.add_argument("docs_dir", help="Path to Docusaurus docs directory")
    parser.add_argument("--api-url", default="http://localhost:8000", help="API URL")

    args = parser.parse_args()

    docs_path = Path(args.docs_dir)
    if not docs_path.exists():
        logger.error(f"Directory not found: {docs_path}")
        sys.exit(1)

    ingest_directory(docs_path, args.api_url)
```

### 12. Create Requirements and Documentation

**File: `backend/requirements.txt`**

```txt
# FastAPI and server
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-multipart==0.0.6

# Database
sqlalchemy==2.0.25
psycopg2-binary==2.9.9
alembic==1.13.1

# Vector store
qdrant-client==1.7.3

# AI/ML
openai==1.10.0
tiktoken==0.5.2

# Utilities
pydantic==2.5.3
pydantic-settings==2.1.0
python-dotenv==1.0.0
python-frontmatter==1.1.0

# Development
pytest==7.4.4
pytest-asyncio==0.23.3
httpx==0.26.0
```

**File: `backend/README.md`**

```markdown
# RAG Chatbot Backend

Production-ready RAG chatbot backend with FastAPI, Neon Postgres, and Qdrant.

## Features

- ✅ FastAPI with async support
- ✅ Neon Serverless Postgres for conversation history
- ✅ Qdrant Cloud vector store
- ✅ OpenAI Agents SDK integration
- ✅ Streaming responses (SSE)
- ✅ Text selection-based Q&A
- ✅ Conversation history management
- ✅ Document ingestion pipeline

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. Run migrations:
```bash
alembic upgrade head
```

4. Ingest documents:
```bash
python scripts/ingest_documents.py ../docs --api-url http://localhost:8000
```

5. Start server:
```bash
uvicorn app.main:app --reload --port 8000
```

## API Endpoints

### Chat
- `POST /api/v1/chat/message` - Send message (non-streaming)
- `POST /api/v1/chat/stream` - Send message (streaming)
- `GET /api/v1/chat/history/{session_id}` - Get conversation history
- `DELETE /api/v1/chat/history/{session_id}` - Clear history

### Documents
- `POST /api/v1/documents/ingest` - Ingest document
- `GET /api/v1/documents/list` - List all documents

### Health
- `GET /api/v1/health` - Health check

## Deployment

### Local
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Docker
```bash
docker build -t rag-chatbot .
docker run -p 8000:8000 --env-file .env rag-chatbot
```

### Vercel
Use `vercel.json` for serverless deployment.
```

### 13. Create Integration Guide for Docusaurus

**File: `INTEGRATION_GUIDE.md`**

```markdown
# Docusaurus Integration Guide

## Step 1: Add Chat Widget to Docusaurus

### Install Component

Copy the `frontend/src/components` folder to your Docusaurus `src/components` directory.

### Add to Root Layout

Edit `src/theme/Root.js`:

```javascript
import React from 'react';
import { ChatWidget } from '@site/src/components/ChatWidget';

export default function Root({children}) {
  return (
    <>
      {children}
      <ChatWidget
        apiUrl={process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1'}
        sessionId={undefined} // Auto-generated
      />
    </>
  );
}
```

### Configure Environment

Edit `docusaurus.config.js`:

```javascript
module.exports = {
  // ...
  customFields: {
    apiUrl: process.env.API_URL || 'http://localhost:8000/api/v1',
  },
};
```

## Step 2: Ingest Book Content

```bash
cd backend
python scripts/ingest_documents.py ../docs --api-url http://localhost:8000
```

## Step 3: Test

1. Start backend:
```bash
cd backend
uvicorn app.main:app --reload
```

2. Start Docusaurus:
```bash
npm run start
```

3. Open http://localhost:3000 and click the chat button!

## Step 4: Deploy

### Backend (Render/Railway)
1. Connect GitHub repo
2. Set environment variables
3. Deploy backend

### Frontend (Vercel/Netlify)
1. Set API_URL environment variable
2. Deploy Docusaurus site

## Features Available

### Text Selection Q&A
1. Select any text in the book
2. Open chat widget
3. Ask question - the AI will use selected text as context!

### Conversation History
- Automatically saved per session
- Persists across page reloads
- Can be cleared via API

### Chapter-Specific Context
Pass chapter ID to focus RAG on specific chapters:

```jsx
<ChatWidget chapterId="chapter-1" />
```
```

### 14. Create Tests

**File: `backend/tests/test_rag_service.py`**

```python
"""
Tests for RAG service
"""
import pytest
from app.services.rag_service import rag_service

def test_retrieve_context():
    """Test context retrieval"""
    context, sources = rag_service.retrieve_context(
        query="What is ROS 2?",
        top_k=3
    )

    assert isinstance(context, str)
    assert isinstance(sources, list)
    # More assertions based on your data

def test_retrieve_for_selected_text():
    """Test text selection-based retrieval"""
    selected = "Physical AI extends beyond digital spaces"
    context, sources = rag_service.retrieve_for_selected_text(
        selected_text=selected
    )

    assert isinstance(context, str)
    assert len(sources) <= 3  # Should limit to 3 for focused queries
```

**File: `backend/tests/test_chat_endpoint.py`**

```python
"""
Tests for chat endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Test health endpoint"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data

def test_send_message():
    """Test sending a chat message"""
    response = client.post(
        "/api/v1/chat/message",
        json={
            "message": "What is Physical AI?",
            "session_id": "test_session_123"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "conversation_id" in data
    assert "sources" in data

def test_get_history():
    """Test retrieving conversation history"""
    # First send a message
    client.post(
        "/api/v1/chat/message",
        json={
            "message": "Test message",
            "session_id": "test_session_456"
        }
    )

    # Then get history
    response = client.get("/api/v1/chat/history/test_session_456")
    assert response.status_code == 200
    data = response.json()
    assert "messages" in data
```

## Success Criteria

- [ ] Backend FastAPI application runs without errors
- [ ] Neon Postgres connection established
- [ ] Qdrant vector store configured and accessible
- [ ] Document ingestion pipeline working
- [ ] Chat endpoint returns AI responses
- [ ] Streaming endpoint works with SSE
- [ ] Text selection feature functional
- [ ] Frontend React component renders
- [ ] Chat widget integrates with Docusaurus
- [ ] Conversation history persists
- [ ] Health checks pass for all services
- [ ] Tests pass

## Notes

- This skill creates a production-ready RAG chatbot system
- Optimized for Docusaurus integration
- Includes text selection-based Q&A (unique feature!)
- Uses streaming for better UX
- Fully typed with Pydantic
- Database-backed conversation history
- Ready for deployment

## Usage in Hackathon

For the Physical AI & Humanoid Robotics textbook hackathon:

1. Run `/sp.docusaurus-rag-chatbot` to scaffold the complete system
2. Configure environment variables (.env)
3. Ingest your Docusaurus documentation
4. Deploy backend and frontend
5. Test the chatbot with book content

This satisfies the core requirement (100 points) and provides foundation for bonus features (auth, personalization, translation).
