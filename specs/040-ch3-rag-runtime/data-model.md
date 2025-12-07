# Data Model: Chapter 3 RAG + Runtime Integration

**Feature**: 040-ch3-rag-runtime
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 3 RAG + runtime integration

## Entity Definitions

### 1. Chapter 3 Chunks Source (Primary Entity)

**Description**: Represents Chapter 3 content chunks for RAG pipeline

**Storage**: `backend/app/content/chapters/chapter_3_chunks.py`

**Structure**:
```python
def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 3 with metadata.
    
    Returns:
        List of chunk dictionaries with structure:
        [
            {
                "id": str,                    # Unique chunk ID
                "text": str,                  # Chunk text content
                "chapter_id": 3,             # Chapter identifier
                "section_id": str,           # Section identifier
                "position": int,              # Position in chapter (0-based)
                "word_count": int,           # Word count
                "metadata": {                # Additional metadata
                    "heading": str,         # Section heading
                    "type": str             # "paragraph", "heading", "glossary", etc.
                }
            },
            ...
        ]
    
    TODO: Implement chunking from Chapter 3 MDX content
    """
    return []  # Placeholder return
```

**Validation Rules**:
- Function MUST exist at specified path
- Function MUST return List[Dict[str, Any]]
- Function MUST include TODO markers
- Placeholder return acceptable

---

### 2. Embedding Client Extension (Sub-entity)

**Description**: Embedding generation support for Chapter 3

**Storage**: `backend/app/ai/embeddings/embedding_client.py`

**Structure**:
```python
def generate_embedding(text: str, chapter_id: int = 1) -> List[float]:
    """
    Generate embedding vector for text.
    
    Args:
        text: Input text to embed
        chapter_id: Chapter identifier (default: 1, supports 3 for Chapter 3)
    
    Returns:
        List of float values representing embedding vector.
    
    TODO: Add chapter_id=3 support
    TODO: Use CH3_EMBEDDING_MODEL when chapter_id=3
    """
    return []  # Placeholder return
```

**Validation Rules**:
- Function MUST support chapter_id=3 parameter (placeholder)
- Function MUST include TODO markers
- Placeholder return acceptable

---

### 3. Qdrant Storage Extension (Sub-entity)

**Description**: Qdrant collection operations for Chapter 3

**Storage**: `backend/app/ai/rag/qdrant_store.py`

**Structure**:
```python
def create_collection(collection_name: str) -> bool:
    """
    Create Qdrant collection for chapter content.
    
    Args:
        collection_name: Name of collection (e.g., "chapter_3")
    
    TODO: For Chapter 3: collection_name = "chapter_3"
    """
    return False  # Placeholder return

def upsert_vectors(collection_name: str, vectors: List[Dict[str, Any]]) -> bool:
    """
    Insert or update vectors in Qdrant collection.
    
    Args:
        collection_name: Name of collection (e.g., "chapter_3")
        vectors: List of vector documents
    
    TODO: For Chapter 3: collection_name = "chapter_3"
    """
    return False  # Placeholder return
```

**Validation Rules**:
- Functions MUST support "chapter_3" collection name (placeholder)
- Functions MUST include TODO markers
- Placeholder returns acceptable

---

### 4. RAG Pipeline Extension (Sub-entity)

**Description**: RAG pipeline routing for Chapter 3

**Storage**: `backend/app/ai/rag/pipeline.py`

**Structure**:
```python
async def run_rag_pipeline(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> Dict[str, Any]:
    """
    Execute RAG pipeline: retrieve → embed → search → context → LLM.
    
    Args:
        query: User query text
        chapter_id: Chapter ID for context retrieval (supports 3 for Chapter 3)
        top_k: Number of chunks to retrieve (default: 5)
    
    TODO: Chapter 3 specific flow (when chapter_id=3):
        - Step 1: Call get_chapter_chunks(chapter_id=3)
        - Step 2: Call generate_embedding(query, chapter_id=3)
        - Step 3: Call similarity_search(collection="chapter_3", query_embedding, top_k)
        - Step 4: Assemble retrieved chunks into context string
    """
    if chapter_id == 3:
        # TODO: Chapter 3 RAG steps
        pass
    return {}  # Placeholder return
```

**Validation Rules**:
- Function MUST have chapter_id=3 branch (placeholder)
- Function MUST include TODO markers
- Placeholder return acceptable

---

### 5. Runtime Engine Extension (Sub-entity)

**Description**: Runtime engine routing for Chapter 3

**Storage**: `backend/app/ai/runtime/engine.py`

**Structure**:
```python
async def run_ai_block(
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Unified AI block runtime entry point.
    
    Args:
        block_type: Type of AI block
        request_data: Request payload (may include chapterId=3)
    
    TODO: Chapter 3 routing
    if request_data.get("chapterId") == 3:
        # TODO: Route to Chapter 3 RAG pipeline
        # TODO: Call Chapter 3 subagents
        pass
    """
    return {}  # Placeholder return
```

**Validation Rules**:
- Function MUST have chapterId=3 routing (placeholder)
- Function MUST include TODO markers
- Placeholder return acceptable

---

## Relationships

- Chapter 3 Chunks → Embedding Client (1:N, chunks embedded)
- Embedding Client → Qdrant Storage (1:1, embeddings stored)
- Qdrant Storage → RAG Pipeline (1:1, collection searched)
- RAG Pipeline → Runtime Engine (1:1, context passed)
- Runtime Engine → API Layer (1:1, responses returned)

---

## Data Integrity Constraints

1. **Chapter ID Consistency**:
   - All Chapter 3 operations MUST use chapter_id=3 or chapterId=3
   - Collection name MUST be "chapter_3"
   - Config variables MUST use CH3_ prefix

2. **Placeholder Completeness**:
   - All functions MUST have TODO markers
   - All functions MUST return placeholder values
   - No real logic implemented

3. **Import Resolution**:
   - All imports MUST resolve correctly
   - chapter_3_chunks MUST be importable
   - No missing module errors

---

## Summary

All structures are placeholder-only. No real RAG logic, embeddings, or Qdrant operations. Backend architecture ready for future AI logic implementation.

