# Implementation Plan: AI Runtime Engine Extension for Chapter 2

**Branch**: `020-chapter-2-ai-runtime` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/020-chapter-2-ai-runtime/spec.md`

## Summary

This feature extends the existing AI Runtime Engine (Feature 005) to support Chapter 2 content by creating scaffolding for RAG collection setup, embedding pipeline extension, runtime routing, subagents, skills reuse, and ChatKit integration. The implementation establishes the architectural foundation for Chapter 2 runtime engine integration with RAG collection operations, chapter-aware embeddings, Chapter 2-specific routing, subagents, chapter-aware skills, and ChatKit scaffolding. **No real AI logic is implemented**—only scaffolding, function signatures, TODO placeholders, and architectural blueprints to prepare for future AI implementation.

**Primary Deliverable**: Complete Chapter 2 runtime engine extension scaffolding (RAG collection, embedding extension, runtime routing, subagents, skills, ChatKit, config)
**Validation**: All files exist, imports resolve, backend starts, no runtime errors

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- No new runtime dependencies required (scaffolding only)
- Existing runtime engine, RAG pipeline, skills, ChatKit from Feature 005
- Existing Chapter 2 subagents from Feature 013 (verify and extend if needed)

**Storage**: 
- No persistent storage (scaffolding only)
- Future: Qdrant for Chapter 2 vectors, Postgres for sessions

**Testing**:
- Manual: File existence verification, import resolution, backend startup
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)

**Project Type**: Backend AI runtime infrastructure extension scaffolding

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (no API calls, no LLM calls, no RAG execution)
- MUST maintain compatibility with Feature 005 (Chapter 1 runtime must still work)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality
- MUST remain deterministic and simple
- MUST prepare for future model swapping

**Scale/Scope**:
- 1 new RAG collection file (ch2_collection.py)
- 1 embedding client file to update (add chapter=2 support)
- 1 runtime engine file to update (add chapterId=2 routing)
- 4 subagent files to verify/create (ch2_*)
- 2 skills files to update (add CH2 TODOs)
- 1 ChatKit file to update (add Chapter 2 scaffolding)
- 2 config files to update (settings.py, .env.example)
- 1 API file to verify (ai_blocks.py)
- ~200-300 lines of scaffolding code (mostly signatures, TODOs, and comments)

---

## 1. Folder Structure

### 1.1 New Directories

**Directory**: `backend/app/ai/rag/collections/`
- **Status**: To be created
- **Purpose**: House Chapter 2 RAG collection module
- **Files**:
  - `__init__.py` (package init)
  - `ch2_collection.py` (NEW - RAG collection setup for Chapter 2)

### 1.2 Existing Directories (To Be Extended)

**Directory**: `backend/app/ai/embeddings/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `embedding_client.py` (extend with chapter=2 support)

**Directory**: `backend/app/ai/runtime/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `engine.py` (extend with chapterId=2 routing)

**Directory**: `backend/app/ai/subagents/`
- **Status**: Already exists (from Feature 005)
- **Files to Verify/Create**:
  - `ch2_ask_question_agent.py` (verify from Feature 013 or create)
  - `ch2_el10_agent.py` (verify from Feature 013 or create)
  - `ch2_quiz_agent.py` (verify from Feature 013 or create)
  - `ch2_diagram_agent.py` (verify from Feature 013 or create)

**Directory**: `backend/app/ai/skills/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `retrieval_skill.py` (add CH2 collection name support)
  - `prompt_builder_skill.py` (add CH2 templates)

**Directory**: `backend/app/ai/chatkit/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `session_manager.py` (extend to track chapterId=2)

**Directory**: `backend/app/content/chapters/`
- **Status**: Already exists
- **Files to Verify**:
  - `chapter_2_chunks.py` (verify exists from Feature 012)

**Directory**: `backend/app/config/`
- **Status**: Already exists
- **Files to Update**:
  - `settings.py` (add Chapter 2 settings)

**Directory**: `backend/app/api/`
- **Status**: Already exists
- **Files to Verify**:
  - `ai_blocks.py` (verify routes chapterId=2 correctly)

**Directory**: Root
- **Files to Update**:
  - `.env.example` (add Chapter 2 environment variables)

---

## 2. Runtime Flow Design

### 2.1 Chapter 2 Runtime Flow

**Flow**: CH2 Query → Retrieval Skill (CH2) → RAG Pipeline → Provider → Formatting Skill → Response

```
Frontend Component (Chapter 2)
    │
    ▼
API Endpoint (ai_blocks.py) - chapterId=2
    │
    ▼
Runtime Engine (engine.py)
    │
    ├─► Router: Determine block type → Select Chapter 2 subagent
    │   ├─► If chapterId=2:
    │   │   ├─► Route to ch2_ask_question_agent
    │   │   ├─► Route to ch2_explain_el10_agent
    │   │   ├─► Route to ch2_quiz_agent
    │   │   └─► Route to ch2_diagram_agent
    │
    ├─► Retrieval Skill (retrieval_skill.py) - Chapter 2 context
    │   ├─► TODO: support CH2 collection name
    │   ├─► Use CH2_COLLECTION_NAME from ch2_collection.py
    │   └─► Retrieve Chapter 2 context
    │
    ├─► RAG Pipeline (pipeline.py)
    │   ├─► Load Chapter 2 chunks (chapter_2_chunks.py)
    │   ├─► Embed user query (embedding_client.py with chapter=2)
    │   ├─► Qdrant similarity search (collection="chapter_2" via ch2_collection.py)
    │   └─► Construct retrieval context
    │
    ├─► Skills System (chapter-aware)
    │   ├─► Retrieval Skill (retrieval_skill.py) - Chapter 2 context
    │   ├─► Prompt Builder Skill (prompt_builder_skill.py) - ROS 2 prompts
    │   └─► Formatting Skill (formatting_skill.py) - Chapter 2 formatting
    │
    ├─► Chapter 2 Subagent
    │   ├─► ch2_ask_question_agent.py
    │   ├─► ch2_explain_el10_agent.py
    │   ├─► ch2_quiz_agent.py
    │   └─► ch2_diagram_agent.py
    │   └─► Uses skills + RAG context → Generates ROS 2 response
    │
    ├─► LLM Provider (base_llm.py → openai_provider.py | gemini_provider.py)
    │   └─► Generates response with ROS 2 context (CH2_LLM_MODEL)
    │
    └─► Response Formatting → Return to API → Frontend
```

### 2.2 Data Flow

1. **Request**: Frontend sends request with chapterId=2 → API endpoint receives
2. **Routing**: Runtime engine identifies chapterId=2 → routes to Chapter 2 subagent
3. **Retrieval Skill**: Retrieval skill uses CH2 collection name → calls RAG pipeline
4. **RAG Pipeline**: RAG pipeline retrieves Chapter 2 context from Qdrant (via ch2_collection.py)
5. **Embedding**: Embedding client generates embeddings with chapter=2 support
6. **Skills**: Skills assemble ROS 2 context + user input into prompts
7. **Subagent**: Chapter 2 subagent processes with ROS 2 context
8. **LLM**: LLM provider generates response with ROS 2 context (CH2_LLM_MODEL)
9. **Formatting**: Skills format response for frontend
10. **Response**: API returns formatted response → Frontend displays

---

## 3. Module-Level Design

### 3.1 RAG Collection Setup

**File**: `backend/app/ai/rag/collections/ch2_collection.py`

**Purpose**: RAG collection operations for Chapter 2

**Structure**:
- Module docstring
- Constant: `CH2_COLLECTION_NAME = "chapter_2"`
- Function: `create_collection()` - TODO stub
- Function: `upsert_vectors(chunks, embeddings)` - TODO stub
- Function: `search(query_embedding, top_k)` - TODO stub

**Input/Output Schemas** (Text Description):

**create_collection()**:
- **Input**: None
- **Output**: None (void function)
- **Purpose**: Create Qdrant collection for Chapter 2
- **TODO**: Implement Qdrant collection creation using CH2_COLLECTION_NAME

**upsert_vectors(chunks, embeddings)**:
- **Input**: 
  - `chunks`: List[str] - Chapter 2 text chunks
  - `embeddings`: List[List[float]] - Embedding vectors for chunks
- **Output**: None (void function)
- **Purpose**: Upsert vectors to Chapter 2 collection
- **TODO**: Implement Qdrant upsert operation using CH2_COLLECTION_NAME

**search(query_embedding, top_k)**:
- **Input**:
  - `query_embedding`: List[float] - Query embedding vector
  - `top_k`: int - Number of results to return
- **Output**: List[Dict[str, Any]] - Search results with chunks and scores
- **Purpose**: Search Chapter 2 collection for relevant chunks
- **TODO**: Implement Qdrant similarity search using CH2_COLLECTION_NAME

**Dependencies**:
- Internal: `app.ai.rag.qdrant_store` (future integration)
- External: None (scaffolding only)

**Reuse of CH1 Modules**:
- Reuses Qdrant store pattern from Feature 005
- Follows same collection structure as Chapter 1
- Uses same embedding and search patterns

---

### 3.2 Embedding Pipeline Extension

**File**: `backend/app/ai/embeddings/embedding_client.py`

**Purpose**: Extend embedding client to support chapter=2

**Current State**: Has `generate_embedding()` and `batch_embed()` functions (from Feature 005)

**Updates Required**:
- Add `chapter_id` parameter to `generate_embedding()` function
- Add TODO stub for chapter=2 support
- Add `batch_embed_ch2()` function with TODO stub
- Add placeholder for batch embedding for CH2

**Input/Output Schemas** (Text Description):

**generate_embedding(text, chapter_id=1)** (Extended):
- **Input**:
  - `text`: str - Input text to embed
  - `chapter_id`: int - Chapter identifier (default: 1, new: support 2)
- **Output**: List[float] - Embedding vector
- **Purpose**: Generate embedding with chapter-aware model selection
- **TODO**: Add chapter_id parameter support, use CH2_EMBEDDING_MODEL when chapter_id=2

**batch_embed_ch2(chunks)** (New):
- **Input**:
  - `chunks`: List[str] - Chapter 2 text chunks to embed
- **Output**: List[List[float]] - List of embedding vectors
- **Purpose**: Batch embedding for Chapter 2 chunks
- **TODO**: Implement batch embedding using CH2_EMBEDDING_MODEL

**Dependencies**:
- Internal: `app.config.settings` (for CH2_EMBEDDING_MODEL)
- External: None (scaffolding only)

**Reuse of CH1 Modules**:
- Reuses same embedding client structure from Feature 005
- Extends existing functions rather than creating new ones
- Uses same embedding model interface

---

### 3.3 Chapter 2 Knowledge Source

**File**: `backend/app/content/chapters/chapter_2_chunks.py`

**Purpose**: Chapter 2 content chunks for RAG

**Status**: Verify exists from Feature 012

**Structure** (if exists):
- Function: `get_chapter_chunks(chapter_id=2)` - Returns List[Dict[str, Any]]
- TODO comments for chunking implementation

**Input/Output Schemas** (Text Description):

**get_chapter_chunks(chapter_id=2)**:
- **Input**:
  - `chapter_id`: int - Chapter identifier (default: 2)
- **Output**: List[Dict[str, Any]] - List of chunk dictionaries with metadata
- **Purpose**: Return Chapter 2 content chunks for RAG
- **TODO**: Implement chunking from Chapter 2 MDX content (if not already implemented)

**Dependencies**:
- Internal: `app.content.chapters.chapter_2` (for metadata)
- External: None (scaffolding only)

**Reuse of CH1 Modules**:
- Reuses same chunk structure as Chapter 1 (from Feature 005)
- Follows same chunking patterns and metadata structure

---

### 3.4 AI Block Runtime Routing Extension

**File**: `backend/app/ai/runtime/engine.py`

**Purpose**: Extend runtime engine to route chapterId=2 calls to CH2 RAG

**Current State**: Has Chapter 2 knowledge source mapping and TODO comments (from Feature 013)

**Updates Required**:
- Add chapterId=2 routing logic with placeholder comments
- Add placeholder handler functions for CH2
- Add TODO notes for future logic implementation
- Ensure existing Chapter 1 routing remains unchanged

**Input/Output Schemas** (Text Description):

**run_ai_block(block_type, request_data)** (Extended):
- **Input**:
  - `block_type`: str - Type of AI block ("ask-question", "explain-like-10", "quiz", "diagram")
  - `request_data`: Dict[str, Any] - Request payload with chapterId=2
- **Output**: Dict[str, Any] - Formatted response for frontend
- **Purpose**: Route Chapter 2 requests to appropriate subagents and RAG pipeline
- **TODO**: 
  - Check chapterId in request_data
  - If chapterId=2, route to Chapter 2 subagent
  - Load Chapter 2 RAG context via ch2_collection.py
  - Call Chapter 2 subagent with context
  - Format response

**Handler Functions** (TODO Placeholders):
- `handle_ch2_ask_question(request_data, context)` - TODO stub
- `handle_ch2_explain_el10(request_data, context)` - TODO stub
- `handle_ch2_quiz(request_data, context)` - TODO stub
- `handle_ch2_diagram(request_data, context)` - TODO stub

**Dependencies**:
- Internal: `app.ai.subagents.ch2_*`, `app.ai.rag.collections.ch2_collection`, `app.ai.rag.pipeline`, `app.ai.providers.*`, `app.ai.skills.*`
- External: None (scaffolding only)

**Reuse of CH1 Modules**:
- Reuses same runtime engine structure from Feature 005
- Extends existing routing logic rather than creating new engine
- Uses same subagent, RAG, and LLM provider patterns

---

### 3.5 Subagents Extension

**Files**: 
- `backend/app/ai/subagents/ch2_ask_question_agent.py`
- `backend/app/ai/subagents/ch2_el10_agent.py`
- `backend/app/ai/subagents/ch2_quiz_agent.py`
- `backend/app/ai/subagents/ch2_diagram_agent.py`

**Purpose**: Chapter 2-specific subagents for ROS 2 knowledge

**Status**: Verify exist from Feature 013 or create if missing

**Structure** (each subagent):
- Module docstring
- Input schema placeholder
- Output schema placeholder
- Function stub with TODO: orchestrate provider + RAG
- No logic (placeholder only)

**Input/Output Schemas** (Text Description):

**ch2_ask_question_agent(question, context)**:
- **Input**:
  - `question`: str - User question about ROS 2
  - `context`: Dict[str, Any] - RAG context from Chapter 2
- **Output**: Dict[str, Any] - Answer with sources and confidence
- **Purpose**: Process ROS 2 question with Chapter 2 context
- **TODO**: Orchestrate provider + RAG, use ROS 2 concepts, return formatted answer

**ch2_el10_agent(concept, context)**:
- **Input**:
  - `concept`: str - ROS 2 concept to explain
  - `context`: Dict[str, Any] - RAG context from Chapter 2
- **Output**: Dict[str, Any] - Explanation with examples and analogies
- **Purpose**: Generate ROS 2 explanation with Chapter 2 context
- **TODO**: Orchestrate provider + RAG, use age-appropriate analogies, return formatted explanation

**ch2_quiz_agent(chapter_id, num_questions, context)**:
- **Input**:
  - `chapter_id`: int - Chapter identifier (2)
  - `num_questions`: int - Number of questions to generate
  - `context`: Dict[str, Any] - RAG context from Chapter 2
- **Output**: Dict[str, Any] - Quiz questions with answers
- **Purpose**: Generate ROS 2 quiz questions with Chapter 2 context
- **TODO**: Orchestrate provider + RAG, use ROS 2 learning objectives, return formatted quiz

**ch2_diagram_agent(diagram_type, concepts, context)**:
- **Input**:
  - `diagram_type`: str - Type of diagram to generate
  - `concepts`: List[str] - ROS 2 concepts to include
  - `context`: Dict[str, Any] - RAG context from Chapter 2
- **Output**: Dict[str, Any] - Diagram with description
- **Purpose**: Generate ROS 2 diagram with Chapter 2 context
- **TODO**: Orchestrate provider + RAG, use ROS 2 concepts, return formatted diagram

**Dependencies**:
- Internal: `app.ai.providers.*`, `app.ai.rag.collections.ch2_collection`, `app.ai.skills.*`
- External: None (scaffolding only)

**Reuse of CH1 Modules**:
- Reuses same subagent structure as Chapter 1 (from Feature 005)
- Follows same input/output patterns
- Uses same orchestration patterns (provider + RAG)

---

### 3.6 Skills Reuse

**File**: `backend/app/ai/skills/retrieval_skill.py`

**Purpose**: Extend retrieval skill to support CH2 collection name

**Current State**: Has `retrieve_content()` function with chapter-aware TODOs (from Feature 013)

**Updates Required**:
- Add TODO: support CH2 collection name
- Add comment referencing ch2_collection.py
- No implementation (TODO only)

**Input/Output Schemas** (Text Description):

**retrieve_content(query, chapter_id, top_k)** (Extended):
- **Input**:
  - `query`: str - Search query
  - `chapter_id`: int - Chapter identifier (1 or 2)
  - `top_k`: int - Number of results (default: 5)
- **Output**: List[Dict[str, Any]] - Retrieved content chunks
- **Purpose**: Retrieve content with chapter-aware collection selection
- **TODO**: 
  - If chapter_id == 2, use CH2_COLLECTION_NAME from ch2_collection.py
  - Call RAG pipeline with Chapter 2 collection
  - Return Chapter 2 chunks

**Dependencies**:
- Internal: `app.ai.rag.collections.ch2_collection` (for CH2_COLLECTION_NAME), `app.ai.rag.pipeline`
- External: None (scaffolding only)

**Reuse of CH1 Modules**:
- Reuses same retrieval skill structure from Feature 005
- Extends existing function rather than creating new one
- Uses same RAG pipeline interface

---

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Purpose**: Extend prompt builder skill to support CH2 templates

**Current State**: Has `build_prompt()` function with chapter-aware TODOs (from Feature 013)

**Updates Required**:
- Add TODO: templates for CH2
- Add comment referencing ROS 2 prompt templates
- No implementation (TODO only)

**Input/Output Schemas** (Text Description):

**build_prompt(block_type, user_input, context, chapter_id)** (Extended):
- **Input**:
  - `block_type`: str - Type of AI block
  - `user_input`: str - User's question or concept
  - `context`: List[Dict[str, Any]] - Retrieved context chunks
  - `chapter_id`: int - Chapter identifier (1 or 2)
- **Output**: str - Constructed prompt string for LLM
- **Purpose**: Build prompt with chapter-aware templates
- **TODO**: 
  - If chapter_id == 2, use ROS 2 prompt templates
  - Include ROS 2 concepts, analogies, examples
  - Format context with ROS 2-specific instructions

**Dependencies**:
- Internal: None (standalone skill)
- External: None (scaffolding only)

**Reuse of CH1 Modules**:
- Reuses same prompt builder skill structure from Feature 005
- Extends existing function rather than creating new one
- Uses same prompt construction patterns

---

### 3.7 ChatKit Session Support

**File**: `backend/app/ai/chatkit/session_manager.py`

**Purpose**: Extend session manager to track chapterId=2

**Current State**: Has session management scaffolding (from Feature 005)

**Updates Required**:
- Extend session_manager to track chapterId=2
- Add TODO stub: attach CH2 memory nodes
- No implementation (placeholder only)

**Input/Output Schemas** (Text Description):

**create_session(chapter_id=1)** (Extended):
- **Input**:
  - `chapter_id`: int - Chapter identifier (default: 1, new: support 2)
- **Output**: Dict[str, Any] - Session dictionary with session_id and chapter_id
- **Purpose**: Create session with chapter-aware tracking
- **TODO**: Support chapterId=2, track Chapter 2 sessions separately

**attach_memory_nodes(session_id, chapter_id)** (Extended):
- **Input**:
  - `session_id`: str - Session identifier
  - `chapter_id`: int - Chapter identifier (1 or 2)
- **Output**: None (void function)
- **Purpose**: Attach chapter-specific memory nodes to session
- **TODO**: 
  - If chapter_id == 2, attach CH2 memory nodes
  - Store Chapter 2 context in session memory

**Dependencies**:
- Internal: None (standalone session manager)
- External: None (scaffolding only)

**Reuse of CH1 Modules**:
- Reuses same session manager structure from Feature 005
- Extends existing functions rather than creating new ones
- Uses same session management patterns

---

### 3.8 Configuration

**File**: `backend/app/config/settings.py`

**Purpose**: Add Chapter 2 runtime settings

**Current State**: Has Chapter 2 runtime configuration (DEFAULT_CH2_MODEL, DEFAULT_CH2_EMBEDDINGS, ENABLE_CHAPTER_2_RUNTIME) from Feature 013

**Updates Required**:
- Add `QDRANT_COLLECTION_CH2: Optional[str] = None`
- Add `CH2_EMBEDDING_MODEL: Optional[str] = None`
- Add `CH2_LLM_MODEL: Optional[str] = None`
- Ensure all settings are optional (default to None)

**Settings Schema** (Text Description):

**QDRANT_COLLECTION_CH2**:
- **Type**: Optional[str]
- **Default**: None
- **Purpose**: Qdrant collection name for Chapter 2
- **Usage**: Used by ch2_collection.py for collection operations

**CH2_EMBEDDING_MODEL**:
- **Type**: Optional[str]
- **Default**: None
- **Purpose**: Embedding model for Chapter 2
- **Usage**: Used by embedding_client.py when chapter_id=2

**CH2_LLM_MODEL**:
- **Type**: Optional[str]
- **Default**: None
- **Purpose**: LLM model for Chapter 2
- **Usage**: Used by runtime engine when chapterId=2

**Dependencies**:
- Internal: None (standalone settings)
- External: Pydantic Settings

**Reuse of CH1 Modules**:
- Reuses same settings structure from Feature 005
- Follows same configuration patterns
- Uses same environment variable loading

---

**File**: `.env.example`

**Purpose**: Document Chapter 2 environment variables

**Updates Required**:
- Add `QDRANT_COLLECTION_CH2="chapter_2"`
- Add `CH2_EMBEDDING_MODEL="text-embedding-3-small"`
- Add `CH2_LLM_MODEL="gpt-4o-mini"`
- Add descriptions for each variable

**Environment Variables Schema** (Text Description):

**QDRANT_COLLECTION_CH2**:
- **Value**: "chapter_2"
- **Description**: Qdrant collection name for Chapter 2 RAG operations
- **Required**: No (optional, defaults to "chapter_2" if not set)

**CH2_EMBEDDING_MODEL**:
- **Value**: "text-embedding-3-small"
- **Description**: Embedding model identifier for Chapter 2 (e.g., "text-embedding-3-small")
- **Required**: No (optional, uses default if not set)

**CH2_LLM_MODEL**:
- **Value**: "gpt-4o-mini"
- **Description**: LLM model identifier for Chapter 2 (e.g., "gpt-4o-mini")
- **Required**: No (optional, uses default if not set)

---

### 3.9 API Stability

**File**: `backend/app/api/ai_blocks.py`

**Purpose**: Verify API routes chapterId=2 correctly

**Current State**: Already routes to runtime engine (from Feature 005)

**Verification Required**:
- Verify chapterId=2 treated the same as chapterId=1
- Verify all block types route to `run_ai_block(block_type, chapter_id=2)`
- Add comments if needed to document Chapter 2 support

**API Routing Schema** (Text Description):

**All Endpoints** (ask-question, explain-like-10, quiz, diagram):
- **Input**: Request model with `chapterId: Optional[int] = None`
- **Routing**: 
  - If chapterId=2, route to `run_ai_block(block_type, request_data)` with chapterId=2
  - Runtime engine handles chapterId routing internally
  - No special handling needed in API layer
- **Output**: AIBlockResponse with formatted response
- **Purpose**: Route Chapter 2 requests to runtime engine

**Dependencies**:
- Internal: `app.ai.runtime.engine` (run_ai_block function)
- External: FastAPI, Pydantic

**Reuse of CH1 Modules**:
- Reuses same API structure from Feature 005
- No changes needed (routing handled by runtime engine)
- Uses same request/response models

---

## 4. Subagent Orchestration Design

### 4.1 Chapter 2 Subagent Architecture

**Pattern**: Chapter 2 subagents mirror Chapter 1 subagent structure but with ROS 2 context

**Orchestration Flow** (TODO):
1. Runtime engine routes to Chapter 2 subagent based on block_type
2. Subagent receives request_data and RAG context
3. Subagent uses retrieval skill to get additional context (if needed)
4. Subagent uses prompt builder skill to construct ROS 2 prompt
5. Subagent calls LLM provider with ROS 2 prompt
6. Subagent uses formatting skill to format response
7. Subagent returns formatted response to runtime engine

### 4.2 ch2_ask_question_agent

**File**: `backend/app/ai/subagents/ch2_ask_question_agent.py`

**Orchestration** (TODO):
- **Input**: question (str), chapterId (2), sectionId (optional str), RAG context (Dict)
- **Step 1**: Use retrieval skill to get additional ROS 2 context (if needed)
- **Step 2**: Use prompt builder skill to construct ROS 2 question-answering prompt
- **Step 3**: Call LLM provider (CH2_LLM_MODEL) with prompt
- **Step 4**: Use formatting skill to format answer with sources
- **Output**: Answer (str), sources (List[str]), confidence (float)

**ROS 2 Context**:
- ROS 2 concepts: nodes, topics, services, actions, packages, launch-files
- ROS 2 analogies: post office, restaurant, phone calls, package delivery
- ROS 2 examples: TurtleBot 3, navigation stack, robot arm control

### 4.3 ch2_el10_agent

**File**: `backend/app/ai/subagents/ch2_el10_agent.py`

**Orchestration** (TODO):
- **Input**: concept (str), chapterId (2), RAG context (Dict)
- **Step 1**: Use retrieval skill to get ROS 2 concept context
- **Step 2**: Use prompt builder skill to construct ELI10 prompt with ROS 2 analogies
- **Step 3**: Call LLM provider (CH2_LLM_MODEL) with prompt
- **Step 4**: Use formatting skill to format explanation with examples
- **Output**: Explanation (str), examples (List[str]), analogies (List[str])

**ROS 2 Context**:
- Age-appropriate analogies for ROS 2 concepts
- Simple explanations using ROS 2 examples
- Visual descriptions for ROS 2 components

### 4.4 ch2_quiz_agent

**File**: `backend/app/ai/subagents/ch2_quiz_agent.py`

**Orchestration** (TODO):
- **Input**: chapterId (2), numQuestions (int), RAG context (Dict)
- **Step 1**: Use retrieval skill to get ROS 2 learning objectives
- **Step 2**: Use prompt builder skill to construct quiz generation prompt
- **Step 3**: Call LLM provider (CH2_LLM_MODEL) with prompt
- **Step 4**: Use formatting skill to format quiz questions and answers
- **Output**: Questions (List[Dict]), Answers (List[Dict]), Difficulty (List[str])

**ROS 2 Context**:
- ROS 2 learning objectives from Chapter 2
- ROS 2 concepts to test (nodes, topics, services, actions)
- ROS 2 practical scenarios for questions

### 4.5 ch2_diagram_agent

**File**: `backend/app/ai/subagents/ch2_diagram_agent.py`

**Orchestration** (TODO):
- **Input**: diagramType (str), chapterId (2), concepts (List[str]), RAG context (Dict)
- **Step 1**: Use retrieval skill to get ROS 2 diagram context
- **Step 2**: Use prompt builder skill to construct diagram generation prompt
- **Step 3**: Call LLM provider (CH2_LLM_MODEL) with prompt
- **Step 4**: Use formatting skill to format diagram with description
- **Output**: Diagram (str), Description (str), Concepts (List[str])

**ROS 2 Context**:
- ROS 2 architecture diagrams (nodes, topics, services)
- ROS 2 communication patterns
- ROS 2 system diagrams (TurtleBot, navigation stack)

---

## 5. Skill Integration Plan

### 5.1 Retrieval Skill Extension

**File**: `backend/app/ai/skills/retrieval_skill.py`

**Extension Plan**:
- Add TODO comment: support CH2 collection name
- Add reference to ch2_collection.py for CH2_COLLECTION_NAME
- Add conditional logic (TODO) to use CH2 collection when chapter_id=2
- No implementation (TODO only)

**Integration Points**:
- Called by Chapter 2 subagents to retrieve additional context
- Uses ch2_collection.py for Chapter 2 collection operations
- Uses RAG pipeline for semantic search

**Reuse Pattern**:
- Reuses same retrieval skill structure from Feature 005
- Extends existing function rather than creating new one
- Uses same RAG pipeline interface

### 5.2 Prompt Builder Skill Extension

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Extension Plan**:
- Add TODO comment: templates for CH2
- Add reference to ROS 2 prompt templates
- Add conditional logic (TODO) to use ROS 2 templates when chapter_id=2
- No implementation (TODO only)

**Integration Points**:
- Called by Chapter 2 subagents to construct ROS 2 prompts
- Uses ROS 2-specific templates and instructions
- Formats context with ROS 2 concepts

**Reuse Pattern**:
- Reuses same prompt builder skill structure from Feature 005
- Extends existing function rather than creating new one
- Uses same prompt construction patterns

---

## 6. Config Plan

### 6.1 Environment Variables

**File**: `.env.example`

**New Variables**:
- `QDRANT_COLLECTION_CH2="chapter_2"` - Qdrant collection name for Chapter 2
- `CH2_EMBEDDING_MODEL="text-embedding-3-small"` - Embedding model for Chapter 2
- `CH2_LLM_MODEL="gpt-4o-mini"` - LLM model for Chapter 2

**Documentation**:
- Each variable should have a comment explaining its purpose
- Default values should be documented
- Required vs optional status should be clear

### 6.2 Settings Extensions

**File**: `backend/app/config/settings.py`

**New Settings**:
- `QDRANT_COLLECTION_CH2: Optional[str] = None` - Qdrant collection name for Chapter 2
- `CH2_EMBEDDING_MODEL: Optional[str] = None` - Embedding model for Chapter 2
- `CH2_LLM_MODEL: Optional[str] = None` - LLM model for Chapter 2

**Settings Structure**:
- All settings must be optional (default to None)
- Settings should be loaded from environment variables
- Settings should be type-safe (Pydantic)

**Usage**:
- Used by ch2_collection.py for collection name
- Used by embedding_client.py for embedding model selection
- Used by runtime engine for LLM model selection

---

## 7. API Routing Plan

### 7.1 API Endpoint Flow

**Flow**: ai_blocks → runtime.engine → chapter switch → subagents → TODO return

**Step 1: API Endpoint (ai_blocks.py)**
- Receives request with chapterId=2
- Routes to `run_ai_block(block_type, request_data)`
- No special handling needed (routing handled by runtime engine)

**Step 2: Runtime Engine (engine.py)**
- Receives request with chapterId=2
- Checks chapterId in request_data
- Routes to Chapter 2 subagent based on block_type
- Loads Chapter 2 RAG context via ch2_collection.py
- Calls Chapter 2 subagent with context

**Step 3: Chapter Switch (engine.py)**
- If chapterId=2:
  - Route to ch2_ask_question_agent (if block_type="ask-question")
  - Route to ch2_explain_el10_agent (if block_type="explain-like-10")
  - Route to ch2_quiz_agent (if block_type="quiz")
  - Route to ch2_diagram_agent (if block_type="diagram")
- Else (chapterId=1):
  - Use existing Chapter 1 routing

**Step 4: Subagents (ch2_*.py)**
- Receive request_data and RAG context
- Use skills to process request
- Call LLM provider with ROS 2 context
- Format response

**Step 5: TODO Return**
- Subagent returns formatted response
- Runtime engine returns response to API
- API returns response to frontend

### 7.2 Routing Table

**Block Type → Subagent Mapping** (Chapter 2):
- "ask-question" → ch2_ask_question_agent
- "explain-like-10" → ch2_explain_el10_agent
- "quiz" → ch2_quiz_agent
- "diagram" → ch2_diagram_agent

**Chapter ID → Collection Mapping**:
- chapterId=1 → "chapter_1" (existing)
- chapterId=2 → "chapter_2" (new, via ch2_collection.py)

**Chapter ID → Model Mapping**:
- chapterId=1 → LLM_MODEL (existing)
- chapterId=2 → CH2_LLM_MODEL (new)

---

## 8. Integration Points

### 8.1 Feature 005 (AI Runtime Engine)

**Integration**: Extends existing runtime engine structure
- Reuses runtime engine, subagents, skills, ChatKit patterns
- Extends existing functions rather than creating new ones
- Maintains compatibility with Chapter 1 functionality

### 8.2 Feature 012 (Chapter 2 RAG)

**Integration**: Uses chapter_2_chunks.py from Feature 012
- Verifies chapter_2_chunks.py exists
- Uses get_chapter_chunks() function for RAG retrieval
- Extends RAG pipeline to support Chapter 2

### 8.3 Feature 013 (Chapter 2 Runtime Engine)

**Integration**: Verifies and extends subagents from Feature 013
- Verifies Chapter 2 subagents exist
- Extends subagents with input/output schema placeholders
- Adds TODO comments for orchestration

---

## 9. Acceptance Checks

### 9.1 File Existence

- [ ] `backend/app/ai/rag/collections/ch2_collection.py` exists
- [ ] `backend/app/ai/embeddings/embedding_client.py` updated with chapter=2 support
- [ ] `backend/app/ai/runtime/engine.py` updated with chapterId=2 routing
- [ ] `backend/app/ai/subagents/ch2_*.py` files exist (4 files)
- [ ] `backend/app/ai/skills/retrieval_skill.py` updated with CH2 TODO
- [ ] `backend/app/ai/skills/prompt_builder_skill.py` updated with CH2 TODO
- [ ] `backend/app/ai/chatkit/session_manager.py` updated with chapterId=2 tracking
- [ ] `backend/app/config/settings.py` updated with Chapter 2 settings
- [ ] `.env.example` updated with Chapter 2 variables

### 9.2 Import Resolution

- [ ] All new modules import without errors
- [ ] All existing imports continue to work
- [ ] No circular dependencies introduced

### 9.3 Backend Startup

- [ ] Backend starts successfully
- [ ] No runtime errors on startup
- [ ] Configuration loads correctly

### 9.4 TODO Placeholders

- [ ] All functions have TODO comments
- [ ] All TODO comments are descriptive and actionable
- [ ] All placeholders return expected structure

---

## 10. Next Steps

After completing this plan:

1. **Task Generation**: Run `/sp.tasks` to create implementation tasks
2. **Implementation**: Run `/sp.implement` to create scaffolding
3. **Verification**: Verify all files exist and imports resolve

---

Plan complete — ready for /sp.tasks.
