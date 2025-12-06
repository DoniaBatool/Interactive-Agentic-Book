# Data Model: Chapter 2 AI Runtime Engine Integration

**Feature**: 013-chapter-2-runtime-engine
**Date**: 2025-12-05
**Purpose**: Define data structures and entities for Chapter 2 runtime engine integration

## Overview

This document defines the data structures, entities, and relationships for Chapter 2 runtime engine integration: routing, RAG binding, subagents, skills, and ChatKit scaffolding. All structures are placeholders with TODO markers for future implementation.

## Entities

### 1. Chapter 2 Runtime Engine Request

**Storage**: Passed to `run_ai_block()` function

**Structure**:
```python
{
    "block_type": str,            # "ask-question", "explain-like-10", "quiz", "diagram"
    "request_data": {
        "chapterId": 2,           # Chapter identifier (always 2 for Chapter 2)
        "question": str,           # User question (for ask-question)
        "sectionId": str,          # Optional section identifier
        "concept": str,            # Concept name (for explain-like-10)
        "numQuestions": int,       # Number of questions (for quiz)
        "diagramType": str,        # Diagram type (for diagram)
        "concepts": List[str]      # Concepts to include (for diagram)
    }
}
```

**Function**:
```python
async def run_ai_block(
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Chapter 2 routing
    TODO: If chapterId=2, route to Chapter 2 subagent
    TODO: Load Chapter 2 RAG context
    TODO: Call Chapter 2 subagent with context
    """
    return {"message": "placeholder", "data": {}}
```

**Validation**:
- Function must exist and be importable
- Function signature must match pattern
- Return type must be `Dict[str, Any]`
- Placeholder return acceptable

**Relationship**: 1:1 with Chapter 2 Subagent (one request → one subagent)

---

### 2. Chapter 2 Subagent

**Storage**: Python modules `backend/app/ai/subagents/ch2_*.py`

**Structure**:
```python
# ch2_ask_question_agent.py
async def ch2_ask_question_agent(
    question: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Process ROS 2 question with Chapter 2 context
    TODO: Use ROS 2 concepts, analogies, examples
    TODO: Return formatted answer
    """
    return {
        "answer": "",
        "sources": [],
        "confidence": 0.0
    }

# ch2_explain_el10_agent.py
async def ch2_explain_el10_agent(
    concept: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Generate ROS 2 explanation with Chapter 2 context
    TODO: Use age-appropriate analogies for ROS 2 concepts
    TODO: Return formatted explanation
    """
    return {
        "explanation": "",
        "examples": [],
        "analogies": []
    }

# ch2_quiz_agent.py
async def ch2_quiz_agent(
    chapter_id: int,
    num_questions: int,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Generate ROS 2 quiz with Chapter 2 context
    TODO: Cover ROS 2 learning objectives
    TODO: Return formatted quiz
    """
    return {
        "questions": [],
        "learning_objectives": []
    }

# ch2_diagram_agent.py
async def ch2_diagram_agent(
    diagram_type: str,
    concepts: List[str],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Generate ROS 2 diagram with Chapter 2 context
    TODO: Use ROS 2 concepts and relationships
    TODO: Return formatted diagram
    """
    return {
        "diagram_url": "",
        "metadata": {
            "title": "",
            "description": "",
            "concepts": [],
            "format": ""
        }
    }
```

**Validation**:
- Functions must exist and be importable
- Function signatures must match patterns
- Return types must match expected structures
- Placeholder returns acceptable

**Relationship**: 1:1 with Runtime Engine Request (one subagent per request)

---

### 3. Chapter 2 RAG Context

**Storage**: Returned by `run_rag_pipeline()` function

**Structure**:
```python
{
    "context": str,                    # Assembled context string
    "chunks": List[Dict[str, Any]],   # Retrieved chunks with metadata
    "query_embedding": List[float]     # Query embedding vector
}
```

**Function**:
```python
async def run_rag_pipeline(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> Dict[str, Any]:
    """
    TODO: Chapter 2 RAG binding
    TODO: If chapter_id == 2, load Chapter 2 chunks
    TODO: Embed query
    TODO: Search in Qdrant collection "chapter_2"
    TODO: Assemble context
    """
    return {
        "context": "",
        "chunks": [],
        "query_embedding": []
    }
```

**Validation**:
- Function must exist and be importable
- Return type must match structure
- Placeholder return acceptable

**Relationship**: N:1 with Chapter 2 Subagent (multiple queries → one context per query)

---

### 4. Chapter 2 Skills Integration

**Storage**: Python modules `backend/app/ai/skills/*.py`

**Structure**:
```python
# retrieval_skill.py
async def retrieve_content(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> List[Dict[str, Any]]:
    """
    TODO: Chapter-aware retrieval
    TODO: If chapter_id == 2, use Chapter 2 RAG pipeline
    TODO: Return Chapter 2 chunks with ROS 2 context
    """
    return []

# prompt_builder_skill.py
def build_prompt(
    block_type: str,
    user_input: str,
    context: List[Dict[str, Any]],
    chapter_id: int
) -> str:
    """
    TODO: Chapter-aware prompt builder
    TODO: If chapter_id == 2, build ROS 2-specific prompts
    TODO: Include ROS 2 concepts, analogies, examples
    """
    return ""

# formatting_skill.py
def format_response(
    response: Dict[str, Any],
    block_type: str,
    chapter_id: int
) -> Dict[str, Any]:
    """
    TODO: Chapter 2 formatting rules
    TODO: If chapter_id == 2, apply Chapter 2 formatting
    TODO: Include ROS 2-specific metadata
    """
    return {}
```

**Validation**:
- Functions must exist and be importable
- Function signatures must match patterns
- Placeholder returns acceptable

**Relationship**: N:1 with Chapter 2 Subagent (multiple skills → one subagent)

---

### 5. Chapter 2 ChatKit Session

**Storage**: Managed by `session_manager.py`

**Structure**:
```python
{
    "session_id": str,              # Unique session identifier
    "user_id": str,                 # User identifier
    "chapter_context": {
        2: {                        # Chapter 2 context
            "last_accessed": str,   # ISO 8601 timestamp
            "message_count": int,    # Number of messages
            "topics": List[str]      # ROS 2 topics discussed
        }
    },
    "messages": List[Dict[str, Any]]  # Message history
}
```

**Function**:
```python
def create_session(user_id: str) -> str:
    """
    TODO: Multi-chapter session contexts
    TODO: Track Chapter 2 context in session
    TODO: Support cross-chapter queries
    """
    return ""

def append_message(session_id: str, message: Dict[str, Any]) -> bool:
    """
    TODO: Append message with Chapter 2 context
    TODO: Update Chapter 2 context in session
    """
    return False

def get_history(session_id: str) -> List[Dict[str, Any]]:
    """
    TODO: Retrieve session history with Chapter 2 context
    TODO: Filter by chapter if needed
    """
    return []
```

**Validation**:
- Functions must exist and be importable
- Function signatures must match patterns
- Placeholder returns acceptable

**Relationship**: 1:N with Chapter 2 Runtime Requests (one session → multiple requests)

---

### 6. Chapter 2 ChatKit Tools

**Storage**: Python module `backend/app/ai/chatkit/tools.py`

**Structure**:
```python
# Tool definitions for Chapter 2 blocks
CH2_TOOLS = {
    "ch2_ask_question": {
        "name": "ch2_ask_question",
        "description": "Ask questions about ROS 2 concepts",
        "input": {
            "question": str,
            "sectionId": str (optional)
        },
        "output": {
            "answer": str,
            "sources": List[str]
        }
    },
    "ch2_explain_el10": {
        "name": "ch2_explain_el10",
        "description": "Explain ROS 2 concepts like I'm 10",
        "input": {
            "concept": str
        },
        "output": {
            "explanation": str,
            "examples": List[str]
        }
    },
    "ch2_quiz": {
        "name": "ch2_quiz",
        "description": "Generate ROS 2 quizzes",
        "input": {
            "numQuestions": int
        },
        "output": {
            "questions": List[Dict],
            "learning_objectives": List[str]
        }
    },
    "ch2_diagram": {
        "name": "ch2_diagram",
        "description": "Generate ROS 2 diagrams",
        "input": {
            "diagramType": str,
            "concepts": List[str]
        },
        "output": {
            "diagram_url": str,
            "metadata": Dict
        }
    }
}
```

**Validation**:
- Tool definitions must be documented
- Input/output schemas must be defined
- Placeholder definitions acceptable

**Relationship**: 1:1 with Chapter 2 Subagents (one tool per subagent)

---

### 7. Chapter 2 Configuration Settings

**Storage**: `backend/app/config/settings.py` and `.env.example`

**Structure**:
```python
# settings.py
DEFAULT_CH2_MODEL = os.getenv("DEFAULT_CH2_MODEL", "gpt-4o")
DEFAULT_CH2_EMBEDDINGS = os.getenv("DEFAULT_CH2_EMBEDDINGS", "text-embedding-3-small")
ENABLE_CHAPTER_2_RUNTIME = os.getenv("ENABLE_CHAPTER_2_RUNTIME", "True").lower() == "true"
```

**Environment Variables**:
```bash
# .env.example
DEFAULT_CH2_MODEL="gpt-4o"                    # Default LLM model for Chapter 2
DEFAULT_CH2_EMBEDDINGS="text-embedding-3-small"  # Default embedding model for Chapter 2
ENABLE_CHAPTER_2_RUNTIME=True                 # Enable/disable Chapter 2 runtime
```

**Validation**:
- Settings must be readable from environment variables
- Default values must be provided
- Settings must be documented in `.env.example`

**Relationship**: 1:1 with Runtime Engine (one config → one runtime engine)

## Relationships

### Entity Relationship Diagram

```
API Request (chapterId=2)
    ↓
Runtime Engine (run_ai_block)
    ↓
RAG Pipeline (run_rag_pipeline, chapter_id=2)
    ↓
Chapter 2 RAG Context
    ↓
Chapter 2 Subagent (ch2_*_agent)
    ↓
Skills (retrieval, prompt_builder, formatting)
    ↓
LLM Provider (DEFAULT_CH2_MODEL)
    ↓
Formatted Response
    ↓
API Response
```

### Data Flow

1. **Request**: Frontend sends request → API endpoint receives with chapterId=2
2. **Routing**: Runtime engine identifies chapterId=2 → routes to Chapter 2 subagent
3. **RAG**: RAG pipeline retrieves Chapter 2 context
4. **Skills**: Skills assemble context + user input into ROS 2 prompts
5. **Subagent**: Chapter 2 subagent processes with ROS 2 context
6. **LLM**: LLM provider generates response with ROS 2 context
7. **Formatting**: Skills format response for frontend
8. **Response**: API returns formatted response → Frontend displays

## Validation Rules

### Runtime Engine Request Validation
- `chapterId` must be 2 for Chapter 2 requests
- `block_type` must be valid ("ask-question", "explain-like-10", "quiz", "diagram")
- Request data must match block type structure

### Subagent Validation
- Subagent functions must exist and be importable
- Function signatures must match expected patterns
- Return types must match expected structures

### RAG Context Validation
- Context must include Chapter 2 chunks when chapter_id=2
- Chunks must have Chapter 2 metadata
- Query embedding must be valid vector

### Skills Validation
- Skills must be chapter-aware
- Skills must handle chapter_id=2 correctly
- Skills must return expected structures

### ChatKit Validation
- Session must track Chapter 2 context
- Tools must be defined for Chapter 2 blocks
- Tool schemas must match subagent contracts

## Status

⚠️ **All data structures are placeholders. Real implementation will be added in future features.**
