# Quickstart Guide: Chapter 3 RAG + Runtime Integration

**Feature**: 040-ch3-rag-runtime
**Branch**: `040-ch3-rag-runtime`
**Estimated Time**: 45-60 minutes (scaffolding only, no real AI logic)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 001 (Base Project Initialization) completed
- [x] Feature 037 (Chapter 3 Content Specification) completed
- [x] Feature 038 (Chapter 3 MDX Implementation) completed
- [x] Feature 039 (Chapter 3 AI Blocks Integration) completed
- [x] Feature 035 (Chapter 2 RAG Integration) completed - Reference for patterns
- [x] Git branch `040-ch3-rag-runtime` checked out
- [x] Read `specs/040-ch3-rag-runtime/spec.md`
- [x] Read `specs/035-ch2-rag-integration/spec.md` (reference pattern)

## Implementation Overview

**Total Steps**: 7 phases
**Primary Deliverable**: Complete RAG + runtime scaffolding for Chapter 3
**Validation**: Backend starts without errors, all imports resolve, no real AI calls

---

## Phase 1: Chapter 3 Chunks Source (10 minutes)

### Step 1.1: Create chapter_3_chunks.py

**File**: `backend/app/content/chapters/chapter_3_chunks.py`

**Action**: Create file with placeholder functions:

```python
"""
Chapter 3 Content Chunks

Provides chapter content chunks for RAG pipeline.
Chunks are used for semantic search and context retrieval.
"""

from typing import List, Dict, Any

def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 3 with metadata.
    
    TODO: Implement chunking from Chapter 3 MDX content
    TODO: Load Chapter 3 content from frontend/docs/chapters/chapter-3.mdx
    TODO: Implement chunking strategy
    """
    return []  # Placeholder return

def get_chapter_3_chunks() -> List[str]:
    """
    Return list of text chunks from Chapter 3 as strings.
    
    TODO: Implement chunking from Chapter 3 MDX content
    """
    return []  # Placeholder return
```

**Validation**: File exists, functions have correct signatures, imports resolve

---

## Phase 2: Embeddings Layer (5 minutes)

### Step 2.1: Update embedding_client.py

**File**: `backend/app/ai/embeddings/embedding_client.py`

**Action**: Add Chapter 3 TODO comments to existing functions:

```python
def generate_embedding(text: str, chapter_id: int = 1) -> List[float]:
    """
    TODO: Add chapter_id=3 support for Chapter 3
    TODO: Use CH3_EMBEDDING_MODEL when chapter_id=3
    """
    return []  # Placeholder return
```

**Validation**: File updated, TODO comments added, no syntax errors

---

## Phase 3: Qdrant Storage Layer (5 minutes)

### Step 3.1: Update qdrant_store.py

**File**: `backend/app/ai/rag/qdrant_store.py`

**Action**: Add Chapter 3 TODO comments to existing functions:

```python
def create_collection(collection_name: str) -> bool:
    """
    TODO: For Chapter 3: collection_name = "chapter_3"
    """
    return False  # Placeholder return

def upsert_vectors(collection_name: str, vectors: List[Dict[str, Any]]) -> bool:
    """
    TODO: For Chapter 3: collection_name = "chapter_3"
    """
    return False  # Placeholder return
```

**Validation**: File updated, TODO comments added, no syntax errors

---

## Phase 4: RAG Pipeline Integration (10 minutes)

### Step 4.1: Update pipeline.py

**File**: `backend/app/ai/rag/pipeline.py`

**Action**: Add Chapter 3 branch to run_rag_pipeline():

```python
async def run_rag_pipeline(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> Dict[str, Any]:
    """
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

**Validation**: File updated, Chapter 3 branch added, no syntax errors

---

## Phase 5: Runtime Engine Routing (10 minutes)

### Step 5.1: Update engine.py

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Add Chapter 3 routing to run_ai_block():

```python
async def run_ai_block(
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Chapter 3 routing
    if request_data.get("chapterId") == 3:
        # TODO: Route to Chapter 3 RAG pipeline
        # TODO: Call Chapter 3 subagents
        pass
    """
    return {}  # Placeholder return
```

**Validation**: File updated, Chapter 3 routing added, no syntax errors

---

## Phase 6: API Layer Verification (5 minutes)

### Step 6.1: Verify ai_blocks.py

**File**: `backend/app/api/ai_blocks.py`

**Action**: Verify all endpoints support chapterId=3 (should already work via runtime engine)

**Validation**: Endpoints accept chapterId=3 parameter, routing handled by runtime engine

---

## Phase 7: Config Layer (5 minutes)

### Step 7.1: Verify settings.py

**File**: `backend/app/config/settings.py`

**Action**: Verify Chapter 3 config exists (already present):
- QDRANT_COLLECTION_CH3
- CH3_EMBEDDING_MODEL
- CH3_LLM_MODEL

### Step 7.2: Update .env.example

**File**: `.env.example`

**Action**: Add Chapter 3 env vars if not present:

```env
# Chapter 3 RAG Configuration
QDRANT_COLLECTION_CH3=chapter_3
CH3_EMBEDDING_MODEL=
CH3_LLM_MODEL=
```

**Validation**: Config verified, .env.example updated

---

## Phase 8: Validation (10 minutes)

### Step 8.1: Backend Startup Test

**Action**: Run `uvicorn app.main:app --reload` in backend directory
**Expected**: Backend starts without errors

### Step 8.2: Import Test

**Action**: Test imports:
```python
from app.content.chapters.chapter_3_chunks import get_chapter_chunks
from app.ai.rag.pipeline import run_rag_pipeline
```

**Expected**: All imports resolve successfully

### Step 8.3: API Test

**Action**: Make API call with chapterId=3:
```bash
curl -X POST http://localhost:8000/api/ai/ask-question \
  -H "Content-Type: application/json" \
  -d '{"question": "test", "chapterId": 3}'
```

**Expected**: Request routes to Chapter 3 placeholder logic (no errors)

---

## Success Criteria

- ✅ Backend runs without errors
- ✅ All Chapter 3 scaffolding files exist
- ✅ No real AI calls or embeddings
- ✅ ai_blocks API recognizes chapterId=3
- ✅ Runtime engine routes to chapter 3 stub
- ✅ Pipeline imports chapter_3_chunks successfully

---

## Troubleshooting

### Import Errors
- Verify chapter_3_chunks.py exists at correct path
- Check function names match imports
- Verify Python path includes backend directory

### Backend Startup Errors
- Check all imports resolve
- Verify settings.py has Chapter 3 config
- Check for syntax errors in modified files

### API Routing Errors
- Verify runtime engine has Chapter 3 routing
- Check request_data includes chapterId=3
- Verify API endpoints accept chapterId parameter

---

## Notes

- This is scaffolding only—no real RAG logic implemented
- All functions return placeholder values
- TODO comments mark future implementation points
- Follows Chapter 2 RAG integration patterns exactly
- Backend architecture ready for future AI logic

