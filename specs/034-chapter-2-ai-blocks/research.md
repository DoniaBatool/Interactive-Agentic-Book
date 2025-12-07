# Research: Chapter 2 AI Blocks Integration Layer

**Feature**: 034-chapter-2-ai-blocks
**Date**: 2025-01-27
**Purpose**: Document integration approach for enabling AI blocks in Chapter 2 using existing infrastructure

## Overview

This document captures research findings for integrating AI-interactive blocks into Chapter 2 (Mechanical Systems) using the existing Runtime Engine, RAG pipeline, subagents, and skills. Since this is a scaffolding phase, research focuses on integration patterns, knowledge source mapping, and Mechanical Systems-specific context handling.

## Technology Decisions

### 1. Reuse Existing Components and Infrastructure

**Decision**: Reuse all AI block components, runtime engine, subagents, and API endpoints from Feature 005 (Chapter 1 AI blocks) and Feature 030 (Chapter 3 AI runtime)

**Rationale**:
- **Consistency**: Same UI/UX across all chapters
- **Efficiency**: No need to recreate components or infrastructure
- **Maintainability**: Single source of truth for AI block functionality
- **Proven Pattern**: Chapter 1 and Chapter 3 integration already tested

**Integration Approach**:
- Import existing React components in chapter-2.mdx
- Route Chapter 2 requests through new API endpoints with chapterId=2
- Extend runtime engine with Chapter 2 knowledge source mapping
- Add TODO sections to subagents for Mechanical Systems-specific handling

**Alternatives Considered**:
- **New Components**: Unnecessary duplication, breaks consistency
- **Separate Endpoints**: Adds complexity, same functionality needed
- **New Subagents**: Overkill, existing subagents can handle Chapter 2 with context

### 2. Knowledge Source Mapping: Chapter ID-Based Routing

**Decision**: Use chapterId parameter to route to appropriate knowledge source in runtime engine

**Rationale**:
- **Scalable**: Easy to add more chapters (chapterId=3, 4, etc.)
- **Generic**: Same routing logic works for all chapters
- **Clear Separation**: Each chapter has its own chunks and metadata

**Routing Pattern**:
```python
# Runtime engine routing
chapter_id = request_data.get("chapterId", 1)
if chapter_id == 2:
    # Route to Chapter 2 subagents
    # Use Chapter 2 RAG context
    # Call Chapter 2 LLM with Mechanical Systems prompts
elif chapter_id == 1:
    # Existing Chapter 1 logic
elif chapter_id == 3:
    # Existing Chapter 3 logic
```

### 3. Subagent Architecture: Chapter-Specific Subagents

**Decision**: Create Chapter 2-specific subagent files (ch2_*) that mirror Chapter 1 and Chapter 3 structure but with Mechanical Systems context

**Rationale**:
- **Clarity**: Clear separation between chapters
- **Maintainability**: Easier to maintain chapter-specific logic
- **Mechanical Systems Context**: Dedicated subagents can handle Mechanical Systems-specific concepts

**Subagent Structure**:
```python
class Ch2AskAgent:
    def run(self, input):
        # TODO: implement model prompting in future feature
        return placeholder_response
```

### 4. API Endpoint Naming Convention

**Decision**: Use `/ai/ch2/{block-type}` pattern for Chapter 2 endpoints

**Rationale**:
- **Consistency**: Matches Chapter 3 pattern (`/ai/ch3/{block-type}`)
- **Clarity**: Clear chapter identification in URL
- **Scalability**: Easy to add more chapters

**Endpoints**:
- `POST /ai/ch2/ask`
- `POST /ai/ch2/explain`
- `POST /ai/ch2/quiz`
- `POST /ai/ch2/diagram`

---

## Integration Patterns

### Pattern 1: API → Runtime Engine → Subagent Flow

All Chapter 2 endpoints follow this pattern:
1. API endpoint receives request
2. Endpoint calls `run_ai_block(block_type, request_data)` with `chapterId=2`
3. Runtime engine routes to Chapter 2 subagent
4. Subagent processes request (placeholder)
5. Response returned to API → Frontend

### Pattern 2: RAG Pipeline Integration

Runtime engine calls RAG pipeline for Chapter 2:
1. Runtime engine identifies `chapterId=2`
2. Calls RAG pipeline with `chapter_id=2`
3. RAG pipeline loads Chapter 2 chunks
4. Returns context to runtime engine
5. Context passed to subagent

---

## References

- Feature 005: Chapter 1 AI Runtime Engine (base pattern)
- Feature 030: Chapter 3 AI Runtime Engine (reference pattern)
- Feature 033: Chapter 2 Content (content source)

---

## Summary

This research establishes:
- Reuse existing infrastructure (API, runtime engine, skills)
- Chapter ID-based routing for scalability
- Chapter-specific subagents for clarity
- API endpoint naming convention for consistency

**Key Principles**:
- Consistency with Chapter 1 and Chapter 3 patterns
- Scalability for future chapters
- Clear separation of chapter-specific logic
- Scaffolding-only approach (no business logic)

