# Research: AI Runtime Engine for Chapter 1

**Feature**: 005-ai-runtime-engine
**Date**: 2025-12-05
**Purpose**: Document technology choices, best practices, and implementation approaches for AI runtime infrastructure scaffolding

## Overview

This document captures research findings for establishing the AI Runtime Engine architecture. Since this is a scaffolding phase with no real AI logic, research focuses on architectural patterns, provider abstraction strategies, RAG pipeline design, and subagent/skills system organization.

## Technology Decisions

### 1. LLM Provider Abstraction: Abstract Base Class Pattern

**Decision**: Use Python `abc.ABC` with `@abstractmethod` decorator for provider interface

**Rationale**:
- **Standard Python Pattern**: Well-established pattern for interface definition
- **Type Safety**: Enforces contract compliance at class definition time
- **Multiple Providers**: Supports OpenAI, Gemini, DeepSeek (future) with same interface
- **Testability**: Easy to mock providers for testing
- **Configuration-Based Selection**: Runtime provider selection via environment variables

**Implementation Pattern**:
```python
from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any

class BaseLLMProvider(ABC):
    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        messages: Optional[List[Dict[str, str]]] = None,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        pass
```

**Alternatives Considered**:
- **Protocol (typing.Protocol)**: More flexible but less explicit
- **Duck Typing**: No interface enforcement, harder to maintain
- **Factory Pattern Only**: Less clear interface definition

**Best Practices**:
- Define clear interface contract in base class
- All providers must implement all abstract methods
- Return consistent response format across providers
- Handle provider-specific differences in implementation classes

### 2. RAG Pipeline Architecture: Step-by-Step Orchestration

**Decision**: Modular RAG pipeline with separate functions for each step

**Rationale**:
- **Testability**: Each step can be tested independently
- **Maintainability**: Clear separation of concerns
- **Flexibility**: Steps can be modified or replaced without affecting others
- **Debugging**: Easy to trace issues to specific pipeline steps
- **Future Enhancement**: Steps can be optimized independently

**Pipeline Steps**:
1. **Chunk Retrieval**: Load chapter content chunks
2. **Query Embedding**: Convert user query to vector
3. **Similarity Search**: Find relevant chunks in Qdrant
4. **Context Assembly**: Combine chunks into prompt context
5. **LLM Generation**: Pass context + query to LLM

**Implementation Pattern**:
```python
async def run_rag_pipeline(query: str, chapter_id: int, top_k: int = 5) -> Dict[str, Any]:
    # Step 1: Retrieve chapter chunks
    chunks = get_chapter_chunks(chapter_id)  # TODO
    
    # Step 2: Embed user query
    query_embedding = generate_embedding(query)  # TODO
    
    # Step 3: Perform Qdrant search
    results = similarity_search(collection_name, query_embedding, top_k)  # TODO
    
    # Step 4: Construct retrieval context
    context = assemble_context(results)  # TODO
    
    # Step 5: Pass into provider LLM
    response = await llm_provider.generate(prompt=query, context=context)  # TODO
    
    return response
```

**Alternatives Considered**:
- **Monolithic Function**: Harder to test and maintain
- **Class-Based Pipeline**: More complex for simple linear flow
- **Pipeline Library**: Adds dependency, overkill for this use case

### 3. Subagent & Skills Pattern: Separation of Concerns

**Decision**: Separate subagents (specialized) from skills (reusable)

**Rationale**:
- **Reusability**: Skills can be shared across multiple subagents
- **Modularity**: Each subagent focuses on its specific task
- **Testability**: Skills and subagents can be tested independently
- **Maintainability**: Changes to skills benefit all subagents
- **Claude Code Alignment**: Matches Claude Code Subagents & Skills pattern

**Architecture**:
- **Subagents**: Specialized agents for each AI block type (ask-question, explain-el10, quiz, diagram)
- **Skills**: Reusable capabilities (retrieval, formatting, prompt building)
- **Pattern**: Subagent → Uses Skills → Calls RAG → Calls LLM → Formats Response

**Implementation Pattern**:
```python
# Subagent uses skills
async def ask_question_agent(question: str, context: Dict[str, Any]) -> Dict[str, Any]:
    # Use retrieval skill
    additional_context = await retrieve_content(question, chapter_id=1)
    
    # Use prompt builder skill
    prompt = build_prompt("ask-question", question, context + additional_context)
    
    # Call LLM (via runtime engine)
    response = await llm_provider.generate(prompt=prompt)
    
    # Use formatting skill
    formatted = format_response(response, block_type="ask-question")
    
    return formatted
```

**Alternatives Considered**:
- **Monolithic Agents**: Less reusable, harder to maintain
- **Skills Only**: No specialization, less clear responsibilities
- **Inheritance Hierarchy**: More complex, less flexible

### 4. Embedding Client: Function-Based Interface

**Decision**: Use standalone functions rather than class-based client

**Rationale**:
- **Simplicity**: Embedding operations are stateless
- **Flexibility**: Easy to swap embedding models
- **Configuration**: Model selection via settings, not class instantiation
- **Stateless Operations**: No need for client state management

**Implementation Pattern**:
```python
def generate_embedding(text: str) -> List[float]:
    """Generate embedding vector for text."""
    # TODO: Use configured embedding model
    pass

def batch_embed(chunks: List[str]) -> List[List[float]]:
    """Generate embeddings for multiple chunks."""
    # TODO: Batch processing for efficiency
    pass
```

**Alternatives Considered**:
- **Class-Based Client**: More complex for simple operations
- **Singleton Pattern**: Unnecessary for stateless operations

### 5. Qdrant Store: Function-Based Interface

**Decision**: Use standalone functions for Qdrant operations

**Rationale**:
- **Simplicity**: Operations are straightforward (create, upsert, search)
- **Stateless**: No need for persistent client connection in scaffolding
- **Future Enhancement**: Can be refactored to class-based if connection pooling needed

**Implementation Pattern**:
```python
def create_collection(collection_name: str) -> bool:
    """Create Qdrant collection."""
    # TODO: Initialize Qdrant client, create collection
    pass

def upsert_vectors(collection_name: str, vectors: List[Dict[str, Any]]) -> bool:
    """Insert or update vectors."""
    # TODO: Batch upsert with metadata
    pass

def similarity_search(collection_name: str, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """Perform similarity search."""
    # TODO: Query Qdrant, return top-K results with scores
    pass
```

### 6. Runtime Engine: Unified Entry Point

**Decision**: Single runtime engine function that routes to subagents

**Rationale**:
- **Centralized Control**: All AI block requests go through one entry point
- **Consistent Flow**: Same routing → RAG → LLM → formatting pattern
- **Easy Extension**: New block types just add new subagent
- **Configuration**: Provider selection and model config in one place

**Implementation Pattern**:
```python
async def run_ai_block(block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Unified runtime entry point.
    
    Flow:
    1. Router: Determine subagent based on block_type
    2. RAG: Run RAG pipeline to get context
    3. LLM Selection: Choose provider from config
    4. Subagent: Call appropriate subagent
    5. Formatting: Format response for frontend
    """
    # TODO: Implement routing and orchestration
    pass
```

**Alternatives Considered**:
- **Separate Endpoints per Block**: More code duplication
- **Class-Based Engine**: More complex for simple routing

### 7. ChatKit Integration: Placeholder Architecture

**Decision**: Scaffold ChatKit modules without implementation

**Rationale**:
- **Future Integration**: ChatKit API may evolve, premature implementation risky
- **Clear Structure**: Placeholder modules show where ChatKit will integrate
- **Documentation**: Tools and session management clearly documented
- **Isolation**: ChatKit code isolated in separate modules

**Implementation Pattern**:
```python
# session_manager.py - Placeholder functions
def create_session(user_id: str) -> str:
    """TODO: Create new chat session."""
    pass

# tools.py - Documentation of tools
# Tools needed: diagram_tool, quiz_tool, explanation_tool
# TODO: Implement tool definitions when ChatKit integrated
```

**Alternatives Considered**:
- **Skip ChatKit**: Would require restructuring later
- **Full Implementation**: Premature, ChatKit API not finalized

## Implementation Patterns

### Provider Factory Pattern

**Pattern**: Runtime provider selection based on configuration

```python
# In runtime/engine.py (TODO)
def get_provider() -> BaseLLMProvider:
    """Select provider based on AI_PROVIDER setting."""
    provider_name = settings.ai_provider
    if provider_name == "openai":
        return OpenAIProvider()
    elif provider_name == "gemini":
        return GeminiProvider()
    else:
        raise ValueError(f"Unknown provider: {provider_name}")
```

### Subagent Router Pattern

**Pattern**: Map block types to subagent functions

```python
# In runtime/engine.py (TODO)
SUBAGENT_MAP = {
    "ask-question": ask_question_agent,
    "explain-like-10": explain_el10_agent,
    "quiz": quiz_agent,
    "diagram": diagram_agent,
}

async def run_ai_block(block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
    subagent = SUBAGENT_MAP.get(block_type)
    if not subagent:
        raise ValueError(f"Unknown block type: {block_type}")
    return await subagent(**request_data)
```

### Skill Composition Pattern

**Pattern**: Subagents compose multiple skills

```python
# Subagent uses multiple skills
async def ask_question_agent(question: str, context: Dict[str, Any]) -> Dict[str, Any]:
    # Compose skills
    retrieved = await retrieve_content(question, chapter_id=1)
    prompt = build_prompt("ask-question", question, retrieved)
    response = await llm_provider.generate(prompt=prompt)
    formatted = format_response(response, "ask-question")
    return formatted
```

## Validation & Success Criteria

### Module Structure Validation

**Checklist**:
1. ✅ All provider files exist with abstract/base classes
2. ✅ All RAG files exist with function signatures
3. ✅ All subagent files exist with expected I/O contracts
4. ✅ All skill files exist with function signatures
5. ✅ Runtime engine exists with routing logic (placeholder)
6. ✅ ChatKit modules exist with placeholder functions

### Import Resolution Validation

**Checklist**:
1. ✅ All `__init__.py` files exist in package directories
2. ✅ All imports resolve without ImportError
3. ✅ Backend starts successfully: `uvicorn app.main:app`
4. ✅ No circular import issues

### Configuration Validation

**Checklist**:
1. ✅ `settings.py` includes all new AI configuration variables
2. ✅ `.env.example` documents all new variables
3. ✅ Backend reads configuration without errors
4. ✅ Default values work when variables not set

## Risks & Mitigations

### Risk 1: Provider API Differences

**Probability**: High (OpenAI vs Gemini have different APIs)
**Impact**: Medium (provider switching complexity)

**Mitigation**:
- Abstract base class standardizes interface
- Provider-specific logic isolated in provider classes
- Configuration-based selection allows easy switching
- Future features will handle provider-specific differences

### Risk 2: RAG Pipeline Complexity

**Probability**: Medium (RAG involves multiple steps)
**Impact**: Medium (implementation complexity)

**Mitigation**:
- Modular pipeline design (each step separate function)
- Clear TODO comments explaining each step
- Step-by-step implementation in future features
- Test each step independently

### Risk 3: Subagent/Skills Boundary Confusion

**Probability**: Medium (when to use skill vs subagent)
**Impact**: Low (refactoring possible)

**Mitigation**:
- Clear documentation: Skills = reusable, Subagents = specialized
- Examples in code comments
- Future features will refine boundaries based on usage

### Risk 4: ChatKit API Changes

**Probability**: Medium (ChatKit may evolve)
**Impact**: Low (scaffolding only, no real implementation)

**Mitigation**:
- ChatKit modules are placeholders only
- Document expected structure
- Isolate ChatKit code in separate modules
- Future features will implement based on latest API

## Next Steps (Future Features)

After this scaffolding phase is complete, future features will:

1. **Implement RAG Pipeline**: Add real chunking, embedding, Qdrant operations
2. **Implement Provider Logic**: Add OpenAI and Gemini API calls
3. **Implement Subagents**: Add real question-answering, explanation, quiz, diagram logic
4. **Implement Skills**: Add real retrieval, formatting, prompt building
5. **Implement ChatKit**: Add session management and tool integration
6. **Add Testing**: Unit tests, integration tests for all modules

## References

- Python ABC Documentation: https://docs.python.org/3/library/abc.html
- FastAPI Best Practices: https://fastapi.tiangolo.com/tutorial/bigger-applications/
- RAG Architecture Patterns: https://www.pinecone.io/learn/retrieval-augmented-generation/
- Claude Code Subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code Skills: https://code.claude.com/docs/en/skills

