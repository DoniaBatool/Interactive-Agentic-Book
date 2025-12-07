# Quickstart: Chapter 2 Backend Runtime Wiring

**Feature**: 024-ch2-runtime-wiring
**Date**: 2025-01-27
**Purpose**: Step-by-step implementation guide for wiring Chapter 2 into backend runtime

## Overview

This quickstart guide provides step-by-step instructions for wiring Chapter 2 AI blocks into the backend runtime system. The implementation involves:

1. Updating API layer with Chapter 2 routing comments
2. Adding Chapter 2 routing placeholders to runtime engine
3. Creating Chapter 2 chunks file
4. Creating Chapter 2 subagent scaffold files
5. Extending skills layer with Chapter 2 placeholder comments
6. Validating backend startup

**Estimated Time**: 45-60 minutes (scaffolding only, no real AI logic)

---

## Prerequisites

- ✅ Feature 006 (AI Runtime Engine) - Runtime engine exists
- ✅ Feature 023 (Chapter 2 AI Block MDX Integration) - Frontend blocks exist
- ✅ Chapter 1 chunks structure exists (reference)
- ✅ Existing subagents exist (reference)
- ✅ Skills layer exists
- ✅ FastAPI backend setup
- ✅ Git branch `024-ch2-runtime-wiring` checked out

---

## Phase 1: API Layer Updates (10 minutes)

### Step 1.1: Update AI Blocks API

**File**: `backend/app/api/ai_blocks.py`

**Action**: Add Chapter 2 routing comments (if not already present)

**Check**: Verify routing to `run_ai_block()` includes chapterId=2 support

**Validation**: File should route chapterId=2 requests to runtime engine

---

## Phase 2: Runtime Engine Updates (10 minutes)

### Step 2.1: Verify Chapter 2 Routing

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Verify placeholder routing for chapterId=2 exists (may already exist from Feature 022)

**Check**: Look for `if chapter_id == 2:` block with TODO comments

**Validation**: Chapter 2 routing path should exist with placeholder comments

---

## Phase 3: RAG Layer - Chapter 2 Chunks (15 minutes)

### Step 3.1: Create Chapter 2 Chunks File

**File**: `backend/app/content/chapters/chapter_2_chunks.py`

**Action**: Create file with placeholder function matching chapter_1_chunks structure

**Template**:
```python
"""
Chapter 2 Content Chunks

Provides chapter content chunks for RAG pipeline.
Chunks are used for semantic search and context retrieval.
"""

from typing import List, Dict, Any


def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 2 with metadata.
    
    TODO: Implement chunking from Chapter 2 MDX content
    TODO: Load Chapter 2 content from frontend/docs/chapters/chapter-2.mdx
    TODO: Implement chunking strategy (same as Chapter 1)
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch2-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Cache chunks for performance
    TODO: Include ROS 2-specific metadata (concepts: nodes, topics, services, actions)
    """
    # Placeholder return - no real chunking implementation
    return []
```

**Validation**: File should be importable: `from app.content.chapters.chapter_2_chunks import get_chapter_chunks`

---

## Phase 4: Subagent Scaffold Files (15 minutes)

### Step 4.1: Create Ask Question Agent

**File**: `backend/app/ai/subagents/ch2_ask_question_agent.py`

**Action**: Create empty scaffold file

**Template**:
```python
"""
Chapter 2 Ask Question Agent

TODO: blueprint for Chapter 2 version of the agent
"""
```

---

### Step 4.2: Create Explain EL10 Agent

**File**: `backend/app/ai/subagents/ch2_explain_el10_agent.py`

**Action**: Create empty scaffold file

**Template**: Same as Step 4.1

---

### Step 4.3: Create Quiz Agent

**File**: `backend/app/ai/subagents/ch2_quiz_agent.py`

**Action**: Create empty scaffold file

**Template**: Same as Step 4.1

---

### Step 4.4: Create Diagram Agent

**File**: `backend/app/ai/subagents/ch2_diagram_agent.py`

**Action**: Create empty scaffold file

**Template**: Same as Step 4.1

**Validation**: All 4 files should be importable without errors

---

## Phase 5: Skills Layer Extensions (10 minutes)

### Step 5.1: Update Retrieval Skill

**File**: `backend/app/ai/skills/retrieval_skill.py`

**Action**: Add Chapter 2 placeholder routing comments

**Template**:
```python
# TODO: Chapter 2 placeholder routing
# TODO: Add Chapter 2 handling path
```

---

### Step 5.2: Update Prompt Builder Skill

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Action**: Add Chapter 2 placeholder routing comments

**Template**: Same as Step 5.1

---

### Step 5.3: Update Formatting Skill

**File**: `backend/app/ai/skills/formatting_skill.py`

**Action**: Add Chapter 2 placeholder routing comments

**Template**: Same as Step 5.1

**Validation**: Files should still import correctly

---

## Phase 6: Validation (10 minutes)

### Step 6.1: Test Backend Startup

**Command**: `cd backend && uvicorn app.main:app`

**Expected**: Backend starts without errors

**Validation Checklist**:
- [ ] No import errors
- [ ] All modules import correctly
- [ ] No syntax errors
- [ ] Backend starts successfully

---

### Step 6.2: Test Module Imports

**Command**: `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; print('Import successful')"`

**Expected**: Import succeeds

**Validation**: All new modules should be importable

---

## Completion Checklist

- [ ] API layer has Chapter 2 routing comments
- [ ] Runtime engine has Chapter 2 routing placeholders
- [ ] chapter_2_chunks.py created with placeholder function
- [ ] All 4 subagent files created (ch2_*_agent.py)
- [ ] Skills layer extended with Chapter 2 placeholder comments
- [ ] Backend starts without errors
- [ ] All modules import correctly
- [ ] Contract file documents runtime flow

---

## Troubleshooting

### Issue: Import errors when starting backend

**Solution**: 
- Check all new files are syntactically correct
- Verify import paths are correct
- Check for circular imports

---

### Issue: Backend doesn't start

**Solution**:
- Check for syntax errors in new files
- Verify all imports resolve
- Check runtime engine routing logic

---

## Next Steps

After completing this quickstart:

1. **RAG Implementation**: Implement real chunking logic in chapter_2_chunks.py
2. **Subagent Implementation**: Implement Chapter 2-specific agent logic
3. **Skills Implementation**: Implement Chapter 2 handling in skills
4. **Testing**: Test Chapter 2 AI block routing

---

## Summary

This quickstart wires Chapter 2 into backend runtime by:
- ✅ Adding API routing comments
- ✅ Creating runtime engine placeholders
- ✅ Creating Chapter 2 chunks file
- ✅ Creating subagent scaffold files
- ✅ Extending skills layer with comments
- ✅ Validating backend startup

**Estimated Total Time**: 45-60 minutes (scaffolding only)

