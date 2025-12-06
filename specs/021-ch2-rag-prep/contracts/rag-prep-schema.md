# RAG Preparation Schema Contract for Chapter 2

**Feature**: 021-ch2-rag-prep
**Created**: 2025-12-05
**Status**: Draft

## Overview

This contract defines the RAG preparation schema for Chapter 2, including chunk marker format, placeholder contracts, embedding boundaries, and retrieval context rules.

---

## Chunk Marker Contract

### Format

**Location**: `frontend/docs/chapters/chapter-2.mdx` within sections

**Marker Format**:
```html
<!-- CHUNK: 1 -->
<!-- CHUNK: 2 -->
<!-- CHUNK: 3 -->
...
```

**Validation Rules**:
- Chunk markers MUST follow regex pattern: `<!-- CHUNK: [0-9]+ -->`
- Chunk markers MUST be placed before logical paragraph groups
- Chunk markers MUST respect H2 section boundaries
- Chunk numbers can be sequential (1, 2, 3, ...) or restart per section
- Expected count: 6-8 chunk markers total across all sections

**Placement Strategy**:
- Place markers before major concept blocks
- Group related paragraphs together
- Avoid breaking glossary entries
- Link diagram explanations with adjacent text
- Respect semantic topic boundaries

**Chunk Size Guidelines**:
- Target: 120-220 words per chunk
- Group by semantic topic, not paragraph count
- Avoid breaking glossary entries
- Link diagram explanations with adjacent text

---

## Placeholder Contract

### Diagram Placeholders

**Format**: HTML comment in MDX file
```html
<!-- DIAGRAM: ros2-ecosystem-overview -->
<!-- DIAGRAM: node-communication-architecture -->
<!-- DIAGRAM: topic-pubsub-flow -->
<!-- DIAGRAM: services-actions-comparison -->
```

**Validation Rules**:
- MUST use kebab-case naming
- MUST be preserved when adding chunk markers
- MUST align with metadata `diagram_placeholders` list

**Diagram Names** (4 total):
1. ros2-ecosystem-overview
2. node-communication-architecture
3. topic-pubsub-flow
4. services-actions-comparison

---

### AI-Block Placeholders

**Format**: React components in MDX file
```jsx
<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />
<ExplainLike10Block concept="topics" chapterId={2} />
<InteractiveQuizBlock chapterId={2} numQuestions={5} />
<GenerateDiagramBlock diagramType="node-communication-architecture" chapterId={2} />
```

**Validation Rules**:
- MUST be preserved when adding chunk markers
- MUST align with metadata `ai_blocks` list
- MUST have correct chapterId={2}

**AI-Block Types** (4 total):
1. ask-question
2. explain-like-i-am-10
3. interactive-quiz
4. generate-diagram

---

## Embedding Boundaries

### Chunk Size Rules

**Target Size**: 120-220 words per chunk

**Constraints**:
- Minimum: 50 words (to maintain semantic meaning)
- Maximum: 300 words (to avoid token limits)
- Optimal: 150-200 words (for best embedding quality)

**Token Limits**:
- Max tokens per chunk: 512 tokens (for text-embedding-3-small)
- Account for metadata overhead
- Reserve space for chunk ID and section context

---

### Semantic Boundaries

**Grouping Strategy**:
- Group by semantic topic, not paragraph count
- Each H2 section is a natural chunk boundary
- Respect concept boundaries (don't split related ideas)
- Avoid breaking glossary entries
- Link diagram explanations with adjacent text

**Boundary Rules**:
- H2 section headings mark natural boundaries
- Diagram placeholders mark visual content boundaries
- AI-block components mark interactive content boundaries
- Glossary entries should be grouped as single chunks

---

## Retrieval Context Rules

### Context Assembly

**Chunk Selection**:
- Select top-k most relevant chunks (default: 5)
- Prioritize chunks from same section when sectionId provided
- Include chunk metadata (section_id, heading, position)
- Limit total context size (RAG_MAX_CONTEXT env var, default: 4 chunks)

**Context Format**:
```yaml
context:
  text: str                    # Assembled context string
  chunks: List[Dict]          # Retrieved chunks with metadata
  query_embedding: List[float] # Query embedding vector
```

**Metadata Inclusion**:
- Section ID for source attribution
- Heading for context clarity
- Position for ordering
- Word count for size tracking
- Diagram/AI-block flags for special handling

---

### Retrieval Linking (Future)

**Future Integration Points**:
- Link chunks to source MDX sections
- Track chunk relationships (parent/child)
- Support cross-chunk references
- Enable chunk versioning

**Future RAG Ingestion Steps**:
1. Extract chunks from MDX using markers
2. Generate embeddings for each chunk
3. Store embeddings in Qdrant collection "chapter_2"
4. Index chunk metadata for filtering
5. Enable semantic search across chunks

---

## Section Structure Schema

**Format**: Markdown H2 headings in MDX file
**Location**: `frontend/docs/chapters/chapter-2.mdx`

**Required Sections** (exactly 7):
1. `## Introduction to ROS 2 {#introduction-to-ros2}`
2. `## Nodes and Node Communication {#nodes-and-node-communication}`
3. `## Topics and Messages {#topics-and-messages}`
4. `## Services and Actions {#services-and-actions}`
5. `## ROS 2 Packages {#ros2-packages}`
6. `## Launch Files and Workflows {#launch-files-and-workflows}`
7. `## Glossary {#glossary}`

**Validation Rules**:
- MUST have exactly 7 H2 sections
- Section IDs MUST match metadata `sections` list
- Section order MUST match metadata
- All sections MUST have chunk markers

---

## Chunking Blueprint Contract

### Function Signature

**File**: `backend/app/content/chapters/chapter_2_chunks.py`

**Function**: `get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]`

**Expected Structure**:
```python
def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 2 with metadata.
    
    TODO: Implement chunking from Chapter 2 MDX content
    TODO: Use chunk markers (<!-- CHUNK: x -->) to identify boundaries
    TODO: Chunk size rules: 120-220 words per chunk
    TODO: Semantic grouping: group by topic, not paragraph count
    TODO: Embedding guidelines: prepare for future embedding generation
    TODO: Retrieval linking: prepare for future RAG ingestion
    """
    return []
```

---

### Chunking Strategy Documentation

**Required TODO Comments**:
1. **Chunk size rules**: 120-220 words per chunk
2. **Semantic grouping**: Group by semantic topic, not paragraph count
3. **Embedding guidelines**: Prepare for future embedding generation
4. **Retrieval linking**: Prepare for future RAG ingestion

**Implementation Notes**:
- Use chunk markers to identify boundaries
- Respect H2 section boundaries
- Group related paragraphs together
- Avoid breaking glossary entries
- Link diagram explanations with adjacent text

---

## RAG Pipeline Integration Contract

### Collection Registration

**File**: `backend/app/ai/rag/pipeline.py`

**TODO Handler**:
```python
# TODO: Register Chapter 2 collection name
# TODO: Use CH2_COLLECTION_NAME from ch2_collection.py
# TODO: Collection name: "chapter_2" (from QDRANT_COLLECTION_CH2 env var)
```

---

### Embedding Batch Preparation

**File**: `backend/app/ai/rag/pipeline.py`

**TODO Handler**:
```python
# TODO: Prepare chapter-specific embedding batch for Chapter 2
# TODO: Use batch_embed_ch2() from embedding_client.py
# TODO: Process chunks in batches (e.g., 100 chunks per batch)
# TODO: Use CH2_EMBEDDING_MODEL for Chapter 2 embeddings
```

---

### Search Function Placeholder

**File**: `backend/app/ai/rag/pipeline.py`

**TODO Handler**:
```python
# TODO: Placeholder search function for Chapter 2
# TODO: Use search() from ch2_collection.py
# TODO: Perform semantic search in "chapter_2" collection
# TODO: Return top-k most relevant chunks
```

---

## Validation Rules Summary

1. **Chunk Markers**:
   - MUST follow regex: `<!-- CHUNK: [0-9]+ -->`
   - MUST be placed before logical paragraph groups
   - Expected count: 6-8 markers

2. **MDX Structure**:
   - MUST build successfully after markers are added
   - MUST have exactly 7 H2 sections
   - Section count MUST match metadata

3. **Chunk File**:
   - MUST import cleanly
   - MUST have function `get_chapter_chunks(chapter_id=2)`
   - MUST have TODO comments on chunking strategy

4. **RAG Pipeline**:
   - MUST have TODO hooks for Chapter 2
   - MUST not break existing functionality
   - MUST import cleanly

---

## Future RAG Ingestion Steps

1. **Extract Chunks**: Use chunk markers to extract chunks from MDX
2. **Generate Embeddings**: Use embedding model to generate vectors
3. **Store in Qdrant**: Upsert embeddings into "chapter_2" collection
4. **Index Metadata**: Store chunk metadata for filtering
5. **Enable Search**: Perform semantic search across chunks

---

## Notes

- This contract defines the **scaffolding** for RAG preparation
- No actual chunking, embedding, or RAG logic is implemented
- All rules are designed to be testable and validatable
- Future implementation will follow this contract
