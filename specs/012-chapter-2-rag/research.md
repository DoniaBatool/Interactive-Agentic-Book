# Research: Chapter 2 RAG Chunking, Embeddings & Qdrant Collection Setup

**Feature**: 012-chapter-2-rag
**Date**: 2025-12-05
**Purpose**: Document RAG architecture patterns, chunking strategies, embedding models, and Qdrant collection design for Chapter 2

## Overview

This document captures research findings for building RAG foundations for Chapter 2 (ROS 2 Fundamentals). Research focuses on chunking strategies, embedding model selection, Qdrant collection design, and retrieval pipeline architecture. Since this is a scaffolding phase, research focuses on architectural patterns and placeholder design.

## Technology Decisions

### 1. Chunking Strategy: Multi-Phase Approach

**Decision**: Use placeholder logic phases (syntactic, semantic, hybrid) with TODO markers for future implementation

**Rationale**:
- **Flexibility**: Multiple chunking strategies can be evaluated during implementation
- **Content-Aware**: Different strategies for different content types (paragraphs, headings, code, glossary)
- **Section-Aware**: Respect section boundaries (H2 headings) for better context
- **Token-Aware**: Max token size constraints prevent context overflow

**Chunking Phases (TODO)**:
1. **Syntactic Chunking**: Split by paragraph boundaries, sentence boundaries
2. **Semantic Chunking**: Use semantic similarity to group related content
3. **Hybrid Chunking**: Combine syntactic and semantic approaches
4. **Heading-Aware**: Respect H2 section boundaries
5. **Overlapping Windows**: Overlap chunks for better context continuity

**Chunking Rules (TODO)**:
- Max token size: TBD (e.g., 512 tokens per chunk)
- Min chunk size: TBD (e.g., 50 tokens)
- Overlap: TBD (e.g., 50 tokens overlap between chunks)
- Section boundaries: Always start new chunk at H2 heading

**Alternatives Considered**:
- **Fixed-Size Chunks**: Too rigid, breaks semantic units
- **Sentence-Based**: Too granular, loses context
- **Paragraph-Based**: Good baseline, but may exceed token limits

### 2. Embedding Model Selection: OpenAI text-embedding-3-small

**Decision**: Use OpenAI text-embedding-3-small as default embedding model (configurable via env var)

**Rationale**:
- **Proven**: Widely used, well-documented
- **Cost-Effective**: Lower cost than text-embedding-3-large
- **Dimensions**: 1536 dimensions (good balance between quality and storage)
- **Token Limit**: 8191 tokens (sufficient for most chunks)
- **API Stability**: Stable API, good error handling

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

**Decision**: Create separate Qdrant collection for Chapter 2 ("chapter_2") with chapter-specific metadata

**Rationale**:
- **Isolation**: Each chapter has its own collection (easier management)
- **Scalability**: Can scale collections independently
- **Filtering**: Easy to filter by chapter_id
- **Metadata**: Chapter-specific metadata schema
- **Future-Proof**: Supports cross-chapter queries later

**Collection Schema**:
- **Name**: "chapter_2" (from QDRANT_COLLECTION_CH2 env var)
- **Vector Size**: 1536 (from embedding model dimensions)
- **Distance Metric**: Cosine similarity (default)
- **Index**: HNSW (fast approximate nearest neighbor search)

**Metadata Schema**:
```yaml
payload:
  text: str                     # Original text chunk
  chapter_id: int               # Chapter identifier (2)
  section_id: str               # Section identifier
  position: int                 # Position in chapter
  word_count: int               # Word count
  metadata:
    heading: str                # Section heading
    type: str                    # Content type
    has_diagram: bool            # Diagram flag
    has_ai_block: bool           # AI block flag
    ros2_concepts: List[str]     # ROS 2 concepts
```

**Alternatives Considered**:
- **Single Collection**: Simpler but harder to manage, requires filtering
- **Section-Based Collections**: Too granular, adds complexity
- **Topic-Based Collections**: Good for cross-chapter queries, but adds complexity

### 4. Retrieval Pipeline Flow: 5-Step Process

**Decision**: Use 5-step retrieval pipeline with placeholder flow for Chapter 2

**Rationale**:
- **Clear Separation**: Each step has distinct responsibility
- **Testable**: Each step can be tested independently
- **Extensible**: Easy to add new steps or modify existing ones
- **Error Handling**: Errors can be isolated to specific steps

**Pipeline Steps**:
1. **Load Chunks**: Retrieve Chapter 2 chunks from `chapter_2_chunks.py`
2. **Embed Query**: Generate embedding for user query
3. **Perform Search**: Vector similarity search in Qdrant collection
4. **Build Context**: Assemble retrieved chunks into context string
5. **Return Context**: Pass context to runtime engine for LLM prompts

**Context Assembly (TODO)**:
- Strategy: Concatenate chunks in order of similarity score
- Max Context: Configurable (default: 4 chunks from RAG_MAX_CONTEXT)
- Section Headers: Include section headers in context
- Metadata: Include chunk metadata in context string

**Alternatives Considered**:
- **Single-Step Pipeline**: Too monolithic, harder to test
- **Streaming Pipeline**: Good for real-time, but adds complexity
- **Cached Pipeline**: Good for performance, but adds cache management

### 5. Runtime Engine Integration: Context Flow

**Decision**: RAG pipeline returns context to runtime engine, which passes to subagents

**Rationale**:
- **Separation of Concerns**: RAG handles retrieval, runtime handles routing
- **Reusability**: Same RAG pipeline works for all AI blocks
- **Flexibility**: Subagents can use context differently
- **Testability**: Each component can be tested independently

**Context Flow**:
```
User Query
    ↓
Runtime Engine (run_ai_block)
    ↓
RAG Pipeline (run_rag_pipeline)
    ↓
Context (chunks + metadata)
    ↓
Runtime Engine
    ↓
Subagents (ask_question_agent, explain_el10_agent, etc.)
    ↓
LLM Provider (with context in prompt)
```

**Alternatives Considered**:
- **Direct Subagent Calls**: Bypasses runtime engine, breaks architecture
- **Embedded RAG**: RAG logic in subagents, reduces reusability
- **Separate RAG Service**: Overkill for current scale

## ROS 2 Specific Considerations

### ROS 2 Concepts

**Key Concepts**:
- Nodes: Individual processes in ROS 2 system
- Topics: Publish/subscribe communication
- Services: Request/response communication
- Actions: Long-running tasks with feedback
- Packages: Code organization units
- Launch Files: Multi-node coordination

**Chunking Implications**:
- Chunks should preserve concept boundaries
- Glossary terms need special handling
- Code examples should be kept intact
- Diagrams need metadata for context

### Section-Specific Retrieval

**Section IDs**:
- "introduction-to-ros2"
- "nodes-and-node-communication"
- "topics-and-messages"
- "services-and-actions"
- "ros2-packages"
- "launch-files-and-workflows"

**Retrieval Strategy**:
- If sectionId provided, filter chunks by section_id
- Prioritize chunks from relevant sections
- Include related sections for context

## Implementation Phases

### Phase 1: Scaffolding (Current Feature)
- Create placeholder functions
- Add TODO markers
- Define contracts and schemas
- No real implementation

### Phase 2: Chunking Implementation (Future)
- Implement chunking from MDX content
- Extract text from chapter-2.mdx
- Apply chunking rules
- Generate chunk metadata

### Phase 3: Embedding Integration (Future)
- Integrate OpenAI embeddings API
- Implement batch embedding
- Handle rate limiting
- Cache embeddings

### Phase 4: Qdrant Integration (Future)
- Set up Qdrant client
- Create collection
- Upsert vectors
- Implement similarity search

### Phase 5: Pipeline Integration (Future)
- Connect all pipeline steps
- Implement context assembly
- Add error handling
- Add logging

## Best Practices

### Chunking Best Practices
- Respect section boundaries (H2 headings)
- Preserve semantic units (paragraphs, code blocks)
- Handle special content (glossary, diagrams)
- Generate unique chunk IDs
- Include comprehensive metadata

### Embedding Best Practices
- Batch embeddings for efficiency
- Handle API rate limits
- Cache frequently embedded texts
- Validate input text length
- Handle API errors gracefully

### Qdrant Best Practices
- Use appropriate vector dimensions
- Configure HNSW index for performance
- Include filterable metadata
- Handle collection creation errors
- Validate vector structure

### Pipeline Best Practices
- Log each pipeline step
- Handle errors at each step
- Return partial results when possible
- Validate inputs and outputs
- Add performance monitoring

## Status

⚠️ **All research is theoretical. Real implementation will be added in future features.**
