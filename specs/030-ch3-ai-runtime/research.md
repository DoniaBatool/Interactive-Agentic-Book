# Research: Chapter 3 — AI Runtime Engine Integration

**Feature**: 030-ch3-ai-runtime
**Date**: 2025-01-27
**Purpose**: Document research findings for connecting Chapter 3 AI Blocks to the global AI Runtime Engine using the same scaffolding architecture as Chapter 1 and Chapter 2

## Overview

This document captures research findings for extending the existing AI Runtime Engine (Feature 005) to support Chapter 3 content. Research focuses on API endpoint routing, runtime engine routing patterns, subagent architecture, skills integration, and pipeline connection. Since this is a scaffolding phase, research focuses on architectural patterns and placeholder design.

## Technology Decisions

### 1. API Endpoint Routing: Chapter-Specific Endpoints

**Decision**: Add 4 new endpoints for Chapter 3 (`/ai/ch3/ask-question`, `/ai/ch3/explain-el10`, `/ai/ch3/quiz`, `/ai/ch3/diagram`)

**Rationale**:
- **Clarity**: Clear separation between chapters
- **Consistency**: Follows Chapter 2 pattern (if separate endpoints exist)
- **Flexibility**: Allows chapter-specific handling if needed
- **Future-Proof**: Supports chapter-specific features

**Endpoint Pattern**:
```python
@router.post("/ai/ch3/ask-question")
async def ch3_ask_question(request: AskQuestionRequest) -> AIBlockResponse:
    result = await run_ai_block("ask-question", request.model_dump())
    return AIBlockResponse(...)
```

**Alternatives Considered**:
- **Single Endpoint with chapterId**: Simpler but less explicit
- **Dynamic Routing**: More complex, explicit endpoints clearer

### 2. Runtime Engine Routing: Chapter ID-Based Routing

**Decision**: Extend runtime engine to route chapterId=3 calls to Chapter 3 subagents and RAG pipeline

**Rationale**:
- **Consistency**: Same pattern as Chapter 1 and Chapter 2
- **Scalability**: Easy to add more chapters
- **Clear Separation**: Each chapter has its own routing logic

**Routing Pattern**:
```python
chapter_id = request_data.get("chapterId", 1)
if chapter_id == 3:
    # TODO: Route to Chapter 3 subagent
    # TODO: Call ch3_pipeline for RAG context
    # TODO: Select provider for Chapter 3
```

**Alternatives Considered**:
- **Separate Runtime Engines**: Too complex, unnecessary separation
- **Config-Based Routing**: Adds overhead, chapterId simpler

### 3. Subagent Architecture: Chapter-Specific Subagents

**Decision**: Create Chapter 3-specific subagent files (ch3_*) that mirror Chapter 1 and Chapter 2 structure but with Physical AI context

**Rationale**:
- **Clarity**: Clear separation between chapters
- **Maintainability**: Easier to maintain chapter-specific logic
- **Physical AI Context**: Dedicated subagents can handle Physical AI-specific concepts

**Subagent Pattern**:
```python
async def ch3_ask_question_agent(question: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    Chapter 3 question-answering agent blueprint.
    Process Physical AI questions with Chapter 3 RAG context.
    """
    # TODO: Implement Physical AI question-answering logic
    return {"answer": "", "sources": [], "confidence": 0.0}
```

**Alternatives Considered**:
- **Single Subagent with Context**: Harder to manage, no chapter boundaries
- **Config-Based**: Adds complexity, separate files clearer

### 4. Skills Integration: Chapter-Aware Skills

**Decision**: Extend skills (retrieval_skill, prompt_builder_skill) with Chapter 3 TODOs

**Rationale**:
- **Reusability**: Skills can be reused across chapters
- **Consistency**: Same pattern as Chapter 1 and Chapter 2
- **Maintainability**: Clear separation of concerns

**Skills Pattern**:
```python
# retrieval_skill.py
if chapter_id == 3:
    # TODO: Use Chapter 3 RAG pipeline
    # TODO: Call ch3_pipeline.run_ch3_rag_pipeline()

# prompt_builder_skill.py
if chapter_id == 3:
    # TODO: Build Physical AI-specific prompts
    # TODO: Include Physical AI concepts
```

**Alternatives Considered**:
- **Separate Skills per Chapter**: Too much duplication
- **Config-Based**: Adds complexity, conditional routing simpler

### 5. Pipeline Connection: Placeholder Integration

**Decision**: Add placeholder call to engine pipeline in ch3_pipeline.py

**Rationale**:
- **Modularity**: Pipeline handles RAG, engine handles routing
- **Separation of Concerns**: Clear boundaries between components
- **Future-Proof**: Ready for real implementation

**Pipeline Pattern**:
```python
# ch3_pipeline.py
async def run_ch3_rag_pipeline(query: str, top_k: int = 5) -> Dict[str, Any]:
    """
    TODO: Runtime engine integration
    TODO: Called from engine.py when chapterId=3
    """
    return {"context": "", "chunks": [], "query_embedding": []}
```

**Alternatives Considered**:
- **Direct Engine Integration**: Less modular, pipeline approach clearer
- **Separate Pipeline per Block Type**: Too complex, unified pipeline simpler

## Industry References

### Runtime Engine Patterns

1. **LangChain Agent Pattern**: Router → Agent → Tools → LLM
2. **LlamaIndex Agent Pattern**: Router → Agent → Query Engine → LLM
3. **Haystack Pipeline Pattern**: Pipeline → Component → Component → LLM

### Subagent Architecture

1. **Single Responsibility**: Each subagent handles one block type
2. **Context Passing**: RAG context passed to subagents
3. **Skill Reuse**: Common skills shared across subagents

### API Routing Patterns

1. **RESTful Endpoints**: Clear, explicit endpoints per resource
2. **Chapter-Specific Routes**: Separate routes for different chapters
3. **Unified Runtime**: Single runtime engine handles all chapters

## Observations

1. **Chapter 3 Content**: Physical AI Perception Systems (sensors, computer vision, signal processing)
2. **Concepts**: Perception, sensors, computer vision, depth perception, signal processing, feature extraction
3. **AI Blocks**: 4 AI blocks (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
4. **RAG Pipeline**: ch3_pipeline.py (from Feature 029)
5. **Subagents**: 4 subagents needed (ch3_ask_question_agent, ch3_explain_el10_agent, ch3_quiz_agent, ch3_diagram_agent)

## Implementation Notes

1. **Scaffolding Only**: No real AI logic implemented in this feature
2. **Placeholder Functions**: All functions return empty dicts/lists
3. **TODO Comments**: Comprehensive TODO comments for future implementation
4. **Pattern Consistency**: Follows Chapter 1 and Chapter 2 AI runtime patterns
5. **Future Integration**: Ready for future AI logic implementation

