# Runtime Overview: Chapter 3

**Chapter**: 3 — Physical AI Perception Systems  
**Date**: 2025-01-27  
**Status**: Scaffolding Complete

## Runtime Structure Tree

### Backend Runtime Structure

```
backend/app/
├── ai/
│   ├── providers/          # LLM provider integrations (placeholder)
│   ├── rag/                 # RAG pipeline components
│   │   ├── pipeline.py      # RAG pipeline orchestration (Chapter 3 branch)
│   │   └── qdrant_store.py  # Qdrant vector database operations
│   ├── embeddings/          # Embedding client
│   │   └── embedding_client.py  # Embedding generation (Chapter 3 support)
│   ├── subagents/            # Chapter-specific subagents
│   │   ├── base_agent.py    # Base agent interface
│   │   └── ch3/              # Chapter 3 subagents
│   │       ├── ask_question_agent.py
│   │       ├── explain_el10_agent.py
│   │       ├── quiz_agent.py
│   │       └── diagram_agent.py
│   ├── skills/               # Reusable skills
│   │   ├── base_skill.py    # Base skill interface
│   │   └── ch3/              # Chapter 3 skills
│   │       ├── retrieval_skill.py
│   │       ├── prompt_builder_skill.py
│   │       └── formatting_skill.py
│   └── runtime/              # Runtime engine
│       └── engine.py        # Unified AI block runtime (Chapter 3 routing)
├── content/
│   └── chapters/
│       ├── chapter_3.py     # Chapter 3 metadata
│       └── chapter_3_chunks.py  # Chapter 3 RAG chunks (placeholder)
└── api/
    └── ai_blocks.py         # AI block API endpoints (Chapter 3 support)
```

---

## Module Responsibilities

### Runtime Engine (`app/ai/runtime/engine.py`)

**Responsibilities**:
- Unified entry point for all AI block requests
- Routes requests to appropriate Chapter 3 subagents
- Coordinates RAG pipeline for Chapter 3 context retrieval
- Selects LLM provider based on configuration
- Formats responses for frontend

**Chapter 3 Routing**:
- Detects `chapterId=3` in request
- Routes to Chapter 3 subagents (Ch3AskQuestionAgent, Ch3ExplainEl10Agent, Ch3QuizAgent, Ch3DiagramAgent)
- Calls RAG pipeline with `chapter_id=3`
- Returns formatted response

**Status**: Scaffolding complete, placeholder routing in place

---

### RAG Pipeline (`app/ai/rag/pipeline.py`)

**Responsibilities**:
- Orchestrates Retrieval-Augmented Generation pipeline
- Retrieves Chapter 3 content chunks
- Embeds user queries
- Performs Qdrant similarity search
- Constructs retrieval context

**Chapter 3 Integration**:
- `run_rag_pipeline(query, chapter_id=3, top_k=5)` - Chapter 3 branch
- Uses Chapter 3 collection name: "chapter_3" (from QDRANT_COLLECTION_CH3 env var)
- Retrieves chunks from `chapter_3_chunks.py`
- Returns context for LLM prompts

**Status**: Scaffolding complete, Chapter 3 branch in place

---

### Embedding Client (`app/ai/embeddings/embedding_client.py`)

**Responsibilities**:
- Generates text embeddings for semantic search
- Supports chapter-specific embedding models
- Batch embedding generation

**Chapter 3 Support**:
- `generate_embedding(text, chapter_id=3)` - Chapter 3 embedding
- Uses CH3_EMBEDDING_MODEL when `chapter_id=3` (from settings)
- `batch_embed_ch3(chunks)` - Batch embedding for Chapter 3

**Status**: Scaffolding complete, Chapter 3 support in place

---

### Qdrant Store (`app/ai/rag/qdrant_store.py`)

**Responsibilities**:
- Qdrant vector database operations
- Collection creation
- Vector upsert operations
- Similarity search

**Chapter 3 Support**:
- `create_collection("chapter_3")` - Create Chapter 3 collection
- `upsert_vectors("chapter_3", vectors)` - Upsert Chapter 3 vectors
- `similarity_search("chapter_3", query, top_k)` - Search Chapter 3 collection

**Status**: Scaffolding complete, Chapter 3 support in place

---

## AI Runtime Components

### Chapter 3 Subagents

**Location**: `backend/app/ai/subagents/ch3/`

**Subagents**:
1. **Ch3AskQuestionAgent** (`ask_question_agent.py`)
   - Answers questions about Physical AI concepts
   - Uses Chapter 3 RAG context
   - Returns formatted answer with source citations

2. **Ch3ExplainEl10Agent** (`explain_el10_agent.py`)
   - Generates simplified explanations (age 10 level)
   - Uses Physical AI analogies
   - Returns explanation with analogies and examples

3. **Ch3QuizAgent** (`quiz_agent.py`)
   - Generates interactive quiz questions
   - Covers learning objectives
   - Returns quiz with questions, answers, explanations

4. **Ch3DiagramAgent** (`diagram_agent.py`)
   - Generates visual diagrams for Physical AI concepts
   - Supports 4 diagram types (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
   - Returns diagram description/JSON

**Base Interface**: All subagents inherit from `BaseAgent` (abstract class)

**Status**: Scaffolding complete, placeholder logic in place

---

### Chapter 3 Skills

**Location**: `backend/app/ai/skills/ch3/`

**Skills**:
1. **Ch3RetrievalSkill** (`retrieval_skill.py`)
   - RAG context pulling for Chapter 3
   - `retrieve_content(query, chapter_id=3, top_k=5)`
   - `retrieve_by_section(section_id, chapter_id=3)`

2. **Ch3PromptBuilderSkill** (`prompt_builder_skill.py`)
   - LLM prompt building for Chapter 3
   - `build_prompt(block_type, request_data, context)`
   - Block-specific prompt builders (ask-question, eli10, quiz, diagram)

3. **Ch3FormattingSkill** (`formatting_skill.py`)
   - Structured response formatting for Chapter 3
   - `format_response(response, block_type)`
   - Block-specific formatters (ask-question, eli10, quiz, diagram)

**Base Interface**: All skills inherit from `BaseSkill` (abstract class)

**Status**: Scaffolding complete, placeholder logic in place

---

## RAG Pipeline Overview

### Chapter 3 RAG Integration

**Flow**:
1. User query received (e.g., "What is perception in Physical AI?")
2. Query embedded using CH3_EMBEDDING_MODEL (if configured)
3. Similarity search in "chapter_3" Qdrant collection
4. Top-k chunks retrieved (e.g., top 5 most relevant chunks)
5. Context assembled for LLM with chunk metadata
6. LLM generates response with Physical AI context
7. Response returned to user with source citations

### Chunk Source

**File**: `backend/app/content/chapters/chapter_3_chunks.py`

**Function**: `get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]`

**Status**: Scaffolding complete, placeholder function in place

**Future Implementation**:
- Load Chapter 3 MDX content
- Chunk by section (H2 boundaries)
- Generate embeddings
- Store in Qdrant collection "chapter_3"

### Collection Configuration

**Collection Name**: "chapter_3" (from QDRANT_COLLECTION_CH3 env var)

**Vector Size**: 1536 (for text-embedding-3-small)

**Distance Metric**: Cosine similarity

**Status**: Scaffolding complete, collection name configured

---

## Subagents/Skills Overview

### Subagent Structure

**Base Class**: `BaseAgent` (abstract)
- Defines `run(request: Dict[str, Any]) -> Dict[str, Any]` method
- All Chapter 3 subagents inherit from BaseAgent

**Chapter 3 Subagents**:
- All in `backend/app/ai/subagents/ch3/` folder
- All have `run()` method with placeholder logic
- All return placeholder responses

### Skill Structure

**Base Class**: `BaseSkill` (abstract)
- Defines basic placeholder interface
- All Chapter 3 skills inherit from BaseSkill

**Chapter 3 Skills**:
- All in `backend/app/ai/skills/ch3/` folder
- All have method stubs with placeholder logic
- All return placeholder values

### Runtime Engine Integration

**Routing**:
- Runtime engine detects `chapterId=3`
- Maps block_type to Ch3*Agent classes
- Calls subagent.run() with request_data + context
- Returns formatted response

**Status**: Scaffolding complete, placeholder routing in place

---

## Configuration

### Environment Variables

**Chapter 3 RAG**:
- `QDRANT_COLLECTION_CH3="chapter_3"` - Qdrant collection name
- `CH3_EMBEDDING_MODEL="text-embedding-3-small"` - Embedding model
- `CH3_LLM_MODEL="gpt-4o-mini"` - LLM model (optional)
- `ENABLE_CHAPTER_3_RUNTIME=True` - Enable Chapter 3 runtime

**RAG Pipeline**:
- `RAG_MAX_CONTEXT=4` - Maximum number of context chunks

---

## Current Status

**Scaffolding**: ✅ Complete
- All subagents exist with placeholder logic
- All skills exist with placeholder logic
- Runtime engine routing in place
- RAG pipeline Chapter 3 branch in place
- Embedding client Chapter 3 support in place
- Qdrant store Chapter 3 support in place

**Real Logic**: ❌ Not Implemented
- No real AI calls
- No real RAG operations
- No real embedding generation
- No real Qdrant operations

**Next Steps**:
- Implement real chunking logic
- Implement real embedding generation
- Implement real Qdrant operations
- Implement real subagent logic
- Implement real skills logic

---

## Summary

Chapter 3 runtime structure is fully scaffolded with placeholder logic. All components are in place and ready for future AI logic implementation. The runtime engine routes Chapter 3 requests correctly, RAG pipeline has Chapter 3 branch, and all subagents/skills exist with proper structure.

