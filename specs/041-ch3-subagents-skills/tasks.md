# Tasks: Chapter 3 — Subagents + Skills Routing Integration

**Feature**: 041-ch3-subagents-skills | **Branch**: `041-ch3-subagents-skills` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating Chapter 3 subagents + skills scaffolding. All tasks are placeholder-only—no real logic implemented.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category`: FOLDER (Folder creation), BASE (Base contracts), SUBAGENTS (Subagents), SKILLS (Skills), RUNTIME (Runtime routing), API (API layer), CONTRACT (Contract document), VALIDATION (Validation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prepare for implementation.

- [ ] [T001] [P1] [SETUP] Verify Feature 040 (Chapter 3 RAG + Runtime Integration) is complete: Check that RAG scaffolding exists
- [ ] [T002] [P1] [SETUP] Verify Feature 024 (Chapter 2 Runtime Wiring) is complete: Check that reference pattern exists
- [ ] [T003] [P1] [SETUP] Verify backend structure exists: Check that backend/app/ai/ directory structure is ready
- [ ] [T004] [P1] [SETUP] Verify subagents folder exists: Check that backend/app/ai/subagents/ directory exists
- [ ] [T005] [P1] [SETUP] Verify skills folder exists: Check that backend/app/ai/skills/ directory exists

**Success Criteria**:
- All prerequisite features complete
- Backend structure ready
- Reference pattern available

**Dependencies**: Feature 040, Feature 024 must be complete

---

## PHASE 1 — FOLDER CREATION

**User Story**: US1 - Developer Implements Chapter 3 Subagents Scaffolding

**Test Strategy**: Can be tested by verifying folders exist.

### Create Folders

- [ ] [T006] [P1] [FOLDER] Create folder: `backend/app/ai/subagents/ch3/`

- [ ] [T007] [P1] [FOLDER] Create folder: `backend/app/ai/skills/ch3/`

**Acceptance Test**: Both folders exist at specified paths

---

## PHASE 2 — BASE CONTRACTS

**User Story**: US1 - Developer Implements Chapter 3 Subagents Scaffolding

**Test Strategy**: Can be tested by verifying base files exist and are importable.

### Create Base Agent

- [ ] [T008] [P1] [BASE] Create `backend/app/ai/subagents/base_agent.py`: Create new file

- [ ] [T009] [P1] [BASE] Add abstract base class to `backend/app/ai/subagents/base_agent.py`:
  - Import ABC and abstractmethod from abc
  - Define BaseAgent class inheriting from ABC
  - Add abstract run() method with signature: `run(request: Dict[str, Any]) -> Dict[str, Any]`
  - Add TODO notes for future polymorphism

### Create Base Skill

- [ ] [T010] [P1] [BASE] Create `backend/app/ai/skills/base_skill.py`: Create new file

- [ ] [T011] [P1] [BASE] Add basic placeholder interface to `backend/app/ai/skills/base_skill.py`:
  - Import ABC from abc
  - Define BaseSkill class inheriting from ABC
  - Add TODO notes for future polymorphism

**Acceptance Test**: base_agent.py and base_skill.py exist, abstract classes defined, imports resolve

---

## PHASE 3 — SUBAGENTS (CH3)

**User Story**: US1 - Developer Implements Chapter 3 Subagents Scaffolding

**Test Strategy**: Can be tested by verifying all subagent files exist with class + run() stub.

### Create Ask Question Agent

- [ ] [T012] [P1] [SUBAGENTS] Create `backend/app/ai/subagents/ch3/ask_question_agent.py`: Create new file

- [ ] [T013] [P1] [SUBAGENTS] Add Ch3AskQuestionAgent class to `backend/app/ai/subagents/ch3/ask_question_agent.py`:
  - Import BaseAgent from app.ai.subagents.base_agent
  - Define Ch3AskQuestionAgent class inheriting from BaseAgent
  - Add run() method stub with signature: `run(self, request: Dict[str, Any]) -> Dict[str, Any]`
  - Add TODO comments describing expected behavior
  - Return placeholder dict: `{"answer": "", "sources": [], "confidence": 0.0}`

### Create Explain ELI10 Agent

- [ ] [T014] [P1] [SUBAGENTS] Create `backend/app/ai/subagents/ch3/explain_el10_agent.py`: Create new file

- [ ] [T015] [P1] [SUBAGENTS] Add Ch3ExplainEl10Agent class to `backend/app/ai/subagents/ch3/explain_el10_agent.py`:
  - Import BaseAgent from app.ai.subagents.base_agent
  - Define Ch3ExplainEl10Agent class inheriting from BaseAgent
  - Add run() method stub with signature: `run(self, request: Dict[str, Any]) -> Dict[str, Any]`
  - Add TODO comments describing expected behavior
  - Return placeholder dict: `{"explanation": "", "analogies": [], "examples": []}`

### Create Quiz Agent

- [ ] [T016] [P1] [SUBAGENTS] Create `backend/app/ai/subagents/ch3/quiz_agent.py`: Create new file

- [ ] [T017] [P1] [SUBAGENTS] Add Ch3QuizAgent class to `backend/app/ai/subagents/ch3/quiz_agent.py`:
  - Import BaseAgent from app.ai.subagents.base_agent
  - Define Ch3QuizAgent class inheriting from BaseAgent
  - Add run() method stub with signature: `run(self, request: Dict[str, Any]) -> Dict[str, Any]`
  - Add TODO comments describing expected behavior
  - Return placeholder dict: `{"questions": [], "answers": [], "explanations": []}`

### Create Diagram Agent

- [ ] [T018] [P1] [SUBAGENTS] Create `backend/app/ai/subagents/ch3/diagram_agent.py`: Create new file

- [ ] [T019] [P1] [SUBAGENTS] Add Ch3DiagramAgent class to `backend/app/ai/subagents/ch3/diagram_agent.py`:
  - Import BaseAgent from app.ai.subagents.base_agent
  - Define Ch3DiagramAgent class inheriting from BaseAgent
  - Add run() method stub with signature: `run(self, request: Dict[str, Any]) -> Dict[str, Any]`
  - Add TODO comments describing expected behavior
  - Return placeholder dict: `{"diagram": "", "metadata": {}}`

**Acceptance Test**: All 4 subagent files exist, classes have correct signatures, TODO markers present, imports resolve

---

## PHASE 4 — SKILLS (CH3)

**User Story**: US1 - Developer Implements Chapter 3 Subagents Scaffolding

**Test Strategy**: Can be tested by verifying all skills files exist with skeleton + TODO.

### Create Retrieval Skill

- [ ] [T020] [P1] [SKILLS] Create `backend/app/ai/skills/ch3/retrieval_skill.py`: Create new file

- [ ] [T021] [P1] [SKILLS] Add Ch3RetrievalSkill class to `backend/app/ai/skills/ch3/retrieval_skill.py`:
  - Import BaseSkill from app.ai.skills.base_skill
  - Define Ch3RetrievalSkill class inheriting from BaseSkill
  - Add method stubs: `retrieve_content()`, `retrieve_by_section()`
  - Add TODO comments for future logic
  - Return placeholder empty lists

### Create Prompt Builder Skill

- [ ] [T022] [P1] [SKILLS] Create `backend/app/ai/skills/ch3/prompt_builder_skill.py`: Create new file

- [ ] [T023] [P1] [SKILLS] Add Ch3PromptBuilderSkill class to `backend/app/ai/skills/ch3/prompt_builder_skill.py`:
  - Import BaseSkill from app.ai.skills.base_skill
  - Define Ch3PromptBuilderSkill class inheriting from BaseSkill
  - Add method stubs: `build_prompt()`, `build_ask_question_prompt()`, `build_eli10_prompt()`, `build_quiz_prompt()`, `build_diagram_prompt()`
  - Add TODO comments for future logic
  - Return placeholder empty strings

### Create Formatting Skill

- [ ] [T024] [P1] [SKILLS] Create `backend/app/ai/skills/ch3/formatting_skill.py`: Create new file

- [ ] [T025] [P1] [SKILLS] Add Ch3FormattingSkill class to `backend/app/ai/skills/ch3/formatting_skill.py`:
  - Import BaseSkill from app.ai.skills.base_skill
  - Define Ch3FormattingSkill class inheriting from BaseSkill
  - Add method stubs: `format_response()`, `format_ask_question_response()`, `format_eli10_response()`, `format_quiz_response()`, `format_diagram_response()`
  - Add TODO comments for future logic
  - Return placeholder empty dicts

**Acceptance Test**: All 3 skills files exist, classes have method stubs, TODO markers present, imports resolve

---

## PHASE 5 — RUNTIME ROUTING

**User Story**: US1, US2 - Developer Implements Chapter 3 Subagents Scaffolding, System Routes Chapter 3 Requests

**Test Strategy**: Can be tested by verifying engine.py has Chapter 3 routing logic.

### Update Runtime Engine

- [ ] [T026] [P1] [RUNTIME] Open `backend/app/ai/runtime/engine.py`: Open file in editor

- [ ] [T027] [P1] [RUNTIME] Add Chapter 3 routing branch to run_ai_block() in `backend/app/ai/runtime/engine.py`:
  - Add `elif chapter_id == 3:` branch (or update existing if present)
  - Add placeholder import comments:
    - `# from app.ai.subagents.ch3.ask_question_agent import Ch3AskQuestionAgent`
    - `# from app.ai.subagents.ch3.explain_el10_agent import Ch3ExplainEl10Agent`
    - `# from app.ai.subagents.ch3.quiz_agent import Ch3QuizAgent`
    - `# from app.ai.subagents.ch3.diagram_agent import Ch3DiagramAgent`
  - Add placeholder mapping comments:
    - `# CH3_SUBAGENT_MAP = {...}`
  - Add placeholder flow comments:
    - `# TODO: Route to Chapter 3 RAG pipeline`
    - `# TODO: Call subagent.run(request_data + context)`
  - Add high-level flow comments: retrieval → prompt-building → formatting → LLM response
  - No real logic (placeholder only)

**Acceptance Test**: engine.py updated, Chapter 3 routing added, placeholder comments present, no syntax errors

---

## PHASE 6 — API COMPATIBILITY

**User Story**: US2 - System Routes Chapter 3 AI Block Requests

**Test Strategy**: Can be tested by verifying ai_blocks.py passes chapterId=3 correctly.

### Verify API Layer

- [ ] [T028] [P2] [API] Open `backend/app/api/ai_blocks.py`: Open file in editor

- [ ] [T029] [P2] [API] Verify ai_blocks.py passes chapterId=3 correctly in `backend/app/api/ai_blocks.py`:
  - Verify all endpoints accept chapterId parameter
  - Verify chapterId=3 is passed to runtime engine
  - Add TODO comments if needed
  - No endpoint changes required

**Acceptance Test**: ai_blocks.py verified, chapterId=3 properly passed, routing handled by runtime engine

---

## PHASE 7 — CONTRACT DOCUMENT

**User Story**: US1 - Developer Implements Chapter 3 Subagents Scaffolding

**Test Strategy**: Can be tested by verifying contract document exists with expected content.

### Create Contract Document

- [ ] [T030] [P1] [CONTRACT] Create `specs/041-ch3-subagents-skills/contracts/subagent-skill-contract.md`: Create new file

- [ ] [T031] [P1] [CONTRACT] Document expected agent inputs/outputs in `specs/041-ch3-subagents-skills/contracts/subagent-skill-contract.md`:
  - Document inputs for each of 4 agents
  - Document outputs placeholder format for each agent
  - Document skills responsibilities
  - Add flow diagram (comment-only)
  - Include TODO markers

**Acceptance Test**: Contract document created, all agents documented, flow diagram included, TODO markers present

---

## PHASE 8 — VALIDATION

**User Story**: US1, US2 - Structure and Routing Validation

**Test Strategy**: Can be tested by running backend startup, import tests, and API tests.

### Backend Startup Validation

- [ ] [T032] [P1] [VALIDATION] Run backend startup test: Run `uvicorn app.main:app --reload` in backend directory
- [ ] [T033] [P1] [VALIDATION] Verify backend starts without errors: Check startup logs for errors
- [ ] [T034] [P1] [VALIDATION] Fix any startup errors: Resolve import errors or syntax errors

### Import Validation

- [ ] [T035] [P1] [VALIDATION] Test base_agent import: Run `python -c "from app.ai.subagents.base_agent import BaseAgent; print('Import successful')"`
- [ ] [T036] [P1] [VALIDATION] Test base_skill import: Run `python -c "from app.ai.skills.base_skill import BaseSkill; print('Import successful')"`
- [ ] [T037] [P1] [VALIDATION] Test Ch3 subagent imports: Run `python -c "from app.ai.subagents.ch3.ask_question_agent import Ch3AskQuestionAgent; print('Import successful')"`
- [ ] [T038] [P1] [VALIDATION] Test Ch3 skills imports: Run `python -c "from app.ai.skills.ch3.retrieval_skill import Ch3RetrievalSkill; print('Import successful')"`
- [ ] [T039] [P1] [VALIDATION] Verify no circular imports: Check import sequence for circular dependencies

### File Path Validation

- [ ] [T040] [P1] [VALIDATION] Verify all file paths exist: Check that all created files exist at specified paths
- [ ] [T041] [P1] [VALIDATION] Verify auto-wiring: Check that runtime engine can import Ch3 subagents

### API Validation

- [ ] [T042] [P2] [VALIDATION] Test API call with chapterId=3: Make POST request to `/api/ai/ask-question` with `{"question": "test", "chapterId": 3}`
- [ ] [T043] [P2] [VALIDATION] Verify API routes to Chapter 3 placeholder logic: Check response (should be placeholder, no errors)

**Acceptance Test**: All validation checks pass (backend starts, imports resolve, API routes correctly, no circular imports)

---

## Summary

**Total Tasks**: 43 tasks across 8 phases
**Estimated Time**: 45-60 minutes (scaffolding only, no real AI logic)
**Complexity**: Low (following existing patterns, placeholder implementation)

**Success Criteria**:
- ✅ All subagent + skill scaffolding exists in correct paths
- ✅ Runtime engine successfully imports and routes to chapter 3 placeholder classes
- ✅ ai_blocks endpoints work with chapterId=3 without errors
- ✅ No AI logic implemented (strictly scaffolding)
- ✅ Backend server starts cleanly
- ✅ All file paths exist and are auto-wired correctly

**Next Steps**: Proceed to `/sp.implement` to execute all tasks in order.

