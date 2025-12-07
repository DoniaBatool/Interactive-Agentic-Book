# Research: System Integration Layer — Phase 1

**Feature**: 044-system-integration-phase-1
**Date**: 2025-01-27
**Purpose**: Document system integration approach for unifying Chapters 1-3 runtime, RAG interfaces, providers, metadata, and runtime engine

## Overview

This document captures research findings for implementing the System Integration Layer (Phase 1). Research focuses on unified runtime routing, chapter registry patterns, provider selection, RAG unification, and dependency management.

## Technology Decisions

### 1. Unified Runtime Router

**Decision**: Create centralized runtime router that routes requests to appropriate chapter runtime

**Rationale**:
- **Scalability**: Easy to add more chapters (chapterId=4, 5, etc.)
- **Maintainability**: Single routing point for all chapters
- **Consistency**: Same routing logic for all chapters
- **Future-Proof**: Supports cross-chapter queries later

**Pattern**:
```python
# Runtime router routing
def route(chapter_id: int, block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
    if chapter_id == 1:
        # Route to Chapter 1 runtime
    elif chapter_id == 2:
        # Route to Chapter 2 runtime
    elif chapter_id == 3:
        # Route to Chapter 3 runtime
    else:
        # Handle unknown chapter
```

**Alternatives Considered**:
- **Separate Routers**: Too complex, unnecessary separation
- **Config-Based**: Adds configuration overhead, switch statement simpler
- **Dynamic Registry**: Phase 2 approach, switch statement for Phase 1

---

### 2. Chapter Runtime Registry

**Decision**: Create registry dictionary mapping chapter IDs to runtime descriptions

**Rationale**:
- **Centralized**: Single source of truth for chapter runtimes
- **Extensible**: Easy to add more chapters
- **Documentation**: Registry serves as documentation
- **Future-Proof**: Can be extended to runtime objects in Phase 2

**Pattern**:
```python
CHAPTER_RUNTIMES = {
    1: "engine for Chapter 1",
    2: "engine for Chapter 2",
    3: "engine for Chapter 3"
}
```

**Future (Phase 2)**:
```python
CHAPTER_RUNTIMES = {
    1: Chapter1Runtime(),
    2: Chapter2Runtime(),
    3: Chapter3Runtime()
}
```

---

### 3. Unified RAG Access Layer

**Decision**: Create unified RAG layer that abstracts chapter-specific RAG operations

**Rationale**:
- **Abstraction**: Hides chapter-specific RAG implementation details
- **Consistency**: Same interface for all chapters
- **Maintainability**: Single point for RAG operations
- **Future-Proof**: Supports cross-chapter RAG queries later

**Pattern**:
```python
# Unified RAG functions
def get_embeddings_for_chapter(chapter_id: int) -> List[List[float]]:
    # Route to chapter-specific embedding logic
    pass

def retrieve_context(chapter_id: int, query: str) -> Dict[str, Any]:
    # Route to chapter-specific RAG pipeline
    pass
```

**Alternatives Considered**:
- **Direct Pipeline Calls**: Too tightly coupled, harder to maintain
- **Chapter-Specific RAG Modules**: Too much duplication, unified layer better

---

### 4. Provider Factory Pattern

**Decision**: Add factory function to base_llm.py for provider selection

**Rationale**:
- **Centralized**: Single point for provider selection
- **Extensible**: Easy to add more providers
- **Consistency**: Same selection logic for all chapters
- **Configuration**: Uses settings for provider selection

**Pattern**:
```python
def get_provider(provider_name: str) -> BaseLLMProvider:
    if provider_name == "openai":
        return OpenAIProvider()
    elif provider_name == "gemini":
        return GeminiProvider()
    else:
        return DefaultProvider()
```

**Alternatives Considered**:
- **Direct Instantiation**: Too scattered, factory better
- **Config-Based**: Adds complexity, factory simpler

---

### 5. Chapter Metadata Registry

**Decision**: Create registry for chapter metadata modules

**Rationale**:
- **Centralized**: Single point for metadata access
- **Extensible**: Easy to add more chapters
- **Consistency**: Same interface for all chapters
- **Documentation**: Registry serves as documentation

**Pattern**:
```python
CHAPTER_METADATA_REGISTRY = {
    1: chapter_1.CHAPTER_METADATA,
    2: chapter_2.CHAPTER_METADATA,
    3: chapter_3.CHAPTER_METADATA
}

def get_chapter_metadata(id: int) -> Dict[str, Any]:
    return CHAPTER_METADATA_REGISTRY.get(id, {})
```

---

### 6. Frontend Runtime Client

**Decision**: Create TypeScript client for frontend-backend communication

**Rationale**:
- **Abstraction**: Hides backend API details from frontend
- **Type Safety**: TypeScript provides type safety
- **Consistency**: Same interface for all AI blocks
- **Future-Proof**: Easy to add more functions

**Pattern**:
```typescript
export async function callAIBlock(type: string, payload: any): Promise<any> {
    // TODO: Call backend API
    return Promise.resolve({});
}

export async function callChapterRuntime(id: number, data: any): Promise<any> {
    // TODO: Call backend API
    return Promise.resolve({});
}
```

---

## Component Integration Patterns

### Pattern 1: API → Router → Runtime → RAG → Provider

**Flow**:
```
API Endpoint (ai_blocks.py)
    ↓
Runtime Router (router.py)
    ↓
Runtime Engine (engine.py)
    ├─► Unified RAG (unified_rag.py)
    │   └─► RAG Pipeline (pipeline.py)
    ├─► Provider Factory (base_llm.py)
    │   └─► Provider Implementation
    └─► Chapter Subagent
```

### Pattern 2: Chapter Registry Lookup

**Flow**:
```
Request with chapterId
    ↓
Runtime Router
    ↓
Runtime Registry (registry.py)
    ↓
Chapter Runtime (engine.py)
```

### Pattern 3: Metadata Registry Lookup

**Flow**:
```
Request with chapterId
    ↓
Chapter Metadata Registry (chapters/registry.py)
    ↓
Chapter Metadata Module (chapter_X.py)
```

---

## References

- Feature 005: AI Runtime Engine (reference pattern)
- Feature 013: Chapter 2 Runtime Engine (reference pattern)
- Feature 040: Chapter 3 RAG + Runtime Integration (reference pattern)
- Feature 041: Chapter 3 Subagents + Skills (reference pattern)

---

## Summary

This research establishes:
- Unified runtime router pattern for chapter routing
- Chapter runtime registry for centralized runtime management
- Unified RAG access layer for chapter-agnostic RAG operations
- Provider factory pattern for provider selection
- Chapter metadata registry for centralized metadata access
- Frontend runtime client for frontend-backend communication

**Key Principles**:
- Centralized routing and registry patterns
- Abstraction layers for RAG and provider selection
- Placeholder-only implementation (no real logic)
- No breaking changes to existing functionality
- Ready for Phase 2 (dynamic registry, runtime objects)

