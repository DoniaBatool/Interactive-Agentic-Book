# Data Model: AI Runtime Engine for Chapter 1

**Feature**: 005-ai-runtime-engine
**Date**: 2025-12-05
**Purpose**: Define function signatures, type hints, request/response structures, and data flow contracts for AI runtime infrastructure

## Overview

This feature creates scaffolding for AI runtime infrastructure with no persistent data storage or database schemas. The "data model" consists of:

1. **Function Signatures**: Type hints for all functions across modules
2. **Request/Response Structures**: Data contracts for API endpoints and internal functions
3. **Configuration Schemas**: Environment variables and settings structures
4. **Data Flow Contracts**: How data flows through the runtime engine

**Note**: No user data, database tables, or persistent storage exists in this phase. Future features will add actual data models for chat history, user sessions, vector embeddings, etc.

## Function Signature Schemas

### 1. LLM Provider Interface

**File**: `backend/app/ai/providers/base_llm.py`

**Abstract Method Signature**:
```python
@abstractmethod
async def generate(
    self,
    prompt: str,                                    # Required: User prompt text
    system: Optional[str] = None,                   # Optional: System message
    messages: Optional[List[Dict[str, str]]] = None, # Optional: Conversation history
    temperature: float = 0.7                        # Optional: Sampling temperature (0.0-2.0)
) -> Dict[str, Any]:                               # Returns: Full response object
    """
    Expected Response Structure:
    {
        "text": str,              # Generated text response
        "metadata": {
            "model": str,          # Model used
            "tokens": int,         # Token count
            "finish_reason": str   # Completion reason
        }
    }
    """
    pass
```

**Type Definitions**:
- `prompt`: `str` - Non-empty string, user's question or input
- `system`: `Optional[str]` - System instructions, role definition, or None
- `messages`: `Optional[List[Dict[str, str]]]` - Conversation history format: `[{"role": "user", "content": "..."}]`
- `temperature`: `float` - Range 0.0-2.0, default 0.7
- **Return**: `Dict[str, Any]` - Provider-specific response format (standardized in future)

---

### 2. Embedding Client Functions

**File**: `backend/app/ai/embeddings/embedding_client.py`

**Function Signatures**:
```python
def generate_embedding(text: str) -> List[float]:
    """
    Generate embedding vector for single text.
    
    Args:
        text: Input text to embed (non-empty string)
    
    Returns:
        List of float values representing embedding vector
        Example: [0.123, -0.456, 0.789, ...] (dimension depends on model)
    
    TODO: Implement using configured embedding model
    """
    pass

def batch_embed(chunks: List[str]) -> List[List[float]]:
    """
    Generate embeddings for multiple text chunks.
    
    Args:
        chunks: List of text strings to embed
    
    Returns:
        List of embedding vectors (one per chunk)
        Example: [[0.123, ...], [0.456, ...], ...]
    
    TODO: Implement batch processing for efficiency
    """
    pass
```

**Type Definitions**:
- `text`: `str` - Non-empty string
- `chunks`: `List[str]` - List of non-empty strings
- **Return (single)**: `List[float]` - Vector of floats (dimension: model-dependent, typically 1536 for text-embedding-3-small)
- **Return (batch)**: `List[List[float]]` - List of vectors

---

### 3. Qdrant Store Functions

**File**: `backend/app/ai/rag/qdrant_store.py`

**Function Signatures**:
```python
def create_collection(collection_name: str) -> bool:
    """
    Create Qdrant collection for chapter content.
    
    Args:
        collection_name: Name of collection to create (e.g., "chapter_1_content")
    
    Returns:
        True if successful, False otherwise
    
    TODO: Implement Qdrant collection creation
    """
    pass

def upsert_vectors(
    collection_name: str,
    vectors: List[Dict[str, Any]]
) -> bool:
    """
    Insert or update vectors in Qdrant collection.
    
    Args:
        collection_name: Name of collection
        vectors: List of vector documents with structure:
            {
                "id": str,                    # Unique document ID
                "vector": List[float],        # Embedding vector
                "payload": {                 # Metadata
                    "text": str,              # Original text chunk
                    "chapter_id": int,        # Chapter identifier
                    "section_id": str,        # Section identifier
                    "position": int           # Position in chapter
                }
            }
    
    Returns:
        True if successful, False otherwise
    
    TODO: Implement vector upsert operation
    """
    pass

def similarity_search(
    collection_name: str,
    query: str,                                # Query text or embedding vector
    top_k: int = 5
) -> List[Dict[str, Any]]:
    """
    Perform similarity search in Qdrant collection.
    
    Args:
        collection_name: Name of collection to search
        query: Query text (will be embedded) or embedding vector
        top_k: Number of results to return (default: 5)
    
    Returns:
        List of similar documents with structure:
            [
                {
                    "id": str,                # Document ID
                    "score": float,           # Similarity score
                    "payload": {              # Metadata
                        "text": str,
                        "chapter_id": int,
                        "section_id": str,
                        "position": int
                    }
                },
                ...
            ]
    
    TODO: Implement similarity search operation
    """
    pass
```

**Type Definitions**:
- `collection_name`: `str` - Non-empty string
- `vectors`: `List[Dict[str, Any]]` - List of vector documents with required fields
- `query`: `str` - Query text (will be embedded internally)
- `top_k`: `int` - Positive integer, default 5
- **Return (search)**: `List[Dict[str, Any]]` - Sorted by similarity score (highest first)

---

### 4. RAG Pipeline Function

**File**: `backend/app/ai/rag/pipeline.py`

**Function Signature**:
```python
async def run_rag_pipeline(
    query: str,                                # User query text
    chapter_id: int,                           # Chapter ID for context
    top_k: int = 5                             # Number of chunks to retrieve
) -> Dict[str, Any]:
    """
    Execute RAG pipeline: retrieve → embed → search → context → LLM.
    
    Args:
        query: User query text
        chapter_id: Chapter ID for context retrieval
        top_k: Number of chunks to retrieve (default: 5)
    
    Returns:
        Dictionary with structure:
        {
            "context": str,                    # Assembled context string
            "chunks": List[Dict[str, Any]],   # Retrieved chunks with metadata
            "query_embedding": List[float]    # Query embedding vector
        }
    
    Pipeline Steps (all TODO):
    1. Retrieve chapter chunks
    2. Embed user query
    3. Perform Qdrant search
    4. Construct retrieval context
    5. Pass into provider LLM (future)
    
    TODO: Implement all RAG pipeline steps
    """
    pass
```

**Type Definitions**:
- `query`: `str` - Non-empty string
- `chapter_id`: `int` - Positive integer (1 for Chapter 1)
- `top_k`: `int` - Positive integer, default 5
- **Return**: `Dict[str, Any]` - Context and metadata for LLM

---

### 5. Runtime Engine Function

**File**: `backend/app/ai/runtime/engine.py`

**Function Signature**:
```python
async def run_ai_block(
    block_type: str,                           # AI block type identifier
    request_data: Dict[str, Any]               # Request payload from API
) -> Dict[str, Any]:
    """
    Unified AI block runtime entry point.
    
    Args:
        block_type: Type of AI block ("ask-question", "explain-like-10", "quiz", "diagram")
        request_data: Request payload matching block type:
            - "ask-question": {"question": str, "chapterId": int, "sectionId": str}
            - "explain-like-10": {"concept": str, "chapterId": int}
            - "quiz": {"chapterId": int, "numQuestions": int}
            - "diagram": {"diagramType": str, "chapterId": int, "concepts": List[str]}
    
    Returns:
        Formatted response for frontend (structure depends on block_type)
    
    Runtime Flow (all TODO):
    1. Router: Determine which subagent to use
    2. RAG: Retrieve relevant context
    3. LLM Selection: Choose provider based on config
    4. Response Formatting: Format output for frontend
    
    TODO: Implement routing, RAG, LLM selection, formatting
    """
    pass
```

**Type Definitions**:
- `block_type`: `str` - One of: "ask-question", "explain-like-10", "quiz", "diagram"
- `request_data`: `Dict[str, Any]` - Block-specific request payload
- **Return**: `Dict[str, Any]` - Block-specific response format

---

### 6. Subagent Function Signatures

#### ask_question_agent

**File**: `backend/app/ai/subagents/ask_question_agent.py`

```python
async def ask_question_agent(
    question: str,                              # User question text
    context: Dict[str, Any]                    # RAG context from pipeline
) -> Dict[str, Any]:
    """
    Question-answering agent blueprint.
    
    Expected Input:
        question: str                          # User question
        context: {
            "context": str,                     # Retrieved context chunks
            "chunks": List[Dict],              # Chunk metadata
            "query_embedding": List[float]     # Query vector
        }
    
    Expected Output:
        {
            "answer": str,                     # Generated answer text
            "sources": List[str],              # Source citations (section IDs)
            "confidence": float                # Confidence score (0.0-1.0)
        }
    
    TODO: Implement question-answering logic
    """
    pass
```

#### explain_el10_agent

**File**: `backend/app/ai/subagents/explain_el10_agent.py`

```python
async def explain_el10_agent(
    concept: str,                               # Concept name to explain
    context: Dict[str, Any]                    # RAG context
) -> Dict[str, Any]:
    """
    Simplified explanation agent blueprint.
    
    Expected Input:
        concept: str                           # Concept name
        context: Dict[str, Any]               # RAG context
    
    Expected Output:
        {
            "explanation": str,                # Simplified explanation
            "examples": List[str],             # Analogies or examples
            "analogies": List[str]             # Age-appropriate analogies
        }
    
    TODO: Implement ELI10 explanation logic
    """
    pass
```

#### quiz_agent

**File**: `backend/app/ai/subagents/quiz_agent.py`

```python
async def quiz_agent(
    chapter_id: int,                            # Chapter ID
    num_questions: int,                        # Number of questions
    context: Dict[str, Any]                    # RAG context
) -> Dict[str, Any]:
    """
    Quiz generation agent blueprint.
    
    Expected Input:
        chapter_id: int                        # Chapter identifier
        num_questions: int                     # Number of questions (1-20)
        context: Dict[str, Any]               # RAG context
    
    Expected Output:
        {
            "questions": [
                {
                    "id": int,                 # Question ID
                    "text": str,               # Question text
                    "type": str,               # "multiple-choice", "true-false", "short-answer"
                    "options": List[str],      # Answer options (if multiple-choice)
                    "correct_answer": str,     # Correct answer
                    "explanation": str         # Answer explanation
                },
                ...
            ],
            "learning_objectives": List[str]   # Covered objectives
        }
    
    TODO: Implement quiz generation logic
    """
    pass
```

#### diagram_agent

**File**: `backend/app/ai/subagents/diagram_agent.py`

```python
async def diagram_agent(
    diagram_type: str,                          # Diagram type identifier
    concepts: List[str],                       # Concepts to include
    context: Dict[str, Any]                    # RAG context
) -> Dict[str, Any]:
    """
    Diagram generation agent blueprint.
    
    Expected Input:
        diagram_type: str                      # "robot-anatomy", "ai-robotics-stack", etc.
        concepts: List[str]                    # Concept names to include
        context: Dict[str, Any]                # RAG context
    
    Expected Output:
        {
            "diagram_url": str,                # URL or base64-encoded image
            "diagram_type": str,               # Diagram type
            "metadata": {
                "title": str,                  # Diagram title
                "description": str,           # Diagram description
                "concepts": List[str],        # Included concepts
                "format": str                 # "svg", "png", "mermaid", etc.
            }
        }
    
    TODO: Implement diagram generation logic
    """
    pass
```

---

### 7. Skill Function Signatures

#### retrieval_skill

**File**: `backend/app/ai/skills/retrieval_skill.py`

```python
async def retrieve_content(
    query: str,                                 # Search query
    chapter_id: int,                           # Chapter ID
    top_k: int = 5                             # Number of results
) -> List[Dict[str, Any]]:
    """
    Content retrieval skill blueprint.
    
    Expected Input:
        query: str                             # Search query
        chapter_id: int                        # Chapter identifier
        top_k: int                             # Number of results (default: 5)
    
    Expected Output:
        List of retrieved content chunks:
        [
            {
                "text": str,                   # Chunk text
                "chapter_id": int,            # Chapter ID
                "section_id": str,           # Section ID
                "position": int,              # Position in chapter
                "score": float                # Relevance score
            },
            ...
        ]
    
    TODO: Implement content retrieval logic
    """
    pass
```

#### formatting_skill

**File**: `backend/app/ai/skills/formatting_skill.py`

```python
def format_response(
    raw_response: Dict[str, Any],              # Raw LLM response
    block_type: str                            # AI block type
) -> Dict[str, Any]:
    """
    Response formatting skill blueprint.
    
    Expected Input:
        raw_response: {
            "text": str,                       # Raw LLM text
            "metadata": Dict[str, Any]        # LLM metadata
        }
        block_type: str                        # "ask-question", "explain-like-10", etc.
    
    Expected Output:
        Formatted response matching block_type:
        - ask-question: {answer, sources, confidence}
        - explain-like-10: {explanation, examples, analogies}
        - quiz: {questions, learning_objectives}
        - diagram: {diagram_url, metadata}
    
    TODO: Implement response formatting logic
    """
    pass
```

#### prompt_builder_skill

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

```python
def build_prompt(
    block_type: str,                            # AI block type
    user_input: str,                           # User input text
    context: List[Dict[str, Any]]              # Retrieved context chunks
) -> str:
    """
    Prompt construction skill blueprint.
    
    Expected Input:
        block_type: str                        # "ask-question", "explain-like-10", etc.
        user_input: str                        # User's question or concept
        context: [
            {
                "text": str,                   # Chunk text
                "section_id": str,            # Section identifier
                "score": float                 # Relevance score
            },
            ...
        ]
    
    Expected Output:
        Constructed prompt string for LLM:
        - System instructions based on block_type
        - Retrieved context chunks
        - User input
        - Formatting instructions
    
    TODO: Implement prompt building logic
    """
    pass
```

---

### 8. ChatKit Function Signatures

#### session_manager

**File**: `backend/app/ai/chatkit/session_manager.py`

```python
def create_session(user_id: str) -> str:
    """
    Create new chat session.
    
    Args:
        user_id: User identifier
    
    Returns:
        Session ID (unique string)
    
    TODO: Implement session creation
    """
    pass

def append_message(
    session_id: str,
    message: Dict[str, Any]
) -> bool:
    """
    Append message to session history.
    
    Args:
        session_id: Session identifier
        message: {
            "role": str,                       # "user" or "assistant"
            "content": str,                   # Message text
            "timestamp": str                   # ISO 8601 timestamp
        }
    
    Returns:
        True if successful
    
    TODO: Implement message appending
    """
    pass

def get_history(session_id: str) -> List[Dict[str, Any]]:
    """
    Retrieve session message history.
    
    Args:
        session_id: Session identifier
    
    Returns:
        List of messages in chronological order
    
    TODO: Implement history retrieval
    """
    pass
```

---

## Configuration Schemas

### Environment Variables Schema

**New Variables** (add to `.env.example` and `settings.py`):

```python
# AI Runtime Engine Configuration
AI_PROVIDER=openai                    # Options: openai, gemini, deepseek
QDRANT_COLLECTION_CH1=chapter_1_content  # Qdrant collection name
EMBEDDING_MODEL=text-embedding-3-small    # Embedding model identifier
LLM_MODEL=gpt-4o                         # LLM model identifier
```

**Settings.py Schema**:
```python
class Settings(BaseSettings):
    # ... existing settings ...
    
    # === AI Runtime Configuration ===
    ai_provider: str = "openai"              # Default: "openai"
    qdrant_collection_ch1: Optional[str] = None
    embedding_model: Optional[str] = None
    llm_model: Optional[str] = None
```

---

## Data Flow Contracts

### Request Flow: Frontend → API → Runtime → Subagent

```
Frontend Component
    │
    ▼
POST /api/ai/ask-question
    │
    ▼
AskQuestionRequest (Pydantic)
    {
        "question": str,
        "chapterId": int,
        "sectionId": str
    }
    │
    ▼
run_ai_block("ask-question", request_data)
    │
    ▼
ask_question_agent(question, context)
    │
    ├─► retrieve_content() → List[chunks]
    ├─► build_prompt() → str
    ├─► llm_provider.generate() → Dict[response]
    └─► format_response() → Dict[formatted]
    │
    ▼
AIBlockResponse (Pydantic)
    {
        "answer": str,
        "sources": List[str],
        "confidence": float
    }
```

### RAG Pipeline Data Flow

```
User Query: "What is Physical AI?"
    │
    ▼
run_rag_pipeline(query, chapter_id=1)
    │
    ├─► Step 1: get_chapter_chunks(1)
    │   └─► Returns: List[{text, section_id, position}]
    │
    ├─► Step 2: generate_embedding(query)
    │   └─► Returns: List[float] (embedding vector)
    │
    ├─► Step 3: similarity_search(collection, embedding, top_k=5)
    │   └─► Returns: List[{id, score, payload}]
    │
    ├─► Step 4: assemble_context(results)
    │   └─► Returns: str (formatted context)
    │
    └─► Step 5: llm_provider.generate(prompt, context)
        └─► Returns: Dict[response]
```

---

## Constraints & Invariants

### Invariants

1. **No Persistent Storage**: All data is ephemeral (scaffolding only)
2. **Type Safety**: All functions have type hints
3. **Placeholder Responses**: All functions return empty/mock data
4. **No Real AI Logic**: No API calls, no embeddings, no Qdrant operations
5. **Import Resolution**: All modules importable without errors

### Constraints

1. **Function Signatures**: MUST match specified type hints
2. **Return Types**: MUST match specified return structures (even if empty)
3. **Configuration**: All new settings MUST be optional
4. **Backend Startup**: MUST start successfully even if AI providers not configured
5. **API Compatibility**: MUST maintain Feature 004 endpoint compatibility

---

## Future Evolution

**Phase 2 (Not in this feature)**:
- Real embedding generation (OpenAI embeddings API)
- Real Qdrant operations (collection creation, vector upsert, search)
- Real LLM API calls (OpenAI, Gemini)
- Real subagent business logic
- Real skill implementations

**Phase 3 (Not in this feature)**:
- Database schemas (chat sessions, message history)
- Vector storage models (embeddings, documents)
- User context models (personalization data)
- Response caching models

**Note**: This scaffolding phase establishes the data contracts and function signatures. Future features will implement actual data processing and persistence on top of this foundation.

