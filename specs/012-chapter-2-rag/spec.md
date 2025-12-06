# Feature Specification: Chapter 2 — RAG Chunking, Embeddings & Qdrant Collection Setup

**Feature Branch**: `012-chapter-2-rag`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "Build the RAG foundations for Chapter 2 so Ask-Question, ELI10, Quiz, and Diagram AI Blocks can retrieve ROS 2 knowledge. This includes chunking scaffolding, embeddings placeholder flow, Qdrant collection creation, and retrieval pipeline scaffolding."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Sets Up Chapter 2 RAG Infrastructure (Priority: P1)

As a backend developer, I need RAG infrastructure scaffolding for Chapter 2 (chunking, embeddings, Qdrant collections, retrieval pipeline) with placeholder functions and TODO markers, so I can implement real RAG logic in future features without restructuring the codebase.

**Why this priority**: This establishes the complete RAG foundation for Chapter 2. Without proper scaffolding, future RAG implementation will require refactoring and restructuring, causing delays and technical debt.

**Independent Test**: Can be fully tested by verifying all required files exist at specified paths, all imports resolve without errors, backend starts successfully, and all modules contain TODO placeholders for future implementation.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/content/chapters/chapter_2_chunks.py`, **Then** I see updated `get_chapter_chunks()` function with TODO comments for chunking rules (max token size, semantic segmentation, heading-aware slicing)
2. **Given** the feature is implemented, **When** I check `backend/app/ai/embeddings/embedding_client.py`, **Then** I see placeholder functions `generate_embedding()` and `batch_embed()` with TODO markers (no real API calls)
3. **Given** the feature is implemented, **When** I check `backend/app/ai/rag/qdrant_store.py`, **Then** I see placeholder function `create_collection("chapter_2")` and `upsert_vectors()` with TODO markers (no real Qdrant client logic)
4. **Given** the feature is implemented, **When** I check `backend/app/ai/rag/pipeline.py`, **Then** I see placeholder pipeline for chapterId=2 with 5-step flow comments (load chunks, embed query, perform search, build retrieval context, return context)
5. **Given** the feature is implemented, **When** I check `backend/app/ai/runtime/engine.py`, **Then** I see mapping for chapterId=2 → chapter_2_chunks with placeholder comments explaining how RAG results feed into provider LLM
6. **Given** the feature is implemented, **When** I check `.env.example`, **Then** I see new environment variables: `QDRANT_COLLECTION_CH2="chapter_2"`, `EMBEDDING_MODEL="text-embedding-3-small"`, `RAG_MAX_CONTEXT=4`
7. **Given** the feature is implemented, **When** I start the backend server, **Then** it starts without import errors or runtime exceptions
8. **Given** the feature is implemented, **When** I check contract files, **Then** I see `specs/012-chapter-2-rag/contracts/rag-pipeline.yaml` and `specs/012-chapter-2-rag/contracts/ch2-schema.yaml` with RAG pipeline contracts

---

### User Story 2 - System Administrator Configures Chapter 2 RAG Settings (Priority: P2)

As a system administrator, I need environment variables and configuration settings for Chapter 2 RAG operations (Qdrant collection name, embedding model, max context size), so I can configure the system for Chapter 2 RAG without code changes.

**Why this priority**: Important for deployment flexibility and Chapter 2-specific configuration, but not critical for initial scaffolding. Configuration can be added incrementally.

**Independent Test**: Can be fully tested by checking `.env.example` for new environment variables, verifying backend can read these variables without errors, and confirming configuration settings are documented.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `.env.example`, **Then** I see all new environment variables documented with descriptions and placeholder values
2. **Given** the backend is running, **When** I check the startup logs, **Then** I see configuration status for Chapter 2 RAG settings (even if values are not set)
3. **Given** I update `.env` with Chapter 2 RAG settings, **When** I restart the backend, **Then** the backend reads and validates the new configuration without errors

---

### User Story 3 - Future Developer Implements Chapter 2 RAG Logic (Priority: P3)

As a future developer implementing real RAG logic for Chapter 2, I need clear TODO placeholders, function signatures, expected input/output contracts, and architectural blueprints in all RAG modules, so I can implement RAG features incrementally without architectural changes.

**Why this priority**: Important for maintainability and developer experience, but not critical for initial scaffolding. Blueprints can be refined during implementation.

**Independent Test**: Can be fully tested by reviewing all RAG module files for TODO comments, function signatures, docstrings describing expected behavior, and architectural notes explaining the flow.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I review any RAG module file, **Then** I see TODO comments explaining what needs to be implemented
2. **Given** the feature is implemented, **When** I review function signatures, **Then** I see clear input/output type hints and docstrings
3. **Given** the feature is implemented, **When** I review `backend/app/ai/rag/pipeline.py`, **Then** I see placeholder flow comments explaining the chunk retrieval → embedding → search → context assembly sequence for Chapter 2
4. **Given** the feature is implemented, **When** I review chunking file, **Then** I see TODO comments explaining chunking strategy (max token size, semantic segmentation, heading-aware slicing)

---

### Edge Cases

- What happens when Qdrant collection environment variables are not set?
  - Backend should start successfully with warnings logged, Qdrant operations should log errors but not crash the server
- What happens when embedding model is not configured?
  - Embedding client should have placeholder logic that returns empty embeddings or raises clear error messages
- What happens when Chapter 2 chunks file is called but chunks don't exist?
  - `get_chapter_chunks()` should return empty list with TODO comment indicating chunks not yet implemented
- What happens when RAG pipeline is called with chapterId=2 but collection doesn't exist?
  - RAG pipeline should handle gracefully, returning placeholder response or error message indicating collection not yet created
- What happens when embedding generation fails?
  - Embedding client should have error handling placeholders that log errors and return empty embeddings

## Requirements *(mandatory)*

### Functional Requirements

#### Chapter 2 Chunking Scaffold

- **FR-001**: System MUST update `backend/app/content/chapters/chapter_2_chunks.py`:
  - Update `get_chapter_chunks()` function signature to return `List[Dict[str, Any]]` (already exists, verify structure)
  - Add comprehensive TODO comments for future chunking rules:
    - Max token size constraints
    - Semantic segmentation by section
    - Heading-aware slicing
    - Overlapping window strategy
  - Function must return empty list or placeholder data (no real chunking implementation)
  - Must include docstring explaining chunk structure and metadata

#### Embeddings Pipeline Scaffold

- **FR-002**: System MUST update `backend/app/ai/embeddings/embedding_client.py`:
  - Verify `generate_embedding(text: str) -> List[float]` function exists with TODO markers
  - Verify `batch_embed(chunks: List[str]) -> List[List[float]]` function exists with TODO markers
  - Add TODO comments explaining:
    - Future embedding model choice (OpenAI text-embedding-3-small or Gemini)
    - Batching plan for Chapter 2 chunks
    - Vector dimensional expectations
    - Safety guidelines (max token size, truncation)
  - No real API calls implemented (placeholder only)

#### Qdrant Setup for Chapter 2

- **FR-003**: System MUST update `backend/app/ai/rag/qdrant_store.py`:
  - Verify `create_collection(collection_name: str) -> bool` function exists
  - Add placeholder comment for `create_collection("chapter_2")` with TODO marker
  - Verify `upsert_vectors(collection_name: str, vectors: List[Dict[str, Any]]) -> bool` function exists
  - Add placeholder comment for Chapter 2 vector upsert with TODO marker
  - Add TODO comments explaining:
    - Collection name: "chapter_2"
    - Vector schema (placeholder)
    - Metadata schema (chunk_id, chapter_id, section_id)
  - No real Qdrant client logic implemented (placeholder only)

#### RAG Pipeline Integration

- **FR-004**: System MUST update `backend/app/ai/rag/pipeline.py`:
  - Verify `run_rag_pipeline(query: str, chapter_id: int, top_k: int = 5)` function exists
  - Add placeholder pipeline flow for chapterId=2 with 5-step comments:
    1. Load chunks (call `get_chapter_chunks(chapter_id=2)`)
    2. Embed query (call `generate_embedding(query)`)
    3. Perform search (call `similarity_search(collection="chapter_2", query_embedding, top_k)`)
    4. Build retrieval context (assemble retrieved chunks into context string)
    5. Return context to runtime (pass context to runtime engine)
  - Add TODO comments for Chapter 2-specific retrieval logic
  - No real LLM or search logic implemented (placeholder only)

#### Runtime Engine Connection

- **FR-005**: System MUST update `backend/app/ai/runtime/engine.py`:
  - Verify mapping exists for chapterId=2 → chapter_2_chunks (already exists from Feature 011)
  - Add placeholder comments explaining how RAG results feed into provider LLM:
    - RAG pipeline returns context chunks
    - Context is passed to subagents
    - Subagents use context in LLM prompts
  - Add TODO comments for Chapter 2 RAG integration in runtime flow
  - No real RAG integration logic implemented (placeholder only)

#### Environment Variable Updates

- **FR-006**: System MUST update `.env.example`:
  - Add `QDRANT_COLLECTION_CH2="chapter_2"` with description
  - Add `EMBEDDING_MODEL="text-embedding-3-small"` with description
  - Add `RAG_MAX_CONTEXT=4` with description (max number of chunks to include in context)
  - All variables must have clear descriptions and placeholder values

#### Contracts

- **FR-007**: System MUST create `specs/012-chapter-2-rag/contracts/rag-pipeline.yaml`:
  - Define RAG pipeline contract for Chapter 2
  - Include input/output schemas for each pipeline step
  - Include error handling contracts
  - Include Chapter 2-specific metadata contracts

- **FR-008**: System MUST create `specs/012-chapter-2-rag/contracts/ch2-schema.yaml`:
  - Define Chapter 2 chunk schema
  - Define Chapter 2 vector schema
  - Define Chapter 2 metadata schema
  - Include Qdrant collection schema for Chapter 2

### Assumptions

- **Assumption 1**: Chapter 2 chunks file (`chapter_2_chunks.py`) already exists from Feature 011 with placeholder function
- **Assumption 2**: Embedding client (`embedding_client.py`) already exists from Feature 005 with placeholder functions
- **Assumption 3**: Qdrant store (`qdrant_store.py`) already exists from Feature 005 with placeholder functions
- **Assumption 4**: RAG pipeline (`pipeline.py`) already exists from Feature 005 with placeholder function
- **Assumption 5**: Runtime engine (`engine.py`) already has Chapter 2 knowledge source mapping from Feature 011
- **Assumption 6**: No real RAG logic needs to be implemented (only scaffolding and TODO placeholders)
- **Assumption 7**: Chapter 2 content chunks will be implemented in future features (this feature only creates scaffolding)
- **Assumption 8**: Qdrant client library will be added in future features (this feature only creates placeholders)
- **Assumption 9**: Embedding API integration will be added in future features (this feature only creates placeholders)

### Key Entities

**Chapter 2 Chunking**:
- Function: `get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]`
- Chunk structure: id, text, chapter_id, section_id, position, word_count, metadata
- Chunking strategy: TODO for max token size, semantic segmentation, heading-aware slicing

**Chapter 2 Embeddings**:
- Function: `generate_embedding(text: str) -> List[float]`
- Function: `batch_embed(chunks: List[str]) -> List[List[float]]`
- Embedding model: TODO for OpenAI text-embedding-3-small or Gemini
- Vector dimensions: TODO (e.g., 1536 for text-embedding-3-small)

**Chapter 2 Qdrant Collection**:
- Collection name: "chapter_2"
- Vector schema: TODO (dimensions, distance metric)
- Metadata schema: chunk_id, chapter_id, section_id, position, word_count, metadata
- Functions: `create_collection("chapter_2")`, `upsert_vectors()`, `similarity_search()`

**Chapter 2 RAG Pipeline**:
- Function: `run_rag_pipeline(query: str, chapter_id: int, top_k: int = 5)`
- Pipeline steps: load chunks → embed query → perform search → build context → return context
- Chapter 2-specific flow: TODO comments for each step

**Chapter 2 Runtime Engine Mapping**:
- Knowledge source: chapterId=2 → chapter_2_chunks
- RAG integration: TODO comments explaining how RAG results feed into provider LLM
- Context flow: RAG pipeline → runtime engine → subagents → LLM prompts

## Out of Scope

- Real chunking implementation (only scaffolding and TODO placeholders)
- Real embedding API calls (only placeholder functions)
- Real Qdrant client integration (only placeholder functions)
- Real RAG pipeline execution (only placeholder flow comments)
- Real LLM provider integration (handled by existing runtime engine)
- Chapter 2 content extraction from MDX (handled by future features)
- Vector database setup and deployment (handled by infrastructure features)
- Embedding model training or fine-tuning (uses pre-trained models)

## Success Criteria

- ✅ All Chapter 2 RAG scaffolding files exist and are importable
- ✅ No embeddings or Qdrant logic implemented (TODO only)
- ✅ Runtime engine recognizes chapterId=2 retrieval request
- ✅ Backend starts successfully without import errors
- ✅ Environment variables documented in `.env.example`
- ✅ Contract files created with RAG pipeline and Chapter 2 schema definitions
- ✅ All TODO placeholders include clear implementation guidance

## Acceptance Criteria

- All chapter 2 RAG scaffolding files exist
- No embeddings or Qdrant logic implemented (TODO only)
- Runtime engine recognizes chapter 2 retrieval request
- Backend starts successfully
