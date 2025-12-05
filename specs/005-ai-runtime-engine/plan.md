# Implementation Plan: AI Runtime Engine for Chapter 1 — LLM, RAG, ChatKit Integration

**Branch**: `005-ai-runtime-engine` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/005-ai-runtime-engine/spec.md`

## Summary

This feature creates the complete AI Runtime Engine scaffolding that powers all Chapter 1 interactive blocks. The implementation establishes the architectural foundation for LLM provider integration (OpenAI, Gemini), RAG pipeline (embeddings, Qdrant, retrieval), subagents and skills system, ChatKit integration, and unified runtime engine. **No real AI logic is implemented**—only scaffolding, function signatures, TODO placeholders, and architectural blueprints to prepare for future AI implementation.

**Primary Deliverable**: Complete AI runtime infrastructure scaffolding (17+ modules, providers, RAG pipeline, subagents, skills, ChatKit)
**Validation**: All files exist, imports resolve, backend starts, no runtime errors

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- No new runtime dependencies required (scaffolding only)

**Storage**: 
- No persistent storage (scaffolding only)
- Future: Qdrant for vectors, Postgres for sessions

**Testing**:
- Manual: File existence verification, import resolution, backend startup
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)

**Project Type**: Backend AI infrastructure scaffolding

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (no API calls, no embeddings, no Qdrant operations)
- MUST maintain compatibility with Feature 004 (ai_blocks.py endpoints must still work)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality

**Scale/Scope**:
- 17+ Python modules/files to create
- ~500-800 lines of scaffolding code (mostly signatures and TODOs)
- 4 provider files, 2 RAG files, 1 runtime engine, 4 subagents, 3 skills, 2 ChatKit files

---

## 1. High-Level Architecture Overview

The AI Runtime Engine provides a unified interface for all Chapter 1 interactive AI blocks. It orchestrates the flow from frontend API requests through RAG retrieval, LLM generation, and response formatting.

### Architecture Flow

```
Frontend Component
    │
    ▼
API Endpoint (ai_blocks.py)
    │
    ▼
Runtime Engine (engine.py)
    │
    ├─► Router: Determine block type → Select subagent
    │
    ├─► RAG Pipeline (pipeline.py)
    │   ├─► Retrieve chapter chunks (chapter_1_chunks.py)
    │   ├─► Embed user query (embedding_client.py)
    │   ├─► Qdrant similarity search (qdrant_store.py)
    │   └─► Construct retrieval context
    │
    ├─► Skills System
    │   ├─► Retrieval Skill (retrieval_skill.py)
    │   ├─► Prompt Builder Skill (prompt_builder_skill.py)
    │   └─► Formatting Skill (formatting_skill.py)
    │
    ├─► Subagent (ask_question_agent.py | explain_el10_agent.py | quiz_agent.py | diagram_agent.py)
    │   └─► Uses skills + RAG context → Generates response
    │
    ├─► LLM Provider (base_llm.py → openai_provider.py | gemini_provider.py)
    │   └─► Generates final response
    │
    └─► Response Formatting → Return to API → Frontend
```

### Component Responsibilities

1. **LLM Provider Layer**: Abstract interface for multiple AI providers (OpenAI, Gemini, DeepSeek)
2. **Embedding Client**: Text-to-vector conversion for semantic search
3. **Qdrant Store**: Vector database operations (collections, upsert, search)
4. **RAG Pipeline**: Orchestrates retrieval → embedding → search → context assembly
5. **Runtime Engine**: Unified entry point routing requests to appropriate subagents
6. **Subagents**: Specialized agents for each AI block type (question, explanation, quiz, diagram)
7. **Skills**: Reusable capabilities (retrieval, formatting, prompt building)
8. **ChatKit**: Session management and tool definitions for conversational AI

### Data Flow

1. **Request**: Frontend sends request → API endpoint receives Pydantic model
2. **Routing**: Runtime engine identifies block type → selects subagent
3. **Retrieval**: RAG pipeline retrieves relevant chapter chunks
4. **Context**: Skills assemble context + user input into prompt
5. **Generation**: LLM provider generates response
6. **Formatting**: Skills format response for frontend
7. **Response**: API returns formatted response → Frontend displays

---

## 2. Module Breakdown (Backend)

### 2.1 AI Provider Modules

#### `backend/app/ai/providers/base_llm.py`

**Purpose**: Abstract base interface for all LLM providers

**Files to Create**:
- `backend/app/ai/providers/__init__.py` (package init)
- `backend/app/ai/providers/base_llm.py`

**Primary Responsibilities**:
- Define abstract interface for LLM generation
- Standardize provider contract (prompt, system, messages, temperature)
- Return full response object structure

**Stub Functions**:
```python
class BaseLLMProvider(ABC):
    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        messages: Optional[List[Dict[str, str]]] = None,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """Generate response from LLM. TODO: Implement in subclasses."""
        pass
```

**Dependencies**:
- Internal: None (base class)
- External: `abc.ABC`, `typing` module

#### `backend/app/ai/providers/openai_provider.py`

**Purpose**: OpenAI provider implementation scaffold

**Files to Create**:
- `backend/app/ai/providers/openai_provider.py`

**Primary Responsibilities**:
- Implement BaseLLMProvider interface
- Scaffold OpenAI API integration
- Handle OpenAI-specific configuration

**Stub Functions**:
```python
class OpenAIProvider(BaseLLMProvider):
    async def generate(...) -> Dict[str, Any]:
        """TODO: Implement OpenAI API calls using openai library."""
        pass
```

**Dependencies**:
- Internal: `app.ai.providers.base_llm.BaseLLMProvider`
- External: None (scaffolding only, no openai import yet)

#### `backend/app/ai/providers/gemini_provider.py`

**Purpose**: Gemini provider implementation scaffold

**Files to Create**:
- `backend/app/ai/providers/gemini_provider.py`

**Primary Responsibilities**:
- Implement BaseLLMProvider interface
- Scaffold Gemini API integration
- Handle Gemini-specific configuration

**Stub Functions**:
```python
class GeminiProvider(BaseLLMProvider):
    async def generate(...) -> Dict[str, Any]:
        """TODO: Implement Gemini API calls using google-generativeai library."""
        pass
```

**Dependencies**:
- Internal: `app.ai.providers.base_llm.BaseLLMProvider`
- External: None (scaffolding only, no google-generativeai import yet)

---

### 2.2 Embedding Client Module

#### `backend/app/ai/embeddings/embedding_client.py`

**Purpose**: Text embedding generation for semantic search

**Files to Create**:
- `backend/app/ai/embeddings/__init__.py` (package init)
- `backend/app/ai/embeddings/embedding_client.py`

**Primary Responsibilities**:
- Generate embeddings for single text
- Batch generate embeddings for multiple chunks
- Support configurable embedding models

**Stub Functions**:
```python
def generate_embedding(text: str) -> List[float]:
    """TODO: Generate embedding vector using configured model."""
    pass

def batch_embed(chunks: List[str]) -> List[List[float]]:
    """TODO: Generate embeddings for multiple text chunks."""
    pass
```

**Dependencies**:
- Internal: `app.config.settings` (for embedding model config)
- External: None (scaffolding only)

---

### 2.3 RAG Infrastructure Modules

#### `backend/app/ai/rag/qdrant_store.py`

**Purpose**: Qdrant vector database operations

**Files to Create**:
- `backend/app/ai/rag/__init__.py` (package init)
- `backend/app/ai/rag/qdrant_store.py`

**Primary Responsibilities**:
- Create Qdrant collections
- Upsert vectors with metadata
- Perform similarity search

**Stub Functions**:
```python
def create_collection(collection_name: str) -> bool:
    """TODO: Create Qdrant collection for chapter content."""
    pass

def upsert_vectors(collection_name: str, vectors: List[Dict[str, Any]]) -> bool:
    """TODO: Insert or update vectors in Qdrant collection."""
    pass

def similarity_search(collection_name: str, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """TODO: Perform similarity search in Qdrant collection."""
    pass
```

**Dependencies**:
- Internal: `app.config.settings` (for Qdrant URL/API key)
- External: None (scaffolding only, no qdrant-client import yet)

#### `backend/app/ai/rag/pipeline.py`

**Purpose**: RAG pipeline orchestration

**Files to Create**:
- `backend/app/ai/rag/pipeline.py`

**Primary Responsibilities**:
- Orchestrate RAG pipeline steps
- Coordinate chunk retrieval, embedding, search, context assembly
- Pass context to LLM provider

**Stub Functions**:
```python
async def run_rag_pipeline(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> Dict[str, Any]:
    """
    RAG Pipeline Steps (all TODO):
    1. Retrieve chapter chunks
    2. Embed user query
    3. Perform Qdrant search
    4. Construct retrieval context
    5. Pass into provider LLM
    """
    pass
```

**Dependencies**:
- Internal: `app.ai.rag.qdrant_store`, `app.ai.embeddings.embedding_client`, `app.content.chapters.chapter_1_chunks`
- External: None (scaffolding only)

---

### 2.4 Chapter Knowledge Source

#### `backend/app/content/chapters/chapter_1_chunks.py`

**Purpose**: Chapter content chunking for RAG

**Files to Create**:
- `backend/app/content/chapters/chapter_1_chunks.py`

**Primary Responsibilities**:
- Provide chapter content chunks
- Support chunking strategies (by section, by paragraph, semantic)
- Return chunks with metadata

**Stub Functions**:
```python
def get_chapter_chunks(chapter_id: int = 1) -> List[Dict[str, Any]]:
    """TODO: Return list of text chunks from Chapter 1 with metadata."""
    pass
```

**Dependencies**:
- Internal: `app.content.chapters.chapter_1` (for metadata)
- External: None (scaffolding only)

---

### 2.5 Runtime Engine Module

#### `backend/app/ai/runtime/engine.py`

**Purpose**: Unified AI block runtime entry point

**Files to Create**:
- `backend/app/ai/runtime/__init__.py` (package init)
- `backend/app/ai/runtime/engine.py`

**Primary Responsibilities**:
- Route requests to appropriate subagents
- Coordinate RAG pipeline
- Select LLM provider based on config
- Format responses for frontend

**Stub Functions**:
```python
async def run_ai_block(
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Runtime Engine Flow (all TODO):
    1. Router: Determine which subagent to use
    2. RAG: Retrieve relevant context
    3. LLM Selection: Choose provider based on config
    4. Response Formatting: Format output for frontend
    """
    pass
```

**Dependencies**:
- Internal: `app.ai.subagents.*`, `app.ai.rag.pipeline`, `app.ai.providers.*`, `app.ai.skills.*`
- External: None (scaffolding only)

---

### 2.6 Subagent Modules

#### `backend/app/ai/subagents/ask_question_agent.py`

**Purpose**: Question-answering agent blueprint

**Files to Create**:
- `backend/app/ai/subagents/__init__.py` (package init)
- `backend/app/ai/subagents/ask_question_agent.py`

**Primary Responsibilities**:
- Process question requests
- Use retrieval skill to get context
- Use prompt builder skill to construct prompt
- Generate answer using LLM
- Use formatting skill to format response

**Stub Functions**:
```python
async def ask_question_agent(
    question: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Expected Input: question, context
    Expected Output: answer, sources
    TODO: Implement question-answering logic
    """
    pass
```

**Dependencies**:
- Internal: `app.ai.skills.retrieval_skill`, `app.ai.skills.prompt_builder_skill`, `app.ai.skills.formatting_skill`
- External: None (scaffolding only)

#### `backend/app/ai/subagents/explain_el10_agent.py`

**Purpose**: Simplified explanation agent blueprint

**Files to Create**:
- `backend/app/ai/subagents/explain_el10_agent.py`

**Stub Functions**:
```python
async def explain_el10_agent(
    concept: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Expected Input: concept, context
    Expected Output: explanation, examples
    TODO: Implement ELI10 explanation logic
    """
    pass
```

#### `backend/app/ai/subagents/quiz_agent.py`

**Purpose**: Quiz generation agent blueprint

**Files to Create**:
- `backend/app/ai/subagents/quiz_agent.py`

**Stub Functions**:
```python
async def quiz_agent(
    chapter_id: int,
    num_questions: int,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Expected Input: chapter_id, num_questions, context
    Expected Output: questions, answers, learning_objectives
    TODO: Implement quiz generation logic
    """
    pass
```

#### `backend/app/ai/subagents/diagram_agent.py`

**Purpose**: Diagram generation agent blueprint

**Files to Create**:
- `backend/app/ai/subagents/diagram_agent.py`

**Stub Functions**:
```python
async def diagram_agent(
    diagram_type: str,
    concepts: List[str],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Expected Input: diagram_type, concepts, context
    Expected Output: diagram_url, diagram_metadata
    TODO: Implement diagram generation logic
    """
    pass
```

---

### 2.7 Skill Modules

#### `backend/app/ai/skills/retrieval_skill.py`

**Purpose**: Content retrieval skill

**Files to Create**:
- `backend/app/ai/skills/__init__.py` (package init)
- `backend/app/ai/skills/retrieval_skill.py`

**Stub Functions**:
```python
async def retrieve_content(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> List[Dict[str, Any]]:
    """TODO: Implement content retrieval logic."""
    pass
```

#### `backend/app/ai/skills/formatting_skill.py`

**Purpose**: Response formatting skill

**Files to Create**:
- `backend/app/ai/skills/formatting_skill.py`

**Stub Functions**:
```python
def format_response(
    raw_response: Dict[str, Any],
    block_type: str
) -> Dict[str, Any]:
    """TODO: Implement response formatting logic."""
    pass
```

#### `backend/app/ai/skills/prompt_builder_skill.py`

**Purpose**: Prompt construction skill

**Files to Create**:
- `backend/app/ai/skills/prompt_builder_skill.py`

**Stub Functions**:
```python
def build_prompt(
    block_type: str,
    user_input: str,
    context: List[Dict[str, Any]]
) -> str:
    """TODO: Implement prompt building logic."""
    pass
```

---

### 2.8 ChatKit Modules

#### `backend/app/ai/chatkit/session_manager.py`

**Purpose**: ChatKit session management scaffold

**Files to Create**:
- `backend/app/ai/chatkit/__init__.py` (package init)
- `backend/app/ai/chatkit/session_manager.py`

**Stub Functions**:
```python
def create_session(user_id: str) -> str:
    """TODO: Create new chat session."""
    pass

def append_message(session_id: str, message: Dict[str, Any]) -> bool:
    """TODO: Append message to session history."""
    pass

def get_history(session_id: str) -> List[Dict[str, Any]]:
    """TODO: Retrieve session message history."""
    pass
```

#### `backend/app/ai/chatkit/tools.py`

**Purpose**: ChatKit tool definitions scaffold

**Files to Create**:
- `backend/app/ai/chatkit/tools.py`

**Content**: Documentation of tools needed later (diagram, quiz, explanation) with TODO placeholders

---

## 3. RAG Pipeline Architecture

### Conceptual Flow

The RAG (Retrieval-Augmented Generation) pipeline retrieves relevant chapter content to provide context for LLM generation, ensuring responses are grounded in textbook content.

**Pipeline Steps** (all placeholder in this feature):

1. **Chunk Loading** (TODO):
   - Load Chapter 1 content from `chapter_1_chunks.py`
   - Chunking strategy: by section, by paragraph, or semantic chunks
   - Each chunk includes metadata: section_id, position, word_count

2. **Embedding Generation** (TODO):
   - Embed user query using `embedding_client.generate_embedding()`
   - Use configured embedding model (e.g., text-embedding-3-small)
   - Return vector representation

3. **Qdrant Similarity Search** (TODO):
   - Query Qdrant collection with embedded query vector
   - Retrieve top-K similar chunks (default: 5)
   - Return chunks with similarity scores and metadata

4. **Retrieval Context Assembly** (TODO):
   - Combine retrieved chunks into context string
   - Include metadata (section titles, chapter references)
   - Format for LLM prompt inclusion

5. **LLM Final Answer Generation** (TODO):
   - Pass context + user query to LLM provider
   - Generate response grounded in retrieved content
   - Include source citations in response

### Architecture Notes

- **No Logic Implementation**: All steps are TODO placeholders
- **Future Integration**: Pipeline will be implemented in future features
- **Modularity**: Each step is a separate function for testability
- **Error Handling**: Placeholder functions should handle missing data gracefully

---

## 4. Provider Architecture (OpenAI + Gemini + DeepSeek Ready)

### Abstract Base Provider Contract

**File**: `backend/app/ai/providers/base_llm.py`

```python
from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any

class BaseLLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        messages: Optional[List[Dict[str, str]]] = None,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """
        Generate response from LLM.
        
        Args:
            prompt: User prompt text
            system: Optional system message
            messages: Optional conversation history
            temperature: Sampling temperature (0.0-2.0)
        
        Returns:
            Full response object with text and metadata
        """
        pass
```

### Provider Selection Flow

**Runtime Selection** (in `engine.py`):
```python
# Pseudo-flow (TODO):
# 1. Read AI_PROVIDER from settings
# 2. Instantiate appropriate provider:
#    - "openai" → OpenAIProvider()
#    - "gemini" → GeminiProvider()
#    - "deepseek" → DeepSeekProvider() (future)
# 3. Call provider.generate() with prompt + context
```

### Environment Variable Application

**Settings Integration**:
- `AI_PROVIDER` (default: "openai") → Selects provider class
- `LLM_MODEL` (e.g., "gpt-4o", "gemini-pro") → Model selection within provider
- Provider-specific API keys loaded from existing settings (OPENAI_API_KEY, etc.)

### Pseudo-Flow: System → Messages → Provider → Response

```
1. System Prompt Construction (TODO):
   - Build system prompt from block type
   - Include RAG context
   - Add personalization hints (future)

2. Messages Array (TODO):
   - Format conversation history
   - Include user query
   - Add context chunks

3. Provider Call (TODO):
   - Select provider based on AI_PROVIDER
   - Call provider.generate(prompt, system, messages, temperature)
   - Handle provider-specific response format

4. Response Processing (TODO):
   - Extract text from provider response
   - Add metadata (sources, confidence, tokens)
   - Format for frontend
```

---

## 5. Subagent & Skills System

### Architecture Overview

Subagents are specialized AI agents for each AI block type. They use reusable skills to perform their tasks.

**Pattern**: Subagent → Uses Skills → Calls RAG → Calls LLM → Formats Response

### ask_question_agent

**Purpose**: Answer questions about chapter content

**Expected I/O Contract**:
- **Input**: `question: str`, `context: Dict[str, Any]` (from RAG)
- **Output**: `{answer: str, sources: List[str], confidence: float}`

**Skills Used**:
1. **retrieval_skill**: Get additional context if needed
2. **prompt_builder_skill**: Construct question-answering prompt with context
3. **formatting_skill**: Format answer with source citations

**Flow** (TODO):
```
1. Receive question + RAG context
2. Use retrieval_skill to get more context if needed
3. Use prompt_builder_skill to build prompt
4. Call LLM provider with prompt
5. Use formatting_skill to format response with sources
6. Return formatted answer
```

### explain_el10_agent

**Purpose**: Generate simplified explanations at age-appropriate level

**Expected I/O Contract**:
- **Input**: `concept: str`, `context: Dict[str, Any]`
- **Output**: `{explanation: str, examples: List[str], analogies: List[str]}`

**Skills Used**:
1. **prompt_builder_skill**: Build ELI10 prompt with concept + context
2. **formatting_skill**: Format explanation with examples

**Flow** (TODO):
```
1. Receive concept + RAG context
2. Use prompt_builder_skill to build ELI10 prompt
3. Call LLM provider with ELI10 instructions
4. Use formatting_skill to extract examples and analogies
5. Return formatted explanation
```

### quiz_agent

**Purpose**: Generate interactive quizzes from chapter learning objectives

**Expected I/O Contract**:
- **Input**: `chapter_id: int`, `num_questions: int`, `context: Dict[str, Any]`
- **Output**: `{questions: List[Question], answers: List[str], learning_objectives: List[str]}`

**Skills Used**:
1. **retrieval_skill**: Get learning objectives from chapter metadata
2. **prompt_builder_skill**: Build quiz generation prompt
3. **formatting_skill**: Format quiz questions and answers

**Flow** (TODO):
```
1. Receive chapter_id + num_questions + RAG context
2. Use retrieval_skill to get learning objectives
3. Use prompt_builder_skill to build quiz generation prompt
4. Call LLM provider to generate questions
5. Use formatting_skill to structure quiz data
6. Return formatted quiz
```

### diagram_agent

**Purpose**: Generate visual diagrams from chapter concepts

**Expected I/O Contract**:
- **Input**: `diagram_type: str`, `concepts: List[str]`, `context: Dict[str, Any]`
- **Output**: `{diagram_url: str, diagram_type: str, metadata: Dict[str, Any]}`

**Skills Used**:
1. **prompt_builder_skill**: Build diagram generation prompt
2. **formatting_skill**: Format diagram output (URL or base64)

**Flow** (TODO):
```
1. Receive diagram_type + concepts + RAG context
2. Use prompt_builder_skill to build diagram prompt
3. Call LLM provider (or diagram generation API)
4. Use formatting_skill to format diagram output
5. Return diagram URL/metadata
```

---

## 6. ChatKit Integration Plan

### Session Manager Responsibilities

**File**: `backend/app/ai/chatkit/session_manager.py`

**Responsibilities** (all TODO):
1. **Session Creation**: Create unique session IDs for conversations
2. **Message Storage**: Append messages to session history
3. **History Retrieval**: Get conversation history for context
4. **Session Cleanup**: Handle session expiration (future)

**Placeholder Functions**:
```python
def create_session(user_id: str) -> str:
    """TODO: Create new chat session, return session_id."""
    pass

def append_message(session_id: str, message: Dict[str, Any]) -> bool:
    """TODO: Append message to session history."""
    pass

def get_history(session_id: str) -> List[Dict[str, Any]]:
    """TODO: Retrieve session message history."""
    pass
```

### Message Memory Handling

**Future Implementation** (documented, not implemented):
- Store messages in database (Neon Postgres)
- Include role (user, assistant, system)
- Include timestamps and metadata
- Support conversation threading

### Tool Definitions

**File**: `backend/app/ai/chatkit/tools.py`

**Tools Needed Later** (documented):
1. **diagram_tool**: Generate visual diagrams
   - Input: diagram_type, concepts
   - Output: diagram_url, metadata

2. **quiz_tool**: Generate interactive quizzes
   - Input: chapter_id, num_questions
   - Output: questions, answers

3. **explanation_tool**: Generate simplified explanations
   - Input: concept, age_level
   - Output: explanation, examples

**Placeholder**: TODO comments documenting tool structure for future ChatKit integration

---

## 7. API Layer Integration

### ai_blocks.py Updates

**File**: `backend/app/api/ai_blocks.py`

**Changes Required**:
1. Add import: `from app.ai.runtime.engine import run_ai_block`
2. Update all 4 endpoints to call `run_ai_block()` instead of returning placeholder

**Updated Endpoint Pattern**:
```python
@router.post("/ask-question", response_model=AIBlockResponse)
async def ask_question(request: AskQuestionRequest) -> AIBlockResponse:
    """Route to runtime engine."""
    result = await run_ai_block(
        block_type="ask-question",
        request_data=request.model_dump()
    )
    return AIBlockResponse(**result)  # TODO: Update response model
```

### Runtime Engine Dispatch Flow

**File**: `backend/app/ai/runtime/engine.py`

**Dispatch Logic** (TODO):
```python
async def run_ai_block(block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Flow (all TODO):
    1. Router: Map block_type to subagent
       - "ask-question" → ask_question_agent
       - "explain-like-10" → explain_el10_agent
       - "quiz" → quiz_agent
       - "diagram" → diagram_agent
    
    2. RAG: Run RAG pipeline to get context
       - Call run_rag_pipeline(query, chapter_id)
    
    3. Subagent: Call appropriate subagent
       - Pass request_data + RAG context
    
    4. LLM: Subagent calls LLM provider
       - Provider selected from config
       - Response generated
    
    5. Formatting: Format response for frontend
       - Use formatting_skill
       - Return structured response
    """
    pass
```

### Subagent → Skills → RAG → Provider Chain

**Example Flow** (ask_question_agent):
```
1. ask_question_agent receives question + context
2. Uses retrieval_skill to get more context if needed
3. Uses prompt_builder_skill to construct prompt
4. Calls LLM provider (via runtime engine)
5. Uses formatting_skill to format response
6. Returns formatted answer with sources
```

---

## 8. Environment & Config Plan

### Environment Variables Needed

**New Variables** (add to `backend/app/config/settings.py`):

1. **AI_PROVIDER** (default: "openai")
   - Options: "openai", "gemini", "deepseek" (future)
   - Purpose: Selects LLM provider

2. **QDRANT_COLLECTION_CH1** (optional)
   - Example: "chapter_1_content"
   - Purpose: Qdrant collection name for Chapter 1

3. **EMBEDDING_MODEL** (optional)
   - Example: "text-embedding-3-small"
   - Purpose: Embedding model identifier

4. **LLM_MODEL** (optional)
   - Example: "gpt-4o", "gemini-pro"
   - Purpose: LLM model identifier

### Settings.py Updates

**File**: `backend/app/config/settings.py`

**Add to Settings class**:
```python
class Settings(BaseSettings):
    # ... existing settings ...
    
    # === AI Runtime Configuration ===
    ai_provider: str = "openai"  # Options: "openai", "gemini", "deepseek"
    qdrant_collection_ch1: Optional[str] = None
    embedding_model: Optional[str] = None  # e.g., "text-embedding-3-small"
    llm_model: Optional[str] = None  # e.g., "gpt-4o", "gemini-pro"
```

### .env.example Updates

**Add to `.env.example`**:
```bash
# AI Runtime Engine Configuration
AI_PROVIDER=openai  # Options: openai, gemini, deepseek
QDRANT_COLLECTION_CH1=chapter_1_content  # Qdrant collection name for Chapter 1
EMBEDDING_MODEL=text-embedding-3-small  # Embedding model identifier
LLM_MODEL=gpt-4o  # LLM model identifier (e.g., gpt-4o, gemini-pro)
```

### Default Model Selections

**Defaults** (when not configured):
- `AI_PROVIDER`: "openai"
- `QDRANT_COLLECTION_CH1`: None (will be created in future feature)
- `EMBEDDING_MODEL`: None (will use provider default in future)
- `LLM_MODEL`: None (will use provider default in future)

### Settings Loading & Validation

**Validation Strategy**:
- All new settings are optional (scaffolding phase)
- Backend starts successfully even if not set
- Log warnings for missing configuration
- Future features will add validation and required checks

---

## 9. File & Folder Structure Tree

### Complete Directory Structure

```
backend/app/
├── ai/                                    # NEW: AI runtime directory
│   ├── __init__.py                        # NEW: Package init
│   ├── providers/                         # NEW: LLM provider interfaces
│   │   ├── __init__.py                   # NEW: Package init
│   │   ├── base_llm.py                   # NEW: Abstract base provider
│   │   ├── openai_provider.py            # NEW: OpenAI scaffold
│   │   └── gemini_provider.py            # NEW: Gemini scaffold
│   ├── embeddings/                        # NEW: Embedding client
│   │   ├── __init__.py                   # NEW: Package init
│   │   └── embedding_client.py           # NEW: Embedding functions
│   ├── rag/                               # NEW: RAG pipeline
│   │   ├── __init__.py                   # NEW: Package init
│   │   ├── qdrant_store.py               # NEW: Qdrant operations
│   │   └── pipeline.py                   # NEW: RAG orchestration
│   ├── runtime/                           # NEW: Runtime engine
│   │   ├── __init__.py                   # NEW: Package init
│   │   └── engine.py                     # NEW: Unified runtime entry
│   ├── subagents/                         # NEW: Specialized agents
│   │   ├── __init__.py                   # NEW: Package init
│   │   ├── ask_question_agent.py         # NEW: Question agent
│   │   ├── explain_el10_agent.py         # NEW: Explanation agent
│   │   ├── quiz_agent.py                 # NEW: Quiz agent
│   │   └── diagram_agent.py               # NEW: Diagram agent
│   ├── skills/                            # NEW: Reusable skills
│   │   ├── __init__.py                   # NEW: Package init
│   │   ├── retrieval_skill.py            # NEW: Retrieval skill
│   │   ├── formatting_skill.py           # NEW: Formatting skill
│   │   └── prompt_builder_skill.py        # NEW: Prompt building skill
│   └── chatkit/                           # NEW: ChatKit integration
│       ├── __init__.py                   # NEW: Package init
│       ├── session_manager.py            # NEW: Session management
│       └── tools.py                      # NEW: Tool definitions
├── api/
│   └── ai_blocks.py                      # MODIFIED: Route to runtime engine
├── config/
│   └── settings.py                       # MODIFIED: Add AI config vars
└── content/
    └── chapters/
        └── chapter_1_chunks.py           # NEW: Chapter chunks module

specs/005-ai-runtime-engine/
├── contracts/
│   └── content-schema.md                 # EXISTS: Schema definitions
└── checklists/
    └── requirements.md                   # EXISTS: Quality checklist
```

### File Count Summary

**New Files**: 17 Python modules + 4 __init__.py files = 21 files
**Modified Files**: 2 files (ai_blocks.py, settings.py)
**Total**: 23 file operations

---

## 10. Implementation Strategy

### Phase 1: Skeleton File Creation

**Goal**: Create all directory structures and empty files

**Tasks**:
1. Create `backend/app/ai/` directory structure
2. Create all subdirectories (providers, embeddings, rag, runtime, subagents, skills, chatkit)
3. Create all `__init__.py` files
4. Create all module files with minimal content (file header comments only)

**Validation**: All files exist at specified paths

### Phase 2: Wiring Imports + Empty Class/Function Definitions

**Goal**: Add function signatures, class definitions, type hints, docstrings

**Tasks**:
1. Add abstract base class to `base_llm.py`
2. Add provider class stubs to `openai_provider.py`, `gemini_provider.py`
3. Add function signatures to embedding_client.py
4. Add function signatures to qdrant_store.py, pipeline.py
5. Add function signature to engine.py
6. Add function signatures to all subagent files
7. Add function signatures to all skill files
8. Add function signatures to chatkit files
9. Add chapter_1_chunks.py function signature
10. Update ai_blocks.py imports and endpoint calls
11. Update settings.py with new config variables

**Validation**: All imports resolve, backend starts without errors

### Phase 3: Connecting Modules Without Business Logic

**Goal**: Wire modules together with placeholder calls, add TODO comments

**Tasks**:
1. Add TODO comments to all functions explaining future implementation
2. Add placeholder return values (empty dicts, empty lists, None)
3. Add flow comments in engine.py explaining routing logic
4. Update .env.example with new variables
5. Verify backend starts and endpoints respond (with placeholder data)

**Validation**: Backend starts, endpoints respond, no runtime errors

---

## 11. Risks & Mitigations

### Risk 1: RAG Pipeline Not Fully Implemented

**Probability**: High (scaffolding phase)
**Impact**: Medium (future features depend on RAG)

**Mitigation**:
- Clear TODO comments in pipeline.py explaining all steps
- Function signatures match expected future implementation
- Document expected input/output contracts
- Future features will implement step-by-step

### Risk 2: Model Provider Differences

**Probability**: Medium (OpenAI vs Gemini API differences)
**Impact**: Medium (provider switching complexity)

**Mitigation**:
- Abstract base provider interface standardizes contract
- Provider-specific logic isolated in provider classes
- Configuration-based provider selection
- Future features will handle provider-specific differences

### Risk 3: Missing Qdrant Connection

**Probability**: Medium (Qdrant not configured in scaffolding)
**Impact**: Low (scaffolding phase, graceful degradation)

**Mitigation**:
- Qdrant operations return empty results or mock data
- Backend starts successfully without Qdrant
- Clear error messages when Qdrant operations attempted
- Future features will add Qdrant connection handling

### Risk 4: ChatKit Future Changes

**Probability**: Medium (ChatKit API may evolve)
**Impact**: Low (scaffolding only, no real implementation)

**Mitigation**:
- ChatKit modules are placeholders only
- Document expected structure for future implementation
- Isolate ChatKit code in separate modules
- Future features will implement based on latest ChatKit API

### Risk 5: Import Resolution Failures

**Probability**: Low (careful import path management)
**Impact**: High (backend won't start)

**Mitigation**:
- Use relative imports where appropriate
- Test imports after each module creation
- Verify backend startup after each phase
- Fix import errors incrementally

### Risk 6: Breaking Feature 004 Compatibility

**Probability**: Low (careful endpoint updates)
**Impact**: High (existing endpoints must work)

**Mitigation**:
- Update ai_blocks.py incrementally
- Test endpoints after updates
- Maintain response model compatibility
- Add runtime engine call without breaking existing flow

---

## 12. Acceptance Criteria Mapping

### SC-001: All Required Files Exist

**Architectural Decision**: Complete file structure defined in Section 9
**Implementation**: Phase 1 (skeleton file creation)

### SC-002: ai_blocks.py Updated

**Architectural Decision**: API layer integration (Section 7)
**Implementation**: Phase 2 (wiring imports, Phase 3 (connecting modules)

### SC-003: settings.py Updated

**Architectural Decision**: Environment & config plan (Section 8)
**Implementation**: Phase 2 (add config variables)

### SC-004: .env.example Updated

**Architectural Decision**: Environment & config plan (Section 8)
**Implementation**: Phase 3 (add environment variables)

### SC-005: Backend Starts Successfully

**Architectural Decision**: All modules (Section 2), import resolution (Section 11)
**Implementation**: Phase 2 validation, Phase 3 final verification

### SC-006: TODO Placeholders Present

**Architectural Decision**: Implementation strategy (Section 10)
**Implementation**: Phase 3 (add TODO comments)

### SC-007: API Contract Stub Exists

**Architectural Decision**: API contract documentation (FR-016)
**Implementation**: Separate file creation (not in main implementation)

### SC-008: Type Hints and Docstrings

**Architectural Decision**: All modules (Section 2)
**Implementation**: Phase 2 (add signatures with type hints and docstrings)

### SC-009: No Real AI Logic

**Architectural Decision**: Constraints (C-001), all modules (Section 2)
**Implementation**: All phases (only placeholders, no API calls)

---

## Constitution Check

*GATE: Must pass before implementation. Re-check after Phase 1 design.*

### ✅ PASS - Principle I: AI-Native Spec-Driven Development

**Status**: COMPLIANT

- Specification created: `specs/005-ai-runtime-engine/spec.md` ✓
- Architecture planning: This plan document ✓
- SDD workflow followed: Spec → Plan → Tasks (next) → Implement ✓
- No code written without corresponding spec/plan artifacts ✓

### ✅ PASS - Principle II: Docusaurus-First Documentation Strategy

**Status**: COMPLIANT (NO FRONTEND CHANGES)

- No frontend changes in this feature ✓
- Frontend components remain unchanged from Feature 004 ✓
- Backend scaffolding supports future frontend integration ✓

### ⚠️ PARTIAL - Principle III: RAG-First Chatbot Architecture

**Status**: SCAFFOLDING PHASE (ACCEPTABLE)

- RAG pipeline architecture defined ✓
- Qdrant store interface scaffolded ✓
- Embedding client interface scaffolded ✓
- Runtime engine routes to RAG pipeline ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No actual RAG pipeline execution
  - No Qdrant operations
  - No embedding generation
  - No retrieval logic

**Justification**: This is a scaffolding feature establishing the RAG architecture foundation. Actual RAG implementation is planned for future features. All interfaces and contracts are defined to support RAG-First architecture.

### ✅ PASS - Principle IV: Personalization & User-Centric Design

**Status**: COMPLIANT (ARCHITECTURE READY)

- Runtime engine accepts user context (future) ✓
- Subagents designed to accept personalization data ✓
- Skills can be extended for personalization ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No user authentication integration
  - No personalization logic

**Justification**: Architecture supports future personalization. BetterAuth integration and personalization logic will be added in future features.

### ✅ PASS - Principle V: Multilingual Support with On-Demand Translation

**Status**: COMPLIANT (STRUCTURE READY)

- Architecture supports translation (no hard-coded language) ✓
- Skills can format responses in multiple languages ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No translation logic

**Justification**: Architecture is translation-ready. Translation will be added in future features.

### ✅ PASS - Principle VI: Test-Driven Quality Gates

**Status**: COMPLIANT (MANUAL TESTING PHASE)

- Clear acceptance criteria defined in spec.md (9 success criteria) ✓
- Manual validation methods specified (file existence, import resolution, backend startup) ✓
- **Not Yet Implemented** (automated testing out of scope for scaffolding):
  - No unit tests (scaffolding only)
  - No integration tests (no real logic to test)

**Justification**: This is a scaffolding feature with no business logic. Automated tests will be added in future features when real AI functionality is implemented (per TDD mandate).

---

### Constitution Check Summary

| Principle | Status | Notes |
|-----------|--------|-------|
| I. SDD Workflow | ✅ PASS | Full spec → plan → tasks workflow followed |
| II. Docusaurus-First | ✅ PASS | No frontend changes, backend supports frontend |
| III. RAG-First | ⚠️ SCAFFOLDING | RAG architecture defined, actual RAG in future features |
| IV. Personalization | ✅ PASS | Architecture supports future personalization |
| V. Multilingual | ✅ PASS | Structure supports translation, implementation deferred |
| VI. TDD Quality Gates | ✅ PASS | Manual validation appropriate for scaffolding phase |

**Overall**: ✅ **APPROVED TO PROCEED**

All principles are either fully compliant or in acceptable scaffolding phase. Partial compliance is justified because this is a foundational AI infrastructure scaffolding feature establishing contracts for future AI implementation.

---

## Project Structure

### Documentation (this feature)

```text
specs/005-ai-runtime-engine/
├── spec.md              # Feature specification (complete)
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output: technical decisions (TO BE CREATED)
├── data-model.md        # Phase 1 output: data structures (TO BE CREATED)
├── quickstart.md        # Phase 1 output: implementation guide (TO BE CREATED)
├── contracts/           # API contracts and schemas
│   └── content-schema.md # EXISTS: Complete schema definitions
├── checklists/          # Specification validation
│   └── requirements.md  # EXISTS: Quality checklist
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT YET CREATED)
```

### Source Code (repository root)

```text
backend/app/
├── ai/                  # NEW: Complete AI runtime infrastructure
│   ├── providers/       # LLM provider interfaces
│   ├── embeddings/      # Embedding client
│   ├── rag/            # RAG pipeline
│   ├── runtime/        # Runtime engine
│   ├── subagents/      # Specialized agents
│   ├── skills/         # Reusable skills
│   └── chatkit/        # ChatKit integration
├── api/
│   └── ai_blocks.py    # MODIFIED: Routes to runtime engine
├── config/
│   └── settings.py     # MODIFIED: AI configuration variables
└── content/
    └── chapters/
        └── chapter_1_chunks.py  # NEW: Chapter chunks module
```

---

**Plan Status**: ✅ **COMPLETE** - Ready for `/sp.tasks` phase


