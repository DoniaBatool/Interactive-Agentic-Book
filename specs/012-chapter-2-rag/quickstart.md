# Quickstart: Chapter 2 — RAG Chunking, Embeddings & Qdrant Collection Setup

**Feature**: 012-chapter-2-rag
**Feature ID**: 012-chapter-2-rag
**Created**: 2025-12-05

## Prerequisites

- Feature 005 (AI Runtime Engine) completed - provides embedding_client.py, qdrant_store.py, pipeline.py
- Feature 011 (Chapter 2 AI Blocks) completed - provides chapter_2_chunks.py placeholder, runtime engine mapping
- Backend Python environment set up
- `.env.example` file exists

## Commands

```
/sp.specify  # ✅ COMPLETED - Specification created
/sp.plan     # Next: Create architecture plan
/sp.tasks    # After plan: Generate implementation tasks
/sp.implement # After tasks: Implement scaffolding
```

## Folder Structure

```
specs/012-chapter-2-rag/
├── spec.md                    # ✅ Feature specification
├── plan.md                    # TODO: Architecture plan
├── tasks.md                   # TODO: Implementation tasks
├── research.md                # ✅ RAG architecture research
├── data-model.md              # ✅ Data structures and entities
├── quickstart.md              # ✅ This file
├── contracts/
│   ├── rag-pipeline.yaml      # ✅ RAG pipeline contract
│   └── ch2-schema.yaml        # ✅ Chapter 2 schema contract
└── checklists/
    └── requirements.md        # ✅ Specification quality checklist
```

## Feature Overview

This feature builds RAG foundations for Chapter 2 by creating scaffolding for:
1. **Chunking**: Update `chapter_2_chunks.py` with TODO comments for chunking rules
2. **Embeddings**: Verify `embedding_client.py` has placeholder functions
3. **Qdrant**: Verify `qdrant_store.py` has placeholder functions for Chapter 2 collection
4. **RAG Pipeline**: Add placeholder flow for chapterId=2 in `pipeline.py`
5. **Runtime Engine**: Add comments explaining RAG integration for Chapter 2
6. **Environment Variables**: Add Chapter 2 RAG config to `.env.example`

## Key Files to Modify

### Backend Files

1. **`backend/app/content/chapters/chapter_2_chunks.py`**
   - Update `get_chapter_chunks()` with TODO comments for chunking rules
   - Add comments for max token size, semantic segmentation, heading-aware slicing

2. **`backend/app/ai/embeddings/embedding_client.py`**
   - Verify `generate_embedding()` and `batch_embed()` exist
   - Add TODO comments for Chapter 2 embedding strategy

3. **`backend/app/ai/rag/qdrant_store.py`**
   - Verify `create_collection()` and `upsert_vectors()` exist
   - Add placeholder comments for Chapter 2 collection ("chapter_2")

4. **`backend/app/ai/rag/pipeline.py`**
   - Verify `run_rag_pipeline()` exists
   - Add placeholder flow comments for chapterId=2

5. **`backend/app/ai/runtime/engine.py`**
   - Verify mapping exists for chapterId=2 → chapter_2_chunks
   - Add comments explaining how RAG results feed into provider LLM

6. **`.env.example`**
   - Add `QDRANT_COLLECTION_CH2="chapter_2"`
   - Add `EMBEDDING_MODEL="text-embedding-3-small"`
   - Add `RAG_MAX_CONTEXT=4`

## Implementation Strategy

### Phase 1: Specification ✅
- Create spec.md with requirements
- Create contracts (rag-pipeline.yaml, ch2-schema.yaml)
- Create research.md, data-model.md, checklists, quickstart.md

### Phase 2: Planning (Next)
- Create plan.md with architecture decisions
- Define chunking strategy
- Define embedding model selection
- Define Qdrant collection design
- Define retrieval pipeline flow

### Phase 3: Task Generation
- Create tasks.md with atomic tasks
- Group tasks by phase (chunking, embeddings, Qdrant, pipeline, runtime)

### Phase 4: Implementation
- Update chapter_2_chunks.py with TODO comments
- Verify embedding_client.py placeholders
- Verify qdrant_store.py placeholders
- Update pipeline.py with Chapter 2 flow comments
- Update runtime engine with RAG integration comments
- Update .env.example with Chapter 2 config

## Validation Steps

After implementation:

1. **Backend Import Validation**:
   ```bash
   cd backend
   python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; print('SUCCESS')"
   python -c "from app.ai.embeddings.embedding_client import generate_embedding; print('SUCCESS')"
   python -c "from app.ai.rag.qdrant_store import create_collection; print('SUCCESS')"
   python -c "from app.ai.rag.pipeline import run_rag_pipeline; print('SUCCESS')"
   ```

2. **Backend Startup Validation**:
   ```bash
   cd backend
   python -m uvicorn app.main:app --reload
   # Should start without import errors
   ```

3. **Environment Variables Validation**:
   ```bash
   # Check .env.example has new variables
   grep QDRANT_COLLECTION_CH2 .env.example
   grep EMBEDDING_MODEL .env.example
   grep RAG_MAX_CONTEXT .env.example
   ```

4. **File Existence Validation**:
   ```bash
   # Check all files exist
   ls backend/app/content/chapters/chapter_2_chunks.py
   ls backend/app/ai/embeddings/embedding_client.py
   ls backend/app/ai/rag/qdrant_store.py
   ls backend/app/ai/rag/pipeline.py
   ```

## Success Criteria

- ✅ All Chapter 2 RAG scaffolding files exist
- ✅ No embeddings or Qdrant logic implemented (TODO only)
- ✅ Runtime engine recognizes chapterId=2 retrieval request
- ✅ Backend starts successfully

## Next Steps

1. Run `/sp.plan` to create architecture plan
2. Review plan.md for chunking strategy, embedding model, Qdrant design
3. Run `/sp.tasks` to generate implementation tasks
4. Run `/sp.implement` to implement scaffolding

## Notes

- This is a **scaffolding-only** feature. No real RAG logic will be implemented.
- All functions return placeholders (empty lists, empty dicts, False, etc.)
- TODO comments explain future implementation requirements.
- Real RAG implementation will be added in future features.
