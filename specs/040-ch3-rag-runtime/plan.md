# Implementation Plan: Chapter 3 — RAG Pipeline + Embeddings + AI Runtime Integration

**Branch**: `040-ch3-rag-runtime` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/040-ch3-rag-runtime/spec.md` and Feature 035 (Chapter 2 RAG Integration) as reference pattern

## Summary

This feature connects Chapter 3 content to the global AI Runtime Engine by creating RAG pipeline scaffolding, embedding placeholders, Qdrant collection scaffolding, retrieval scaffolding, and wiring Chapter 3 to the ai_blocks runtime engine. **No business logic is implemented**—only placeholder RAG flow with TODO markers, following Chapter 2 RAG integration patterns exactly.

**Primary Deliverable**: Complete RAG + runtime scaffolding for Chapter 3
**Validation**: Backend starts without errors, all imports resolve, no real AI calls, API recognizes chapterId=3

---

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI
- RAG: Qdrant vector database (scaffolding only)
- Embeddings: OpenAI embeddings API (scaffolding only)

**Primary Dependencies**:
- Feature 001 (Base Project Initialization) - Backend structure
- Feature 037 (Chapter 3 Content Specification) - Content structure
- Feature 038 (Chapter 3 MDX Implementation) - MDX file exists
- Feature 039 (Chapter 3 AI Blocks Integration) - Frontend integration
- Feature 035 (Chapter 2 RAG Integration) - Reference pattern

**Storage**: 
- Chunks: Python files (chapter_3_chunks.py)
- Embeddings: Placeholder only (no storage)
- Qdrant: Placeholder only (no real operations)

**Testing**:
- Backend: `uvicorn app.main:app --reload` startup test
- Imports: Python import verification
- API: Manual API call with chapterId=3

**Target Platform**:
- Backend: FastAPI server (Python)

**Project Type**: Backend AI integration scaffolding

**Performance Goals**:
- Backend startup: < 5 seconds
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real RAG logic (scaffolding only)
- MUST NOT embed real text (placeholders only)
- MUST NOT call live LLMs (placeholders only)
- MUST follow Chapter 2 RAG integration patterns exactly
- MUST ensure backend boots successfully

**Scale/Scope**:
- 1 new file (chapter_3_chunks.py)
- 5 files updated (embedding_client.py, qdrant_store.py, pipeline.py, engine.py, ai_blocks.py)
- 1 config file verified (settings.py)
- 1 env file updated (.env.example)

---

## 1. File Map

### 1.1 Create chapter_3_chunks.py

**Location**: `backend/app/content/chapters/chapter_3_chunks.py`
**Status**: Create new file
**Action**: Create file with placeholder functions:
- `get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]`
- `get_chapter_3_chunks() -> List[str]`
- All functions return empty lists with TODO markers

### 1.2 Update embedding_client.py

**Location**: `backend/app/ai/embeddings/embedding_client.py`
**Status**: Update existing file
**Action**: Add Chapter 3 TODO comments to `generate_embedding()` function:
- Add TODO for chapter_id=3 support
- Add TODO for CH3_EMBEDDING_MODEL usage
- No real logic changes (placeholder only)

### 1.3 Update qdrant_store.py

**Location**: `backend/app/ai/rag/qdrant_store.py`
**Status**: Update existing file
**Action**: Add Chapter 3 TODO comments to existing functions:
- `create_collection()`: Add TODO for "chapter_3" collection
- `upsert_vectors()`: Add TODO for Chapter 3 vectors
- No real logic changes (placeholder only)

### 1.4 Update rag/pipeline.py

**Location**: `backend/app/ai/rag/pipeline.py`
**Status**: Update existing file
**Action**: Add Chapter 3 branch to `run_rag_pipeline()`:
- Add `if chapter_id == 3:` branch
- Add placeholder flow comments (retrieve → embed → search → context-build)
- No real logic (placeholder only)

### 1.5 Update runtime/engine.py

**Location**: `backend/app/ai/runtime/engine.py`
**Status**: Update existing file
**Action**: Add Chapter 3 routing to `run_ai_block()`:
- Add `if chapterId == 3:` routing logic
- Add placeholder subagent calls
- No real logic (placeholder only)

### 1.6 Update ai_blocks.py

**Location**: `backend/app/api/ai_blocks.py`
**Status**: Update existing file (verify only)
**Action**: Verify all endpoints support chapterId=3:
- Endpoints should already accept chapterId parameter
- Routing handled by runtime engine
- Add TODO comments if needed

### 1.7 Update settings.py and .env.example

**Location**: `backend/app/config/settings.py` and `.env.example`
**Status**: Verify and update
**Action**: 
- Verify settings.py has Chapter 3 config (already present)
- Update .env.example with Chapter 3 env vars if missing

---

## 2. Chunk Flow Architecture

### 2.1 Chapter 3 Chunks Source

**Flow**:
```
Chapter 3 MDX Content (frontend/docs/chapters/chapter-3.mdx)
    │
    ▼
chapter_3_chunks.py
    │
    ├─► get_chapter_chunks(chapter_id=3)
    │   └─► Returns List[Dict[str, Any]] (placeholder: empty list)
    │
    └─► get_chapter_3_chunks()
        └─► Returns List[str] (placeholder: empty list)
```

**Placeholder Design**:
- Functions return empty lists
- TODO markers explain future chunking implementation
- No real chunk extraction logic

---

## 3. Embedding Flow

### 3.1 Embedding Client Extension

**Flow**:
```
User Query or Chunk Text
    │
    ▼
embedding_client.py
    │
    ├─► generate_embedding(text, chapter_id=3)
    │   └─► Returns List[float] (placeholder: empty list)
    │   └─► TODO: Use CH3_EMBEDDING_MODEL
    │
    └─► batch_embed() (if needed)
        └─► Returns List[List[float]] (placeholder: empty list)
```

**Placeholder Design**:
- Functions return empty lists
- TODO markers explain future embedding generation
- No real API calls

---

## 4. Qdrant Flow

### 4.1 Qdrant Collection Operations

**Flow**:
```
Chapter 3 Collection Setup
    │
    ▼
qdrant_store.py
    │
    ├─► create_collection("chapter_3")
    │   └─► Returns bool (placeholder: False)
    │   └─► TODO: Create "chapter_3" collection
    │
    ├─► upsert_vectors("chapter_3", vectors)
    │   └─► Returns bool (placeholder: False)
    │   └─► TODO: Upsert Chapter 3 vectors
    │
    └─► similarity_search("chapter_3", query, top_k)
        └─► Returns List[Dict] (placeholder: empty list)
        └─► TODO: Search Chapter 3 collection
```

**Placeholder Design**:
- Functions return placeholder values
- TODO markers explain future Qdrant operations
- No real Qdrant client logic

---

## 5. RAG Pipeline Integration

### 5.1 Pipeline Flow for Chapter 3

**Flow**:
```
User Query
    │
    ▼
pipeline.py::run_rag_pipeline(query, chapter_id=3, top_k=5)
    │
    ├─► Step 1: get_chapter_chunks(chapter_id=3)
    │   └─► TODO: Retrieve Chapter 3 chunks
    │
    ├─► Step 2: generate_embedding(query, chapter_id=3)
    │   └─► TODO: Embed user query
    │
    ├─► Step 3: similarity_search("chapter_3", query_embedding, top_k)
    │   └─► TODO: Search Qdrant collection
    │
    ├─► Step 4: Assemble context from retrieved chunks
    │   └─► TODO: Build retrieval context
    │
    └─► Step 5: Return context to runtime engine
        └─► Returns Dict[str, Any] (placeholder: empty dict)
```

**Placeholder Design**:
- All steps are TODO comments only
- No real RAG logic implemented
- Returns placeholder empty dict

---

## 6. Runtime Routing Layer

### 6.1 Runtime Engine Routing

**Flow**:
```
API Request (chapterId=3)
    │
    ▼
engine.py::run_ai_block(block_type, request_data)
    │
    ├─► Check chapterId in request_data
    │   └─► if chapterId == 3:
    │       │
    │       ├─► TODO: Route to Chapter 3 RAG pipeline
    │       │   └─► run_rag_pipeline(query, chapter_id=3)
    │       │
    │       ├─► TODO: Call Chapter 3 subagents
    │       │   └─► ch3_ask_agent.run() (future)
    │       │   └─► ch3_explain_agent.run() (future)
    │       │   └─► ch3_quiz_agent.run() (future)
    │       │   └─► ch3_diagram_agent.run() (future)
    │       │
    │       └─► Return placeholder response
    │
    └─► Returns Dict[str, Any] (placeholder: empty dict)
```

**Placeholder Design**:
- Routing logic is TODO comments only
- No real subagent calls
- Returns placeholder empty dict

---

## 7. API Mapping

### 7.1 API Endpoints Support

**Endpoints**:
- `POST /api/ai/ask-question` - Supports chapterId=3
- `POST /api/ai/explain-like-10` - Supports chapterId=3
- `POST /api/ai/quiz` - Supports chapterId=3
- `POST /api/ai/diagram` - Supports chapterId=3

**Flow**:
```
API Request (chapterId=3)
    │
    ▼
ai_blocks.py endpoint
    │
    ├─► Validate request (chapterId=3 accepted)
    │
    ├─► Call runtime engine
    │   └─► run_ai_block(block_type, request_data)
    │
    └─► Return response (placeholder)
```

**Placeholder Design**:
- Endpoints accept chapterId=3
- Routing handled by runtime engine
- Returns placeholder responses

---

## 8. Constraints

### 8.1 No Real AI Logic

- **Constraint**: MUST NOT implement real RAG logic
- **Rationale**: This is scaffolding phase only
- **Implementation**: All logic is TODO comments and placeholder returns

### 8.2 No Real Embeddings

- **Constraint**: MUST NOT embed real text
- **Rationale**: Embedding generation is future feature
- **Implementation**: Functions return empty lists

### 8.3 No Real Qdrant Operations

- **Constraint**: MUST NOT perform real Qdrant operations
- **Rationale**: Qdrant setup is future feature
- **Implementation**: Functions return placeholder values

### 8.4 Follow Chapter 2 Patterns

- **Constraint**: MUST follow Chapter 2 RAG integration patterns exactly
- **Rationale**: Maintains consistency across chapters
- **Implementation**: Replicate Chapter 2 structure for Chapter 3

---

## 9. Success Criteria

- ✅ Backend runs without errors (`uvicorn app.main:app --reload` succeeds)
- ✅ All Chapter 3 scaffolding files exist
- ✅ No real AI calls or embeddings
- ✅ ai_blocks API recognizes chapterId=3
- ✅ Runtime engine routes to chapter 3 stub
- ✅ Pipeline imports chapter_3_chunks successfully

---

## 10. Dependencies + Risks

### Dependencies:
- Feature 001: Base Project Initialization
- Feature 037: Chapter 3 Content Specification
- Feature 038: Chapter 3 MDX Implementation
- Feature 039: Chapter 3 AI Blocks Integration
- Feature 035: Chapter 2 RAG Integration (reference pattern)

### Risks:
1. **Risk**: Import errors if chapter_3_chunks.py not created correctly
   - **Mitigation**: Verify imports resolve, test backend startup
2. **Risk**: Backend startup fails if syntax errors
   - **Mitigation**: Test backend startup after each file update
3. **Risk**: API routing doesn't work for chapterId=3
   - **Mitigation**: Test API calls with chapterId=3, verify routing

---

## Summary

This plan establishes the complete architecture for Chapter 3 RAG + runtime integration. The implementation follows Chapter 2 RAG integration patterns exactly, creates all necessary scaffolding files, and ensures backend starts successfully. All logic is placeholder-only—no real RAG, embeddings, or Qdrant operations.

**Estimated Implementation Time**: 45-60 minutes (scaffolding only, no real AI logic)
**Complexity**: Low (following existing patterns, placeholder implementation)
**Dependencies**: Feature 001, Feature 037, Feature 038, Feature 039, Feature 035
**Out of Scope**: Real RAG pipeline, real embeddings, real Qdrant operations, real AI logic

