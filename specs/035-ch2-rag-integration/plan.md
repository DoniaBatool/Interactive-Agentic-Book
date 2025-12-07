# Implementation Plan: Chapter 2 — RAG + Embeddings + AI Runtime Integration

**Branch**: `035-ch2-rag-integration` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/035-ch2-rag-integration/spec.md`

## Summary

This feature implements the full RAG + embedding + runtime integration layer for Chapter 2 (Mechanical Systems) by creating scaffolding for embeddings, Qdrant storage, retrieval pipeline, and connecting AI blocks to the runtime engine. The implementation creates placeholder embedding client, Qdrant store, RAG pipeline module, updates runtime engine routing, verifies subagents exist, and adds environment variables. **No real RAG logic is implemented**—only scaffolding, TODO placeholders, and architectural blueprints to prepare for future RAG implementation.

**Primary Deliverable**: Complete RAG infrastructure scaffolding for Chapter 2 (embeddings, Qdrant, pipeline, runtime integration, environment variables)
**Validation**: All files exist, imports resolve, backend starts, no runtime errors, environment variables documented

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- No new runtime dependencies required (scaffolding only)
- Future: Qdrant client library, OpenAI SDK (not in this feature)
- Feature 033 (Chapter 2 Content) - MDX file and metadata exist
- Feature 034 (Chapter 2 AI Blocks Integration) - Subagents exist

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
- MUST maintain compatibility with Feature 034 (Chapter 2 AI blocks must still work)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality
- MUST follow Chapter 3 RAG prep patterns (Feature 029) for consistency

**Scale/Scope**:
- 3 new backend files to create (ch2_embedding_client.py, ch2_qdrant_store.py, ch2_pipeline.py)
- 2 backend files to update (chapter_2_chunks.py, engine.py)
- 1 environment file to update (.env.example)
- ~200-300 lines of scaffolding code (mostly signatures, TODOs, and comments)

---

## 1. Folder Structure Plan

### 1.1 New Files

**Directory**: `backend/app/ai/embeddings/`
- **Status**: Already exists (from Feature 005)
- **Files to Create**:
  - `ch2_embedding_client.py` (NEW - Chapter 2 embedding client)

**Directory**: `backend/app/ai/rag/`
- **Status**: Already exists (from Feature 005)
- **Files to Create**:
  - `ch2_qdrant_store.py` (NEW - Chapter 2 Qdrant store)
  - `ch2_pipeline.py` (NEW - Chapter 2 RAG pipeline)

### 1.2 Existing Directories (To Be Extended)

**Directory**: `backend/app/content/chapters/`
- **Status**: Already exists (from Feature 033)
- **Files to Update**:
  - `chapter_2_chunks.py` (verify/update get_chapter_2_chunks function)

**Directory**: `backend/app/ai/runtime/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `engine.py` (add Chapter 2 routing to ch2_pipeline)

**Directory**: `backend/app/ai/subagents/`
- **Status**: Already exists (from Feature 034)
- **Files to Verify**:
  - `ch2_ask_agent.py` (already exists)
  - `ch2_explain_agent.py` (already exists)
  - `ch2_quiz_agent.py` (already exists)
  - `ch2_diagram_agent.py` (already exists)

**Directory**: `.env.example`
- **Status**: Already exists (from Feature 001)
- **Files to Update**:
  - `.env.example` (add Chapter 2 environment variables)

**Directory**: `specs/035-ch2-rag-integration/contracts/`
- **Status**: Already exists (from spec phase)
- **Files to Verify**:
  - `rag-flow.yaml` (verify exists from spec phase)

---

## 2. Embedding Module Plan

### 2.1 Chapter 2 Embedding Client

**File**: `backend/app/ai/embeddings/ch2_embedding_client.py`

**Purpose**: Chapter 2-specific embedding generation functions

**Status**: Create new file

**Structure**:
- Module docstring
- Placeholder function `generate_embedding(text: str) -> List[float]`
- Placeholder function `batch_embed(chunks: List[str]) -> List[List[float]]`
- TODO comments for model selection, vector dimensions, safety guidelines
- No real API calls (placeholder only)

**Input/Output Schemas** (Text Description):

**generate_embedding(text)**:
- **Input**: `text: str` - Text to embed
- **Output**: `List[float]` - Embedding vector
- **Purpose**: Convert text into embedding vector using Chapter 2 model
- **TODO**: 
  - Select model from ENV (EMBEDDING_MODEL_CH2)
  - Generate embedding vector
  - Handle max token size, truncation
  - Return vector with expected dimensions

**batch_embed(chunks)**:
- **Input**: `chunks: List[str]` - List of text chunks
- **Output**: `List[List[float]]` - List of embedding vectors
- **Purpose**: Generate embeddings for multiple chunks in batch
- **TODO**: 
  - Process chunks in batches
  - Use Chapter 2 embedding model
  - Return list of vectors

**Dependencies**:
- Internal: `app.config.settings` (for embedding model config)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Follows same pattern as Chapter 3 embedding client (if exists)
- Uses same embedding model configuration pattern

---

## 3. Qdrant Storage Plan

### 3.1 Chapter 2 Qdrant Store

**File**: `backend/app/ai/rag/ch2_qdrant_store.py`

**Purpose**: Chapter 2-specific Qdrant vector database operations

**Status**: Create new file

**Structure**:
- Module docstring
- Placeholder function `create_collection() -> None`
- Placeholder function `upsert_vectors(vectors: List[List[float]], metadata: List[Dict]) -> None`
- Placeholder function `similarity_search(query: str, top_k: int = 5) -> List[Dict]`
- TODO comments for collection creation, vector upsertion, similarity search
- No real Qdrant client logic (placeholder only)

**Input/Output Schemas** (Text Description):

**create_collection()**:
- **Input**: None
- **Output**: None
- **Purpose**: Create Qdrant collection for Chapter 2
- **TODO**: 
  - Create collection "chapter_2" (from QDRANT_COLLECTION_CH2 env var)
  - Configure vector dimensions
  - Set distance metric (cosine similarity)
  - Configure indexing (HNSW)

**upsert_vectors(vectors, metadata)**:
- **Input**: 
  - `vectors: List[List[float]]` - Embedding vectors
  - `metadata: List[Dict]` - Chunk metadata
- **Output**: None
- **Purpose**: Insert or update vectors in Qdrant collection
- **TODO**: 
  - Upsert vectors to "chapter_2" collection
  - Include metadata (chapter_id, section_id, position, etc.)
  - Handle batch upsertion

**similarity_search(query, top_k)**:
- **Input**: 
  - `query: str` - Search query
  - `top_k: int` - Number of results (default: 5)
- **Output**: `List[Dict]` - Retrieved chunks with metadata
- **Purpose**: Perform similarity search in Qdrant collection
- **TODO**: 
  - Embed query using ch2_embedding_client
  - Search "chapter_2" collection
  - Return top-k most relevant chunks
  - Include chunk metadata

**Dependencies**:
- Internal: `app.config.settings` (for Qdrant URL/API key), `app.ai.embeddings.ch2_embedding_client`
- External: None (scaffolding only, no qdrant-client import yet)

**Reuse of Existing Modules**:
- Follows same pattern as Chapter 3 Qdrant store (if exists)
- Uses same Qdrant collection configuration pattern

---

## 4. Chapter 2 Chunk Source Plan

### 4.1 Chapter 2 Chunks File

**File**: `backend/app/content/chapters/chapter_2_chunks.py`

**Purpose**: Provide Chapter 2 content chunks for RAG pipeline

**Status**: Already exists (from Feature 033), verify/update

**Current State**: Has `get_chapter_chunks(chapter_id: int = 2)` function with placeholder return

**Updates Required**:
- Verify function exists and has correct signature
- Add `get_chapter_2_chunks() -> List[str]` function (if not exists)
- Add TODO comments explaining chunking rules (no real chunking logic)
- Ensure placeholder return: empty list

**Input/Output Schemas** (Text Description):

**get_chapter_2_chunks()**:
- **Input**: None
- **Output**: `List[str]` - List of chunk strings
- **Purpose**: Retrieve Chapter 2 content chunks for embedding and storage
- **TODO**: 
  - Load Chapter 2 content from MDX file
  - Implement chunking strategy (syntactic, semantic, hybrid)
  - Extract metadata (section titles, positions, word counts)
  - Generate unique chunk IDs
  - Handle special content (glossary, diagrams, AI blocks)
  - Return list of chunk strings

**Dependencies**:
- Internal: `app.content.chapters.chapter_2` (for metadata)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Follows same pattern as Chapter 3 chunks file
- Uses same chunking strategy patterns

---

## 5. RAG Pipeline Flow Plan

### 5.1 Chapter 2 RAG Pipeline

**File**: `backend/app/ai/rag/ch2_pipeline.py`

**Purpose**: Orchestrate RAG pipeline for Chapter 2

**Status**: Create new file

**Structure**:
- Module docstring
- Placeholder function `run_ch2_rag_pipeline(query: str, top_k: int = 5) -> Dict[str, Any]`
- 5-step flow comments:
  1. Load chapter chunks
  2. Embed query
  3. Search Qdrant
  4. Prepare context
  5. Pass into AI runtime
- All placeholder logic with TODOs
- Placeholder return: empty dict

**Input/Output Schemas** (Text Description):

**run_ch2_rag_pipeline(query, top_k)**:
- **Input**: 
  - `query: str` - User query text
  - `top_k: int` - Number of chunks to retrieve (default: 5)
- **Output**: `Dict[str, Any]` - Context dictionary with structure:
  ```python
  {
      "context": str,                    # Assembled context string
      "chunks": List[Dict[str, Any]],   # Retrieved chunks with metadata
      "query_embedding": List[float]    # Query embedding vector
  }
  ```
- **Purpose**: Execute RAG pipeline for Chapter 2
- **TODO**: 
  - Step 1: Load chapter chunks (call get_chapter_2_chunks())
  - Step 2: Embed query (call generate_embedding(query))
  - Step 3: Search Qdrant (call similarity_search(query, top_k))
  - Step 4: Prepare context (assemble retrieved chunks into context string)
  - Step 5: Pass into AI runtime (return context dictionary)

**Dependencies**:
- Internal: `app.content.chapters.chapter_2_chunks`, `app.ai.embeddings.ch2_embedding_client`, `app.ai.rag.ch2_qdrant_store`
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Follows same pattern as Chapter 3 RAG pipeline (ch3_pipeline.py)
- Uses same 5-step flow structure

---

## 6. Subagents Architecture

### 6.1 Chapter 2 Subagents Verification

**Directory**: `backend/app/ai/subagents/`

**Purpose**: Verify Chapter 2 subagents exist (from Feature 034)

**Status**: Already exists (from Feature 034)

**Files to Verify**:
- `ch2_ask_agent.py` - Already exists with Ch2AskAgent class
- `ch2_explain_agent.py` - Already exists with Ch2ExplainAgent class
- `ch2_quiz_agent.py` - Already exists with Ch2QuizAgent class
- `ch2_diagram_agent.py` - Already exists with Ch2DiagramAgent class

**Verification**:
- Each subagent has placeholder `run()` signature
- Each subagent has TODO comments
- No business logic (already scaffolded in Feature 034)

**Dependencies**:
- Internal: Feature 034 (Chapter 2 AI Blocks Integration)
- External: None

**Reuse of Existing Modules**:
- Subagents already created in Feature 034
- No changes needed

---

## 7. Runtime Routing Logic

### 7.1 Runtime Engine Integration

**File**: `backend/app/ai/runtime/engine.py`

**Purpose**: Route Chapter 2 requests to ch2_pipeline

**Status**: Already exists (from Feature 005), update with Chapter 2 routing

**Current State**: Has Chapter 2 routing comments (from Feature 034)

**Updates Required**:
- Add routing logic to detect `chapter="2"` → use `ch2_pipeline`
- Add TODO comments explaining routing rules:
  - When chapterId=2, call run_ch2_rag_pipeline()
  - Pass context to Chapter 2 subagents
  - Ensure existing Chapter 1 and Chapter 3 routing remains unchanged
- No real routing logic implemented (placeholder comments only)

**Input/Output Schemas** (Text Description):

**run_ai_block(block_type, request_data)** (Extended):
- **Input**: 
  - `block_type: str` - Type of AI block
  - `request_data: Dict[str, Any]` - Request payload with chapterId=2
- **Output**: `Dict[str, Any]` - Formatted response for frontend
- **Purpose**: Route Chapter 2 requests to ch2_pipeline and subagents
- **TODO**: 
  - Check chapterId in request_data
  - If chapterId=2, call run_ch2_rag_pipeline(query, top_k)
  - Pass context to Chapter 2 subagents
  - Format response

**Dependencies**:
- Internal: `app.ai.rag.ch2_pipeline`, `app.ai.subagents.ch2_*`
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same runtime engine structure from Feature 005
- Extends existing routing logic rather than creating new one
- Uses same subagent, RAG, and LLM provider patterns

---

## 8. API Touchpoints

### 8.1 API Endpoints

**File**: `backend/app/api/ai_blocks.py`

**Purpose**: Chapter 2 AI block endpoints (already created in Feature 034)

**Status**: Already exists (from Feature 034)

**Verification**:
- Endpoints already exist: `/ai/ch2/ask`, `/ai/ch2/explain`, `/ai/ch2/quiz`, `/ai/ch2/diagram`
- All endpoints route to `run_ai_block()` with `chapterId=2`
- No changes needed

**Dependencies**:
- Internal: Feature 034 (Chapter 2 AI Blocks Integration)
- External: None

**Reuse of Existing Modules**:
- API endpoints already created in Feature 034
- No changes needed

---

## 9. Environment Variables

### 9.1 Chapter 2 RAG Configuration

**File**: `.env.example`

**Purpose**: Document Chapter 2 RAG environment variables

**Status**: Already exists (from Feature 001), update with Chapter 2 variables

**Updates Required**:
- Add `EMBEDDING_MODEL_CH2=""` with description
- Add `QDRANT_COLLECTION_CH2=""` with description
- All variables must have placeholder values and descriptions

**Environment Variables**:
- `EMBEDDING_MODEL_CH2`: Embedding model for Chapter 2 (e.g., "text-embedding-3-small")
- `QDRANT_COLLECTION_CH2`: Qdrant collection name for Chapter 2 (e.g., "chapter_2")

**Dependencies**:
- Internal: None
- External: None

**Reuse of Existing Modules**:
- Follows same pattern as Chapter 3 environment variables
- Uses same variable naming convention

---

## 10. Future-proofing Notes

### 10.1 Scalability Considerations

- **Chapter-Specific Modules**: Each chapter has its own embedding client, Qdrant store, and pipeline for clear separation
- **Configuration-Driven**: Environment variables allow per-chapter configuration without code changes
- **Consistent Patterns**: All chapters follow same architectural patterns for maintainability

### 10.2 Extension Points

- **Embedding Models**: Easy to switch models per chapter via environment variables
- **Qdrant Collections**: Each chapter has its own collection for isolation
- **Pipeline Customization**: Chapter-specific pipelines allow custom retrieval strategies

### 10.3 Integration Points

- **Runtime Engine**: Centralized routing for all chapters
- **Subagents**: Chapter-specific subagents with consistent interface
- **Skills**: Shared skills layer for prompts and formatting

---

## 11. Success Criteria

- ✅ All ch2 pipeline files exist and import correctly
- ✅ No business logic implemented; placeholders only
- ✅ Chapter 2 AI blocks route through ch2_pipeline
- ✅ Embedding, Qdrant, Subagents folders updated
- ✅ .env.example updated with CH2 vars
- ✅ Backend boots without errors
- ✅ Contract file exists and documents RAG flow

---

## 12. Dependencies + Risks

### Dependencies:
- Feature 001: Base Project Initialization
- Feature 033: Chapter 2 Content (MDX file and metadata)
- Feature 034: Chapter 2 AI Blocks Integration (Subagents)
- Feature 029: Chapter 3 RAG Prep (reference pattern)

### Risks:
1. **Risk**: Import errors if file paths are incorrect
   - **Mitigation**: Verify all paths match existing structure
2. **Risk**: Breaking existing Chapter 1 or Chapter 3 functionality
   - **Mitigation**: Ensure all changes are additive, no modifications to existing logic
3. **Risk**: Subagent naming conflicts
   - **Mitigation**: Subagents already exist from Feature 034, verify only

---

## Summary

This plan establishes the complete architecture for Chapter 2 RAG integration scaffolding. The implementation follows Chapter 3 patterns exactly, creates all necessary files with placeholders, and ensures consistency across chapters. All components are scaffolding only—no business logic is implemented.

**Estimated Implementation Time**: 1-2 hours (scaffolding only, no business logic)
**Complexity**: Low (scaffolding, following existing patterns)
**Dependencies**: Feature 001, Feature 033, Feature 034, Feature 029
**Out of Scope**: Actual RAG logic, embedding API integration, Qdrant client integration, chunking logic implementation

