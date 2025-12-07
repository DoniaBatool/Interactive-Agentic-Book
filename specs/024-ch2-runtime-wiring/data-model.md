# Data Model: Chapter 2 Backend Runtime Wiring

**Feature**: 024-ch2-runtime-wiring
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 2 backend runtime wiring

## Overview

This document defines the data structures, entities, and relationships for wiring Chapter 2 AI blocks into the backend runtime system. All structures are placeholders with TODO comments—no real AI logic is implemented.

---

## Entities

### 1. Chapter 2 Runtime Routing

**Storage**: Python code in `backend/app/ai/runtime/engine.py`

**Structure**:
```python
# Runtime engine routing for chapterId=2
chapter_id = request_data.get("chapterId", 1)
if chapter_id == 2:
    # TODO: Chapter 2 routing
    # Placeholder routing with comments
```

**Attributes**:
- **Chapter ID**: 2 (fixed for Chapter 2)
- **Routing Path**: Chapter 2 handling path (placeholder)
- **Subagent Mapping**: ch2_*_agent.py files (placeholders)

**Validation**:
- chapterId must be 2 for Chapter 2 routing
- Routing path must exist (placeholder with TODO comments)

---

### 2. Chapter 2 Chunks File

**Storage**: Python file `backend/app/content/chapters/chapter_2_chunks.py`

**Structure**:
```python
def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 2 with metadata.
    TODO: Implement chunking logic
    """
    return []  # Placeholder
```

**Attributes**:
- **Function Name**: `get_chapter_chunks`
- **Parameters**: `chapter_id` (default: 2)
- **Return Type**: `List[Dict[str, Any]]`
- **Return Value**: Empty list or placeholder structure

**Validation**:
- Function must be importable
- Function signature must match chapter_1_chunks structure
- Return type must be List[Dict[str, Any]]

---

### 3. Chapter 2 Subagent Files

**Storage**: Python files in `backend/app/ai/subagents/`

**Files**:
- `ch2_ask_question_agent.py`
- `ch2_explain_el10_agent.py`
- `ch2_quiz_agent.py`
- `ch2_diagram_agent.py`

**Structure**:
```python
"""
Chapter 2 [Agent Type] Agent

TODO: blueprint for Chapter 2 version of the agent
"""
```

**Attributes**:
- **File Name**: ch2_*_agent.py pattern
- **Content**: Empty scaffold with TODO comment
- **Purpose**: Placeholder for future Chapter 2-specific agent logic

**Validation**:
- All 4 files must exist
- Files must be importable
- Files must contain TODO comment

---

### 4. Skills Layer Extensions

**Storage**: Python files in `backend/app/ai/skills/`

**Files**:
- `retrieval_skill.py`
- `prompt_builder_skill.py`
- `formatting_skill.py`

**Structure**:
```python
# Chapter 2 placeholder routing
# TODO: Add Chapter 2 handling path
```

**Attributes**:
- **Extension Type**: Comment-only (no logic)
- **Purpose**: Document expected Chapter 2 handling paths

**Validation**:
- Files must exist and be importable
- Chapter 2 placeholder comments must be present

---

## Relationships

### API → Runtime Engine
- **Type**: 1:1 (API routes to runtime engine)
- **Storage**: `backend/app/api/ai_blocks.py` calls `run_ai_block()`
- **Chapter 2 Context**: chapterId=2 passed in request_data

### Runtime Engine → Chapter 2 Subagents
- **Type**: 1:N (runtime engine routes to one of 4 subagents)
- **Storage**: Routing logic in `engine.py` (placeholder)
- **Chapter 2 Context**: Routes to ch2_*_agent.py files

### Runtime Engine → Chapter 2 Chunks
- **Type**: 1:1 (runtime engine calls get_chapter_chunks)
- **Storage**: Import from `chapter_2_chunks.py` (placeholder)
- **Chapter 2 Context**: chapter_id=2 parameter

### Skills → Chapter 2
- **Type**: N:1 (multiple skills extend for Chapter 2)
- **Storage**: Comment-only extensions in skills files
- **Chapter 2 Context**: Placeholder routing comments

---

## Data Flow

### Request Flow

1. **API Endpoint**: Receives request with chapterId=2
2. **Runtime Engine**: Detects chapterId=2, routes to Chapter 2 path
3. **Chapter 2 Chunks**: Loads chunks (placeholder)
4. **Chapter 2 Subagent**: Processes request (placeholder)
5. **Skills Layer**: Applies skills (placeholder)
6. **Response**: Returns to API endpoint

---

## Validation Rules Summary

### File Existence
- `chapter_2_chunks.py` must exist
- All 4 subagent files must exist
- Skills files must exist

### Importability
- All new modules must be importable
- No circular import errors
- No syntax errors

### Structure Parity
- `chapter_2_chunks.py` must match `chapter_1_chunks.py` structure
- Subagent files must follow naming pattern (ch2_*_agent.py)

---

## Notes

- All structures are placeholders with TODO comments
- No real AI logic is implemented
- Backend must start without errors
- All modules must import correctly

