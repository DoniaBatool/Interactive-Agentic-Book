# Feature Specification: Chapter 2 — Interactive Quiz Runtime Engine

**Feature Branch**: `027-ch2-quiz-runtime`
**Created**: 2025-01-27
**Status**: Draft
**Type**: backend-ai-runtime
**Input**: User description: "Build the Quiz Runtime Engine scaffolding for Chapter 2. This includes runtime module, routing, quiz prompt templates, stub skill functions, contract definition, API updates. No AI logic or quiz generation logic must be implemented."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Sets Up Chapter 2 Quiz Runtime Infrastructure (Priority: P1)

As a backend developer, I need the Chapter 2 quiz runtime scaffolding in place with all runtime modules, prompt templates, routing, and integration points defined, so I can implement real AI quiz generation logic for Chapter 2 in future features without restructuring the codebase.

**Why this priority**: This establishes the complete architectural foundation for Chapter 2 quiz generation runtime. Without proper scaffolding, future AI quiz implementation for Chapter 2 will require refactoring and restructuring, causing delays and technical debt.

**Independent Test**: Can be fully tested by verifying all required files exist at specified paths, all imports resolve without errors, backend starts successfully, and all modules contain TODO placeholders for future implementation.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/ai/quiz/ch2_quiz_runtime.py`, **Then** I see blueprint for quiz generation flow with 6 steps (validate request, build prompt, retrieve chapter context, call RAG pipeline, call LLM provider, format output) all containing TODO markers only
2. **Given** the feature is implemented, **When** I check `backend/app/ai/prompts/quiz/ch2_quiz_prompt.txt`, **Then** I see placeholder template with variables `{{chapter_id}}`, `{{num_questions}}`, `{{learning_objectives}}`, `{{context}}` and TODO comments for future difficulty-level tuning
3. **Given** the feature is implemented, **When** I check `backend/app/ai/runtime/engine.py`, **Then** I see case for `if block_type == "interactive-quiz" AND chapterId == 2` that routes to `ch2_quiz_runtime.run()` with comments only (no logic)
4. **Given** the feature is implemented, **When** I check `backend/app/api/ai_blocks.py`, **Then** I see quiz endpoint supports chapterId=2 with CH2-specific handling comments
5. **Given** the feature is implemented, **When** I check `backend/app/ai/skills/prompt_builder_skill.py`, **Then** I see placeholder function `build_quiz_prompt_ch2()` with TODO comments
6. **Given** the feature is implemented, **When** I check `backend/app/ai/skills/formatting_skill.py`, **Then** I see placeholder function `format_quiz_output_ch2()` with TODO comments
7. **Given** the feature is implemented, **When** I check `backend/app/content/chapters/chapter_2_chunks.py`, **Then** I see TODO function `get_chapter2_quiz_chunks()` with placeholder
8. **Given** the feature is implemented, **When** I check `specs/027-ch2-quiz-runtime/contracts/quiz-contract.yaml`, **Then** I see expected placeholders for CH2 quiz with no real question schema
9. **Given** the feature is implemented, **When** I start the backend server, **Then** it starts without import errors or runtime exceptions

---

### User Story 2 - System Routes Chapter 2 Quiz Requests (Priority: P1)

As a system integrator, I need Chapter 2 quiz requests to route correctly through the API layer to the quiz runtime, so the routing infrastructure is ready for future AI quiz generation implementation.

**Why this priority**: This enables Chapter 2 quiz routing infrastructure. Without proper routing, Chapter 2 quiz generation cannot function, and future AI implementation will be blocked.

**Independent Test**: Can be fully tested by verifying quiz endpoint can accept chapterId=2, runtime engine routes Chapter 2 quiz requests correctly, and all routing paths contain TODO placeholders for Chapter 2 quiz operations.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I send a POST request to `/api/ai/quiz` with `chapterId=2`, **Then** the request routes to Chapter 2 quiz runtime with routing comments
2. **Given** the feature is implemented, **When** I check the runtime engine routing logic, **Then** I see `if block_type == "interactive-quiz" AND chapterId == 2` case that routes to `ch2_quiz_runtime.run()` (comments only)
3. **Given** the feature is implemented, **When** I check the quiz runtime module, **Then** I see all 6 steps (validate request, build prompt, retrieve chapter context, call RAG pipeline, call LLM provider, format output) with TODO markers only

---

### Edge Cases

- What happens when Chapter 2 quiz runtime is called but ch2_quiz_runtime.py doesn't exist?
  - Backend should handle gracefully, returning placeholder response or error message indicating runtime not yet implemented
- What happens when runtime engine receives quiz request with chapterId=2 but Chapter 2 quiz routing is not implemented?
  - Runtime engine should have placeholder routing with TODO comments indicating implementation needed
- What happens when prompt template file is missing?
  - Quiz runtime should handle gracefully, using placeholder prompt or returning error message
- What happens when skills functions are called but contain only TODO placeholders?
  - Skills functions should be callable without errors, returning placeholder responses
- What happens when backend starts but new modules have import errors?
  - Backend should not start, and import errors should be fixed before considering feature complete

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Chapter 2 Quiz Runtime Module

- **FR-001.1**: System MUST create `backend/app/ai/quiz/ch2_quiz_runtime.py`:
  - Blueprint for quiz generation flow
  - Function signature: `async def run(chapter_id: int, num_questions: int, learning_objectives: List[str] = None) -> Dict[str, Any]:`
  - Steps (all TODO markers only):
    1. Validate request
    2. Build prompt (placeholder)
    3. Retrieve chapter context (placeholder)
    4. Call RAG pipeline (placeholder)
    5. Call LLM provider (placeholder)
    6. Format output (placeholder)
  - All steps contain TODO markers only
  - Placeholder return structure
  - Must contain no executable AI logic

#### FR-002: Quiz Prompt Template

- **FR-002.1**: System MUST create `backend/app/ai/prompts/quiz/ch2_quiz_prompt.txt`:
  - Include placeholder template with variables:
    - `{{chapter_id}}`
    - `{{num_questions}}`
    - `{{learning_objectives}}`
    - `{{context}}`
  - Add TODO comment for future difficulty-level tuning
  - Template structure for Chapter 2 ROS 2 quizzes

#### FR-003: Runtime Engine Routing

- **FR-003.1**: System MUST update `backend/app/ai/runtime/engine.py`:
  - Add case: `if block_type == "interactive-quiz" AND chapterId == 2`
  - Route to `ch2_quiz_runtime.run()`
  - Comments only, no logic
  - Placeholder routing with TODO comments
  - Routing logic must be comment-only placeholder

#### FR-004: API Integration

- **FR-004.1**: System MUST update `backend/app/api/ai_blocks.py`:
  - Quiz endpoint must support chapterId=2
  - Add CH2-specific handling comments
  - Ensure request model supports chapterId=2
  - Must call runtime engine for CH2
  - Add comments documenting CH2 workflow

#### FR-005: Chapter 2 Quiz Placeholder Contract

- **FR-005.1**: System MUST create `specs/027-ch2-quiz-runtime/contracts/quiz-contract.yaml`:
  - High-level description of quiz runtime pipeline
  - Define placeholder behavior
  - No real question schema (placeholder only)

#### FR-006: Skills Extensions

- **FR-006.1**: System MUST update `backend/app/ai/skills/prompt_builder_skill.py`:
  - Add placeholder function: `build_quiz_prompt_ch2()`
  - Function signature with TODO comments
  - No logic implementation (placeholder only)
- **FR-006.2**: System MUST update `backend/app/ai/skills/formatting_skill.py`:
  - Add placeholder function: `format_quiz_output_ch2()`
  - Function signature with TODO comments
  - No logic implementation (placeholder only)

#### FR-007: Knowledge Source Preparation

- **FR-007.1**: System MUST update `backend/app/content/chapters/chapter_2_chunks.py`:
  - Add TODO function: `get_chapter2_quiz_chunks()`
  - Function signature with TODO comments
  - Placeholder return structure

#### FR-008: Stability Requirement

- **FR-008.1**: Backend MUST compile:
  - No import errors when starting FastAPI server
  - All imports resolve correctly
  - No syntax errors in new files
- **FR-008.2**: All new modules MUST import correctly:
  - `ch2_quiz_runtime.py` is importable
  - Prompt template file exists and is readable
  - Skills functions are importable

### Assumptions

- **Assumption 1**: Feature 026 (Chapter 2 ELI10 Runtime) exists and can be used as reference
- **Assumption 2**: Quiz runtime structure can be adapted for Chapter 2 ROS 2 quizzes
- **Assumption 3**: Prompt template structure can be adapted for Chapter 2 ROS 2 concepts
- **Assumption 4**: Skills layer exists and can be extended with Chapter 2 quiz functions
- **Assumption 5**: No new AI logic needs to be implemented (only scaffolding and placeholders)
- **Assumption 6**: Backend API routing is generic enough to handle chapterId=2 (may only need comments)
- **Assumption 7**: Chapter 2 chunks file exists from Feature 024

### Key Entities

**Chapter 2 Quiz Runtime**:
- File: `ch2_quiz_runtime.py`
- Function: `run(chapter_id, num_questions, learning_objectives)`
- Steps: Validate, Build prompt, Retrieve chapter context, Call RAG, Call LLM, Format output
- All steps: TODO markers only

**Chapter 2 Quiz Prompt Template**:
- File: `ch2_quiz_prompt.txt`
- Variables: `{{chapter_id}}`, `{{num_questions}}`, `{{learning_objectives}}`, `{{context}}`
- Purpose: Placeholder template for future difficulty-level tuning

**Chapter 2 Quiz Routing**:
- Runtime engine: Routes `block_type == "interactive-quiz" AND chapterId == 2` to ch2_quiz_runtime
- API layer: Routes chapterId=2 quiz requests to Chapter 2 runtime
- Comments only, no logic

**Chapter 2 Quiz Skills**:
- `build_quiz_prompt_ch2()` - Prompt building for Chapter 2 quizzes
- `format_quiz_output_ch2()` - Formatting for Chapter 2 quiz output
- Both: Placeholder functions with TODO comments

**Chapter 2 Quiz Chunks**:
- File: `chapter_2_chunks.py`
- Function: `get_chapter2_quiz_chunks()`
- Purpose: Placeholder function for quiz-specific chunk retrieval

## Success Criteria *(mandatory)*

- **SC-001**: Runtime module exists with TODO-only scaffolding (ch2_quiz_runtime.py)
- **SC-002**: Prompt template exists (ch2_quiz_prompt.txt)
- **SC-003**: Engine routing added for CH2 quiz (if block_type == "interactive-quiz" AND chapterId == 2)
- **SC-004**: API quiz endpoint supports CH2 (endpoint supports chapterId=2)
- **SC-005**: Contract YAML created (quiz-contract.yaml)
- **SC-006**: Skills extended (build_quiz_prompt_ch2, format_quiz_output_ch2)
- **SC-007**: Knowledge source preparation (get_chapter2_quiz_chunks function added)
- **SC-008**: No real AI logic implemented (only placeholders and structure)
- **SC-009**: Backend must start without errors

## Constraints *(mandatory)*

- **Constraint 1**: Must not implement real AI logic (only scaffolding and placeholders)
- **Constraint 2**: Must not break existing Chapter 1 quiz functionality
- **Constraint 3**: Must follow same patterns used in Feature 026 (Chapter 2 ELI10 Runtime)
- **Constraint 4**: Must ensure backend starts without errors
- **Constraint 5**: Must ensure all imports resolve correctly
- **Constraint 6**: Must contain no executable AI logic

## Dependencies *(mandatory)*

- **Dependency 1**: Feature 026 (Chapter 2 ELI10 Runtime) - Required as reference for structure
- **Dependency 2**: Feature 024 (Chapter 2 Backend Runtime Wiring) - Required for runtime engine routing
- **Dependency 3**: Skills layer - Required for skills extension
- **Dependency 4**: Runtime engine - Required for routing integration
- **Dependency 5**: Chapter 2 chunks file - Required for knowledge source preparation

## Out of Scope

- ❌ Implementing real AI logic for Chapter 2 quiz generation
- ❌ Implementing RAG pipeline for Chapter 2 quizzes
- ❌ Implementing LLM provider calls for quiz generation
- ❌ Implementing quiz generation logic
- ❌ Creating actual question schemas or formats
- ❌ Implementing question validation or scoring
- ❌ Adding authentication or personalization

