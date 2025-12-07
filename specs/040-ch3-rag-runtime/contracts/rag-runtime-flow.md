# RAG + Runtime Flow Contract: Chapter 3

**Feature**: 040-ch3-rag-runtime
**Created**: 2025-01-27
**Status**: Draft

## Overview

This contract defines the high-level RAG (Retrieval-Augmented Generation) flow for Chapter 3. The flow orchestrates chunking, embedding generation, Qdrant storage, similarity search, and context assembly for Physical AI Perception Systems knowledge. All steps are placeholders with TODO markers—no real logic implemented.

## RAG Flow

```
Chapter 3 MDX Content
    │
    ▼
Chapter 3 Chunking (chapter_3_chunks.py)
    │ (TODO: Implement chunking)
    ▼
Chapter 3 Chunks (List[Dict])
    │
    ▼
Embedding Generation (embedding_client.py)
    │ (TODO: generate_embedding for chapter_id=3)
    ▼
Embedding Vectors (List[List[float]])
    │
    ▼
Qdrant Storage (qdrant_store.py)
    │ (TODO: create_collection, upsert_vectors for "chapter_3")
    ▼
Qdrant Collection "chapter_3"
    │
    ▼
User Query
    │
    ▼
RAG Pipeline (pipeline.py)
    │
    ├─► Step 1: Load chapter chunks
    │   └─► get_chapter_chunks(chapter_id=3)
    │
    ├─► Step 2: Embed query
    │   └─► generate_embedding(query, chapter_id=3)
    │
    ├─► Step 3: Search Qdrant
    │   └─► similarity_search(collection="chapter_3", query_embedding, top_k)
    │
    ├─► Step 4: Prepare context
    │   └─► Assemble retrieved chunks into context string
    │
    └─► Step 5: Pass into AI runtime
        └─► Return context to runtime engine
            │
            ▼
Runtime Engine (engine.py)
    │ (chapterId=3 → use Chapter 3 routing)
    ▼
Subagents (ch3_*_agent.py - future)
    │
    ▼
LLM Provider
    │
    ▼
Response
```

## Step 1: Load Chapter Chunks

**Function**: `get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]`

**Purpose**: Retrieve Chapter 3 content chunks for embedding and storage

**Input**: chapter_id (default: 3)

**Output**: List of chunk dictionaries with metadata

**TODO**: Implement chunking from Chapter 3 MDX content

---

## Step 2: Embed Query

**Function**: `generate_embedding(text: str, chapter_id: int = 3) -> List[float]`

**Purpose**: Generate embedding vector for user query

**Input**: text (query string), chapter_id (3)

**Output**: Embedding vector (List[float])

**TODO**: Implement embedding generation using CH3_EMBEDDING_MODEL

---

## Step 3: Search Qdrant

**Function**: `similarity_search(collection_name: str, query: str, top_k: int) -> List[Dict]`

**Purpose**: Perform semantic search in Chapter 3 collection

**Input**: collection_name ("chapter_3"), query (text or embedding), top_k (default: 5)

**Output**: List of similar documents with scores

**TODO**: Implement Qdrant similarity search for Chapter 3 collection

---

## Step 4: Prepare Context

**Function**: Assemble context string from retrieved chunks

**Purpose**: Build retrieval context for LLM prompts

**Input**: Retrieved chunks from Step 3

**Output**: Context string with chunk metadata

**TODO**: Implement context assembly with chunk metadata

---

## Step 5: Runtime Engine Routing

**Function**: `run_ai_block(block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]`

**Purpose**: Route Chapter 3 AI block requests to appropriate subagents

**Input**: block_type, request_data (with chapterId=3)

**Output**: Formatted response for frontend

**TODO**: Implement Chapter 3 routing in runtime engine

---

## Summary

This contract defines the complete RAG + runtime flow for Chapter 3. All steps are placeholders with TODO markers—no real logic implemented. The flow follows Chapter 2 RAG integration patterns exactly.

