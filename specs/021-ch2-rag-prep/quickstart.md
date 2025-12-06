# Quickstart: Chapter 2 — RAG Chunking, Embedding Prep & Knowledge Source Scaffolding

**Feature**: 021-ch2-rag-prep
**Created**: 2025-12-05

## Prerequisites

- Feature 005 (AI Runtime Engine): RAG pipeline file must exist
- Feature 012 (Chapter 2 RAG): Chunk file may already exist
- Feature 014 (Chapter 2 Content): MDX file must exist
- Feature 020 (Chapter 2 AI Runtime): RAG collection scaffolding exists

## Commands

```bash
# Specification phase
/sp.specify

# Planning phase
/sp.plan

# Tasks phase
/sp.tasks

# Implementation phase
/sp.implement
```

## Folder Structure

```
specs/021-ch2-rag-prep/
├── spec.md
├── plan.md (future)
├── tasks.md (future)
├── contracts/
│   └── rag-prep-schema.md
├── checklists/
│   └── requirements.md
├── research.md
├── data-model.md
└── quickstart.md

frontend/docs/chapters/
└── chapter-2.mdx (to be updated)

backend/app/content/chapters/
└── chapter_2_chunks.py (to be updated)

backend/app/ai/rag/
└── pipeline.py (to be updated)
```

## Feature Overview

This feature establishes the RAG preparation layer for Chapter 2 by:

1. **Adding Chunk Markers**: Insert `<!-- CHUNK: x -->` markers in MDX file
2. **Updating Chunk Blueprint**: Enhance `chapter_2_chunks.py` with chunking strategy documentation
3. **Adding RAG Hooks**: Add TODO handlers to `pipeline.py` for Chapter 2
4. **Creating Contracts**: Document chunk marker contract, embedding boundaries, retrieval rules

## Key Files to Create/Modify

### Files to Update

1. `frontend/docs/chapters/chapter-2.mdx`
   - Add chunk markers before logical paragraph groups
   - Preserve existing diagram and AI-block markers

2. `backend/app/content/chapters/chapter_2_chunks.py`
   - Enhance TODO comments on chunking strategy
   - Document chunk size rules (120-220 words)
   - Document semantic grouping strategy

3. `backend/app/ai/rag/pipeline.py`
   - Add TODO handler for Chapter 2 collection registration
   - Add TODO handler for Chapter 2 embedding batch
   - Add TODO placeholder search function for Chapter 2

### Files to Create

1. `specs/021-ch2-rag-prep/contracts/rag-prep-schema.md`
   - Document chunk marker contract
   - Document placeholder contract
   - Document embedding boundaries
   - Document retrieval context rules

## Implementation Steps

### Step 1: Add Chunk Markers to MDX

1. Open `frontend/docs/chapters/chapter-2.mdx`
2. Insert `<!-- CHUNK: 1 -->` before first logical paragraph group
3. Insert `<!-- CHUNK: 2 -->` before second logical paragraph group
4. Continue for 6-8 chunk markers total
5. Ensure markers follow regex: `<!-- CHUNK: [0-9]+ -->`
6. Preserve existing diagram and AI-block markers

### Step 2: Update Chunk Blueprint

1. Open `backend/app/content/chapters/chapter_2_chunks.py`
2. Enhance TODO comments on:
   - Chunk size rules (120-220 words)
   - Semantic grouping (group by topic)
   - Embedding guidelines (future)
   - Retrieval linking (future)

### Step 3: Add RAG Pipeline Hooks

1. Open `backend/app/ai/rag/pipeline.py`
2. Add TODO handler for Chapter 2 collection registration
3. Add TODO handler for Chapter 2 embedding batch
4. Add TODO placeholder search function for Chapter 2

### Step 4: Validate

1. Build frontend: `npm run build` (should succeed)
2. Test imports: `python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks"`
3. Verify chunk markers: Check regex pattern
4. Verify section count: Should match metadata (7 sections)

## Success Criteria

- ✅ Chapter 2 MDX contains properly structured chunk markers (6-8 markers)
- ✅ Chunk markers follow regex pattern `<!-- CHUNK: [0-9]+ -->`
- ✅ Chunk schema contract documented in `rag-prep-schema.md`
- ✅ `chapter_2_chunks.py` scaffold updated with enhanced TODO comments
- ✅ RAG pipeline updated with TODO hooks for Chapter 2
- ✅ MDX builds successfully after markers are added
- ✅ All files import cleanly
- ✅ No business logic implemented (scaffolding only)

## Troubleshooting

### MDX Build Fails

**Problem**: MDX file doesn't compile after adding chunk markers

**Solution**:
- Check chunk marker format (must match regex)
- Ensure markers are valid HTML comments
- Verify no syntax errors in MDX file

### Import Errors

**Problem**: `chapter_2_chunks.py` doesn't import

**Solution**:
- Check function signature
- Verify no syntax errors
- Ensure proper type hints

### Chunk Markers Not Valid

**Problem**: Chunk markers don't follow regex pattern

**Solution**:
- Verify format: `<!-- CHUNK: [0-9]+ -->`
- Check spacing and capitalization
- Ensure numbers are sequential

## Next Steps

After completing this feature:

1. **Planning Phase**: Create architecture plan for chunking strategy
2. **Tasks Phase**: Generate atomic tasks for implementation
3. **Implementation Phase**: Add chunk markers and update files
4. **Future Features**: Implement actual chunking, embedding, and RAG logic

## Resources

- **Specification**: `specs/021-ch2-rag-prep/spec.md`
- **Contract**: `specs/021-ch2-rag-prep/contracts/rag-prep-schema.md`
- **Research**: `specs/021-ch2-rag-prep/research.md`
- **Data Model**: `specs/021-ch2-rag-prep/data-model.md`
