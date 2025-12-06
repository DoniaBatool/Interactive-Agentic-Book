# Data Model: AI Runtime Engine Extension for Chapter 2

**Feature**: 020-chapter-2-ai-runtime
**Date**: 2025-12-05
**Purpose**: Define data structures and entities for extending the AI Runtime Engine to support Chapter 2 content

## Overview

This document defines the data structures, entities, and relationships for extending the AI Runtime Engine (Feature 005) to support Chapter 2: RAG collection setup, embedding pipeline extension, runtime routing, subagents, skills reuse, and ChatKit integration. All structures are placeholders with TODO markers for future implementation.

## Entities

### 1. RAG Collection Setup

**Storage**: `backend/app/ai/rag/collections/ch2_collection.py`

**Structure**:
```python
CH2_COLLECTION_NAME: str = "chapter_2"

def create_collection() -> None:
    """TODO: Create Qdrant collection for Chapter 2"""
    pass

def upsert_vectors(chunks: List[str], embeddings: List[List[float]]) -> None:
    """TODO: Upsert vectors to Chapter 2 collection"""
    pass

def search(query_embedding: List[float], top_k: int) -> List[Dict[str, Any]]:
    """TODO: Search Chapter 2 collection"""
    return []
```

**Validation**:
- File must exist at specified path
- Constant `CH2_COLLECTION_NAME` must be defined
- Functions must have correct signatures
- Placeholder implementations acceptable

**Relationship**: 1:1 with Chapter 2 RAG Pipeline (collection used by pipeline)

---

### 2. Embedding Pipeline Extension

**Storage**: `backend/app/ai/embeddings/embedding_client.py`

**Structure**:
```python
def generate_embedding(text: str, chapter_id: int = 1) -> List[float]:
    """TODO: Add chapter_id parameter support for Chapter 2"""
    return []

def batch_embed_ch2(chunks: List[str]) -> List[List[float]]:
    """TODO: Batch embedding for Chapter 2 chunks"""
    return []
```

**Validation**:
- Functions must exist and be importable
- Function signatures must match pattern
- Placeholder implementations acceptable

**Relationship**: N:1 with RAG Pipeline (embeddings used by pipeline)

---

### 3. Runtime Routing Extension

**Storage**: `backend/app/ai/runtime/engine.py`

**Structure**:
```python
async def run_ai_block(block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    TODO: Chapter 2 routing
    chapter_id = request_data.get("chapterId", 1)
    if chapter_id == 2:
        # TODO: Route to CH2 RAG
        # TODO: Call CH2 subagents
        # TODO: Use CH2 context
    """
    return {"message": "placeholder", "data": {}}
```

**Validation**:
- Function must exist and be importable
- Function signature must match pattern
- Chapter 2 routing logic must be present (TODO acceptable)
- Placeholder return acceptable

**Relationship**: 1:N with Chapter 2 Subagents (one request → one subagent)

---

### 4. Chapter 2 Subagents

**Storage**: Python modules `backend/app/ai/subagents/ch2_*.py`

**Structure**:
```python
# ch2_ask_question_agent.py
async def ch2_ask_question_agent(question: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Input schema placeholder
    Output schema placeholder
    TODO: orchestrate provider + RAG
    """
    return {"answer": "", "sources": []}

# ch2_el10_agent.py
async def ch2_el10_agent(concept: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Input schema placeholder
    Output schema placeholder
    TODO: orchestrate provider + RAG
    """
    return {"explanation": "", "examples": []}

# ch2_quiz_agent.py
async def ch2_quiz_agent(chapter_id: int, num_questions: int, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Input schema placeholder
    Output schema placeholder
    TODO: orchestrate provider + RAG
    """
    return {"questions": [], "answers": []}

# ch2_diagram_agent.py
async def ch2_diagram_agent(diagram_type: str, concepts: List[str], context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Input schema placeholder
    Output schema placeholder
    TODO: orchestrate provider + RAG
    """
    return {"diagram": "", "description": ""}
```

**Validation**:
- All 4 subagent files must exist
- Functions must have correct signatures
- Input/output schema placeholders must be present
- TODO comments must be present

**Relationship**: 1:1 with Runtime Engine (one subagent per request)

---

### 5. Skills Reuse

**Storage**: `backend/app/ai/skills/retrieval_skill.py`, `backend/app/ai/skills/prompt_builder_skill.py`

**Structure**:
```python
# retrieval_skill.py
async def retrieve_content(query: str, chapter_id: int, top_k: int = 5) -> List[Dict[str, Any]]:
    """
    TODO: support CH2 collection name
    if chapter_id == 2:
        # TODO: Use CH2 collection
    """
    return []

# prompt_builder_skill.py
def build_prompt(block_type: str, user_input: str, context: List[Dict], chapter_id: int = None) -> str:
    """
    TODO: templates for CH2
    if chapter_id == 2:
        # TODO: Use CH2 templates
    """
    return ""
```

**Validation**:
- Functions must exist and be importable
- TODO comments for CH2 support must be present
- Placeholder implementations acceptable

**Relationship**: N:1 with Subagents (skills used by subagents)

---

### 6. ChatKit Session Support

**Storage**: `backend/app/ai/chatkit/session_manager.py`

**Structure**:
```python
class SessionManager:
    """
    TODO: Extend session_manager to track chapterId=2
    TODO: attach CH2 memory nodes
    """
    def create_session(self, chapter_id: int = 1) -> Dict[str, Any]:
        """TODO: Support chapterId=2"""
        return {"session_id": "", "chapter_id": chapter_id}
    
    def attach_memory_nodes(self, session_id: str, chapter_id: int) -> None:
        """TODO: attach CH2 memory nodes"""
        pass
```

**Validation**:
- Session manager must exist and be importable
- TODO comments for Chapter 2 support must be present
- Placeholder implementations acceptable

**Relationship**: 1:N with Sessions (one manager → many sessions)

---

### 7. Configuration

**Storage**: `backend/app/config/settings.py`, `.env.example`

**Structure**:
```python
# settings.py
class Settings(BaseSettings):
    QDRANT_COLLECTION_CH2: Optional[str] = None
    CH2_EMBEDDING_MODEL: Optional[str] = None
    CH2_LLM_MODEL: Optional[str] = None
```

```env
# .env.example
QDRANT_COLLECTION_CH2="chapter_2"
CH2_EMBEDDING_MODEL="text-embedding-3-small"
CH2_LLM_MODEL="gpt-4o-mini"
```

**Validation**:
- Settings must be added to Settings class
- Environment variables must be documented in .env.example
- All settings must be optional (default to None)

**Relationship**: 1:1 with Runtime Engine (configuration used by runtime)

---

## Data Relationships

```
Runtime Engine (engine.py)
    │
    ├─► RAG Collection (ch2_collection.py)
    │   └─► Uses: QDRANT_COLLECTION_CH2
    │
    ├─► Embedding Pipeline (embedding_client.py)
    │   └─► Uses: CH2_EMBEDDING_MODEL
    │
    ├─► Chapter 2 Subagents (ch2_*.py)
    │   ├─► Uses: Skills (retrieval_skill.py, prompt_builder_skill.py)
    │   └─► Uses: LLM Provider (CH2_LLM_MODEL)
    │
    └─► ChatKit Session Manager (session_manager.py)
        └─► Tracks: chapterId=2
```

## Data Flow

### Current Flow (Scaffolding)

1. **Request**: Frontend sends request with chapterId=2 → API endpoint
2. **Routing**: API routes to runtime engine → Runtime engine checks chapterId
3. **RAG**: Runtime engine calls RAG collection (TODO) → Returns placeholder context
4. **Embedding**: Embedding client generates embeddings (TODO) → Returns placeholder embeddings
5. **Subagent**: Runtime engine calls Chapter 2 subagent (TODO) → Returns placeholder response
6. **Response**: Runtime engine formats response → Returns to API → Frontend

### Future Flow (Implementation)

1. **Request**: Frontend sends request with chapterId=2 → API endpoint
2. **Routing**: API routes to runtime engine → Runtime engine routes to Chapter 2 handlers
3. **RAG**: Runtime engine calls RAG collection → Searches Chapter 2 collection → Returns context
4. **Embedding**: Embedding client generates embeddings for query → Returns embeddings
5. **Subagent**: Runtime engine calls Chapter 2 subagent with context → Subagent uses skills + LLM → Returns response
6. **Response**: Runtime engine formats response → Returns to API → Frontend

## Validation Summary

- ✅ All entities have clear structure definitions
- ✅ All relationships are documented
- ✅ All TODO placeholders are identified
- ✅ All validation rules are specified
- ✅ Data flow is documented for both scaffolding and future implementation
