# Quickstart Guide: AI Runtime Engine for Chapter 1

**Feature**: 005-ai-runtime-engine
**Date**: 2025-12-05
**Audience**: Developers implementing or reviewing AI runtime infrastructure scaffolding

## Overview

This guide walks you through verifying and understanding the AI Runtime Engine scaffolding for Chapter 1. After completing these steps, you'll be able to:

- ✅ Verify all AI runtime modules exist at specified paths
- ✅ Understand the architecture and data flow
- ✅ Review function signatures and TODO placeholders
- ✅ Verify backend starts with all new modules
- ✅ Understand how modules connect (even if placeholders)

**Estimated Time**: 10 minutes

## Prerequisites

Before starting, ensure you have:

1. **Feature 001 (Base Project)** complete - Backend structure, FastAPI setup
2. **Feature 004 (Chapter 1 Interactive Blocks)** complete - API endpoints in `ai_blocks.py`
3. **Backend running**: `cd backend && uvicorn app.main:app --reload` → `http://localhost:8000`

## Step-by-Step Guide

### Step 1: Verify Directory Structure

1. **Check AI Directory Structure**:
   ```bash
   # From project root
   ls -la backend/app/ai/
   
   # Should see:
   # - providers/
   # - embeddings/
   # - rag/
   # - runtime/
   # - subagents/
   # - skills/
   # - chatkit/
   ```

2. **Verify Provider Files**:
   ```bash
   ls backend/app/ai/providers/
   # Should see: base_llm.py, openai_provider.py, gemini_provider.py
   ```

3. **Verify RAG Files**:
   ```bash
   ls backend/app/ai/rag/
   # Should see: qdrant_store.py, pipeline.py
   ```

4. **Verify Subagent Files**:
   ```bash
   ls backend/app/ai/subagents/
   # Should see: ask_question_agent.py, explain_el10_agent.py, quiz_agent.py, diagram_agent.py
   ```

5. **Verify Skill Files**:
   ```bash
   ls backend/app/ai/skills/
   # Should see: retrieval_skill.py, formatting_skill.py, prompt_builder_skill.py
   ```

6. **Verify ChatKit Files**:
   ```bash
   ls backend/app/ai/chatkit/
   # Should see: session_manager.py, tools.py
   ```

### Step 2: Verify Function Signatures

1. **Check Base LLM Provider**:
   ```bash
   # View base provider interface
   cat backend/app/ai/providers/base_llm.py
   
   # Should see:
   # - Abstract class BaseLLMProvider
   # - Abstract method generate() with type hints
   # - TODO comments
   ```

2. **Check Runtime Engine**:
   ```bash
   # View runtime engine
   cat backend/app/ai/runtime/engine.py
   
   # Should see:
   # - Function run_ai_block() with type hints
   # - Flow comments explaining routing → RAG → LLM → formatting
   # - TODO placeholders
   ```

3. **Check RAG Pipeline**:
   ```bash
   # View RAG pipeline
   cat backend/app/ai/rag/pipeline.py
   
   # Should see:
   # - Function run_rag_pipeline() with type hints
   # - Step-by-step comments (5 steps)
   # - TODO placeholders for each step
   ```

### Step 3: Verify Configuration Updates

1. **Check Settings.py**:
   ```bash
   # View settings file
   grep -A 5 "AI Runtime" backend/app/config/settings.py
   
   # Should see:
   # - ai_provider: str = "openai"
   # - qdrant_collection_ch1: Optional[str] = None
   # - embedding_model: Optional[str] = None
   # - llm_model: Optional[str] = None
   ```

2. **Check .env.example**:
   ```bash
   # View environment variables
   grep -A 4 "AI Runtime" .env.example
   
   # Should see:
   # - AI_PROVIDER=openai
   # - QDRANT_COLLECTION_CH1=chapter_1_content
   # - EMBEDDING_MODEL=text-embedding-3-small
   # - LLM_MODEL=gpt-4o
   ```

### Step 4: Verify API Integration

1. **Check ai_blocks.py Updates**:
   ```bash
   # View API file
   grep -A 3 "run_ai_block" backend/app/api/ai_blocks.py
   
   # Should see:
   # - Import: from app.ai.runtime.engine import run_ai_block
   # - Endpoints calling run_ai_block()
   ```

2. **Verify Import Resolution**:
   ```bash
   # Test Python imports
   cd backend
   python -c "from app.ai.runtime.engine import run_ai_block; print('Import successful')"
   
   # Should output: Import successful
   ```

### Step 5: Verify Backend Startup

1. **Start Backend**:
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

2. **Check Startup Logs**:
   - Should see: "🚀 Starting AI Robotics Textbook API v0.1.0"
   - Should see: Configuration status for AI provider settings
   - Should NOT see: ImportError or ModuleNotFoundError

3. **Verify Health Endpoint**:
   ```bash
   curl http://localhost:8000/health
   
   # Should return: {"status": "healthy", "timestamp": "..."}
   ```

4. **Verify AI Block Endpoints**:
   ```bash
   # Test ask-question endpoint
   curl -X POST http://localhost:8000/api/ai/ask-question \
     -H "Content-Type: application/json" \
     -d '{"question": "test", "chapterId": 1}'
   
   # Should return: Response (even if placeholder)
   # Should NOT return: 500 Internal Server Error
   ```

### Step 6: Review Architecture

1. **Review Plan.md**:
   - Read `specs/005-ai-runtime-engine/plan.md`
   - Understand high-level architecture (Section 1)
   - Review module breakdown (Section 2)
   - Understand RAG pipeline flow (Section 3)

2. **Review Data Model**:
   - Read `specs/005-ai-runtime-engine/data-model.md`
   - Understand function signatures
   - Review data flow contracts

3. **Review Research**:
   - Read `specs/005-ai-runtime-engine/research.md`
   - Understand technology decisions
   - Review implementation patterns

## Verification Checklist

Before proceeding to next features, verify:

- [ ] All 17+ module files exist at specified paths
- [ ] All `__init__.py` files exist in package directories
- [ ] All function signatures have type hints
- [ ] All modules contain TODO placeholders
- [ ] `settings.py` includes all new AI configuration variables
- [ ] `.env.example` includes all new variables
- [ ] `ai_blocks.py` updated to call `run_ai_block()`
- [ ] Backend starts without import errors
- [ ] All imports resolve successfully
- [ ] API endpoints respond (even with placeholder data)

## Common Issues

### Issue 1: Import Errors

**Symptoms**: `ModuleNotFoundError` or `ImportError` when starting backend

**Solutions**:
- Verify all `__init__.py` files exist in package directories
- Check import paths match file structure
- Verify Python path includes `backend/` directory
- Test imports individually: `python -c "from app.ai.providers.base_llm import BaseLLMProvider"`

### Issue 2: Missing Files

**Symptoms**: Files don't exist at expected paths

**Solutions**:
- Check file structure matches Section 9 of plan.md
- Verify all directories created: `find backend/app/ai -type d`
- Verify all Python files created: `find backend/app/ai -name "*.py"`

### Issue 3: Configuration Not Loading

**Symptoms**: Settings not reading new environment variables

**Solutions**:
- Verify `.env` file exists and contains new variables
- Check `settings.py` includes new fields
- Restart backend after updating `.env`
- Check Pydantic settings loading: `python -c "from app.config.settings import settings; print(settings.ai_provider)"`

### Issue 4: API Endpoints Return Errors

**Symptoms**: Endpoints return 500 errors or fail to call runtime engine

**Solutions**:
- Verify `ai_blocks.py` imports `run_ai_block` correctly
- Check endpoint function calls `run_ai_block()` with correct parameters
- Verify runtime engine function exists and is importable
- Check backend logs for specific error messages

## Understanding the Architecture

### Module Relationships

```
Runtime Engine (engine.py)
    │
    ├─► Routes to Subagents
    │   ├─► ask_question_agent
    │   ├─► explain_el10_agent
    │   ├─► quiz_agent
    │   └─► diagram_agent
    │
    ├─► Coordinates RAG Pipeline
    │   ├─► chapter_1_chunks.py (chunk retrieval)
    │   ├─► embedding_client.py (embedding generation)
    │   ├─► qdrant_store.py (vector search)
    │   └─► pipeline.py (orchestration)
    │
    ├─► Selects LLM Provider
    │   ├─► BaseLLMProvider (interface)
    │   ├─► OpenAIProvider (implementation)
    │   └─► GeminiProvider (implementation)
    │
    └─► Uses Skills
        ├─► retrieval_skill.py
        ├─► formatting_skill.py
        └─► prompt_builder_skill.py
```

### Data Flow Example

**Request**: User asks "What is Physical AI?"

1. **API Layer**: `POST /api/ai/ask-question` receives request
2. **Runtime Engine**: `run_ai_block("ask-question", request_data)` routes request
3. **RAG Pipeline**: `run_rag_pipeline(query, chapter_id)` retrieves context
4. **Subagent**: `ask_question_agent(question, context)` processes request
5. **Skills**: Uses retrieval, prompt building, formatting skills
6. **LLM Provider**: `llm_provider.generate(prompt)` generates response
7. **Response**: Formatted answer returned to frontend

**Note**: All steps are placeholders in this feature. Actual implementation in future features.

## Next Steps

Once scaffolding is verified:

1. **Review Implementation Plan**: Check `specs/005-ai-runtime-engine/plan.md` for detailed architecture
2. **Review Data Models**: Check `specs/005-ai-runtime-engine/data-model.md` for function signatures
3. **Review Research**: Check `specs/005-ai-runtime-engine/research.md` for technology decisions
4. **Future Features**: Prepare for real AI implementation (RAG pipeline, provider logic, subagent business logic)

## Resources

- **Architecture Plan**: `specs/005-ai-runtime-engine/plan.md`
- **Data Models**: `specs/005-ai-runtime-engine/data-model.md`
- **Research Notes**: `specs/005-ai-runtime-engine/research.md`
- **Feature Spec**: `specs/005-ai-runtime-engine/spec.md`
- **API Documentation**: `http://localhost:8000/docs` (Swagger UI)

---

**Success!** 🎉 AI Runtime Engine scaffolding is in place and ready for future AI implementation.

