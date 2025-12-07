# Research: Chapter 2 RAG + Embeddings + Runtime Integration

**Feature**: 035-ch2-rag-integration
**Date**: 2025-01-27
**Purpose**: Document integration approach for enabling RAG infrastructure for Chapter 2 using existing patterns

## Overview

This document captures research findings for integrating RAG infrastructure (embeddings, Qdrant storage, retrieval pipeline) into Chapter 2 (Mechanical Systems) using the existing patterns from Chapter 3 RAG prep (Feature 029). Since this is a scaffolding phase, research focuses on integration patterns, embedding strategies, and Qdrant collection design.

## Technology Decisions

### 1. Follow Chapter 3 RAG Prep Patterns

**Decision**: Reuse all RAG infrastructure patterns from Feature 029 (Chapter 3 RAG prep)

**Rationale**:
- **Consistency**: Same architecture across all chapters
- **Efficiency**: No need to recreate patterns or infrastructure
- **Maintainability**: Single source of truth for RAG functionality
- **Proven Pattern**: Chapter 3 integration already tested

**Integration Approach**:
- Create Chapter 2-specific files following Chapter 3 naming conventions
- Use same function signatures and placeholder patterns
- Follow same TODO comment structure
- Maintain same directory structure

**Alternatives Considered**:
- **New Patterns**: Unnecessary duplication, breaks consistency
- **Separate Architecture**: Adds complexity, same functionality needed
- **Different Naming**: Overkill, existing naming works well

### 2. Embedding Model Selection: Configurable via ENV

**Decision**: Use configurable embedding model via EMBEDDING_MODEL_CH2 environment variable

**Rationale**:
- **Flexibility**: Can switch models without code changes
- **Cost Control**: Can use different models for different chapters
- **Future-Proof**: Easy to add new models

**Model Options** (TODO):
- OpenAI text-embedding-3-small (1536 dimensions)
- OpenAI text-embedding-3-large (3072 dimensions)
- Gemini embeddings
- Local models (sentence-transformers)

### 3. Qdrant Collection Design: Chapter-Specific Collections

**Decision**: Create separate Qdrant collection for Chapter 2 ("chapter_2") with chapter-specific metadata

**Rationale**:
- **Isolation**: Each chapter has its own collection (easier management)
- **Scalability**: Can scale collections independently
- **Filtering**: Easy to filter by chapter_id
- **Metadata**: Chapter-specific metadata schema (Mechanical Systems concepts)

**Collection Name**: "chapter_2" (from QDRANT_COLLECTION_CH2 env var)

### 4. Chunking Strategy: Placeholder with TODO

**Decision**: Use placeholder chunking function with TODO comments for future implementation

**Rationale**:
- **Flexibility**: Multiple chunking strategies can be evaluated during implementation
- **Content-Aware**: Different strategies for different content types
- **Section-Aware**: Respect section boundaries (H2 headings)
- **Token-Aware**: Max token size constraints prevent context overflow

**Chunking Approaches** (TODO):
- Section-based (H2 headings)
- Paragraph-based
- Semantic chunking (overlapping windows)
- Hybrid approach

---

## Integration Patterns

### Pattern 1: Embedding → Qdrant → Pipeline Flow

All Chapter 2 RAG operations follow this pattern:
1. Chunks loaded from chapter_2_chunks.py
2. Chunks embedded using ch2_embedding_client.py
3. Embeddings stored in Qdrant using ch2_qdrant_store.py
4. Queries embedded and searched using ch2_pipeline.py
5. Context returned to runtime engine

### Pattern 2: Runtime Engine Integration

Runtime engine routes Chapter 2 requests:
1. Runtime engine identifies chapterId=2
2. Calls ch2_pipeline.run_ch2_rag_pipeline()
3. Pipeline returns context
4. Context passed to Chapter 2 subagents
5. Subagents use context in LLM prompts

---

## References

- Feature 029: Chapter 3 RAG Prep (reference pattern)
- Feature 034: Chapter 2 AI Blocks Integration (subagents exist)
- Feature 033: Chapter 2 Content (content source)

---

## Summary

This research establishes:
- Reuse Chapter 3 RAG prep patterns for consistency
- Configurable embedding model via ENV
- Chapter-specific Qdrant collections
- Placeholder chunking with TODO comments

**Key Principles**:
- Consistency with Chapter 3 patterns
- Scalability for future chapters
- Clear separation of chapter-specific logic
- Scaffolding-only approach (no business logic)

