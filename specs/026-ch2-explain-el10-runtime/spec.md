# Feature Specification: Chapter 2 — Explain-Like-I'm-10 (ELI10) Runtime

**Feature Branch**: `026-ch2-explain-el10-runtime`
**Created**: 2025-01-27
**Status**: Draft
**Type**: backend-ai-pipeline
**Input**: User description: "Build the full scaffolding for the Explain-Like-I'm-10 (ELI10) AI runtime specifically for Chapter 2. This includes runtime modules, routing, prompt templates, skill extensions, and contracts. No AI logic must be implemented."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Sets Up Chapter 2 ELI10 Runtime Infrastructure (Priority: P1)

As a backend developer, I need the Chapter 2 ELI10 runtime scaffolding in place with all runtime modules, prompt templates, routing, and integration points defined, so I can implement real AI explanation logic for Chapter 2 in future features without restructuring the codebase.

**Why this priority**: This establishes the complete architectural foundation for Chapter 2 ELI10 explanation runtime. Without proper scaffolding, future AI explanation implementation for Chapter 2 will require refactoring and restructuring, causing delays and technical debt.

**Independent Test**: Can be fully tested by verifying all required files exist at specified paths, all imports resolve without errors, backend starts successfully, and all modules contain TODO placeholders for future implementation.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/ai/explain/ch2_el10_runtime.py`, **Then** I see blueprint for ELI10 explanation flow with 5 steps (validate input, build prompt, RAG retrieve, call LLM, format output) all containing TODO markers only
2. **Given** the feature is implemented, **When** I check `backend/app/ai/prompts/explain/ch2_el10_prompt.txt`, **Then** I see placeholder template with variables `{{concept}}`, `{{chapter_id}}`, `{{context}}` and TODO comments for future ELI10 style tuning
3. **Given** the feature is implemented, **When** I check `backend/app/ai/runtime/engine.py`, **Then** I see case for `if block_type == "explain-like-i-am-10" AND chapterId == 2` that routes to `ch2_el10_runtime.run()` with comments only (no logic)
4. **Given** the feature is implemented, **When** I check `backend/app/api/ai_blocks.py`, **Then** I see ELI10 endpoint supports chapterId=2 with TODO documentation tags
5. **Given** the feature is implemented, **When** I check `backend/app/ai/skills/prompt_builder_skill.py`, **Then** I see placeholder function `build_el10_prompt_ch2()` with TODO comments
6. **Given** the feature is implemented, **When** I check `backend/app/ai/skills/formatting_skill.py`, **Then** I see placeholder function `format_el10_output_ch2()` with TODO comments
7. **Given** the feature is implemented, **When** I check `specs/026-ch2-explain-el10-runtime/contracts/el10-contract.yaml`, **Then** I see expected placeholders for CH2 ELI10 with no structure for real outputs
8. **Given** the feature is implemented, **When** I start the backend server, **Then** it starts without import errors or runtime exceptions

---

### User Story 2 - System Routes Chapter 2 ELI10 Requests (Priority: P1)

As a system integrator, I need Chapter 2 ELI10 requests to route correctly through the API layer to the ELI10 runtime, so the routing infrastructure is ready for future AI explanation implementation.

**Why this priority**: This enables Chapter 2 ELI10 routing infrastructure. Without proper routing, Chapter 2 explanation generation cannot function, and future AI implementation will be blocked.

**Independent Test**: Can be fully tested by verifying ELI10 endpoint can accept chapterId=2, runtime engine routes Chapter 2 ELI10 requests correctly, and all routing paths contain TODO placeholders for Chapter 2 ELI10 operations.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I send a POST request to `/api/ai/explain-like-10` with `chapterId=2`, **Then** the request routes to Chapter 2 ELI10 runtime with routing comments
2. **Given** the feature is implemented, **When** I check the runtime engine routing logic, **Then** I see `if block_type == "explain-like-i-am-10" AND chapterId == 2` case that routes to `ch2_el10_runtime.run()` (comments only)
3. **Given** the feature is implemented, **When** I check the ELI10 runtime module, **Then** I see all 5 steps (validate input, build prompt, RAG retrieve, call LLM, format output) with TODO markers only

---

### Edge Cases

- What happens when Chapter 2 ELI10 runtime is called but ch2_el10_runtime.py doesn't exist?
  - Backend should handle gracefully, returning placeholder response or error message indicating runtime not yet implemented
- What happens when runtime engine receives ELI10 request with chapterId=2 but Chapter 2 ELI10 routing is not implemented?
  - Runtime engine should have placeholder routing with TODO comments indicating implementation needed
- What happens when prompt template file is missing?
  - ELI10 runtime should handle gracefully, using placeholder prompt or returning error message
- What happens when skills functions are called but contain only TODO placeholders?
  - Skills functions should be callable without errors, returning placeholder responses
- What happens when backend starts but new modules have import errors?
  - Backend should not start, and import errors should be fixed before considering feature complete

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Chapter 2 ELI10 Runtime Module

- **FR-001.1**: System MUST create `backend/app/ai/explain/ch2_el10_runtime.py`:
  - Blueprint for ELI10 explanation flow
  - Function signature: `async def run(concept: str, chapter_id: int, context: Dict[str, Any] = None) -> Dict[str, Any]:`
  - Steps (all TODO markers only):
    1. Validate input
    2. Build prompt (placeholder)
    3. RAG retrieve (placeholder)
    4. Call LLM (placeholder)
    5. Format output (placeholder)
  - All steps contain TODO markers only
  - Placeholder return structure

#### FR-002: ELI10 Prompt Template

- **FR-002.1**: System MUST create `backend/app/ai/prompts/explain/ch2_el10_prompt.txt`:
  - Include placeholder template with variables:
    - `{{concept}}`
    - `{{chapter_id}}`
    - `{{context}}`
  - Add TODO comment for future ELI10 style tuning
  - Template structure for Chapter 2 ROS 2 explanations

#### FR-003: Runtime Engine Routing

- **FR-003.1**: System MUST update `backend/app/ai/runtime/engine.py`:
  - Add case: `if block_type == "explain-like-i-am-10" AND chapterId == 2`
  - Route to `ch2_el10_runtime.run()`
  - Comments only, no logic
  - Placeholder routing with TODO comments

#### FR-004: API Layer Integration

- **FR-004.1**: System MUST update `backend/app/api/ai_blocks.py`:
  - ELI10 endpoint must support chapterId=2
  - Add comments documenting CH2 workflow
  - Ensure routing supports chapterId=2

#### FR-005: Chapter 2 ELI10 Placeholder Contract

- **FR-005.1**: System MUST create `specs/026-ch2-explain-el10-runtime/contracts/el10-contract.yaml`:
  - Document high-level flow
  - Define expected placeholder behavior
  - No structure for real outputs (placeholder only)

#### FR-006: Skills Extension

- **FR-006.1**: System MUST update `backend/app/ai/skills/prompt_builder_skill.py`:
  - Add placeholder function: `build_el10_prompt_ch2()`
  - Function signature with TODO comments
  - No logic implementation (placeholder only)
- **FR-006.2**: System MUST update `backend/app/ai/skills/formatting_skill.py`:
  - Add placeholder function: `format_el10_output_ch2()`
  - Function signature with TODO comments
  - No logic implementation (placeholder only)

#### FR-007: Stability Requirement

- **FR-007.1**: Backend MUST compile:
  - No import errors when starting FastAPI server
  - All imports resolve correctly
  - No syntax errors in new files
- **FR-007.2**: All new modules MUST import correctly:
  - `ch2_el10_runtime.py` is importable
  - Prompt template file exists and is readable
  - Skills functions are importable

### Assumptions

- **Assumption 1**: Feature 025 (Chapter 2 Diagram Runtime) exists and can be used as reference
- **Assumption 2**: ELI10 runtime structure can be adapted for Chapter 2 ROS 2 explanations
- **Assumption 3**: Prompt template structure can be adapted for Chapter 2 ROS 2 concepts
- **Assumption 4**: Skills layer exists and can be extended with Chapter 2 ELI10 functions
- **Assumption 5**: No new AI logic needs to be implemented (only scaffolding and placeholders)
- **Assumption 6**: Backend API routing is generic enough to handle chapterId=2 (may only need comments)

### Key Entities

**Chapter 2 ELI10 Runtime**:
- File: `ch2_el10_runtime.py`
- Function: `run(concept, chapter_id, context)`
- Steps: Validate, Build prompt, RAG retrieve, Call LLM, Format output
- All steps: TODO markers only

**Chapter 2 ELI10 Prompt Template**:
- File: `ch2_el10_prompt.txt`
- Variables: `{{concept}}`, `{{chapter_id}}`, `{{context}}`
- Purpose: Placeholder template for future ELI10 style tuning

**Chapter 2 ELI10 Routing**:
- Runtime engine: Routes `block_type == "explain-like-i-am-10" AND chapterId == 2` to ch2_el10_runtime
- API layer: Routes chapterId=2 ELI10 requests to Chapter 2 runtime
- Comments only, no logic

**Chapter 2 ELI10 Skills**:
- `build_el10_prompt_ch2()` - Prompt building for Chapter 2 ELI10 explanations
- `format_el10_output_ch2()` - Formatting for Chapter 2 ELI10 output
- Both: Placeholder functions with TODO comments

## Success Criteria *(mandatory)*

- **SC-001**: CH2 ELI10 runtime module exists (ch2_el10_runtime.py)
- **SC-002**: CH2 ELI10 prompt template exists (ch2_el10_prompt.txt)
- **SC-003**: Runtime engine routed for CH2 ELI10 (if block_type == "explain-like-i-am-10" AND chapterId == 2)
- **SC-004**: API updated for CH2 ELI10 (endpoint supports chapterId=2)
- **SC-005**: Contract spec created (el10-contract.yaml)
- **SC-006**: Skills extended (build_el10_prompt_ch2, format_el10_output_ch2)
- **SC-007**: No business logic implemented (only placeholders and structure)
- **SC-008**: Backend compiles and runs without errors

## Constraints *(mandatory)*

- **Constraint 1**: Must not implement real AI logic (only scaffolding and placeholders)
- **Constraint 2**: Must not break existing Chapter 1 ELI10 functionality
- **Constraint 3**: Must follow same patterns used in Feature 025 (Chapter 2 Diagram Runtime)
- **Constraint 4**: Must ensure backend starts without errors
- **Constraint 5**: Must ensure all imports resolve correctly

## Dependencies *(mandatory)*

- **Dependency 1**: Feature 025 (Chapter 2 Diagram Runtime) - Required as reference for structure
- **Dependency 2**: Feature 024 (Chapter 2 Backend Runtime Wiring) - Required for runtime engine routing
- **Dependency 3**: Skills layer - Required for skills extension
- **Dependency 4**: Runtime engine - Required for routing integration

## Out of Scope

- ❌ Implementing real AI logic for Chapter 2 ELI10 explanations
- ❌ Implementing RAG pipeline for Chapter 2 ELI10
- ❌ Implementing LLM provider calls for explanation generation
- ❌ Implementing explanation generation logic
- ❌ Creating actual explanation schemas or formats
- ❌ Implementing analogies or examples generation
- ❌ Adding authentication or personalization

