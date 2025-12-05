# Tasks: AI Diagram Generation Engine — Chapter Diagrams via AI → SVG → MDX

**Feature**: 006-diagram-generation-engine | **Branch**: `006-diagram-generation-engine` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating diagram generation infrastructure scaffolding (providers, pipeline, templates, API, frontend component). All tasks are scaffolding only—no real AI logic implementation.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category**: SETUP (Initial setup), MODULE (Module creation), CONNECT (Integration), VALIDATE (Validation), DOCS (Documentation)

---

## Phase 0: Project Setup & Prerequisites

**Purpose**: Verify dependencies and prepare directory structure before creating modules.

- [ ] [T001] [P1] [SETUP] Verify Feature 005 (AI Runtime Engine) is complete: `backend/app/ai/runtime/engine.py` exists and `run_ai_block()` function is available
- [ ] [T002] [P1] [SETUP] Create directory structure: `backend/app/ai/diagrams/` and `backend/app/ai/diagrams/templates/`
- [ ] [T003] [P1] [SETUP] Create directory structure: `frontend/src/components/diagrams/`
- [ ] [T004] [P1] [SETUP] Verify backend starts successfully: Run `cd backend && uvicorn app.main:app` to confirm no errors before adding new modules
- [ ] [T005] [P1] [SETUP] Verify frontend compiles successfully: Run `cd frontend && npm run build` to confirm no errors before adding new components

**Success Criteria**:
- All prerequisite features complete
- Directory structure ready
- Backend starts without errors
- Frontend compiles without errors

**Dependencies**: Feature 005 (AI Runtime Engine) must be complete

---

## Phase 1: Providers Module Tasks

**Purpose**: Create diagram provider abstraction layer with base interface and provider scaffolds.

### Base Diagram Provider

- [ ] [T006] [P1] [MODULE] Create `backend/app/ai/diagrams/__init__.py` with package initialization
- [ ] [T007] [P1] [MODULE] Create `backend/app/ai/diagrams/base_diagram_provider.py` with:
  - Import statements: `from abc import ABC, abstractmethod`, `from typing import Dict, Any`
  - Abstract base class `BaseDiagramProvider(ABC)` with abstract method `async def generate_diagram(payload: Dict[str, Any]) -> Dict[str, Any]`
  - Docstring explaining interface contract
  - TODO comment: `# TODO: Implement in provider subclasses`

### OpenAI Diagram Provider

- [ ] [T008] [P1] [MODULE] Create `backend/app/ai/diagrams/openai_diagram_provider.py` with:
  - Import: `from app.ai.diagrams.base_diagram_provider import BaseDiagramProvider`
  - Class `OpenAIDiagramProvider(BaseDiagramProvider)` implementing base interface
  - Method `async def generate_diagram(payload: Dict[str, Any]) -> Dict[str, Any]` with TODO placeholder: `# TODO: Implement OpenAI API calls for diagram generation`
  - Placeholder return: `return {"svg": "<svg><!-- TODO --></svg>", "format": "svg"}`
  - Docstring explaining OpenAI-specific implementation

### Gemini Diagram Provider

- [ ] [T009] [P1] [MODULE] Create `backend/app/ai/diagrams/gemini_diagram_provider.py` with:
  - Import: `from app.ai.diagrams.base_diagram_provider import BaseDiagramProvider`
  - Class `GeminiDiagramProvider(BaseDiagramProvider)` implementing base interface
  - Method `async def generate_diagram(payload: Dict[str, Any]) -> Dict[str, Any]` with TODO placeholder: `# TODO: Implement Gemini API calls for diagram generation`
  - Placeholder return: `return {"svg": "<svg><!-- TODO --></svg>", "format": "svg"}`
  - Docstring explaining Gemini-specific implementation

**Acceptance Test**: All provider files exist, imports resolve, backend starts without errors

---

## Phase 2: Pipeline Module Tasks

**Purpose**: Create diagram generation pipeline with placeholder flow steps.

- [ ] [T010] [P1] [MODULE] Create `backend/app/ai/diagrams/pipeline.py` with:
  - Import statements: `from typing import Dict, Any`
  - Function `async def run_diagram_pipeline(diagram_type: str, payload: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints for all parameters and return value
    - Docstring explaining pipeline purpose
    - Step-by-step TODO comments:
      - `# Step 1: Validate diagram type (TODO)`
      - `# Step 2: Build prompt template (TODO)`
      - `# Step 3: Call provider (TODO)`
      - `# Step 4: Receive SVG or textual diagram description (TODO)`
      - `# Step 5: Format output (TODO)`
    - Placeholder return: `return {"svg": "<svg><!-- TODO --></svg>", "format": "svg"}`

**Acceptance Test**: Pipeline file exists, function signature correct, imports resolve

---

## Phase 3: Templates Tasks

**Purpose**: Create template files for different diagram types with placeholder instructions.

- [ ] [T011] [P1] [MODULE] Create `backend/app/ai/diagrams/templates/anatomy_robot.txt` with:
  - Placeholder instructions explaining expected fields (sensors, actuators, control_system)
  - TODO guidelines for future implementation
  - Example structure for prompt building

- [ ] [T012] [P1] [MODULE] Create `backend/app/ai/diagrams/templates/physical_ai_overview.txt` with:
  - Placeholder instructions explaining expected fields (ai_components, robotics_components, integration_points)
  - TODO guidelines for future implementation
  - Example structure for prompt building

- [ ] [T013] [P1] [MODULE] Create `backend/app/ai/diagrams/templates/ai_robotics_stack.txt` with:
  - Placeholder instructions explaining expected fields (layers, technologies, dependencies)
  - TODO guidelines for future implementation
  - Example structure for prompt building

- [ ] [T014] [P1] [MODULE] Create `backend/app/ai/diagrams/templates/core_concepts_flow.txt` with:
  - Placeholder instructions explaining expected fields (concepts, relationships, flow_direction)
  - TODO guidelines for future implementation
  - Example structure for prompt building

**Acceptance Test**: All 4 template files exist, each contains placeholder instructions

---

## Phase 4: Backend API Tasks

**Purpose**: Create API endpoint for diagram generation with request/response models.

- [ ] [T015] [P1] [MODULE] Create `backend/app/api/diagram_generation.py` with:
  - Import statements: `from fastapi import APIRouter`, `from pydantic import BaseModel`, `from typing import Optional, List, Dict, Any`
  - Router creation: `router = APIRouter(prefix="/api/diagram", tags=["diagram-generation"])`
  - Request model `DiagramGenerateRequest` with fields:
    - `diagramType: str` (required)
    - `chapterId: Optional[int] = None`
    - `concepts: List[str] = []`
  - Response model `DiagramGenerateResponse` with fields:
    - `svg: str` (placeholder: `"<svg><!-- TODO --></svg>"`)
    - `format: str = "svg"`
    - `metadata: Optional[Dict[str, Any]] = None`
  - Endpoint `@router.post("/generate", response_model=DiagramGenerateResponse)` with:
    - TODO placeholder implementation
    - Placeholder return: `return DiagramGenerateResponse(svg="<svg><!-- TODO --></svg>")`

- [ ] [T016] [P1] [CONNECT] Update `backend/app/main.py`:
  - Add import: `from app.api import diagram_generation`
  - Include router: `app.include_router(diagram_generation.router)`
  - Verify no syntax errors: Run `python -m py_compile backend/app/main.py`

**Acceptance Test**: API endpoint file exists, request/response models correct, router included in main.py, backend starts without errors

---

## Phase 5: Runtime Engine Integration Tasks

**Purpose**: Integrate diagram generation into runtime engine.

- [ ] [T017] [P1] [CONNECT] Update `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Route diagram block → diagram pipeline`
  - Add conditional routing for "diagram" block type:
    ```python
    if block_type == "diagram":
        from app.ai.diagrams.pipeline import run_diagram_pipeline
        result = await run_diagram_pipeline(
            diagram_type=request_data.get("diagramType"),
            payload=request_data
        )
        return result
    ```
  - Ensure no breaking changes to existing functionality
  - Verify no syntax errors: Run `python -m py_compile backend/app/ai/runtime/engine.py`

**Acceptance Test**: Runtime engine updated, diagram routing added, no breaking changes, imports resolve

---

## Phase 6: Frontend Integration Tasks

**Purpose**: Create frontend component for diagram rendering.

- [ ] [T018] [P1] [MODULE] Create `frontend/src/components/diagrams/DiagramRenderer.tsx` with:
  - Import statements: `import React from 'react';`
  - TypeScript interface `DiagramRendererProps` with:
    - `svgString: string` (required)
    - `className?: string` (optional)
  - Component `export const DiagramRenderer: React.FC<DiagramRendererProps>` with:
    - Placeholder rendering: `return <div className={className}>diagram goes here</div>;`
    - TODO comment: `// TODO: Implement SVG rendering`
  - Ensure TypeScript compiles without errors

**Acceptance Test**: Component file exists, TypeScript types correct, component compiles, can be imported in MDX files

---

## Phase 7: Configuration Tasks

**Purpose**: Add diagram-related configuration to settings and .env.example.

### Settings.py Updates

- [ ] [T019] [P1] [CONNECT] Update `backend/app/config/settings.py`:
  - Add to Settings class:
    - `diagram_model: Optional[str] = None` with docstring: "Diagram model identifier (e.g., gpt-4o, gemini-flash)"
    - `diagram_provider: str = "openai"` with docstring: "Diagram provider selection (openai, gemini)"
  - Verify no syntax errors: Run `python -m py_compile backend/app/config/settings.py`

### .env.example Updates

- [ ] [T020] [P1] [CONNECT] Update `.env.example`:
  - Add section: `# Diagram Generation Configuration`
  - Add `DIAGRAM_MODEL=...` with comment: `# Diagram model identifier`
  - Add `DIAGRAM_PROVIDER=openai` with comment: `# Options: openai, gemini`

### Main.py Configuration Logging

- [ ] [T021] [P2] [CONNECT] Update `backend/app/main.py` startup logging:
  - Add diagram configuration status:
    ```python
    print(f"  - Diagram Provider: {settings.diagram_provider}")
    print(f"  - Diagram Model: {'✅ Configured' if settings.diagram_model else '⚠️  Not set (optional)'}")
    ```

**Acceptance Test**: Settings.py includes new variables, .env.example updated, backend reads config without errors

---

## Phase 8: Validation Tasks

**Purpose**: Verify all modules exist, imports resolve, and backend/frontend work correctly.

### File Existence Validation

- [ ] [T022] [P1] [VALIDATE] Verify all provider files exist:
  - Check `backend/app/ai/diagrams/base_diagram_provider.py` exists
  - Check `backend/app/ai/diagrams/openai_diagram_provider.py` exists
  - Check `backend/app/ai/diagrams/gemini_diagram_provider.py` exists

- [ ] [T023] [P1] [VALIDATE] Verify pipeline file exists:
  - Check `backend/app/ai/diagrams/pipeline.py` exists

- [ ] [T024] [P1] [VALIDATE] Verify all template files exist:
  - Check `backend/app/ai/diagrams/templates/anatomy_robot.txt` exists
  - Check `backend/app/ai/diagrams/templates/physical_ai_overview.txt` exists
  - Check `backend/app/ai/diagrams/templates/ai_robotics_stack.txt` exists
  - Check `backend/app/ai/diagrams/templates/core_concepts_flow.txt` exists

- [ ] [T025] [P1] [VALIDATE] Verify API endpoint file exists:
  - Check `backend/app/api/diagram_generation.py` exists

- [ ] [T026] [P1] [VALIDATE] Verify frontend component exists:
  - Check `frontend/src/components/diagrams/DiagramRenderer.tsx` exists

### Import Resolution Validation

- [ ] [T027] [P1] [VALIDATE] Test provider imports:
  - Run: `python -c "from app.ai.diagrams.base_diagram_provider import BaseDiagramProvider; print('OK')"`
  - Run: `python -c "from app.ai.diagrams.openai_diagram_provider import OpenAIDiagramProvider; print('OK')"`
  - Run: `python -c "from app.ai.diagrams.gemini_diagram_provider import GeminiDiagramProvider; print('OK')"`

- [ ] [T028] [P1] [VALIDATE] Test pipeline import:
  - Run: `python -c "from app.ai.diagrams.pipeline import run_diagram_pipeline; print('OK')"`

- [ ] [T029] [P1] [VALIDATE] Test API endpoint import:
  - Run: `python -c "from app.api.diagram_generation import router; print('OK')"`

### Backend Startup Validation

- [ ] [T030] [P1] [VALIDATE] Start backend server: Run `cd backend && uvicorn app.main:app --reload`
  - Verify: Server starts without ImportError
  - Verify: Server starts without ModuleNotFoundError
  - Verify: Server starts without syntax errors
  - Verify: Health endpoint responds: `curl http://localhost:8000/health`

- [ ] [T031] [P1] [VALIDATE] Test API endpoint responds:
  - Test `POST /api/diagram/generate` with `{"diagramType": "anatomy_robot", "chapterId": 1, "concepts": ["sensors"]}`
  - Verify: Endpoint responds (even if placeholder response)
  - Verify: No 500 Internal Server Error
  - Verify: Response format is valid JSON with `svg` field

### Frontend Compilation Validation

- [ ] [T032] [P1] [VALIDATE] Test frontend compilation: Run `cd frontend && npm run build`
  - Verify: TypeScript compiles without errors
  - Verify: DiagramRenderer.tsx compiles
  - Verify: Docusaurus build succeeds
  - Verify: No linting errors

- [ ] [T033] [P1] [VALIDATE] Test DiagramRenderer import:
  - Create test MDX file or verify component can be imported
  - Verify: Component imports without errors

### Module Dependency Validation

- [ ] [T034] [P1] [VALIDATE] Verify no circular imports:
  - Check all imports are forward references or top-level
  - Verify diagram pipeline imports providers without circular dependency

- [ ] [T035] [P1] [VALIDATE] Verify all TODO placeholders present:
  - Check all functions contain TODO comments
  - Check all modules have docstrings explaining purpose
  - Verify no real AI logic (no OpenAI, Gemini API calls)

### Runtime Engine Integration Validation

- [ ] [T036] [P1] [VALIDATE] Test runtime engine diagram routing:
  - Verify: Runtime engine includes diagram block routing
  - Verify: No breaking changes to existing block types
  - Verify: Diagram routing calls pipeline correctly

---

## Task Summary

**Total Tasks**: 36 tasks
- **Phase 0 (Setup)**: 5 tasks
- **Phase 1 (Providers)**: 4 tasks
- **Phase 2 (Pipeline)**: 1 task
- **Phase 3 (Templates)**: 4 tasks
- **Phase 4 (Backend API)**: 2 tasks
- **Phase 5 (Runtime Engine)**: 1 task
- **Phase 6 (Frontend)**: 1 task
- **Phase 7 (Configuration)**: 3 tasks
- **Phase 8 (Validation)**: 15 tasks

**Critical Path**: T001-T005 → T006-T009 → T010 → T011-T014 → T015-T016 → T017 → T018 → T019-T021 → T022-T036

**Estimated Time**: 2-3 hours (file creation + function signatures + imports + validation)

---

## Success Criteria Validation

### Spec Success Criteria → Task Mapping

| Success Criteria | Task IDs | Validation Method |
|------------------|----------|-------------------|
| **SC-001**: All scaffold modules exist | T022-T026 | File existence checks |
| **SC-002**: No real AI logic | T035 | Code review |
| **SC-003**: Backend starts successfully | T030 | Backend startup test |
| **SC-004**: Frontend compiles | T032-T033 | Frontend compilation test |
| **SC-005**: API contract documented | ✅ Already exists | File existence |

---

## Dependencies & Risks

### Internal Dependencies
- ✅ Feature 005 (AI Runtime Engine) complete

### External Dependencies
- ✅ Python 3.11+, FastAPI 0.109+, Pydantic 2.x (already installed)
- ✅ React, TypeScript, Docusaurus 3.x (already installed)
- ✅ No new runtime dependencies required (scaffolding only)

### Risks & Mitigations

**Risk 1**: Import resolution failures
- **Mitigation**: Test imports incrementally (T027-T029), fix errors immediately

**Risk 2**: Breaking Feature 005 compatibility
- **Mitigation**: Update runtime engine carefully (T017), test existing endpoints after update

**Risk 3**: Missing __init__.py files
- **Mitigation**: Create all __init__.py files in Phase 1 (T006)

**Risk 4**: Frontend compilation errors
- **Mitigation**: Test TypeScript compilation (T032), fix errors immediately

**Risk 5**: Circular import issues
- **Mitigation**: Validate dependencies (T034), use forward references if needed

---

**Task Generation Complete**: 2025-12-05
**Ready for Implementation**: Yes ✅
**Next Command**: `/sp.implement` (or manual task-by-task execution)

