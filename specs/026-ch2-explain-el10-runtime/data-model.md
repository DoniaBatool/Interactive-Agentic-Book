# Data Model: Chapter 2 Explain-Like-I'm-10 (ELI10) Runtime

**Feature**: 026-ch2-explain-el10-runtime
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 2 ELI10 explanation runtime

## Overview

This document defines the data structures, entities, and relationships for Chapter 2 ELI10 explanation runtime. All structures are placeholders with TODO comments—no real AI logic is implemented.

---

## Entities

### 1. Chapter 2 ELI10 Runtime Module

**Storage**: Python file `backend/app/ai/explain/ch2_el10_runtime.py`

**Structure**:
```python
async def run(
    concept: str,
    chapter_id: int,
    context: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Blueprint for Chapter 2 ELI10 explanation flow.
    
    Steps (all TODO):
    1. Validate input
    2. Build prompt (placeholder)
    3. RAG retrieve (placeholder)
    4. Call LLM (placeholder)
    5. Format output (placeholder)
    """
```

**Attributes**:
- **Function Name**: `run`
- **Parameters**: concept, chapter_id (should be 2), context (optional)
- **Return Type**: `Dict[str, Any]`
- **Steps**: 5 steps (all TODO markers only)

**Validation**:
- Function must be importable
- All 5 steps must have TODO markers
- No real logic implementation

---

### 2. Chapter 2 ELI10 Prompt Template

**Storage**: Text file `backend/app/ai/prompts/explain/ch2_el10_prompt.txt`

**Structure**:
```
TODO: Engineer full ELI10 prompt template for Chapter 2

Template variables:
- {{concept}}
- {{chapter_id}}
- {{context}}
```

**Attributes**:
- **File Type**: Text file (.txt)
- **Variables**: {{concept}}, {{chapter_id}}, {{context}}
- **Content**: Placeholder template with TODO comments

**Validation**:
- File must exist and be readable
- All 3 variables must be present
- TODO comments must be present

---

### 3. Chapter 2 ELI10 Routing

**Storage**: Python code in `backend/app/ai/runtime/engine.py`

**Structure**:
```python
# TODO: Chapter 2 ELI10 routing
# if block_type == "explain-like-i-am-10" AND chapterId == 2:
#     from app.ai.explain.ch2_el10_runtime import run as ch2_el10_run
#     result = await ch2_el10_run(...)
```

**Attributes**:
- **Condition**: `block_type == "explain-like-i-am-10" AND chapterId == 2`
- **Routing**: To `ch2_el10_runtime.run()`
- **Implementation**: Comments only (no logic)

**Validation**:
- Routing condition must check both block_type and chapterId
- Routing must be comment-only
- TODO comments must be present

---

### 4. Chapter 2 ELI10 Skills

**Storage**: Python files in `backend/app/ai/skills/`

**Files**:
- `prompt_builder_skill.py` - `build_el10_prompt_ch2()` function
- `formatting_skill.py` - `format_el10_output_ch2()` function

**Structure**:
```python
def build_el10_prompt_ch2(...) -> str:
    """TODO: Implement prompt building for Chapter 2 ELI10 explanations"""
    return ""  # Placeholder

def format_el10_output_ch2(...) -> Dict[str, Any]:
    """TODO: Implement formatting for Chapter 2 ELI10 output"""
    return {}  # Placeholder
```

**Attributes**:
- **Functions**: 2 functions (build_el10_prompt_ch2, format_el10_output_ch2)
- **Content**: Placeholder functions with TODO comments
- **Return**: Placeholder values

**Validation**:
- Functions must be importable
- Functions must have TODO comments
- No real logic implementation

---

## Relationships

### API → Runtime Engine → ELI10 Runtime
- **Type**: 1:1:1 (API routes to runtime engine, runtime engine routes to ELI10 runtime)
- **Storage**: Routing logic in engine.py (comments only)
- **Chapter 2 Context**: Routes when `block_type == "explain-like-i-am-10" AND chapterId == 2`

### ELI10 Runtime → Prompt Template
- **Type**: 1:1 (runtime uses prompt template)
- **Storage**: File reference in ch2_el10_runtime.py (TODO)
- **Chapter 2 Context**: Loads ch2_el10_prompt.txt

### ELI10 Runtime → Skills
- **Type**: 1:N (runtime uses multiple skills)
- **Storage**: Function calls in ch2_el10_runtime.py (TODO)
- **Chapter 2 Context**: Calls build_el10_prompt_ch2() and format_el10_output_ch2()

---

## Data Flow

### ELI10 Explanation Flow

1. **API Endpoint**: Receives ELI10 request with chapterId=2
2. **Runtime Engine**: Detects `block_type == "explain-like-i-am-10" AND chapterId == 2`, routes to ch2_el10_runtime
3. **ELI10 Runtime**: Executes 5 steps (all TODO):
   - Validate input
   - Build prompt (uses ch2_el10_prompt.txt)
   - RAG retrieve (placeholder)
   - Call LLM (placeholder)
   - Format output (uses format_el10_output_ch2())
4. **Response**: Returns to API endpoint

---

## Validation Rules Summary

### File Existence
- `ch2_el10_runtime.py` must exist
- `ch2_el10_prompt.txt` must exist
- Skills functions must exist

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
- Explanation formats are placeholders for future implementation

