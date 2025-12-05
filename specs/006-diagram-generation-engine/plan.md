# Implementation Plan: AI Diagram Generation Engine — Chapter Diagrams via AI → SVG → MDX

**Branch**: `006-diagram-generation-engine` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/006-diagram-generation-engine/spec.md`

## Summary

This feature creates the complete diagram generation engine scaffolding that converts conceptual inputs (robot anatomy, physical AI overview, etc.) into generated diagrams (SVG/PNG/Mermaid). The implementation establishes the architectural foundation for diagram providers (OpenAI, Gemini), diagram pipeline, template system, API endpoints, and frontend integration. **No real AI logic is implemented**—only scaffolding, function signatures, TODO placeholders, and architectural blueprints to prepare for future AI diagram generation implementation.

**Primary Deliverable**: Complete diagram generation infrastructure scaffolding (providers, pipeline, templates, API, frontend component)
**Validation**: All files exist, imports resolve, backend starts, frontend compiles, no runtime errors

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+
- Frontend: TypeScript/React with Docusaurus 3.x

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- React, TypeScript (already installed)
- No new runtime dependencies required (scaffolding only)

**Storage**:
- No persistent storage (scaffolding only)
- Future: Cache generated diagrams

**Testing**:
- Manual: File existence verification, import resolution, backend startup, frontend compilation
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)
- Frontend: Docusaurus MDX pages

**Project Type**: Backend AI infrastructure + Frontend component scaffolding

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- Frontend compilation: No errors
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (no API calls, no diagram generation)
- MUST maintain compatibility with Feature 005 (runtime engine integration)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend/frontend functionality

**Scale/Scope**:
- 8+ Python modules/files to create
- 1 TypeScript/React component
- 4 template files
- ~300-500 lines of scaffolding code (mostly signatures and TODOs)
- 2 provider files, 1 pipeline, 1 API endpoint, 1 frontend component

---

## 1. System Overview

### Architecture Purpose

The diagram generation engine provides a unified interface for generating visual diagrams from conceptual inputs. The system follows a provider-based architecture where different AI providers (OpenAI, Gemini) can be used to generate diagrams in various formats (SVG, PNG, Mermaid).

### High-Level Data Flow

```
Frontend (MDX) 
  → POST /api/diagram/generate 
  → Diagram Pipeline 
  → Base Diagram Provider (OpenAI/Gemini) 
  → SVG/Diagram Output 
  → Frontend DiagramRenderer Component
```

### Key Components

1. **Diagram Providers**: Abstract base class + OpenAI/Gemini implementations
2. **Diagram Pipeline**: Orchestrates diagram generation flow
3. **Template System**: Prompt templates for different diagram types
4. **API Endpoint**: RESTful interface for diagram generation
5. **Runtime Engine Integration**: Routes diagram blocks to pipeline
6. **Frontend Component**: Renders generated diagrams in MDX

### Integration Points

- **AI Runtime Engine** (Feature 005): Routes "diagram" block type to diagram pipeline
- **RAG Pipeline** (Feature 005): Can provide context for diagram generation (future)
- **MDX Content** (Feature 003): Diagrams embedded in chapter content

---

## 2. Folder + Module Structure

### Backend Structure

```
backend/app/
├── ai/
│   ├── diagrams/                    # NEW: Diagram generation module
│   │   ├── __init__.py
│   │   ├── base_diagram_provider.py # Abstract base class
│   │   ├── openai_diagram_provider.py
│   │   ├── gemini_diagram_provider.py
│   │   ├── pipeline.py              # Diagram generation pipeline
│   │   └── templates/               # NEW: Template directory
│   │       ├── anatomy_robot.txt
│   │       ├── physical_ai_overview.txt
│   │       ├── ai_robotics_stack.txt
│   │       └── core_concepts_flow.txt
│   └── runtime/
│       └── engine.py                # UPDATE: Add diagram routing
├── api/
│   └── diagram_generation.py       # NEW: Diagram API endpoint
└── config/
    └── settings.py                  # UPDATE: Add diagram config vars
```

### Frontend Structure

```
frontend/src/
└── components/
    └── diagrams/                    # NEW: Diagram components
        └── DiagramRenderer.tsx     # Diagram rendering component
```

### Specs Structure

```
specs/006-diagram-generation-engine/
├── spec.md                          # ✅ Complete
├── plan.md                          # ✅ In progress
├── tasks.md                         # TODO
├── research.md                      # ✅ Complete
├── data-model.md                    # ✅ Complete
├── quickstart.md                    # ✅ Complete
├── checklists/
│   └── requirements.md              # ✅ Complete
└── contracts/
    └── diagram-api.yaml             # ✅ Complete
```

---

## 3. Diagram Provider Architecture

### Base Provider Interface

**File**: `backend/app/ai/diagrams/base_diagram_provider.py`

**Purpose**: Abstract base class defining standard interface for all diagram providers.

**Structure**:
```python
class BaseDiagramProvider(ABC):
    @abstractmethod
    async def generate_diagram(payload: Dict[str, Any]) -> Dict[str, Any]
```

**Responsibilities**:
- Define interface contract
- Document expected input/output structure
- Provide base for provider implementations

**Integration**: Extended by OpenAI and Gemini providers

---

### OpenAI Provider Scaffold

**File**: `backend/app/ai/diagrams/openai_diagram_provider.py`

**Purpose**: Scaffold for OpenAI GPT-4o vision/output diagram generation.

**Structure**:
```python
class OpenAIDiagramProvider(BaseDiagramProvider):
    async def generate_diagram(payload: Dict[str, Any]) -> Dict[str, Any]
        # TODO: Implement OpenAI API calls
        return {"svg": "<svg><!-- TODO --></svg>", "format": "svg"}
```

**Responsibilities**:
- Implement BaseDiagramProvider interface
- Placeholder for OpenAI API integration
- Return placeholder SVG structure

**Future Implementation**:
- Use OpenAI API for diagram generation
- Support GPT-4o vision models
- Handle OpenAI-specific response format

---

### Gemini Provider Scaffold

**File**: `backend/app/ai/diagrams/gemini_diagram_provider.py`

**Purpose**: Scaffold for Gemini Flash/Image models diagram generation.

**Structure**:
```python
class GeminiDiagramProvider(BaseDiagramProvider):
    async def generate_diagram(payload: Dict[str, Any]) -> Dict[str, Any]
        # TODO: Implement Gemini API calls
        return {"svg": "<svg><!-- TODO --></svg>", "format": "svg"}
```

**Responsibilities**:
- Implement BaseDiagramProvider interface
- Placeholder for Gemini API integration
- Return placeholder SVG structure

**Future Implementation**:
- Use Gemini API for diagram generation
- Support Gemini Flash/Image models
- Handle Gemini-specific response format

---

## 4. Pipeline Architecture

### Pipeline Module

**File**: `backend/app/ai/diagrams/pipeline.py`

**Purpose**: Orchestrates the diagram generation flow from request to output.

**Pipeline Steps** (all TODO placeholders):

1. **Validate Diagram Type**
   - Check if diagram_type is supported
   - Validate input payload structure
   - TODO: Implement validation logic

2. **Build Prompt Template**
   - Load template file for diagram type
   - Substitute variables (concepts, chapter_id)
   - TODO: Implement template processing

3. **Call Provider**
   - Select provider based on config (DIAGRAM_PROVIDER)
   - Call provider.generate_diagram() with payload
   - TODO: Implement provider selection and call

4. **Receive SVG/Textual Description**
   - Receive diagram output from provider
   - Handle different output formats (SVG, PNG, Mermaid)
   - TODO: Implement output handling

5. **Format Output**
   - Format response for API
   - Add metadata (format, generation time, etc.)
   - TODO: Implement output formatting

**Function Signature**:
```python
async def run_diagram_pipeline(
    diagram_type: str,
    payload: Dict[str, Any]
) -> Dict[str, Any]:
    # Pipeline steps (all TODO)
    return {"svg": "<svg><!-- TODO --></svg>", "format": "svg"}
```

**Integration**:
- Called by API endpoint
- Called by runtime engine for diagram blocks
- Uses providers for actual generation

---

## 5. Template System

### Template Directory

**Path**: `backend/app/ai/diagrams/templates/`

**Purpose**: Store prompt templates for different diagram types.

### Template Files

1. **anatomy_robot.txt**
   - Robot anatomy diagram template
   - Placeholder instructions for robot components
   - Expected fields: sensors, actuators, control_system

2. **physical_ai_overview.txt**
   - Physical AI overview diagram template
   - Placeholder instructions for AI-robotics integration
   - Expected fields: ai_components, robotics_components, integration_points

3. **ai_robotics_stack.txt**
   - AI Robotics stack diagram template
   - Placeholder instructions for technology stack
   - Expected fields: layers, technologies, dependencies

4. **core_concepts_flow.txt**
   - Core concepts flow diagram template
   - Placeholder instructions for concept relationships
   - Expected fields: concepts, relationships, flow_direction

### Template Structure

Each template file contains:
- Placeholder instructions explaining expected fields
- TODO guidelines for future implementation
- Example structure for prompt building

**Future Implementation**:
- Variable substitution ({{concept}}, {{chapter_id}})
- Template validation
- Dynamic template loading

---

## 6. API Routing & Request Flow

### API Endpoint

**File**: `backend/app/api/diagram_generation.py`

**Route**: `POST /api/diagram/generate`

**Request Model**:
```python
class DiagramGenerateRequest(BaseModel):
    diagramType: str                  # "anatomy_robot", "physical_ai_overview", etc.
    chapterId: Optional[int] = None
    concepts: List[str] = []
```

**Response Model**:
```python
class DiagramGenerateResponse(BaseModel):
    svg: str                          # SVG string (placeholder)
    format: str = "svg"
    metadata: Optional[Dict[str, Any]] = None
```

**Endpoint Implementation**:
```python
@router.post("/generate", response_model=DiagramGenerateResponse)
async def generate_diagram(request: DiagramGenerateRequest):
    # TODO: Call run_diagram_pipeline()
    return DiagramGenerateResponse(svg="<svg><!-- TODO --></svg>")
```

### Request Flow

1. **Frontend** → POST `/api/diagram/generate` with request payload
2. **API Endpoint** → Validates request, calls `run_diagram_pipeline()`
3. **Pipeline** → Validates diagram type, builds prompt, calls provider
4. **Provider** → Generates diagram (placeholder currently)
5. **Pipeline** → Formats output
6. **API Endpoint** → Returns `DiagramGenerateResponse`
7. **Frontend** → Receives SVG string, renders with DiagramRenderer

### Router Integration

**File**: `backend/app/main.py`

**Update**: Include diagram_generation router
```python
from app.api import diagram_generation
app.include_router(diagram_generation.router)
```

---

## 7. Runtime Engine Integration

### Runtime Engine Update

**File**: `backend/app/ai/runtime/engine.py`

**Update**: Add diagram block routing

**Current Structure**:
```python
async def run_ai_block(block_type: str, request_data: Dict[str, Any]):
    # Step 1: Router - Determine which subagent to use
    # Step 2: RAG - Retrieve relevant context
    # Step 3: LLM Selection - Choose provider
    # Step 4: Subagent - Call appropriate subagent
    # Step 5: Response Formatting - Format output
```

**New Addition**:
```python
# TODO: Route diagram block → diagram pipeline
if block_type == "diagram":
    from app.ai.diagrams.pipeline import run_diagram_pipeline
    result = await run_diagram_pipeline(
        diagram_type=request_data.get("diagramType"),
        payload=request_data
    )
    return result
```

**Integration Point**: 
- Diagram blocks from Feature 004 (Interactive Blocks) route through runtime engine
- Runtime engine dispatches to diagram pipeline
- Pipeline handles diagram generation flow

---

## 8. Frontend Integration Scaffold

### DiagramRenderer Component

**File**: `frontend/src/components/diagrams/DiagramRenderer.tsx`

**Purpose**: React component for rendering diagrams in MDX pages.

**Props Interface**:
```typescript
interface DiagramRendererProps {
  svgString: string;                  // SVG string to render
  className?: string;                 // Optional CSS class
}
```

**Implementation** (Placeholder):
```typescript
export const DiagramRenderer: React.FC<DiagramRendererProps> = ({ svgString, className }) => {
  // TODO: Implement SVG rendering
  return <div className={className}>diagram goes here</div>;
};
```

**MDX Integration**:
- Component can be imported in MDX files
- Accepts SVG string from API response
- Renders placeholder initially

**Future Implementation**:
- Parse and render SVG
- Support Mermaid diagrams
- Add error handling
- Add loading states

---

## 9. Environment Variables

### Settings Configuration

**File**: `backend/app/config/settings.py`

**New Variables**:
```python
class Settings(BaseSettings):
    # ... existing settings ...
    
    # === Diagram Generation Configuration ===
    diagram_model: Optional[str] = None      # Diagram model identifier
    diagram_provider: str = "openai"         # Diagram provider selection
```

### Environment File

**File**: `.env.example`

**New Variables**:
```bash
# Diagram Generation Configuration
DIAGRAM_MODEL=...                            # Diagram model identifier
DIAGRAM_PROVIDER=openai                      # Options: "openai", "gemini"
```

### Usage

- `DIAGRAM_PROVIDER`: Selects which provider to use (OpenAI or Gemini)
- `DIAGRAM_MODEL`: Specific model identifier (e.g., "gpt-4o", "gemini-flash")

---

## 10. Contracts Explanation

### API Contract

**File**: `specs/006-diagram-generation-engine/contracts/diagram-api.yaml`

**Purpose**: Documents the API contract for diagram generation endpoint.

**Contents**:
- Endpoint definition
- Request schema with all fields
- Response schema (placeholder)
- Error responses
- Examples

**Status**: ✅ Already created in specification phase

---

## 11. Future Enhancements

### Phase 1: Real AI Implementation
- Implement OpenAI API calls for diagram generation
- Implement Gemini API calls for diagram generation
- Add error handling and retry logic
- Add response validation

### Phase 2: Template Processing
- Implement variable substitution in templates
- Add template validation
- Support dynamic template loading
- Add template caching

### Phase 3: Diagram Rendering
- Implement SVG rendering in frontend
- Support Mermaid diagram rendering
- Add diagram validation
- Add diagram caching

### Phase 4: Multiple Formats
- Support PNG output format
- Support PlantUML output format
- Add format conversion
- Add format validation

### Phase 5: Advanced Features
- Add diagram caching
- Add diagram versioning
- Add diagram editing
- Add diagram sharing

---

## 12. Implementation Sequencing (Phases 0–5)

### Phase 0: Project Setup & Prerequisites

**Purpose**: Verify dependencies and prepare directory structure.

**Tasks**:
- Verify Feature 005 (AI Runtime Engine) is complete
- Create `backend/app/ai/diagrams/` directory
- Create `backend/app/ai/diagrams/templates/` directory
- Create `frontend/src/components/diagrams/` directory
- Verify backend starts successfully
- Verify frontend compiles successfully

**Success Criteria**:
- All directories exist
- Backend starts without errors
- Frontend compiles without errors

---

### Phase 1: Providers Module

**Purpose**: Create diagram provider abstraction layer.

**Tasks**:
- Create `backend/app/ai/diagrams/__init__.py`
- Create `backend/app/ai/diagrams/base_diagram_provider.py` (abstract base class)
- Create `backend/app/ai/diagrams/openai_diagram_provider.py` (scaffold)
- Create `backend/app/ai/diagrams/gemini_diagram_provider.py` (scaffold)

**Success Criteria**:
- All provider files exist
- Abstract base class defined
- Provider scaffolds implement base interface
- Imports resolve correctly

---

### Phase 2: Pipeline Module

**Purpose**: Create diagram generation pipeline.

**Tasks**:
- Create `backend/app/ai/diagrams/pipeline.py`
- Add function `run_diagram_pipeline()` with 5-step flow
- Add TODO placeholders for each step
- Add placeholder return structure

**Success Criteria**:
- Pipeline file exists
- Function signature correct
- All 5 steps documented as TODO
- Imports resolve correctly

---

### Phase 3: Templates

**Purpose**: Create template files for different diagram types.

**Tasks**:
- Create `backend/app/ai/diagrams/templates/anatomy_robot.txt`
- Create `backend/app/ai/diagrams/templates/physical_ai_overview.txt`
- Create `backend/app/ai/diagrams/templates/ai_robotics_stack.txt`
- Create `backend/app/ai/diagrams/templates/core_concepts_flow.txt`
- Add placeholder instructions to each template

**Success Criteria**:
- All 4 template files exist
- Each file contains placeholder instructions
- Each file documents expected fields

---

### Phase 4: Backend API

**Purpose**: Create API endpoint for diagram generation.

**Tasks**:
- Create `backend/app/api/diagram_generation.py`
- Define `POST /api/diagram/generate` endpoint
- Add request/response models (Pydantic)
- Add TODO placeholder implementation
- Include router in `backend/app/main.py`

**Success Criteria**:
- API endpoint file exists
- Endpoint defined with proper route
- Request/response models correct
- Router included in main.py
- Backend starts without errors

---

### Phase 5: Runtime Engine Integration

**Purpose**: Integrate diagram generation into runtime engine.

**Tasks**:
- Update `backend/app/ai/runtime/engine.py`
- Add diagram block routing logic
- Add TODO comment for diagram pipeline integration
- Ensure no breaking changes

**Success Criteria**:
- Runtime engine updated
- Diagram routing added
- No breaking changes
- Imports resolve correctly

---

### Phase 6: Frontend Integration

**Purpose**: Create frontend component for diagram rendering.

**Tasks**:
- Create `frontend/src/components/diagrams/DiagramRenderer.tsx`
- Add TypeScript interface for props
- Add placeholder rendering
- Ensure component compiles

**Success Criteria**:
- Component file exists
- TypeScript types correct
- Component compiles without errors
- Can be imported in MDX files

---

### Phase 7: Configuration

**Purpose**: Add diagram-related configuration.

**Tasks**:
- Update `backend/app/config/settings.py` (add diagram_model, diagram_provider)
- Update `.env.example` (add DIAGRAM_MODEL, DIAGRAM_PROVIDER)
- Update `backend/app/main.py` (add config logging)

**Success Criteria**:
- Settings.py includes new variables
- .env.example includes new variables
- Backend reads configuration without errors

---

### Phase 8: Validation

**Purpose**: Verify all modules work correctly.

**Tasks**:
- Test backend imports (all modules resolve)
- Test backend startup (no errors)
- Test frontend compilation (no errors)
- Test API endpoint (returns placeholder response)
- Verify no breaking changes to existing features

**Success Criteria**:
- All imports resolve
- Backend starts successfully
- Frontend compiles successfully
- API endpoint responds correctly
- No breaking changes

---

## Risk Analysis & Mitigation

### Risk 1: Breaking Existing Features

**Risk**: Changes to runtime engine may break existing AI block functionality.

**Mitigation**: 
- Add diagram routing as separate conditional block
- Test all existing endpoints after changes
- Maintain backward compatibility

### Risk 2: Import Resolution Failures

**Risk**: New modules may have import errors.

**Mitigation**:
- Create all `__init__.py` files
- Test imports incrementally
- Fix errors immediately

### Risk 3: Frontend Compilation Errors

**Risk**: New TypeScript component may have compilation errors.

**Mitigation**:
- Use proper TypeScript types
- Test compilation after component creation
- Fix errors immediately

---

## Acceptance Criteria Mapping

| Success Criteria | Implementation Phase | Validation Method |
|------------------|---------------------|-------------------|
| **SC-001**: All scaffold modules exist | Phase 1-3 | File existence checks |
| **SC-002**: No real AI logic | All phases | Code review |
| **SC-003**: Backend starts successfully | Phase 8 | Backend startup test |
| **SC-004**: Frontend compiles | Phase 6, 8 | Frontend compilation test |
| **SC-005**: API contract documented | ✅ Complete | File existence |

---

**Plan Generation Complete**: 2025-12-05
**Ready for Tasks**: Yes ✅

