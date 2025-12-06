# Research: Chapter 2 AI Runtime Engine Integration

**Feature**: 013-chapter-2-runtime-engine
**Date**: 2025-12-05
**Purpose**: Document runtime engine integration patterns, subagent architecture, skills integration, and ChatKit scaffolding for Chapter 2

## Overview

This document captures research findings for activating the full runtime pathway for Chapter 2 AI blocks. Research focuses on routing patterns, RAG binding, subagent architecture, skills integration, and ChatKit scaffolding. Since this is a scaffolding phase, research focuses on architectural patterns and placeholder design.

## Technology Decisions

### 1. Runtime Engine Routing: Chapter ID-Based Routing

**Decision**: Use chapter_id parameter to route to appropriate subagents and RAG pipeline in runtime engine

**Rationale**:
- **Scalable**: Easy to add more chapters (chapterId=3, 4, etc.)
- **Generic**: Same routing logic works for all chapters
- **Clear Separation**: Each chapter has its own subagents and context
- **Future-Proof**: Supports cross-chapter queries later

**Routing Pattern**:
```python
# Runtime engine routing
chapter_id = request_data.get("chapterId", 1)
if chapter_id == 2:
    # Route to Chapter 2 subagents
    # Use Chapter 2 RAG context
    # Call Chapter 2 LLM with ROS 2 prompts
elif chapter_id == 1:
    # Existing Chapter 1 logic
```

**Alternatives Considered**:
- **Separate Runtime Engines**: Too complex, unnecessary separation
- **Single Subagent with Context**: Harder to manage, no chapter boundaries
- **Config-Based**: Adds configuration overhead, chapterId simpler

### 2. Subagent Architecture: Chapter-Specific Subagents

**Decision**: Create Chapter 2-specific subagent files (ch2_*) that mirror Chapter 1 structure but with ROS 2 context

**Rationale**:
- **Clarity**: Clear separation between Chapter 1 and Chapter 2 logic
- **Maintainability**: Easier to maintain chapter-specific logic
- **ROS 2 Context**: Dedicated subagents can handle ROS 2-specific concepts
- **Pattern Replication**: Follows Chapter 1 pattern for consistency

**Subagent Structure**:
```python
# ch2_ask_question_agent.py
async def ch2_ask_question_agent(question: str, context: Dict[str, Any]) -> Dict[str, Any]:
    """
    TODO: Process ROS 2 question with Chapter 2 context
    TODO: Use ROS 2 concepts, analogies, examples
    TODO: Return formatted answer
    """
    return {"answer": "", "sources": [], "confidence": 0.0}
```

**Alternatives Considered**:
- **Shared Subagents with Context**: Less clear, harder to maintain
- **Single Subagent with Switch**: Too monolithic, harder to test
- **Plugin-Based**: Overkill for current scale

### 3. RAG Pipeline Binding: Chapter-Aware Retrieval

**Decision**: RAG pipeline resolves chapter_2_chunks when chapter_id=2

**Rationale**:
- **Consistency**: Same pattern as Chapter 1
- **Isolation**: Each chapter has its own chunks
- **Context**: Chapter-specific context improves retrieval quality
- **Future-Proof**: Supports cross-chapter queries later

**Binding Pattern**:
```python
# RAG pipeline binding
if chapter_id == 2:
    from app.content.chapters.chapter_2_chunks import get_chapter_chunks
    chunks = get_chapter_chunks(chapter_id=2)
    # Use chunks for RAG retrieval
    # Search in Qdrant collection "chapter_2"
```

**Alternatives Considered**:
- **Single Chunk Source**: Harder to manage, no chapter boundaries
- **Dynamic Chunk Loading**: Adds complexity, chapter_id routing simpler

### 4. Skills Integration: Chapter-Aware Skills

**Decision**: Update skills to be chapter-aware with Chapter 2-specific TODOs

**Rationale**:
- **Reusability**: Same skills work for all chapters
- **Flexibility**: Skills can adapt to chapter-specific context
- **Maintainability**: Single skill file per capability
- **Consistency**: Follows established pattern

**Skills Pattern**:
```python
# retrieval_skill.py
async def retrieve_content(query: str, chapter_id: int, top_k: int = 5):
    # TODO: Chapter-aware retrieval
    if chapter_id == 2:
        # TODO: Use Chapter 2 RAG pipeline
        # TODO: Return Chapter 2 chunks with ROS 2 context
```

**Alternatives Considered**:
- **Chapter-Specific Skills**: Too much duplication
- **Separate Skill Files**: Unnecessary complexity

### 5. ChatKit Integration: Multi-Chapter Session Context

**Decision**: Extend ChatKit session manager to support multi-chapter contexts

**Rationale**:
- **User Experience**: Users may ask questions across chapters
- **Context Continuity**: Maintain context across chapter boundaries
- **Future-Proof**: Supports advanced conversational features
- **Scalability**: Easy to extend to more chapters

**Session Pattern**:
```python
# session_manager.py
# TODO: Multi-chapter session contexts
# TODO: Track Chapter 2 context in session
# TODO: Support cross-chapter queries
```

**Alternatives Considered**:
- **Single-Chapter Sessions**: Simpler but less flexible
- **Separate Sessions Per Chapter**: Too fragmented

### 6. Configuration: Chapter-Specific Settings

**Decision**: Add Chapter 2-specific configuration settings (model, embeddings, runtime flag)

**Rationale**:
- **Flexibility**: Different chapters may need different models
- **Testing**: Can disable Chapter 2 runtime for testing
- **Deployment**: Can configure per deployment
- **Future-Proof**: Easy to add more chapter-specific settings

**Configuration Pattern**:
```python
# settings.py
DEFAULT_CH2_MODEL = os.getenv("DEFAULT_CH2_MODEL", "gpt-4o")
DEFAULT_CH2_EMBEDDINGS = os.getenv("DEFAULT_CH2_EMBEDDINGS", "text-embedding-3-small")
ENABLE_CHAPTER_2_RUNTIME = os.getenv("ENABLE_CHAPTER_2_RUNTIME", "True").lower() == "true"
```

**Alternatives Considered**:
- **Single Model for All Chapters**: Less flexible
- **Hardcoded Settings**: Not configurable

## ROS 2 Specific Considerations

### ROS 2 Concepts

**Key Concepts**:
- Nodes: Individual processes in ROS 2 system
- Topics: Publish/subscribe communication
- Services: Request/response communication
- Actions: Long-running tasks with feedback
- Packages: Code organization units
- Launch Files: Multi-node coordination

**Subagent Implications**:
- Subagents should understand ROS 2 terminology
- Prompts should include ROS 2 analogies
- Responses should reference ROS 2 examples
- Diagrams should show ROS 2 architecture

### Section-Specific Routing

**Section IDs**:
- "introduction-to-ros2"
- "nodes-and-node-communication"
- "topics-and-messages"
- "services-and-actions"
- "ros2-packages"
- "launch-files-and-workflows"

**Routing Strategy**:
- If sectionId provided, filter RAG context by section
- Prioritize chunks from relevant sections
- Include related sections for context

## Implementation Phases

### Phase 1: Scaffolding (Current Feature)
- Create placeholder functions
- Add TODO markers
- Define contracts and schemas
- No real implementation

### Phase 2: Routing Implementation (Future)
- Implement chapter_id=2 routing
- Connect to Chapter 2 subagents
- Wire RAG pipeline for Chapter 2

### Phase 3: Subagent Implementation (Future)
- Implement real ROS 2 question-answering
- Implement ROS 2 explanation generation
- Implement ROS 2 quiz generation
- Implement ROS 2 diagram generation

### Phase 4: Skills Implementation (Future)
- Implement chapter-aware retrieval
- Implement ROS 2 prompt building
- Implement Chapter 2 formatting

### Phase 5: ChatKit Implementation (Future)
- Implement multi-chapter sessions
- Implement Chapter 2 tools
- Integrate with ChatKit API

## Best Practices

### Runtime Engine Best Practices
- Route by chapter_id early in flow
- Validate chapter_id before processing
- Handle missing subagents gracefully
- Log routing decisions for debugging

### Subagent Best Practices
- Use ROS 2-specific context in prompts
- Include ROS 2 analogies and examples
- Handle ROS 2 terminology correctly
- Return structured responses

### Skills Best Practices
- Make skills chapter-aware
- Support chapter-specific formatting
- Handle chapter-specific context
- Maintain skill reusability

### ChatKit Best Practices
- Track chapter context in sessions
- Support cross-chapter queries
- Maintain conversation history
- Handle tool calls appropriately

## Status

⚠️ **All research is theoretical. Real implementation will be added in future features.**
