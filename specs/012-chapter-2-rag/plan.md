# Implementation Plan: Chapter 2 — RAG Chunking, Embeddings & Qdrant Collection Setup

**Branch**: `012-chapter-2-rag` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/012-chapter-2-rag/spec.md`

## Summary

This feature builds RAG foundations for Chapter 2 (ROS 2 Fundamentals) by creating scaffolding for chunking, embeddings, Qdrant collections, and retrieval pipeline. The implementation updates Chapter 2 chunks file with TODO comments for chunking rules, verifies embedding client placeholders, adds Qdrant collection scaffolding for Chapter 2, extends RAG pipeline with Chapter 2 flow comments, updates runtime engine with RAG integration notes, and adds environment variables for Chapter 2 RAG configuration. **No real RAG logic is implemented**—only scaffolding, TODO placeholders, and architectural blueprints to prepare for future RAG implementation.

**Primary Deliverable**: Complete RAG infrastructure scaffolding for Chapter 2 (chunking, embeddings, Qdrant, pipeline, runtime integration)
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
- Future: Qdrant for Chapter 2 vectors, embedding cache

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
- MUST maintain compatibility with Feature 011 (Chapter 2 AI blocks must still work)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality

**Scale/Scope**:
- 5 backend files to update (chapter_2_chunks.py, embedding_client.py, qdrant_store.py, pipeline.py, engine.py)
- 1 environment file to update (.env.example)
- ~100-200 lines of scaffolding code (mostly signatures, TODOs, and comments)

---

## 1. High-Level Architecture Overview

The RAG infrastructure for Chapter 2 provides the foundation for semantic search and context retrieval for ROS 2 knowledge. It establishes the architectural patterns for chunking Chapter 2 content, generating embeddings, storing vectors in Qdrant, and retrieving relevant context for AI blocks.

### Architecture Flow

```
Chapter 2 MDX Content
    │
    ▼
Chapter 2 Chunking (chapter_2_chunks.py)
    │ (TODO: Implement chunking)
    ▼
Chapter 2 Chunks (List[Dict])
    │
    ▼
Embedding Generation (embedding_client.py)
    │ (TODO: Generate embeddings)
    ▼
Embedding Vectors (List[List[float]])
    │
    ▼
Qdrant Storage (qdrant_store.py)
    │ (TODO: Upsert vectors)
    ▼
Qdrant Collection "chapter_2"
    │
    ▼
User Query
    │
    ▼
RAG Pipeline (pipeline.py)
    │ ├─► Load Chapter 2 chunks
    │ ├─► Embed query
    │ ├─► Qdrant similarity search
    │ ├─► Build retrieval context
    │ └─► Return context
    │
    ▼
Runtime Engine (engine.py)
    │ (TODO: Pass context to subagents)
    ▼
Subagents → LLM Provider
```

### Component Responsibilities

1. **Chapter 2 Chunking**: Segment Chapter 2 content into semantic chunks with metadata
2. **Embedding Client**: Convert text chunks and queries into embedding vectors
3. **Qdrant Store**: Manage vector database operations (collection creation, vector upsert, similarity search)
4. **RAG Pipeline**: Orchestrate retrieval → embedding → search → context assembly for Chapter 2
5. **Runtime Engine**: Integrate RAG context into AI block processing flow

### Data Flow

1. **Chunking**: Chapter 2 MDX content → Text chunks with metadata
2. **Embedding**: Text chunks → Embedding vectors (1536 dimensions)
3. **Storage**: Embedding vectors → Qdrant collection "chapter_2"
4. **Query**: User query → Embedding vector
5. **Retrieval**: Query embedding → Qdrant similarity search → Top K chunks
6. **Context Assembly**: Retrieved chunks → Context string
7. **Integration**: Context → Runtime engine → Subagents → LLM prompts

---

## 2. Chunking Strategy

### 2.1 Chunking Approach: Multi-Phase Placeholder Strategy

**Decision**: Use placeholder logic phases (syntactic, semantic, hybrid) with TODO markers for future implementation

**Rationale**:
- **Flexibility**: Multiple chunking strategies can be evaluated during implementation
- **Content-Aware**: Different strategies for different content types (paragraphs, headings, code, glossary)
- **Section-Aware**: Respect section boundaries (H2 headings) for better context
- **Token-Aware**: Max token size constraints prevent context overflow

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

#### Phase 5: Overlapping Windows (TODO)
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

### 2.4 Chapter 2 Chunking Implementation (Placeholder)

**File**: `backend/app/content/chapters/chapter_2_chunks.py`

**Current State**: Placeholder function exists from Feature 011

**Updates Required**:
- Add comprehensive TODO comments for chunking rules
- Document max token size constraints
- Document semantic segmentation strategy
- Document heading-aware slicing approach
- Document overlapping window strategy

**Function Signature** (already exists):
```python
def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    TODO: Implement chunking from Chapter 2 MDX content
    TODO: Load Chapter 2 content from frontend/docs/chapters/chapter-2.mdx
    TODO: Implement chunking strategy:
        - Max token size constraints (e.g., 512 tokens per chunk)
        - Semantic segmentation by section
        - Heading-aware slicing (respect H2 boundaries)
        - Overlapping window strategy (e.g., 50 tokens overlap)
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch2-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Cache chunks for performance
    TODO: Include ROS 2-specific metadata (concepts: nodes, topics, services, actions)
    """
    return []  # Placeholder
```

---

## 3. Embeddings Strategy

### 3.1 Embedding Model Selection: OpenAI text-embedding-3-small

**Decision**: Use OpenAI text-embedding-3-small as default embedding model (configurable via env var)

**Rationale**:
- **Proven**: Widely used, well-documented
- **Cost-Effective**: Lower cost than text-embedding-3-large
- **Dimensions**: 1536 dimensions (good balance between quality and storage)
- **Token Limit**: 8191 tokens (sufficient for most chunks)
- **API Stability**: Stable API, good error handling

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

**Functions** (already exist, verify and add TODOs):
```python
def generate_embedding(text: str) -> List[float]:
    """
    TODO: Implement embedding generation using configured embedding model
    TODO: Use settings.embedding_model for model selection (default: "text-embedding-3-small")
    TODO: Use OpenAI embeddings API or other embedding service
    TODO: Handle max token size (8191 for text-embedding-3-small)
    TODO: Truncate text if exceeds max tokens
    TODO: Add error handling for API failures
    TODO: Add caching for frequently embedded texts
    TODO: Return 1536-dimensional vector for text-embedding-3-small
    """
    return []  # Placeholder

def batch_embed(chunks: List[str]) -> List[List[float]]:
    """
    TODO: Implement batch embedding generation
    TODO: Use batch API endpoint for efficiency
    TODO: Handle large batches (split if needed, e.g., 100 chunks per batch)
    TODO: Add progress tracking for large batches
    TODO: Add error handling for partial failures
    TODO: Return list of 1536-dimensional vectors
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

**Decision**: Create separate Qdrant collection for Chapter 2 ("chapter_2") with chapter-specific metadata

**Rationale**:
- **Isolation**: Each chapter has its own collection (easier management)
- **Scalability**: Can scale collections independently
- **Filtering**: Easy to filter by chapter_id
- **Metadata**: Chapter-specific metadata schema
- **Future-Proof**: Supports cross-chapter queries later

### 4.2 Collection Schema

**Collection Name**: "chapter_2" (from QDRANT_COLLECTION_CH2 env var)

**Vector Configuration**:
- **Vector Size**: 1536 (from embedding model dimensions)
- **Distance Metric**: Cosine similarity (default)
- **Index**: HNSW (fast approximate nearest neighbor search)
- **HNSW Config**: TODO (m, ef_construct parameters)

**Metadata Schema**:
```python
payload = {
    "text": str,                 # Original text chunk
    "chapter_id": int,            # Chapter identifier (2)
    "section_id": str,            # Section identifier (e.g., "introduction-to-ros2")
    "position": int,              # Position in chapter (0-based)
    "word_count": int,           # Word count
    "metadata": {
        "heading": str,           # Section heading
        "type": str,              # Content type ("paragraph", "heading", "glossary", etc.)
        "has_diagram": bool,      # Diagram placeholder flag
        "has_ai_block": bool,      # AI block flag
        "ros2_concepts": List[str],  # ROS 2 concepts in chunk
        "difficulty": str         # Difficulty level
    }
}
```

### 4.3 Qdrant Functions (Placeholder)

**File**: `backend/app/ai/rag/qdrant_store.py`

**Current State**: Placeholder functions exist from Feature 005

**Functions** (already exist, verify and add Chapter 2 TODOs):
```python
def create_collection(collection_name: str) -> bool:
    """
    TODO: Create Qdrant collection for chapter content
    TODO: Use settings.qdrant_url and settings.qdrant_api_key for connection
    TODO: Configure collection with appropriate vector size (1536 for text-embedding-3-small)
    TODO: Set distance metric to Cosine similarity
    TODO: Configure HNSW index (m, ef_construct parameters)
    TODO: Add collection metadata (chapter_id, created_at, etc.)
    TODO: Handle collection already exists error
    TODO: Add error handling for connection failures
    TODO: For Chapter 2: collection_name = "chapter_2" (from QDRANT_COLLECTION_CH2 env var)
    """
    return False  # Placeholder

def upsert_vectors(
    collection_name: str,
    vectors: List[Dict[str, Any]]
) -> bool:
    """
    TODO: Insert or update vectors in Qdrant collection
    TODO: Use Qdrant client to batch upsert vectors
    TODO: Handle large batches (split if needed)
    TODO: Add error handling for upsert failures
    TODO: Add validation for vector structure
    TODO: For Chapter 2: collection_name = "chapter_2"
    TODO: Vector structure: {id, vector (1536 dims), payload (metadata)}
    """
    return False  # Placeholder

def similarity_search(
    collection_name: str,
    query: str,
    top_k: int = 5
) -> List[Dict[str, Any]]:
    """
    TODO: Perform similarity search in Qdrant collection
    TODO: Embed query text using embedding_client.generate_embedding()
    TODO: Use Qdrant client to perform vector search
    TODO: Filter by chapter_id if provided
    TODO: Add error handling for search failures
    TODO: Add result validation and filtering
    TODO: For Chapter 2: collection_name = "chapter_2"
    TODO: Return top_k results sorted by similarity score
    """
    return []  # Placeholder
```

---

## 5. Retrieval Pipeline Flow

### 5.1 Pipeline Architecture: 5-Step Process

**Decision**: Use 5-step retrieval pipeline with placeholder flow for Chapter 2

**Rationale**:
- **Clear Separation**: Each step has distinct responsibility
- **Testable**: Each step can be tested independently
- **Extensible**: Easy to add new steps or modify existing ones
- **Error Handling**: Errors can be isolated to specific steps

### 5.2 Pipeline Steps (Placeholder)

**File**: `backend/app/ai/rag/pipeline.py`

**Current State**: Placeholder function exists from Feature 005

**Function** (update with Chapter 2 flow comments):
```python
async def run_rag_pipeline(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> Dict[str, Any]:
    """
    Execute RAG pipeline: retrieve → embed → search → context → LLM.
    
    Pipeline Steps (all TODO):
    1. Load chunks (call get_chapter_chunks(chapter_id))
    2. Embed query (call generate_embedding(query))
    3. Perform search (call similarity_search(collection, query_embedding, top_k))
    4. Build context (assemble retrieved chunks into context string)
    5. Return context (pass context to runtime engine)
    
    TODO: Chapter 2 specific flow (when chapter_id=2):
        - Step 1: Call get_chapter_chunks(chapter_id=2) to retrieve Chapter 2 chunks
        - Step 2: Call generate_embedding(query) to embed user query
        - Step 3: Call similarity_search(collection="chapter_2", query_embedding, top_k) to find relevant chunks
        - Step 4: Assemble retrieved chunks into context string with metadata
        - Step 5: Return context to runtime engine for LLM prompts
    
    TODO: Add error handling for each step
    TODO: Add logging for pipeline execution
    TODO: Filter chunks by section_id when sectionId provided in request
    TODO: Limit context size (use RAG_MAX_CONTEXT env var, default: 4 chunks)
    """
    # Step 1: Load chunks (TODO)
    # if chapter_id == 2:
    #     from app.content.chapters.chapter_2_chunks import get_chapter_chunks
    #     chunks = get_chapter_chunks(chapter_id=2)
    
    # Step 2: Embed query (TODO)
    # query_embedding = generate_embedding(query)
    
    # Step 3: Perform search (TODO)
    # if chapter_id == 2:
    #     results = similarity_search(collection_name="chapter_2", query_embedding, top_k)
    
    # Step 4: Build context (TODO)
    # context = assemble_context(results, max_chunks=RAG_MAX_CONTEXT)
    
    # Step 5: Return context (TODO)
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
- Limit total context size (max chunks from RAG_MAX_CONTEXT)

**Max Context**: Configurable (default: 4 chunks from RAG_MAX_CONTEXT env var)
- Prevents context overflow
- Balances relevance with token limits
- Configurable per deployment

**Section Headers**: Include in context string
- Provides section context
- Improves LLM understanding
- Maintains document structure

**Metadata**: Include chunk metadata in context
- Section IDs
- ROS 2 concepts
- Content type information

---

## 6. Runtime Engine Connection

### 6.1 Integration Pattern: Context Flow to Subagents

**Decision**: RAG pipeline returns context to runtime engine, which passes to subagents

**Rationale**:
- **Separation of Concerns**: RAG handles retrieval, runtime handles routing
- **Reusability**: Same RAG pipeline works for all AI blocks
- **Flexibility**: Subagents can use context differently
- **Testability**: Each component can be tested independently

### 6.2 Runtime Engine Updates

**File**: `backend/app/ai/runtime/engine.py`

**Current State**: Chapter 2 knowledge source mapping exists from Feature 011

**Updates Required**:
- Add placeholder comments explaining how RAG results feed into provider LLM
- Document context flow from RAG pipeline to subagents
- Add TODO comments for Chapter 2 RAG integration

**Existing Mapping** (from Feature 011):
```python
knowledge_sources = {
    1: "chapter_1_chunks",  # Existing
    2: "chapter_2_chunks",  # NEW for Chapter 2
}
```

**Additional Comments to Add**:
```python
# TODO: Chapter 2 (ROS 2) RAG Integration
# When chapterId=2:
#   1. Import get_chapter_chunks from app.content.chapters.chapter_2_chunks
#   2. Call get_chapter_chunks(chapter_id=2) to retrieve Chapter 2 chunks
#   3. Use chunks for RAG retrieval (semantic search in Qdrant)
#   4. Filter chunks by section_id when sectionId provided in request
#   5. Pass Chapter 2 context (chunks + metadata) to subagents
#   6. Subagents will use ROS 2-specific context for LLM prompts:
#      - ROS 2 concepts: nodes, topics, services, actions, packages, launch-files
#      - ROS 2 analogies: post office, restaurant, phone calls, package delivery
#      - ROS 2 examples: TurtleBot 3, navigation stack, robot arm control
#
# RAG Pipeline Integration Flow:
#   1. Runtime engine calls run_rag_pipeline(query, chapter_id=2, top_k=5)
#   2. RAG pipeline returns context: {context: str, chunks: List, query_embedding: List}
#   3. Runtime engine passes context to subagent along with request_data
#   4. Subagent uses context in LLM prompt for generating response
#   5. LLM provider generates response with ROS 2 context
```

---

## 7. Environment Variable Updates

### 7.1 New Environment Variables

**File**: `.env.example`

**Variables to Add**:
```bash
# Chapter 2 RAG Configuration
QDRANT_COLLECTION_CH2="chapter_2"           # Qdrant collection name for Chapter 2
EMBEDDING_MODEL="text-embedding-3-small"     # Embedding model name (OpenAI)
RAG_MAX_CONTEXT=4                            # Maximum number of chunks in context
```

**Descriptions**:
- `QDRANT_COLLECTION_CH2`: Name of Qdrant collection for storing Chapter 2 embeddings
- `EMBEDDING_MODEL`: Embedding model to use (default: text-embedding-3-small)
- `RAG_MAX_CONTEXT`: Maximum number of chunks to include in retrieval context

---

## 8. File Creation Diagram

### 8.1 Files to Update

```
backend/
├── app/
│   ├── content/
│   │   └── chapters/
│   │       └── chapter_2_chunks.py          # UPDATE: Add chunking TODO comments
│   ├── ai/
│   │   ├── embeddings/
│   │   │   └── embedding_client.py         # VERIFY: Add Chapter 2 TODOs
│   │   ├── rag/
│   │   │   ├── qdrant_store.py              # VERIFY: Add Chapter 2 TODOs
│   │   │   └── pipeline.py                  # UPDATE: Add Chapter 2 flow comments
│   │   └── runtime/
│   │       └── engine.py                    # UPDATE: Add RAG integration comments
│   └── config/
│       └── settings.py                       # VERIFY: No changes needed (env vars read automatically)
.env.example                                   # UPDATE: Add Chapter 2 RAG env vars
```

### 8.2 File Modification Summary

1. **`backend/app/content/chapters/chapter_2_chunks.py`**
   - Update: Add comprehensive TODO comments for chunking rules
   - Lines: ~20-30 new TODO comments

2. **`backend/app/ai/embeddings/embedding_client.py`**
   - Verify: Functions exist with TODOs
   - Update: Add Chapter 2-specific TODO comments if needed

3. **`backend/app/ai/rag/qdrant_store.py`**
   - Verify: Functions exist with TODOs
   - Update: Add Chapter 2 collection-specific TODO comments

4. **`backend/app/ai/rag/pipeline.py`**
   - Update: Add Chapter 2 flow comments in `run_rag_pipeline()`
   - Lines: ~15-20 new comments

5. **`backend/app/ai/runtime/engine.py`**
   - Update: Add RAG integration comments (already has Chapter 2 mapping)
   - Lines: ~10-15 new comments

6. **`.env.example`**
   - Update: Add 3 new environment variables
   - Lines: ~5 new lines

**Total**: ~50-80 lines of scaffolding code (mostly comments and TODOs)

---

## 9. Risks

### 9.1 Risk Assessment

#### Risk 1: No Real Logic Allowed at This Stage
**Severity**: Low
**Probability**: Low
**Impact**: Medium

**Description**: This is a scaffolding-only feature. No real RAG logic should be implemented.

**Mitigation**:
- Clear TODO markers in all functions
- Placeholder returns (empty lists, empty dicts, False)
- Comprehensive comments explaining future implementation
- Code review to ensure no real API calls

#### Risk 2: Token Length Mismatch Later
**Severity**: Medium
**Probability**: Medium
**Impact**: Medium

**Description**: Chunking rules (max token size) may need adjustment when real implementation happens.

**Mitigation**:
- Document chunking rules clearly in TODO comments
- Make max token size configurable (document in env vars)
- Include safety guidelines in embedding client TODOs
- Plan for iterative refinement during implementation

#### Risk 3: Chunk Size Variations Between Chapters
**Severity**: Low
**Probability**: Medium
**Impact**: Low

**Description**: Chapter 1 and Chapter 2 may have different optimal chunk sizes.

**Mitigation**:
- Document chunking strategy per chapter in TODO comments
- Make chunking rules configurable per chapter
- Include chapter-specific metadata in chunks
- Plan for chapter-specific chunking strategies

#### Risk 4: Environment Variable Configuration Errors
**Severity**: Low
**Probability**: Low
**Impact**: Low

**Description**: Missing or incorrect environment variables may cause issues.

**Mitigation**:
- Document all env vars in `.env.example` with descriptions
- Add validation in settings.py (future feature)
- Provide clear error messages for missing vars
- Document default values

#### Risk 5: Import Errors After Updates
**Severity**: Low
**Probability**: Low
**Impact**: Medium

**Description**: Adding TODOs and comments should not break imports.

**Mitigation**:
- Verify all imports after updates
- Test backend startup after each file update
- Maintain existing function signatures
- No syntax errors in new comments

---

## 10. Acceptance Criteria Mapping

### 10.1 Success Criteria

- ✅ All Chapter 2 RAG scaffolding files exist
- ✅ No embeddings or Qdrant logic implemented (TODO only)
- ✅ Runtime engine recognizes chapterId=2 retrieval request
- ✅ Backend starts successfully

### 10.2 Validation Steps

1. **File Existence**:
   - Verify all 5 backend files updated
   - Verify `.env.example` updated

2. **Import Validation**:
   - All imports resolve without errors
   - Backend starts successfully

3. **TODO Validation**:
   - All functions have TODO comments
   - No real API calls or logic implemented

4. **Environment Variables**:
   - `.env.example` has 3 new variables
   - Variables are documented with descriptions

---

## 11. Dependencies & Risks

### 11.1 Dependencies

- **Feature 005** (AI Runtime Engine): Provides embedding_client.py, qdrant_store.py, pipeline.py
- **Feature 011** (Chapter 2 AI Blocks): Provides chapter_2_chunks.py placeholder, runtime engine mapping

### 11.2 Blocking Dependencies

- None (all dependencies already exist)

### 11.3 Future Dependencies

- Qdrant client library (future feature)
- OpenAI SDK (future feature)
- Real chunking implementation (future feature)

---

## 12. Next Steps

1. Run `/sp.tasks` to generate implementation tasks
2. Review tasks.md for atomic task breakdown
3. Run `/sp.implement` to implement scaffolding
4. Validate all files updated correctly
5. Test backend startup and imports

---

**Status**: Plan complete, ready for `/sp.tasks`
