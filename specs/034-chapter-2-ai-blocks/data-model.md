# Data Model: Chapter 2 AI Blocks Integration Layer

**Feature**: 034-chapter-2-ai-blocks
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 2 AI block integration

## Entity Definitions

### 1. API Endpoint (Primary Entity)

**Description**: FastAPI endpoint that receives Chapter 2 AI block requests

**Storage**: `backend/app/api/ai_blocks.py`

**Endpoints**:
- `POST /ai/ch2/ask`
- `POST /ai/ch2/explain`
- `POST /ai/ch2/quiz`
- `POST /ai/ch2/diagram`

**Request Structure**:
```python
{
    "question": str,           # For ask endpoint
    "concept": str,            # For explain endpoint
    "numQuestions": int,       # For quiz endpoint
    "diagramType": str,        # For diagram endpoint
    "chapterId": 2,           # Always 2 for Chapter 2
    "sectionId": str (optional) # For ask endpoint
}
```

---

### 2. Runtime Engine Router (Sub-entity)

**Description**: Routes Chapter 2 requests to appropriate subagents

**Storage**: `backend/app/ai/runtime/engine.py`

**Routing Logic**:
```python
if chapter_id == 2:
    if block_type == "ask-question":
        route_to(ch2_ask_agent)
    elif block_type == "explain-like-i-am-10":
        route_to(ch2_explain_agent)
    elif block_type == "interactive-quiz":
        route_to(ch2_quiz_agent)
    elif block_type == "generate-diagram":
        route_to(ch2_diagram_agent)
```

---

### 3. Subagent (Sub-entity)

**Description**: Chapter 2-specific agent that processes AI block requests

**Storage**: `backend/app/ai/subagents/ch2_*_agent.py`

**Subagents**:
- `ch2_ask_agent.py` - Question answering
- `ch2_explain_agent.py` - ELI10 explanations
- `ch2_quiz_agent.py` - Quiz generation
- `ch2_diagram_agent.py` - Diagram generation

**Structure**:
```python
class Ch2AskAgent:
    def run(self, input: Dict[str, Any]) -> Dict[str, Any]:
        # TODO: implement model prompting in future feature
        return placeholder_response
```

---

### 4. Skills Integration (Sub-entity)

**Description**: Chapter 2-specific skill functions for prompts and formatting

**Storage**: 
- `backend/app/ai/skills/prompt_builder_skill.py`
- `backend/app/ai/skills/formatting_skill.py`

**Functions** (TODO):
- `build_ask_prompt_ch2()`
- `build_explain_prompt_ch2()`
- `build_quiz_prompt_ch2()`
- `build_diagram_prompt_ch2()`
- `format_ask_response_ch2()`
- `format_explain_response_ch2()`
- `format_quiz_response_ch2()`
- `format_diagram_response_ch2()`

---

### 5. RAG Pipeline Router (Sub-entity)

**Description**: Routes Chapter 2 requests to Chapter 2 chunks

**Storage**: `backend/app/ai/rag/pipeline.py`

**Routing Logic**:
```python
if chapter_id == 2:
    # TODO: Load chapter_2_chunks
    # TODO: Embed query for Chapter 2
    # TODO: Search Chapter 2 collection
    # TODO: Return Chapter 2 context
```

---

## Relationships

- API Endpoint → Runtime Engine (1:1)
- Runtime Engine → Subagent (1:4, one per block type)
- Runtime Engine → RAG Pipeline (1:1)
- Subagent → Skills (N:M, multiple skills per subagent)
- RAG Pipeline → Chapter 2 Chunks (1:1)

---

## Data Flow

1. **Request**: Frontend → API Endpoint (`/ai/ch2/{block-type}`)
2. **Routing**: API → Runtime Engine (`run_ai_block()`)
3. **RAG**: Runtime Engine → RAG Pipeline (Chapter 2 context)
4. **Processing**: Runtime Engine → Subagent (with context)
5. **Skills**: Subagent → Skills (prompts, formatting)
6. **Response**: Subagent → Runtime Engine → API → Frontend

---

## Summary

All structures are placeholders with TODO comments. No business logic is implemented—only scaffolding for future implementation.

