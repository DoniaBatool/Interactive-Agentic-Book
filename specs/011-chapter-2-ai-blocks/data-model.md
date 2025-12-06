# Data Model: Chapter 2 AI Blocks Integration

**Feature**: 011-chapter-2-ai-blocks
**Date**: 2025-12-05
**Purpose**: Define data structures and entities for Chapter 2 AI blocks integration

## Overview

This document defines the data structures, entities, and relationships for integrating AI-interactive blocks into Chapter 2. All structures reuse patterns from Chapter 1 but include Chapter 2-specific context (chapterId=2, ROS 2 concepts, section IDs).

## Entities

### 1. Chapter 2 AI Block Component

**Storage**: React component instances in `frontend/docs/chapters/chapter-2.mdx`

**Structure**:
```typescript
interface Chapter2AIBlockProps {
  chapterId: 2;                    // Fixed: Chapter 2
  sectionId?: string;              // Optional: "introduction-to-ros2", "nodes-and-node-communication", etc.
  concept?: string;                // Optional: "topics", "nodes", "services", "actions"
  diagramType?: string;            // Optional: "node-communication-architecture", etc.
  numQuestions?: number;           // Optional: Default 5
}
```

**Component Types**:
- `AskQuestionBlock` - Props: `{ chapterId: 2, sectionId: string }`
- `ExplainLike10Block` - Props: `{ concept: string, chapterId: 2 }`
- `InteractiveQuizBlock` - Props: `{ chapterId: 2, numQuestions: number }`
- `GenerateDiagramBlock` - Props: `{ diagramType: string, chapterId: 2 }`

**Validation**:
- `chapterId` must be 2
- `sectionId` must match section anchors from chapter-2.mdx (kebab-case)
- `concept` must be valid ROS 2 concept (topics, nodes, services, actions, packages, launch-files)
- `diagramType` must match diagram placeholders from chapter-2.mdx

**Relationship**: N:1 with Chapter 2 MDX Content (4 instances in chapter-2.mdx)

---

### 2. Chapter 2 Chunks

**Storage**: Python module `backend/app/content/chapters/chapter_2_chunks.py`

**Structure**:
```python
def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    Returns list of chunk dictionaries:
    [
        {
            "id": str,                    # "ch2-s1-c0"
            "text": str,                  # Chunk text content
            "chapter_id": 2,              # Chapter identifier
            "section_id": str,            # "introduction-to-ros2", etc.
            "position": int,              # Position in chapter (0-based)
            "word_count": int,            # Word count
            "metadata": {
                "heading": str,          # Section heading
                "type": str              # "paragraph", "heading", "glossary", etc.
            }
        },
        ...
    ]
    """
    return []  # Placeholder - no real implementation
```

**Validation**:
- Function must exist and be importable
- Function signature must match Chapter 1 pattern
- Return type must be `List[Dict[str, Any]]`
- Placeholder return acceptable (empty list)

**Relationship**: 1:1 with Chapter 2 Content (future: chunks derived from chapter-2.mdx)

---

### 3. Runtime Engine Knowledge Source Mapping

**Storage**: Python module `backend/app/ai/runtime/engine.py`

**Structure**:
```python
# Knowledge source mapping
knowledge_sources = {
    1: "chapter_1_chunks",  # Existing
    2: "chapter_2_chunks",  # NEW for Chapter 2
}

# TODO: Chapter 2 RAG Integration
# When chapterId=2:
#   1. Import get_chapter_chunks from chapter_2_chunks
#   2. Call get_chapter_chunks(chapter_id=2)
#   3. Use chunks for RAG retrieval
#   4. Pass Chapter 2 context to subagents
```

**Validation**:
- Mapping must include `2: "chapter_2_chunks"`
- TODO comments must explain Chapter 2 integration
- No breaking changes to Chapter 1 routing

**Relationship**: N:1 with Runtime Engine (one mapping entry per chapter)

---

### 4. API Request/Response Models

**Storage**: Python module `backend/app/api/ai_blocks.py`

**Request Models** (Chapter 2 context):
```python
class AskQuestionRequest(BaseModel):
    question: str
    chapterId: Optional[int] = 2  # Default: Chapter 2
    sectionId: Optional[str] = None  # "introduction-to-ros2", etc.

class ExplainLike10Request(BaseModel):
    concept: str  # "topics", "nodes", "services", "actions"
    chapterId: Optional[int] = 2  # Default: Chapter 2

class QuizRequest(BaseModel):
    chapterId: int = 2  # Default: Chapter 2
    numQuestions: Optional[int] = 5

class DiagramRequest(BaseModel):
    diagramType: str  # "node-communication-architecture", etc.
    chapterId: Optional[int] = 2  # Default: Chapter 2
```

**Response Models** (Placeholder):
```python
class AIBlockResponse(BaseModel):
    message: str = "AI block placeholder"
    received: Dict[str, Any]  # Echo of request
```

**Validation**:
- Request models must accept `chapterId=2`
- Response models must return placeholder structure
- No real AI logic in responses (scaffolding only)

**Relationship**: N:1 with API Router (4 endpoints share same response structure)

---

### 5. Subagent TODO Sections

**Storage**: Python modules in `backend/app/ai/subagents/`

**Structure** (per subagent):
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

**Subagents**:
- `ask_question_agent.py` - TODO for ROS 2 question handling
- `explain_el10_agent.py` - TODO for ROS 2 concept explanations
- `quiz_agent.py` - TODO for ROS 2 quiz generation
- `diagram_agent.py` - TODO for ROS 2 diagram generation

**Validation**:
- TODO sections must exist in all 4 subagents
- TODO sections must document ROS 2-specific inputs/outputs
- No breaking changes to existing Chapter 1 functionality

**Relationship**: 1:1 with Subagent (one TODO section per subagent)

---

## Relationships

### Component → API Request Flow

```
Chapter 2 AI Block Component (chapter-2.mdx)
    ↓ (user interaction)
API Request (chapterId=2)
    ↓ (routing)
Runtime Engine (knowledge source mapping)
    ↓ (RAG retrieval)
Chapter 2 Chunks (get_chapter_chunks)
    ↓ (context)
Subagent (ROS 2-specific handling)
    ↓ (response)
API Response
    ↓ (display)
Chapter 2 AI Block Component
```

### Knowledge Source Resolution

```
Runtime Engine
    ├── chapterId=1 → chapter_1_chunks.get_chapter_chunks(1)
    └── chapterId=2 → chapter_2_chunks.get_chapter_chunks(2)  # NEW
```

### Section ID Mapping

```
Chapter 2 MDX Sections
    ├── "introduction-to-ros2" → AskQuestionBlock
    ├── "nodes-and-node-communication" → GenerateDiagramBlock
    ├── "topics-and-messages" → ExplainLike10Block
    └── "services-and-actions" → InteractiveQuizBlock
```

---

## Data Validation Rules

### Frontend Validation

- **chapterId**: Must be 2 for Chapter 2 AI blocks
- **sectionId**: Must be valid section anchor from chapter-2.mdx
- **concept**: Must be valid ROS 2 concept (topics, nodes, services, actions, packages, launch-files)
- **diagramType**: Must match diagram placeholder names (kebab-case)

### Backend Validation

- **chapterId**: Must be 2 for Chapter 2 requests
- **Request Models**: Must validate with Pydantic
- **Chunks Function**: Must be importable and callable
- **Knowledge Source**: Must map chapterId=2 to chapter_2_chunks

### Integration Validation

- **Component Rendering**: All 4 AI blocks must render in chapter-2.mdx
- **API Routing**: chapterId=2 must route correctly
- **Import Resolution**: All imports must resolve (frontend and backend)
- **Build Success**: Docusaurus build must succeed

---

## State Management

### Component State

- **Local State**: Each AI block component manages its own state (React useState)
- **No Global State**: No Redux or context needed for scaffolding
- **API State**: Components handle loading/error states locally

### Backend State

- **No Persistent State**: All endpoints return placeholder responses
- **No Caching**: Chunks function returns empty list (no caching needed)
- **Stateless**: All endpoints are stateless (no session management)

---

## Future Data Structures

### Real Chunking Implementation

```python
# Future: Real chunk structure
{
    "id": "ch2-s1-c0",
    "text": "ROS 2 is a communication framework...",
    "chapter_id": 2,
    "section_id": "introduction-to-ros2",
    "position": 0,
    "word_count": 250,
    "embedding": List[float],  # Vector embedding
    "metadata": {
        "heading": "Introduction to ROS 2",
        "type": "paragraph",
        "has_diagram": True,
        "has_ai_block": True
    }
}
```

### ROS 2-Specific Context

```python
# Future: ROS 2 context for subagents
{
    "chapter_id": 2,
    "concepts": ["nodes", "topics", "services", "actions"],
    "analogies": ["post office", "restaurant", "phone calls"],
    "examples": ["TurtleBot 3", "navigation stack"],
    "section_context": "introduction-to-ros2"
}
```
