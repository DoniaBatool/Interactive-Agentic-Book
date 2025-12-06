# Research Notes: Chapter 2 — RAG Chunking, Embedding Prep & Knowledge Source Scaffolding

**Feature**: 021-ch2-rag-prep
**Date**: 2025-12-05

## Problem Context

This feature establishes the RAG preparation layer for Chapter 2, including chunk markers in MDX, chunking strategy documentation, and RAG pipeline integration hooks. The goal is to prepare Chapter 2 content for future RAG operations (embedding generation, vector storage, semantic search) without implementing actual RAG logic.

## Technology Decisions

### 1. Chunk Marker Format

**Decision**: Use numbered format `<!-- CHUNK: x -->` for Chapter 2

**Rationale**:
- Simpler than START/END pairs (used in Chapter 3)
- Easier to validate with regex pattern
- Clear sequential numbering
- Matches requirements specification

**Alternatives Considered**:
- START/END pairs (like Chapter 3): More explicit but more verbose
- Section-based markers: Less granular control

**Trade-offs**:
- Numbered format is simpler but requires careful placement
- START/END pairs are more explicit but require pairing validation

---

### 2. Chunk Size Guidelines

**Decision**: 120-220 words per chunk

**Rationale**:
- Optimal for embedding quality (not too small, not too large)
- Balances semantic meaning with token limits
- Allows for meaningful context in RAG retrieval
- Matches industry best practices

**Alternatives Considered**:
- 50-100 words: Too small, loses context
- 300-500 words: Too large, exceeds token limits

**Trade-offs**:
- Smaller chunks: Better precision but less context
- Larger chunks: More context but less precision

---

### 3. Semantic Grouping Strategy

**Decision**: Group by semantic topic, not paragraph count

**Rationale**:
- Preserves semantic meaning
- Better embedding quality
- More relevant RAG retrieval
- Respects concept boundaries

**Alternatives Considered**:
- Paragraph-based: Simpler but breaks semantic meaning
- Fixed-size chunks: Easier but loses context

**Trade-offs**:
- Semantic grouping: Better quality but more complex
- Fixed-size: Simpler but less effective

---

### 4. Chunking Blueprint Location

**Decision**: Update existing `chapter_2_chunks.py` file (from Feature 012)

**Rationale**:
- File already exists with function signature
- Avoids duplication
- Maintains consistency
- Matches Feature 012 structure

**Alternatives Considered**:
- Create new file: Would duplicate existing structure
- Separate chunking file: Unnecessary complexity

**Trade-offs**:
- Update existing: Maintains consistency but requires careful merging
- Create new: Cleaner but duplicates code

---

### 5. RAG Pipeline Integration

**Decision**: Add TODO hooks to existing `pipeline.py` file

**Rationale**:
- Pipeline file already exists (from Feature 005)
- Maintains single source of truth
- Clear integration points
- No breaking changes

**Alternatives Considered**:
- Separate Chapter 2 pipeline: Would duplicate logic
- New pipeline module: Unnecessary complexity

**Trade-offs**:
- Add hooks to existing: Maintains consistency but requires careful placement
- Separate pipeline: Cleaner but duplicates code

---

## Industry References

### RAG Chunking Best Practices

1. **Semantic Chunking**: Group related content together for better embedding quality
2. **Size Guidelines**: 100-200 words per chunk is optimal for most embedding models
3. **Boundary Respect**: Respect section boundaries and concept boundaries
4. **Metadata Inclusion**: Include section context, headings, and position for better retrieval

### Embedding Preparation

1. **Token Limits**: Most embedding models have 512-8191 token limits
2. **Batch Processing**: Process chunks in batches for efficiency
3. **Metadata Preservation**: Preserve chunk metadata for filtering and context

### Vector Database Preparation

1. **Collection Naming**: Use consistent naming convention (chapter_2)
2. **Metadata Schema**: Define metadata schema for filtering
3. **Indexing Strategy**: Plan for efficient semantic search

---

## Observations

### Key Points

1. **Chunk Markers**: Numbered format is simpler and easier to validate
2. **Chunk Size**: 120-220 words balances context and precision
3. **Semantic Grouping**: Grouping by topic preserves meaning
4. **Integration Hooks**: TODO hooks prepare for future implementation

### Challenges

1. **Chunk Placement**: Determining optimal chunk boundaries requires content understanding
2. **Marker Validation**: Ensuring markers follow regex pattern
3. **Metadata Alignment**: Ensuring chunk metadata matches MDX structure

### Technical Considerations

1. **MDX Build Stability**: Chunk markers must not break MDX compilation
2. **Import Stability**: All Python files must import cleanly
3. **No Breaking Changes**: Existing functionality must continue to work

---

## Technology Stack

- **MDX**: Markdown with JSX for content structure
- **Python**: Backend chunking and RAG pipeline
- **Regex**: Chunk marker validation
- **Qdrant**: Future vector database (not implemented in this feature)

---

## Next Steps

1. **Planning Phase**: Create architecture plan for chunking strategy
2. **Tasks Phase**: Generate atomic tasks for implementation
3. **Implementation Phase**: Add chunk markers and update files
4. **Validation Phase**: Verify MDX builds and imports work

---

## Notes

- This feature focuses on **scaffolding only** - no actual RAG logic
- Chunk markers prepare content for future embedding generation
- Chunking strategy documentation guides future implementation
- RAG pipeline hooks prepare for future integration
