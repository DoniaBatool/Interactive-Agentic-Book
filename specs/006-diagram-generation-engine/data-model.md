# Data Model: AI Diagram Generation Engine

**Generated**: 2025-12-05
**Feature**: 006-diagram-generation-engine

## Function Signatures

### Base Diagram Provider

```python
class BaseDiagramProvider(ABC):
    @abstractmethod
    async def generate_diagram(
        self,
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate diagram from payload.
        
        Expected Input:
            payload: {
                "diagram_type": str,        # "anatomy_robot", "physical_ai_overview", etc.
                "concepts": List[str],       # Concepts to include
                "chapter_id": int,          # Chapter identifier
                "format": str                # "svg", "png", "mermaid"
            }
        
        Expected Output:
            {
                "svg": str,                 # SVG string or diagram code
                "format": str,              # Output format
                "metadata": Dict[str, Any]  # Additional metadata
            }
        """
        pass
```

### OpenAI Diagram Provider

```python
class OpenAIDiagramProvider(BaseDiagramProvider):
    async def generate_diagram(
        self,
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        # TODO: Implement OpenAI API calls
        return {"svg": "<svg><!-- TODO --></svg>", "format": "svg"}
```

### Gemini Diagram Provider

```python
class GeminiDiagramProvider(BaseDiagramProvider):
    async def generate_diagram(
        self,
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        # TODO: Implement Gemini API calls
        return {"svg": "<svg><!-- TODO --></svg>", "format": "svg"}
```

### Diagram Pipeline

```python
async def run_diagram_pipeline(
    diagram_type: str,
    payload: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Execute diagram generation pipeline.
    
    Expected Input:
        diagram_type: str                   # "anatomy_robot", "physical_ai_overview", etc.
        payload: {
            "concepts": List[str],          # Concepts to include
            "chapter_id": int,              # Chapter identifier
            "format": str                   # Output format
        }
    
    Expected Output:
        {
            "svg": str,                     # Generated SVG string
            "format": str,                  # Output format
            "metadata": Dict[str, Any]      # Pipeline metadata
        }
    """
    # TODO: Implement pipeline steps
    return {"svg": "<svg><!-- TODO --></svg>", "format": "svg"}
```

## API Request/Response Models

### Diagram Generate Request

```python
class DiagramGenerateRequest(BaseModel):
    diagramType: str                        # "anatomy_robot", "physical_ai_overview", etc.
    chapterId: Optional[int] = None        # Chapter identifier
    concepts: List[str] = []               # Concepts to include in diagram
```

### Diagram Generate Response

```python
class DiagramGenerateResponse(BaseModel):
    svg: str                                # SVG string (placeholder: "<svg><!-- TODO --></svg>")
    format: str = "svg"                     # Output format
    metadata: Optional[Dict[str, Any]] = None  # Additional metadata
```

## Frontend Component Props

### DiagramRenderer Component

```typescript
interface DiagramRendererProps {
  svgString: string;                        // SVG string to render
  className?: string;                       // Optional CSS class
}
```

## Configuration Schema

### Settings Configuration

```python
class Settings(BaseSettings):
    diagram_model: Optional[str] = None    # Diagram model identifier
    diagram_provider: str = "openai"       # Diagram provider selection
```

### Environment Variables

```bash
DIAGRAM_MODEL=...                          # Diagram model identifier
DIAGRAM_PROVIDER=openai                    # Options: "openai", "gemini"
```

## Data Flow Contracts

### Request Flow

1. **Frontend** → `POST /api/diagram/generate` → `DiagramGenerateRequest`
2. **API Endpoint** → `run_diagram_pipeline()` → `diagram_type, payload`
3. **Pipeline** → `BaseDiagramProvider.generate_diagram()` → `payload`
4. **Provider** → Returns `{"svg": str, "format": str, "metadata": Dict}`

### Response Flow

1. **Provider** → Returns diagram data
2. **Pipeline** → Formats output
3. **API Endpoint** → Returns `DiagramGenerateResponse`
4. **Frontend** → `DiagramRenderer` renders SVG

## Template Structure

### Template File Format

```
# Diagram Template: <diagram_type>

## Expected Fields
- concept: str
- chapter_id: int
- format: str

## TODO Guidelines
- Build prompt from template
- Substitute variables
- Call provider with prompt

## Placeholder Instructions
[Template content with placeholder fields]
```

## Type Definitions

### Diagram Type Enum

```python
DiagramType = Literal[
    "anatomy_robot",
    "physical_ai_overview",
    "ai_robotics_stack",
    "core_concepts_flow"
]
```

### Diagram Format Enum

```python
DiagramFormat = Literal["svg", "png", "mermaid", "plantuml"]
```

