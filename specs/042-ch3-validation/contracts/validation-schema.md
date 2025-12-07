# Validation Schema: Chapter 3

**Feature**: 042-ch3-validation
**Created**: 2025-01-27
**Status**: Draft

## Overview

This contract defines the validation schema for Chapter 3. All validation checks are scaffolding-only—no real validation logic implemented. The contract defines expected validation categories, test structure, and validation report format.

## Validation Categories

### 1. Frontend MDX Validation

**File**: `frontend/docs/chapters/chapter-3.mdx`

**Validation Checks** (Placeholder):
- [ ] Exactly 7 H2 sections
- [ ] 4 diagram placeholders (kebab-case)
- [ ] 4 AI-block React components (chapterId={3})
- [ ] Glossary section with 7 terms
- [ ] YAML frontmatter completeness
- [ ] No broken Markdown syntax

**Expected Output**:
- Pass/Fail status for each check
- Error messages if validation fails

---

### 2. Backend Runtime Validation

**Files**:
- `backend/app/ai/runtime/engine.py`
- `backend/app/ai/rag/pipeline.py`
- `backend/app/ai/embeddings/*`
- `backend/app/ai/providers/*`
- `backend/app/ai/subagents/*`
- `backend/app/ai/skills/*`

**Validation Checks** (Placeholder):
- [ ] All imports resolve successfully
- [ ] No circular import errors
- [ ] ai_blocks.py routes correctly
- [ ] chapter_3_chunks.py returns placeholder chunks
- [ ] Backend starts without errors

**Expected Output**:
- Pass/Fail status for each check
- Import error details if validation fails

---

### 3. RAG Infrastructure Validation

**Files**:
- `backend/app/ai/embeddings/embedding_client.py`
- `backend/app/ai/rag/qdrant_store.py`
- `backend/app/ai/rag/pipeline.py`

**Validation Checks** (Placeholder):
- [ ] Embedding client loads successfully
- [ ] qdrant_store.py functions exist
- [ ] similarity_search() returns correct shape
- [ ] RAG pipeline has Chapter 3 branch

**Expected Output**:
- Pass/Fail status for each check
- Function signature validation results

---

### 4. Subagent & Skill Layer Validation

**Files**:
- `backend/app/ai/subagents/ch3/*`
- `backend/app/ai/skills/ch3/*`
- `backend/app/ai/subagents/base_agent.py`
- `backend/app/ai/skills/base_skill.py`

**Validation Checks** (Placeholder):
- [ ] All Ch3 subagents import successfully
- [ ] All Ch3 skills import successfully
- [ ] BaseAgent and BaseSkill classes exist
- [ ] Runtime engine routes to Chapter 3 subagents
- [ ] No circular imports

**Expected Output**:
- Pass/Fail status for each check
- Import validation results

---

### 5. Backend Startup Validation

**Command**: `uvicorn app.main:app --reload`

**Validation Checks** (Placeholder):
- [ ] Backend starts without errors
- [ ] No missing imports
- [ ] No unresolved symbols
- [ ] All routers load correctly

**Expected Output**:
- Pass/Fail status
- Startup error details if validation fails

---

### 6. API Endpoint Validation

**Endpoints**:
- `/api/ai/ask-question` (chapterId=3)
- `/api/ai/explain-like-10` (chapterId=3)
- `/api/ai/quiz` (chapterId=3)
- `/api/ai/diagram` (chapterId=3)

**Validation Checks** (Placeholder):
- [ ] All endpoints accept chapterId=3
- [ ] All endpoints return placeholder responses
- [ ] No errors in API routing

**Expected Output**:
- Pass/Fail status for each endpoint
- Response validation results

---

### 7. Frontend Build Validation

**Command**: `npm run build` (in frontend directory)

**Validation Checks** (Placeholder):
- [ ] Frontend builds successfully
- [ ] No MDX compilation errors
- [ ] All AI-block components compile

**Expected Output**:
- Pass/Fail status
- Build error details if validation fails

---

## Test Script Structure

### Test Files (Placeholder)

**Location**: `tests/ch3/`

**Files**:
- `test_frontend_build.py` - Frontend build validation
- `test_backend_startup.py` - Backend startup validation
- `test_ai_blocks_api.py` - API endpoint validation
- `test_rag_pipeline.py` - RAG pipeline validation
- `test_subagent_imports.py` - Subagent/skill import validation

**Structure** (Placeholder):
```python
"""
Test scaffolding for Chapter 3 validation.
All tests contain TODO placeholders - no real test logic.
"""

def test_validation_check():
    """Test validation check."""
    # TODO: Implement validation check
    # TODO: Run validation
    # TODO: Assert pass/fail
    pass
```

---

## Validation Report Format

**File**: `CH3_VALIDATION.md`

**Structure**:
```markdown
# Chapter 3 Validation Report

**Date**: YYYY-MM-DD
**Status**: PASS/FAIL

## Validation Results

### Frontend MDX Validation
- [ ] H2 sections: PASS/FAIL
- [ ] Diagram placeholders: PASS/FAIL
- [ ] AI-block components: PASS/FAIL
- [ ] Glossary terms: PASS/FAIL
- [ ] Frontmatter: PASS/FAIL

### Backend Runtime Validation
- [ ] Imports resolve: PASS/FAIL
- [ ] No circular imports: PASS/FAIL
- [ ] ai_blocks.py routing: PASS/FAIL
- [ ] chapter_3_chunks.py: PASS/FAIL
- [ ] Backend startup: PASS/FAIL

### RAG Infrastructure Validation
- [ ] Embedding client: PASS/FAIL
- [ ] qdrant_store.py: PASS/FAIL
- [ ] similarity_search(): PASS/FAIL
- [ ] RAG pipeline Chapter 3 branch: PASS/FAIL

### Subagent & Skill Layer Validation
- [ ] Ch3 subagents import: PASS/FAIL
- [ ] Ch3 skills import: PASS/FAIL
- [ ] BaseAgent/BaseSkill: PASS/FAIL
- [ ] Runtime engine routing: PASS/FAIL
- [ ] No circular imports: PASS/FAIL

### API Endpoint Validation
- [ ] ask-question endpoint: PASS/FAIL
- [ ] explain-like-10 endpoint: PASS/FAIL
- [ ] quiz endpoint: PASS/FAIL
- [ ] diagram endpoint: PASS/FAIL

### Frontend Build Validation
- [ ] Frontend build: PASS/FAIL
- [ ] MDX compilation: PASS/FAIL
- [ ] AI-block components: PASS/FAIL

## Summary

**Total Checks**: X
**Passed**: Y
**Failed**: Z
**Status**: PASS/FAIL
```

---

## Summary

This contract defines the complete validation schema for Chapter 3. All validation checks are placeholder-only—no real validation logic implemented. The contract follows Chapter 2 validation patterns exactly.

