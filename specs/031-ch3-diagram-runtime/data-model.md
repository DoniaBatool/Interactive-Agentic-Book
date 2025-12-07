# Data Model: Chapter 3 Diagram Generator Runtime Layer

**Feature**: 031-ch3-diagram-runtime
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 3 diagram generation runtime

## Overview

This document defines the data structures, entities, and relationships for Chapter 3 diagram generation runtime. All structures are placeholders with TODO comments—no real AI logic is implemented.

---

## Entities

### 1. Chapter 3 Diagram Runtime Module

**Storage**: Python file `backend/app/ai/diagram/ch3_diagram_runtime.py`

**Structure**:
```python
async def run(
    diagram_type: str,
    chapter_id: int,
    concepts: List[str]
) -> Dict[str, Any]:
    """
    Blueprint for Chapter 3 diagram generation flow.
    
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
- **Parameters**: diagram_type, chapter_id (should be 3), concepts
- **Return Type**: `Dict[str, Any]`
- **Steps**: 5 steps (all TODO markers only)

**Validation**:
- Function must be importable
- All 5 steps must have TODO markers
- No real logic implementation

---

### 2. Chapter 3 Diagram Prompt Template

**Storage**: Text file `backend/app/ai/prompts/diagram/ch3_diagram_prompt.txt`

**Structure**:
```
TODO: Engineer full prompt template for Chapter 3 diagrams

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

### 3. Chapter 3 Diagram Routing

**Storage**: Python code in `backend/app/ai/runtime/engine.py`

**Structure**:
```python
# TODO: Chapter 3 diagram routing
# if block_type == "diagram" AND chapterId == 3:
#     from app.ai.diagram.ch3_diagram_runtime import run as ch3_diagram_run
#     result = await ch3_diagram_run(...)
```

**Attributes**:
- **Condition**: `block_type == "diagram" AND chapterId == 3`
- **Routing**: To `ch3_diagram_runtime.run()`
- **Implementation**: Comments only (no logic)

**Validation**:
- Routing condition must check both block_type and chapterId
- Routing must be comment-only
- TODO comments must be present

---

### 4. Chapter 3 Diagram Skills

**Storage**: Python files in `backend/app/ai/skills/`

**Files**:
- `prompt_builder_skill.py` - `build_diagram_prompt_ch3()` function
- `formatting_skill.py` - `format_diagram_output_ch3()` function

**Structure**:
```python
def build_diagram_prompt_ch3(...) -> str:
    """TODO: Implement prompt building for Chapter 3 diagrams"""
    return ""  # Placeholder

def format_diagram_output_ch3(...) -> Dict[str, Any]:
    """TODO: Implement formatting for Chapter 3 diagram output"""
    return {}  # Placeholder
```

**Attributes**:
- **Functions**: 2 functions (build_diagram_prompt_ch3, format_diagram_output_ch3)
- **Content**: Placeholder functions with TODO comments
- **Return**: Placeholder values

**Validation**:
- Functions must be importable
- Functions must have TODO comments
- No real logic implementation

---

### 5. Chapter 3 Diagram Subagent

**Storage**: Python file `backend/app/ai/subagents/ch3_diagram_agent.py` (from Feature 030)

**Structure**:
```python
async def ch3_diagram_agent(
    diagram_type: str,
    concepts: List[str],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """Chapter 3 diagram agent blueprint."""
```

**Attributes**:
- **Function Name**: `ch3_diagram_agent`
- **Parameters**: diagram_type, concepts, context
- **Return Type**: `Dict[str, Any]`
- **Status**: Already exists from Feature 030

**Validation**:
- Subagent must exist (from Feature 030)
- Runtime module must call subagent (in TODO comments)

---

## Relationships

### API → Runtime Engine → Diagram Runtime
- **Type**: 1:1:1 (API routes to runtime engine, runtime engine routes to diagram runtime)
- **Storage**: Routing logic in engine.py (comments only)
- **Chapter 3 Context**: Routes when `block_type == "diagram" AND chapterId == 3`

### Diagram Runtime → Prompt Template
- **Type**: 1:1 (runtime uses prompt template)
- **Storage**: File reference in ch3_diagram_runtime.py (TODO)
- **Chapter 3 Context**: Loads ch3_diagram_prompt.txt

### Diagram Runtime → Skills
- **Type**: 1:N (runtime uses multiple skills)
- **Storage**: Function calls in ch3_diagram_runtime.py (TODO)
- **Chapter 3 Context**: Calls build_diagram_prompt_ch3() and format_diagram_output_ch3()

### Diagram Runtime → Subagent
- **Type**: 1:1 (runtime calls subagent)
- **Storage**: Function call in ch3_diagram_runtime.py (TODO)
- **Chapter 3 Context**: Calls ch3_diagram_agent() from Feature 030

### Diagram Runtime → RAG Pipeline
- **Type**: 1:1 (runtime uses RAG pipeline)
- **Storage**: Function call in ch3_diagram_runtime.py (TODO)
- **Chapter 3 Context**: Calls ch3_pipeline for diagram context retrieval

---

## Data Flow

### Diagram Generation Flow

1. **API Endpoint**: Receives diagram request with chapterId=3 at `/ai/ch3/diagram`
2. **Runtime Engine**: Detects `block_type == "diagram" AND chapterId == 3`, routes to ch3_diagram_runtime
3. **Diagram Runtime**: Executes 5 steps (all TODO):
   - Validate diagram request
   - Build prompt (uses ch3_diagram_prompt.txt)
   - Call RAG (uses ch3_pipeline)
   - Call provider LLM (calls ch3_diagram_agent)
   - Format response (uses format_diagram_output_ch3())
4. **Response**: Returns to API endpoint

---

## Validation Rules Summary

### File Existence
- `ch3_diagram_runtime.py` must exist
- `ch3_diagram_prompt.txt` must exist
- Skills functions must exist
- `ch3_diagram_agent.py` must exist (from Feature 030)

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
- Diagram types are placeholders matching chapter-3.mdx
- Subagent (ch3_diagram_agent) already exists from Feature 030
- Runtime module orchestrates the diagram generation flow

