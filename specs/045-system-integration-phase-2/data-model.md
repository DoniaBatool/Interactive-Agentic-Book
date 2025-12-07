# Data Model: System Integration Layer — Phase 2

**Feature**: 045-system-integration-phase-2
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for real AI logic activation

## Entity Definitions

### 1. LLM Provider Response (Primary Entity)

**Description**: Response from LLM provider (OpenAI or Gemini)

**Storage**: Returned from provider.generate() method

**Structure**:
```python
{
    "text": str,              # Generated text response
    "metadata": {
        "model": str,          # Model used (e.g., "gpt-4o-mini")
        "tokens": int,         # Token count
        "finish_reason": str   # Completion reason ("stop", "length", etc.)
    }
}
```

**Attributes**:
- `text`: Generated text response
- `metadata.model`: Model identifier
- `metadata.tokens`: Token count
- `metadata.finish_reason`: Completion reason

**Validation Rules**:
- text MUST be non-empty string
- metadata MUST contain model, tokens, finish_reason

---

### 2. Embedding Vector (Sub-entity)

**Description**: Text embedding vector from OpenAI embeddings API

**Storage**: Returned from embedding_client.generate_embedding()

**Structure**:
```python
List[float]  # 1536-dimensional vector
# Example: [0.123, -0.456, 0.789, ...]
```

**Attributes**:
- `dimension`: 1536 (for text-embedding-3-small)
- `values`: List of float values (-1.0 to 1.0)

**Validation Rules**:
- Vector MUST have 1536 dimensions
- All values MUST be floats

---

### 3. Qdrant Vector Document (Sub-entity)

**Description**: Vector document stored in Qdrant

**Storage**: Stored in Qdrant collection

**Structure**:
```python
{
    "id": str,                    # Unique document ID (e.g., "ch3-s1-c0")
    "vector": List[float],        # Embedding vector (1536 dims)
    "payload": {                 # Metadata
        "text": str,              # Original text chunk
        "chapter_id": int,        # Chapter identifier
        "section_id": str,        # Section identifier
        "position": int           # Position in chapter (0-based)
    }
}
```

**Attributes**:
- `id`: Unique document identifier
- `vector`: 1536-dimensional embedding vector
- `payload.text`: Original text chunk
- `payload.chapter_id`: Chapter identifier
- `payload.section_id`: Section identifier
- `payload.position`: Position in chapter

**Validation Rules**:
- id MUST be unique
- vector MUST have 1536 dimensions
- payload MUST contain text, chapter_id, section_id, position

---

### 4. Qdrant Search Result (Sub-entity)

**Description**: Search result from Qdrant similarity search

**Storage**: Returned from qdrant_store.similarity_search()

**Structure**:
```python
{
    "id": str,                # Document ID
    "score": float,           # Similarity score (0.0-1.0)
    "payload": {              # Metadata
        "text": str,
        "chapter_id": int,
        "section_id": str,
        "position": int
    }
}
```

**Attributes**:
- `id`: Document identifier
- `score`: Similarity score (0.0-1.0, higher is better)
- `payload`: Document metadata

**Validation Rules**:
- score MUST be between 0.0 and 1.0
- payload MUST contain text, chapter_id, section_id, position

---

### 5. RAG Context (Sub-entity)

**Description**: RAG context assembled from retrieved chunks

**Storage**: Returned from run_rag_pipeline()

**Structure**:
```python
{
    "context": str,                    # Assembled context string
    "chunks": List[Dict[str, Any]],   # Retrieved chunks with metadata
    "query_embedding": List[float]    # Query embedding vector
}
```

**Attributes**:
- `context`: Assembled context string (concatenated chunks)
- `chunks`: List of retrieved chunks with metadata
- `query_embedding`: Query embedding vector

**Validation Rules**:
- context MUST be non-empty string (if chunks retrieved)
- chunks MUST be list of search results
- query_embedding MUST be 1536-dimensional vector

---

### 6. AI Block Response (Sub-entity)

**Description**: Formatted response for AI block

**Storage**: Returned from runtime engine

**Structure** (varies by block type):

**ask-question**:
```python
{
    "answer": str,                     # Generated answer
    "sources": List[str],              # Source citations (section IDs)
    "confidence": float                # Confidence score (0.0-1.0)
}
```

**explain-like-10**:
```python
{
    "explanation": str,                # Simplified explanation
    "analogies": List[str],            # List of analogies used
    "examples": List[str]              # List of real-world examples
}
```

**quiz**:
```python
{
    "quiz_title": str,                 # Title of the quiz
    "questions": List[Dict[str, Any]] # List of quiz questions
}
```

**diagram**:
```python
{
    "diagram_prompt": str,             # Diagram description/prompt
    "diagram_type": str,               # Confirmed diagram type
    "description": str                 # Textual description
}
```

---

## Relationships

- LLM Provider → LLM Response (1:1, provider generates response)
- Embedding Client → Embedding Vector (1:1, client generates vector)
- Qdrant Store → Vector Document (1:N, store contains many documents)
- Qdrant Store → Search Result (1:N, search returns many results)
- RAG Pipeline → RAG Context (1:1, pipeline generates context)
- Runtime Engine → AI Block Response (1:1, engine generates response)

---

## Data Integrity Constraints

1. **Embedding Vector Consistency**:
   - All embeddings MUST have 1536 dimensions
   - All values MUST be floats

2. **Qdrant Document Consistency**:
   - All documents MUST have unique IDs
   - All vectors MUST have 1536 dimensions
   - All payloads MUST contain required fields

3. **RAG Context Consistency**:
   - Context MUST be assembled from retrieved chunks
   - Query embedding MUST match query text

4. **AI Block Response Consistency**:
   - Response structure MUST match block type
   - Response MUST contain required fields

---

## Summary

All structures are real implementations with actual data. No placeholders—all entities represent real API responses, database documents, and formatted outputs. Ready for real AI logic activation.

