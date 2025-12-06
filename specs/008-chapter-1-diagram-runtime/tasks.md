# Tasks: Chapter 1 — Diagram Generator Runtime

**Feature**: 008-chapter-1-diagram-runtime | **Branch**: `008-chapter-1-diagram-runtime` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating diagram generator runtime infrastructure scaffolding (runtime, agent, schema, skills, RAG retrieval, API integration). All tasks are scaffolding only—no real AI logic implementation.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category**: SETUP (Initial setup), RUNTIME (Runtime module), AGENT (Agent module), SKILLS (Skills module), SCHEMA (Schema module), API (API integration), RAG (RAG module), VALIDATE (Validation), DOCS (Documentation)

---

## Setup Tasks

**Purpose**: Verify dependencies and prepare directory structure.

- [ ] [T001] [P1] [SETUP] Verify Feature 005 (AI Runtime Engine) is complete: `backend/app/ai/runtime/engine.py`, `backend/app/ai/rag/pipeline.py` exist
- [ ] [T002] [P1] [SETUP] Verify Feature 006 (Diagram Generation Engine) is complete: `backend/app/ai/diagrams/` directory exists
- [ ] [T003] [P1] [SETUP] Create directory structure: `backend/app/ai/diagram/` (if not exists)
- [ ] [T004] [P1] [SETUP] Verify backend starts successfully: Run `cd backend && uvicorn app.main:app` to confirm no errors before adding new modules

**Success Criteria**:
- All prerequisite features complete
- Directory structure ready
- Backend starts without errors

**Dependencies**: Feature 005 and Feature 006 must be complete

---

## Runtime Tasks

**Purpose**: Create diagram runtime orchestrator module.

- [ ] [T005] [P1] [RUNTIME] Create `backend/app/ai/diagram/__init__.py` with package initialization
- [ ] [T006] [P1] [RUNTIME] Create `backend/app/ai/diagram/runtime.py` with:
  - Import statements: `from typing import List, Dict, Any`
  - Function `async def run_diagram_generator(diagram_type: str, chapter_id: int, concepts: List[str]) -> Dict[str, Any]` with:
    - Type hints for all parameters and return value
    - Docstring explaining orchestration flow
    - Step-by-step TODO comments:
      - `# Step 1: Validate input (diagramType, chapterId, concepts[]) - TODO`
      - `# Step 2: Retrieve contextual chunks (future RAG) - TODO`
      - `# Step 3: Use Diagram Agent - TODO`
      - `# Step 4: Format final diagram output structure - TODO`
    - Placeholder return: `return {"nodes": [], "edges": [], "svg": "", "metadata": {}}`

**Acceptance Test**: Runtime file exists, function signature correct, imports resolve

---

## Agent Tasks

**Purpose**: Update diagram agent with plan, create, generate methods.

- [ ] [T007] [P1] [AGENT] Update `backend/app/ai/subagents/diagram_agent.py`:
  - Add function `def plan_diagram(diagram_type: str, concepts: List[str], context: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints and docstring: "Plan diagram structure using LLM reasoning. TODO: Implement"
    - TODO placeholder: `# TODO: Implement planning logic`
    - Placeholder return: `return {}`
  - Add function `def create_structure(plan: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints and docstring: "Create diagram structure (nodes, edges). TODO: Implement"
    - TODO placeholder: `# TODO: Implement structure creation`
    - Placeholder return: `return {}`
  - Add function `def generate_svg_stub(structure: Dict[str, Any]) -> str` with:
    - Type hints and docstring: "Generate SVG stub or code. TODO: Implement"
    - TODO placeholder: `# TODO: Implement SVG generation`
    - Placeholder return: `return ""`
  - Maintain existing `diagram_agent()` function (no breaking changes)
  - Verify no syntax errors: Run `python -m py_compile backend/app/ai/subagents/diagram_agent.py`

**Acceptance Test**: Diagram agent updated, all three methods defined, no breaking changes

---

## Schema Tasks

**Purpose**: Create Pydantic models for diagram data structures.

- [ ] [T008] [P1] [SCHEMA] Create `backend/app/ai/diagram/schema.py` with:
  - Import statements: `from pydantic import BaseModel`, `from typing import Optional, List, Dict, Any`
  - Model `class DiagramRequest(BaseModel)` with:
    - `diagram_type: str` (required)
    - `chapter_id: Optional[int] = None`
    - `concepts: List[str] = []`
  - Model `class DiagramNode(BaseModel)` with:
    - `id: str` (required)
    - `label: Optional[str] = None`
    - `type: Optional[str] = None`
    - `position: Optional[Dict[str, float]] = None`
    - `metadata: Optional[Dict[str, Any]] = None`
  - Model `class DiagramEdge(BaseModel)` with:
    - `source: str` (required)
    - `target: str` (required)
    - `label: Optional[str] = None`
    - `type: Optional[str] = None`
    - `metadata: Optional[Dict[str, Any]] = None`
  - Model `class DiagramResponse(BaseModel)` with:
    - `nodes: List[DiagramNode] = []`
    - `edges: List[DiagramEdge] = []`
    - `svg: Optional[str] = None`
    - `metadata: Optional[Dict[str, Any]] = None`

**Acceptance Test**: Schema file exists, all four models defined, imports resolve

---

## Skills Tasks

**Purpose**: Create diagram skills module.

- [ ] [T009] [P1] [SKILLS] Create `backend/app/ai/skills/diagram_skill.py` with:
  - Import statements: `from typing import List, Dict, Any`
  - Function `def extraction_skill(context: Dict[str, Any], concepts: List[str]) -> Dict[str, Any]` with:
    - Type hints and docstring: "Extract diagram elements from context. TODO: Implement"
    - TODO placeholder: `# TODO: Implement extraction logic`
    - Placeholder return: `return {}`
  - Function `def layout_skill(elements: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints and docstring: "Layout diagram structure. TODO: Implement"
    - TODO placeholder: `# TODO: Implement layout logic`
    - Placeholder return: `return {}`
  - Function `def svg_conversion_skill(structure: Dict[str, Any]) -> str` with:
    - Type hints and docstring: "Convert structured diagram to SVG. TODO: Implement"
    - TODO placeholder: `# TODO: Implement SVG conversion`
    - Placeholder return: `return ""`

**Acceptance Test**: Skills file exists, all three functions defined, imports resolve

---

## API Integration Tasks

**Purpose**: Update diagram endpoint to call diagram runtime.

- [ ] [T010] [P1] [API] Update `backend/app/api/ai_blocks.py`:
  - Add import: `from app.ai.diagram.runtime import run_diagram_generator`
  - Update `diagram` endpoint:
    - Replace placeholder return with: `result = await run_diagram_generator(request.diagramType, request.chapterId or 1, request.concepts or [])`
    - Add TODO comment: `# TODO: Update response model to match diagram runtime output format`
    - Return: `return AIBlockResponse(**result)` (or handle response format)
  - Verify no syntax errors: Run `python -m py_compile backend/app/api/ai_blocks.py`

**Acceptance Test**: API endpoint updated, routes to diagram runtime, no breaking changes, backend starts without errors

---

## RAG Placeholder Tasks

**Purpose**: Create RAG retrieval module for diagram context.

- [ ] [T011] [P1] [RAG] Create `backend/app/ai/rag/diagram_retrieval.py` with:
  - Import statements: `from typing import List, Dict, Any`
  - Function `def get_relevant_diagram_chunks(chapter_id: int, concepts: List[str]) -> List[Dict[str, Any]]` with:
    - Type hints for all parameters and return value
    - Docstring: "Retrieve relevant chunks for diagram generation. TODO: Implement retrieval logic"
    - TODO placeholders:
      - `# TODO: Implement retrieval logic`
      - `# TODO: Use RAG pipeline to retrieve chunks`
      - `# TODO: Filter chunks by relevance to concepts`
      - `# TODO: Rank chunks by relevance score`
    - Placeholder return: `return []`

**Acceptance Test**: RAG retrieval file exists, function signature correct, imports resolve

---

## Validation Tasks

**Purpose**: Verify all modules exist, imports resolve, and backend works correctly.

### File Existence Validation

- [ ] [T012] [P1] [VALIDATE] Verify diagram runtime file exists:
  - Check `backend/app/ai/diagram/runtime.py` exists

- [ ] [T013] [P1] [VALIDATE] Verify diagram schema file exists:
  - Check `backend/app/ai/diagram/schema.py` exists

- [ ] [T014] [P1] [VALIDATE] Verify diagram skills file exists:
  - Check `backend/app/ai/skills/diagram_skill.py` exists

- [ ] [T015] [P1] [VALIDATE] Verify RAG diagram retrieval file exists:
  - Check `backend/app/ai/rag/diagram_retrieval.py` exists

### Import Resolution Validation

- [ ] [T016] [P1] [VALIDATE] Test diagram runtime import:
  - Run: `python -c "from app.ai.diagram.runtime import run_diagram_generator; print('OK')"`

- [ ] [T017] [P1] [VALIDATE] Test diagram schema imports:
  - Run: `python -c "from app.ai.diagram.schema import DiagramRequest, DiagramNode, DiagramEdge, DiagramResponse; print('OK')"`

- [ ] [T018] [P1] [VALIDATE] Test diagram skills imports:
  - Run: `python -c "from app.ai.skills.diagram_skill import extraction_skill, layout_skill, svg_conversion_skill; print('OK')"`

- [ ] [T019] [P1] [VALIDATE] Test RAG diagram retrieval import:
  - Run: `python -c "from app.ai.rag.diagram_retrieval import get_relevant_diagram_chunks; print('OK')"`

- [ ] [T020] [P1] [VALIDATE] Test diagram agent methods:
  - Run: `python -c "from app.ai.subagents.diagram_agent import plan_diagram, create_structure, generate_svg_stub; print('OK')"`

### Backend Startup Validation

- [ ] [T021] [P1] [VALIDATE] Start backend server: Run `cd backend && uvicorn app.main:app --reload`
  - Verify: Server starts without ImportError
  - Verify: Server starts without ModuleNotFoundError
  - Verify: Server starts without syntax errors
  - Verify: Health endpoint responds: `curl http://localhost:8000/health`

- [ ] [T022] [P1] [VALIDATE] Test API endpoint routes correctly:
  - Test `POST /api/ai/diagram` with `{"diagramType": "anatomy_robot", "chapterId": 1, "concepts": ["sensors"]}`
  - Verify: Endpoint responds (even if placeholder response)
  - Verify: No 500 Internal Server Error
  - Verify: Response format is valid JSON

### Module Dependency Validation

- [ ] [T023] [P1] [VALIDATE] Verify no circular imports:
  - Check all imports are forward references or top-level
  - Verify diagram runtime imports agent/skills without circular dependency

- [ ] [T024] [P1] [VALIDATE] Verify all TODO placeholders present:
  - Check all functions contain TODO comments
  - Check all modules have docstrings explaining purpose
  - Verify no real AI logic (no LLM calls, no diagram generation)

---

## Documentation Tasks

**Purpose**: Verify all documentation files exist and are complete.

- [ ] [T025] [P2] [DOCS] Verify `specs/008-chapter-1-diagram-runtime/contracts/diagram-schema.yaml` exists and is complete (already created in spec phase)
- [ ] [T026] [P2] [DOCS] Verify `specs/008-chapter-1-diagram-runtime/checklists/requirements.md` exists and is complete (already created in spec phase)
- [ ] [T027] [P2] [DOCS] Verify `specs/008-chapter-1-diagram-runtime/research.md` exists and is complete (already created in spec phase)
- [ ] [T028] [P2] [DOCS] Verify `specs/008-chapter-1-diagram-runtime/quickstart.md` exists and is complete (already created in spec phase)
- [ ] [T029] [P2] [DOCS] Verify `specs/008-chapter-1-diagram-runtime/data-model.md` exists and is complete (already created in spec phase)

**Acceptance Test**: All documentation files exist and are complete

---

## Task Summary

**Total Tasks**: 29 tasks
- **Setup**: 4 tasks
- **Runtime**: 2 tasks
- **Agent**: 1 task
- **Schema**: 1 task
- **Skills**: 1 task
- **API Integration**: 1 task
- **RAG Placeholder**: 1 task
- **Validation**: 13 tasks
- **Documentation**: 5 tasks

**Critical Path**: T001-T004 → T005-T006 → T007 → T008 → T009 → T010 → T011 → T012-T024 → T025-T029

**Estimated Time**: 2-3 hours (file creation + function signatures + imports + validation)

---

## Success Criteria Validation

### Spec Success Criteria → Task Mapping

| Success Criteria | Task IDs | Validation Method |
|------------------|----------|-------------------|
| **SC-001**: All scaffold modules exist | T012-T015 | File existence checks |
| **SC-002**: No real AI logic | T024 | Code review |
| **SC-003**: Backend starts successfully | T021 | Backend startup test |
| **SC-004**: API integration complete | T010, T022 | Endpoint routing test |
| **SC-005**: Documentation complete | T025-T029 | File existence |

---

## Dependencies & Risks

### Internal Dependencies
- ✅ Feature 005 (AI Runtime Engine) complete
- ✅ Feature 006 (Diagram Generation Engine) complete

### External Dependencies
- ✅ Python 3.11+, FastAPI 0.109+, Pydantic 2.x (already installed)
- ✅ No new runtime dependencies required (scaffolding only)

### Risks & Mitigations

**Risk 1**: Import resolution failures
- **Mitigation**: Test imports incrementally (T016-T020), fix errors immediately

**Risk 2**: Breaking Feature 005/006 compatibility
- **Mitigation**: Update files carefully (T007, T010), test existing endpoints after update

**Risk 3**: Missing __init__.py files
- **Mitigation**: Create all __init__.py files in Setup phase (T005)

**Risk 4**: Circular import issues
- **Mitigation**: Validate dependencies (T023), use forward references if needed

---

**Task Generation Complete**: 2025-12-05
**Ready for Implementation**: Yes ✅
**Next Command**: `/sp.implement` (or manual task-by-task execution)

