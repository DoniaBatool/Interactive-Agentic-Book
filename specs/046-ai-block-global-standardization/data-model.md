# Data Model: Global AI Block Standardization

**Feature**: 046-ai-block-global-standardization
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for unified AI block system

## Entity Definitions

### 1. Global AI Block Contract (Primary Entity)

**Description**: Defines the unified contract for all AI blocks across all chapters

**Storage**: `specs/046-ai-block-global-standardization/contracts/ai-blocks.yaml`

**Structure**:
```yaml
GlobalContract:
  version: string
  blocks: Dict[str, BlockContract]
  rag_context_rules: RAGContextRules
  error_handling: ErrorHandlingRules
  override_rules: OverrideRules
```

**Block Types**:
- `ask-question`
- `explain-like-el10`
- `interactive-quiz`
- `diagram-generator`

---

### 2. Block Contract (Sub-entity)

**Description**: Defines input/output schema for a specific AI block type

**Structure**:
```yaml
BlockContract:
  description: string
  inputs:
    required: List[InputField]
    optional: List[InputField]
  outputs:
    structure: Dict[str, Any]
    constraints: Dict[str, List[Constraint]]
  error_format:
    structure: Dict[str, Any]
    example: Dict[str, Any]
  rag_context_usage: List[string]
```

**Input Field**:
```yaml
InputField:
  name: string
  type: string  # "string" | "integer" | "array" | "object"
  constraints: List[Constraint]
  default: Any  # Optional
```

**Constraint**:
```yaml
Constraint:
  type: string  # "min_length" | "max_length" | "min" | "max" | "pattern" | "enum"
  value: Any
```

---

### 3. Subagent Registry (Primary Entity)

**Description**: Central registry mapping (block_type, chapter_id) to subagent classes

**Storage**: `backend/app/ai/subagents/registry.py`

**Structure**:
```python
SUBAGENT_REGISTRY: Dict[Tuple[str, int], Type[BaseAgent]]

# Key: (block_type: str, chapter_id: int)
# Value: Subagent class (Type[BaseAgent])
```

**Registration Functions**:
```python
def register_subagent(
    block_type: str,
    chapter_id: int,
    subagent_class: Type[BaseAgent]
) -> None

def get_subagent(
    block_type: str,
    chapter_id: int
) -> Optional[Type[BaseAgent]]

def list_registered_subagents() -> List[Tuple[str, int]]
```

**Example Registry Entry**:
```python
SUBAGENT_REGISTRY = {
    ("ask-question", 1): Ch1AskQuestionAgent,
    ("ask-question", 2): Ch2AskQuestionAgent,
    ("ask-question", 3): Ch3AskQuestionAgent,
    ("explain-like-el10", 1): Ch1ExplainEl10Agent,
    # ... etc
}
```

---

### 4. Unified Request Structure (Data Transfer Object)

**Description**: Standardized request structure passed to all subagents

**Structure**:
```python
UnifiedRequest = {
    "block_type": str,           # "ask-question" | "explain-like-el10" | etc.
    "chapter_id": int,           # 1, 2, 3, ...
    "user_input": Dict[str, Any], # Block-specific input data
    "context": {                  # RAG context (standardized)
        "context": str,           # Assembled context string
        "chunks": List[Dict],     # Retrieved chunks with metadata
        "query_embedding": List[float]  # Query embedding vector
    },
    "overrides": Optional[Dict[str, Any]]  # Chapter-specific overrides
}
```

---

### 5. Unified Response Structure (Data Transfer Object)

**Description**: Standardized response structure returned by all subagents

**Structure** (varies by block_type):

**ask-question**:
```python
{
    "answer": str,
    "sources": List[str],
    "confidence": float
}
```

**explain-like-el10**:
```python
{
    "explanation": str,
    "analogies": List[str],
    "examples": List[str]
}
```

**interactive-quiz**:
```python
{
    "quiz_title": str,
    "questions": List[Question]
}

Question = {
    "id": str,
    "question_text": str,
    "type": str,  # "multiple-choice" | "true-false" | "short-answer"
    "options": List[str],  # Required for multiple-choice
    "correct_answer": str,
    "explanation": str
}
```

**diagram-generator**:
```python
{
    "diagram_prompt": str,  # Mermaid.js or structured description
    "diagram_type": str,
    "description": str
}
```

---

### 6. Chapter Override (Configuration Entity)

**Description**: Optional chapter-specific overrides for tone, difficulty, formatting

**Storage**: `backend/app/content/overrides/chapter_{id}.py`

**Structure**:
```python
CHAPTER_OVERRIDES = {
    "tone": str,  # "formal" | "casual" | "enthusiastic"
    "difficulty": str,  # "beginner" | "intermediate" | "advanced"
    "formatting_style": Dict[str, Any],  # Custom formatting rules
    "prompt_modifications": Dict[str, str]  # Block-specific prompt tweaks
}
```

**Example**:
```python
# backend/app/content/overrides/chapter_1.py
CHAPTER_OVERRIDES = {
    "tone": "enthusiastic",
    "difficulty": "beginner",
    "formatting_style": {
        "max_explanation_length": 500
    },
    "prompt_modifications": {
        "ask-question": "Use simple language and provide examples.",
        "explain-like-el10": "Use more analogies and real-world examples."
    }
}
```

---

### 7. Error Response Structure (Data Transfer Object)

**Description**: Standardized error response across all chapters

**Structure**:
```python
ErrorResponse = {
    "error": str,           # Human-readable error message
    "code": str,            # Error code (e.g., "INVALID_INPUT")
    "details": Dict[str, Any]  # Additional error details
}
```

**Standard Error Codes**:
- `INVALID_INPUT`: Input validation failed
- `RAG_CONTEXT_ERROR`: Failed to retrieve RAG context
- `SUBAGENT_NOT_FOUND`: No subagent registered for block type and chapter
- `LLM_PROVIDER_ERROR`: LLM provider request failed
- `FORMATTING_ERROR`: Response formatting failed

---

### 8. RAG Context Structure (Data Transfer Object)

**Description**: Standardized RAG context structure used by all chapters

**Structure**:
```python
RAGContext = {
    "context": str,                    # Assembled context string
    "chunks": List[Dict[str, Any]],    # Retrieved chunks with metadata
    "query_embedding": List[float]     # Query embedding vector
}

Chunk = {
    "id": str,
    "score": float,
    "text": str,
    "chapter_id": int,
    "section_id": str,
    "position": int,
    "metadata": Dict[str, Any]  # Full payload
}
```

**RAG Context Rules**:
- Max chunks: 5
- Max context length: 2000 characters
- Chunk selection strategy: similarity
- Context assembly: sequential

---

## Relationships

### Registry → Subagents
- One registry entry maps to one subagent class
- Multiple registry entries can map to same subagent class (if shared)
- Registry lookup: O(1) dictionary lookup

### Contract → Blocks
- One contract defines multiple block types
- Each block type has its own contract
- All block contracts share common error format

### Override → Runtime
- Override is optional (may not exist for chapter)
- Override is loaded at runtime
- Override is applied in prompt builder and formatter

### Request → Response
- One request produces one response
- Request structure is standardized
- Response structure varies by block_type but is standardized per type

---

## Data Flow

### Request Flow
```
API Endpoint
  → ai_block_router()
    → Extract query from user_input
    → Call unified RAG pipeline
    → Get context
    → Load chapter override (if exists)
    → Get subagent from registry
    → Call subagent with unified request
    → Format response using unified formatter
    → Return standardized response
```

### Registry Flow
```
Subagent Class Definition
  → Auto-register on import (or manual registration)
  → Store in SUBAGENT_REGISTRY
  → Runtime engine looks up by (block_type, chapter_id)
  → Return subagent class or None
```

### Override Flow
```
Runtime Engine
  → Check if override file exists for chapter_id
  → Load override if exists
  → Apply override in prompt builder
  → Apply override in formatter
  → Ensure override doesn't break contract
```

---

## Notes

- All data structures are standardized across chapters
- Overrides are optional and don't break base contract
- Registry enables easy extension to new chapters
- Contract-first approach ensures consistency

