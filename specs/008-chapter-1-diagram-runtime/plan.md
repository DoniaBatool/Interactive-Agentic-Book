# Implementation Plan: Chapter 1 — Diagram Generator Runtime

**Branch**: `008-chapter-1-diagram-runtime` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/008-chapter-1-diagram-runtime/spec.md`

## Summary

This feature creates the complete diagram generator runtime scaffolding for Chapter 1 that generates diagrams using LLM reasoning + structured outputs. The implementation establishes the architectural foundation for diagram runtime orchestrator, diagram agent (plan, create, generate), schema models (Request, Node, Edge, Response), skills (extraction, layout, SVG conversion), RAG integration, and API integration. **No real AI logic is implemented**—only scaffolding, function signatures, TODO placeholders, and architectural blueprints to prepare for future AI diagram generation implementation.

**Primary Deliverable**: Complete diagram generator runtime infrastructure scaffolding (runtime, agent, schema, skills, RAG retrieval, API integration)
**Validation**: All files exist, imports resolve, backend starts, no runtime errors

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- No new runtime dependencies required (scaffolding only)

**Storage**:
- No persistent storage (scaffolding only)
- Future: Cache for generated diagrams

**Testing**:
- Manual: File existence verification, import resolution, backend startup
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)

**Project Type**: Backend AI infrastructure scaffolding

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (no API calls, no diagram generation)
- MUST maintain compatibility with Feature 005, 006, 007
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality

**Scale/Scope**:
- 5+ Python modules/files to create
- 2 files to update (diagram_agent.py, ai_blocks.py)
- ~300-500 lines of scaffolding code (mostly signatures and TODOs)
- 1 runtime module, 1 schema module, 1 agent update, 1 skill module, 1 RAG module

---

## 1. Overview

### Architecture Purpose

The diagram generator runtime provides a unified system for generating diagrams using LLM reasoning + structured outputs. The system integrates with the existing RAG pipeline for context retrieval, uses diagram agents for planning and generation, and employs skills for extraction, layout, and SVG conversion.

### High-Level Architecture

The diagram generator runtime follows a pipeline architecture:

```
API Request (POST /api/ai/diagram)
  ↓
Diagram Runtime Orchestrator
  ↓
Input Validation → RAG Retrieval → Diagram Agent → Skills → Schema → Response
  ↓
Structured Diagram Output (nodes, edges, SVG)
```

### Key Components

1. **Diagram Runtime**: Orchestrates diagram generation flow
2. **Diagram Agent**: Plans, creates structure, generates SVG
3. **Schema Models**: Type-safe data structures (Request, Node, Edge, Response)
4. **Diagram Skills**: Extraction, layout, SVG conversion
5. **RAG Retrieval**: Context retrieval for diagrams
6. **API Integration**: Routes requests to runtime

### Integration Points

- **AI Runtime Engine** (Feature 005): Routes diagram blocks to diagram runtime
- **RAG Pipeline** (Feature 005): Provides context retrieval infrastructure
- **Diagram Generation Engine** (Feature 006): Provides diagram providers and pipeline
- **Quiz Engine** (Feature 007): Shared RAG and skills architecture
- **ChatKit Tools** (Future): Diagram generation as ChatKit tool

---

## 2. Architecture Diagram (Text-Based)

### Sequence Diagram: Diagram Generation Flow

```
Frontend
  │
  │ POST /api/ai/diagram
  │ {diagramType, chapterId, concepts}
  ▼
API Layer (ai_blocks.py)
  │
  │ run_diagram_generator(diagramType, chapterId, concepts)
  ▼
Diagram Runtime (runtime.py)
  │
  │ Step 1: Validate input
  │ Step 2: get_relevant_diagram_chunks(chapterId, concepts)
  ▼
RAG Retrieval (diagram_retrieval.py)
  │
  │ Returns: context chunks
  ▼
Diagram Runtime
  │
  │ Step 3: plan_diagram() → create_structure() → generate_svg_stub()
  ▼
Diagram Agent (diagram_agent.py)
  │
  │ Uses: extraction_skill() → layout_skill() → svg_conversion_skill()
  ▼
Diagram Skills (diagram_skill.py)
  │
  │ Returns: structured diagram (nodes, edges, SVG)
  ▼
Diagram Runtime
  │
  │ Step 4: Format using DiagramResponse schema
  ▼
API Layer
  │
  │ Returns: DiagramResponse
  ▼
Frontend
```

### Component Interaction Diagram

```
┌─────────────────┐
│   API Layer     │
│  (ai_blocks.py) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Diagram Runtime │
│  (runtime.py)   │
└────────┬────────┘
         │
    ┌────┴────┬──────────────┬─────────────┐
    │         │              │             │
    ▼         ▼              ▼             ▼
┌────────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐
│  RAG   │ │ Diagram │ │ Diagram  │ │  Schema    │
│Retrieval│ │  Agent  │ │  Skills  │ │  Models   │
└────────┘ └──────────┘ └──────────┘ └────────────┘
```

---

## 3. Module Breakdown

### 3.1 Diagram Runtime Module

**Path**: `backend/app/ai/diagram/runtime.py`

**Purpose**: Orchestrate the complete diagram generation flow.

**Responsibilities**:
- Validate input (diagramType, chapterId, concepts)
- Retrieve contextual chunks via RAG
- Coordinate diagram agent methods
- Format final diagram output structure
- Return structured response

**Key Functions**:
- `async def run_diagram_generator(diagram_type: str, chapter_id: int, concepts: List[str]) -> Dict[str, Any]`

**Integration Points**:
- Calls RAG retrieval for context
- Calls diagram agent for generation
- Uses schema models for validation
- Returns formatted response

---

### 3.2 Diagram Agent Module

**Path**: `backend/app/ai/subagents/diagram_agent.py` (UPDATE existing file)

**Purpose**: High-level agent for diagram planning, structure creation, and SVG generation.

**Responsibilities**:
- Plan diagram structure using LLM reasoning
- Create diagram structure (nodes, edges)
- Generate SVG stub or code
- Return structured diagram payload

**Key Functions**:
- `def plan_diagram(diagram_type: str, concepts: List[str], context: Dict[str, Any]) -> Dict[str, Any]`
- `def create_structure(plan: Dict[str, Any]) -> Dict[str, Any]`
- `def generate_svg_stub(structure: Dict[str, Any]) -> str`

**Integration Points**:
- Called by diagram runtime
- Uses diagram skills for processing
- Returns structured diagram data

---

### 3.3 Diagram Schema Module

**Path**: `backend/app/ai/diagram/schema.py` (NEW)

**Purpose**: Define Pydantic models for type-safe diagram data structures.

**Responsibilities**:
- Define request/response models
- Define node and edge structures
- Provide validation
- Support optional fields for flexibility

**Key Models**:
- `DiagramRequest(BaseModel)` - Request validation
- `DiagramNode(BaseModel)` - Node structure
- `DiagramEdge(BaseModel)` - Edge structure
- `DiagramResponse(BaseModel)` - Response structure

**Integration Points**:
- Used by API layer for request validation
- Used by runtime for response formatting
- Used by agent for structure creation

---

### 3.4 Diagram Skills Module

**Path**: `backend/app/ai/skills/diagram_skill.py` (NEW)

**Purpose**: Provide reusable skills for diagram processing.

**Responsibilities**:
- Extract diagram elements from context
- Layout diagram structure (positions, relationships)
- Convert structured diagram to SVG

**Key Functions**:
- `def extraction_skill(context: Dict[str, Any], concepts: List[str]) -> Dict[str, Any]`
- `def layout_skill(elements: Dict[str, Any]) -> Dict[str, Any]`
- `def svg_conversion_skill(structure: Dict[str, Any]) -> str`

**Integration Points**:
- Called by diagram agent
- Used by diagram runtime
- Processes diagram data

---

### 3.5 RAG Diagram Retrieval Module

**Path**: `backend/app/ai/rag/diagram_retrieval.py` (NEW)

**Purpose**: Retrieve relevant chunks for diagram generation.

**Responsibilities**:
- Retrieve chapter chunks relevant to diagram concepts
- Filter and rank chunks by relevance
- Return structured context for diagram generation

**Key Functions**:
- `def get_relevant_diagram_chunks(chapter_id: int, concepts: List[str]) -> List[Dict[str, Any]]`

**Integration Points**:
- Called by diagram runtime
- Uses existing RAG pipeline infrastructure
- Returns context for diagram agent

---

## 4. File Specifications

### 4.1 Diagram Runtime File

**File**: `backend/app/ai/diagram/runtime.py`

**Structure**:
```python
"""
Diagram Generator Runtime

Orchestrates the complete diagram generation flow:
1. Validate input
2. Retrieve contextual chunks (RAG)
3. Use Diagram Agent
4. Format final diagram output structure
"""

from typing import List, Dict, Any
from app.ai.diagram.schema import DiagramRequest, DiagramResponse

async def run_diagram_generator(
    diagram_type: str,
    chapter_id: int,
    concepts: List[str]
) -> Dict[str, Any]:
    """
    Orchestrate diagram generation flow.
    
    Pipeline Steps (all TODO):
    1. Validate input (diagramType, chapterId, concepts[])
    2. Retrieve contextual chunks (future RAG)
    3. Use Diagram Agent
    4. Format final diagram output structure
    """
    # Step 1: Validate input - TODO
    # Step 2: Retrieve contextual chunks - TODO
    # Step 3: Use Diagram Agent - TODO
    # Step 4: Format final diagram output structure - TODO
    return {}
```

**Key Characteristics**:
- Async function for async operations
- Type hints for all parameters
- TODO placeholders for all steps
- Placeholder return structure

---

### 4.2 Diagram Agent File

**File**: `backend/app/ai/subagents/diagram_agent.py` (UPDATE)

**Current Structure** (from Feature 005):
```python
async def diagram_agent(
    diagram_type: str,
    concepts: List[str],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    # Existing placeholder
```

**Update Required**:
- Add `plan_diagram()` function
- Add `create_structure()` function
- Add `generate_svg_stub()` function
- Update existing function to use new methods
- Maintain backward compatibility

**New Structure**:
```python
def plan_diagram(
    diagram_type: str,
    concepts: List[str],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """Plan diagram structure using LLM reasoning. TODO: Implement"""
    return {}

def create_structure(
    plan: Dict[str, Any]
) -> Dict[str, Any]:
    """Create diagram structure (nodes, edges). TODO: Implement"""
    return {}

def generate_svg_stub(
    structure: Dict[str, Any]
) -> str:
    """Generate SVG stub or code. TODO: Implement"""
    return ""
```

---

### 4.3 Diagram Schema File

**File**: `backend/app/ai/diagram/schema.py` (NEW)

**Structure**:
```python
"""
Diagram Schema Models

Pydantic models for type-safe diagram data structures.
"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class DiagramRequest(BaseModel):
    diagram_type: str
    chapter_id: Optional[int] = None
    concepts: List[str] = []

class DiagramNode(BaseModel):
    id: str
    label: Optional[str] = None
    type: Optional[str] = None
    position: Optional[Dict[str, float]] = None
    metadata: Optional[Dict[str, Any]] = None

class DiagramEdge(BaseModel):
    source: str
    target: str
    label: Optional[str] = None
    type: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class DiagramResponse(BaseModel):
    nodes: List[DiagramNode] = []
    edges: List[DiagramEdge] = []
    svg: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
```

**Key Characteristics**:
- All fields optional or placeholder
- Type hints for validation
- Support for flexible diagram structures

---

### 4.4 Diagram Skills File

**File**: `backend/app/ai/skills/diagram_skill.py` (NEW)

**Structure**:
```python
"""
Diagram Skills

Reusable skills for diagram processing:
- Extraction: Extract diagram elements from context
- Layout: Layout diagram structure
- SVG Conversion: Convert structured diagram to SVG
"""

from typing import List, Dict, Any

def extraction_skill(
    context: Dict[str, Any],
    concepts: List[str]
) -> Dict[str, Any]:
    """Extract diagram elements from context. TODO: Implement"""
    return {}

def layout_skill(
    elements: Dict[str, Any]
) -> Dict[str, Any]:
    """Layout diagram structure. TODO: Implement"""
    return {}

def svg_conversion_skill(
    structure: Dict[str, Any]
) -> str:
    """Convert structured diagram to SVG. TODO: Implement"""
    return ""
```

**Key Characteristics**:
- Three core skills for diagram processing
- TODO placeholders for implementation
- Type hints for all parameters

---

### 4.5 RAG Diagram Retrieval File

**File**: `backend/app/ai/rag/diagram_retrieval.py` (NEW)

**Structure**:
```python
"""
RAG Diagram Retrieval

Retrieve relevant chunks for diagram generation.
"""

from typing import List, Dict, Any

def get_relevant_diagram_chunks(
    chapter_id: int,
    concepts: List[str]
) -> List[Dict[str, Any]]:
    """
    Retrieve relevant chunks for diagram generation.
    
    TODO: Implement retrieval logic
    TODO: Use RAG pipeline to retrieve chunks
    TODO: Filter chunks by relevance to concepts
    TODO: Rank chunks by relevance score
    """
    return []
```

**Key Characteristics**:
- TODO-only function
- Integrates with existing RAG pipeline
- Returns structured context

---

## 5. Data Models

### 5.1 Request Model

**Model**: `DiagramRequest`

**Fields**:
- `diagram_type: str` - Required, diagram type identifier
- `chapter_id: Optional[int]` - Optional, chapter identifier
- `concepts: List[str]` - Optional, concepts to include

**Usage**: API request validation

---

### 5.2 Node Model

**Model**: `DiagramNode`

**Fields**:
- `id: str` - Required, node identifier
- `label: Optional[str]` - Optional, node label
- `type: Optional[str]` - Optional, node type
- `position: Optional[Dict[str, float]]` - Optional, position (x, y)
- `metadata: Optional[Dict[str, Any]]` - Optional, additional metadata

**Usage**: Represent diagram nodes in structured format

---

### 5.3 Edge Model

**Model**: `DiagramEdge`

**Fields**:
- `source: str` - Required, source node ID
- `target: str` - Required, target node ID
- `label: Optional[str]` - Optional, edge label
- `type: Optional[str]` - Optional, edge type
- `metadata: Optional[Dict[str, Any]]` - Optional, additional metadata

**Usage**: Represent diagram edges/relationships

---

### 5.4 Response Model

**Model**: `DiagramResponse`

**Fields**:
- `nodes: List[DiagramNode]` - Optional, list of nodes
- `edges: List[DiagramEdge]` - Optional, list of edges
- `svg: Optional[str]` - Optional, SVG string
- `metadata: Optional[Dict[str, Any]]` - Optional, additional metadata

**Usage**: API response structure

---

## 6. API Integration Flow

### 6.1 Request Flow

1. **Frontend** → `POST /api/ai/diagram` with `DiagramRequest`
2. **API Endpoint** (`ai_blocks.py`) → Validates request, calls `run_diagram_generator()`
3. **Diagram Runtime** → Orchestrates generation flow
4. **RAG Retrieval** → Retrieves context chunks
5. **Diagram Agent** → Plans → creates structure → generates SVG
6. **Diagram Skills** → Extract → layout → convert to SVG
7. **Diagram Runtime** → Formats response using `DiagramResponse`
8. **API Endpoint** → Returns `DiagramResponse` to frontend

### 6.2 API Endpoint Update

**File**: `backend/app/api/ai_blocks.py`

**Current Structure**:
```python
@router.post("/diagram", response_model=AIBlockResponse)
async def diagram(request: DiagramRequest) -> AIBlockResponse:
    # Existing placeholder
```

**Update Required**:
- Add import: `from app.ai.diagram.runtime import run_diagram_generator`
- Replace placeholder with: `result = await run_diagram_generator(...)`
- Maintain existing response model (or update if needed)

---

## 7. RAG Integration Flow

### 7.1 Context Retrieval Flow

1. **Diagram Runtime** → Calls `get_relevant_diagram_chunks(chapter_id, concepts)`
2. **RAG Retrieval** → Uses existing RAG pipeline infrastructure
3. **RAG Pipeline** → Retrieves chapter chunks
4. **RAG Retrieval** → Filters and ranks chunks by relevance
5. **RAG Retrieval** → Returns structured context
6. **Diagram Runtime** → Passes context to diagram agent

### 7.2 Integration Points

- **Existing RAG Pipeline** (Feature 005): Provides infrastructure
- **Chapter Chunks** (Feature 005): Provides chapter content
- **Embedding Client** (Feature 005): Provides embedding functionality
- **Qdrant Store** (Feature 005): Provides vector search

---

## 8. ChatKit Integration (Future)

### 8.1 Future Integration Plan

**Purpose**: Enable diagram generation as ChatKit tool.

**Integration Points**:
- ChatKit tools system (Feature 005)
- Diagram runtime orchestrator
- Diagram agent methods

**Tool Structure** (Future):
```python
# ChatKit tool definition (future)
diagram_tool = {
    "name": "generate_diagram",
    "description": "Generate diagram from concepts",
    "parameters": {
        "diagram_type": str,
        "concepts": List[str]
    }
}
```

**TODO**: Implement ChatKit tool integration when ChatKit is fully integrated

---

## 9. Risks & Mitigations

### Risk 1: Breaking Existing Features

**Risk**: Updates to existing files (diagram_agent.py, ai_blocks.py) may break existing functionality.

**Mitigation**: 
- Add new functions as separate methods
- Maintain existing function signatures
- Test all existing endpoints after updates
- No breaking changes to existing code

### Risk 2: Import Resolution Failures

**Risk**: New modules may have import errors.

**Mitigation**:
- Create all `__init__.py` files
- Test imports incrementally
- Fix errors immediately

### Risk 3: Schema Validation Issues

**Risk**: Pydantic models may have validation errors.

**Mitigation**:
- Use optional fields for flexibility
- Test model validation
- Provide default values

### Risk 4: No Business Logic Allowed

**Risk**: Accidentally implementing real diagram generation logic.

**Mitigation**:
- All functions return placeholder values
- All logic marked with TODO comments
- Code review to ensure no real implementation

---

## 10. Success Criteria Mapping

| Success Criteria | Implementation Phase | Validation Method |
|------------------|---------------------|-------------------|
| **SC-001**: All scaffold modules exist | Runtime, Agent, Schema, Skills, RAG | File existence checks |
| **SC-002**: No real AI logic | All modules | Code review |
| **SC-003**: Backend starts successfully | All phases | Backend startup test |
| **SC-004**: API integration complete | API update | Endpoint routing test |
| **SC-005**: Documentation complete | ✅ Complete | File existence |

---

**Plan Generation Complete**: 2025-12-05
**Ready for Tasks**: Yes ✅

