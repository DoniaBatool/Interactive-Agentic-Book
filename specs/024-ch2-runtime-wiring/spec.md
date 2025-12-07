# Feature Specification: Chapter 2 — Backend Runtime Wiring for AI Blocks

**Feature Branch**: `024-ch2-runtime-wiring`
**Created**: 2025-01-27
**Status**: Draft
**Type**: backend-integration
**Input**: User description: "Connect all Chapter 2 interactive blocks (Ask Question, Explain Like I'm 10, Quiz Generator, Diagram Generator) to the AI Runtime Engine created in Feature 006. This is a pure scaffolding feature with NO real AI logic."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Wires Chapter 2 into Backend Runtime (Priority: P1)

As a backend developer, I need Chapter 2 fully wired into the AI Runtime Engine with API routing, runtime engine awareness, RAG layer scaffolding, subagent placeholders, and skills extensions, so I can implement real AI logic in future features without restructuring the codebase.

**Why this priority**: This connects Chapter 2 into the existing AI Runtime Engine. Without proper wiring, Chapter 2 AI blocks cannot route correctly, runtime engine cannot handle Chapter 2 requests, and future AI implementation will require restructuring.

**Independent Test**: Can be fully tested by verifying all required files are updated with Chapter 2 wiring, all imports resolve without errors, backend starts successfully, and all modules contain TODO placeholders for Chapter 2 operations.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/api/ai_blocks.py`, **Then** I see each POST request includes chapterId=2 routing and TODO comments for Chapter 2 runtime calls
2. **Given** the feature is implemented, **When** I check `backend/app/ai/runtime/engine.py`, **Then** I see placeholder routing for chapterId=2 with comments describing expected flows
3. **Given** the feature is implemented, **When** I check `backend/app/content/chapters/chapter_2_chunks.py`, **Then** I see `get_chapter_chunks()` function with TODO placeholder list, ensuring parity with chapter_1_chunks structure
4. **Given** the feature is implemented, **When** I check `backend/app/ai/subagents/ch2_ask_question_agent.py`, **Then** I see empty scaffold file with TODO comment: "# TODO: blueprint for Chapter 2 version of the agent"
5. **Given** the feature is implemented, **When** I check `backend/app/ai/subagents/ch2_explain_el10_agent.py`, **Then** I see empty scaffold file with TODO comment
6. **Given** the feature is implemented, **When** I check `backend/app/ai/subagents/ch2_quiz_agent.py`, **Then** I see empty scaffold file with TODO comment
7. **Given** the feature is implemented, **When** I check `backend/app/ai/subagents/ch2_diagram_agent.py`, **Then** I see empty scaffold file with TODO comment
8. **Given** the feature is implemented, **When** I check `backend/app/ai/skills/retrieval_skill.py`, **Then** I see Chapter 2 placeholder routing comments (no logic)
9. **Given** the feature is implemented, **When** I check `backend/app/ai/skills/prompt_builder_skill.py`, **Then** I see Chapter 2 placeholder routing comments (no logic)
10. **Given** the feature is implemented, **When** I check `backend/app/ai/skills/formatting_skill.py`, **Then** I see Chapter 2 placeholder routing comments (no logic)
11. **Given** the feature is implemented, **When** I check `specs/024-ch2-runtime-wiring/contracts/runtime-flow.yaml`, **Then** I see documentation for expected runtime flow for Chapter 2
12. **Given** the feature is implemented, **When** I start the backend server, **Then** it starts without import errors or runtime exceptions
13. **Given** the feature is implemented, **When** I check all new modules, **Then** they import correctly without errors

---

### User Story 2 - System Routes Chapter 2 AI Block Requests (Priority: P1)

As a system integrator, I need Chapter 2 AI block requests to route correctly through the API layer to the runtime engine, so the routing infrastructure is ready for future AI logic implementation.

**Why this priority**: This enables Chapter 2 AI block routing infrastructure. Without proper routing, Chapter 2 AI blocks cannot function, and future AI implementation will be blocked.

**Independent Test**: Can be fully tested by verifying all AI block endpoints can accept chapterId=2, runtime engine routes Chapter 2 requests correctly, and all routing paths contain TODO placeholders for Chapter 2 operations.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I send a POST request to `/api/ai/ask-question` with `chapterId=2`, **Then** the request routes to runtime engine with Chapter 2 routing comments
2. **Given** the feature is implemented, **When** I send a POST request to `/api/ai/explain-like-10` with `chapterId=2`, **Then** the request routes to runtime engine with Chapter 2 routing comments
3. **Given** the feature is implemented, **When** I send a POST request to `/api/ai/quiz` with `chapterId=2`, **Then** the request routes to runtime engine with Chapter 2 routing comments
4. **Given** the feature is implemented, **When** I send a POST request to `/api/ai/diagram` with `chapterId=2`, **Then** the request routes to runtime engine with Chapter 2 routing comments
5. **Given** the feature is implemented, **When** I check the runtime engine routing logic, **Then** I see chapterId=2 handling path with placeholder comments

---

### Edge Cases

- What happens when Chapter 2 runtime is called but chapter_2_chunks.py doesn't exist?
  - Backend should handle gracefully, returning placeholder response or error message indicating chunks not yet implemented
- What happens when runtime engine receives chapterId=2 but Chapter 2 routing is not implemented?
  - Runtime engine should have placeholder routing with TODO comments indicating implementation needed
- What happens when a Chapter 2 subagent file is imported but contains only TODO comments?
  - Subagent files should be importable without errors, containing only TODO placeholders
- What happens when skills layer receives Chapter 2 request but Chapter 2 handling is not implemented?
  - Skills should have placeholder routing comments indicating Chapter 2 handling needs implementation
- What happens when backend starts but new modules have import errors?
  - Backend should not start, and import errors should be fixed before considering feature complete

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: API Layer Updates

- **FR-001.1**: System MUST update `backend/app/api/ai_blocks.py`:
  - Ensure each POST request includes chapterId=2 routing capability
  - Route requests to `from app.ai.runtime.engine import run_ai_block`
  - Add routing comments: `# TODO: Chapter 2 runtime call`
  - No real routing logic changes if routing is already generic (only add comments)

#### FR-002: Runtime Engine Awareness of Chapter 2

- **FR-002.1**: System MUST update `backend/app/ai/runtime/engine.py`:
  - Add placeholder routing for chapterId=2
  - Add comments describing expected flows for Chapter 2
  - Ensure chapterId=2 routes correctly to Chapter 2 subagents (placeholders)
  - No logic implemented (only placeholders and comments)

#### FR-003: RAG Layer for Chapter 2

- **FR-003.1**: System MUST create `backend/app/content/chapters/chapter_2_chunks.py`:
  - Define `get_chapter_chunks()` function with TODO placeholder list
  - Ensure parity with `chapter_1_chunks` structure
  - Function signature: `def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:`
  - Return empty list or placeholder structure (no real implementation)

#### FR-004: Subagent Draft Files (Placeholders)

- **FR-004.1**: System MUST create empty scaffold files:
  - `backend/app/ai/subagents/ch2_ask_question_agent.py`
  - `backend/app/ai/subagents/ch2_explain_el10_agent.py`
  - `backend/app/ai/subagents/ch2_quiz_agent.py`
  - `backend/app/ai/subagents/ch2_diagram_agent.py`
- **FR-004.2**: Each file MUST contain:
  - Module docstring describing purpose
  - TODO comment: `# TODO: blueprint for Chapter 2 version of the agent`
  - Function placeholder with proper signature (if applicable)
  - No real implementation (only placeholders)

#### FR-005: Skills Layer Extension

- **FR-005.1**: System MUST update `backend/app/ai/skills/retrieval_skill.py`:
  - Add Chapter 2 placeholder routing comments (no logic)
  - Document expected Chapter 2 handling path
- **FR-005.2**: System MUST update `backend/app/ai/skills/prompt_builder_skill.py`:
  - Add Chapter 2 placeholder routing comments (no logic)
  - Document expected Chapter 2 handling path
- **FR-005.3**: System MUST update `backend/app/ai/skills/formatting_skill.py`:
  - Add Chapter 2 placeholder routing comments (no logic)
  - Document expected Chapter 2 handling path

#### FR-006: Contracts

- **FR-006.1**: System MUST create `specs/024-ch2-runtime-wiring/contracts/runtime-flow.yaml`:
  - Document expected runtime flow for Chapter 2
  - Document API → Runtime Engine → Subagent flow
  - Document Chapter 2-specific routing patterns

#### FR-007: Stability + Build Requirements

- **FR-007.1**: Backend MUST start without errors:
  - No import errors when starting FastAPI server
  - All imports resolve correctly
  - No syntax errors in new files
- **FR-007.2**: All new modules MUST import correctly:
  - `chapter_2_chunks.py` is importable
  - All subagent files are importable
  - No circular import errors

### Assumptions

- **Assumption 1**: AI Runtime Engine exists from Feature 006
- **Assumption 2**: Chapter 1 chunks structure exists and can be used as reference
- **Assumption 3**: Existing subagents exist and can be used as reference for structure
- **Assumption 4**: Skills layer exists and can be extended with Chapter 2 placeholders
- **Assumption 5**: No new AI logic needs to be implemented (only scaffolding and placeholders)
- **Assumption 6**: Backend API routing is generic enough to handle chapterId=2 (may only need comments)

### Key Entities

**Chapter 2 Runtime Routing**:
- API endpoint routing (chapterId=2)
- Runtime engine routing (chapterId=2 handling path)
- Subagent routing (ch2_* agents)

**Chapter 2 Chunks File**:
- Function: `get_chapter_chunks(chapter_id=2)`
- Structure: Parity with chapter_1_chunks
- Return: Empty list or placeholder structure

**Chapter 2 Subagents**:
- Files: ch2_ask_question_agent.py, ch2_explain_el10_agent.py, ch2_quiz_agent.py, ch2_diagram_agent.py
- Structure: Empty scaffolds with TODO comments
- Purpose: Placeholders for future Chapter 2-specific agent logic

**Skills Layer Extensions**:
- Files: retrieval_skill.py, prompt_builder_skill.py, formatting_skill.py
- Updates: Chapter 2 placeholder routing comments
- Purpose: Document expected Chapter 2 handling paths

## Success Criteria *(mandatory)*

- **SC-001**: Chapter 2 has complete scaffolding for backend runtime
- **SC-002**: All subagent files exist (4 files: ch2_ask_question_agent.py, ch2_explain_el10_agent.py, ch2_quiz_agent.py, ch2_diagram_agent.py)
- **SC-003**: Runtime engine references Chapter 2 correctly (chapterId=2 routing exists)
- **SC-004**: No AI logic exists—only placeholders and structure
- **SC-005**: Backend compiles and runs without errors
- **SC-006**: All new modules import correctly
- **SC-007**: Contract file documents expected runtime flow for Chapter 2

## Constraints *(mandatory)*

- **Constraint 1**: Must not implement real AI logic (only scaffolding and placeholders)
- **Constraint 2**: Must not break existing Chapter 1 functionality
- **Constraint 3**: Must follow same patterns used in Chapter 1 runtime wiring
- **Constraint 4**: Must ensure backend starts without errors
- **Constraint 5**: Must ensure all imports resolve correctly

## Dependencies *(mandatory)*

- **Dependency 1**: Feature 006 (AI Runtime Engine) - Required for runtime engine infrastructure
- **Dependency 2**: Feature 023 (Chapter 2 AI Block MDX Integration) - Required for frontend AI blocks
- **Dependency 3**: Chapter 1 chunks structure - Required as reference for chapter_2_chunks.py structure
- **Dependency 4**: Existing subagents - Required as reference for subagent structure
- **Dependency 5**: Skills layer - Required for skills extension

## Out of Scope

- ❌ Implementing real AI logic for Chapter 2
- ❌ Implementing RAG pipeline for Chapter 2
- ❌ Implementing chunking logic for Chapter 2
- ❌ Implementing subagent logic for Chapter 2
- ❌ Implementing skills logic for Chapter 2
- ❌ Creating new runtime engine infrastructure
- ❌ Adding authentication or personalization
- ❌ Implementing LLM provider calls
- ❌ Creating database schemas or migrations

