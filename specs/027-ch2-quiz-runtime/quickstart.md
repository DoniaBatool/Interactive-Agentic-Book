# Quickstart: Chapter 2 Interactive Quiz Runtime Engine

**Feature**: 027-ch2-quiz-runtime
**Date**: 2025-01-27
**Purpose**: Step-by-step implementation guide for Chapter 2 quiz runtime scaffolding

## Overview

This quickstart guide provides step-by-step instructions for creating Chapter 2 quiz runtime scaffolding. The implementation involves:

1. Creating quiz runtime module (ch2_quiz_runtime.py)
2. Creating prompt template file (ch2_quiz_prompt.txt)
3. Updating runtime engine routing
4. Updating API layer
5. Extending skills layer
6. Adding quiz chunks function
7. Validating backend startup

**Estimated Time**: 30-45 minutes (scaffolding only, no real AI logic)

---

## Prerequisites

- ✅ Feature 026 (Chapter 2 ELI10 Runtime) - Reference structure exists
- ✅ Feature 024 (Chapter 2 Backend Runtime Wiring) - Runtime engine routing exists
- ✅ Skills layer exists
- ✅ Chapter 2 chunks file exists
- ✅ FastAPI backend setup
- ✅ Git branch `027-ch2-quiz-runtime` checked out

---

## Phase 1: Quiz Runtime Module (10 minutes)

### Step 1.1: Create Chapter 2 Quiz Runtime

**File**: `backend/app/ai/quiz/ch2_quiz_runtime.py`

**Action**: Create file with blueprint for quiz generation flow

**Template**:
```python
"""
Chapter 2 Interactive Quiz Runtime Engine

Orchestrates the complete quiz generation flow for ROS 2 concepts:
1. Validate request
2. Build prompt (placeholder)
3. Retrieve chapter context (placeholder)
4. Call RAG pipeline (placeholder)
5. Call LLM provider (placeholder)
6. Format output (placeholder)
"""

from typing import Dict, Any, List, Optional


async def run(
    chapter_id: int,
    num_questions: int,
    learning_objectives: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Blueprint for Chapter 2 quiz generation flow.
    
    Args:
        chapter_id: Chapter identifier (should be 2)
        num_questions: Number of questions to generate
        learning_objectives: Optional list of learning objectives to cover
    
    Returns:
        Dictionary with structured quiz:
        {
            "questions": List[Dict],      # Quiz questions (placeholder)
            "learning_objectives": List[str], # Learning objectives covered (placeholder)
            "metadata": Dict[str, Any]     # Additional metadata
        }
    
    Steps (all TODO):
    1. Validate request
    2. Build prompt (placeholder)
    3. Retrieve chapter context (placeholder)
    4. Call RAG pipeline (placeholder)
    5. Call LLM provider (placeholder)
    6. Format output (placeholder)
    """
    # Step 1: Validate request (TODO)
    # TODO: Check chapter_id is 2
    # TODO: Validate num_questions is positive
    # TODO: Validate learning_objectives if provided
    
    # Step 2: Build prompt (placeholder)
    # TODO: Load ch2_quiz_prompt.txt template
    # TODO: Replace template variables ({{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}})
    # TODO: Call build_quiz_prompt_ch2() from prompt_builder_skill
    
    # Step 3: Retrieve chapter context (placeholder)
    # TODO: Call get_chapter2_quiz_chunks() from chapter_2_chunks
    # TODO: Filter chunks by learning_objectives if provided
    
    # Step 4: Call RAG pipeline (placeholder)
    # TODO: Use RAG pipeline to get relevant ROS 2 content
    # TODO: Enhance context with RAG retrieval
    
    # Step 5: Call LLM provider (placeholder)
    # TODO: Call LLM provider with prompt and context
    # TODO: Generate quiz questions using LLM reasoning
    
    # Step 6: Format output (placeholder)
    # TODO: Call format_quiz_output_ch2() from formatting_skill
    # TODO: Format questions, answers, learning objectives
    
    # Placeholder return - no real quiz generation
    return {
        "questions": [],
        "learning_objectives": [],
        "metadata": {}
    }
```

**Validation**: File should be importable: `from app.ai.quiz.ch2_quiz_runtime import run`

---

## Phase 2: Prompt Template (5 minutes)

### Step 2.1: Create Prompt Template Directory

**Directory**: `backend/app/ai/prompts/quiz/`

**Action**: Create directory if it doesn't exist

---

### Step 2.2: Create Chapter 2 Prompt Template

**File**: `backend/app/ai/prompts/quiz/ch2_quiz_prompt.txt`

**Action**: Create file with placeholder template

**Template**:
```
TODO: Engineer full quiz prompt template for Chapter 2

Template variables:
- {{chapter_id}} - Chapter identifier (should be 2)
- {{num_questions}} - Number of questions to generate
- {{learning_objectives}} - Learning objectives to cover
- {{context}} - RAG context chunks from Chapter 2

TODO: Add system instructions for quiz generation
TODO: Add context placeholders for RAG chunks
TODO: Add structured output format instructions
TODO: Add difficulty-level tuning guidelines
TODO: Include ROS 2-specific question types
TODO: Add question format requirements (multiple choice, true/false, short answer)
```

**Validation**: File should exist and be readable

---

## Phase 3: Runtime Engine Routing (5 minutes)

### Step 3.1: Update Runtime Engine

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Add Chapter 2 quiz routing case

**Location**: In `run_ai_block()` function, before existing quiz routing

**Template**:
```python
# TODO: Chapter 2 quiz routing
# if block_type == "interactive-quiz" AND chapterId == 2:
#     from app.ai.quiz.ch2_quiz_runtime import run as ch2_quiz_run
#     result = await ch2_quiz_run(
#         chapter_id=2,
#         num_questions=request_data.get("numQuestions", 5),
#         learning_objectives=request_data.get("learningObjectives")
#     )
#     return result
```

**Validation**: File should still import correctly

---

## Phase 4: API Layer Update (5 minutes)

### Step 4.1: Update Quiz Endpoint

**File**: `backend/app/api/ai_blocks.py`

**Action**: Add Chapter 2 routing comment to quiz endpoint

**Location**: In `quiz()` function, before routing to runtime engine

**Template**:
```python
# TODO: Chapter 2 quiz routing
# if request.chapterId == 2:
#     from app.ai.quiz.ch2_quiz_runtime import run as ch2_quiz_run
#     result = await ch2_quiz_run(
#         chapter_id=2,
#         num_questions=request.numQuestions,
#         learning_objectives=request.learningObjectives
#     )
#     return result
```

**Validation**: File should still import correctly

---

## Phase 5: Skills Extension (10 minutes)

### Step 5.1: Update Prompt Builder Skill

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Action**: Add build_quiz_prompt_ch2() placeholder function

**Template**:
```python
def build_quiz_prompt_ch2(
    chapter_id: int,
    num_questions: int,
    learning_objectives: Optional[List[str]] = None
) -> str:
    """
    Build quiz prompt for Chapter 2.
    
    Args:
        chapter_id: Chapter identifier (should be 2)
        num_questions: Number of questions to generate
        learning_objectives: Optional list of learning objectives
    
    Returns:
        Constructed prompt string
    
    TODO: Implement prompt building for Chapter 2 quizzes
    TODO: Load ch2_quiz_prompt.txt template
    TODO: Replace template variables ({{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}})
    TODO: Add ROS 2-specific context
    TODO: Return constructed prompt string
    """
    # Placeholder return - no real prompt building
    return ""
```

---

### Step 5.2: Update Formatting Skill

**File**: `backend/app/ai/skills/formatting_skill.py`

**Action**: Add format_quiz_output_ch2() placeholder function

**Template**:
```python
def format_quiz_output_ch2(
    raw_response: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Format quiz output for Chapter 2.
    
    Args:
        raw_response: Raw LLM response with quiz data
    
    Returns:
        Formatted quiz structure:
        {
            "questions": List[Dict],
            "learning_objectives": List[str],
            "metadata": Dict[str, Any]
        }
    
    TODO: Implement formatting for Chapter 2 quiz output
    TODO: Parse raw LLM response
    TODO: Extract questions, answers, learning objectives
    TODO: Format ROS 2-specific metadata
    TODO: Return formatted quiz structure
    """
    # Placeholder return - no real formatting
    return {
        "questions": [],
        "learning_objectives": [],
        "metadata": {}
    }
```

**Validation**: Files should still import correctly

---

## Phase 6: Knowledge Source Preparation (5 minutes)

### Step 6.1: Update Chapter 2 Chunks

**File**: `backend/app/content/chapters/chapter_2_chunks.py`

**Action**: Add get_chapter2_quiz_chunks() placeholder function

**Template**:
```python
def get_chapter2_quiz_chunks(
    chapter_id: int = 2,
    learning_objectives: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """
    Get Chapter 2 chunks for quiz generation.
    
    Args:
        chapter_id: Chapter identifier (should be 2)
        learning_objectives: Optional list of learning objectives to filter by
    
    Returns:
        List of chapter chunks relevant for quiz generation
    
    TODO: Implement quiz-specific chunk retrieval
    TODO: Filter chunks by learning objectives if provided
    TODO: Return chunks relevant for quiz generation
    TODO: Include ROS 2-specific metadata
    """
    # Placeholder return - no real chunk retrieval
    return []
```

**Validation**: File should still import correctly

---

## Phase 7: Validation (5 minutes)

### Step 7.1: Test Backend Startup

**Command**: `cd backend && uvicorn app.main:app`

**Expected**: Backend starts without errors

**Validation Checklist**:
- [ ] No import errors
- [ ] All modules import correctly
- [ ] No syntax errors
- [ ] Backend starts successfully

---

### Step 7.2: Test Module Imports

**Command**: `cd backend && python -c "from app.ai.quiz.ch2_quiz_runtime import run; print('Import successful')"`

**Expected**: Import succeeds

**Validation**: All new modules should be importable

---

## Completion Checklist

- [ ] ch2_quiz_runtime.py created with 6-step blueprint
- [ ] ch2_quiz_prompt.txt created with template variables
- [ ] Runtime engine has Chapter 2 quiz routing (comments only)
- [ ] API layer has Chapter 2 quiz routing comments
- [ ] Skills have Chapter 2 quiz placeholder functions
- [ ] Quiz chunks function added to chapter_2_chunks.py
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
- Verify directory structure: `backend/app/ai/prompts/quiz/`
- Check file exists: `ch2_quiz_prompt.txt`
- Verify file is readable

---

## Next Steps

After completing this quickstart:

1. **Prompt Engineering**: Engineer full prompt template for ROS 2 quizzes
2. **Runtime Implementation**: Implement 6-step pipeline logic
3. **Skills Implementation**: Implement prompt building and formatting functions
4. **Testing**: Test Chapter 2 quiz generation

---

## Summary

This quickstart creates Chapter 2 quiz runtime scaffolding by:
- ✅ Creating quiz runtime module with 6-step blueprint
- ✅ Creating prompt template with ROS 2 variables
- ✅ Adding runtime engine routing (comments only)
- ✅ Adding API layer routing comments
- ✅ Extending skills with placeholder functions
- ✅ Adding quiz chunks function
- ✅ Validating backend startup

**Estimated Total Time**: 30-45 minutes (scaffolding only)

