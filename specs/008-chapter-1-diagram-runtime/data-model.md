# Data Model: Chapter 1 Diagram Generator Runtime

**Generated**: 2025-12-05
**Feature**: 008-chapter-1-diagram-runtime

## Function Signatures

### Diagram Runtime

```python
async def run_diagram_generator(
    diagram_type: str,
    chapter_id: int,
    concepts: List[str]
) -> Dict[str, Any]:
    """
    Orchestrate diagram generation flow.
    
    Expected Input:
        diagram_type: str                   # "anatomy_robot", "physical_ai_overview", etc.
        chapter_id: int                      # Chapter identifier
        concepts: List[str]                  # Concepts to include in diagram
    
    Expected Output:
        {
            "nodes": List[DiagramNode],      # Diagram nodes
            "edges": List[DiagramEdge],      # Diagram edges
            "svg": str,                      # SVG string or code
            "metadata": Dict[str, Any]       # Additional metadata
        }
    
    Pipeline Steps (all TODO):
    1. Validate input
    2. Retrieve contextual chunks (RAG)
    3. Use Diagram Agent
    4. Format final diagram output structure
    """
    # TODO: Implement orchestration
    return {}
```

### Diagram Agent

```python
def plan_diagram(
    diagram_type: str,
    concepts: List[str],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Plan diagram structure using LLM reasoning.
    
    Expected Input:
        diagram_type: str
        concepts: List[str]
        context: Dict[str, Any]              # RAG context
    
    Expected Output:
        {
            "structure": Dict[str, Any],     # Planned structure
            "nodes": List[str],              # Planned nodes
            "edges": List[Dict[str, str]]    # Planned edges
        }
    """
    # TODO: Implement planning
    return {}

def create_structure(
    plan: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Create diagram structure (nodes, edges).
    
    Expected Input:
        plan: Dict[str, Any]                 # Plan from plan_diagram()
    
    Expected Output:
        {
            "nodes": List[DiagramNode],
            "edges": List[DiagramEdge]
        }
    """
    # TODO: Implement structure creation
    return {}

def generate_svg_stub(
    structure: Dict[str, Any]
) -> str:
    """
    Generate SVG stub or code.
    
    Expected Input:
        structure: Dict[str, Any]            # Structure from create_structure()
    
    Expected Output:
        str                                  # SVG string or code
    """
    # TODO: Implement SVG generation
    return ""
```

### Diagram Skills

```python
def extraction_skill(
    context: Dict[str, Any],
    concepts: List[str]
) -> Dict[str, Any]:
    """
    Extract diagram elements from context.
    
    Expected Input:
        context: Dict[str, Any]              # RAG context
        concepts: List[str]                  # Concepts to extract
    
    Expected Output:
        {
            "elements": List[Dict[str, Any]], # Extracted elements
            "relationships": List[Dict[str, Any]]  # Extracted relationships
        }
    """
    # TODO: Implement extraction
    return {}

def layout_skill(
    elements: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Layout diagram structure (positions, relationships).
    
    Expected Input:
        elements: Dict[str, Any]             # Extracted elements
    
    Expected Output:
        {
            "positions": Dict[str, Tuple[int, int]],  # Node positions
            "layout": str                    # Layout algorithm used
        }
    """
    # TODO: Implement layout
    return {}

def svg_conversion_skill(
    structure: Dict[str, Any]
) -> str:
    """
    Convert structured diagram to SVG.
    
    Expected Input:
        structure: Dict[str, Any]            # Diagram structure
    
    Expected Output:
        str                                  # SVG string
    """
    # TODO: Implement SVG conversion
    return ""
```

### RAG Retrieval

```python
def get_relevant_diagram_chunks(
    chapter_id: int,
    concepts: List[str]
) -> List[Dict[str, Any]]:
    """
    Retrieve relevant chunks for diagram generation.
    
    Expected Input:
        chapter_id: int
        concepts: List[str]
    
    Expected Output:
        List of chunk dictionaries:
        [
            {
                "text": str,
                "section_id": str,
                "relevance_score": float
            },
            ...
        ]
    """
    # TODO: Implement retrieval
    return []
```

## Pydantic Models

### DiagramRequest

```python
class DiagramRequest(BaseModel):
    diagram_type: str                        # Diagram type
    chapter_id: Optional[int] = None         # Chapter identifier
    concepts: List[str] = []                # Concepts to include
```

### DiagramNode

```python
class DiagramNode(BaseModel):
    id: str                                  # Node ID
    label: Optional[str] = None              # Node label
    type: Optional[str] = None              # Node type
    position: Optional[Dict[str, float]] = None  # Position (x, y)
    metadata: Optional[Dict[str, Any]] = None  # Additional metadata
```

### DiagramEdge

```python
class DiagramEdge(BaseModel):
    source: str                              # Source node ID
    target: str                              # Target node ID
    label: Optional[str] = None              # Edge label
    type: Optional[str] = None              # Edge type
    metadata: Optional[Dict[str, Any]] = None  # Additional metadata
```

### DiagramResponse

```python
class DiagramResponse(BaseModel):
    nodes: List[DiagramNode] = []            # Diagram nodes
    edges: List[DiagramEdge] = []           # Diagram edges
    svg: Optional[str] = None                # SVG string
    metadata: Optional[Dict[str, Any]] = None  # Additional metadata
```

## Data Flow Contracts

### Diagram Generation Flow

1. **Request** → `POST /api/ai/diagram` → `DiagramRequest`
2. **API** → `run_diagram_generator(diagram_type, chapter_id, concepts)` → Diagram Runtime
3. **Runtime** → `get_relevant_diagram_chunks(chapter_id, concepts)` → RAG Retrieval
4. **Runtime** → `plan_diagram()` → Diagram Agent
5. **Runtime** → `create_structure()` → Diagram Agent
6. **Runtime** → `generate_svg_stub()` → Diagram Agent
7. **Runtime** → `extraction_skill()`, `layout_skill()`, `svg_conversion_skill()` → Skills
8. **Runtime** → Returns `DiagramResponse` → API
9. **API** → Returns formatted response → Frontend

