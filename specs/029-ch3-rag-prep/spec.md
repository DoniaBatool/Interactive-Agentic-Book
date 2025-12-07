# Feature Specification: Chapter 3 — RAG + Embedding Preparation Layer

**Feature Branch**: `029-ch3-rag-prep`
**Created**: 2025-01-27
**Status**: Draft
**Type**: backend-rag-architecture
**Input**: User description: "Add the scaffolding for embeddings, chunking, retrieval preparation, and Qdrant collection setup for Chapter 3. No logic. Only structure, placeholders, TODOs, and metadata required for future RAG operations."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Sets Up Chapter 3 RAG Infrastructure (Priority: P1)

As a backend developer, I need RAG infrastructure scaffolding for Chapter 3 (chunking, embeddings, Qdrant collections, retrieval pipeline) with placeholder functions and TODO markers, so I can implement real RAG logic in future features without restructuring the codebase.

**Why this priority**: This establishes the complete RAG foundation for Chapter 3. Without proper scaffolding, future RAG implementation will require refactoring and restructuring, causing delays and technical debt.

**Independent Test**: Can be fully tested by verifying all required files exist at specified paths, all imports resolve without errors, backend starts successfully, and all modules contain TODO placeholders for future implementation.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/content/chapters/chapter_3_chunks.py`, **Then** I see `get_chapter_chunks()` function with TODO comments for chunking rules (max token size, semantic segmentation, heading-aware slicing) and placeholder CH3_CHUNKS list
2. **Given** the feature is implemented, **When** I check `backend/app/ai/embeddings/embedding_client.py`, **Then** I see placeholder functions `embed_chapter3_chunks()` and `normalize_chapter3_embeddings()` with TODO markers (no real API calls)
3. **Given** the feature is implemented, **When** I check `backend/app/ai/rag/qdrant_store.py`, **Then** I see placeholder functions for `create_collection("chapter3")`, `upsert_vectors()` for Chapter 3, and `similarity_search_ch3()` with TODO markers (no real Qdrant client logic)
4. **Given** the feature is implemented, **When** I check `backend/app/ai/rag/ch3_pipeline.py`, **Then** I see placeholder pipeline with 5-step flow comments (retrieve chunks, embed query, perform search, construct retrieval context, return placeholder response)
5. **Given** the feature is implemented, **When** I check `frontend/docs/chapters/chapter-3.mdx`, **Then** I see `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers defining chunk boundaries
6. **Given** the feature is implemented, **When** I check `backend/app/config/settings.py`, **Then** I see `qdrant_collection_ch3` and `ch3_embedding_model` configuration fields
7. **Given** the feature is implemented, **When** I check `.env.example`, **Then** I see new environment variables: `QDRANT_COLLECTION_CH3="chapter3"`, `EMBEDDING_MODEL_CH3="text-embedding-3-small"`
8. **Given** the feature is implemented, **When** I start the backend server, **Then** it starts without import errors or runtime exceptions
9. **Given** the feature is implemented, **When** I check contract files, **Then** I see `specs/029-ch3-rag-prep/contracts/ch3-rag-definition.yaml` with RAG pipeline contracts

---

### User Story 2 - System Administrator Configures Chapter 3 RAG Settings (Priority: P2)

As a system administrator, I need environment variables and configuration settings for Chapter 3 RAG operations (Qdrant collection name, embedding model), so I can configure the system for Chapter 3 RAG without code changes.

**Why this priority**: Important for deployment flexibility and Chapter 3-specific configuration, but not critical for initial scaffolding. Configuration can be added incrementally.

**Independent Test**: Can be fully tested by checking `.env.example` for new environment variables, verifying backend can read these variables without errors, and confirming configuration settings are documented.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `.env.example`, **Then** I see all new environment variables documented with descriptions and placeholder values
2. **Given** the backend is running, **When** I check the startup logs, **Then** I see configuration status for Chapter 3 RAG settings (even if values are not set)
3. **Given** I update `.env` with Chapter 3 RAG settings, **When** I restart the backend, **Then** the backend reads and validates the new configuration without errors

---

### Edge Cases

- What happens when Qdrant collection environment variables are not set?
  - Backend should start successfully with warnings logged, Qdrant operations should log errors but not crash the server
- What happens when embedding model is not configured?
  - Embedding client should have placeholder logic that returns empty embeddings or raises clear error messages
- What happens when Chapter 3 chunks file is called but chunks don't exist?
  - `get_chapter_chunks()` should return empty list with TODO comment indicating chunks not yet implemented
- What happens when RAG pipeline is called with chapterId=3 but collection doesn't exist?
  - RAG pipeline should handle gracefully, returning placeholder response or error message indicating collection not yet created
- What happens when embedding generation fails?
  - Embedding client should have error handling placeholders that log errors and return empty embeddings

## Requirements *(mandatory)*

### Functional Requirements

#### Chapter 3 Chunking Scaffold

- **FR-001**: System MUST update `backend/app/content/chapters/chapter_3_chunks.py`:
  - Verify `get_chapter_chunks(chapter_id: int = 3)` function exists (already exists)
  - Add placeholder `CH3_CHUNKS = []` list constant
  - Add comprehensive TODO comments for future chunking rules:
    - Max token size constraints
    - Semantic segmentation by section
    - Heading-aware slicing
    - Overlapping window strategy
    - Respect RAG-CHUNK markers from MDX
  - Function must return empty list or placeholder data (no real chunking implementation)
  - Must include docstring explaining chunk structure and metadata

#### Embeddings Pipeline Scaffold

- **FR-002**: System MUST update `backend/app/ai/embeddings/embedding_client.py`:
  - Add placeholder function `embed_chapter3_chunks(chunks: List[str]) -> List[List[float]]`:
    - Function signature with type hints
    - TODO comments explaining:
      - Future embedding model choice (OpenAI text-embedding-3-small or Gemini)
      - Batching plan for Chapter 3 chunks
      - Vector dimensional expectations (1536 for text-embedding-3-small)
      - Safety guidelines (max token size, truncation)
    - Placeholder return: empty list
  - Add placeholder function `normalize_chapter3_embeddings(embeddings: List[List[float]]) -> List[List[float]]`:
    - Function signature with type hints
    - TODO comments explaining normalization requirements
    - Placeholder return: empty list
  - No real API calls implemented (placeholder only)

#### Qdrant Setup for Chapter 3

- **FR-003**: System MUST update `backend/app/ai/rag/qdrant_store.py`:
  - Add placeholder comment for `create_collection("chapter3")` with TODO marker:
    - Collection name: "chapter3" (from QDRANT_COLLECTION_CH3 env var)
    - Vector schema (placeholder)
    - Metadata schema (chunk_id, chapter_id, section_id)
  - Add placeholder comment for Chapter 3 vector upsert with TODO marker:
    - Use `upsert_vectors(collection_name="chapter3", vectors=...)`
    - Vector structure: {id, vector (1536 dims), payload (metadata)}
  - Add placeholder function `similarity_search_ch3(query: str, top_k: int = 5) -> List[Dict[str, Any]]`:
    - Function signature with type hints
    - TODO comments explaining Chapter 3 search logic
    - Placeholder return: empty list
  - No real Qdrant client logic implemented (placeholder only)

#### RAG Pipeline Integration

- **FR-004**: System MUST create `backend/app/ai/rag/ch3_pipeline.py`:
  - Create file with placeholder pipeline function:
    - Function signature: `async def run_ch3_rag_pipeline(query: str, top_k: int = 5) -> Dict[str, Any]`
    - Add 5-step pipeline flow comments:
      1. Retrieve chunks (call `get_chapter_chunks(chapter_id=3)`)
      2. Embed query (call `generate_embedding(query, chapter_id=3)`)
      3. Perform search (call `similarity_search_ch3(query, top_k)`)
      4. Construct retrieval context (assemble retrieved chunks into context string)
      5. Return placeholder response (return context dictionary)
    - Add TODO comments for Chapter 3-specific retrieval logic
    - Placeholder return structure: `{"context": "", "chunks": [], "query_embedding": []}`
  - No real LLM or search logic implemented (placeholder only)

#### MDX RAG Markers

- **FR-005**: System MUST update `frontend/docs/chapters/chapter-3.mdx`:
  - Add `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers around each section
  - Markers should wrap section content including AI blocks and diagrams
  - Markers define future chunk boundaries for RAG pipeline
  - Ensure markers don't interfere with existing `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` markers

#### Environment Variable Updates

- **FR-006**: System MUST update `backend/app/config/settings.py`:
  - Add `qdrant_collection_ch3: Optional[str] = None` field with comment
  - Add `ch3_embedding_model: Optional[str] = None` field with comment
  - Fields should follow same pattern as Chapter 2 configuration

- **FR-007**: System MUST update `.env.example` (create if doesn't exist):
  - Add `QDRANT_COLLECTION_CH3="chapter3"` with description
  - Add `EMBEDDING_MODEL_CH3="text-embedding-3-small"` with description
  - All variables must have clear descriptions and placeholder values

#### Contracts

- **FR-008**: System MUST create `specs/029-ch3-rag-prep/contracts/ch3-rag-definition.yaml`:
  - Document expected structure of Chapter 3 RAG data
  - Document chunk structure, embedding format, Qdrant collection schema
  - Document pipeline flow (5 steps)
  - No implementation details (structure only)

### Assumptions

- **Assumption 1**: Chapter 3 chunks file already exists from Feature 028 (may need updates)
- **Assumption 2**: Embedding client and Qdrant store files exist from previous features
- **Assumption 3**: Chapter 3 MDX file exists from Feature 028
- **Assumption 4**: No new external dependencies required (scaffolding only)
- **Assumption 5**: Backend configuration system (settings.py) already supports environment variables

### Key Entities

**Chapter 3 Chunk**:
- Structure: {id, text, chapter_id: 3, section_id, position, word_count, metadata}
- Source: chapter_3_chunks.py
- Function: get_chapter_chunks(chapter_id=3)

**Chapter 3 Embedding**:
- Structure: List[float] (1536 dimensions for text-embedding-3-small)
- Source: embedding_client.py
- Functions: embed_chapter3_chunks(), normalize_chapter3_embeddings()

**Chapter 3 Qdrant Collection**:
- Name: "chapter3" (from QDRANT_COLLECTION_CH3 env var)
- Vector schema: 1536 dimensions
- Metadata schema: {chunk_id, chapter_id: 3, section_id, position, text, metadata}

**Chapter 3 RAG Pipeline**:
- File: ch3_pipeline.py
- Function: run_ch3_rag_pipeline(query, top_k)
- Flow: Retrieve → Embed → Search → Context → Response

## Success Criteria *(mandatory)*

- **SC-001**: Chapter 3 chunks file exists with placeholder CH3_CHUNKS list and get_chapter_chunks() function
- **SC-002**: Embedding client has embed_chapter3_chunks() and normalize_chapter3_embeddings() placeholder functions
- **SC-003**: Qdrant store has create_collection("chapter3"), upsert_vectors for Chapter 3, and similarity_search_ch3() placeholder functions
- **SC-004**: Chapter 3 RAG pipeline file (ch3_pipeline.py) exists with 5-step flow comments
- **SC-005**: Chapter 3 MDX contains RAG-CHUNK markers
- **SC-006**: Settings file has qdrant_collection_ch3 and ch3_embedding_model fields
- **SC-007**: .env.example has QDRANT_COLLECTION_CH3 and EMBEDDING_MODEL_CH3 variables
- **SC-008**: Contract file exists and documents Chapter 3 RAG structure
- **SC-009**: Backend starts without import errors or runtime exceptions
- **SC-010**: No real RAG/LLM logic implemented (only placeholders and TODOs)

## Constraints *(mandatory)*

- **Constraint 1**: Must NOT implement real RAG logic (no vector operations, no embedding API calls, no Qdrant client operations)
- **Constraint 2**: Must NOT break existing Chapter 1 or Chapter 2 RAG functionality
- **Constraint 3**: Must follow same patterns used in Chapter 2 RAG prep (Feature 012 or 021)
- **Constraint 4**: Must ensure backend starts without errors
- **Constraint 5**: Must ensure all imports resolve correctly
- **Constraint 6**: Must use Python 3.11+ type hints
- **Constraint 7**: Must include TODO comments in all placeholder functions

## Dependencies

- **Feature 028**: Chapter 3 AI Blocks Integration (provides chapter_3_chunks.py and chapter-3.mdx)
- **Feature 012 or 021**: Chapter 2 RAG Prep (reference for patterns)
- **Feature 005**: AI Runtime Engine (provides embedding_client.py, qdrant_store.py, pipeline.py)

## Out of Scope

- Real chunking implementation (only placeholder structure)
- Real embedding generation (only placeholder functions)
- Real Qdrant operations (only placeholder functions)
- Real RAG pipeline execution (only placeholder flow)
- Vector database setup (only configuration placeholders)
- Embedding model integration (only configuration placeholders)

