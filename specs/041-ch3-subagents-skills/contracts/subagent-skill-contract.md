# Subagent + Skill Contract: Chapter 3

**Feature**: 041-ch3-subagents-skills
**Created**: 2025-01-27
**Status**: Draft

## Overview

This contract defines the subagent and skills scaffolding for Chapter 3. All subagents and skills are placeholders with TODO markers—no real logic implemented. The contract defines expected inputs, outputs, and flow diagrams.

## Subagent Contract

### Ask Question Agent

**File**: `backend/app/ai/subagents/ch3/ask_question_agent.py`

**Class**: `Ch3AskQuestionAgent`

**Method**: `run(request: Dict[str, Any]) -> Dict[str, Any]`

**Expected Input**:
```python
{
    "question": str,                          # User question about Physical AI
    "chapterId": 3,                          # Chapter identifier
    "sectionId": Optional[str],              # Section identifier (optional)
    "context": {
        "context": str,                      # Retrieved Chapter 3 context chunks
        "chunks": List[Dict],                # Chunk metadata
        "query_embedding": List[float]       # Query vector
    }
}
```

**Expected Output** (Placeholder):
```python
{
    "answer": str,                           # Generated answer text (placeholder: "")
    "sources": List[str],                    # Source citations (placeholder: [])
    "confidence": float                      # Confidence score (placeholder: 0.0)
}
```

**Flow** (Comment-only):
```
1. TODO: Use retrieval_skill to get additional context if needed
2. TODO: Use prompt_builder_skill to construct Physical AI question-answering prompt
3. TODO: Call LLM provider with prompt + context
4. TODO: Use formatting_skill to format response with source citations
5. TODO: Return formatted answer
```

---

### Explain ELI10 Agent

**File**: `backend/app/ai/subagents/ch3/explain_el10_agent.py`

**Class**: `Ch3ExplainEl10Agent`

**Method**: `run(request: Dict[str, Any]) -> Dict[str, Any]`

**Expected Input**:
```python
{
    "concept": str,                          # Concept to explain (e.g., "computer-vision")
    "chapterId": 3,                          # Chapter identifier
    "context": {
        "context": str,                      # Retrieved Chapter 3 context chunks
        "chunks": List[Dict],                # Chunk metadata
        "query_embedding": List[float]       # Query vector
    }
}
```

**Expected Output** (Placeholder):
```python
{
    "explanation": str,                      # Simplified explanation (placeholder: "")
    "analogies": List[str],                  # Analogies used (placeholder: [])
    "examples": List[str]                    # Real-world examples (placeholder: [])
}
```

**Flow** (Comment-only):
```
1. TODO: Use retrieval_skill to get concept-specific context
2. TODO: Use prompt_builder_skill to construct ELI10 prompt
3. TODO: Call LLM provider with prompt + context
4. TODO: Use formatting_skill to format explanation
5. TODO: Return formatted explanation
```

---

### Quiz Agent

**File**: `backend/app/ai/subagents/ch3/quiz_agent.py`

**Class**: `Ch3QuizAgent`

**Method**: `run(request: Dict[str, Any]) -> Dict[str, Any]`

**Expected Input**:
```python
{
    "chapterId": 3,                          # Chapter identifier
    "numQuestions": int,                     # Number of questions (default: 5)
    "learningObjectives": Optional[List[str]], # Learning objectives to focus on
    "context": {
        "context": str,                      # Retrieved Chapter 3 context chunks
        "chunks": List[Dict],                # Chunk metadata
    }
}
```

**Expected Output** (Placeholder):
```python
{
    "questions": List[Dict],                 # Quiz questions (placeholder: [])
    "answers": List[Dict],                   # Answer keys (placeholder: [])
    "explanations": List[str]                # Explanations (placeholder: [])
}
```

**Flow** (Comment-only):
```
1. TODO: Use retrieval_skill to get quiz-relevant context
2. TODO: Use prompt_builder_skill to construct quiz generation prompt
3. TODO: Call LLM provider with prompt + context
4. TODO: Use formatting_skill to format quiz questions
5. TODO: Return formatted quiz
```

---

### Diagram Agent

**File**: `backend/app/ai/subagents/ch3/diagram_agent.py`

**Class**: `Ch3DiagramAgent`

**Method**: `run(request: Dict[str, Any]) -> Dict[str, Any]`

**Expected Input**:
```python
{
    "diagramType": str,                      # Diagram type (e.g., "sensor-types")
    "chapterId": 3,                         # Chapter identifier
    "concepts": Optional[List[str]],         # Concepts to include
    "context": {
        "context": str,                      # Retrieved Chapter 3 context chunks
        "chunks": List[Dict],                # Chunk metadata
    }
}
```

**Expected Output** (Placeholder):
```python
{
    "diagram": str,                          # Diagram description/JSON (placeholder: "")
    "metadata": Dict[str, Any]               # Diagram metadata (placeholder: {})
}
```

**Flow** (Comment-only):
```
1. TODO: Use retrieval_skill to get diagram-relevant context
2. TODO: Use prompt_builder_skill to construct diagram generation prompt
3. TODO: Call LLM provider with prompt + context
4. TODO: Use formatting_skill to format diagram output
5. TODO: Return formatted diagram
```

---

## Skills Contract

### Retrieval Skill

**File**: `backend/app/ai/skills/ch3/retrieval_skill.py`

**Class**: `Ch3RetrievalSkill`

**Methods** (Placeholder):
- `retrieve_content(query: str, chapter_id: int = 3, top_k: int = 5) -> List[Dict[str, Any]]`
- `retrieve_by_section(section_id: str, chapter_id: int = 3) -> List[Dict[str, Any]]`

**Purpose**: RAG context pulling for Chapter 3

**Flow** (Comment-only):
```
1. TODO: Call RAG pipeline with query and chapter_id=3
2. TODO: Filter chunks by section_id if provided
3. TODO: Return top-k most relevant chunks
```

---

### Prompt Builder Skill

**File**: `backend/app/ai/skills/ch3/prompt_builder_skill.py`

**Class**: `Ch3PromptBuilderSkill`

**Methods** (Placeholder):
- `build_prompt(block_type: str, request_data: Dict[str, Any], context: Dict[str, Any]) -> str`
- `build_ask_question_prompt(question: str, context: str) -> str`
- `build_eli10_prompt(concept: str, context: str) -> str`
- `build_quiz_prompt(num_questions: int, context: str) -> str`
- `build_diagram_prompt(diagram_type: str, concepts: List[str], context: str) -> str`

**Purpose**: LLM prompt building for Chapter 3

**Flow** (Comment-only):
```
1. TODO: Select prompt template based on block_type
2. TODO: Inject context into prompt template
3. TODO: Add Physical AI-specific instructions
4. TODO: Return formatted prompt string
```

---

### Formatting Skill

**File**: `backend/app/ai/skills/ch3/formatting_skill.py`

**Class**: `Ch3FormattingSkill`

**Methods** (Placeholder):
- `format_response(response: Dict[str, Any], block_type: str) -> Dict[str, Any]`
- `format_ask_question_response(answer: str, sources: List[str]) -> Dict[str, Any]`
- `format_eli10_response(explanation: str, analogies: List[str]) -> Dict[str, Any]`
- `format_quiz_response(questions: List[Dict]) -> Dict[str, Any]`
- `format_diagram_response(diagram: str, metadata: Dict) -> Dict[str, Any]`

**Purpose**: Structured response formatting for Chapter 3

**Flow** (Comment-only):
```
1. TODO: Select formatter based on block_type
2. TODO: Format response according to block type
3. TODO: Add metadata and structure
4. TODO: Return formatted response
```

---

## Runtime Routing Flow

**Flow Diagram** (Comment-only):
```
API Request (chapterId=3)
    │
    ▼
ai_blocks.py
    │
    ▼
engine.py::run_ai_block()
    │
    ├─► Check chapterId == 3
    │   │
    │   ├─► Map block_type to subagent:
    │   │   - "ask-question" → Ch3AskQuestionAgent
    │   │   - "explain-like-10" → Ch3ExplainEl10Agent
    │   │   - "interactive-quiz" → Ch3QuizAgent
    │   │   - "generate-diagram" → Ch3DiagramAgent
    │   │
    │   ├─► Call RAG pipeline (chapter_id=3)
    │   │   └─► Get context from Chapter 3 collection
    │   │
    │   ├─► Call subagent.run(request_data + context)
    │   │   │
    │   │   ├─► Use Ch3RetrievalSkill (if needed)
    │   │   ├─► Use Ch3PromptBuilderSkill
    │   │   ├─► Call LLM provider
    │   │   └─► Use Ch3FormattingSkill
    │   │
    │   └─► Return formatted response
    │
    └─► Response to frontend
```

---

## Base Interface Contracts

### Base Agent

**File**: `backend/app/ai/subagents/base_agent.py`

**Class**: `BaseAgent` (Abstract)

**Method**: `run(request: Dict[str, Any]) -> Dict[str, Any]` (Abstract)

**Purpose**: Define abstract interface for all subagents

**TODO**: Future polymorphism support

---

### Base Skill

**File**: `backend/app/ai/skills/base_skill.py`

**Class**: `BaseSkill` (Abstract)

**Purpose**: Define basic placeholder interface for all skills

**TODO**: Future polymorphism support

---

## Summary

This contract defines the complete subagent and skills scaffolding for Chapter 3. All components are placeholders with TODO markers—no real logic implemented. The contract follows Chapter 2 subagents/skills patterns exactly.

