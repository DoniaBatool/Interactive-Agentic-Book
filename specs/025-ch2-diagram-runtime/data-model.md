# Data Model: Chapter 2 Diagram Generator Runtime

**Feature**: 025-ch2-diagram-runtime
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 2 diagram generation runtime

## Overview

This document defines the data structures, entities, and relationships for Chapter 2 diagram generation runtime. All structures are placeholders with TODO comments—no real AI logic is implemented.

---

## Entities

### 1. Chapter 2 Diagram Runtime Module

**Storage**: Python file `backend/app/ai/diagram/ch2_diagram_runtime.py`

**Structure**:
```python
async def run(
    diagram_type: str,
    chapter_id: int,
    concepts: List[str]
) -> Dict[str, Any]:
    """
    Blueprint for Chapter 2 diagram generation flow.
    
    Steps (all TODO):
    1. Validate diagram request
    2. Build prompt (placeholder)
    3. Call RAG (placeholder)
    4. Call provider LLM (placeholder)
    5. Format response (placeholder)
    """
```

**Attributes**:
- **Function Name**: `run`
- **Parameters**: diagram_type, chapter_id (should be 2), concepts
- **Return Type**: `Dict[str, Any]`
- **Steps**: 5 steps (all TODO markers only)

**Validation**:
- Function must be importable
- All 5 steps must have TODO markers
- No real logic implementation

---

### 2. Chapter 2 Diagram Prompt Template

**Storage**: Text file `backend/app/ai/prompts/diagram/ch2_diagram_prompt.txt`

**Structure**:
```
TODO: Engineer full prompt template for Chapter 2 diagrams

Template variables:
- {{diagram_type}}
- {{chapter_id}}
- {{concepts}}
```

**Attributes**:
- **File Type**: Text file (.txt)
- **Variables**: {{diagram_type}}, {{chapter_id}}, {{concepts}}
- **Content**: Placeholder template with TODO comments

**Validation**:
- File must exist and be readable
- All 3 variables must be present
- TODO comments must be present

---

### 3. Chapter 2 Diagram Routing

**Storage**: Python code in `backend/app/ai/runtime/engine.py`

**Structure**:
```python
# TODO: Chapter 2 diagram routing
# if block_type == "diagram" AND chapterId == 2:
#     from app.ai.diagram.ch2_diagram_runtime import run as ch2_diagram_run
#     result = await ch2_diagram_run(...)
```

**Attributes**:
- **Condition**: `block_type == "diagram" AND chapterId == 2`
- **Routing**: To `ch2_diagram_runtime.run()`
- **Implementation**: Comments only (no logic)

**Validation**:
- Routing condition must check both block_type and chapterId
- Routing must be comment-only
- TODO comments must be present

---

### 4. Chapter 2 Diagram Skills

**Storage**: Python files in `backend/app/ai/skills/`

**Files**:
- `prompt_builder_skill.py` - `build_diagram_prompt_ch2()` function
- `formatting_skill.py` - `format_diagram_output_ch2()` function

**Structure**:
```python
def build_diagram_prompt_ch2(...) -> str:
    """TODO: Implement prompt building for Chapter 2 diagrams"""
    return ""  # Placeholder

def format_diagram_output_ch2(...) -> Dict[str, Any]:
    """TODO: Implement formatting for Chapter 2 diagram output"""
    return {}  # Placeholder
```

**Attributes**:
- **Functions**: 2 functions (build_diagram_prompt_ch2, format_diagram_output_ch2)
- **Content**: Placeholder functions with TODO comments
- **Return**: Placeholder values

**Validation**:
- Functions must be importable
- Functions must have TODO comments
- No real logic implementation

---

## Relationships

### API → Runtime Engine → Diagram Runtime
- **Type**: 1:1:1 (API routes to runtime engine, runtime engine routes to diagram runtime)
- **Storage**: Routing logic in engine.py (comments only)
- **Chapter 2 Context**: Routes when `block_type == "diagram" AND chapterId == 2`

### Diagram Runtime → Prompt Template
- **Type**: 1:1 (runtime uses prompt template)
- **Storage**: File reference in ch2_diagram_runtime.py (TODO)
- **Chapter 2 Context**: Loads ch2_diagram_prompt.txt

### Diagram Runtime → Skills
- **Type**: 1:N (runtime uses multiple skills)
- **Storage**: Function calls in ch2_diagram_runtime.py (TODO)
- **Chapter 2 Context**: Calls build_diagram_prompt_ch2() and format_diagram_output_ch2()

---

## Data Flow

### Diagram Generation Flow

1. **API Endpoint**: Receives diagram request with chapterId=2
2. **Runtime Engine**: Detects `block_type == "diagram" AND chapterId == 2`, routes to ch2_diagram_runtime
3. **Diagram Runtime**: Executes 5 steps (all TODO):
   - Validate diagram request
   - Build prompt (uses ch2_diagram_prompt.txt)
   - Call RAG (placeholder)
   - Call provider LLM (placeholder)
   - Format response (uses format_diagram_output_ch2())
4. **Response**: Returns to API endpoint

---

## Validation Rules Summary

### File Existence
- `ch2_diagram_runtime.py` must exist
- `ch2_diagram_prompt.txt` must exist
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
- Diagram types are placeholders matching chapter-2.mdx

