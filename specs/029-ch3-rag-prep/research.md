# Research: Chapter 3 — RAG + Embedding Preparation Layer

**Feature**: 029-ch3-rag-prep
**Date**: 2025-01-27
**Purpose**: Document RAG architecture patterns, chunking strategies, embedding models, and Qdrant collection design for Chapter 3

## Overview

This document captures research findings for building RAG foundations for Chapter 3 (Physical AI Perception Systems). Research focuses on chunking strategies, embedding model selection, Qdrant collection design, and retrieval pipeline architecture. Since this is a scaffolding phase, research focuses on architectural patterns and placeholder design.

## Technology Decisions

### 1. Chunking Strategy: Multi-Phase Approach

**Decision**: Use placeholder logic phases (syntactic, semantic, hybrid) with TODO markers for future implementation

**Rationale**:
- **Flexibility**: Multiple chunking strategies can be evaluated during implementation
- **Content-Aware**: Different strategies for different content types (paragraphs, headings, code, glossary)
- **Section-Aware**: Respect section boundaries (H2 headings) for better context
- **Token-Aware**: Max token size constraints prevent context overflow
- **RAG-Marker-Aware**: Respect `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers from MDX

**Chunking Phases (TODO)**:
1. **Syntactic Chunking**: Split by paragraph boundaries, sentence boundaries
2. **Semantic Chunking**: Use semantic similarity to group related content
3. **Hybrid Chunking**: Combine syntactic and semantic approaches
4. **Heading-Aware**: Respect H2 section boundaries
5. **Overlapping Windows**: Overlap chunks for better context continuity
6. **RAG-Marker-Aware**: Respect RAG-CHUNK markers from MDX

**Chunking Rules (TODO)**:
- Max token size: TBD (e.g., 512 tokens per chunk)
- Min chunk size: TBD (e.g., 50 tokens)
- Overlap: TBD (e.g., 50 tokens overlap between chunks)
- Section boundaries: Always start new chunk at H2 heading
- RAG markers: Respect `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` boundaries

**Alternatives Considered**:
- **Fixed-Size Chunks**: Too rigid, breaks semantic units
- **Sentence-Based**: Too granular, loses context
- **Paragraph-Based**: Good baseline, but may exceed token limits

### 2. Embedding Model Selection: OpenAI text-embedding-3-small

**Decision**: Use OpenAI text-embedding-3-small as default embedding model for Chapter 3 (configurable via env var)

**Rationale**:
- **Proven**: Widely used, well-documented
- **Cost-Effective**: Lower cost than text-embedding-3-large
- **Dimensions**: 1536 dimensions (good balance between quality and storage)
- **Token Limit**: 8191 tokens (sufficient for most chunks)
- **API Stability**: Stable API, good error handling
- **Consistency**: Same model as Chapter 2 for consistency

**Model Specifications**:
- **Name**: text-embedding-3-small
- **Provider**: OpenAI
- **Dimensions**: 1536
- **Max Tokens**: 8191
- **Cost**: Lower than text-embedding-3-large
- **Quality**: Good for semantic search

**Alternatives Considered**:
- **text-embedding-3-large**: Higher quality but more expensive, 3072 dimensions (more storage)
- **Gemini Embeddings**: Good alternative, but OpenAI more established
- **Local Models**: Lower cost but lower quality, requires GPU

**Batching Strategy (TODO)**:
- Batch size: TBD (e.g., 100 chunks per batch)
- Rate limiting: Handle API rate limits
- Error handling: Retry failed batches
- Progress tracking: Log batch progress

### 3. Qdrant Collection Design: Chapter-Specific Collections

**Decision**: Create separate Qdrant collection for Chapter 3 ("chapter3") with chapter-specific metadata

**Rationale**:
- **Isolation**: Each chapter has its own collection (easier management)
- **Scalability**: Can scale collections independently
- **Filtering**: Easy to filter by chapter_id
- **Metadata**: Chapter-specific metadata schema (Physical AI concepts)
- **Future-Proof**: Supports cross-chapter queries later
- **Consistency**: Follows Chapter 2 pattern

**Collection Configuration**:
- **Name**: "chapter3" (from QDRANT_COLLECTION_CH3 env var)
- **Vector Dimension**: 1536 (for text-embedding-3-small)
- **Distance Metric**: Cosine similarity
- **Index**: HNSW (m, ef_construct parameters)

**Metadata Schema**:
```yaml
payload:
  text: str                     # Original text chunk
  chapter_id: int               # Chapter identifier (3)
  section_id: str               # Section identifier
  position: int                 # Position in chapter
  word_count: int               # Word count
  metadata:
    heading: str
    type: str
    has_diagram: bool
    has_ai_block: bool
    concepts: List[str]          # Physical AI concepts (e.g., ["perception", "sensors", "vision"])
    chunk_markers: bool          # True if chunk has RAG-CHUNK markers
```

**Alternatives Considered**:
- **Single Collection**: Simpler but harder to manage, less scalable
- **Topic-Based Collections**: More complex, requires topic classification

### 4. RAG Pipeline Architecture: Chapter-Specific Pipeline

**Decision**: Create separate pipeline file `ch3_pipeline.py` for Chapter 3 RAG operations

**Rationale**:
- **Modularity**: Separate pipeline per chapter (easier to maintain)
- **Chapter-Specific Logic**: Allows chapter-specific retrieval logic
- **Isolation**: Changes to one chapter don't affect others
- **Consistency**: Follows Chapter 2 pattern (if separate pipeline exists)

**Pipeline Flow (5 Steps)**:
1. **Retrieve Chunks**: Call `get_chapter_chunks(chapter_id=3)`
2. **Embed Query**: Call `generate_embedding(query, chapter_id=3)`
3. **Perform Search**: Call `similarity_search_ch3(query, top_k)`
4. **Construct Context**: Assemble retrieved chunks into context string
5. **Return Response**: Return context dictionary

**Alternatives Considered**:
- **Unified Pipeline**: Simpler but less flexible, harder to customize per chapter
- **Dynamic Routing**: More complex, requires routing logic

### 5. MDX RAG Markers: Complementary to Existing Markers

**Decision**: Add `<!-- RAG-CHUNK: start -->` and `<!-- RAG-CHUNK: end -->` markers to Chapter 3 MDX

**Rationale**:
- **Explicit Boundaries**: Clear chunk boundaries for RAG pipeline
- **Complementary**: Works alongside existing `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` markers
- **Flexibility**: Allows fine-grained control over chunk boundaries
- **Future-Proof**: Supports future chunking strategies

**Marker Usage**:
- Wrap section content including AI blocks and diagrams
- Define future chunk boundaries for RAG pipeline
- Complement existing chunk markers

**Alternatives Considered**:
- **Only Existing Markers**: Simpler but less flexible
- **No Markers**: More flexible but less explicit

## Industry References

### RAG Architecture Patterns

1. **LangChain RAG Pattern**: Retrieve → Embed → Search → Context → LLM
2. **LlamaIndex RAG Pattern**: Index → Query → Retrieve → Generate
3. **Haystack RAG Pattern**: Document Store → Retriever → Reader → Generator

### Chunking Best Practices

1. **Semantic Chunking**: Group related content by meaning
2. **Heading-Aware**: Respect document structure
3. **Token-Aware**: Respect model token limits
4. **Overlapping Windows**: Improve context continuity

### Embedding Model Selection

1. **OpenAI text-embedding-3-small**: 1536 dimensions, cost-effective
2. **OpenAI text-embedding-3-large**: 3072 dimensions, higher quality
3. **Gemini Embeddings**: Alternative to OpenAI

### Qdrant Collection Design

1. **Chapter-Specific Collections**: Isolation and scalability
2. **Metadata Schema**: Rich metadata for filtering and search
3. **Vector Dimensions**: Match embedding model dimensions

## Observations

1. **Chapter 3 Content**: Physical AI Perception Systems (sensors, computer vision, signal processing)
2. **Concepts**: Perception, sensors, computer vision, depth perception, signal processing, feature extraction
3. **Sections**: 7 sections (What Is Perception, Types of Sensors, Computer Vision, Signal Processing, Feature Extraction, Learning Objectives, Glossary)
4. **AI Blocks**: 4 AI blocks (ask-question, generate-diagram, explain-like-i-am-10, interactive-quiz)
5. **Diagrams**: 4 diagram placeholders (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)

## Implementation Notes

1. **Scaffolding Only**: No real RAG logic implemented in this feature
2. **Placeholder Functions**: All functions return empty lists/dicts
3. **TODO Comments**: Comprehensive TODO comments for future implementation
4. **Pattern Consistency**: Follows Chapter 2 RAG prep patterns
5. **Future Integration**: Ready for future RAG runtime integration

