# Tasks: System Integration Layer — Phase 2 (Real AI Logic Activation)

**Feature**: 045-system-integration-phase-2 | **Branch**: `045-system-integration-phase-2` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for activating real AI logic. All tasks implement real functionality—no placeholders.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category**: PROVIDER (Provider activation), EMBEDDING (Embedding activation), QDRANT (Qdrant integration), RAG (RAG pipeline), SKILLS (Skills activation), SUBAGENT (Subagent activation), RUNTIME (Runtime engine), CLI (CLI indexer), VALIDATION (Validation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prepare for implementation.

- [ ] [T001] [P1] [SETUP] Verify Feature 044 (System Integration Phase 1) is complete: Check that router.py, registry.py, unified_rag.py exist
- [ ] [T002] [P1] [SETUP] Verify Feature 005 (AI Runtime Engine) is complete: Check that engine.py exists
- [ ] [T003] [P1] [SETUP] Verify Feature 040-041 (Chapter 3 RAG + Runtime Integration) is complete: Check that Chapter 3 routing exists
- [ ] [T004] [P1] [SETUP] Verify all chapter chunk files exist: Check chapter_1_chunks.py, chapter_2_chunks.py, chapter_3_chunks.py
- [ ] [T005] [P1] [SETUP] Verify external dependencies: Check that openai, qdrant-client are in pyproject.toml
- [ ] [T006] [P1] [SETUP] Add google-generativeai to pyproject.toml: Add dependency for Gemini provider

**Success Criteria**:
- All prerequisite features complete
- All required modules exist
- External dependencies configured

**Dependencies**: Feature 044, 005, 040-041 must be complete

---

## PHASE 1 — PROVIDER ACTIVATION TASKS

**User Story**: US1 - AI Blocks Produce Real Responses

**Test Strategy**: Can be tested by verifying real LLM responses are returned.

### OpenAI Provider

- [ ] [T007] [P1] [PROVIDER] Update `backend/app/ai/providers/openai_provider.py`:
  - Import openai library (AsyncOpenAI)
  - Import settings from app.config.settings
  - Initialize OpenAI client in __init__ with settings.openai_api_key

- [ ] [T008] [P1] [PROVIDER] Implement real generate() method in `backend/app/ai/providers/openai_provider.py`:
  - Build messages array (system + user prompt or messages parameter)
  - Call client.chat.completions.create() with model, messages, temperature
  - Extract text from response.choices[0].message.content
  - Extract metadata (model, usage.tokens, finish_reason)
  - Return formatted response: {text: str, metadata: {model, tokens, finish_reason}}
  - Add error handling for API failures

- [ ] [T009] [P1] [PROVIDER] Add error handling to `backend/app/ai/providers/openai_provider.py`:
  - Handle RateLimitError, AuthenticationError, APIError
  - Return error response or raise exception
  - Add TODO logging for errors

### Gemini Provider

- [ ] [T010] [P1] [PROVIDER] Update `backend/app/ai/providers/gemini_provider.py`:
  - Import google.generativeai library
  - Import settings from app.config.settings
  - Initialize Gemini client with GEMINI_API_KEY or settings.gemini_api_key

- [ ] [T011] [P1] [PROVIDER] Implement real generate() method in `backend/app/ai/providers/gemini_provider.py`:
  - Build prompt (system + user prompt)
  - Call model.generate_content() with prompt, temperature
  - Extract text from response.text
  - Extract metadata (model, usage, finish_reason)
  - Return formatted response: {text: str, metadata: {model, tokens, finish_reason}}
  - Add error handling for API failures

- [ ] [T012] [P1] [PROVIDER] Add error handling to `backend/app/ai/providers/gemini_provider.py`:
  - Handle API errors, rate limits, authentication errors
  - Return error response or raise exception
  - Add TODO logging for errors

### Provider Factory

- [ ] [T013] [P1] [PROVIDER] Update `backend/app/ai/providers/base_llm.py`:
  - Implement real get_provider() factory function
  - Import OpenAIProvider and GeminiProvider
  - Return OpenAIProvider() if provider_name == "openai"
  - Return GeminiProvider() if provider_name == "gemini"
  - Return default provider (OpenAI) if provider_name is invalid
  - Add error handling for missing API keys

**Acceptance Test**: Provider calls return real LLM responses

---

## PHASE 2 — EMBEDDING ACTIVATION TASKS

**User Story**: US1 - AI Blocks Produce Real Responses

**Test Strategy**: Can be tested by verifying real embeddings are generated.

### Single Embedding

- [ ] [T014] [P1] [EMBEDDING] Update `backend/app/ai/embeddings/embedding_client.py`:
  - Import openai library (AsyncOpenAI)
  - Import settings from app.config.settings
  - Initialize OpenAI client in module scope

- [ ] [T015] [P1] [EMBEDDING] Implement real generate_embedding() function in `backend/app/ai/embeddings/embedding_client.py`:
  - Select embedding model based on chapter_id (CH2_EMBEDDING_MODEL, CH3_EMBEDDING_MODEL, or default)
  - Handle max token size (8191 for text-embedding-3-small)
  - Truncate text if exceeds max tokens (simple truncation)
  - Call client.embeddings.create(input=text, model=model)
  - Extract embedding vector from response.data[0].embedding
  - Return 1536-dimensional vector
  - Add error handling for API failures

### Batch Embedding

- [ ] [T016] [P1] [EMBEDDING] Implement real batch_embed() function in `backend/app/ai/embeddings/embedding_client.py`:
  - Handle large batches (split if needed, e.g., 100 chunks per batch)
  - Call client.embeddings.create(input=chunks, model=model) for each batch
  - Combine results from all batches
  - Return list of 1536-dimensional vectors
  - Add error handling for partial failures

- [ ] [T017] [P1] [EMBEDDING] Implement real batch_embed_ch2() function in `backend/app/ai/embeddings/embedding_client.py`:
  - Use CH2_EMBEDDING_MODEL for Chapter 2
  - Call batch_embed() with Chapter 2 model
  - Return list of embedding vectors

- [ ] [T018] [P1] [EMBEDDING] Implement real batch_embed_ch3() function in `backend/app/ai/embeddings/embedding_client.py`:
  - Use CH3_EMBEDDING_MODEL for Chapter 3
  - Call batch_embed() with Chapter 3 model
  - Return list of embedding vectors

**Acceptance Test**: Embedding functions return real 1536-dimensional vectors

---

## PHASE 3 — QDRANT INTEGRATION TASKS

**User Story**: US1 - AI Blocks Produce Real Responses

**Test Strategy**: Can be tested by verifying real Qdrant operations work.

### Qdrant Client Initialization

- [ ] [T019] [P1] [QDRANT] Update `backend/app/ai/rag/qdrant_store.py`:
  - Import qdrant_client library (QdrantClient)
  - Import settings from app.config.settings
  - Initialize Qdrant client in module scope with settings.qdrant_url and settings.qdrant_api_key

### Create Collection

- [ ] [T020] [P1] [QDRANT] Implement real create_collection() function in `backend/app/ai/rag/qdrant_store.py`:
  - Use Qdrant client to create collection
  - Configure collection with vector size 1536 (for text-embedding-3-small)
  - Set distance metric to Cosine similarity
  - Configure HNSW index (m=16, ef_construct=100)
  - Handle collection already exists error (return True if exists)
  - Return True if successful, False otherwise
  - Add error handling for connection failures

### Upsert Vectors

- [ ] [T021] [P1] [QDRANT] Implement real upsert_vectors() function in `backend/app/ai/rag/qdrant_store.py`:
  - Use Qdrant client to batch upsert vectors
  - Vector structure: {id, vector (1536 dims), payload (metadata)}
  - Handle large batches (split if needed, e.g., 100 vectors per batch)
  - Call client.upsert(collection_name, points) for each batch
  - Return True if successful, False otherwise
  - Add error handling for upsert failures

### Similarity Search

- [ ] [T022] [P1] [QDRANT] Implement real similarity_search() function in `backend/app/ai/rag/qdrant_store.py`:
  - Embed query text using embedding_client.generate_embedding() (if query is string)
  - Use Qdrant client to perform vector search
  - Call client.search(collection_name, query_vector, limit=top_k)
  - Filter by chapter_id if provided (using payload filter)
  - Return top_k results sorted by similarity score
  - Format results: [{id, score, payload}, ...]
  - Add error handling for search failures

**Acceptance Test**: Qdrant operations (create, upsert, search) work correctly

---

## PHASE 4 — RAG PIPELINE TASKS

**User Story**: US1 - AI Blocks Produce Real Responses

**Test Strategy**: Can be tested by verifying real RAG context is built.

### RAG Pipeline Implementation

- [ ] [T023] [P1] [RAG] Update `backend/app/ai/rag/pipeline.py`:
  - Import get_chapter_chunks from chapter_X_chunks modules
  - Import embedding_client.generate_embedding
  - Import qdrant_store.similarity_search

- [ ] [T024] [P1] [RAG] Implement Step 1 in `backend/app/ai/rag/pipeline.py`:
  - Load chapter chunks: get_chapter_chunks(chapter_id)
  - Handle empty chunks gracefully

- [ ] [T025] [P1] [RAG] Implement Step 2 in `backend/app/ai/rag/pipeline.py`:
  - Embed user query: generate_embedding(query, chapter_id)
  - Get query vector (1536 dimensions)

- [ ] [T026] [P1] [RAG] Implement Step 3 in `backend/app/ai/rag/pipeline.py`:
  - Determine collection name (chapter_1, chapter_2, chapter_3)
  - Perform Qdrant search: similarity_search(collection_name, query_vector, top_k)
  - Get retrieved chunks with metadata

- [ ] [T027] [P1] [RAG] Implement Step 4 in `backend/app/ai/rag/pipeline.py`:
  - Build context window: assemble retrieved chunks into context string
  - Format chunks with section references
  - Limit context size (use RAG_MAX_CONTEXT env var, default: 4 chunks)

- [ ] [T028] [P1] [RAG] Implement Step 5 in `backend/app/ai/rag/pipeline.py`:
  - Prepare final prompt: combine query + context
  - Return context dictionary: {context: str, chunks: List[Dict], query_embedding: List[float]}

- [ ] [T029] [P1] [RAG] Add error handling to `backend/app/ai/rag/pipeline.py`:
  - Handle empty context gracefully
  - Handle Qdrant search failures
  - Handle embedding generation failures
  - Return fallback context if needed

**Acceptance Test**: RAG pipeline returns real context with retrieved chunks

---

## PHASE 5 — SKILLS REAL LOGIC TASKS

**User Story**: US1 - AI Blocks Produce Real Responses

**Test Strategy**: Can be tested by verifying real skill logic works.

### Retrieval Skill

- [ ] [T030] [P1] [SKILLS] Update `backend/app/ai/skills/retrieval_skill.py`:
  - Import run_rag_pipeline from app.ai.rag.pipeline
  - Implement real retrieve_content() function
  - Call run_rag_pipeline(query, chapter_id, top_k)
  - Format results as list of chunk dictionaries
  - Return retrieved chunks with metadata

### Prompt Builder Skill

- [ ] [T031] [P1] [SKILLS] Update `backend/app/ai/skills/prompt_builder_skill.py`:
  - Implement real build_prompt() function
  - Build system prompt based on block_type (ask-question, explain-like-10, quiz, diagram)
  - Include retrieved context chunks in prompt
  - Format context with section references
  - Add user input to prompt
  - Add formatting instructions for structured output
  - Return formatted prompt string

### Formatting Skill

- [ ] [T032] [P1] [SKILLS] Update `backend/app/ai/skills/formatting_skill.py`:
  - Implement real format_response() function
  - Parse raw LLM response based on block_type
  - Extract structured data from LLM text (answer, sources, explanation, etc.)
  - Format sources, examples, questions based on block_type
  - Return formatted response dictionary
  - Add validation for response structure

**Acceptance Test**: Skills return real formatted outputs

---

## PHASE 6 — SUBAGENT ACTIVATION TASKS

**User Story**: US1 - AI Blocks Produce Real Responses

**Test Strategy**: Can be tested by verifying real subagent logic works.

### Ask Question Agent

- [ ] [T033] [P1] [SUBAGENT] Update `backend/app/ai/subagents/ch3/ask_question_agent.py`:
  - Import retrieval_skill, prompt_builder_skill, formatting_skill
  - Import get_provider from app.ai.providers.base_llm
  - Import settings from app.config.settings
  - Implement real run() method:
    - Call retrieval_skill.retrieve_content() to get context
    - Call prompt_builder_skill.build_prompt() with context
    - Call LLM provider with prompt
    - Call formatting_skill.format_response() with LLM response
    - Extract source citations from retrieved chunks
    - Calculate confidence score based on context relevance
    - Return formatted answer

### Explain EL10 Agent

- [ ] [T034] [P1] [SUBAGENT] Update `backend/app/ai/subagents/ch3/explain_el10_agent.py`:
  - Import skills and provider (same as ask_question_agent)
  - Implement real run() method:
    - Call retrieval_skill to get context
    - Call prompt_builder_skill to build ELI10 prompt
    - Call LLM provider with prompt
    - Call formatting_skill to format response
    - Extract analogies and examples from LLM response
    - Return formatted explanation

### Quiz Agent

- [ ] [T035] [P1] [SUBAGENT] Update `backend/app/ai/subagents/ch3/quiz_agent.py`:
  - Import skills and provider (same as ask_question_agent)
  - Implement real run() method:
    - Call retrieval_skill to get context (all sections)
    - Call prompt_builder_skill to build quiz prompt
    - Call LLM provider with prompt
    - Call formatting_skill to format response
    - Parse quiz questions from LLM response
    - Return formatted quiz

### Diagram Agent

- [ ] [T036] [P1] [SUBAGENT] Update `backend/app/ai/subagents/ch3/diagram_agent.py`:
  - Import skills and provider (same as ask_question_agent)
  - Implement real run() method:
    - Call retrieval_skill to get context (optional)
    - Call prompt_builder_skill to build diagram prompt
    - Call LLM provider with prompt
    - Call formatting_skill to format response
    - Return formatted diagram description/prompt

**Acceptance Test**: Subagents return real formatted responses

---

## PHASE 7 — RUNTIME ENGINE LOGIC TASKS

**User Story**: US1 - AI Blocks Produce Real Responses

**Test Strategy**: Can be tested by verifying real AI block results are produced.

### Ask Question Flow

- [ ] [T037] [P1] [RUNTIME] Update `backend/app/ai/runtime/engine.py`:
  - Implement real flow for ask-question:
    - Call RAG pipeline to get context
    - Call LLM provider with prompt + context
    - Format response with answer and sources
  - Connect to: RAG pipeline, LLM provider, output formatters

### Explain Like 10 Flow

- [ ] [T038] [P1] [RUNTIME] Update `backend/app/ai/runtime/engine.py`:
  - Implement real flow for explain-like-10:
    - Call RAG pipeline to get context
    - Call LLM provider with ELI10 prompt + context
    - Format response with explanation, analogies, examples

### Quiz Flow

- [ ] [T039] [P1] [RUNTIME] Update `backend/app/ai/runtime/engine.py`:
  - Implement real flow for quiz:
    - Call RAG pipeline to get context (all sections)
    - Call LLM provider with quiz generation prompt + context
    - Format response with quiz questions, answers, explanations

### Diagram Flow

- [ ] [T040] [P1] [RUNTIME] Update `backend/app/ai/runtime/engine.py`:
  - Implement real flow for diagram:
    - Call RAG pipeline to get context (optional)
    - Call LLM provider with diagram generation prompt + context
    - Format response with diagram description/prompt

**Acceptance Test**: Runtime engine returns real AI block results

---

## PHASE 8 — CLI INDEXER TASKS

**User Story**: US2 - Developer Can Index Chapters

**Test Strategy**: Can be tested by running CLI script and verifying embeddings are generated and vectors are upserted.

### CLI Script Creation

- [ ] [T041] [P1] [CLI] Create `backend/app/cli/index_chapter.py`:
  - Import argparse for command-line arguments
  - Import get_chapter_chunks from chapter_X_chunks modules
  - Import embedding_client.batch_embed
  - Import qdrant_store.create_collection, upsert_vectors
  - Import settings from app.config.settings

- [ ] [T042] [P1] [CLI] Implement index_chapter() function in `backend/app/cli/index_chapter.py`:
  - Read chapter chunks from chapter_X_chunks.py
  - Generate embeddings using batch_embed()
  - Prepare vectors: {id, vector, payload}
  - Create collection if not exists
  - Upsert into Qdrant using upsert_vectors()
  - Log progress and results

- [ ] [T043] [P1] [CLI] Add command-line arguments to `backend/app/cli/index_chapter.py`:
  - --chapter-id: Chapter identifier (required)
  - --collection-name: Qdrant collection name (optional)
  - Add argument parsing and validation

- [ ] [T044] [P1] [CLI] Add error handling and logging to `backend/app/cli/index_chapter.py`:
  - Handle empty chunks gracefully
  - Handle embedding generation failures
  - Handle Qdrant connection failures
  - Log progress (chunks processed, embeddings generated, vectors upserted)
  - Log errors if any

**Acceptance Test**: CLI script indexes chapters successfully

---

## PHASE 9 — VALIDATION TASKS

**User Story**: US1, US2 - Validation

**Test Strategy**: Can be tested by verifying all components work end-to-end.

### Integration Validation

- [ ] [T045] [P1] [VALIDATION] Test provider calls: Verify OpenAI and Gemini providers return real responses
- [ ] [T046] [P1] [VALIDATION] Test embedding generation: Verify embeddings are 1536-dimensional vectors
- [ ] [T047] [P1] [VALIDATION] Test Qdrant operations: Verify create, upsert, search work correctly
- [ ] [T048] [P1] [VALIDATION] Test RAG pipeline: Verify context is built correctly
- [ ] [T049] [P1] [VALIDATION] Test AI block endpoints: Verify real responses are returned
- [ ] [T050] [P1] [VALIDATION] Test CLI indexer: Verify chapters are indexed successfully
- [ ] [T051] [P1] [VALIDATION] Verify no broken imports: Check all imports resolve
- [ ] [T052] [P1] [VALIDATION] Verify error handling: Test error cases (API failures, empty context, etc.)

**Acceptance Test**: All validation checks pass

---

## Summary

**Total Tasks**: 52 tasks across 9 phases
**Estimated Time**: 4-6 hours (real AI logic implementation)
**Complexity**: High (multiple API integrations, error handling, end-to-end flow)

**Success Criteria**:
- ✅ Real LLM responses returned through runtime engine
- ✅ Real embeddings and Qdrant search working
- ✅ Real AI Block results produced
- ✅ CLI script indexes all chapters successfully
- ✅ No broken imports, no missing modules
- ✅ All error handling in place

**Next Steps**: Proceed to `/sp.implement` to execute all tasks in order.

