# Data Model: Chapter 2 Interactive Quiz Runtime Engine

**Feature**: 027-ch2-quiz-runtime
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 2 quiz generation runtime

## Overview

This document defines the data structures, entities, and relationships for Chapter 2 quiz generation runtime. All structures are placeholders with TODO comments—no real AI logic is implemented.

---

## Entities

### 1. Chapter 2 Quiz Runtime Module

**Storage**: Python file `backend/app/ai/quiz/ch2_quiz_runtime.py`

**Structure**:
```python
async def run(
    chapter_id: int,
    num_questions: int,
    learning_objectives: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Blueprint for Chapter 2 quiz generation flow.
    
    Steps (all TODO):
    1. Validate request
    2. Build prompt (placeholder)
    3. Retrieve chapter context (placeholder)
    4. Call RAG pipeline (placeholder)
    5. Call LLM provider (placeholder)
    6. Format output (placeholder)
    """
```

**Attributes**:
- **Function Name**: `run`
- **Parameters**: chapter_id (should be 2), num_questions, learning_objectives (optional)
- **Return Type**: `Dict[str, Any]`
- **Steps**: 6 steps (all TODO markers only)

**Validation**:
- Function must be importable
- All 6 steps must have TODO markers
- No real logic implementation

---

### 2. Chapter 2 Quiz Prompt Template

**Storage**: Text file `backend/app/ai/prompts/quiz/ch2_quiz_prompt.txt`

**Structure**:
```
TODO: Engineer full quiz prompt template for Chapter 2

Template variables:
- {{chapter_id}}
- {{num_questions}}
- {{learning_objectives}}
- {{context}}
```

**Attributes**:
- **File Type**: Text file (.txt)
- **Variables**: {{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}}
- **Content**: Placeholder template with TODO comments

**Validation**:
- File must exist and be readable
- All 4 variables must be present
- TODO comments must be present

---

### 3. Chapter 2 Quiz Routing

**Storage**: Python code in `backend/app/ai/runtime/engine.py`

**Structure**:
```python
# TODO: Chapter 2 quiz routing
# if block_type == "interactive-quiz" AND chapterId == 2:
#     from app.ai.quiz.ch2_quiz_runtime import run as ch2_quiz_run
#     result = await ch2_quiz_run(...)
```

**Attributes**:
- **Condition**: `block_type == "interactive-quiz" AND chapterId == 2`
- **Routing**: To `ch2_quiz_runtime.run()`
- **Implementation**: Comments only (no logic)

**Validation**:
- Routing condition must check both block_type and chapterId
- Routing must be comment-only
- TODO comments must be present

---

### 4. Chapter 2 Quiz Skills

**Storage**: Python files in `backend/app/ai/skills/`

**Files**:
- `prompt_builder_skill.py` - `build_quiz_prompt_ch2()` function
- `formatting_skill.py` - `format_quiz_output_ch2()` function

**Structure**:
```python
def build_quiz_prompt_ch2(...) -> str:
    """TODO: Implement prompt building for Chapter 2 quizzes"""
    return ""  # Placeholder

def format_quiz_output_ch2(...) -> Dict[str, Any]:
    """TODO: Implement formatting for Chapter 2 quiz output"""
    return {}  # Placeholder
```

**Attributes**:
- **Functions**: 2 functions (build_quiz_prompt_ch2, format_quiz_output_ch2)
- **Content**: Placeholder functions with TODO comments
- **Return**: Placeholder values

**Validation**:
- Functions must be importable
- Functions must have TODO comments
- No real logic implementation

---

### 5. Chapter 2 Quiz Chunks

**Storage**: Python file `backend/app/content/chapters/chapter_2_chunks.py`

**Structure**:
```python
def get_chapter2_quiz_chunks(
    chapter_id: int = 2,
    learning_objectives: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """
    Get Chapter 2 chunks for quiz generation.
    
    TODO: Implement quiz-specific chunk retrieval
    """
    return []  # Placeholder
```

**Attributes**:
- **Function Name**: `get_chapter2_quiz_chunks`
- **Parameters**: chapter_id (should be 2), learning_objectives (optional)
- **Return Type**: `List[Dict[str, Any]]`
- **Content**: Placeholder function with TODO comments

**Validation**:
- Function must be importable
- Function must have TODO comments
- No real logic implementation

---

## Relationships

### API → Runtime Engine → Quiz Runtime
- **Type**: 1:1:1 (API routes to runtime engine, runtime engine routes to quiz runtime)
- **Storage**: Routing logic in engine.py (comments only)
- **Chapter 2 Context**: Routes when `block_type == "interactive-quiz" AND chapterId == 2`

### Quiz Runtime → Prompt Template
- **Type**: 1:1 (runtime uses prompt template)
- **Storage**: File reference in ch2_quiz_runtime.py (TODO)
- **Chapter 2 Context**: Loads ch2_quiz_prompt.txt

### Quiz Runtime → Skills
- **Type**: 1:N (runtime uses multiple skills)
- **Storage**: Function calls in ch2_quiz_runtime.py (TODO)
- **Chapter 2 Context**: Calls build_quiz_prompt_ch2() and format_quiz_output_ch2()

### Quiz Runtime → Quiz Chunks
- **Type**: 1:1 (runtime uses quiz chunks)
- **Storage**: Function call in ch2_quiz_runtime.py (TODO)
- **Chapter 2 Context**: Calls get_chapter2_quiz_chunks()

---

## Data Flow

### Quiz Generation Flow

1. **API Endpoint**: Receives quiz request with chapterId=2
2. **Runtime Engine**: Detects `block_type == "interactive-quiz" AND chapterId == 2`, routes to ch2_quiz_runtime
3. **Quiz Runtime**: Executes 6 steps (all TODO):
   - Validate request
   - Build prompt (uses ch2_quiz_prompt.txt)
   - Retrieve chapter context (uses get_chapter2_quiz_chunks())
   - Call RAG pipeline (placeholder)
   - Call LLM provider (placeholder)
   - Format output (uses format_quiz_output_ch2())
4. **Response**: Returns to API endpoint

---

## Validation Rules Summary

### File Existence
- `ch2_quiz_runtime.py` must exist
- `ch2_quiz_prompt.txt` must exist
- Skills functions must exist
- Quiz chunks function must exist

### Importability
- All new modules must be importable
- No circular import errors
- No syntax errors

### Placeholder Structure
- All steps must have TODO markers
- All functions must have TODO comments
- No real logic implementation

---

## Notes

- All structures are placeholders with TODO comments
- No real AI logic is implemented
- Backend must start without errors
- All modules must import correctly
- Question formats are placeholders for future implementation

