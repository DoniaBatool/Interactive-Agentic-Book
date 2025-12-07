# Dependency Map: System Integration Layer — Phase 1

**Feature**: 044-system-integration-phase-1
**Created**: 2025-01-27
**Status**: Draft

## Overview

This document maps all dependencies for the System Integration Layer (Phase 1). It documents chapter metadata dependencies, runtime dependencies, subagent/skills dependencies, and RAG dependencies to ensure proper integration and avoid circular imports.

---

## Chapter Metadata Dependencies

### Chapter 1 Metadata

**Source**: `backend/app/content/chapters/chapter_1.py`
**Exports**: `CHAPTER_METADATA` dictionary
**Dependencies**:
- None (standalone module)

**Used By**:
- `backend/app/content/chapters/registry.py` (registry registration)
- `backend/app/ai/runtime/router.py` (routing decisions)
- `backend/app/ai/rag/unified_rag.py` (RAG context)

---

### Chapter 2 Metadata

**Source**: `backend/app/content/chapters/chapter_2.py`
**Exports**: `CHAPTER_METADATA` dictionary
**Dependencies**:
- None (standalone module)

**Used By**:
- `backend/app/content/chapters/registry.py` (registry registration)
- `backend/app/ai/runtime/router.py` (routing decisions)
- `backend/app/ai/rag/unified_rag.py` (RAG context)

---

### Chapter 3 Metadata

**Source**: `backend/app/content/chapters/chapter_3.py`
**Exports**: `CHAPTER_METADATA` dictionary
**Dependencies**:
- None (standalone module)

**Used By**:
- `backend/app/content/chapters/registry.py` (registry registration)
- `backend/app/ai/runtime/router.py` (routing decisions)
- `backend/app/ai/rag/unified_rag.py` (RAG context)

---

## Runtime Dependencies

### Runtime Engine

**Source**: `backend/app/ai/runtime/engine.py`
**Exports**: `run_ai_block()` function
**Dependencies**:
- `backend/app/ai/rag/pipeline.py` (RAG pipeline)
- `backend/app/ai/providers/base_llm.py` (provider selection)
- Chapter-specific subagents (ch1, ch2, ch3)

**Used By**:
- `backend/app/api/ai_blocks.py` (API endpoints)
- `backend/app/ai/runtime/router.py` (routing layer)

---

### Runtime Router

**Source**: `backend/app/ai/runtime/router.py` (NEW)
**Exports**: `route()` function
**Dependencies**:
- `backend/app/ai/runtime/registry.py` (chapter runtime registry)
- `backend/app/ai/runtime/engine.py` (runtime engine)

**Used By**:
- `backend/app/api/ai_blocks.py` (API endpoints)

---

### Runtime Registry

**Source**: `backend/app/ai/runtime/registry.py` (NEW)
**Exports**: `CHAPTER_RUNTIMES` dictionary
**Dependencies**:
- None (standalone registry)

**Used By**:
- `backend/app/ai/runtime/router.py` (routing decisions)

---

## Subagent/Skills Dependencies

### Chapter 1 Subagents

**Source**: `backend/app/ai/subagents/ch1/` (if exists)
**Dependencies**:
- `backend/app/ai/subagents/base_agent.py` (base interface)
- `backend/app/ai/skills/ch1/` (chapter-specific skills)

**Used By**:
- `backend/app/ai/runtime/engine.py` (runtime engine routing)

---

### Chapter 2 Subagents

**Source**: `backend/app/ai/subagents/ch2/` (if exists)
**Dependencies**:
- `backend/app/ai/subagents/base_agent.py` (base interface)
- `backend/app/ai/skills/ch2/` (chapter-specific skills)

**Used By**:
- `backend/app/ai/runtime/engine.py` (runtime engine routing)

---

### Chapter 3 Subagents

**Source**: `backend/app/ai/subagents/ch3/`
**Dependencies**:
- `backend/app/ai/subagents/base_agent.py` (base interface)
- `backend/app/ai/skills/ch3/` (chapter-specific skills)

**Used By**:
- `backend/app/ai/runtime/engine.py` (runtime engine routing)

---

### Base Agent Interface

**Source**: `backend/app/ai/subagents/base_agent.py`
**Exports**: `BaseAgent` abstract class
**Dependencies**:
- None (standalone interface)

**Used By**:
- All chapter-specific subagents (ch1, ch2, ch3)

---

### Base Skill Interface

**Source**: `backend/app/ai/skills/base_skill.py`
**Exports**: `BaseSkill` abstract class
**Dependencies**:
- None (standalone interface)

**Used By**:
- All chapter-specific skills (ch1, ch2, ch3)

---

## RAG Dependencies

### Unified RAG Layer

**Source**: `backend/app/ai/rag/unified_rag.py` (NEW)
**Exports**: `get_embeddings_for_chapter()`, `retrieve_context()` functions
**Dependencies**:
- `backend/app/ai/rag/pipeline.py` (RAG pipeline)
- `backend/app/ai/embeddings/embedding_client.py` (embedding client)
- `backend/app/ai/rag/qdrant_store.py` (Qdrant store)
- Chapter chunk files (chapter_1_chunks.py, chapter_2_chunks.py, chapter_3_chunks.py)

**Used By**:
- `backend/app/ai/runtime/router.py` (routing layer)
- `backend/app/ai/runtime/engine.py` (runtime engine)

---

### RAG Pipeline

**Source**: `backend/app/ai/rag/pipeline.py`
**Exports**: `run_rag_pipeline()` function
**Dependencies**:
- `backend/app/ai/embeddings/embedding_client.py` (embedding client)
- `backend/app/ai/rag/qdrant_store.py` (Qdrant store)
- Chapter chunk files (chapter_1_chunks.py, chapter_2_chunks.py, chapter_3_chunks.py)

**Used By**:
- `backend/app/ai/rag/unified_rag.py` (unified RAG layer)
- `backend/app/ai/runtime/engine.py` (runtime engine)

---

### Embedding Client

**Source**: `backend/app/ai/embeddings/embedding_client.py`
**Exports**: `generate_embedding()`, `batch_embed()` functions
**Dependencies**:
- `backend/app/config/settings.py` (embedding model configuration)

**Used By**:
- `backend/app/ai/rag/pipeline.py` (RAG pipeline)
- `backend/app/ai/rag/unified_rag.py` (unified RAG layer)

---

### Qdrant Store

**Source**: `backend/app/ai/rag/qdrant_store.py`
**Exports**: `create_collection()`, `upsert_vectors()`, `similarity_search()` functions
**Dependencies**:
- `backend/app/config/settings.py` (Qdrant configuration)

**Used By**:
- `backend/app/ai/rag/pipeline.py` (RAG pipeline)
- `backend/app/ai/rag/unified_rag.py` (unified RAG layer)

---

## Provider Dependencies

### Base LLM Provider

**Source**: `backend/app/ai/providers/base_llm.py`
**Exports**: `BaseLLMProvider` abstract class, `get_provider()` factory (NEW)
**Dependencies**:
- None (standalone interface)

**Used By**:
- `backend/app/ai/providers/openai_provider.py` (OpenAI implementation)
- `backend/app/ai/providers/gemini_provider.py` (Gemini implementation)
- `backend/app/ai/runtime/engine.py` (runtime engine)

---

### Provider Implementations

**Source**: `backend/app/ai/providers/openai_provider.py`, `backend/app/ai/providers/gemini_provider.py`
**Dependencies**:
- `backend/app/ai/providers/base_llm.py` (base interface)
- `backend/app/config/settings.py` (provider configuration)

**Used By**:
- `backend/app/ai/providers/base_llm.py` (factory function)
- `backend/app/ai/runtime/engine.py` (runtime engine)

---

## Settings Dependencies

### Settings Module

**Source**: `backend/app/config/settings.py`
**Exports**: `Settings` class, `settings` singleton
**Dependencies**:
- Environment variables (.env file)
- Pydantic Settings

**Used By**:
- All modules (runtime, RAG, providers, embeddings, Qdrant)

---

## API Dependencies

### AI Blocks API

**Source**: `backend/app/api/ai_blocks.py`
**Exports**: API endpoints (ask-question, explain-like-10, quiz, diagram)
**Dependencies**:
- `backend/app/ai/runtime/router.py` (routing layer) (NEW)
- `backend/app/ai/runtime/engine.py` (runtime engine)

**Used By**:
- Frontend components (via HTTP requests)
- `frontend/src/integration/runtime-client.ts` (frontend client)

---

## Frontend Dependencies

### Runtime Client

**Source**: `frontend/src/integration/runtime-client.ts` (NEW)
**Exports**: `callAIBlock()`, `callChapterRuntime()` functions
**Dependencies**:
- Backend API endpoints (via HTTP)

**Used By**:
- Frontend AI block components (AskQuestionBlock, ExplainLike10Block, etc.)

---

## Dependency Graph Summary

```
API Layer (ai_blocks.py)
    ↓
Runtime Router (router.py) ← NEW
    ↓
Runtime Registry (registry.py) ← NEW
    ↓
Runtime Engine (engine.py)
    ├─► Unified RAG (unified_rag.py) ← NEW
    │   ├─► RAG Pipeline (pipeline.py)
    │   ├─► Embedding Client (embedding_client.py)
    │   └─► Qdrant Store (qdrant_store.py)
    ├─► Provider Factory (base_llm.py) ← NEW
    │   ├─► OpenAI Provider
    │   └─► Gemini Provider
    └─► Chapter Subagents (ch1, ch2, ch3)
        └─► Chapter Skills (ch1, ch2, ch3)

Chapter Metadata Registry (chapters/registry.py) ← NEW
    ├─► Chapter 1 Metadata
    ├─► Chapter 2 Metadata
    └─► Chapter 3 Metadata

Settings (settings.py)
    └─► All modules
```

---

## Circular Import Prevention

### Potential Circular Imports

1. **Runtime Engine ↔ Router**:
   - **Risk**: Runtime engine imports router, router imports runtime engine
   - **Prevention**: Router calls runtime engine, not vice versa

2. **Unified RAG ↔ Pipeline**:
   - **Risk**: Unified RAG imports pipeline, pipeline imports unified RAG
   - **Prevention**: Unified RAG calls pipeline, not vice versa

3. **Provider Factory ↔ Providers**:
   - **Risk**: Factory imports providers, providers import factory
   - **Prevention**: Factory imports providers, providers don't import factory

### Import Order

1. Settings (no dependencies)
2. Base interfaces (BaseAgent, BaseSkill, BaseLLMProvider)
3. Chapter metadata (standalone)
4. Chapter chunks (standalone)
5. Embedding client (depends on settings)
6. Qdrant store (depends on settings)
7. RAG pipeline (depends on embedding client, Qdrant store)
8. Unified RAG (depends on RAG pipeline)
9. Provider implementations (depend on base interface, settings)
10. Provider factory (depends on provider implementations)
11. Chapter skills (depend on base interface)
12. Chapter subagents (depend on base interface, skills)
13. Runtime registry (standalone)
14. Runtime router (depends on registry, runtime engine)
15. Runtime engine (depends on unified RAG, provider factory, subagents)
16. API endpoints (depend on runtime router)

---

## Summary

This dependency map documents all dependencies for the System Integration Layer (Phase 1). All dependencies are placeholder-only—no real logic implementation. The map ensures proper integration and prevents circular imports.

