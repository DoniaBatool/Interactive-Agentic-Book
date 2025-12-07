# AI Activation Schema: System Integration Layer — Phase 2

**Feature**: 045-system-integration-phase-2
**Created**: 2025-01-27
**Status**: Draft

## Overview

This contract defines the real AI logic activation schema for System Integration Layer (Phase 2). All implementations must be minimal but fully functional, with real LLM calls, embeddings, Qdrant search, and RAG pipeline operations.

---

## Provider Activation Schema

### OpenAI Provider

**File**: `backend/app/ai/providers/openai_provider.py`

**Implementation**:
```python
async def generate(
    self,
    prompt: str,
    system: Optional[str] = None,
    messages: Optional[List[Dict[str, str]]] = None,
    temperature: float = 0.7
) -> Dict[str, Any]:
    # Real OpenAI API call using openai library
    # Use settings.openai_api_key for authentication
    # Use settings.llm_model for model selection
    # Return real response with text and metadata
```

**Response Format**:
```python
{
    "text": str,              # Generated text response
    "metadata": {
        "model": str,          # Model used (e.g., "gpt-4o-mini")
        "tokens": int,         # Token count
        "finish_reason": str   # Completion reason
    }
}
```

**Error Handling**:
- Handle API failures gracefully
- Return error response or fallback
- Log errors with TODO logging

---

### Gemini Provider

**File**: `backend/app/ai/providers/gemini_provider.py`

**Implementation**:
```python
async def generate(
    self,
    prompt: str,
    system: Optional[str] = None,
    messages: Optional[List[Dict[str, str]]] = None,
    temperature: float = 0.7
) -> Dict[str, Any]:
    # Real Gemini API call using google-generativeai library
    # Use GEMINI_API_KEY for authentication
    # Use settings.llm_model for model selection
    # Return real response with text and metadata
```

**Response Format**: Same as OpenAI provider

**Error Handling**: Same as OpenAI provider

---

## Embedding Activation Schema

### generate_embedding()

**File**: `backend/app/ai/embeddings/embedding_client.py`

**Implementation**:
```python
def generate_embedding(text: str, chapter_id: int = 1) -> List[float]:
    # Real OpenAI embeddings API call
    # Use text-embedding-3-small model
    # Support chapter-specific models (CH2_EMBEDDING_MODEL, CH3_EMBEDDING_MODEL)
    # Handle max token size (8191)
    # Truncate text if exceeds max tokens
    # Return 1536-dimensional vector
```

**Input**:
- `text`: Non-empty string
- `chapter_id`: Chapter identifier (1, 2, or 3)

**Output**:
- `List[float]`: 1536-dimensional embedding vector

**Error Handling**:
- Handle API failures gracefully
- Return empty list or error
- Log errors

---

### batch_embed()

**File**: `backend/app/ai/embeddings/embedding_client.py`

**Implementation**:
```python
def batch_embed(chunks: List[str]) -> List[List[float]]:
    # Real batch embedding generation
    # Use batch API endpoint for efficiency
    # Handle large batches (split if needed, e.g., 100 chunks per batch)
    # Return list of 1536-dimensional vectors
```

**Input**:
- `chunks`: List of text strings

**Output**:
- `List[List[float]]`: List of embedding vectors (one per chunk)

**Error Handling**:
- Handle partial failures gracefully
- Return partial results if some chunks fail
- Log errors

---

## Qdrant Integration Schema

### create_collection()

**File**: `backend/app/ai/rag/qdrant_store.py`

**Implementation**:
```python
def create_collection(collection_name: str) -> bool:
    # Real Qdrant collection creation
    # Use Qdrant client SDK
    # Configure: vector_size=1536, distance_metric=Cosine
    # Configure HNSW index
    # Handle collection already exists error
    # Return True if successful, False otherwise
```

**Input**:
- `collection_name`: Collection name (e.g., "chapter_1", "chapter_2", "chapter_3")

**Output**:
- `bool`: True if successful, False otherwise

**Error Handling**:
- Handle connection failures
- Handle collection already exists
- Log errors

---

### upsert_vectors()

**File**: `backend/app/ai/rag/qdrant_store.py`

**Implementation**:
```python
def upsert_vectors(
    collection_name: str,
    vectors: List[Dict[str, Any]]
) -> bool:
    # Real Qdrant vector upsert
    # Batch upsert vectors
    # Vector structure: {id, vector (1536 dims), payload (metadata)}
    # Handle large batches (split if needed)
    # Return True if successful, False otherwise
```

**Input**:
- `collection_name`: Collection name
- `vectors`: List of vector documents with structure:
  ```python
  {
      "id": str,                    # Unique document ID
      "vector": List[float],        # Embedding vector (1536 dims)
      "payload": {                 # Metadata
          "text": str,
          "chapter_id": int,
          "section_id": str,
          "position": int
      }
  }
  ```

**Output**:
- `bool`: True if successful, False otherwise

**Error Handling**:
- Handle upsert failures
- Handle validation errors
- Log errors

---

### similarity_search()

**File**: `backend/app/ai/rag/qdrant_store.py`

**Implementation**:
```python
def similarity_search(
    collection_name: str,
    query: str,
    top_k: int = 5
) -> List[Dict[str, Any]]:
    # Real Qdrant similarity search
    # Embed query text using embedding_client.generate_embedding()
    # Perform vector search
    # Return top_k results sorted by similarity score
    # Filter by chapter_id if provided
```

**Input**:
- `collection_name`: Collection name
- `query`: Query text (will be embedded)
- `top_k`: Number of results to return (default: 5)

**Output**:
- `List[Dict[str, Any]]`: List of similar documents:
  ```python
  [
      {
          "id": str,                # Document ID
          "score": float,           # Similarity score (0.0-1.0)
          "payload": {              # Metadata
              "text": str,
              "chapter_id": int,
              "section_id": str,
              "position": int
          }
      },
      ...
  ]
  ```

**Error Handling**:
- Handle search failures
- Handle empty results
- Log errors

---

## RAG Pipeline Schema

### run_rag_pipeline()

**File**: `backend/app/ai/rag/pipeline.py`

**Implementation**:
```python
async def run_rag_pipeline(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> Dict[str, Any]:
    # Step 1: Load chapter metadata + chunks
    # Step 2: Embed user query
    # Step 3: Perform Qdrant search
    # Step 4: Build context window
    # Step 5: Prepare final prompt
    # Return context dictionary
```

**Input**:
- `query`: User query text
- `chapter_id`: Chapter identifier (1, 2, or 3)
- `top_k`: Number of chunks to retrieve (default: 5)

**Output**:
```python
{
    "context": str,                    # Assembled context string
    "chunks": List[Dict[str, Any]],   # Retrieved chunks with metadata
    "query_embedding": List[float]    # Query embedding vector
}
```

**Error Handling**:
- Handle empty context gracefully
- Handle search failures
- Log errors

---

## Runtime Engine Schema

### run_ai_block()

**File**: `backend/app/ai/runtime/engine.py`

**Implementation**:
```python
async def run_ai_block(
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    # Real flow for ask-question, explain-like-10, quiz, diagram
    # Connect to: RAG pipeline, LLM provider call, output formatters
    # Return formatted response
```

**Flow**:
1. Extract chapter_id and query from request_data
2. Call RAG pipeline to get context
3. Build prompt using prompt_builder_skill
4. Call LLM provider with prompt + context
5. Format response using formatting_skill
6. Return formatted response

**Error Handling**:
- Handle RAG failures (use empty context)
- Handle LLM failures (return error response)
- Handle formatting failures
- Log errors

---

## CLI Indexer Schema

### index_chapter()

**File**: `backend/app/cli/index_chapter.py`

**Implementation**:
```python
def index_chapter(chapter_id: int) -> None:
    # Step 1: Read chapter chunks from chapter_X_chunks.py
    # Step 2: Generate embeddings using embedding_client.batch_embed()
    # Step 3: Upsert into Qdrant using qdrant_store.upsert_vectors()
    # Step 4: Log progress and results
```

**Input**:
- `chapter_id`: Chapter identifier (1, 2, or 3)

**Output**:
- None (logs progress and results)

**Error Handling**:
- Handle empty chunks gracefully
- Handle embedding failures
- Handle upsert failures
- Log errors and progress

---

## Summary

This contract defines the complete real AI logic activation schema for System Integration Layer (Phase 2). All implementations must be minimal but fully functional, with real API calls, error handling, and logging.

