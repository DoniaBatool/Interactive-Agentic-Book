# Research: Chapter 2 AI Blocks Integration (ROS 2 Fundamentals)

**Feature**: 011-chapter-2-ai-blocks
**Date**: 2025-12-05
**Purpose**: Document integration approach for enabling AI blocks in Chapter 2 using existing infrastructure

## Overview

This document captures research findings for integrating AI-interactive blocks into Chapter 2 (ROS 2 Fundamentals) using the existing Runtime Engine, RAG pipeline, subagents, and skills from Chapter 1. Since this is a scaffolding phase, research focuses on integration patterns, knowledge source mapping, and ROS 2-specific context handling.

## Technology Decisions

### 1. Reuse Existing Components and Infrastructure

**Decision**: Reuse all AI block components, runtime engine, subagents, and API endpoints from Feature 004 (Chapter 1 AI blocks)

**Rationale**:
- **Consistency**: Same UI/UX across all chapters
- **Efficiency**: No need to recreate components or infrastructure
- **Maintainability**: Single source of truth for AI block functionality
- **Proven Pattern**: Chapter 1 integration already tested and working

**Integration Approach**:
- Import existing React components in chapter-2.mdx
- Route Chapter 2 requests through same API endpoints with chapterId=2
- Extend runtime engine with Chapter 2 knowledge source mapping
- Add TODO sections to subagents for ROS 2-specific handling

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
- **Future-Proof**: Supports cross-chapter queries later

**Mapping Pattern**:
```python
# Runtime engine mapping
knowledge_sources = {
    1: "chapter_1_chunks",
    2: "chapter_2_chunks",  # NEW for Chapter 2
    # Future: 3: "chapter_3_chunks"
}
```

**Alternatives Considered**:
- **Separate Runtime Engines**: Too complex, unnecessary separation
- **Single Knowledge Source**: Harder to manage, no chapter boundaries
- **Config-Based**: Adds configuration overhead, chapterId simpler

### 3. Chapter 2 Chunks: Placeholder Function Pattern

**Decision**: Create `chapter_2_chunks.py` with placeholder function matching Chapter 1 pattern

**Rationale**:
- **Consistency**: Same pattern as Chapter 1 chunks file
- **Future-Ready**: Structure ready for real chunking implementation
- **Clear Contract**: Function signature defines expected interface
- **Documentation**: TODO comments explain future implementation

**Function Pattern**:
```python
def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    TODO: Implement chunking from Chapter 2 MDX content
    TODO: Load Chapter 2 content from frontend/docs/chapters/chapter-2.mdx
    TODO: Implement chunking strategy (same as Chapter 1)
    """
    return []  # Placeholder
```

**Alternatives Considered**:
- **No Chunks File**: Runtime engine would fail, needs structure
- **Real Implementation**: Out of scope, future feature
- **Mock Data**: Adds complexity, placeholder sufficient

### 4. Subagent Extension: TODO Sections for ROS 2 Context

**Decision**: Add TODO sections to each subagent explaining Chapter 2 integration without implementing logic

**Rationale**:
- **Documentation**: Clear guidance for future ROS 2-specific handling
- **No Breaking Changes**: Existing Chapter 1 functionality unchanged
- **Future-Ready**: Structure for ROS 2-specific prompts and context
- **Maintainability**: All Chapter 2 notes in one place per subagent

**TODO Pattern**:
```python
# TODO: Chapter 2 (ROS 2) Integration
# Expected ROS 2 inputs:
#   - Concepts: "nodes", "topics", "services", "actions", "packages", "launch-files"
#   - Section IDs: "introduction-to-ros2", "nodes-and-node-communication", etc.
# Expected output format: [same as Chapter 1, but with ROS 2 context]
# ROS 2-specific considerations:
#   - Use ROS 2 analogies (post office, restaurant, phone calls)
#   - Reference real-world examples (TurtleBot 3, navigation stack)
#   - Handle ROS 2 terminology correctly
```

**Alternatives Considered**:
- **Separate Subagents**: Unnecessary, same logic with different context
- **Config-Based**: Adds complexity, TODO comments sufficient
- **Real Implementation**: Out of scope, future feature

### 5. MDX Component Integration: Same Pattern as Chapter 1

**Decision**: Use same import and component usage pattern as Chapter 1

**Rationale**:
- **Consistency**: Learners see same UI across chapters
- **Proven**: Chapter 1 pattern already tested
- **Simple**: Direct import, no configuration needed
- **Type-Safe**: TypeScript validates props

**Integration Pattern**:
```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';

<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />
```

**Alternatives Considered**:
- **Global Mapping**: More complex, direct import clearer
- **Dynamic Loading**: Not supported in static generation
- **Wrapper Components**: Unnecessary abstraction

## ROS 2-Specific Considerations

### Concept Mapping

**ROS 2 Concepts for AI Blocks**:
- **Nodes**: Independent processes in ROS 2 system
- **Topics**: Publish/subscribe communication channels
- **Services**: Request/response communication
- **Actions**: Long-running tasks with feedback
- **Packages**: ROS 2 code organization units
- **Launch Files**: Multi-node startup configuration

**AI Block Usage**:
- **Ask Question**: Questions about ROS 2 concepts, node communication, topic usage
- **Explain Like 10**: Simplified explanations of topics, services, actions using analogies
- **Interactive Quiz**: Questions about ROS 2 fundamentals, communication patterns
- **Generate Diagram**: Visual representations of ROS 2 architecture, node graphs, communication flows

### Section ID Mapping

**Chapter 2 Section IDs** (from chapter-2.mdx):
- `introduction-to-ros2`
- `nodes-and-node-communication`
- `topics-and-messages`
- `services-and-actions`
- `ros2-packages`
- `launch-files-and-workflows`
- `learning-objectives`
- `summary`
- `glossary`

**AI Block Placement**:
- Ask Question: `introduction-to-ros2`
- Generate Diagram: `nodes-and-node-communication`
- Explain Like 10: `topics-and-messages`
- Interactive Quiz: `services-and-actions`

### Diagram Type Mapping

**Chapter 2 Diagram Types** (from chapter-2.mdx):
- `ros2-ecosystem-overview`
- `node-communication-architecture`
- `topic-pubsub-flow`
- `services-actions-comparison`

**Generate Diagram Block Usage**:
- `diagramType="node-communication-architecture"` for nodes section
- Future: Other diagram types as needed

## Integration Flow

### Frontend → Backend Flow

1. **User interacts with AI block** in chapter-2.mdx
2. **Component sends request** to `/api/ai/{block-type}` with `chapterId=2`
3. **API endpoint routes** to runtime engine with `chapterId=2`
4. **Runtime engine maps** `chapterId=2` to `chapter_2_chunks` knowledge source
5. **RAG pipeline retrieves** Chapter 2 chunks (TODO: implement chunking)
6. **Subagent processes** request with Chapter 2 context (TODO: ROS 2-specific handling)
7. **Response returned** to frontend component

### Knowledge Source Resolution

**Runtime Engine Logic** (TODO):
```python
if chapter_id == 1:
    from app.content.chapters.chapter_1_chunks import get_chapter_chunks
    chunks = get_chapter_chunks(chapter_id=1)
elif chapter_id == 2:
    from app.content.chapters.chapter_2_chunks import get_chapter_chunks
    chunks = get_chapter_chunks(chapter_id=2)  # NEW
else:
    raise ValueError(f"Unknown chapter_id: {chapter_id}")
```

## Best Practices

### Code Organization

- **Reuse over Recreate**: Always prefer reusing existing components and infrastructure
- **Consistent Patterns**: Follow Chapter 1 patterns exactly for maintainability
- **Clear TODOs**: Document future implementation clearly with TODO comments
- **No Breaking Changes**: Ensure Chapter 1 functionality remains intact

### Documentation

- **Inline Comments**: Add TODO comments explaining Chapter 2 integration points
- **Function Docstrings**: Document expected inputs/outputs for ROS 2 context
- **API Contracts**: Define Chapter 2-specific request/response formats
- **Section IDs**: Document all Chapter 2 section IDs for reference

### Testing Strategy

- **Component Rendering**: Verify all 4 AI blocks render in chapter-2.mdx
- **API Routing**: Test that chapterId=2 routes correctly to runtime engine
- **Import Validation**: Ensure all imports resolve (frontend and backend)
- **Build Validation**: Verify Docusaurus build succeeds with Chapter 2 blocks

## Future Enhancements

- **Real Chunking**: Implement actual chunking logic for Chapter 2 content
- **ROS 2-Specific Prompts**: Add ROS 2 context to LLM prompts
- **Cross-Chapter Queries**: Enable queries spanning Chapter 1 and Chapter 2
- **ROS 2 Examples**: Include TurtleBot 3, navigation stack examples in responses
- **Diagram Generation**: Implement actual diagram generation for ROS 2 concepts
