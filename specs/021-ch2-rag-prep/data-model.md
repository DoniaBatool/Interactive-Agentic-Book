# Data Model: Chapter 2 — RAG Chunking, Embedding Prep & Knowledge Source Scaffolding

**Feature**: 021-ch2-rag-prep
**Date**: 2025-12-05
**Purpose**: Define data structures and entities for Chapter 2 RAG preparation system

## Entity Definitions

### 1. Chunk Marker (Primary Entity)

**Description**: A marker for RAG chunk boundaries in Chapter 2 MDX content

**Storage**: MDX file as HTML comment

**Structure**:
```html
<!-- CHUNK: 1 -->
<!-- CHUNK: 2 -->
<!-- CHUNK: 3 -->
```

**Attributes**:
- **Number**: Sequential chunk number (1, 2, 3, ...)
- **Section**: Section where chunk marker appears
- **Position**: Position within section
- **Format**: Must match regex `<!-- CHUNK: [0-9]+ -->`

**Validation Rules**:
- MUST follow regex pattern: `<!-- CHUNK: [0-9]+ -->`
- MUST be placed before logical paragraph groups
- Expected count: 6-8 markers total
- MUST respect H2 section boundaries

**Relationships**:
- **Parent**: Section (1:N - one section can have multiple chunk markers)
- **Order**: Sequential within section

---

### 2. Chunk Blueprint (Primary Entity)

**Description**: Documentation and TODO structure for Chapter 2 chunking strategy

**Storage**: `backend/app/content/chapters/chapter_2_chunks.py`

**Structure**:
```python
def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 2 with metadata.
    
    TODO: Chunk size rules: 120-220 words per chunk
    TODO: Semantic grouping: group by topic, not paragraph count
    TODO: Embedding guidelines: prepare for future embedding generation
    TODO: Retrieval linking: prepare for future RAG ingestion
    """
    return []
```

**Attributes**:
- **Function Name**: `get_chapter_chunks`
- **Parameters**: `chapter_id: int = 2`
- **Return Type**: `List[Dict[str, Any]]`
- **TODO Comments**: Chunk size rules, semantic grouping, embedding guidelines, retrieval linking

**Validation Rules**:
- Function MUST exist with correct signature
- Function MUST import cleanly
- TODO comments MUST be descriptive

**Relationships**:
- **Used By**: RAG pipeline (future integration)
- **References**: MDX chunk markers

---

### 3. RAG Pipeline Hook (Primary Entity)

**Description**: TODO handlers for Chapter 2 RAG operations in pipeline

**Storage**: `backend/app/ai/rag/pipeline.py`

**Structure**:
```python
# TODO: Register Chapter 2 collection name
# TODO: Use CH2_COLLECTION_NAME from ch2_collection.py

# TODO: Prepare chapter-specific embedding batch for Chapter 2
# TODO: Use batch_embed_ch2() from embedding_client.py

# TODO: Placeholder search function for Chapter 2
# TODO: Use search() from ch2_collection.py
```

**Attributes**:
- **Type**: TODO comment handlers
- **Purpose**: Collection registration, embedding batch, search function
- **Location**: `pipeline.py` file

**Validation Rules**:
- TODO handlers MUST be descriptive
- File MUST import cleanly
- No breaking changes to existing functionality

**Relationships**:
- **References**: ch2_collection.py (future)
- **References**: embedding_client.py (future)
- **Used By**: Runtime engine (future)

---

### 4. Chunk Metadata (Future Entity)

**Description**: Metadata structure for Chapter 2 chunks (future implementation)

**Structure**:
```python
{
    "id": str,                    # Unique chunk ID (e.g., "ch2-s1-c0")
    "text": str,                  # Chunk text content
    "chapter_id": 2,              # Chapter identifier
    "section_id": str,            # Section identifier
    "position": int,              # Position in chapter (0-based)
    "word_count": int,            # Word count
    "metadata": {                 # Additional metadata
        "heading": str,          # Section heading
        "type": str,             # "paragraph", "heading", "glossary", etc.
        "has_diagram": bool,     # True if section has diagram placeholder
        "has_ai_block": bool     # True if section has AI block
    }
}
```

**Note**: This structure is documented but not implemented in this feature.

---

## Data Relationships

```
MDX File (chapter-2.mdx)
    │
    ├─► Chunk Markers (<!-- CHUNK: x -->)
    │   └─► Chunk Blueprint (chapter_2_chunks.py)
    │       └─► RAG Pipeline Hooks (pipeline.py)
    │
    ├─► Diagram Placeholders (<!-- DIAGRAM: ... -->)
    │   └─► Preserved in chunking
    │
    └─► AI-Block Components (<AskQuestionBlock ... />)
        └─► Preserved in chunking
```

---

## Data Flow

### Current Scaffolding Flow

```
1. MDX File
   └─► Chunk Markers Added
       └─► Chunk Blueprint Updated
           └─► RAG Pipeline Hooks Added
               └─► Validation Passes
```

### Future Implementation Flow

```
1. MDX File
   └─► Extract Chunks (using markers)
       └─► Generate Embeddings
           └─► Store in Qdrant
               └─► Enable Semantic Search
```

---

## Validation Summary

### Chunk Marker Validation

- Format: `<!-- CHUNK: [0-9]+ -->`
- Count: 6-8 markers
- Placement: Before logical paragraph groups
- Section alignment: Respects H2 boundaries

### Chunk Blueprint Validation

- Function exists: `get_chapter_chunks(chapter_id=2)`
- Imports cleanly: No errors
- TODO comments: Descriptive and complete

### RAG Pipeline Validation

- TODO hooks exist: Collection registration, embedding batch, search function
- Imports cleanly: No errors
- No breaking changes: Existing functionality works

---

## Notes

- All entities are **scaffolding only** - no actual implementation
- Chunk metadata structure is documented for future use
- Data relationships show integration points
- Validation rules ensure correctness
