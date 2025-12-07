# Data Model: Chapter 3 — AI Runtime Engine Integration

**Feature**: 030-ch3-ai-runtime
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 3 AI Runtime Engine integration

## Overview

This document defines the data structures, entities, and relationships for Chapter 3 AI Runtime Engine integration: API endpoints, runtime routing, subagents, skills extensions, and pipeline connection. All structures are placeholders with TODO markers for future implementation.

## Entities

### 1. API Endpoint Request/Response

**Storage**: `backend/app/api/ai_blocks.py`

**Request Models**:
```python
class AskQuestionRequest(BaseModel):
    question: str
    chapterId: Optional[int] = None
    sectionId: Optional[str] = None

class ExplainLike10Request(BaseModel):
    concept: str
    chapterId: Optional[int] = None

class QuizRequest(BaseModel):
    chapterId: int
    numQuestions: Optional[int] = 5
    learningObjectives: Optional[List[str]] = None

class DiagramRequest(BaseModel):
    diagramType: str
    chapterId: Optional[int] = None
    concepts: Optional[List[str]] = []
```

**Response Model**:
```python
class AIBlockResponse(BaseModel):
    message: str
    received: dict
```

**Validation**:
- Models must exist and be importable
- Models must have correct type hints
- Placeholder responses acceptable

**Relationship**: 1:1 with Runtime Engine (one request → one runtime call)

---

### 2. Runtime Engine Routing

**Storage**: `backend/app/ai/runtime/engine.py`

**Structure**:
```python
async def run_ai_block(block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    TODO: Chapter 3 routing
    chapter_id = request_data.get("chapterId", 1)
    if chapter_id == 3:
        # TODO: Route to Chapter 3 subagent
        # TODO: Call ch3_pipeline for RAG context
        # TODO: Select provider for Chapter 3
        # TODO: Call appropriate Chapter 3 subagent
        # TODO: Format response
    """
    return {"message": "placeholder", "data": {}}
```

**Validation**:
- Function must exist and be importable
- Function signature must match pattern
- Chapter 3 routing logic must be present (TODO acceptable)
- Placeholder return acceptable

**Relationship**: 1:N with Chapter 3 Subagents (one request → one subagent)

---

### 3. Chapter 3 Subagents

**Storage**: Python modules `backend/app/ai/subagents/ch3_*.py`

**Structure**:
```python
# ch3_ask_question_agent.py
async def ch3_ask_question_agent(
    question: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Expected Input:
        question: str
        context: {
            "context": str,
            "chunks": List[Dict],
            "query_embedding": List[float]
        }
    
    Expected Output:
        {
            "answer": str,
            "sources": List[str],
            "confidence": float
        }
    """
    return {"answer": "", "sources": [], "confidence": 0.0}

# ch3_explain_el10_agent.py
async def ch3_explain_el10_agent(
    concept: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Expected Input:
        concept: str
        context: {
            "context": str,
            "chunks": List[Dict]
        }
    
    Expected Output:
        {
            "explanation": str,
            "examples": List[str],
            "analogies": List[str]
        }
    """
    return {"explanation": "", "examples": [], "analogies": []}

# ch3_quiz_agent.py
async def ch3_quiz_agent(
    chapter_id: int,
    num_questions: int,
    learning_objectives: Optional[List[str]],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Expected Input:
        chapter_id: int (3)
        num_questions: int
        learning_objectives: Optional[List[str]]
        context: {
            "context": str,
            "chunks": List[Dict]
        }
    
    Expected Output:
        {
            "questions": List[Dict],
            "learning_objectives": List[str],
            "metadata": Dict
        }
    """
    return {"questions": [], "learning_objectives": [], "metadata": {}}

# ch3_diagram_agent.py
async def ch3_diagram_agent(
    diagram_type: str,
    concepts: List[str],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Expected Input:
        diagram_type: str
        concepts: List[str]
        context: {
            "context": str,
            "chunks": List[Dict]
        }
    
    Expected Output:
        {
            "nodes": List[Dict],
            "edges": List[Dict],
            "svg": str,
            "metadata": Dict
        }
    """
    return {"nodes": [], "edges": [], "svg": "", "metadata": {}}
```

**Validation**:
- All 4 subagent files must exist
- Function signatures must match pattern
- Placeholder returns acceptable

**Relationship**: 1:1 with Runtime Engine (one subagent per request)

---

### 4. Skills Extensions

**Storage**: `backend/app/ai/skills/prompt_builder_skill.py`, `backend/app/ai/skills/retrieval_skill.py`

**Structure**:
```python
# prompt_builder_skill.py
def build_prompt(block_type: str, user_input: str, context: List[Dict], chapter_id: int = None) -> str:
    """
    TODO: Chapter 3 support
    if chapter_id == 3:
        # TODO: Build Physical AI-specific prompts
        # TODO: Include Physical AI concepts
    """
    return ""

# retrieval_skill.py
async def retrieve_content(query: str, chapter_id: int, top_k: int = 5) -> List[Dict[str, Any]]:
    """
    TODO: Chapter 3 support
    if chapter_id == 3:
        # TODO: Use Chapter 3 RAG pipeline
        # TODO: Call ch3_pipeline.run_ch3_rag_pipeline()
    """
    return []
```

**Validation**:
- Functions must exist and be importable
- Chapter 3 TODOs must be present
- Placeholder returns acceptable

**Relationship**: N:1 with Subagents (skills used by subagents)

---

### 5. Pipeline Connection

**Storage**: `backend/app/ai/rag/ch3_pipeline.py`

**Structure**:
```python
async def run_ch3_rag_pipeline(query: str, top_k: int = 5) -> Dict[str, Any]:
    """
    TODO: Runtime engine integration
    TODO: Called from engine.py when chapterId=3
    TODO: Return context for subagents
    """
    return {"context": "", "chunks": [], "query_embedding": []}
```

**Validation**:
- Function must exist and be importable
- Function signature must match pattern
- Placeholder return acceptable

**Relationship**: 1:1 with Runtime Engine (one pipeline call per request)

---

## Relationships

### API Endpoint → Runtime Engine
- **Type**: 1:1 (one endpoint call → one runtime call)
- **Source**: `ai_blocks.py`
- **Function**: `run_ai_block(block_type, request_data)`

### Runtime Engine → RAG Pipeline
- **Type**: 1:1 (one request → one pipeline call)
- **Source**: `engine.py` → `ch3_pipeline.py`
- **Function**: `run_ch3_rag_pipeline(query, top_k)`

### Runtime Engine → Subagent
- **Type**: 1:1 (one request → one subagent)
- **Source**: `engine.py` → `ch3_*.py`
- **Function**: `ch3_*_agent(...)`

### Subagent → Skills
- **Type**: 1:N (one subagent → multiple skills)
- **Source**: `ch3_*.py` → `skills/*.py`
- **Functions**: `retrieve_content()`, `build_prompt()`, `format_response()`

## Notes

- All structures are placeholders with TODO markers
- No real AI/LLM logic implemented
- Structure only, no implementation details
- Follows Chapter 1 and Chapter 2 AI runtime patterns

