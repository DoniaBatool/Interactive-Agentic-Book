# Data Model: System Integration Layer — Phase 1

**Feature**: 044-system-integration-phase-1
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for System Integration Layer (Phase 1)

## Entity Definitions

### 1. Runtime Router (Primary Entity)

**Description**: Centralized router that routes requests to appropriate chapter runtime

**Storage**: `backend/app/ai/runtime/router.py`

**Structure**:
```python
def route(chapter_id: int, block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
    # Placeholder switch logic
    if chapter_id == 1:
        # Route to Chapter 1 runtime
    elif chapter_id == 2:
        # Route to Chapter 2 runtime
    elif chapter_id == 3:
        # Route to Chapter 3 runtime
    else:
        # Handle unknown chapter
    return {}
```

**Attributes**:
- `chapter_id`: Integer (1, 2, 3)
- `block_type`: String ("ask-question", "explain-like-10", "quiz", "diagram")
- `request_data`: Dictionary (request payload)

**Validation Rules**:
- chapter_id MUST be 1, 2, or 3
- block_type MUST be valid AI block type
- request_data MUST be dictionary

---

### 2. Runtime Registry (Sub-entity)

**Description**: Registry mapping chapter IDs to runtime descriptions

**Storage**: `backend/app/ai/runtime/registry.py`

**Structure**:
```python
CHAPTER_RUNTIMES = {
    1: "engine for Chapter 1",
    2: "engine for Chapter 2",
    3: "engine for Chapter 3"
}
```

**Attributes**:
- `chapter_id`: Integer (1, 2, 3)
- `runtime_description`: String (placeholder description)

**Validation Rules**:
- All chapters 1-3 MUST be registered
- Runtime descriptions MUST be strings (Phase 1)

---

### 3. Unified RAG Layer (Sub-entity)

**Description**: Unified RAG access layer for chapter-agnostic RAG operations

**Storage**: `backend/app/ai/rag/unified_rag.py`

**Structure**:
```python
def get_embeddings_for_chapter(chapter_id: int) -> List[List[float]]:
    # Placeholder function
    return []

def retrieve_context(chapter_id: int, query: str) -> Dict[str, Any]:
    # Placeholder function
    return {}
```

**Attributes**:
- `chapter_id`: Integer (1, 2, 3)
- `query`: String (user query)
- `embeddings`: List of embedding vectors (placeholder)
- `context`: Dictionary (retrieved context)

**Validation Rules**:
- chapter_id MUST be 1, 2, or 3
- query MUST be non-empty string
- Functions MUST return correct types (placeholder)

---

### 4. Provider Factory (Sub-entity)

**Description**: Factory function for provider selection

**Storage**: `backend/app/ai/providers/base_llm.py`

**Structure**:
```python
def get_provider(provider_name: str) -> BaseLLMProvider:
    # Placeholder factory
    return None
```

**Attributes**:
- `provider_name`: String ("openai", "gemini", "deepseek")
- `provider`: BaseLLMProvider instance (placeholder)

**Validation Rules**:
- provider_name MUST be valid provider name
- Function MUST return BaseLLMProvider or None (placeholder)

---

### 5. Chapter Metadata Registry (Sub-entity)

**Description**: Registry mapping chapter IDs to metadata modules

**Storage**: `backend/app/content/chapters/registry.py`

**Structure**:
```python
CHAPTER_METADATA_REGISTRY = {
    1: chapter_1.CHAPTER_METADATA,
    2: chapter_2.CHAPTER_METADATA,
    3: chapter_3.CHAPTER_METADATA
}

def get_chapter_metadata(id: int) -> Dict[str, Any]:
    return CHAPTER_METADATA_REGISTRY.get(id, {})
```

**Attributes**:
- `chapter_id`: Integer (1, 2, 3)
- `metadata`: Dictionary (chapter metadata)

**Validation Rules**:
- All chapters 1-3 MUST be registered
- Metadata MUST be dictionary

---

### 6. Frontend Runtime Client (Sub-entity)

**Description**: TypeScript client for frontend-backend communication

**Storage**: `frontend/src/integration/runtime-client.ts`

**Structure**:
```typescript
export async function callAIBlock(type: string, payload: any): Promise<any> {
    // Placeholder function
    return Promise.resolve({});
}

export async function callChapterRuntime(id: number, data: any): Promise<any> {
    // Placeholder function
    return Promise.resolve({});
}
```

**Attributes**:
- `type`: String (AI block type)
- `payload`: Any (request payload)
- `id`: Number (chapter ID)
- `data`: Any (request data)

**Validation Rules**:
- Functions MUST return Promise
- Functions MUST have correct signatures

---

## Relationships

- Runtime Router → Runtime Registry (1:1, router uses registry)
- Runtime Router → Runtime Engine (1:1, router calls engine)
- Runtime Engine → Unified RAG (1:1, engine uses unified RAG)
- Runtime Engine → Provider Factory (1:1, engine uses provider factory)
- Unified RAG → RAG Pipeline (1:1, unified RAG calls pipeline)
- Provider Factory → Provider Implementations (1:N, factory creates providers)
- Chapter Metadata Registry → Chapter Metadata Modules (1:N, registry maps to modules)

---

## Data Integrity Constraints

1. **Runtime Registry Completeness**:
   - All chapters 1-3 MUST be registered
   - Runtime descriptions MUST be strings (Phase 1)

2. **Chapter Metadata Registry Completeness**:
   - All chapters 1-3 MUST be registered
   - Metadata MUST be dictionaries

3. **Provider Factory Validity**:
   - Provider names MUST be valid
   - Factory MUST return BaseLLMProvider or None (placeholder)

4. **Import Resolution**:
   - All imports MUST resolve without errors
   - No circular imports allowed

---

## Summary

All structures are placeholder-only. No real routing logic, RAG operations, provider selection, or API calls. Ready for Phase 2 (dynamic registry, runtime objects).

