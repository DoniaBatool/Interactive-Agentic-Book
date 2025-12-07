# Quickstart: Chapter 2 Explain-Like-I'm-10 (ELI10) Runtime

**Feature**: 026-ch2-explain-el10-runtime
**Date**: 2025-01-27
**Purpose**: Step-by-step implementation guide for Chapter 2 ELI10 runtime scaffolding

## Overview

This quickstart guide provides step-by-step instructions for creating Chapter 2 ELI10 runtime scaffolding. The implementation involves:

1. Creating ELI10 runtime module (ch2_el10_runtime.py)
2. Creating prompt template file (ch2_el10_prompt.txt)
3. Updating runtime engine routing
4. Updating API layer
5. Extending skills layer
6. Validating backend startup

**Estimated Time**: 30-45 minutes (scaffolding only, no real AI logic)

---

## Prerequisites

- ✅ Feature 025 (Chapter 2 Diagram Runtime) - Reference structure exists
- ✅ Feature 024 (Chapter 2 Backend Runtime Wiring) - Runtime engine routing exists
- ✅ Skills layer exists
- ✅ FastAPI backend setup
- ✅ Git branch `026-ch2-explain-el10-runtime` checked out

---

## Phase 1: ELI10 Runtime Module (10 minutes)

### Step 1.1: Create Chapter 2 ELI10 Runtime

**File**: `backend/app/ai/explain/ch2_el10_runtime.py`

**Action**: Create file with blueprint for ELI10 explanation flow

**Template**:
```python
"""
Chapter 2 Explain-Like-I'm-10 (ELI10) Runtime

Orchestrates the complete ELI10 explanation flow for ROS 2 concepts:
1. Validate input
2. Build prompt (placeholder)
3. RAG retrieve (placeholder)
4. Call LLM (placeholder)
5. Format output (placeholder)
"""

from typing import Dict, Any, Optional


async def run(
    concept: str,
    chapter_id: int,
    context: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Blueprint for Chapter 2 ELI10 explanation flow.
    
    Args:
        concept: ROS 2 concept to explain (e.g., "topics", "nodes", "services")
        chapter_id: Chapter identifier (should be 2)
        context: Optional RAG context chunks
    
    Returns:
        Dictionary with structured explanation:
        {
            "explanation": str,        # Age-appropriate explanation (placeholder)
            "examples": List[str],      # ROS 2 examples (placeholder)
            "analogies": List[str]      # Age-appropriate analogies (placeholder)
        }
    
    Steps (all TODO):
    1. Validate input
    2. Build prompt (placeholder)
    3. RAG retrieve (placeholder)
    4. Call LLM (placeholder)
    5. Format output (placeholder)
    """
    # Step 1: Validate input (TODO)
    # TODO: Check concept is valid ROS 2 concept
    # TODO: Validate chapter_id is 2
    # TODO: Validate context structure if provided
    
    # Step 2: Build prompt (placeholder)
    # TODO: Load ch2_el10_prompt.txt template
    # TODO: Replace template variables ({{concept}}, {{chapter_id}}, {{context}})
    # TODO: Call build_el10_prompt_ch2() from prompt_builder_skill
    
    # Step 3: RAG retrieve (placeholder)
    # TODO: Retrieve Chapter 2 context chunks for concept
    # TODO: Use RAG pipeline to get relevant ROS 2 content
    
    # Step 4: Call LLM (placeholder)
    # TODO: Call LLM provider with prompt and context
    # TODO: Generate explanation using LLM reasoning with ELI10 style
    
    # Step 5: Format output (placeholder)
    # TODO: Call format_el10_output_ch2() from formatting_skill
    # TODO: Format explanation, examples, analogies
    
    # Placeholder return - no real explanation generation
    return {
        "explanation": "",
        "examples": [],
        "analogies": []
    }
```

**Validation**: File should be importable: `from app.ai.explain.ch2_el10_runtime import run`

---

## Phase 2: Prompt Template (5 minutes)

### Step 2.1: Create Prompt Template Directory

**Directory**: `backend/app/ai/prompts/explain/`

**Action**: Create directory if it doesn't exist

---

### Step 2.2: Create Chapter 2 Prompt Template

**File**: `backend/app/ai/prompts/explain/ch2_el10_prompt.txt`

**Action**: Create file with placeholder template

**Template**:
```
TODO: Engineer full ELI10 prompt template for Chapter 2

Template variables:
- {{concept}} - ROS 2 concept to explain (e.g., "topics", "nodes", "services", "actions")
- {{chapter_id}} - Chapter identifier (should be 2)
- {{context}} - RAG context chunks for the concept

TODO: Add system instructions for ELI10 style (age-appropriate, simple language)
TODO: Add context placeholders for RAG chunks
TODO: Add ROS 2-specific analogies (post office, restaurant, phone calls, package delivery)
TODO: Add structured output format instructions
TODO: Add ELI10 style tuning guidelines
TODO: Include ROS 2 examples (TurtleBot 3, navigation stack, robot arm control)
```

**Validation**: File should exist and be readable

---

## Phase 3: Runtime Engine Routing (5 minutes)

### Step 3.1: Update Runtime Engine

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Add Chapter 2 ELI10 routing case

**Location**: In `run_ai_block()` function, before existing ELI10 routing

**Template**:
```python
# TODO: Chapter 2 ELI10 routing
# if block_type == "explain-like-i-am-10" AND chapterId == 2:
#     from app.ai.explain.ch2_el10_runtime import run as ch2_el10_run
#     result = await ch2_el10_run(
#         concept=request_data.get("concept", ""),
#         chapter_id=2,
#         context=request_data.get("context")
#     )
#     return result
```

**Validation**: File should still import correctly

---

## Phase 4: API Layer Update (5 minutes)

### Step 4.1: Update ELI10 Endpoint

**File**: `backend/app/api/ai_blocks.py`

**Action**: Add Chapter 2 routing comment to ELI10 endpoint

**Location**: In `explain_like_10()` function, before routing to runtime engine

**Template**:
```python
# TODO: Chapter 2 ELI10 routing
# if request.chapterId == 2:
#     from app.ai.explain.ch2_el10_runtime import run as ch2_el10_run
#     result = await ch2_el10_run(
#         concept=request.concept,
#         chapter_id=2,
#         context=None
#     )
#     return result
```

**Validation**: File should still import correctly

---

## Phase 5: Skills Extension (10 minutes)

### Step 5.1: Update Prompt Builder Skill

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Action**: Add build_el10_prompt_ch2() placeholder function

**Template**:
```python
def build_el10_prompt_ch2(
    concept: str,
    chapter_id: int,
    context: Optional[Dict[str, Any]] = None
) -> str:
    """
    Build ELI10 prompt for Chapter 2.
    
    Args:
        concept: ROS 2 concept to explain
        chapter_id: Chapter identifier (should be 2)
        context: Optional RAG context chunks
    
    Returns:
        Constructed prompt string
    
    TODO: Implement prompt building for Chapter 2 ELI10 explanations
    TODO: Load ch2_el10_prompt.txt template
    TODO: Replace template variables ({{concept}}, {{chapter_id}}, {{context}})
    TODO: Add ROS 2-specific context
    TODO: Return constructed prompt string
    """
    # Placeholder return - no real prompt building
    return ""
```

---

### Step 5.2: Update Formatting Skill

**File**: `backend/app/ai/skills/formatting_skill.py`

**Action**: Add format_el10_output_ch2() placeholder function

**Template**:
```python
def format_el10_output_ch2(
    raw_response: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Format ELI10 output for Chapter 2.
    
    Args:
        raw_response: Raw LLM response with explanation data
    
    Returns:
        Formatted explanation structure:
        {
            "explanation": str,
            "examples": List[str],
            "analogies": List[str]
        }
    
    TODO: Implement formatting for Chapter 2 ELI10 output
    TODO: Parse raw LLM response
    TODO: Extract explanation, examples, analogies
    TODO: Format ROS 2-specific metadata
    TODO: Return formatted explanation structure
    """
    # Placeholder return - no real formatting
    return {
        "explanation": "",
        "examples": [],
        "analogies": []
    }
```

**Validation**: Files should still import correctly

---

## Phase 6: Validation (5 minutes)

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

**Command**: `cd backend && python -c "from app.ai.explain.ch2_el10_runtime import run; print('Import successful')"`

**Expected**: Import succeeds

**Validation**: All new modules should be importable

---

## Completion Checklist

- [ ] ch2_el10_runtime.py created with 5-step blueprint
- [ ] ch2_el10_prompt.txt created with template variables
- [ ] Runtime engine has Chapter 2 ELI10 routing (comments only)
- [ ] API layer has Chapter 2 ELI10 routing comments
- [ ] Skills have Chapter 2 ELI10 placeholder functions
- [ ] Contract file documents expected placeholders
- [ ] Backend starts without errors
- [ ] All modules import correctly

---

## Troubleshooting

### Issue: Import errors when starting backend

**Solution**: 
- Check all new files are syntactically correct
- Verify import paths are correct
- Check for circular imports

---

### Issue: Prompt template not found

**Solution**:
- Verify directory structure: `backend/app/ai/prompts/explain/`
- Check file exists: `ch2_el10_prompt.txt`
- Verify file is readable

---

## Next Steps

After completing this quickstart:

1. **Prompt Engineering**: Engineer full prompt template for ROS 2 ELI10 explanations
2. **Runtime Implementation**: Implement 5-step pipeline logic
3. **Skills Implementation**: Implement prompt building and formatting functions
4. **Testing**: Test Chapter 2 ELI10 explanation generation

---

## Summary

This quickstart creates Chapter 2 ELI10 runtime scaffolding by:
- ✅ Creating ELI10 runtime module with 5-step blueprint
- ✅ Creating prompt template with ROS 2 variables
- ✅ Adding runtime engine routing (comments only)
- ✅ Adding API layer routing comments
- ✅ Extending skills with placeholder functions
- ✅ Validating backend startup

**Estimated Total Time**: 30-45 minutes (scaffolding only)

