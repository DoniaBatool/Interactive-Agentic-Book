# Research: Chapter 3 Subagents + Skills Integration

**Feature**: 041-ch3-subagents-skills
**Date**: 2025-01-27
**Purpose**: Document subagent + skills integration approach for Chapter 3

## Overview

This document captures research findings for integrating Chapter 3 subagents and skills into the AI runtime engine. Research focuses on scaffolding patterns, placeholder design, and architectural consistency with Chapter 2 subagents/skills integration.

## Technology Decisions

### 1. Subagent Folder Structure

**Decision**: Create ch3/ folder structure for Chapter 3 subagents

**Rationale**:
- **Organization**: Clear separation between chapters
- **Scalability**: Easy to add more chapters
- **Maintainability**: Easier to find and maintain chapter-specific code
- **Consistency**: Matches requirements specification

**Pattern**:
- `backend/app/ai/subagents/ch3/ask_question_agent.py`
- `backend/app/ai/subagents/ch3/explain_el10_agent.py`
- `backend/app/ai/subagents/ch3/quiz_agent.py`
- `backend/app/ai/subagents/ch3/diagram_agent.py`

**Alternatives Considered**:
- **Flat Structure**: Less organized, harder to scale
- **Different Naming**: Would break consistency

### 2. Skills Folder Structure

**Decision**: Create ch3/ folder structure for Chapter 3 skills

**Rationale**:
- **Organization**: Clear separation between chapters
- **Scalability**: Easy to add more chapters
- **Maintainability**: Easier to find and maintain chapter-specific code
- **Consistency**: Matches requirements specification

**Pattern**:
- `backend/app/ai/skills/ch3/retrieval_skill.py`
- `backend/app/ai/skills/ch3/prompt_builder_skill.py`
- `backend/app/ai/skills/ch3/formatting_skill.py`

### 3. Base Interface Contracts

**Decision**: Create base_agent.py and base_skill.py for shared interfaces

**Rationale**:
- **Polymorphism**: Future support for shared interfaces
- **Consistency**: Common interface for all subagents/skills
- **Extensibility**: Easy to extend with new chapters

**Pattern**:
- Abstract base classes with method definitions
- TODO markers for future polymorphism

### 4. Placeholder Design Strategy

**Decision**: Use TODO comments and empty return values

**Rationale**:
- **Clear Intent**: TODO comments explain future implementation
- **No Side Effects**: Empty returns don't break existing code
- **Easy to Find**: TODO markers make future work easy to locate

**Pattern**:
```python
class Ch3AskQuestionAgent:
    def run(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        TODO: Implement Physical AI question-answering logic
        TODO: Step 1: Use retrieval_skill
        TODO: Step 2: Use prompt_builder_skill
        TODO: Step 3: Call LLM provider
        TODO: Step 4: Use formatting_skill
        """
        return {}  # Placeholder return
```

### 5. Runtime Engine Routing

**Decision**: Add Chapter 3 routing branch in engine.py

**Rationale**:
- **Centralized Routing**: All chapter routing in one place
- **Easy to Extend**: Simple to add more chapters
- **Consistent Pattern**: Matches Chapter 2 routing

**Pattern**:
```python
if chapter_id == 3:
    # TODO: Route to Chapter 3 subagents
    # TODO: Map block_type to Ch3*Agent classes
    pass
```

---

## Component Integration Patterns

### Pattern 1: Subagent Structure

All subagents follow same structure:
```python
# backend/app/ai/subagents/ch3/{agent_name}_agent.py
class Ch3{AgentName}Agent:
    def run(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """TODO: Implement agent logic"""
        return {}  # Placeholder
```

### Pattern 2: Skills Structure

All skills follow same structure:
```python
# backend/app/ai/skills/ch3/{skill_name}_skill.py
class Ch3{SkillName}Skill:
    def method_name(self, ...) -> ...:
        """TODO: Implement skill logic"""
        return ...  # Placeholder
```

### Pattern 3: Runtime Routing

Runtime engine routes by chapterId:
```python
if chapter_id == 3:
    # TODO: Import Ch3 subagents
    # TODO: Map block_type to Ch3*Agent
    # TODO: Call subagent.run(request_data + context)
    pass
```

---

## References

- Feature 024: Chapter 2 Runtime Wiring (reference pattern)
- Feature 013: Chapter 2 Runtime Engine (routing patterns)
- Feature 040: Chapter 3 RAG + Runtime Integration (RAG context)
- Feature 039: Chapter 3 AI Blocks Integration (frontend integration)

---

## Summary

This research establishes:
- Chapter 2 subagents/skills patterns as authoritative reference
- Folder structure for Chapter 3 subagents and skills
- Base interface contracts for shared interfaces
- Placeholder design strategy with TODO comments
- Runtime engine routing pattern for Chapter 3

**Key Principles**:
- Follow Chapter 2 patterns exactly
- Use TODO comments for all future logic
- Empty return values for placeholders
- No real AI calls, LLM operations, or RAG operations
- Backend architecture ready for future implementation

