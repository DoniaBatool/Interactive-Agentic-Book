# Implementation Plan: Chapter 3 — RAG + Embedding Preparation Layer

**Branch**: `029-ch3-rag-prep` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/029-ch3-rag-prep/spec.md`

## Summary

This feature builds RAG foundations for Chapter 3 (Physical AI Perception Systems) by creating scaffolding for chunking, embeddings, Qdrant collections, and retrieval pipeline. The implementation updates Chapter 3 chunks file with placeholder CH3_CHUNKS list and TODO comments for chunking rules, adds Chapter 3 embedding functions to embedding client, adds Qdrant collection scaffolding for Chapter 3, creates separate Chapter 3 RAG pipeline file, adds RAG-CHUNK markers to Chapter 3 MDX, and adds environment variables for Chapter 3 RAG configuration. **No real RAG logic is implemented**—only scaffolding, TODO placeholders, and architectural blueprints to prepare for future RAG implementation.

**Primary Deliverable**: Complete RAG infrastructure scaffolding for Chapter 3 (chunking, embeddings, Qdrant, pipeline, MDX markers, environment variables)
**Validation**: All files exist, imports resolve, backend starts, no runtime errors, environment variables documented

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- No new runtime dependencies required (scaffolding only)
- Future: Qdrant client library, OpenAI SDK (not in this feature)

**Storage**: 
- No persistent storage (scaffolding only)
- Future: Qdrant for Chapter 3 vectors, embedding cache

**Testing**:
- Manual: File existence verification, import resolution, backend startup
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)

**Project Type**: Backend RAG infrastructure scaffolding

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real RAG logic (no API calls, no embeddings, no Qdrant operations)
- MUST maintain compatibility with Feature 028 (Chapter 3 AI blocks must still work)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality
- MUST follow Chapter 2 RAG prep patterns for consistency

**Scale/Scope**:
- 1 new backend file to create (ch3_pipeline.py)
- 4 backend files to update (chapter_3_chunks.py, embedding_client.py, qdrant_store.py, settings.py)
- 1 frontend file to update (chapter-3.mdx)
- 1 environment file to update (.env.example)
- ~150-200 lines of scaffolding code (mostly signatures, TODOs, and comments)

---

## 1. High-Level Architecture Overview

The RAG infrastructure for Chapter 3 provides the foundation for semantic search and context retrieval for Physical AI Perception Systems knowledge. It establishes the architectural patterns for chunking Chapter 3 content, generating embeddings, storing vectors in Qdrant, and retrieving relevant context for AI blocks.

### Architecture Flow

```
Chapter 3 MDX Content
    │
    ▼
Chapter 3 Chunking (chapter_3_chunks.py)
    │ (TODO: Implement chunking, respect RAG-CHUNK markers)
    ▼
Chapter 3 Chunks (List[Dict]) + CH3_CHUNKS = []
    │
    ▼
Embedding Generation (embedding_client.py)
    │ (TODO: embed_chapter3_chunks(), normalize_chapter3_embeddings())
    ▼
Embedding Vectors (List[List[float]])
    │
    ▼
Qdrant Storage (qdrant_store.py)
    │ (TODO: create_collection("chapter3"), upsert_vectors, similarity_search_ch3())
    ▼
Qdrant Collection "chapter3"
    │
    ▼
User Query
    │
    ▼
RAG Pipeline (ch3_pipeline.py)
    │ ├─► Retrieve Chapter 3 chunks
    │ ├─► Embed query
    │ ├─► Qdrant similarity search
    │ ├─► Construct retrieval context
    │ └─► Return placeholder response
    │
    ▼
Future: Runtime Engine → Subagents → LLM Provider
```

### Component Responsibilities

1. **Chapter 3 Chunking**: Segment Chapter 3 content into semantic chunks with metadata, respect RAG-CHUNK markers
2. **Embedding Client**: Convert text chunks and queries into embedding vectors for Chapter 3
3. **Qdrant Store**: Manage vector database operations for Chapter 3 (collection creation, vector upsert, similarity search)
4. **RAG Pipeline**: Orchestrate retrieval → embedding → search → context assembly for Chapter 3 (separate file)
5. **MDX RAG Markers**: Define chunk boundaries in Chapter 3 MDX content

### Data Flow

1. **Chunking**: Chapter 3 MDX content → Text chunks with metadata (respect RAG-CHUNK markers)
2. **Embedding**: Text chunks → Embedding vectors (1536 dimensions)
3. **Storage**: Embedding vectors → Qdrant collection "chapter3"
4. **Query**: User query → Embedding vector
5. **Retrieval**: Query embedding → Qdrant similarity search → Top K chunks
6. **Context Assembly**: Retrieved chunks → Context string
7. **Future Integration**: Context → Runtime engine → Subagents → LLM prompts

---

## 2. Chunking Strategy

### 2.1 Chunking Approach: Multi-Phase Placeholder Strategy with RAG Markers

**Decision**: Use placeholder logic phases (syntactic, semantic, hybrid) with TODO markers for future implementation, respect RAG-CHUNK markers from MDX

**Rationale**:
- **Flexibility**: Multiple chunking strategies can be evaluated during implementation
- **Content-Aware**: Different strategies for different content types (paragraphs, headings, code, glossary)
- **Section-Aware**: Respect section boundaries (H2 headings) for better context
- **Token-Aware**: Max token size constraints prevent context overflow
- **RAG-Marker-Aware**: Respect `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers from MDX

### 2.2 Chunking Phases (TODO)

#### Phase 1: Syntactic Chunking (TODO)
- Split by paragraph boundaries
- Split by sentence boundaries
- Preserve code blocks intact
- Handle list items appropriately

#### Phase 2: Semantic Chunking (TODO)
- Use semantic similarity to group related content
- Identify topic boundaries
- Preserve conceptual units
- Handle cross-references

#### Phase 3: Hybrid Chunking (TODO)
- Combine syntactic and semantic approaches
- Use syntactic rules for structure
- Use semantic rules for content grouping
- Balance between granularity and context

#### Phase 4: Heading-Aware Chunking (TODO)
- Always start new chunk at H2 heading
- Preserve section boundaries
- Include section metadata in chunks
- Maintain section context

#### Phase 5: RAG-Marker-Aware Chunking (TODO)
- Respect `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers
- Use markers as explicit chunk boundaries
- Complement existing `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` markers
- Markers define future chunk boundaries for RAG pipeline

#### Phase 6: Overlapping Windows (TODO)
- Add overlap between chunks for context continuity
- Overlap size: TBD (e.g., 50 tokens)
- Prevent information loss at chunk boundaries
- Improve retrieval quality

### 2.3 Chunking Rules (TODO)

**Max Token Size**: TBD (e.g., 512 tokens per chunk)
- Prevents context overflow in LLM prompts
- Ensures chunks fit in embedding model limits
- Balances granularity with context

**Min Chunk Size**: TBD (e.g., 50 tokens)
- Prevents overly small chunks
- Ensures meaningful semantic units
- Maintains retrieval quality

**Overlap Size**: TBD (e.g., 50 tokens)
- Provides context continuity
- Prevents information loss at boundaries
- Improves retrieval relevance

**Section Boundaries**: Always respect H2 headings
- Start new chunk at each H2 section
- Include section metadata (section_id, heading)
- Maintain section context in chunks

**RAG Marker Boundaries**: Respect RAG-CHUNK markers
- Use `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` as explicit boundaries
- Complement existing chunk markers
- Markers define future chunk boundaries

### 2.4 Chapter 3 Chunking Implementation (Placeholder)

**File**: `backend/app/content/chapters/chapter_3_chunks.py`

**Current State**: Placeholder function exists from Feature 028

**Updates Required**:
- Add placeholder constant `CH3_CHUNKS = []`
- Add comprehensive TODO comments for chunking rules
- Document max token size constraints
- Document semantic segmentation strategy
- Document heading-aware slicing approach
- Document RAG-CHUNK marker handling
- Document overlapping window strategy

**Function Signature** (already exists, update with CH3_CHUNKS):
```python
# Placeholder constant
CH3_CHUNKS = []  # TODO: Populate with Chapter 3 chunks

def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 3 with metadata.
    
    Chunks respect chunk markers (CHUNK: START / CHUNK: END) and RAG-CHUNK markers.
    
    TODO: Implement chunking from Chapter 3 MDX content
    TODO: Load Chapter 3 content from frontend/docs/chapters/chapter-3.mdx
    TODO: Implement chunking strategy:
        - Respect chunk markers (CHUNK: START / CHUNK: END)
        - Respect RAG-CHUNK markers (<!-- RAG-CHUNK: start --> / <!-- RAG-CHUNK: end -->)
        - Section-based logical chunks (each H2 section is a natural chunk boundary)
        - Semantic segmentation by section
        - Heading-aware slicing (respect H2 boundaries)
        - Max token size constraints (e.g., 512 tokens per chunk)
        - Overlapping window strategy (e.g., 50 tokens overlap)
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch3-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Include Physical AI-specific metadata (concepts: perception, sensors, vision, signal processing)
    TODO: Include chunk marker metadata (chunk_markers: bool flag)
    TODO: Future: Generate embeddings for each chunk using embedding model
    TODO: Future: Store embeddings in Qdrant collection "chapter3"
    TODO: Future: Include chunk metadata for semantic search
    """
    return CH3_CHUNKS  # Placeholder
```

---

## 3. Embeddings Strategy

### 3.1 Embedding Model Selection: OpenAI text-embedding-3-small

**Decision**: Use OpenAI text-embedding-3-small as default embedding model for Chapter 3 (configurable via env var)

**Rationale**:
- **Proven**: Widely used, well-documented
- **Cost-Effective**: Lower cost than text-embedding-3-large
- **Dimensions**: 1536 dimensions (good balance between quality and storage)
- **Token Limit**: 8191 tokens (sufficient for most chunks)
- **API Stability**: Stable API, good error handling
- **Consistency**: Same model as Chapter 2 for consistency

**Model Specifications**:
- **Name**: text-embedding-3-small
- **Provider**: OpenAI
- **Dimensions**: 1536
- **Max Tokens**: 8191
- **Cost**: Lower than text-embedding-3-large
- **Quality**: Good for semantic search

**Alternatives Considered**:
- **text-embedding-3-large**: Higher quality but more expensive, 3072 dimensions (more storage)
- **Gemini Embeddings**: Good alternative, but OpenAI more established
- **Local Models**: Lower cost but lower quality, requires GPU

### 3.2 Embedding Functions (Placeholder)

**File**: `backend/app/ai/embeddings/embedding_client.py`

**Current State**: Placeholder functions exist from Feature 005

**New Functions to Add**:
```python
def embed_chapter3_chunks(chunks: List[str]) -> List[List[float]]:
    """
    Generate batch embeddings for Chapter 3 chunks.
    
    Args:
        chunks: List of text chunks from Chapter 3
    
    Returns:
        List of embedding vectors (one per chunk).
        Example: [[0.123, ...], [0.456, ...], ...]
        Dimension: 1536 (for text-embedding-3-small)
    
    TODO: Implement batch embedding for Chapter 3 chunks
    TODO: Use CH3_EMBEDDING_MODEL for Chapter 3
    TODO: Use settings.ch3_embedding_model for model selection
    TODO: Use batch API endpoint for efficiency
    TODO: Handle large batches (split if needed, e.g., 100 chunks per batch)
    TODO: Add progress tracking for large batches
    TODO: Add error handling for partial failures
    TODO: Return list of 1536-dimensional vectors
    """
    return []  # Placeholder

def normalize_chapter3_embeddings(embeddings: List[List[float]]) -> List[List[float]]:
    """
    Normalize Chapter 3 embeddings (optional L2 normalization).
    
    Args:
        embeddings: List of embedding vectors from embed_chapter3_chunks()
    
    Returns:
        List of normalized embedding vectors (same structure as input)
    
    TODO: Implement normalization for Chapter 3 embeddings
    TODO: Optional L2 normalization
    TODO: Return normalized embeddings
    TODO: Handle empty embeddings list
    TODO: Add error handling for invalid embeddings
    """
    return []  # Placeholder
```

### 3.3 Batching Strategy (TODO)

**Batch Size**: TBD (e.g., 100 chunks per batch)
- Optimize API usage
- Balance between efficiency and error handling
- Handle rate limits appropriately

**Rate Limiting**: TODO
- Handle API rate limits
- Implement retry logic
- Add exponential backoff

**Error Handling**: TODO
- Retry failed batches
- Handle partial failures
- Log errors appropriately

**Progress Tracking**: TODO
- Log batch progress
- Track embedding generation time
- Monitor API usage

### 3.4 Safety Guidelines (TODO)

**Max Token Size**: 8191 tokens (text-embedding-3-small)
- Truncate text if exceeds limit
- Log warnings for truncation
- Preserve important content at beginning

**Truncation Strategy**: TODO
- Truncate from end (preserve beginning)
- Or truncate intelligently (preserve key sentences)
- Log truncation events

**Input Validation**: TODO
- Validate text is non-empty
- Validate text length
- Handle special characters

---

## 4. Qdrant Collection Design

### 4.1 Collection Architecture: Chapter-Specific Collections

**Decision**: Create separate Qdrant collection for Chapter 3 ("chapter3") with chapter-specific metadata

**Rationale**:
- **Isolation**: Each chapter has its own collection (easier management)
- **Scalability**: Can scale collections independently
- **Filtering**: Easy to filter by chapter_id
- **Metadata**: Chapter-specific metadata schema (Physical AI concepts)
- **Future-Proof**: Supports cross-chapter queries later
- **Consistency**: Follows Chapter 2 pattern

### 4.2 Collection Schema

**Collection Name**: "chapter3" (from QDRANT_COLLECTION_CH3 env var)

**Vector Configuration**:
- **Vector Size**: 1536 (from embedding model dimensions)
- **Distance Metric**: Cosine similarity (default)
- **Index**: HNSW (fast approximate nearest neighbor search)
- **HNSW Config**: TODO (m, ef_construct parameters)

**Metadata Schema**:
```python
payload = {
    "text": str,                 # Original text chunk
    "chapter_id": int,            # Chapter identifier (3)
    "section_id": str,            # Section identifier (e.g., "what-is-perception-in-physical-ai")
    "position": int,              # Position in chapter (0-based)
    "word_count": int,           # Word count
    "metadata": {
        "heading": str,           # Section heading
        "type": str,              # Content type ("paragraph", "heading", "glossary", etc.)
        "has_diagram": bool,      # Diagram placeholder flag
        "has_ai_block": bool,      # AI block flag
        "chunk_markers": bool,     # True if chunk has RAG-CHUNK markers
        "concepts": List[str]      # Physical AI concepts (e.g., ["perception", "sensors", "vision", "signal-processing"])
    }
}
```

### 4.3 Qdrant Functions (Placeholder)

**File**: `backend/app/ai/rag/qdrant_store.py`

**Current State**: Placeholder functions exist from Feature 005

**Updates Required**:
- Add placeholder comment for `create_collection("chapter3")` with TODO marker
- Add placeholder comment for Chapter 3 vector upsert with TODO marker
- Add placeholder function `similarity_search_ch3()` with TODO markers

**Function Updates**:
```python
def create_collection(collection_name: str) -> bool:
    """
    Create Qdrant collection for chapter content.
    
    TODO: For Chapter 3: collection_name = "chapter3" (from QDRANT_COLLECTION_CH3 env var)
    TODO: Configure collection with appropriate vector size (1536 for text-embedding-3-small)
    TODO: Set distance metric to Cosine similarity
    TODO: Configure HNSW index (m, ef_construct parameters)
    TODO: Add collection metadata (chapter_id, created_at, etc.)
    TODO: Handle collection already exists error
    TODO: Add error handling for connection failures
    """
    return False  # Placeholder

def upsert_vectors(
    collection_name: str,
    vectors: List[Dict[str, Any]]
) -> bool:
    """
    Insert or update vectors in Qdrant collection.
    
    TODO: For Chapter 3: collection_name = "chapter3"
    TODO: Vector structure: {id, vector (1536 dims), payload (metadata)}
    TODO: Payload metadata: {text, chapter_id: 3, section_id, position, word_count, metadata}
    TODO: Handle large batches (split if needed)
    TODO: Add error handling for upsert failures
    TODO: Add validation for vector structure
    """
    return False  # Placeholder

def similarity_search_ch3(query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """
    Perform similarity search in Chapter 3 Qdrant collection.
    
    Args:
        query: Query text (will be embedded internally)
        top_k: Number of results to return (default: 5)
    
    Returns:
        List of similar documents sorted by similarity score (highest first):
        [
            {
                "id": str,                # Document ID
                "score": float,           # Similarity score (0.0-1.0)
                "payload": {              # Metadata
                    "text": str,
                    "chapter_id": int,
                    "section_id": str,
                    "position": int,
                    "metadata": {
                        "heading": str,
                        "concepts": List[str]
                    }
                }
            },
            ...
        ]
    
    TODO: Implement similarity search for Chapter 3
    TODO: Use collection "chapter3" (from QDRANT_COLLECTION_CH3 env var)
    TODO: Embed query using generate_embedding(query, chapter_id=3)
    TODO: Perform vector search in Qdrant
    TODO: Return top-k most relevant chunks
    TODO: Add error handling for search failures
    TODO: Add result validation and filtering
    """
    return []  # Placeholder
```

---

## 5. Retrieval Pipeline Flow

### 5.1 Pipeline Architecture: 5-Step Process (Separate File)

**Decision**: Create separate pipeline file `ch3_pipeline.py` for Chapter 3 RAG operations

**Rationale**:
- **Modularity**: Separate pipeline per chapter (easier to maintain)
- **Chapter-Specific Logic**: Allows chapter-specific retrieval logic
- **Isolation**: Changes to one chapter don't affect others
- **Consistency**: Follows Chapter 2 pattern (if separate pipeline exists)

### 5.2 Pipeline Steps (Placeholder)

**File**: `backend/app/ai/rag/ch3_pipeline.py` (NEW FILE)

**Function**:
```python
from typing import Dict, Any, List

async def run_ch3_rag_pipeline(query: str, top_k: int = 5) -> Dict[str, Any]:
    """
    Execute RAG pipeline for Chapter 3: retrieve → embed → search → context → response.
    
    Args:
        query: User query text
        top_k: Number of chunks to retrieve (default: 5)
    
    Returns:
        Dictionary with structure:
        {
            "context": str,                    # Assembled context string from retrieved chunks
            "chunks": List[Dict[str, Any]],   # Retrieved chunks with metadata
            "query_embedding": List[float]    # Query embedding vector
        }
    
    Pipeline Steps (all TODO):
    1. Retrieve chunks (call get_chapter_chunks(chapter_id=3))
    2. Embed query (call generate_embedding(query, chapter_id=3))
    3. Perform search (call similarity_search_ch3(query, top_k))
    4. Construct retrieval context (assemble retrieved chunks into context string)
    5. Return placeholder response (return context dictionary)
    
    TODO: Step 1 - Retrieve Chapter 3 chunks
    TODO:     from app.content.chapters.chapter_3_chunks import get_chapter_chunks
    TODO:     chunks = get_chapter_chunks(chapter_id=3)
    TODO:     Validate chunks are available
    
    TODO: Step 2 - Embed user query
    TODO:     from app.ai.embeddings.embedding_client import generate_embedding
    TODO:     query_embedding = generate_embedding(query, chapter_id=3)
    TODO:     Validate embedding is generated
    
    TODO: Step 3 - Perform similarity search
    TODO:     from app.ai.rag.qdrant_store import similarity_search_ch3
    TODO:     results = similarity_search_ch3(query, top_k)
    TODO:     Validate results are returned
    
    TODO: Step 4 - Construct retrieval context
    TODO:     context = assemble_context_string(results)
    TODO:     Include section headers for context
    TODO:     Limit context size (max chunks from config)
    TODO:     Include chunk metadata
    
    TODO: Step 5 - Return response
    TODO:     return {
    TODO:         "context": context,
    TODO:         "chunks": results,
    TODO:         "query_embedding": query_embedding
    TODO:     }
    
    TODO: Add error handling for each step
    TODO: Add logging for pipeline execution
    TODO: Filter chunks by section_id when sectionId provided in request
    TODO: Limit context size (use configurable max chunks)
    """
    # Step 1: Retrieve chunks (TODO)
    # chunks = get_chapter_chunks(chapter_id=3)
    
    # Step 2: Embed query (TODO)
    # query_embedding = generate_embedding(query, chapter_id=3)
    
    # Step 3: Perform search (TODO)
    # results = similarity_search_ch3(query, top_k)
    
    # Step 4: Construct context (TODO)
    # context = assemble_context_string(results)
    
    # Step 5: Return response (TODO)
    # return {"context": context, "chunks": results, "query_embedding": query_embedding}
    
    return {
        "context": "",
        "chunks": [],
        "query_embedding": []
    }  # Placeholder
```

### 5.3 Context Assembly Strategy (TODO)

**Strategy**: Concatenate chunks in order of similarity score
- Highest similarity chunks first
- Include section headers for context
- Limit total context size (max chunks from config)

**Max Context**: Configurable (default: 4 chunks)
- Prevents context overflow
- Balances relevance with token limits
- Configurable per deployment

**Section Headers**: Include in context string
- Provides section context
- Improves LLM understanding
- Maintains document structure

**Metadata**: Include chunk metadata in context
- Section IDs
- Physical AI concepts (perception, sensors, vision, signal processing)
- Content type information

---

## 6. MDX RAG Markers

### 6.1 Marker Strategy: Complementary to Existing Markers

**Decision**: Add `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers to Chapter 3 MDX

**Rationale**:
- **Explicit Boundaries**: Clear chunk boundaries for RAG pipeline
- **Complementary**: Works alongside existing `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` markers
- **Flexibility**: Allows fine-grained control over chunk boundaries
- **Future-Proof**: Supports future chunking strategies

### 6.2 Marker Implementation

**File**: `frontend/docs/chapters/chapter-3.mdx`

**Current State**: Has `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` markers from Feature 028

**Updates Required**:
- Add `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers around each section
- Markers should wrap section content including AI blocks and diagrams
- Ensure markers don't interfere with existing chunk markers

**Marker Pattern**:
```mdx
<!-- RAG-CHUNK: start -->
<!-- CHUNK: START -->
## Section Title {#section-id}

<!-- Content -->

<!-- DIAGRAM: diagram-name -->

<AIBlockComponent ... />

<!-- CHUNK: END -->
<!-- RAG-CHUNK: end -->
```

**Marker Placement**:
- Wrap each H2 section with RAG-CHUNK markers
- Include all section content (text, diagrams, AI blocks)
- Complement existing CHUNK markers
- Define future chunk boundaries for RAG pipeline

---

## 7. Environment Variable Updates

### 7.1 New Environment Variables

**File**: `.env.example` (create if doesn't exist)

**Variables to Add**:
```bash
# Chapter 3 RAG Configuration
QDRANT_COLLECTION_CH3="chapter3"              # Qdrant collection name for Chapter 3
EMBEDDING_MODEL_CH3="text-embedding-3-small"   # Embedding model for Chapter 3 (OpenAI)
```

**Descriptions**:
- `QDRANT_COLLECTION_CH3`: Name of Qdrant collection for storing Chapter 3 embeddings
- `EMBEDDING_MODEL_CH3`: Embedding model to use for Chapter 3 (default: text-embedding-3-small)

### 7.2 Settings Configuration

**File**: `backend/app/config/settings.py`

**Fields to Add**:
```python
# === Chapter 3 Runtime Configuration ===
qdrant_collection_ch3: Optional[str] = None  # Qdrant collection name for Chapter 3 RAG operations
ch3_embedding_model: Optional[str] = None   # Embedding model for Chapter 3 (e.g., "text-embedding-3-small")
```

**Pattern**: Follows Chapter 2 configuration pattern

---

## 8. File Creation Diagram

### 8.1 Files to Create/Update

```
backend/
├── app/
│   ├── content/
│   │   └── chapters/
│   │       └── chapter_3_chunks.py          # UPDATE: Add CH3_CHUNKS constant and TODO comments
│   ├── ai/
│   │   ├── embeddings/
│   │   │   └── embedding_client.py          # UPDATE: Add embed_chapter3_chunks() and normalize_chapter3_embeddings()
│   │   └── rag/
│   │       ├── qdrant_store.py              # UPDATE: Add Chapter 3 TODOs and similarity_search_ch3()
│   │       └── ch3_pipeline.py              # CREATE: New file with 5-step pipeline
│   └── config/
│       └── settings.py                       # UPDATE: Add qdrant_collection_ch3 and ch3_embedding_model
frontend/
└── docs/
    └── chapters/
        └── chapter-3.mdx                     # UPDATE: Add RAG-CHUNK markers
.env.example                                   # UPDATE: Add Chapter 3 RAG env vars
```

### 8.2 File Modification Summary

1. **`backend/app/content/chapters/chapter_3_chunks.py`**
   - Update: Add `CH3_CHUNKS = []` constant
   - Update: Add comprehensive TODO comments for chunking rules (including RAG-CHUNK markers)
   - Lines: ~30-40 new TODO comments

2. **`backend/app/ai/embeddings/embedding_client.py`**
   - Create: Add `embed_chapter3_chunks()` function
   - Create: Add `normalize_chapter3_embeddings()` function
   - Lines: ~40-50 new lines (function signatures + TODOs)

3. **`backend/app/ai/rag/qdrant_store.py`**
   - Update: Add Chapter 3 TODOs to existing functions
   - Create: Add `similarity_search_ch3()` function
   - Lines: ~30-40 new lines (function signature + TODOs)

4. **`backend/app/ai/rag/ch3_pipeline.py`** (NEW FILE)
   - Create: New file with `run_ch3_rag_pipeline()` function
   - Lines: ~80-100 new lines (function signature + 5-step flow comments + TODOs)

5. **`backend/app/config/settings.py`**
   - Update: Add `qdrant_collection_ch3` and `ch3_embedding_model` fields
   - Lines: ~5 new lines

6. **`frontend/docs/chapters/chapter-3.mdx`**
   - Update: Add RAG-CHUNK markers around each section
   - Lines: ~14 new lines (7 sections × 2 markers)

7. **`.env.example`** (create if doesn't exist)
   - Update: Add 2 new environment variables
   - Lines: ~5 new lines

**Total**: ~200-250 lines of scaffolding code (mostly comments and TODOs)

---

## 9. Risks

### 9.1 Risk Assessment

#### Risk 1: No Real Logic Allowed at This Stage
**Severity**: Low
**Probability**: Low
**Mitigation**: Clear TODO comments, placeholder returns, validation checks

#### Risk 2: MDX RAG Markers Interfere with Existing Markers
**Severity**: Low
**Probability**: Low
**Mitigation**: Markers are complementary, test MDX build after changes

#### Risk 3: Backend Import Errors
**Severity**: Medium
**Probability**: Low
**Mitigation**: Validate all imports resolve, test backend startup

#### Risk 4: Pattern Inconsistency with Chapter 2
**Severity**: Low
**Probability**: Low
**Mitigation**: Follow Chapter 2 patterns exactly, review consistency

### 9.2 Mitigation Strategies

1. **Validation**: Test all imports and backend startup after each file update
2. **Pattern Consistency**: Follow Chapter 2 RAG prep patterns exactly
3. **Documentation**: Comprehensive TODO comments explain future implementation
4. **Testing**: Manual validation of file existence, imports, backend startup

---

## 10. Validation Steps

### 10.1 File Existence Validation

```bash
# Check all files exist
ls backend/app/content/chapters/chapter_3_chunks.py
ls backend/app/ai/embeddings/embedding_client.py
ls backend/app/ai/rag/qdrant_store.py
ls backend/app/ai/rag/ch3_pipeline.py
ls backend/app/config/settings.py
ls frontend/docs/chapters/chapter-3.mdx
ls .env.example
```

### 10.2 Import Resolution Validation

```bash
cd backend
python -c "from app.content.chapters.chapter_3_chunks import get_chapter_chunks, CH3_CHUNKS; print('SUCCESS')"
python -c "from app.ai.embeddings.embedding_client import embed_chapter3_chunks, normalize_chapter3_embeddings; print('SUCCESS')"
python -c "from app.ai.rag.qdrant_store import similarity_search_ch3; print('SUCCESS')"
python -c "from app.ai.rag.ch3_pipeline import run_ch3_rag_pipeline; print('SUCCESS')"
```

### 10.3 Backend Startup Validation

```bash
cd backend
python -m uvicorn app.main:app --reload
# Should start without import errors
```

### 10.4 MDX Build Validation

```bash
cd frontend
npm run build
# Should build successfully with RAG-CHUNK markers
```

### 10.5 Environment Variables Validation

```bash
# Check .env.example has new variables
grep QDRANT_COLLECTION_CH3 .env.example
grep EMBEDDING_MODEL_CH3 .env.example
```

---

## 11. Success Criteria

- ✅ Chapter 3 chunks file has CH3_CHUNKS constant and comprehensive TODO comments
- ✅ Embedding client has embed_chapter3_chunks() and normalize_chapter3_embeddings() functions
- ✅ Qdrant store has Chapter 3 TODOs and similarity_search_ch3() function
- ✅ Chapter 3 RAG pipeline file (ch3_pipeline.py) exists with 5-step flow comments
- ✅ Chapter 3 MDX contains RAG-CHUNK markers
- ✅ Settings file has qdrant_collection_ch3 and ch3_embedding_model fields
- ✅ .env.example has QDRANT_COLLECTION_CH3 and EMBEDDING_MODEL_CH3 variables
- ✅ Backend starts without import errors or runtime exceptions
- ✅ No real RAG/LLM logic implemented (only placeholders and TODOs)
- ✅ All files follow Chapter 2 RAG prep patterns for consistency

---

## 12. Next Steps

1. Run `/sp.tasks` to generate implementation tasks
2. Review tasks.md for atomic task breakdown
3. Run `/sp.implement` to implement scaffolding
4. Validate all files exist and imports resolve
5. Test backend startup and MDX build

