# Implementation Plan: Chapter 2 — RAG Chunking, Embedding Prep & Knowledge Source Scaffolding

**Branch**: `021-ch2-rag-prep` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/021-ch2-rag-prep/spec.md`

## Summary

This feature establishes the complete RAG preparation layer for Chapter 2 by adding chunk markers to MDX content, updating the chunking blueprint file with enhanced TODO comments, adding RAG pipeline integration hooks, and documenting contracts for chunk markers, embedding boundaries, and retrieval context rules. **No actual chunking, embedding, or RAG logic is implemented**—only scaffolding, chunk markers, TODO placeholders, and architectural blueprints to prepare for future RAG implementation.

**Primary Deliverable**: Complete RAG preparation scaffolding for Chapter 2 (chunk markers in MDX, enhanced chunking blueprint, RAG pipeline hooks, contracts)
**Validation**: MDX builds successfully, chunk markers follow regex pattern, all files import cleanly, section counts match metadata

## Technical Context

**Language/Version**:
- Frontend: MDX (Markdown + JSX) compatible with Docusaurus 3.x
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- Frontend: Docusaurus 3.x (already installed)
- Backend: FastAPI 0.109+, Pydantic 2.x (already installed)
- Feature 005 (AI Runtime Engine): RAG pipeline file must exist
- Feature 012 (Chapter 2 RAG): Chunk file may already exist
- Feature 014 (Chapter 2 Content): MDX file must exist
- Feature 020 (Chapter 2 AI Runtime): RAG collection scaffolding exists

**Storage**: 
- Static files (MDX content, Python modules) - no database
- Future: Qdrant for Chapter 2 vectors, embedding cache

**Testing**:
- Manual: MDX build verification, chunk marker validation, import resolution, backend startup
- Frontend: `npm run build` validation (Docusaurus build process)
- Backend: Python import test (`python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks"`)

**Target Platform**:
- Frontend: Web browsers via Docusaurus static site
- Backend: FastAPI server (localhost:8000)

**Project Type**: RAG preparation scaffolding (frontend MDX markers + backend chunking blueprint + RAG pipeline hooks)

**Performance Goals**:
- MDX build time: Incremental build < 5 seconds
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement actual chunking logic (only markers and TODO comments)
- MUST maintain compatibility with Feature 014 (Chapter 2 Content must still work)
- MUST use numbered chunk marker format: `<!-- CHUNK: x -->` (not START/END pairs)
- MUST follow regex pattern: `<!-- CHUNK: [0-9]+ -->`
- MUST preserve existing diagram and AI-block markers
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality

**Scale/Scope**:
- 1 MDX file to update (chapter-2.mdx)
- 1 backend chunk file to update (chapter_2_chunks.py)
- 1 RAG pipeline file to update (pipeline.py)
- 1 contract file already created (rag-prep-schema.md)
- ~6-8 chunk markers to add
- ~50-100 lines of scaffolding code (mostly markers, TODOs, and comments)

---

## 1. High-Level Architecture Overview

The RAG preparation layer for Chapter 2 establishes the foundation for future chunking, embedding generation, and semantic search. It adds chunk markers to MDX content to identify semantic boundaries, documents chunking strategy in the chunking blueprint file, and adds integration hooks to the RAG pipeline for Chapter 2 operations.

### Architecture Flow

```
Chapter 2 MDX Content (chapter-2.mdx)
    │
    ├─► Chunk Markers Added (<!-- CHUNK: x -->)
    │   └─► 6-8 markers before logical paragraph groups
    │
    ├─► Diagram Placeholders Preserved (<!-- DIAGRAM: ... -->)
    │
    └─► AI-Block Components Preserved (<AskQuestionBlock ... />)
        │
        ▼
Chunking Blueprint (chapter_2_chunks.py)
    │
    ├─► Enhanced TODO Comments
    │   ├─► Chunk size rules (120-220 words)
    │   ├─► Semantic grouping strategy
    │   ├─► Embedding guidelines
    │   └─► Retrieval linking (future)
    │
    └─► Function: get_chapter_chunks(chapter_id=2)
        │
        ▼
RAG Pipeline Integration (pipeline.py)
    │
    ├─► TODO: Register Chapter 2 collection name
    ├─► TODO: Prepare chapter-specific embedding batch
    └─► TODO: Placeholder search function for Chapter 2
        │
        ▼
Future RAG Implementation
    ├─► Extract chunks using markers
    ├─► Generate embeddings
    ├─► Store in Qdrant collection "chapter_2"
    └─► Enable semantic search
```

### Component Responsibilities

1. **MDX Chunk Markers**: Identify semantic boundaries in Chapter 2 content for future chunking
2. **Chunking Blueprint**: Document chunking strategy and provide function signature for future implementation
3. **RAG Pipeline Hooks**: Prepare integration points for Chapter 2 RAG operations
4. **Contracts**: Document chunk marker format, embedding boundaries, and retrieval rules

### Data Flow

1. **Chunk Marker Placement**: MDX content → Chunk markers identify boundaries
2. **Chunking Strategy Documentation**: Chunk markers → Chunking blueprint documents strategy
3. **RAG Integration Preparation**: Chunking blueprint → RAG pipeline hooks prepare integration
4. **Future Implementation**: Chunk markers → Extract chunks → Generate embeddings → Store in Qdrant → Enable search

---

## 2. MDX Layer

### 2.1 Semantic Section Identification

**Decision**: Identify ~6-8 semantic sections in Chapter 2 MDX for chunk marker placement

**Rationale**:
- Chapter 2 has 7 H2 sections (from metadata)
- Each section can have 1-2 logical chunks
- Total expected: 6-8 chunk markers
- Chunk markers placed before major concept blocks

**Section Analysis** (from `chapter-2.mdx`):

1. **Introduction to ROS 2** (`#introduction-to-ros2`)
   - Content: Definition, differences from ROS 1, examples
   - Chunk marker: `<!-- CHUNK: 1 -->` before content placeholder
   - Has diagram: `ros2-ecosystem-overview`
   - Has AI-block: `AskQuestionBlock`

2. **Nodes and Node Communication** (`#nodes-and-node-communication`)
   - Content: Node explanation, communication, lifecycle, examples
   - Chunk marker: `<!-- CHUNK: 2 -->` before content placeholder
   - Has diagram: `node-communication-architecture`
   - Has AI-block: `GenerateDiagramBlock`

3. **Topics and Messages** (`#topics-and-messages`)
   - Content: Topics, publish/subscribe, message types, examples
   - Chunk marker: `<!-- CHUNK: 3 -->` before content placeholder
   - Has diagram: `topic-pubsub-flow`
   - Has AI-block: `ExplainLike10Block`

4. **Services and Actions** (`#services-and-actions`)
   - Content: Services, actions, differences, when to use each
   - Chunk marker: `<!-- CHUNK: 4 -->` before content placeholder
   - Has diagram: `services-actions-comparison`
   - Has AI-block: `InteractiveQuizBlock`

5. **ROS 2 Packages** (`#ros2-packages`)
   - Content: Package structure, dependencies, organization
   - Chunk marker: `<!-- CHUNK: 5 -->` before content placeholder
   - No diagram or AI-block

6. **Launch Files and Workflows** (`#launch-files-and-workflows`)
   - Content: Launch files, starting nodes, workflows, patterns
   - Chunk marker: `<!-- CHUNK: 6 -->` before content placeholder
   - No diagram or AI-block

7. **Glossary** (`#glossary`)
   - Content: 7 glossary terms with definitions
   - Chunk marker: `<!-- CHUNK: 7 -->` before content placeholder (glossary as single chunk)
   - No diagram or AI-block

**Total Chunk Markers**: 7 markers (one per section)

**Note**: If sections have multiple logical chunks, additional markers can be added (e.g., `<!-- CHUNK: 1 -->`, `<!-- CHUNK: 1a -->`), but for simplicity, we'll use one marker per section initially.

---

### 2.2 Chunk Marker Placement Strategy

**Decision**: Place chunk markers before logical paragraph groups, preserving existing placeholders

**Placement Rules**:
1. Place `<!-- CHUNK: x -->` before content placeholder in each section
2. Preserve existing `<!-- DIAGRAM: ... -->` markers
3. Preserve existing AI-block React components
4. Ensure markers follow regex: `<!-- CHUNK: [0-9]+ -->`
5. Respect H2 section boundaries (one marker per section minimum)

**Example Placement** (for Section 1):
```markdown
## Introduction to ROS 2 {#introduction-to-ros2}

<!-- CHUNK: 1 -->
<!-- Content placeholder: Definition of ROS 2, why ROS 2 exists, differences from ROS 1, and at least 3 real-world examples of ROS 2 usage (TurtleBot 3, navigation stack, etc.). Use post office analogy for communication system. Min 200 words, 7th-8th grade level. -->

<!-- DIAGRAM: ros2-ecosystem-overview -->

<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />
```

**Validation Rules**:
- Chunk markers MUST follow regex: `<!-- CHUNK: [0-9]+ -->`
- Chunk markers MUST be placed before content placeholders
- Existing diagram markers MUST be preserved
- Existing AI-block components MUST be preserved
- Section count MUST match metadata (7 sections)

---

### 2.3 Placeholder Alignment Validation

**Decision**: Validate that chunk markers align with existing placeholders and metadata

**Validation Checks**:
1. **Section Count**: MDX has exactly 7 H2 sections (matches metadata)
2. **Diagram Placeholders**: 4 diagram markers exist (matches metadata)
3. **AI-Block Components**: 4 AI-block components exist (matches metadata)
4. **Chunk Markers**: 6-8 chunk markers added (one per section minimum)
5. **Metadata Alignment**: Section IDs match metadata `sections` list

**Metadata Reference** (from `chapter_2.py`):
```python
"sections": [
    "Introduction to ROS 2",
    "Nodes and Node Communication",
    "Topics and Messages",
    "Services and Actions",
    "ROS 2 Packages",
    "Launch Files and Workflows",
    "Glossary"
]
```

**Validation Process**:
1. Count H2 sections in MDX → Should be 7
2. Count diagram placeholders → Should be 4
3. Count AI-block components → Should be 4
4. Count chunk markers → Should be 6-8
5. Verify section IDs match metadata → All must match

---

## 3. Chunking Rules

### 3.1 Chunk Size Guidelines

**Decision**: Chunk size target of 120-220 words per chunk

**Rationale**:
- Optimal for embedding quality (not too small, not too large)
- Balances semantic meaning with token limits
- Allows for meaningful context in RAG retrieval
- Matches industry best practices

**Size Constraints**:
- **Minimum**: 50 words (to maintain semantic meaning)
- **Maximum**: 300 words (to avoid token limits)
- **Optimal**: 150-200 words (for best embedding quality)
- **Token Limit**: 512 tokens per chunk (for text-embedding-3-small)

**Implementation Notes** (TODO in chunking blueprint):
- TODO: Implement chunk size validation (120-220 words)
- TODO: Split large chunks if they exceed 300 words
- TODO: Merge small chunks if they are below 50 words
- TODO: Account for metadata overhead in token count

---

### 3.2 Semantic Grouping Strategy

**Decision**: Group by semantic topic, not paragraph count

**Rationale**:
- Preserves semantic meaning
- Better embedding quality
- More relevant RAG retrieval
- Respects concept boundaries

**Grouping Rules**:
1. **Group by Topic**: Related paragraphs should be in same chunk
2. **Respect Section Boundaries**: H2 sections are natural chunk boundaries
3. **Preserve Concept Units**: Don't split related ideas across chunks
4. **Avoid Breaking Glossary**: Glossary entries should be grouped as single chunks
5. **Link Diagram Explanations**: Diagram explanations should be in adjacent chunks

**Implementation Notes** (TODO in chunking blueprint):
- TODO: Group paragraphs by semantic topic
- TODO: Respect H2 section boundaries
- TODO: Preserve concept units (don't split related ideas)
- TODO: Group glossary entries together
- TODO: Link diagram explanations with adjacent text

---

### 3.3 Glossary Handling

**Decision**: Avoid breaking glossary entries; group as single chunks

**Rationale**:
- Glossary entries are self-contained definitions
- Breaking entries loses context
- Single chunk per glossary entry maintains semantic meaning

**Glossary Chunking Strategy**:
- Each glossary term should be in its own chunk (if large enough)
- Or group related terms together (if small)
- Minimum chunk size: 50 words per glossary entry
- Maximum chunk size: 300 words for grouped entries

**Implementation Notes** (TODO in chunking blueprint):
- TODO: Group glossary entries as single chunks
- TODO: Don't split glossary entries across chunks
- TODO: Maintain glossary entry integrity

---

### 3.4 Diagram Explanation Linking

**Decision**: Link diagram explanations with adjacent text

**Rationale**:
- Diagram explanations need context from surrounding text
- Adjacent chunks provide better context for diagrams
- Improves RAG retrieval for diagram-related queries

**Linking Strategy**:
- Include diagram explanation in same chunk as related text
- Or place in adjacent chunk with cross-reference
- Maintain diagram-to-text relationship

**Implementation Notes** (TODO in chunking blueprint):
- TODO: Link diagram explanations with adjacent text
- TODO: Include diagram context in chunks
- TODO: Maintain diagram-to-text relationships

---

## 4. Backend Chunk Module

### 4.1 Chunking Blueprint File Structure

**File**: `backend/app/content/chapters/chapter_2_chunks.py`

**Status**: File already exists (from Feature 012), needs enhancement

**Current Structure** (from existing file):
```python
def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 2 with metadata.
    
    TODO: Implement chunking from Chapter 2 MDX content
    TODO: Load Chapter 2 content from frontend/docs/chapters/chapter-2.mdx
    TODO: Implement chunking strategy:
        - Max token size constraints (e.g., 512 tokens per chunk)
        - Semantic segmentation by section
        - Heading-aware slicing (respect H2 boundaries)
        - Overlapping window strategy (e.g., 50 tokens overlap)
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch2-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Cache chunks for performance
    TODO: Include ROS 2-specific metadata (concepts: nodes, topics, services, actions)
    """
    return []
```

**Enhancement Required**: Add TODO comments on:
1. Chunk size rules (120-220 words)
2. Semantic grouping (group by topic, not paragraph count)
3. Embedding guidelines (future embedding generation)
4. Retrieval linking (future RAG ingestion)

---

### 4.2 Enhanced TODO Comments

**Decision**: Add comprehensive TODO comments for chunking strategy

**Enhanced Function Structure**:
```python
def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 2 with metadata.
    
    Args:
        chapter_id: Chapter identifier (default: 2 for Chapter 2)
    
    Returns:
        List of chunk dictionaries with structure:
        [
            {
                "id": str,                    # Unique chunk ID (e.g., "ch2-s1-c0")
                "text": str,                  # Chunk text content
                "chapter_id": 2,              # Chapter identifier
                "section_id": str,            # Section identifier (e.g., "introduction-to-ros2")
                "position": int,              # Position in chapter (0-based)
                "word_count": int,            # Word count
                "metadata": {                 # Additional metadata
                    "heading": str,          # Section heading
                    "type": str,             # "paragraph", "heading", "glossary", etc.
                    "has_diagram": bool,     # True if section has diagram placeholder
                    "has_ai_block": bool     # True if section has AI block
                }
            },
            ...
        ]
    
    Chunking Strategy (TODO):
    1. Chunk Size Rules:
       - Target: 120-220 words per chunk
       - Minimum: 50 words (to maintain semantic meaning)
       - Maximum: 300 words (to avoid token limits)
       - Token limit: 512 tokens per chunk (for text-embedding-3-small)
       - TODO: Implement chunk size validation
       - TODO: Split large chunks if they exceed 300 words
       - TODO: Merge small chunks if they are below 50 words
    
    2. Semantic Grouping:
       - Group by semantic topic, not paragraph count
       - Respect H2 section boundaries
       - Preserve concept units (don't split related ideas)
       - TODO: Group paragraphs by semantic topic
       - TODO: Respect H2 section boundaries
       - TODO: Preserve concept units
    
    3. Special Content Handling:
       - Avoid breaking glossary entries (group as single chunks)
       - Link diagram explanations with adjacent text
       - TODO: Group glossary entries as single chunks
       - TODO: Link diagram explanations with adjacent text
    
    4. Chunk Marker Usage:
       - Use chunk markers (<!-- CHUNK: x -->) to identify boundaries
       - Maintain order of chunks
       - TODO: Extract chunks using chunk markers
       - TODO: Maintain chunk order
    
    5. Embedding Guidelines (Future):
       - Prepare chunks for embedding generation
       - Include metadata for embedding context
       - TODO: Prepare chunks for embedding generation
       - TODO: Include metadata for embedding context
    
    6. Retrieval Linking (Future):
       - Prepare chunks for RAG ingestion
       - Include section context for retrieval
       - TODO: Prepare chunks for RAG ingestion
       - TODO: Include section context for retrieval
    
    TODO: Implement chunking from Chapter 2 MDX content
    TODO: Load Chapter 2 content from frontend/docs/chapters/chapter-2.mdx
    TODO: Use chunk markers (<!-- CHUNK: x -->) to identify boundaries
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch2-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Cache chunks for performance
    TODO: Include ROS 2-specific metadata (concepts: nodes, topics, services, actions)
    """
    # Placeholder return - no real chunking implementation
    return []
```

---

### 4.3 Function Signature

**Decision**: Keep existing function signature `get_chapter_chunks(chapter_id: int = 2)`

**Rationale**:
- Function already exists from Feature 012
- Signature is consistent with Chapter 1 and Chapter 3
- No breaking changes needed

**Function Signature**:
```python
def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 2 with metadata.
    
    Uses chunk markers (<!-- CHUNK: x -->) in MDX to identify boundaries.
    Maintains order and aligns with RAG ingestion requirements.
    
    Returns:
        List of chunk dictionaries with id, text, chapter_id, section_id,
        position, word_count, and metadata fields.
    """
    return []
```

---

## 5. RAG Pipeline Integration

### 5.1 Collection Name Registration

**File**: `backend/app/ai/rag/pipeline.py`

**Decision**: Add TODO handler for registering Chapter 2 collection name

**Current Structure** (from existing file):
```python
async def run_rag_pipeline(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> Dict[str, Any]:
    """
    Execute RAG pipeline: retrieve → embed → search → context → LLM.
    
    TODO: Chapter 2 specific flow (when chapter_id=2):
        - Step 1: Call get_chapter_chunks(chapter_id=2) to retrieve Chapter 2 chunks
        - Step 2: Call generate_embedding(query) to embed user query
        - Step 3: Call similarity_search(collection="chapter_2", query_embedding, top_k) to find relevant chunks
        - Step 4: Assemble retrieved chunks into context string with metadata
        - Step 5: Return context to runtime engine for LLM prompts
    
    TODO: Ensure pipeline resolves chapter_2_chunks when chapter_id=2
    TODO: Chapter 2 chunks are loaded from app.content.chapters.chapter_2_chunks
    TODO: Chapter 2 collection name is "chapter_2" (from QDRANT_COLLECTION_CH2 env var)
    """
    return {
        "context": "",
        "chunks": [],
        "query_embedding": []
    }
```

**Enhancement Required**: Add TODO handler for Chapter 2 collection name registration

**Enhanced TODO Comments**:
```python
# TODO: Register Chapter 2 collection name
# TODO: Use CH2_COLLECTION_NAME from ch2_collection.py
# TODO: Collection name: "chapter_2" (from QDRANT_COLLECTION_CH2 env var)
# TODO: from app.ai.rag.collections.ch2_collection import CH2_COLLECTION_NAME
# TODO: Register collection name when chapter_id=2
```

---

### 5.2 Embedding Batch Preparation

**File**: `backend/app/ai/rag/pipeline.py`

**Decision**: Add TODO handler for preparing chapter-specific embedding batch

**Enhanced TODO Comments**:
```python
# TODO: Prepare chapter-specific embedding batch for Chapter 2
# TODO: Use batch_embed_ch2() from embedding_client.py
# TODO: Process chunks in batches (e.g., 100 chunks per batch)
# TODO: Use CH2_EMBEDDING_MODEL for Chapter 2 embeddings
# TODO: from app.ai.embeddings.embedding_client import batch_embed_ch2
# TODO: Prepare embedding batch when chapter_id=2
```

---

### 5.3 Local Retrieval Context Builder

**File**: `backend/app/ai/rag/pipeline.py`

**Decision**: Add TODO placeholder search function for Chapter 2

**Enhanced TODO Comments**:
```python
# TODO: Placeholder search function for Chapter 2
# TODO: Use search() from ch2_collection.py
# TODO: Perform semantic search in "chapter_2" collection
# TODO: Return top-k most relevant chunks
# TODO: from app.ai.rag.collections.ch2_collection import search
# TODO: Build retrieval context from search results
# TODO: Assemble context string with chunk metadata
```

---

## 6. Contracts & Validation

### 6.1 RAG Prep Schema Contract

**File**: `specs/021-ch2-rag-prep/contracts/rag-prep-schema.md`

**Status**: Already created in spec phase

**Content**: Complete contract with:
- Chunk marker contract (format, validation rules, placement strategy)
- Placeholder contract (diagram, AI-block markers)
- Embedding boundaries (chunk size rules, semantic boundaries)
- Retrieval context rules (context assembly, metadata inclusion)
- Chunking blueprint contract (function signature, chunking strategy documentation)
- RAG pipeline integration contract (collection registration, embedding batch, search function)
- Validation rules summary

**Validation**: Contract is complete and comprehensive

---

### 6.2 Regex Rules for Markers

**Contract Section**: Chunk Marker Contract

**Regex Pattern**: `<!-- CHUNK: [0-9]+ -->`

**Validation Rules**:
- MUST follow regex pattern: `<!-- CHUNK: [0-9]+ -->`
- MUST be placed before logical paragraph groups
- Expected count: 6-8 markers total
- MUST respect H2 section boundaries

**Implementation**: Regex validation in contract file

---

### 6.3 Embedding Boundary Rules

**Contract Section**: Embedding Boundaries

**Chunk Size Rules**:
- Target: 120-220 words per chunk
- Minimum: 50 words
- Maximum: 300 words
- Token limit: 512 tokens per chunk

**Semantic Boundaries**:
- Group by semantic topic, not paragraph count
- Respect H2 section boundaries
- Preserve concept units
- Avoid breaking glossary entries
- Link diagram explanations with adjacent text

**Implementation**: Rules documented in contract file

---

### 6.4 RAG Ingestion Steps (Future)

**Contract Section**: Future RAG Ingestion Steps

**Steps Documented**:
1. Extract chunks using chunk markers
2. Generate embeddings for each chunk
3. Store embeddings in Qdrant collection "chapter_2"
4. Index chunk metadata for filtering
5. Enable semantic search across chunks

**Implementation**: Steps documented in contract file for future reference

---

## 7. Integration Points

### 7.1 Feature 005 (AI Runtime Engine)

**Integration**: RAG pipeline file exists from Feature 005

**Changes**: Add TODO hooks for Chapter 2 in existing `pipeline.py` file

**Compatibility**: No breaking changes, only TODO comments added

---

### 7.2 Feature 012 (Chapter 2 RAG)

**Integration**: Chunk file exists from Feature 012

**Changes**: Enhance existing `chapter_2_chunks.py` with additional TODO comments

**Compatibility**: No breaking changes, only TODO comments enhanced

---

### 7.3 Feature 014 (Chapter 2 Content)

**Integration**: MDX file exists from Feature 014

**Changes**: Add chunk markers to existing `chapter-2.mdx` file

**Compatibility**: No breaking changes, only markers added (preserve existing content)

---

### 7.4 Feature 020 (Chapter 2 AI Runtime)

**Integration**: RAG collection scaffolding exists from Feature 020

**Changes**: Reference CH2_COLLECTION_NAME in pipeline TODO comments

**Compatibility**: No breaking changes, only references added

---

## 8. Acceptance Checks

### 8.1 MDX Build Validation

**Check**: MDX file builds successfully after chunk markers are added

**Validation**: Run `npm run build` in frontend directory

**Expected**: Build succeeds without errors

---

### 8.2 Chunk Marker Validation

**Check**: Chunk markers follow regex pattern `<!-- CHUNK: [0-9]+ -->`

**Validation**: Manual review or regex validation script

**Expected**: All markers match regex pattern

---

### 8.3 Section Count Validation

**Check**: Section count matches metadata (7 sections)

**Validation**: Count H2 sections in MDX, compare with metadata

**Expected**: Exactly 7 sections match metadata

---

### 8.4 Import Validation

**Check**: All Python files import cleanly

**Validation**: Run `python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks"`

**Expected**: Import succeeds without errors

---

### 8.5 Placeholder Preservation

**Check**: Existing diagram and AI-block markers are preserved

**Validation**: Manual review of MDX file

**Expected**: All existing placeholders remain intact

---

## 9. Next Steps

1. **Tasks Phase**: Generate atomic tasks for implementation
2. **Implementation Phase**: Add chunk markers, update files, add TODO hooks
3. **Validation Phase**: Verify MDX builds, chunk markers valid, imports work
4. **Future Features**: Implement actual chunking, embedding, and RAG logic

---

## 10. Risk Analysis

### 10.1 MDX Build Failure

**Risk**: Adding chunk markers might break MDX compilation

**Mitigation**: Test MDX build after each marker addition, preserve existing structure

**Impact**: Low (markers are HTML comments, shouldn't affect MDX)

---

### 10.2 Chunk Marker Format Errors

**Risk**: Chunk markers might not follow regex pattern

**Mitigation**: Validate markers with regex before committing, document format clearly

**Impact**: Low (format is simple, easy to validate)

---

### 10.3 Import Errors

**Risk**: Enhanced TODO comments might cause import errors

**Mitigation**: Test imports after each file update, ensure syntax is correct

**Impact**: Low (TODO comments are just strings, shouldn't affect imports)

---

## 11. Summary

This plan establishes the RAG preparation layer for Chapter 2 by:

1. **MDX Layer**: Adding 6-8 chunk markers before logical paragraph groups, preserving existing placeholders
2. **Chunking Rules**: Documenting chunk size (120-220 words), semantic grouping, glossary handling, diagram linking
3. **Backend Chunk Module**: Enhancing `chapter_2_chunks.py` with comprehensive TODO comments on chunking strategy
4. **RAG Pipeline Integration**: Adding TODO hooks for Chapter 2 collection registration, embedding batch, and search function
5. **Contracts & Validation**: Using existing `rag-prep-schema.md` contract with regex rules, embedding boundaries, and RAG ingestion steps

**No actual chunking, embedding, or RAG logic is implemented**—only scaffolding, markers, TODO placeholders, and architectural blueprints to prepare for future RAG implementation.

**Plan complete — ready for /sp.tasks.**
