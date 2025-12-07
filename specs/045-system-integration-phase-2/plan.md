# Implementation Plan: System Integration Layer — Phase 2 (Real AI Logic Activation)

**Branch**: `045-system-integration-phase-2` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/045-system-integration-phase-2/spec.md`

## Summary

This feature activates the FIRST working version of the full AI runtime with real LLM calls, embeddings, Qdrant search, RAG pipeline, and AI block logic. **All implementations are minimal but fully functional**—no complex ranking, caching, or parallelization.

**Primary Deliverable**: Fully functional AI runtime with real LLM responses, embeddings, Qdrant search, and RAG pipeline
**Validation**: Real LLM responses returned, real embeddings generated, real Qdrant search working, real AI block results produced, CLI script indexes chapters successfully

---

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ (FastAPI)
- Dependencies: openai, google-generativeai, qdrant-client (already in pyproject.toml)

**Primary Dependencies**:
- Feature 044: System Integration Phase 1 (scaffolding complete)
- Feature 005: AI Runtime Engine
- Feature 040-041: Chapter 3 RAG + Runtime Integration
- All chapter chunk files exist

**External Dependencies**:
- OpenAI Python SDK (`openai` package) - already in pyproject.toml
- Google Generative AI SDK (`google-generativeai` package) - needs to be added
- Qdrant Python Client (`qdrant-client` package) - already in pyproject.toml
- Environment variables: `OPENAI_API_KEY`, `GEMINI_API_KEY` (optional), `QDRANT_URL`, `QDRANT_API_KEY`

**Storage**:
- Qdrant vector database (local or cloud)
- No persistent storage modifications (read-only for chunks)

**Testing**:
- Manual: Test provider calls, embedding generation, Qdrant operations, RAG pipeline, AI block endpoints
- Automated: Placeholder test stubs (future)

**Target Platform**:
- Backend: FastAPI server
- Qdrant: Local or cloud instance

**Project Type**: AI Logic Activation / Real Implementation

**Performance Goals**:
- Provider calls: < 5 seconds per request
- Embedding generation: < 2 seconds per request
- Qdrant search: < 1 second per request
- RAG pipeline: < 10 seconds end-to-end

**Constraints**:
- MUST NOT implement complex ranking algorithms
- MUST NOT implement caching
- MUST NOT implement parallelization
- MUST NOT implement diagram generation logic (placeholder only)
- MUST NOT implement advanced quiz logic (basic generation only)
- MUST keep implementations minimal but functional
- MUST include error handling for all API calls

**Scale/Scope**:
- 2 provider implementations (OpenAI, Gemini)
- 1 embedding client
- 1 Qdrant store
- 1 RAG pipeline
- 3 skills (retrieval, prompt_builder, formatting)
- 4 subagents (Chapter 3)
- 1 runtime engine
- 1 CLI indexer
- ~2000-3000 lines of real implementation code

---

## 1. Overview

### Architecture Purpose

The System Integration Layer (Phase 2) activates real AI logic across all components: providers make real LLM calls, embedding client generates real embeddings, Qdrant store performs real vector search, RAG pipeline builds real context, and AI blocks produce real intelligent responses.

### High-Level Architecture

The activation follows a bottom-up approach:

```
CLI Indexer (index_chapter.py) ← NEW
    ↓
Chapter Chunks → Embeddings → Qdrant Upsert
    ↓
RAG Pipeline (pipeline.py) ← ACTIVATED
    ├─► Embedding Client (embedding_client.py) ← ACTIVATED
    ├─► Qdrant Store (qdrant_store.py) ← ACTIVATED
    └─► Context Building ← ACTIVATED
    ↓
Runtime Engine (engine.py) ← ACTIVATED
    ├─► Provider Factory (base_llm.py) ← ACTIVATED
    │   ├─► OpenAI Provider (openai_provider.py) ← ACTIVATED
    │   └─► Gemini Provider (gemini_provider.py) ← ACTIVATED
    ├─► Subagents (ch3/*) ← ACTIVATED
    │   └─► Skills (ch3/*) ← ACTIVATED
    └─► Response Formatting ← ACTIVATED
    ↓
API Endpoints (ai_blocks.py) ← EXISTING
    ↓
Frontend Components ← EXISTING
```

### Key Components

1. **Provider Activation**: Real OpenAI and Gemini API calls
2. **Embedding Activation**: Real embedding generation using OpenAI embeddings API
3. **Qdrant Integration**: Real vector database operations (create, upsert, search)
4. **RAG Pipeline**: Real context retrieval and assembly
5. **Skills Activation**: Real retrieval, prompt building, and formatting logic
6. **Subagent Activation**: Real subagent logic using skills
7. **Runtime Engine**: Real flow connecting all components
8. **CLI Indexer**: Real chapter indexing script

### Integration Points

- **Provider Layer**: OpenAI/Gemini SDK → Provider Classes → Runtime Engine
- **Embedding Layer**: OpenAI Embeddings API → Embedding Client → RAG Pipeline
- **Qdrant Layer**: Qdrant Client → Qdrant Store → RAG Pipeline
- **RAG Layer**: Pipeline → Runtime Engine → Subagents
- **Skills Layer**: Skills → Subagents → Runtime Engine
- **Subagent Layer**: Subagents → Runtime Engine → API Endpoints

---

## 2. Provider Activation Architecture

### OpenAI Provider

**File**: `backend/app/ai/providers/openai_provider.py`

**Implementation**:
- Use `openai` library (AsyncOpenAI client)
- Initialize client with `settings.openai_api_key`
- Use `settings.llm_model` for model selection (default: "gpt-4o-mini")
- Implement `generate()` method:
  - Build messages array (system + user prompt or messages)
  - Call `client.chat.completions.create()`
  - Extract text from response
  - Extract metadata (model, tokens, finish_reason)
  - Return formatted response

**Input/Output Contract**:
- Input: prompt, system (optional), messages (optional), temperature
- Output: {text: str, metadata: {model, tokens, finish_reason}}

**Error Handling**:
- Handle API errors (rate limits, authentication, network)
- Return error response or raise exception
- Log errors with TODO logging

---

### Gemini Provider

**File**: `backend/app/ai/providers/gemini_provider.py`

**Implementation**:
- Use `google.generativeai` library
- Initialize client with `GEMINI_API_KEY` (or `settings.gemini_api_key` if exists)
- Use `settings.llm_model` for model selection (default: "gemini-pro")
- Implement `generate()` method:
  - Build prompt (system + user prompt)
  - Call `model.generate_content()`
  - Extract text from response
  - Extract metadata (model, tokens, finish_reason)
  - Return formatted response

**Input/Output Contract**: Same as OpenAI provider

**Error Handling**: Same as OpenAI provider

---

### Provider Selection Flow

1. **Settings Lookup**:
   - Runtime engine reads `settings.ai_provider` or `settings.default_runtime_provider`
   - Falls back to "openai" if not set

2. **Factory Call**:
   - Runtime engine calls `get_provider(provider_name)`
   - Factory returns provider instance (OpenAIProvider or GeminiProvider)

3. **Provider Usage**:
   - Runtime engine calls `provider.generate(prompt, system, messages, temperature)`
   - Provider makes real API call
   - Provider returns real response

---

## 3. Embedding Strategy

### Model Selection

**Default Model**: `text-embedding-3-small` (1536 dimensions)

**Chapter-Specific Models**:
- Chapter 1: `settings.embedding_model` or default
- Chapter 2: `settings.ch2_embedding_model` or default
- Chapter 3: `settings.ch3_embedding_model` or default

**Model Selection Logic**:
```python
if chapter_id == 2 and settings.ch2_embedding_model:
    model = settings.ch2_embedding_model
elif chapter_id == 3 and settings.ch3_embedding_model:
    model = settings.ch3_embedding_model
else:
    model = settings.embedding_model or "text-embedding-3-small"
```

### Single Embedding

**Function**: `generate_embedding(text: str, chapter_id: int) -> List[float]`

**Implementation**:
- Use OpenAI embeddings API
- Handle max token size (8191 for text-embedding-3-small)
- Truncate text if exceeds max tokens (simple truncation)
- Call `client.embeddings.create(input=text, model=model)`
- Return 1536-dimensional vector

### Batch Embedding

**Function**: `batch_embed(chunks: List[str]) -> List[List[float]]`

**Implementation**:
- Use batch API endpoint for efficiency
- Handle large batches (split if needed, e.g., 100 chunks per batch)
- Call `client.embeddings.create(input=chunks, model=model)` for each batch
- Combine results
- Return list of 1536-dimensional vectors

---

## 4. RAG Pipeline Architecture

### Query Embedding

**Step**: Embed user query using `embedding_client.generate_embedding(query, chapter_id)`

**Output**: 1536-dimensional query vector

### Similarity Search

**Step**: Perform Qdrant similarity search using `qdrant_store.similarity_search(collection_name, query_vector, top_k)`

**Input**:
- Collection name (e.g., "chapter_1", "chapter_2", "chapter_3")
- Query vector (1536 dimensions)
- Top-k (default: 5)

**Output**: List of documents with id, score, payload

### Context Window Building

**Step**: Assemble retrieved chunks into context string

**Implementation**:
- Format each chunk with metadata (section_id, position)
- Combine chunks into single context string
- Limit context size (use RAG_MAX_CONTEXT env var, default: 4 chunks)
- Add section references for source citations

**Context Format**:
```
[Section: {section_id}]
{chunk_text}

[Section: {section_id}]
{chunk_text}
...
```

### Final Prompt Preparation

**Step**: Combine query + context for LLM

**Implementation**:
- Build system prompt (block-type specific)
- Include context chunks
- Include user query
- Add formatting instructions

**Prompt Format**:
```
System: {system_instructions}

Context:
{context_string}

User: {query}

Instructions: {formatting_instructions}
```

### Future Improvement Hooks

- Advanced ranking (reranking, hybrid search)
- Context compression (summarization)
- Multi-query generation
- Cross-chapter retrieval

---

## 5. Subagents Activation Flow

### How Subagents Call Skills

**Flow**:
1. Subagent receives request_data + context
2. Subagent calls `retrieval_skill.retrieve_content()` if needed
3. Subagent calls `prompt_builder_skill.build_prompt()` with context
4. Subagent calls LLM provider with prompt
5. Subagent calls `formatting_skill.format_response()` with LLM response
6. Subagent returns formatted response

### How Skills Call RAG and Providers

**Retrieval Skill**:
- Calls `run_rag_pipeline(query, chapter_id, top_k)`
- Returns retrieved chunks

**Prompt Builder Skill**:
- Takes context chunks and user input
- Builds formatted prompt string
- Returns prompt for LLM

**Formatting Skill**:
- Takes raw LLM response
- Parses and structures response
- Returns formatted response for frontend

---

## 6. Error Handling Plan

### Provider Failure Fallback

**Strategy**:
- Try primary provider (from settings)
- If fails, try fallback provider (if configured)
- If all fail, return error response

**Implementation**:
```python
try:
    provider = get_provider(settings.ai_provider)
    response = await provider.generate(prompt, system, messages, temperature)
except Exception as e:
    # TODO: Log error
    # Try fallback provider if configured
    # Return error response
    return {"error": str(e)}
```

### Empty Context Fallback

**Strategy**:
- If RAG search returns no results, use chapter metadata
- If chapter metadata unavailable, use generic response
- Log warning for empty context

**Implementation**:
```python
if not context_chunks:
    # TODO: Log warning
    # Use chapter metadata or generic response
    context = get_chapter_metadata(chapter_id).get("summary", "")
```

### Rate Limit Behavior

**Strategy**:
- Handle rate limit errors gracefully
- Return rate limit error response
- Log rate limit events
- TODO: Implement retry logic (future)

**Implementation**:
```python
except RateLimitError as e:
    # TODO: Log rate limit error
    return {"error": "Rate limit exceeded", "retry_after": e.retry_after}
```

---

## 7. CLI Indexer Plan

### End-to-End Embedding + Upsert Flow

**Steps**:
1. **Load Chapter Chunks**:
   - Import `get_chapter_chunks(chapter_id)` from `chapter_X_chunks.py`
   - Get list of chunks with metadata

2. **Generate Embeddings**:
   - Call `batch_embed(chunks)` for all chunks
   - Get list of embedding vectors

3. **Prepare Vectors**:
   - Combine chunks with embeddings
   - Create vector documents: {id, vector, payload}
   - Generate unique IDs (e.g., "ch{chapter_id}-s{section}-c{chunk}")

4. **Upsert into Qdrant**:
   - Create collection if not exists
   - Call `upsert_vectors(collection_name, vectors)`
   - Verify upsert success

5. **Logging & Durability**:
   - Log progress (chunks processed, embeddings generated, vectors upserted)
   - Log errors if any
   - Return success/failure status

### Command-Line Arguments

**Arguments**:
- `--chapter-id`: Chapter identifier (1, 2, or 3) - required
- `--collection-name`: Qdrant collection name (optional, defaults to "chapter_{id}")

**Usage**:
```bash
python backend/app/cli/index_chapter.py --chapter-id 1
python backend/app/cli/index_chapter.py --chapter-id 2 --collection-name chapter_2
python backend/app/cli/index_chapter.py --chapter-id 3
```

---

## 8. Success Criteria

- ✅ Real LLM responses returned through runtime engine
- ✅ Real embeddings and Qdrant search working
- ✅ Real AI Block results produced
- ✅ CLI script indexes all chapters successfully
- ✅ No broken imports, no missing modules
- ✅ All error handling in place

---

## 9. Dependencies + Risks

### Dependencies:
- Feature 044: System Integration Phase 1
- Feature 005: AI Runtime Engine
- Feature 040-041: Chapter 3 RAG + Runtime Integration
- All chapter chunk files exist
- External SDKs: openai, google-generativeai, qdrant-client

### Risks:
1. **Risk**: API key not configured
   - **Mitigation**: Check settings, return clear error message
2. **Risk**: Qdrant connection fails
   - **Mitigation**: Handle connection errors, return graceful fallback
3. **Risk**: Embedding generation fails
   - **Mitigation**: Handle API errors, return empty vector or error
4. **Risk**: Rate limits exceeded
   - **Mitigation**: Handle rate limit errors, return error response
5. **Risk**: Empty context from RAG
   - **Mitigation**: Use fallback context or generic response

---

## Summary

This plan establishes the complete architecture for System Integration Layer (Phase 2). The implementation activates real AI logic across all components: providers make real LLM calls, embedding client generates real embeddings, Qdrant store performs real vector search, RAG pipeline builds real context, and AI blocks produce real intelligent responses. All implementations are minimal but fully functional—no complex ranking, caching, or parallelization.

**Estimated Implementation Time**: 4-6 hours (real AI logic implementation)
**Complexity**: High (multiple API integrations, error handling, end-to-end flow)
**Dependencies**: Feature 044, 005, 040-041, external SDKs
**Out of Scope**: Complex ranking, caching, parallelization, diagram generation, advanced quiz logic

