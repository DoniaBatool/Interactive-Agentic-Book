# Tasks: Chapter 2 — Explain-Like-I'm-10 (ELI10) Runtime

**Feature**: 026-ch2-explain-el10-runtime | **Branch**: `026-ch2-explain-el10-runtime` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating Chapter 2 ELI10 explanation runtime infrastructure scaffolding (runtime module, prompt template, routing, skills, API integration). All tasks are scaffolding only—no real AI logic implementation.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category`: SETUP (Initial setup), RUNTIME (Runtime module), PROMPT (Prompt template), ROUTING (Routing integration), API (API integration), SKILLS (Skills module), VALIDATE (Validation), DOCS (Documentation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before creating Chapter 2 ELI10 runtime scaffolding.

- [ ] [T001] [P1] [SETUP] Verify Feature 025 (Chapter 2 Diagram Runtime) exists: Check that `backend/app/ai/diagram/ch2_diagram_runtime.py` exists and is importable (for reference structure)
- [ ] [T002] [P1] [SETUP] Verify Feature 024 (Chapter 2 Backend Runtime Wiring) exists: Check that `backend/app/ai/runtime/engine.py` has Chapter 2 routing structure
- [ ] [T003] [P1] [SETUP] Verify API layer exists: Check that `backend/app/api/ai_blocks.py` exists and has explain-like-10 endpoint
- [ ] [T004] [P1] [SETUP] Verify skills layer exists: Check that `backend/app/ai/skills/prompt_builder_skill.py` and `formatting_skill.py` exist
- [ ] [T005] [P1] [SETUP] Verify backend starts successfully: Run `cd backend && uvicorn app.main:app` to confirm server starts without errors
- [ ] [T006] [P1] [SETUP] Verify explain directory exists: Check that `backend/app/ai/explain/` directory exists (create if needed)

**Success Criteria**:
- All required files and directories exist
- Backend starts without errors
- All imports resolve correctly

**Dependencies**: Feature 025 (Chapter 2 Diagram Runtime) and Feature 024 (Chapter 2 Backend Runtime Wiring) must be complete

---

## PHASE 1 — ELI10 Runtime Module

**User Story**: US1 - Developer Sets Up Chapter 2 ELI10 Runtime Infrastructure

**Test Strategy**: Can be tested by verifying runtime module exists, function signature is correct, and all 5 steps have TODO markers.

### Runtime Module Creation

- [ ] [T007] [P1] [RUNTIME] Create `backend/app/ai/explain/ch2_el10_runtime.py`:
  - Add module docstring: `"""Chapter 2 Explain-Like-I'm-10 (ELI10) Runtime - Orchestrates ELI10 explanation flow for ROS 2 concepts"""`
  - Import statements: `from typing import Dict, Any, Optional`
  - Function definition: `async def run(concept: str, chapter_id: int, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:`
  - Function docstring explaining:
    - Args: concept, chapter_id (should be 2), context (optional)
    - Returns: Dictionary with structured explanation (explanation, examples, analogies)
    - Pipeline steps (all TODO): Validate → Build Prompt → RAG Retrieve → Call LLM → Format
  - Add 5-step pipeline blueprint (all TODO):
    1. `# Step 1: Validate input (TODO)`
       - `# TODO: Check concept is valid ROS 2 concept`
       - `# TODO: Validate chapter_id is 2`
       - `# TODO: Validate context structure if provided`
    2. `# Step 2: Build prompt (placeholder)`
       - `# TODO: Load ch2_el10_prompt.txt template`
       - `# TODO: Replace template variables ({{concept}}, {{chapter_id}}, {{context}})`
       - `# TODO: Call build_el10_prompt_ch2() from prompt_builder_skill`
    3. `# Step 3: RAG retrieve (placeholder)`
       - `# TODO: Retrieve Chapter 2 context chunks for concept`
       - `# TODO: Use RAG pipeline to get relevant ROS 2 content`
    4. `# Step 4: Call LLM (placeholder)`
       - `# TODO: Call LLM provider with prompt and context`
       - `# TODO: Generate explanation using LLM reasoning with ELI10 style`
    5. `# Step 5: Format output (placeholder)`
       - `# TODO: Call format_el10_output_ch2() from formatting_skill`
       - `# TODO: Format explanation, examples, analogies`
  - Placeholder return: `return {"explanation": "", "examples": [], "analogies": []}`
  - Add TODO comment: `# TODO: Implement orchestration logic`
  - Add TODO comment: `# TODO: Add error handling for each step`
  - Add TODO comment: `# TODO: Add logging for ELI10 explanation flow`

- [ ] [T008] [P1] [RUNTIME] Verify ch2_el10_runtime.py is importable: Run `cd backend && python -c "from app.ai.explain.ch2_el10_runtime import run; print('Import successful')"` - should complete without errors

- [ ] [T009] [P2] [RUNTIME] Verify ch2_el10_runtime.py structure matches ch2_diagram_runtime.py (Chapter 2):
  - Compare function signatures
  - Compare return type structure
  - Ensure parity in structure (same 5-step pipeline pattern)

**Acceptance Test**: Runtime file exists, function signature correct, all 5 steps have TODO markers, imports resolve, no real logic implementation

---

## PHASE 2 — Prompt Template

**User Story**: US1 - Developer Sets Up Chapter 2 ELI10 Runtime Infrastructure

**Test Strategy**: Can be tested by verifying prompt template file exists, contains all 3 variables, and has TODO comments.

### Prompt Template Creation

- [ ] [T010] [P1] [PROMPT] Create directory structure if needed: `backend/app/ai/prompts/explain/` (create if doesn't exist)

- [ ] [T011] [P1] [PROMPT] Create `backend/app/ai/prompts/explain/ch2_el10_prompt.txt`:
  - Add header comment: `# TODO: Engineer full ELI10 prompt template for Chapter 2`
  - Add template variables section:
    - `# Template variables:`
    - `# - {{concept}} - ROS 2 concept to explain (e.g., "topics", "nodes", "services", "actions")`
    - `# - {{chapter_id}} - Chapter identifier (should be 2)`
    - `# - {{context}} - RAG context chunks for the concept`
  - Add TODO comments for future ELI10 style tuning:
    - `# TODO: Add system instructions for ELI10 style (age-appropriate, simple language)`
    - `# TODO: Add context placeholders for RAG chunks`
    - `# TODO: Add ROS 2-specific analogies (post office, restaurant, phone calls, package delivery)`
    - `# TODO: Add structured output format instructions`
    - `# TODO: Add ELI10 style tuning guidelines`
    - `# TODO: Include ROS 2 examples (TurtleBot 3, navigation stack, robot arm control)`
  - Add placeholder template structure (can be minimal, just showing variable usage)

- [ ] [T012] [P1] [PROMPT] Verify ch2_el10_prompt.txt is readable: Check that file exists and can be read by Python `open()` function

**Acceptance Test**: Prompt template file exists, all 3 variables are present, TODO comments are present, file is readable

---

## PHASE 3 — Runtime Engine Routing

**User Story**: US2 - System Routes Chapter 2 ELI10 Requests

**Test Strategy**: Can be tested by verifying runtime engine has Chapter 2 ELI10 routing comments and TODO markers.

### Runtime Engine Updates

- [ ] [T013] [P1] [ROUTING] Update `backend/app/ai/runtime/engine.py` with Chapter 2 ELI10 routing:
  - Locate `run_ai_block()` function
  - Add routing case (comments only, before existing ELI10 routing if present):
    ```python
    # TODO: Chapter 2 ELI10 routing
    # if block_type == "explain-like-i-am-10" AND chapterId == 2:
    #     from app.ai.explain.ch2_el10_runtime import run as ch2_el10_run
    #     result = await ch2_el10_run(
    #         concept=request_data.get("concept", ""),
    #         chapter_id=2,
    #         context=request_data.get("context")
    #     )
    #     return result
    ```
  - Ensure routing condition checks both `block_type == "explain-like-i-am-10"` AND `chapterId == 2`
  - Add comment explaining: `# Routes Chapter 2 ELI10 requests to ch2_el10_runtime (placeholder routing)`

- [ ] [T014] [P1] [ROUTING] Verify engine.py still imports correctly: Run `cd backend && python -c "from app.ai.runtime.engine import run_ai_block; print('Import successful')"` - should complete without errors

- [ ] [T015] [P2] [ROUTING] Verify routing comments are clear: Check that routing logic is well-documented with TODO comments

**Acceptance Test**: Runtime engine has Chapter 2 ELI10 routing (comments only), routing condition checks both block_type and chapterId, file still imports correctly, TODO comments are present

---

## PHASE 4 — API Layer Update

**User Story**: US2 - System Routes Chapter 2 ELI10 Requests

**Test Strategy**: Can be tested by verifying API endpoint has Chapter 2 routing comments and supports chapterId=2.

### API Layer Updates

- [ ] [T016] [P1] [API] Update `backend/app/api/ai_blocks.py` explain-like-10 endpoint with Chapter 2 routing:
  - Locate `explain_like_10()` function (POST /api/ai/explain-like-10 endpoint)
  - Add routing comment (before existing routing logic):
    ```python
    # TODO: Chapter 2 ELI10 routing
    # if request.chapterId == 2:
    #     from app.ai.explain.ch2_el10_runtime import run as ch2_el10_run
    #     result = await ch2_el10_run(
    #         concept=request.concept,
    #         chapter_id=2,
    #         context=None
    #     )
    #     return result
    ```
  - Add comments documenting CH2 workflow: `# Route Chapter 2 ELI10 requests to ch2_el10_runtime (placeholder routing)`
  - Ensure routing supports chapterId=2 (may already be generic)

- [ ] [T017] [P1] [API] Verify ai_blocks.py still imports correctly: Run `cd backend && python -c "from app.api.ai_blocks import explain_like_10; print('Import successful')"` - should complete without errors

- [ ] [T018] [P2] [API] Verify endpoint accepts chapterId=2: Check that ExplainLike10Request model supports chapterId parameter (should already exist)

**Acceptance Test**: API endpoint has Chapter 2 routing comments, endpoint accepts chapterId=2, file still imports correctly, no breaking changes to existing functionality

---

## PHASE 5 — Contracts

**User Story**: US1 - Developer Sets Up Chapter 2 ELI10 Runtime Infrastructure

**Test Strategy**: Can be tested by verifying contract file exists and documents expected placeholders.

### Contract Verification

- [ ] [T019] [P1] [DOCS] Verify `specs/026-ch2-explain-el10-runtime/contracts/el10-contract.yaml` exists:
  - Check that file was created during spec phase
  - Verify file contains:
    - Chapter 2 ELI10 runtime flow contract
    - Prompt template contract
    - Routing contracts
    - Skills contracts
    - Validation contracts

- [ ] [T020] [P2] [DOCS] Verify contract file documents expected placeholders:
  - Check that contract documents placeholder-only implementation
  - Verify no structure for real outputs (placeholder only)

**Acceptance Test**: Contract file exists, documents expected placeholders, no structure for real outputs

---

## PHASE 6 — Skills Extension

**User Story**: US1 - Developer Sets Up Chapter 2 ELI10 Runtime Infrastructure

**Test Strategy**: Can be tested by verifying skills functions exist, are importable, and have TODO comments.

### Prompt Builder Skill

- [ ] [T021] [P1] [SKILLS] Update `backend/app/ai/skills/prompt_builder_skill.py` with build_el10_prompt_ch2() function:
  - Add function definition: `def build_el10_prompt_ch2(concept: str, chapter_id: int, context: Optional[Dict[str, Any]] = None) -> str:`
  - Add function docstring:
    ```python
    """
    Build ELI10 prompt for Chapter 2.
    
    Args:
        concept: ROS 2 concept to explain
        chapter_id: Chapter identifier (should be 2)
        context: Optional RAG context chunks
    
    Returns:
        Constructed prompt string
    
    TODO: Implement prompt building for Chapter 2 ELI10 explanations
    TODO: Load ch2_el10_prompt.txt template
    TODO: Replace template variables ({{concept}}, {{chapter_id}}, {{context}})
    TODO: Add ROS 2-specific context
    TODO: Return constructed prompt string
    """
    ```
  - Add placeholder return: `return ""  # Placeholder return - no real prompt building`
  - Add TODO comment: `# TODO: Implement prompt building for Chapter 2 ELI10 explanations`

- [ ] [T022] [P1] [SKILLS] Verify prompt_builder_skill.py still imports correctly: Run `cd backend && python -c "from app.ai.skills.prompt_builder_skill import build_el10_prompt_ch2; print('Import successful')"` - should complete without errors

### Formatting Skill

- [ ] [T023] [P1] [SKILLS] Update `backend/app/ai/skills/formatting_skill.py` with format_el10_output_ch2() function:
  - Add function definition: `def format_el10_output_ch2(raw_response: Dict[str, Any]) -> Dict[str, Any]:`
  - Add function docstring:
    ```python
    """
    Format ELI10 output for Chapter 2.
    
    Args:
        raw_response: Raw LLM response with explanation data
    
    Returns:
        Formatted explanation structure:
        {
            "explanation": str,
            "examples": List[str],
            "analogies": List[str]
        }
    
    TODO: Implement formatting for Chapter 2 ELI10 output
    TODO: Parse raw LLM response
    TODO: Extract explanation, examples, analogies
    TODO: Format ROS 2-specific metadata
    TODO: Return formatted explanation structure
    """
    ```
  - Add placeholder return: `return {"explanation": "", "examples": [], "analogies": []}  # Placeholder return - no real formatting`
  - Add TODO comment: `# TODO: Implement formatting for Chapter 2 ELI10 output`

- [ ] [T024] [P1] [SKILLS] Verify formatting_skill.py still imports correctly: Run `cd backend && python -c "from app.ai.skills.formatting_skill import format_el10_output_ch2; print('Import successful')"` - should complete without errors

**Acceptance Test**: Both skills functions exist, are importable, have TODO comments, no real logic implementation

---

## PHASE 7 — Validation

**User Story**: US1 - Developer Sets Up Chapter 2 ELI10 Runtime Infrastructure

**Test Strategy**: Can be tested by verifying backend starts, all imports resolve, and no real logic exists.

### Backend Startup Validation

- [ ] [T025] [P1] [VALIDATE] Test backend startup: Run `cd backend && uvicorn app.main:app` - should start without errors
  - Check for import errors
  - Check for syntax errors
  - Check for runtime exceptions
  - Backend should start successfully

- [ ] [T026] [P1] [VALIDATE] Test all new module imports:
  - Test ch2_el10_runtime: `python -c "from app.ai.explain.ch2_el10_runtime import run; print('ch2_el10_runtime: OK')"`
  - Test prompt template: `python -c "with open('backend/app/ai/prompts/explain/ch2_el10_prompt.txt') as f: print('ch2_el10_prompt.txt: OK')"`
  - Test skills functions: `python -c "from app.ai.skills.prompt_builder_skill import build_el10_prompt_ch2; from app.ai.skills.formatting_skill import format_el10_output_ch2; print('Skills: OK')"`
  - All imports should succeed

### Logic Verification

- [ ] [T027] [P1] [VALIDATE] Verify no real AI logic implemented:
  - Check ch2_el10_runtime.py: All steps should have TODO markers only
  - Check prompt_builder_skill.py: build_el10_prompt_ch2() should return placeholder
  - Check formatting_skill.py: format_el10_output_ch2() should return placeholder
  - Check engine.py: Chapter 2 routing should be comments only
  - Check ai_blocks.py: Chapter 2 routing should be comments only

- [ ] [T028] [P1] [VALIDATE] Verify Chapter 1 ELI10 functionality still works:
  - Check that existing Chapter 1 ELI10 runtime is not broken
  - Verify no breaking changes to existing functionality

### File Existence Verification

- [ ] [T029] [P1] [VALIDATE] Verify all required files exist:
  - [ ] `backend/app/ai/explain/ch2_el10_runtime.py` exists
  - [ ] `backend/app/ai/prompts/explain/ch2_el10_prompt.txt` exists
  - [ ] `specs/026-ch2-explain-el10-runtime/contracts/el10-contract.yaml` exists
  - [ ] Skills functions exist in prompt_builder_skill.py and formatting_skill.py

**Acceptance Test**: Backend starts without errors, all imports resolve, no real AI logic implemented, all required files exist, Chapter 1 functionality still works

---

## Summary

**Total Tasks**: 29 tasks across 7 phases

**Phase Breakdown**:
- Phase 0 (Setup): 6 tasks
- Phase 1 (Runtime Module): 3 tasks
- Phase 2 (Prompt Template): 3 tasks
- Phase 3 (Runtime Engine Routing): 3 tasks
- Phase 4 (API Layer): 3 tasks
- Phase 5 (Contracts): 2 tasks
- Phase 6 (Skills Extension): 4 tasks
- Phase 7 (Validation): 5 tasks

**Priority Breakdown**:
- P1 (Critical): 27 tasks
- P2 (Important): 2 tasks
- P3 (Nice-to-have): 0 tasks

**Estimated Time**: 30-45 minutes (scaffolding only, no real AI logic)

**Dependencies**: Feature 025 (Chapter 2 Diagram Runtime), Feature 024 (Chapter 2 Backend Runtime Wiring)

**Out of Scope**: Real AI logic, RAG implementation, LLM calls, explanation generation

---

## Completion Checklist

Before marking feature complete, verify:

- [ ] All 29 tasks completed
- [ ] Backend starts without errors
- [ ] All imports resolve correctly
- [ ] All files exist at specified paths
- [ ] All TODO comments are present
- [ ] No real AI logic implemented (only placeholders)
- [ ] Chapter 1 ELI10 functionality still works
- [ ] Contract file documents expected placeholders
- [ ] All validation tests pass

---

## Next Steps

After completing all tasks:

1. **Implementation Review**: Review all created files for consistency
2. **Documentation**: Update PHR with implementation details
3. **Testing**: Run final validation tests
4. **Commit**: Commit changes with appropriate message

