# Tasks: Chapter 3 — Diagram Generator Runtime Layer

**Feature**: 031-ch3-diagram-runtime | **Branch**: `031-ch3-diagram-runtime` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating Chapter 3 diagram generator runtime infrastructure scaffolding (runtime module, prompt template, routing, skills, API integration, RAG stub). All tasks are scaffolding only—no real AI logic implementation.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category`: SETUP (Initial setup), RUNTIME (Runtime module), PROMPT (Prompt template), ROUTING (Routing integration), API (API integration), SKILLS (Skills module), RAG (RAG integration), VALIDATE (Validation), DOCS (Documentation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before creating Chapter 3 diagram runtime scaffolding.

- [ ] [T001] [P1] [SETUP] Verify Feature 025 (Chapter 2 Diagram Runtime) exists: Check that `backend/app/ai/diagram/ch2_diagram_runtime.py` exists and is importable (for reference structure)
- [ ] [T002] [P1] [SETUP] Verify Feature 030 (Chapter 3 AI Runtime Engine Integration) exists: Check that `backend/app/ai/subagents/ch3_diagram_agent.py` exists (subagent already created)
- [ ] [T003] [P1] [SETUP] Verify API layer exists: Check that `backend/app/api/ai_blocks.py` exists and has `/ai/ch3/diagram` endpoint (already exists from Feature 030)
- [ ] [T004] [P1] [SETUP] Verify skills layer exists: Check that `backend/app/ai/skills/prompt_builder_skill.py` and `formatting_skill.py` exist
- [ ] [T005] [P1] [SETUP] Verify RAG pipeline exists: Check that `backend/app/ai/rag/ch3_pipeline.py` exists (from Feature 029)
- [ ] [T006] [P1] [SETUP] Verify backend starts successfully: Run `cd backend && uvicorn app.main:app` to confirm server starts without errors
- [ ] [T007] [P1] [SETUP] Verify diagram directory exists: Check that `backend/app/ai/diagram/` directory exists (create if needed)

**Success Criteria**:
- All required files and directories exist
- Backend starts without errors
- All imports resolve correctly
- ch3_diagram_agent subagent exists from Feature 030
- `/ai/ch3/diagram` endpoint exists from Feature 030

**Dependencies**: Feature 025 (Chapter 2 Diagram Runtime) and Feature 030 (Chapter 3 AI Runtime Engine Integration) must be complete

---

## PHASE 1 — Diagram Runtime Module

**User Story**: US1 - Developer Sets Up Chapter 3 Diagram Runtime Infrastructure

**Test Strategy**: Can be tested by verifying runtime module exists, function signature is correct, and all 5 steps have TODO markers.

### Runtime Module Creation

- [ ] [T008] [P1] [RUNTIME] Create `backend/app/ai/diagram/ch3_diagram_runtime.py`:
  - Add module docstring: `"""Chapter 3 Diagram Generator Runtime - Orchestrates diagram generation flow for Physical AI diagrams"""`
  - Import statements: `from typing import List, Dict, Any`
  - Function definition: `async def run(diagram_type: str, chapter_id: int, concepts: List[str]) -> Dict[str, Any]:`
  - Function docstring explaining:
    - Args: diagram_type, chapter_id (should be 3), concepts
    - Returns: Dictionary with structured diagram (nodes, edges, svg, metadata)
    - Pipeline steps (all TODO): Validate → Build Prompt → Call RAG → Call LLM → Format
  - Add 5-step pipeline blueprint (all TODO):
    1. `# Step 1: Validate diagram request (TODO)`
       - `# TODO: Check diagram_type is supported for Chapter 3`
       - `# TODO: Validate chapter_id is 3`
       - `# TODO: Validate concepts list`
    2. `# Step 2: Build prompt (placeholder)`
       - `# TODO: Load ch3_diagram_prompt.txt template`
       - `# TODO: Replace template variables ({{diagram_type}}, {{chapter_id}}, {{concepts}})`
       - `# TODO: Call build_diagram_prompt_ch3() from prompt_builder_skill`
    3. `# Step 3: Call RAG (placeholder)`
       - `# TODO: Retrieve Chapter 3 context chunks for diagram`
       - `# TODO: Use RAG pipeline to get relevant Physical AI content`
       - `# TODO: Call ch3_pipeline for diagram context retrieval`
    4. `# Step 4: Call provider LLM (placeholder)`
       - `# TODO: Call LLM provider with prompt and context`
       - `# TODO: Call ch3_diagram_agent() from subagents (already exists from Feature 030)`
       - `# TODO: Generate diagram structure using LLM reasoning`
    5. `# Step 5: Format response (placeholder)`
       - `# TODO: Call format_diagram_output_ch3() from formatting_skill`
       - `# TODO: Format nodes, edges, SVG structure`
  - Placeholder return: `return {"nodes": [], "edges": [], "svg": "", "metadata": {}}`
  - Add TODO comment: `# TODO: Implement orchestration logic`
  - Add TODO comment: `# TODO: Add error handling for each step`
  - Add TODO comment: `# TODO: Add logging for diagram generation flow`
  - Add TODO comment: `# TODO: Integrate with ch3_diagram_agent (from Feature 030)`

- [ ] [T009] [P1] [RUNTIME] Verify ch3_diagram_runtime.py is importable: Run `cd backend && python -c "from app.ai.diagram.ch3_diagram_runtime import run; print('Import successful')"` - should complete without errors

- [ ] [T010] [P2] [RUNTIME] Verify ch3_diagram_runtime.py structure matches ch2_diagram_runtime.py (Chapter 2):
  - Compare function signatures
  - Compare return type structure
  - Ensure parity in structure (same 5-step pipeline pattern)

**Acceptance Test**: Runtime file exists, function signature correct, all 5 steps have TODO markers, imports resolve, no real logic implementation, integration with ch3_diagram_agent documented

---

## PHASE 2 — Prompt Template

**User Story**: US1 - Developer Sets Up Chapter 3 Diagram Runtime Infrastructure

**Test Strategy**: Can be tested by verifying prompt template file exists, contains all 3 variables, and has TODO comments.

### Prompt Template Creation

- [ ] [T011] [P1] [PROMPT] Create directory structure if needed: `backend/app/ai/prompts/diagram/` (create if doesn't exist)

- [ ] [T012] [P1] [PROMPT] Create `backend/app/ai/prompts/diagram/ch3_diagram_prompt.txt`:
  - Add header comment: `# TODO: Engineer full prompt template for Chapter 3 diagrams`
  - Add template variables section:
    - `# Template variables:`
    - `# - {{diagram_type}} - Type of diagram (e.g., "perception-overview", "sensor-types", "cv-depth-flow", "feature-extraction-pipeline")`
    - `# - {{chapter_id}} - Chapter identifier (should be 3)`
    - `# - {{concepts}} - Physical AI concepts to include (perception, sensors, computer-vision, signal-processing, feature-extraction)`
  - Add TODO comments for future engineering:
    - `# TODO: Add system instructions for Physical AI diagram generation`
    - `# TODO: Add context placeholders for RAG chunks`
    - `# TODO: Add structured output format instructions`
    - `# TODO: Add Physical AI-specific diagram guidelines`
    - `# TODO: Include Physical AI analogies and examples`
    - `# TODO: Add diagram type-specific instructions`
  - Add placeholder template structure (can be minimal, just showing variable usage)

- [ ] [T013] [P1] [PROMPT] Verify ch3_diagram_prompt.txt is readable: Check that file exists and can be read by Python `open()` function

**Acceptance Test**: Prompt template file exists, all 3 variables are present, TODO comments are present, file is readable

---

## PHASE 3 — Runtime Engine Routing

**User Story**: US2 - System Routes Chapter 3 Diagram Requests

**Test Strategy**: Can be tested by verifying runtime engine has Chapter 3 diagram routing comments and TODO markers.

### Runtime Engine Updates

- [ ] [T014] [P1] [ROUTING] Update `backend/app/ai/runtime/engine.py` with Chapter 3 diagram routing:
  - Locate `run_ai_block()` function
  - Add routing case (comments only, in chapter_id == 3 block):
    ```python
    # TODO: Chapter 3 diagram routing
    # if block_type == "diagram" AND chapterId == 3:
    #     from app.ai.diagram.ch3_diagram_runtime import run as ch3_diagram_run
    #     result = await ch3_diagram_run(
    #         diagram_type=request_data.get("diagramType", ""),
    #         chapter_id=3,
    #         concepts=request_data.get("concepts", [])
    #     )
    #     return result
    ```
  - Ensure routing condition checks both `block_type == "diagram"` AND `chapterId == 3`
  - Add comment explaining: `# Routes Chapter 3 diagram requests to ch3_diagram_runtime (placeholder routing)`
  - Add TODO sections for:
    - `# TODO: diagram prompt assembly`
    - `# TODO: diagram metadata extraction`
    - `# TODO: RAG optional context injection`

- [ ] [T015] [P1] [ROUTING] Verify engine.py still imports correctly: Run `cd backend && python -c "from app.ai.runtime.engine import run_ai_block; print('Import successful')"` - should complete without errors

- [ ] [T016] [P2] [ROUTING] Verify routing comments are clear: Check that routing logic is well-documented with TODO comments

**Acceptance Test**: Runtime engine has Chapter 3 diagram routing (comments only), routing condition checks both block_type and chapterId, file still imports correctly, TODO comments are present

---

## PHASE 4 — API Layer Update

**User Story**: US2 - System Routes Chapter 3 Diagram Requests

**Test Strategy**: Can be tested by verifying API endpoint routes to Chapter 3 diagram runtime when chapterId=3.

### API Layer Updates

- [ ] [T017] [P1] [API] Update `backend/app/api/ai_blocks.py` `/ai/ch3/diagram` endpoint (already exists from Feature 030):
  - Locate `ch3_diagram()` function (POST /ai/ch3/diagram endpoint)
  - Update routing to call: `run_ai_block(block_type="diagram", chapter=3, payload=request)`
  - Add TODO documentation tag: `# TODO: Route Chapter 3 diagram requests to ch3_diagram_runtime`
  - Ensure routing supports chapterId=3
  - Add comment: `# Routes to ch3_diagram_runtime via runtime engine`

- [ ] [T018] [P1] [API] Verify ai_blocks.py still imports correctly: Run `cd backend && python -c "from app.api.ai_blocks import ch3_diagram; print('Import successful')"` - should complete without errors

- [ ] [T019] [P2] [API] Verify endpoint accepts chapterId=3: Check that DiagramRequest model supports chapterId parameter (should already exist)

**Acceptance Test**: API endpoint routes to Chapter 3 diagram runtime, endpoint accepts chapterId=3, file still imports correctly, no breaking changes to existing functionality

---

## PHASE 5 — Contracts

**User Story**: US1 - Developer Sets Up Chapter 3 Diagram Runtime Infrastructure

**Test Strategy**: Can be tested by verifying contract file exists and documents expected placeholders.

### Contract Verification

- [ ] [T020] [P1] [DOCS] Verify `specs/031-ch3-diagram-runtime/contracts/diagram-api.yaml` exists:
  - Check that file was created during spec phase
  - Verify file contains:
    - Chapter 3 diagram types documentation
    - Runtime flow contract
    - Prompt template contract
    - Routing contracts
    - Skills contracts
    - RAG integration contract
    - Subagent responsibilities (ch3_diagram_agent from Feature 030)
    - Validation contracts

- [ ] [T021] [P2] [DOCS] Verify contract file documents expected placeholders:
  - Check that contract documents placeholder-only implementation
  - Verify no schemas for actual diagram formats (placeholder only)
  - Verify routing flow is documented
  - Verify subagent responsibilities are documented

**Acceptance Test**: Contract file exists, documents expected placeholders, documents routing flow, documents subagent responsibilities, no schemas for actual diagram formats

---

## PHASE 6 — Skills Extension

**User Story**: US1 - Developer Sets Up Chapter 3 Diagram Runtime Infrastructure

**Test Strategy**: Can be tested by verifying skills functions exist, are importable, and have TODO comments.

### Prompt Builder Skill

- [ ] [T022] [P1] [SKILLS] Update `backend/app/ai/skills/prompt_builder_skill.py` with build_diagram_prompt_ch3() function:
  - Add function definition: `def build_diagram_prompt_ch3(diagram_type: str, chapter_id: int, concepts: List[str]) -> str:`
  - Add function docstring:
    ```python
    """
    Build diagram prompt for Chapter 3.
    
    Args:
        diagram_type: Type of diagram to generate
        chapter_id: Chapter identifier (should be 3)
        concepts: List of Physical AI concepts to include
    
    Returns:
        Constructed prompt string
    
    TODO: Implement prompt building for Chapter 3 diagrams
    TODO: Load ch3_diagram_prompt.txt template
    TODO: Replace template variables ({{diagram_type}}, {{chapter_id}}, {{concepts}})
    TODO: Add Physical AI-specific context
    TODO: Return constructed prompt string
    """
    ```
  - Add placeholder return: `return ""  # Placeholder return - no real prompt building`
  - Add TODO comment: `# TODO: Implement prompt building for Chapter 3 diagrams`

- [ ] [T023] [P1] [SKILLS] Verify prompt_builder_skill.py still imports correctly: Run `cd backend && python -c "from app.ai.skills.prompt_builder_skill import build_diagram_prompt_ch3; print('Import successful')"` - should complete without errors

### Formatting Skill

- [ ] [T024] [P1] [SKILLS] Update `backend/app/ai/skills/formatting_skill.py` with format_diagram_output_ch3() function:
  - Add function definition: `def format_diagram_output_ch3(raw_response: Dict[str, Any]) -> Dict[str, Any]:`
  - Add function docstring:
    ```python
    """
    Format diagram output for Chapter 3.
    
    Args:
        raw_response: Raw LLM response with diagram data
    
    Returns:
        Formatted diagram structure:
        {
            "nodes": List[Dict],
            "edges": List[Dict],
            "svg": str,
            "metadata": Dict[str, Any]
        }
    
    TODO: Implement formatting for Chapter 3 diagram output
    TODO: Parse raw LLM response
    TODO: Extract nodes, edges, SVG
    TODO: Format Physical AI-specific metadata
    TODO: Return formatted diagram structure
    """
    ```
  - Add placeholder return: `return {"nodes": [], "edges": [], "svg": "", "metadata": {}}  # Placeholder return - no real formatting`
  - Add TODO comment: `# TODO: Implement formatting for Chapter 3 diagram output`

- [ ] [T025] [P1] [SKILLS] Verify formatting_skill.py still imports correctly: Run `cd backend && python -c "from app.ai.skills.formatting_skill import format_diagram_output_ch3; print('Import successful')"` - should complete without errors

**Acceptance Test**: Both skills functions exist, are importable, have TODO comments, no real logic implementation

---

## PHASE 7 — RAG Integration Stub

**User Story**: US1 - Developer Sets Up Chapter 3 Diagram Runtime Infrastructure

**Test Strategy**: Can be tested by verifying RAG pipeline has diagram context retrieval stub with TODO comments.

### RAG Pipeline Updates

- [ ] [T026] [P1] [RAG] Update `backend/app/ai/rag/ch3_pipeline.py` with diagram context retrieval stub:
  - Add TODO section for diagram context retrieval:
    ```python
    # TODO: Retrieve diagram-related context
    # TODO: Filter chunks by diagram_type
    # TODO: Include Physical AI concepts in context
    # TODO: Return relevant chunks for diagram generation
    ```
  - Add comment: `# Diagram context retrieval stub (for ch3_diagram_runtime)`
  - Placeholder stub only, no real RAG operations

- [ ] [T027] [P1] [RAG] Verify ch3_pipeline.py still imports correctly: Run `cd backend && python -c "from app.ai.rag.ch3_pipeline import run_ch3_rag_pipeline; print('Import successful')"` - should complete without errors

- [ ] [T028] [P2] [RAG] Verify RAG stub is well-documented: Check that stub has clear TODO comments explaining future implementation

**Acceptance Test**: RAG stub is present in ch3_pipeline.py, stub has TODO comments, no real RAG operations implemented, file still imports correctly

---

## PHASE 8 — Validation

**User Story**: US1 - Developer Sets Up Chapter 3 Diagram Runtime Infrastructure

**Test Strategy**: Can be tested by verifying backend starts, all imports resolve, and no real logic exists.

### Backend Startup Validation

- [ ] [T029] [P1] [VALIDATE] Test backend startup: Run `cd backend && uvicorn app.main:app` - should start without errors
  - Check for import errors
  - Check for syntax errors
  - Check for runtime exceptions
  - Backend should start successfully

- [ ] [T030] [P1] [VALIDATE] Test all new module imports:
  - Test ch3_diagram_runtime: `python -c "from app.ai.diagram.ch3_diagram_runtime import run; print('ch3_diagram_runtime: OK')"`
  - Test prompt template: `python -c "with open('backend/app/ai/prompts/diagram/ch3_diagram_prompt.txt') as f: print('ch3_diagram_prompt.txt: OK')"`
  - Test skills functions: `python -c "from app.ai.skills.prompt_builder_skill import build_diagram_prompt_ch3; from app.ai.skills.formatting_skill import format_diagram_output_ch3; print('Skills: OK')"`
  - All imports should succeed

### Logic Verification

- [ ] [T031] [P1] [VALIDATE] Verify no real AI logic implemented:
  - Check ch3_diagram_runtime.py: All steps should have TODO markers only
  - Check prompt_builder_skill.py: build_diagram_prompt_ch3() should return placeholder
  - Check formatting_skill.py: format_diagram_output_ch3() should return placeholder
  - Check engine.py: Chapter 3 routing should be comments only
  - Check ai_blocks.py: Chapter 3 routing should be comments only
  - Check ch3_pipeline.py: RAG stub should be comments only

- [ ] [T032] [P1] [VALIDATE] Verify Chapter 1 and Chapter 2 diagram functionality still works:
  - Check that existing Chapter 1 diagram runtime is not broken
  - Check that existing Chapter 2 diagram runtime is not broken
  - Verify no breaking changes to existing functionality

### File Existence Verification

- [ ] [T033] [P1] [VALIDATE] Verify all required files exist:
  - [ ] `backend/app/ai/diagram/ch3_diagram_runtime.py` exists
  - [ ] `backend/app/ai/prompts/diagram/ch3_diagram_prompt.txt` exists
  - [ ] `specs/031-ch3-diagram-runtime/contracts/diagram-api.yaml` exists
  - [ ] Skills functions exist in prompt_builder_skill.py and formatting_skill.py
  - [ ] RAG stub exists in ch3_pipeline.py

**Acceptance Test**: Backend starts without errors, all imports resolve, no real AI logic implemented, all required files exist, Chapter 1 and Chapter 2 functionality still works

---

## Summary

**Total Tasks**: 33 tasks across 8 phases

**Phase Breakdown**:
- Phase 0 (Setup): 7 tasks
- Phase 1 (Runtime Module): 3 tasks
- Phase 2 (Prompt Template): 3 tasks
- Phase 3 (Runtime Engine Routing): 3 tasks
- Phase 4 (API Layer): 3 tasks
- Phase 5 (Contracts): 2 tasks
- Phase 6 (Skills Extension): 4 tasks
- Phase 7 (RAG Integration Stub): 3 tasks
- Phase 8 (Validation): 5 tasks

**Priority Breakdown**:
- P1 (Critical): 31 tasks
- P2 (Important): 2 tasks
- P3 (Nice-to-have): 0 tasks

**Estimated Time**: 30-45 minutes (scaffolding only, no real AI logic)

**Dependencies**: Feature 025 (Chapter 2 Diagram Runtime), Feature 030 (Chapter 3 AI Runtime Engine Integration)

**Out of Scope**: Real AI logic, RAG implementation, LLM calls, diagram generation

---

## Completion Checklist

Before marking feature complete, verify:

- [ ] All 33 tasks completed
- [ ] Backend starts without errors
- [ ] All imports resolve correctly
- [ ] All files exist at specified paths
- [ ] All TODO comments are present
- [ ] No real AI logic implemented (only placeholders)
- [ ] Chapter 1 and Chapter 2 diagram functionality still works
- [ ] Contract file documents expected placeholders
- [ ] RAG stub is present in ch3_pipeline.py
- [ ] Integration with ch3_diagram_agent is documented
- [ ] All validation tests pass

---

## Next Steps

After completing all tasks:

1. **Implementation Review**: Review all created files for consistency
2. **Documentation**: Update PHR with implementation details
3. **Testing**: Run final validation tests
4. **Commit**: Commit changes with appropriate message

