# Quickstart: Chapter 3 — RAG + Embedding Preparation Layer

**Feature**: 029-ch3-rag-prep
**Feature ID**: 029-ch3-rag-prep
**Created**: 2025-01-27

## Prerequisites

- Feature 028 (Chapter 3 AI Blocks Integration) completed - provides chapter_3_chunks.py and chapter-3.mdx
- Feature 012 or 021 (Chapter 2 RAG Prep) completed - provides reference patterns
- Feature 005 (AI Runtime Engine) completed - provides embedding_client.py, qdrant_store.py, pipeline.py
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
specs/029-ch3-rag-prep/
├── spec.md                    # ✅ Feature specification
├── plan.md                    # TODO: Architecture plan
├── tasks.md                   # TODO: Implementation tasks
├── research.md                # ✅ RAG architecture research
├── data-model.md              # ✅ Data structures and entities
├── quickstart.md              # ✅ This file
├── contracts/
│   └── ch3-rag-definition.yaml # ✅ Chapter 3 RAG definition contract
└── checklists/
    └── requirements.md        # ✅ Specification quality checklist
```

## Feature Overview

This feature builds RAG foundations for Chapter 3 by creating scaffolding for:
1. **Chunking**: Update `chapter_3_chunks.py` with placeholder CH3_CHUNKS list and TODO comments
2. **Embeddings**: Add `embed_chapter3_chunks()` and `normalize_chapter3_embeddings()` placeholder functions
3. **Qdrant**: Add `create_collection("chapter3")`, `upsert_vectors()` for Chapter 3, and `similarity_search_ch3()` placeholder functions
4. **RAG Pipeline**: Create `ch3_pipeline.py` with 5-step flow comments
5. **MDX RAG Markers**: Add `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers to chapter-3.mdx
6. **Environment Variables**: Add Chapter 3 RAG config to `settings.py` and `.env.example`

## Key Files to Modify

### Backend Files

1. **`backend/app/content/chapters/chapter_3_chunks.py`**
   - Add placeholder `CH3_CHUNKS = []` constant
   - Update `get_chapter_chunks()` with TODO comments for chunking rules
   - Add comments for max token size, semantic segmentation, heading-aware slicing, RAG-CHUNK markers

2. **`backend/app/ai/embeddings/embedding_client.py`**
   - Add placeholder function `embed_chapter3_chunks(chunks: List[str]) -> List[List[float]]`
   - Add placeholder function `normalize_chapter3_embeddings(embeddings: List[List[float]]) -> List[List[float]]`
   - Add TODO comments for Chapter 3 embedding strategy

3. **`backend/app/ai/rag/qdrant_store.py`**
   - Add placeholder comment for `create_collection("chapter3")` with TODO marker
   - Add placeholder comment for Chapter 3 vector upsert with TODO marker
   - Add placeholder function `similarity_search_ch3(query: str, top_k: int = 5) -> List[Dict[str, Any]]`

4. **`backend/app/ai/rag/ch3_pipeline.py`** (NEW FILE)
   - Create file with placeholder pipeline function
   - Add 5-step pipeline flow comments (retrieve → embed → search → context → response)
   - Add TODO comments for Chapter 3-specific retrieval logic

5. **`backend/app/config/settings.py`**
   - Add `qdrant_collection_ch3: Optional[str] = None` field
   - Add `ch3_embedding_model: Optional[str] = None` field

6. **`.env.example`** (create if doesn't exist)
   - Add `QDRANT_COLLECTION_CH3="chapter3"` with description
   - Add `EMBEDDING_MODEL_CH3="text-embedding-3-small"` with description

### Frontend Files

7. **`frontend/docs/chapters/chapter-3.mdx`**
   - Add `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers around each section
   - Markers should wrap section content including AI blocks and diagrams
   - Ensure markers don't interfere with existing `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` markers

## Implementation Strategy

### Phase 1: Specification ✅
- Create spec.md with requirements
- Create contracts (ch3-rag-definition.yaml)
- Create research.md, data-model.md, checklists, quickstart.md

### Phase 2: Planning (Next)
- Create plan.md with architecture decisions
- Define chunking strategy
- Define embedding model selection
- Define Qdrant collection design
- Define retrieval pipeline flow

### Phase 3: Task Generation
- Create tasks.md with atomic tasks
- Group tasks by phase (chunking, embeddings, Qdrant, pipeline, MDX, settings)

### Phase 4: Implementation
- Update chapter_3_chunks.py with placeholder CH3_CHUNKS and TODO comments
- Add embed_chapter3_chunks() and normalize_chapter3_embeddings() to embedding_client.py
- Add Chapter 3 placeholders to qdrant_store.py
- Create ch3_pipeline.py with 5-step flow comments
- Add RAG-CHUNK markers to chapter-3.mdx
- Update settings.py with Chapter 3 config
- Update .env.example with Chapter 3 config

## Validation Steps

After implementation:

1. **Backend Import Validation**:
   ```bash
   cd backend
   python -c "from app.content.chapters.chapter_3_chunks import get_chapter_chunks; print('SUCCESS')"
   python -c "from app.ai.embeddings.embedding_client import embed_chapter3_chunks; print('SUCCESS')"
   python -c "from app.ai.rag.qdrant_store import similarity_search_ch3; print('SUCCESS')"
   python -c "from app.ai.rag.ch3_pipeline import run_ch3_rag_pipeline; print('SUCCESS')"
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
   grep QDRANT_COLLECTION_CH3 .env.example
   grep EMBEDDING_MODEL_CH3 .env.example
   ```

4. **File Existence Validation**:
   ```bash
   # Check all files exist
   ls backend/app/content/chapters/chapter_3_chunks.py
   ls backend/app/ai/embeddings/embedding_client.py
   ls backend/app/ai/rag/qdrant_store.py
   ls backend/app/ai/rag/ch3_pipeline.py
   ls frontend/docs/chapters/chapter-3.mdx
   ```

5. **MDX RAG Markers Validation**:
   ```bash
   # Check RAG-CHUNK markers exist
   grep "RAG-CHUNK" frontend/docs/chapters/chapter-3.mdx
   ```

## Success Criteria

- ✅ All Chapter 3 RAG scaffolding files exist
- ✅ No embeddings or Qdrant logic implemented (TODO only)
- ✅ Chapter 3 MDX contains RAG-CHUNK markers
- ✅ Backend starts successfully
- ✅ All imports resolve correctly

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
- Follows Chapter 2 RAG prep patterns for consistency.

