# Content Schema: AI Runtime Engine for Chapter 1

**Feature**: 005-ai-runtime-engine
**Created**: 2025-12-05

## MDX Frontmatter Schema

**Note**: This feature does not modify MDX frontmatter. MDX frontmatter is managed by Feature 003 (Chapter 1 Content).

**Existing Schema** (from Feature 003):
```yaml
title: "Chapter 1 — Introduction to Physical AI & Robotics"
description: "Learn the fundamentals of Physical AI and how robots become intelligent through AI integration"
sidebar_position: 1
sidebar_label: "Chapter 1: Intro to Physical AI"
tags: ["physical-ai", "robotics", "introduction", "beginner"]
```

**Validation Rules**:
- No changes to MDX frontmatter in this feature
- Frontmatter remains managed by Feature 003

---

## Python Metadata Schema

**Format**: Python modules with type hints
**Location**: `backend/app/ai/` directory structure

### AI Provider Interface Schema

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

**Validation Rules**:
- MUST be abstract class or protocol
- MUST define interface for all LLM providers
- MUST support prompt, system, messages, temperature parameters
- MUST return full response object

### Provider Implementation Schemas

**File**: `backend/app/ai/providers/openai_provider.py`

```python
from app.ai.providers.base_llm import BaseLLMProvider

class OpenAIProvider(BaseLLMProvider):
    """OpenAI provider implementation (scaffold)."""
    
    # TODO: Implement OpenAI API integration
    # TODO: Add API key configuration
    # TODO: Add error handling
    pass
```

**File**: `backend/app/ai/providers/gemini_provider.py`

```python
from app.ai.providers.base_llm import BaseLLMProvider

class GeminiProvider(BaseLLMProvider):
    """Gemini provider implementation (scaffold)."""
    
    # TODO: Implement Gemini API integration
    # TODO: Add API key configuration
    # TODO: Add error handling
    pass
```

**Validation Rules**:
- MUST extend or implement BaseLLMProvider
- MUST contain TODO placeholders
- MUST have no real API calls

### Embedding Client Schema

**File**: `backend/app/ai/embeddings/embedding_client.py`

```python
from typing import List

def generate_embedding(text: str) -> List[float]:
    """
    Generate embedding vector for text.
    
    Args:
        text: Input text to embed
    
    Returns:
        List of float values representing embedding vector
    
    TODO: Implement embedding generation using configured model
    """
    pass

def batch_embed(chunks: List[str]) -> List[List[float]]:
    """
    Generate embeddings for multiple text chunks.
    
    Args:
        chunks: List of text chunks to embed
    
    Returns:
        List of embedding vectors
    
    TODO: Implement batch embedding generation
    """
    pass
```

**Validation Rules**:
- MUST have type hints for all parameters and return values
- MUST contain TODO placeholders
- MUST return empty list or mock data for scaffolding

### Qdrant Store Schema

**File**: `backend/app/ai/rag/qdrant_store.py`

```python
from typing import List, Dict, Any

def create_collection(collection_name: str) -> bool:
    """
    Create Qdrant collection for chapter content.
    
    Args:
        collection_name: Name of collection to create
    
    Returns:
        True if successful, False otherwise
    
    TODO: Implement Qdrant collection creation
    """
    pass

def upsert_vectors(collection_name: str, vectors: List[Dict[str, Any]]) -> bool:
    """
    Insert or update vectors in Qdrant collection.
    
    Args:
        collection_name: Name of collection
        vectors: List of vector documents with embeddings and metadata
    
    Returns:
        True if successful, False otherwise
    
    TODO: Implement vector upsert operation
    """
    pass

def similarity_search(collection_name: str, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """
    Perform similarity search in Qdrant collection.
    
    Args:
        collection_name: Name of collection to search
        query: Query text or embedding vector
        top_k: Number of results to return
    
    Returns:
        List of similar documents with scores
    
    TODO: Implement similarity search operation
    """
    pass
```

**Validation Rules**:
- MUST have type hints for all parameters and return values
- MUST contain TODO placeholders
- MUST return empty list or mock data for scaffolding

### RAG Pipeline Schema

**File**: `backend/app/ai/rag/pipeline.py`

```python
from typing import Dict, Any, List

async def run_rag_pipeline(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> Dict[str, Any]:
    """
    Execute RAG pipeline: retrieve → embed → search → context → LLM.
    
    Steps:
    1. Retrieve chapter chunks (TODO)
    2. Embed user query (TODO)
    3. Perform Qdrant search (TODO)
    4. Construct retrieval context (TODO)
    5. Pass into provider LLM (TODO)
    
    Args:
        query: User query text
        chapter_id: Chapter ID for context
        top_k: Number of chunks to retrieve
    
    Returns:
        Dictionary with retrieved context and metadata
    
    TODO: Implement all RAG pipeline steps
    """
    pass
```

**Validation Rules**:
- MUST have placeholder flow comments for all steps
- MUST have type hints
- MUST contain TODO placeholders for each step
- MUST return empty dict or mock data for scaffolding

### Runtime Engine Schema

**File**: `backend/app/ai/runtime/engine.py`

```python
from typing import Dict, Any

async def run_ai_block(
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Unified AI block runtime engine.
    
    Flow:
    1. Router: Determine which subagent to use (TODO)
    2. RAG: Retrieve relevant context (TODO)
    3. LLM Selection: Choose provider based on config (TODO)
    4. Response Formatting: Format output for frontend (TODO)
    
    Args:
        block_type: Type of AI block ("ask-question", "explain-like-10", "quiz", "diagram")
        request_data: Request payload from API endpoint
    
    Returns:
        Formatted response for frontend
    
    TODO: Implement routing, RAG, LLM selection, formatting
    """
    pass
```

**Validation Rules**:
- MUST have placeholder flow comments
- MUST accept block_type and request_data
- MUST return Dict[str, Any] format
- MUST contain TODO placeholders

### Subagent Schemas

**File**: `backend/app/ai/subagents/ask_question_agent.py`

```python
from typing import Dict, Any

async def ask_question_agent(
    question: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Question-answering agent blueprint.
    
    Expected Input:
        question: User question text
        context: Retrieved context from RAG pipeline
    
    Expected Output:
        answer: Generated answer text
        sources: List of source citations
    
    TODO: Implement question-answering logic
    """
    pass
```

**File**: `backend/app/ai/subagents/explain_el10_agent.py`

```python
from typing import Dict, Any

async def explain_el10_agent(
    concept: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Simplified explanation agent blueprint.
    
    Expected Input:
        concept: Concept name to explain
        context: Retrieved context from RAG pipeline
    
    Expected Output:
        explanation: Simplified explanation text
        examples: List of analogies or examples
    
    TODO: Implement ELI10 explanation logic
    """
    pass
```

**File**: `backend/app/ai/subagents/quiz_agent.py`

```python
from typing import Dict, Any, List

async def quiz_agent(
    chapter_id: int,
    num_questions: int,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Quiz generation agent blueprint.
    
    Expected Input:
        chapter_id: Chapter ID for quiz content
        num_questions: Number of questions to generate
        context: Retrieved context from RAG pipeline
    
    Expected Output:
        questions: List of quiz questions with answers
        learning_objectives: Covered learning objectives
    
    TODO: Implement quiz generation logic
    """
    pass
```

**File**: `backend/app/ai/subagents/diagram_agent.py`

```python
from typing import Dict, Any

async def diagram_agent(
    diagram_type: str,
    concepts: List[str],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Diagram generation agent blueprint.
    
    Expected Input:
        diagram_type: Type of diagram to generate
        concepts: List of concepts to include
        context: Retrieved context from RAG pipeline
    
    Expected Output:
        diagram_url: URL or base64-encoded diagram
        diagram_metadata: Diagram type, concepts, description
    
    TODO: Implement diagram generation logic
    """
    pass
```

**Validation Rules**:
- MUST have expected input/output signatures documented
- MUST contain TODO blueprints
- MUST have type hints
- MUST have no business logic

### Skill Schemas

**File**: `backend/app/ai/skills/retrieval_skill.py`

```python
from typing import Dict, Any, List

async def retrieve_content(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> List[Dict[str, Any]]:
    """
    Content retrieval skill blueprint.
    
    Expected Input:
        query: Search query
        chapter_id: Chapter ID for context
        top_k: Number of results
    
    Expected Output:
        List of retrieved content chunks with metadata
    
    TODO: Implement content retrieval logic
    """
    pass
```

**File**: `backend/app/ai/skills/formatting_skill.py`

```python
from typing import Dict, Any

def format_response(
    raw_response: Dict[str, Any],
    block_type: str
) -> Dict[str, Any]:
    """
    Response formatting skill blueprint.
    
    Expected Input:
        raw_response: Raw LLM response
        block_type: Type of AI block
    
    Expected Output:
        Formatted response for frontend
    
    TODO: Implement response formatting logic
    """
    pass
```

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

```python
from typing import Dict, Any, List

def build_prompt(
    block_type: str,
    user_input: str,
    context: List[Dict[str, Any]]
) -> str:
    """
    Prompt construction skill blueprint.
    
    Expected Input:
        block_type: Type of AI block
        user_input: User input text
        context: Retrieved context chunks
    
    Expected Output:
        Constructed prompt string for LLM
    
    TODO: Implement prompt building logic
    """
    pass
```

**Validation Rules**:
- MUST have expected input/output signatures
- MUST contain TODO blueprints
- MUST have type hints
- MUST have no business logic

### ChatKit Schema

**File**: `backend/app/ai/chatkit/session_manager.py`

```python
from typing import Dict, Any, List

def create_session(user_id: str) -> str:
    """
    Create new chat session.
    
    Args:
        user_id: User identifier
    
    Returns:
        Session ID
    
    TODO: Implement session creation
    """
    pass

def append_message(session_id: str, message: Dict[str, Any]) -> bool:
    """
    Append message to session history.
    
    Args:
        session_id: Session identifier
        message: Message data
    
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
        List of messages
    
    TODO: Implement history retrieval
    """
    pass
```

**File**: `backend/app/ai/chatkit/tools.py`

```python
# ChatKit Tools Documentation
# Tools needed for future ChatKit integration:

# 1. diagram_tool: Generate visual diagrams
#    - Input: diagram_type, concepts
#    - Output: diagram_url, metadata

# 2. quiz_tool: Generate interactive quizzes
#    - Input: chapter_id, num_questions
#    - Output: questions, answers

# 3. explanation_tool: Generate simplified explanations
#    - Input: concept, age_level
#    - Output: explanation, examples

# TODO: Implement tool definitions
```

**Validation Rules**:
- MUST have function signatures with type hints
- MUST contain TODO placeholders
- MUST document expected behavior

### Configuration Schema

**File**: `backend/app/config/settings.py` (updates)

```python
class Settings(BaseSettings):
    # ... existing settings ...
    
    # AI Provider Configuration
    ai_provider: str = "openai"  # Options: "openai", "gemini", "deepseek"
    
    # Qdrant Configuration
    qdrant_collection_ch1: Optional[str] = None
    
    # Model Configuration
    embedding_model: Optional[str] = None  # e.g., "text-embedding-3-small"
    llm_model: Optional[str] = None  # e.g., "gpt-4", "gemini-pro"
    
    class Config:
        env_file = ".env"
```

**Validation Rules**:
- MUST have default values or Optional types
- MUST be readable from environment variables
- MUST not break existing configuration

---

## Placeholder Contracts

### Module Import Contracts

All modules MUST be importable without errors:

```python
# Provider imports
from app.ai.providers.base_llm import BaseLLMProvider
from app.ai.providers.openai_provider import OpenAIProvider
from app.ai.providers.gemini_provider import GeminiProvider

# Embedding imports
from app.ai.embeddings.embedding_client import generate_embedding, batch_embed

# RAG imports
from app.ai.rag.qdrant_store import create_collection, upsert_vectors, similarity_search
from app.ai.rag.pipeline import run_rag_pipeline

# Runtime imports
from app.ai.runtime.engine import run_ai_block

# Subagent imports
from app.ai.subagents.ask_question_agent import ask_question_agent
from app.ai.subagents.explain_el10_agent import explain_el10_agent
from app.ai.subagents.quiz_agent import quiz_agent
from app.ai.subagents.diagram_agent import diagram_agent

# Skill imports
from app.ai.skills.retrieval_skill import retrieve_content
from app.ai.skills.formatting_skill import format_response
from app.ai.skills.prompt_builder_skill import build_prompt

# ChatKit imports
from app.ai.chatkit.session_manager import create_session, append_message, get_history
```

**Validation Rules**:
- All imports MUST resolve without ImportError
- All modules MUST exist at specified paths
- All functions MUST be defined (even if placeholder)

---

## Glossary Term Rules

**Note**: This feature does not add new glossary terms. Glossary terms are managed by Feature 003 (Chapter 1 Content).

**AI-Specific Terms** (for future reference):
- **RAG**: Retrieval-Augmented Generation - AI architecture pattern combining retrieval and generation
- **Embedding**: Vector representation of text for semantic search
- **Subagent**: Specialized AI agent for specific tasks (question-answering, explanation, etc.)
- **Skill**: Reusable AI capability (retrieval, formatting, prompt building)
- **ChatKit**: OpenAI ChatKit framework for conversational AI

**Validation Rules**:
- No new glossary terms added in this feature
- Terms documented for future reference

---

## Validation Checklist

### File Existence Validation

- [ ] All provider files exist: `base_llm.py`, `openai_provider.py`, `gemini_provider.py`
- [ ] Embedding client exists: `embedding_client.py`
- [ ] RAG files exist: `qdrant_store.py`, `pipeline.py`
- [ ] Chapter chunks file exists: `chapter_1_chunks.py`
- [ ] Runtime engine exists: `engine.py`
- [ ] All 4 subagent files exist
- [ ] All 3 skill files exist
- [ ] ChatKit files exist: `session_manager.py`, `tools.py`

### Import Resolution Validation

- [ ] All imports resolve without ImportError
- [ ] Backend starts without import errors
- [ ] All modules are importable from other modules

### TODO Placeholder Validation

- [ ] All functions contain TODO comments
- [ ] All modules have docstrings explaining purpose
- [ ] No real AI logic implemented (no API calls)

### Configuration Validation

- [ ] `settings.py` includes all new environment variables
- [ ] `.env.example` includes all new variables
- [ ] Backend reads configuration without errors

### API Integration Validation

- [ ] `ai_blocks.py` updated to call `run_ai_block()`
- [ ] All 4 endpoints route to runtime engine
- [ ] Endpoints still return responses (even if placeholder)

---

**Schema Status**: ✅ **COMPLETE** - All contracts defined for scaffolding phase

