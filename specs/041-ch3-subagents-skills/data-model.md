# Data Model: Chapter 3 Subagents + Skills Integration

**Feature**: 041-ch3-subagents-skills
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 3 subagents + skills integration

## Entity Definitions

### 1. Chapter 3 Subagents (Primary Entity)

**Description**: Represents Chapter 3-specific subagents for AI block processing

**Storage**: Python files in `backend/app/ai/subagents/ch3/`

**Files**:
- `ask_question_agent.py`
- `explain_el10_agent.py`
- `quiz_agent.py`
- `diagram_agent.py`

**Structure**:
```python
class Ch3AskQuestionAgent:
    def run(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        TODO: Implement Physical AI question-answering logic
        """
        return {}  # Placeholder return
```

**Validation Rules**:
- All 4 files MUST exist at specified paths
- All classes MUST have `run()` method
- All methods MUST return Dict[str, Any]
- All methods MUST include TODO markers
- Placeholder returns acceptable

---

### 2. Chapter 3 Skills (Sub-entity)

**Description**: Represents Chapter 3-specific skills for subagent support

**Storage**: Python files in `backend/app/ai/skills/ch3/`

**Files**:
- `retrieval_skill.py`
- `prompt_builder_skill.py`
- `formatting_skill.py`

**Structure**:
```python
class Ch3RetrievalSkill:
    def retrieve_content(self, query: str, chapter_id: int = 3, top_k: int = 5) -> List[Dict[str, Any]]:
        """TODO: Implement retrieval logic"""
        return []  # Placeholder return
```

**Validation Rules**:
- All 3 files MUST exist at specified paths
- All classes MUST have method stubs
- All methods MUST include TODO markers
- Placeholder returns acceptable

---

### 3. Base Agent Interface (Sub-entity)

**Description**: Abstract base class for all subagents

**Storage**: `backend/app/ai/subagents/base_agent.py`

**Structure**:
```python
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    def run(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Abstract method for all subagents"""
        pass
```

**Validation Rules**:
- File MUST exist at specified path
- Class MUST be abstract
- Method MUST be abstract
- TODO markers for future polymorphism

---

### 4. Base Skill Interface (Sub-entity)

**Description**: Basic placeholder interface for all skills

**Storage**: `backend/app/ai/skills/base_skill.py`

**Structure**:
```python
from abc import ABC

class BaseSkill(ABC):
    """Base interface for all skills"""
    pass
```

**Validation Rules**:
- File MUST exist at specified path
- Class MUST be abstract
- TODO markers for future polymorphism

---

### 5. Runtime Engine Routing (Sub-entity)

**Description**: Runtime engine routing for Chapter 3

**Storage**: `backend/app/ai/runtime/engine.py`

**Structure**:
```python
if chapter_id == 3:
    # TODO: Route to Chapter 3 subagents
    # TODO: Map block_type to Ch3*Agent classes
    # TODO: Call subagent.run(request_data + context)
    pass
```

**Validation Rules**:
- Routing logic MUST have chapterId=3 branch
- Routing MUST include TODO markers
- Placeholder routing acceptable

---

## Relationships

- Runtime Engine → Chapter 3 Subagents (1:N, routes to one of 4 subagents)
- Chapter 3 Subagents → Chapter 3 Skills (1:N, uses skills for support)
- Base Agent → Chapter 3 Subagents (1:N, all subagents inherit from base)
- Base Skill → Chapter 3 Skills (1:N, all skills inherit from base)
- API Layer → Runtime Engine (1:1, routes requests)

---

## Data Integrity Constraints

1. **Chapter ID Consistency**:
   - All Chapter 3 operations MUST use chapter_id=3 or chapterId=3
   - Subagents MUST be in ch3/ folder
   - Skills MUST be in ch3/ folder

2. **Placeholder Completeness**:
   - All classes MUST have TODO markers
   - All methods MUST return placeholder values
   - No real logic implemented

3. **Import Resolution**:
   - All imports MUST resolve correctly
   - Chapter 3 subagents MUST be importable
   - Chapter 3 skills MUST be importable
   - No missing module errors

---

## Summary

All structures are placeholder-only. No real subagent logic, skills logic, or AI operations. Backend architecture ready for future AI logic implementation.

