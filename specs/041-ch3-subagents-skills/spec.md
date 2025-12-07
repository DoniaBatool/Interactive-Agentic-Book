# Feature Specification: Chapter 3 — Subagents + Skills Routing Integration

**Feature Branch**: `041-ch3-subagents-skills`
**Created**: 2025-01-27
**Status**: Draft
**Type**: backend-ai-architecture
**Input**: User description: "Add the subagent + skills scaffolding for Chapter 3 so that all four AI-interactive blocks (ask-question, explain-like-I-am-10, quiz, diagram) route through placeholder subagents and skills. No business logic."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Implements Chapter 3 Subagents Scaffolding (Priority: P1)

As a developer, I need to implement subagent and skills scaffolding for Chapter 3, so the backend architecture is ready for future AI logic implementation and Chapter 3 AI blocks can route through placeholder subagents and skills.

**Why this priority**: This establishes the subagent and skills infrastructure foundation for Chapter 3. Without proper scaffolding, future AI logic implementation cannot proceed.

**Independent Test**: Can be fully tested by verifying all scaffolding files exist, backend starts without errors, and Chapter 3 routing is in place.

**Acceptance Scenarios**:

1. **Given** the backend is running, **When** I start the server with `uvicorn app.main:app --reload`, **Then** the server starts without errors
2. **Given** the scaffolding is complete, **When** I check `backend/app/ai/subagents/ch3/ask_question_agent.py`, **Then** I see class with `run()` method stub and TODO markers
3. **Given** the scaffolding is complete, **When** I check `backend/app/ai/skills/ch3/retrieval_skill.py`, **Then** I see class with method stubs and TODO comments
4. **Given** the scaffolding is complete, **When** I check `backend/app/ai/runtime/engine.py`, **Then** I see Chapter 3 routing logic with placeholder subagent calls
5. **Given** the scaffolding is complete, **When** I check `backend/app/ai/subagents/base_agent.py`, **Then** I see abstract base class with `run()` method definition
6. **Given** I make an API call with chapterId=3, **When** the request is processed, **Then** it routes to Chapter 3 placeholder subagents (no real AI calls)

---

### User Story 2 - System Routes Chapter 3 AI Block Requests (Priority: P2)

As a backend system, I need to route Chapter 3 AI block requests through subagents and skills, so future AI logic can process Chapter 3 content correctly.

**Why this priority**: Ensures routing infrastructure is in place for future AI logic implementation.

**Independent Test**: Can be fully tested by making API calls with chapterId=3 and verifying routing occurs (even if placeholder responses).

**Acceptance Scenarios**:

1. **Given** the API is running, **When** I call POST `/api/ai/ask-question` with chapterId=3, **Then** the request routes to Chapter 3 ask_question_agent placeholder
2. **Given** the API is running, **When** I call POST `/api/ai/explain-like-10` with chapterId=3, **Then** the request routes to Chapter 3 explain_el10_agent placeholder
3. **Given** the API is running, **When** I call POST `/api/ai/quiz` with chapterId=3, **Then** the request routes to Chapter 3 quiz_agent placeholder
4. **Given** the API is running, **When** I call POST `/api/ai/diagram` with chapterId=3, **Then** the request routes to Chapter 3 diagram_agent placeholder

---

### Edge Cases

- What happens when chapterId=3 is passed but Chapter 3 subagents don't exist?
  - **Expected**: Backend should handle gracefully with placeholder logic, no errors
- What happens when a subagent class is missing?
  - **Expected**: Import error or graceful fallback, backend should not crash
- What happens when base_agent.py doesn't exist?
  - **Expected**: Subagents may not inherit from base, but should still work as standalone classes
- What happens when skills are called but not implemented?
  - **Expected**: Placeholder methods return empty values, no errors

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Subagents Folder for Chapter 3

- **FR-001.1**: System MUST create `backend/app/ai/subagents/ch3/` folder
- **FR-001.2**: System MUST create 4 subagent files:
  - `ask_question_agent.py` - Class with `run(request)` method stub
  - `explain_el10_agent.py` - Class with `run(request)` method stub
  - `quiz_agent.py` - Class with `run(request)` method stub
  - `diagram_agent.py` - Class with `run(request)` method stub
- **FR-001.3**: Each file MUST include:
  - Class definition (e.g., `Ch3AskQuestionAgent`)
  - `run(request)` method with `pass` or placeholder return
  - TODO comments describing expected behavior
  - No real logic implementation

#### FR-002: Skills Folder for Chapter 3

- **FR-002.1**: System MUST create `backend/app/ai/skills/ch3/` folder
- **FR-002.2**: System MUST create 3 skills files:
  - `retrieval_skill.py` - Class with method stubs for RAG context pulling
  - `prompt_builder_skill.py` - Class with method stubs for LLM prompt building
  - `formatting_skill.py` - Class with method stubs for response formatting
- **FR-002.3**: Each file MUST include:
  - Class definition (e.g., `Ch3RetrievalSkill`)
  - Method stubs with TODO comments
  - No real logic implementation

#### FR-003: Runtime Engine Routing

- **FR-003.1**: System MUST update `backend/app/ai/runtime/engine.py`:
  - Add routing logic for `chapterId == 3`
  - Map AI block types to Chapter 3 subagent classes
  - Add high-level flow comments: retrieval → prompt-building → formatting → LLM response
  - No real logic (placeholder routing only)

#### FR-004: Shared Interface Contracts

- **FR-004.1**: System MUST create `backend/app/ai/subagents/base_agent.py`:
  - Define abstract base class with `run()` method
  - Add TODO notes for future polymorphism
  - No real implementation (abstract class only)

- **FR-004.2**: System MUST create `backend/app/ai/skills/base_skill.py`:
  - Define basic placeholder interface
  - Add TODO notes for future polymorphism
  - No real implementation (abstract class only)

#### FR-005: API Integration Layer

- **FR-005.1**: System MUST verify `backend/app/api/ai_blocks.py`:
  - Ensures chapterId=3 is properly passed to runtime engine
  - No new endpoints required
  - Only routing support verification

#### FR-006: Documentation

- **FR-006.1**: System MUST create `specs/041-ch3-subagents-skills/contracts/subagent-skill-contract.md`:
  - Define expected inputs for each agent
  - Define expected outputs placeholder format
  - Include flow diagram (comment-only)
  - Include TODO markers

---

## Non-Functional Requirements

- **NFR-001**: All scaffolding MUST use TODO comments (no real logic)
- **NFR-002**: Backend MUST start without errors
- **NFR-003**: All imports MUST resolve correctly
- **NFR-004**: No circular imports
- **NFR-005**: Follow Chapter 2 subagents/skills patterns exactly

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All subagent + skill scaffolding exists in correct paths
- **SC-002**: Runtime engine successfully imports and routes to chapter 3 placeholder classes
- **SC-003**: ai_blocks endpoints work with chapterId=3 without errors
- **SC-004**: No AI logic implemented (strictly scaffolding)
- **SC-005**: Backend server starts cleanly
- **SC-006**: All file paths exist and are auto-wired correctly

---

## Constraints *(mandatory)*

### Technical Constraints

- **C-001**: MUST NOT implement real AI logic (scaffolding only)
- **C-002**: MUST NOT implement real subagent logic (placeholders only)
- **C-003**: MUST NOT implement real skills logic (placeholders only)
- **C-004**: MUST follow Chapter 2 subagents/skills patterns exactly
- **C-005**: MUST ensure backend boots successfully

### Process Constraints

- **C-006**: MUST use TODO comments for all future logic
- **C-007**: MUST ensure all imports resolve
- **C-008**: MUST verify backend startup before marking complete
- **C-009**: MUST maintain exact file paths as specified

### Scope Constraints (Out of Scope)

- **OOS-001**: Real subagent implementation
- **OOS-002**: Real skills implementation
- **OOS-003**: Real AI logic
- **OOS-004**: Real LLM calls
- **OOS-005**: Real RAG operations

---

## Dependencies *(mandatory)*

### Internal Dependencies

- **D-001**: Feature 001 (Base Project Initialization) MUST be complete
- **D-002**: Feature 040 (Chapter 3 RAG + Runtime Integration) MUST be complete
- **D-003**: Feature 024 (Chapter 2 Runtime Wiring) MUST be complete - Reference for patterns

### External Dependencies

- **D-004**: No new external dependencies required (scaffolding only)

### Blocking Issues

- None identified. All dependencies resolved.

### Assumptions

- **A-001**: Chapter 2 subagents/skills patterns are correct and can be replicated
- **A-002**: Backend structure supports chapter-specific subagents/skills folders
- **A-003**: Runtime engine can route to chapter-specific subagents

---

## Implementation Notes *(optional guidance)*

### Recommended Implementation Order

1. **Phase 1: Base Contracts**
   - Create base_agent.py with abstract class
   - Create base_skill.py with placeholder interface

2. **Phase 2: Subagents**
   - Create ch3/ folder
   - Create 4 subagent files with class stubs

3. **Phase 3: Skills**
   - Create ch3/ folder
   - Create 3 skills files with class stubs

4. **Phase 4: Runtime Routing**
   - Update engine.py with Chapter 3 routing
   - Add placeholder subagent mapping

5. **Phase 5: API Verification**
   - Verify ai_blocks.py passes chapterId=3

6. **Phase 6: Documentation**
   - Create contract documentation

---

**Next Steps**: Proceed to `/sp.plan` to create architectural plan for subagents + skills integration.

