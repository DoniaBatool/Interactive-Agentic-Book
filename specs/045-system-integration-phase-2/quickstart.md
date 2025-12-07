# Quickstart Guide: System Integration Layer — Phase 2

**Feature**: 045-system-integration-phase-2
**Branch**: `045-system-integration-phase-2`
**Estimated Time**: 2-3 hours (real AI logic implementation)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 044 (System Integration Phase 1) completed
- [x] Feature 005 (AI Runtime Engine) completed
- [x] Feature 040 (Chapter 3 RAG + Runtime Integration) completed
- [x] Feature 041 (Chapter 3 Subagents + Skills) completed
- [x] Git branch `045-system-integration-phase-2` checked out
- [x] Read `specs/045-system-integration-phase-2/spec.md`
- [x] Environment variables set:
  - `OPENAI_API_KEY` (required)
  - `GEMINI_API_KEY` (optional)
  - `QDRANT_URL` (required)
  - `QDRANT_API_KEY` (optional)
- [x] Python packages installed:
  - `openai` (pip install openai)
  - `google-generativeai` (pip install google-generativeai) - optional
  - `qdrant-client` (pip install qdrant-client)

## Implementation Overview

**Total Steps**: 8 phases
**Primary Deliverable**: Fully functional AI runtime with real LLM calls, embeddings, Qdrant search, and RAG pipeline
**Validation**: Real LLM responses, real embeddings, real Qdrant search, real AI block results

---

## Phase 1: Provider Activation (30 minutes)

### Step 1.1: Implement OpenAI Provider

**File**: `backend/app/ai/providers/openai_provider.py`

**Action**: Implement real generate() method:
- Import OpenAI SDK: `from openai import OpenAI`
- Initialize client with `settings.openai_api_key`
- Call OpenAI API with prompt, system, messages, temperature
- Return real response with text and metadata
- Add error handling for API failures
- Add TODO logging

### Step 1.2: Implement Gemini Provider

**File**: `backend/app/ai/providers/gemini_provider.py`

**Action**: Implement real generate() method:
- Import Gemini SDK: `import google.generativeai as genai`
- Initialize client with `GEMINI_API_KEY`
- Call Gemini API with prompt, system, messages, temperature
- Return real response with text and metadata
- Add error handling for API failures
- Add TODO logging

**Validation**: Test provider calls with simple prompts

---

## Phase 2: Embedding Activation (30 minutes)

### Step 2.1: Implement generate_embedding()

**File**: `backend/app/ai/embeddings/embedding_client.py`

**Action**: Implement real generate_embedding() function:
- Import OpenAI SDK
- Call OpenAI embeddings API (text-embedding-3-small)
- Support chapter-specific models (CH2_EMBEDDING_MODEL, CH3_EMBEDDING_MODEL)
- Handle max token size (8191)
- Truncate text if exceeds max tokens
- Return 1536-dimensional vector
- Add error handling

### Step 2.2: Implement batch_embed()

**File**: `backend/app/ai/embeddings/embedding_client.py`

**Action**: Implement real batch_embed() function:
- Use batch API endpoint for efficiency
- Handle large batches (split if needed, e.g., 100 chunks per batch)
- Return list of 1536-dimensional vectors
- Add error handling for partial failures

**Validation**: Test embedding generation with sample text

---

## Phase 3: Qdrant Integration (30 minutes)

### Step 3.1: Implement create_collection()

**File**: `backend/app/ai/rag/qdrant_store.py`

**Action**: Implement real create_collection() function:
- Import Qdrant client: `from qdrant_client import QdrantClient`
- Initialize client with `settings.qdrant_url` and `settings.qdrant_api_key`
- Configure collection: vector_size=1536, distance_metric=Cosine
- Configure HNSW index (m=16, ef_construct=100)
- Handle collection already exists error
- Return True if successful, False otherwise

### Step 3.2: Implement upsert_vectors()

**File**: `backend/app/ai/rag/qdrant_store.py`

**Action**: Implement real upsert_vectors() function:
- Use Qdrant client to batch upsert vectors
- Vector structure: {id, vector (1536 dims), payload (metadata)}
- Handle large batches (split if needed)
- Return True if successful, False otherwise

### Step 3.3: Implement similarity_search()

**File**: `backend/app/ai/rag/qdrant_store.py`

**Action**: Implement real similarity_search() function:
- Embed query text using embedding_client.generate_embedding()
- Use Qdrant client to perform vector search
- Return top_k results sorted by similarity score
- Filter by chapter_id if provided

**Validation**: Test Qdrant operations (create collection, upsert vectors, search)

---

## Phase 4: RAG Pipeline (30 minutes)

### Step 4.1: Implement run_rag_pipeline()

**File**: `backend/app/ai/rag/pipeline.py`

**Action**: Implement real run_rag_pipeline() function:
- Step 1: Load chapter chunks from chapter_X_chunks.py
- Step 2: Embed user query using embedding_client.generate_embedding()
- Step 3: Perform Qdrant search using qdrant_store.similarity_search()
- Step 4: Build context window (assemble retrieved chunks into context string)
- Step 5: Prepare final prompt (combine query + context)
- Return context dictionary with context, chunks, query_embedding
- Implement minimal, safe logic (no advanced ranking)

**Validation**: Test RAG pipeline end-to-end with sample query

---

## Phase 5: Skills Activation (20 minutes)

### Step 5.1: Implement retrieval_skill

**File**: `backend/app/ai/skills/ch3/retrieval_skill.py` (and others if exist)

**Action**: Implement real retrieval logic:
- Call RAG pipeline to get context
- Return retrieved context

### Step 5.2: Implement prompt_builder_skill

**File**: `backend/app/ai/skills/ch3/prompt_builder_skill.py` (and others if exist)

**Action**: Implement real prompt building logic:
- Build prompts for different block types (ask-question, explain-like-10, quiz, diagram)
- Combine query, context, and system instructions
- Return formatted prompt

### Step 5.3: Implement formatting_skill

**File**: `backend/app/ai/skills/ch3/formatting_skill.py` (and others if exist)

**Action**: Implement real formatting logic:
- Format LLM response for frontend
- Extract answer, sources, confidence (for ask-question)
- Extract explanation, analogies, examples (for explain-like-10)
- Extract quiz questions (for quiz)
- Extract diagram description (for diagram)
- Return formatted response

**Validation**: Test skills with sample inputs

---

## Phase 6: Subagent Activation (30 minutes)

### Step 6.1: Activate ask_question_agent

**File**: `backend/app/ai/subagents/ch3/ask_question_agent.py`

**Action**: Implement real run() method:
- Use retrieval_skill to get context
- Use prompt_builder_skill to build prompt
- Call LLM provider with prompt + context
- Use formatting_skill to format response
- Return formatted answer with sources

### Step 6.2: Activate explain_el10_agent

**File**: `backend/app/ai/subagents/ch3/explain_el10_agent.py`

**Action**: Implement real run() method:
- Use retrieval_skill to get context
- Use prompt_builder_skill to build ELI10 prompt
- Call LLM provider with prompt + context
- Use formatting_skill to format response
- Return formatted explanation with analogies and examples

### Step 6.3: Activate quiz_agent

**File**: `backend/app/ai/subagents/ch3/quiz_agent.py`

**Action**: Implement real run() method:
- Use retrieval_skill to get context (all sections)
- Use prompt_builder_skill to build quiz prompt
- Call LLM provider with prompt + context
- Use formatting_skill to format response
- Return formatted quiz with questions, answers, explanations

### Step 6.4: Activate diagram_agent

**File**: `backend/app/ai/subagents/ch3/diagram_agent.py`

**Action**: Implement real run() method:
- Use retrieval_skill to get context (optional)
- Use prompt_builder_skill to build diagram prompt
- Call LLM provider with prompt + context
- Use formatting_skill to format response
- Return formatted diagram description/prompt

**Validation**: Test subagents with sample requests

---

## Phase 7: Runtime Engine (20 minutes)

### Step 7.1: Activate real flow in engine.py

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Implement real flow for all block types:
- ask-question: Call RAG pipeline → Call LLM provider → Format response
- explain-like-10: Call RAG pipeline → Call LLM provider → Format response
- quiz: Call RAG pipeline → Call LLM provider → Format response
- diagram: Call RAG pipeline (optional) → Call LLM provider → Format response
- Connect to: RAG pipeline, LLM provider call, output formatters

**Validation**: Test AI block endpoints with real requests

---

## Phase 8: CLI Indexer (30 minutes)

### Step 8.1: Create index_chapter.py

**File**: `backend/app/cli/index_chapter.py`

**Action**: Create CLI script with index_chapter() function:
- Step 1: Read chapter chunks from chapter_X_chunks.py
- Step 2: Generate embeddings using embedding_client.batch_embed()
- Step 3: Upsert into Qdrant using qdrant_store.upsert_vectors()
- Step 4: Log progress and results
- Support command-line arguments: `--chapter-id`, `--collection-name`
- Add error handling and logging

**Validation**: Test indexing for all chapters (1, 2, 3)

---

## Success Criteria

- ✅ Real LLM responses returned through runtime engine
- ✅ Real embeddings and Qdrant search working
- ✅ Real AI Block results produced
- ✅ CLI script indexes all chapters successfully
- ✅ No broken imports, no missing modules
- ✅ All error handling in place

---

## Troubleshooting

### API Key Errors
- Verify OPENAI_API_KEY is set in environment
- Verify QDRANT_URL is set in environment
- Check API key permissions

### Qdrant Connection Errors
- Verify Qdrant instance is running
- Check QDRANT_URL and QDRANT_API_KEY
- Test connection manually

### Embedding Errors
- Verify OpenAI API key has embeddings access
- Check token limits (8191 for text-embedding-3-small)
- Verify text is not empty

### Import Errors
- Verify all packages installed (openai, qdrant-client, google-generativeai)
- Check Python version (3.11+)
- Verify import paths

---

## Notes

- This is real AI logic implementation—all API calls are real
- All implementations are minimal but fully functional
- No complex ranking, caching, or parallelization
- No diagram generation logic (placeholder only)
- No advanced quiz logic (basic generation only)
- Ready for real AI responses

