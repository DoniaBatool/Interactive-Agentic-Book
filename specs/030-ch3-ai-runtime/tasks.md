# Tasks: Chapter 3 — AI Runtime Engine Integration

**Feature**: 030-ch3-ai-runtime | **Branch**: `030-ch3-ai-runtime` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for connecting Chapter 3's AI Blocks to the global AI Runtime Engine (scaffolding only, no real AI logic).

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), SETUP (Initial setup), VALIDATION (Validation tasks)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before implementing Chapter 3 runtime engine integration scaffolding.

- [ ] [T001] [P1] [SETUP] Verify Feature 005 is complete: Check that `backend/app/ai/runtime/engine.py` exists with runtime engine structure
- [ ] [T002] [P1] [SETUP] Verify Feature 017 or 020 is complete: Check that Chapter 2 runtime patterns exist for reference
- [ ] [T003] [P1] [SETUP] Verify Feature 028 is complete: Check that `backend/app/content/chapters/chapter_3.py` exists with Chapter 3 metadata
- [ ] [T004] [P1] [SETUP] Verify Feature 029 is complete: Check that `backend/app/ai/rag/ch3_pipeline.py` exists with `run_ch3_rag_pipeline()` function
- [ ] [T005] [P1] [SETUP] Verify API file exists: Check that `backend/app/api/ai_blocks.py` exists
- [ ] [T006] [P1] [SETUP] Verify skills exist: Check that `backend/app/ai/skills/retrieval_skill.py` and `prompt_builder_skill.py` exist
- [ ] [T007] [P1] [SETUP] Verify subagents directory exists: Check that `backend/app/ai/subagents/` directory exists
- [ ] [T008] [P1] [SETUP] Verify backend imports work: Run `cd backend && python -c "from app.main import app; print('Backend imports OK')"` - should complete without errors

**Success Criteria**:
- All prerequisite files exist
- Backend imports resolve without errors
- Ready to implement scaffolding

**Dependencies**: Feature 005 (AI Runtime Engine), Feature 017/020 (Chapter 2 AI Runtime), Feature 028 (Chapter 3 AI Blocks), Feature 029 (Chapter 3 RAG Prep)

---

## PHASE A — API Routing Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 3

**Test Strategy**: Can be tested by adding Chapter 3 endpoints and verifying imports work.

### Add Chapter 3 Ask Question Endpoint

- [ ] [T009] [P1] [US1] Add `POST /ai/ch3/ask-question` endpoint to `backend/app/api/ai_blocks.py`:
  - Add endpoint function: `async def ch3_ask_question(request: AskQuestionRequest) -> AIBlockResponse:`
  - Add docstring explaining Chapter 3 ask-question endpoint
  - Add TODO comment: `# TODO: Chapter 3 ask-question routing`
  - Add call: `result = await run_ai_block("ask-question", request.model_dump())`
  - Add placeholder return: `return AIBlockResponse(message="AI block placeholder", received=request.model_dump())`
  - Expected content: New endpoint that routes to runtime engine
  - Dependencies: Existing `run_ai_block()` function, `AskQuestionRequest` model
  - Acceptance test: Endpoint exists, imports work, no syntax errors

### Add Chapter 3 Explain EL10 Endpoint

- [ ] [T010] [P1] [US1] Add `POST /ai/ch3/explain-el10` endpoint to `backend/app/api/ai_blocks.py`:
  - Add endpoint function: `async def ch3_explain_el10(request: ExplainLike10Request) -> AIBlockResponse:`
  - Add docstring explaining Chapter 3 explain-el10 endpoint
  - Add TODO comment: `# TODO: Chapter 3 explain-el10 routing`
  - Add call: `result = await run_ai_block("explain-like-10", request.model_dump())`
  - Add placeholder return: `return AIBlockResponse(message="AI block placeholder", received=request.model_dump())`
  - Expected content: New endpoint that routes to runtime engine
  - Dependencies: Existing `run_ai_block()` function, `ExplainLike10Request` model
  - Acceptance test: Endpoint exists, imports work, no syntax errors

### Add Chapter 3 Quiz Endpoint

- [ ] [T011] [P1] [US1] Add `POST /ai/ch3/quiz` endpoint to `backend/app/api/ai_blocks.py`:
  - Add endpoint function: `async def ch3_quiz(request: QuizRequest) -> AIBlockResponse:`
  - Add docstring explaining Chapter 3 quiz endpoint
  - Add TODO comment: `# TODO: Chapter 3 quiz routing`
  - Add call: `result = await run_ai_block("quiz", request.model_dump())`
  - Add placeholder return: `return AIBlockResponse(message="AI block placeholder", received=request.model_dump())`
  - Expected content: New endpoint that routes to runtime engine
  - Dependencies: Existing `run_ai_block()` function, `QuizRequest` model
  - Acceptance test: Endpoint exists, imports work, no syntax errors

### Add Chapter 3 Diagram Endpoint

- [ ] [T012] [P1] [US1] Add `POST /ai/ch3/diagram` endpoint to `backend/app/api/ai_blocks.py`:
  - Add endpoint function: `async def ch3_diagram(request: DiagramRequest) -> AIBlockResponse:`
  - Add docstring explaining Chapter 3 diagram endpoint
  - Add TODO comment: `# TODO: Chapter 3 diagram routing`
  - Add call: `result = await run_ai_block("diagram", request.model_dump())`
  - Add placeholder return: `return AIBlockResponse(message="AI block placeholder", received=request.model_dump())`
  - Expected content: New endpoint that routes to runtime engine
  - Dependencies: Existing `run_ai_block()` function, `DiagramRequest` model
  - Acceptance test: Endpoint exists, imports work, no syntax errors

### Verify API Imports

- [ ] [T013] [P1] [US1] Verify `backend/app/api/ai_blocks.py` imports correctly:
  - Run: `cd backend && python -c "from app.api.ai_blocks import router; print('API imports OK')"`
  - Expected: Import succeeds without errors
  - Dependencies: All updated code in ai_blocks.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: All 4 Chapter 3 API endpoints added, imports work

---

## PHASE B — Runtime Engine Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 3

**Test Strategy**: Can be tested by updating runtime engine and verifying imports work.

### Add Chapter 3 Routing Logic

- [ ] [T014] [P1] [US1] Update `backend/app/ai/runtime/engine.py` function `run_ai_block()`:
  - Add TODO comment block: `# TODO: Chapter 3 routing`
  - Add code: `chapter_id = request_data.get("chapterId", 1)` (if not already present)
  - Add conditional: `if chapter_id == 3:`
  - Add TODO: `#     # TODO: Route to Chapter 3 subagent`
  - Add TODO: `#     # TODO: Call ch3_pipeline.run_ch3_rag_pipeline() for RAG context`
  - Add TODO: `#     # TODO: Select provider for Chapter 3`
  - Add TODO: `#     # TODO: Call appropriate Chapter 3 subagent`
  - Add TODO: `#     # TODO: Format response`
  - Expected content: Chapter 3 routing logic with TODO comments
  - Dependencies: Existing `run_ai_block()` function from Feature 005
  - Acceptance test: Code added, imports work, no syntax errors

### Add Chapter 3 RAG Integration Comments

- [ ] [T015] [P1] [US1] Add Chapter 3 RAG integration comments to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Import ch3_pipeline for Chapter 3 RAG operations`
  - Add TODO comment: `# TODO: from app.ai.rag.ch3_pipeline import run_ch3_rag_pipeline`
  - Add TODO comment: `# TODO: Use run_ch3_rag_pipeline() when chapter_id=3`
  - Add TODO comment: `# TODO: Pass RAG context to Chapter 3 subagents`
  - Expected content: TODO comments for Chapter 3 RAG integration
  - Dependencies: ch3_pipeline.py (from Feature 029)
  - Acceptance test: Comments added, no syntax errors

### Add Chapter 3 Subagent Routing Comments

- [ ] [T016] [P1] [US1] Add Chapter 3 subagent routing comments to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Import Chapter 3 subagents`
  - Add TODO comment: `# TODO: from app.ai.subagents.ch3_ask_question_agent import ch3_ask_question_agent`
  - Add TODO comment: `# TODO: from app.ai.subagents.ch3_explain_el10_agent import ch3_explain_el10_agent`
  - Add TODO comment: `# TODO: from app.ai.subagents.ch3_quiz_agent import ch3_quiz_agent`
  - Add TODO comment: `# TODO: from app.ai.subagents.ch3_diagram_agent import ch3_diagram_agent`
  - Add TODO comment: `# TODO: CH3_SUBAGENT_MAP = {"ask-question": ch3_ask_question_agent, ...}`
  - Expected content: TODO comments for Chapter 3 subagent routing
  - Dependencies: Chapter 3 subagent files (from Phase C)
  - Acceptance test: Comments added, no syntax errors

### Add Chapter 3 Provider Selection Comments

- [ ] [T017] [P1] [US1] Add Chapter 3 provider selection comments to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Select provider for Chapter 3`
  - Add TODO comment: `# TODO: Use settings.ch3_llm_model for Chapter 3 (if configured)`
  - Add TODO comment: `# TODO: Fallback to default provider if Chapter 3 model not configured`
  - Expected content: TODO comments for Chapter 3 provider selection
  - Dependencies: settings.py (for Chapter 3 model configuration)
  - Acceptance test: Comments added, no syntax errors

### Verify Engine Imports

- [ ] [T018] [P1] [US1] Verify `backend/app/ai/runtime/engine.py` imports correctly:
  - Run: `cd backend && python -c "from app.ai.runtime.engine import run_ai_block; print('Engine import OK')"`
  - Expected: Import succeeds without errors
  - Dependencies: All updated code in engine.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: Runtime engine extended with Chapter 3 routing logic, imports work

---

## PHASE C — Subagent Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 3

**Test Strategy**: Can be tested by creating subagent files and verifying imports work.

### Create ch3_ask_question_agent.py

- [ ] [T019] [P1] [US1] Create `backend/app/ai/subagents/ch3_ask_question_agent.py`:
  - Add module docstring: `"""Chapter 3 Ask Question Agent - Specialized agent for answering questions about Physical AI concepts using Chapter 3 context."""`
  - Add function: `async def ch3_ask_question_agent(question: str, context: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Expected input/output signatures
    - Agent flow comments (5 steps: retrieve → build prompt → call LLM → format → return)
    - Physical AI-specific considerations
  - Add TODO comments for each step
  - Add placeholder return: `return {"answer": "", "sources": [], "confidence": 0.0}`
  - Expected content: Complete subagent file with placeholder function
  - Dependencies: `typing` module (Dict, Any)
  - Acceptance test: File exists, imports work, function is callable

### Create ch3_explain_el10_agent.py

- [ ] [T020] [P1] [US1] Create `backend/app/ai/subagents/ch3_explain_el10_agent.py`:
  - Add module docstring: `"""Chapter 3 Explain Like I'm 10 Agent - Specialized agent for generating simplified explanations of Physical AI concepts using Chapter 3 context."""`
  - Add function: `async def ch3_explain_el10_agent(concept: str, context: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Expected input/output signatures
    - Agent flow comments (5 steps: retrieve → build prompt → call LLM → format → return)
    - Physical AI-specific considerations (analogies, examples)
  - Add TODO comments for each step
  - Add placeholder return: `return {"explanation": "", "examples": [], "analogies": []}`
  - Expected content: Complete subagent file with placeholder function
  - Dependencies: `typing` module (Dict, Any)
  - Acceptance test: File exists, imports work, function is callable

### Create ch3_quiz_agent.py

- [ ] [T021] [P1] [US1] Create `backend/app/ai/subagents/ch3_quiz_agent.py`:
  - Add module docstring: `"""Chapter 3 Quiz Agent - Specialized agent for generating quiz questions about Physical AI concepts using Chapter 3 context."""`
  - Add function: `async def ch3_quiz_agent(chapter_id: int, num_questions: int, learning_objectives: Optional[List[str]], context: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Expected input/output signatures
    - Agent flow comments (6 steps: retrieve → build prompt → call LLM → format → return)
    - Physical AI-specific considerations (learning objectives, concepts)
  - Add TODO comments for each step
  - Add placeholder return: `return {"questions": [], "learning_objectives": [], "metadata": {}}`
  - Expected content: Complete subagent file with placeholder function
  - Dependencies: `typing` module (Dict, Any, List, Optional)
  - Acceptance test: File exists, imports work, function is callable

### Create ch3_diagram_agent.py

- [ ] [T022] [P1] [US1] Create `backend/app/ai/subagents/ch3_diagram_agent.py`:
  - Add module docstring: `"""Chapter 3 Diagram Agent - Specialized agent for generating diagrams of Physical AI concepts using Chapter 3 context."""`
  - Add function: `async def ch3_diagram_agent(diagram_type: str, concepts: List[str], context: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Expected input/output signatures
    - Agent flow comments (5 steps: retrieve → build prompt → call LLM → format → return)
    - Physical AI-specific considerations (diagram types, concepts)
  - Add TODO comments for each step
  - Add placeholder return: `return {"nodes": [], "edges": [], "svg": "", "metadata": {}}`
  - Expected content: Complete subagent file with placeholder function
  - Dependencies: `typing` module (Dict, Any, List)
  - Acceptance test: File exists, imports work, function is callable

### Verify Subagent Imports

- [ ] [T023] [P1] [US1] Verify all Chapter 3 subagents import correctly:
  - Run: `cd backend && python -c "from app.ai.subagents.ch3_ask_question_agent import ch3_ask_question_agent; from app.ai.subagents.ch3_explain_el10_agent import ch3_explain_el10_agent; from app.ai.subagents.ch3_quiz_agent import ch3_quiz_agent; from app.ai.subagents.ch3_diagram_agent import ch3_diagram_agent; print('All subagents import OK')"`
  - Expected: All imports succeed without errors
  - Dependencies: All 4 subagent files created
  - Acceptance test: All imports work, no syntax errors

**Phase Completion**: All 4 Chapter 3 subagent files created, imports work

---

## PHASE D — Skills Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 3

**Test Strategy**: Can be tested by updating skills files and verifying imports work.

### Update prompt_builder_skill.py

- [ ] [T024] [P1] [US1] Update `backend/app/ai/skills/prompt_builder_skill.py` function `build_prompt()`:
  - Add TODO comment block: `# TODO: Chapter 3 support`
  - Add conditional comment: `# if chapter_id == 3:`
  - Add TODO: `#     # TODO: Build Physical AI-specific prompts`
  - Add TODO: `#     # TODO: Include Physical AI concepts (perception, sensors, vision, signal processing)`
  - Add TODO: `#     # TODO: Use Physical AI analogies (sensors as eyes/ears, signal processing as filtering)`
  - Add TODO: `#     # TODO: Include real-world examples (autonomous vehicles, robotics, drones)`
  - Add TODO: `#     # TODO: Format context with Physical AI-specific instructions`
  - Expected content: TODO comments for Chapter 3 prompt building
  - Dependencies: Existing `build_prompt()` function from Feature 005
  - Acceptance test: Comments added, imports work, no syntax errors

### Update retrieval_skill.py

- [ ] [T025] [P1] [US1] Update `backend/app/ai/skills/retrieval_skill.py` function `retrieve_content()`:
  - Add TODO comment block: `# TODO: Chapter 3 support`
  - Add conditional comment: `# if chapter_id == 3:`
  - Add TODO: `#     # TODO: Use Chapter 3 RAG pipeline`
  - Add TODO: `#     # TODO: from app.ai.rag.ch3_pipeline import run_ch3_rag_pipeline`
  - Add TODO: `#     # TODO: Call run_ch3_rag_pipeline(query, top_k) for Chapter 3`
  - Add TODO: `#     # TODO: Return Chapter 3 chunks with Physical AI metadata`
  - Expected content: TODO comments for Chapter 3 retrieval
  - Dependencies: Existing `retrieve_content()` function from Feature 005, ch3_pipeline.py (from Feature 029)
  - Acceptance test: Comments added, imports work, no syntax errors

### Verify Skills Imports

- [ ] [T026] [P1] [US1] Verify skills files import correctly:
  - Run: `cd backend && python -c "from app.ai.skills.prompt_builder_skill import build_prompt; from app.ai.skills.retrieval_skill import retrieve_content; print('Skills import OK')"`
  - Expected: All imports succeed without errors
  - Dependencies: All updated code in skills files
  - Acceptance test: All imports work, no syntax errors

**Phase Completion**: Skills extended with Chapter 3 TODOs, imports work

---

## PHASE E — Pipeline Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 3

**Test Strategy**: Can be tested by updating ch3_pipeline.py and verifying imports work.

### Add Runtime Engine Integration Comments

- [ ] [T027] [P1] [US1] Update `backend/app/ai/rag/ch3_pipeline.py` function `run_ch3_rag_pipeline()`:
  - Add TODO comment block: `# TODO: Runtime engine integration`
  - Add TODO: `# TODO: Called from engine.py when chapterId=3`
  - Add TODO: `# TODO: Return context for subagents`
  - Add TODO: `# TODO: Format context for Physical AI concepts`
  - Expected content: TODO comments for runtime engine integration
  - Dependencies: Existing `run_ch3_rag_pipeline()` function from Feature 029
  - Acceptance test: Comments added, imports work, no syntax errors

### Verify Pipeline Imports

- [ ] [T028] [P1] [US1] Verify `backend/app/ai/rag/ch3_pipeline.py` imports correctly:
  - Run: `cd backend && python -c "from app.ai.rag.ch3_pipeline import run_ch3_rag_pipeline; print('Pipeline import OK')"`
  - Expected: Import succeeds without errors
  - Dependencies: All updated code in ch3_pipeline.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: Pipeline extended with runtime engine integration comments, imports work

---

## PHASE F — Contract Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 3

**Test Strategy**: Contract already created in specification phase, verify it exists.

### Verify Contract File

- [ ] [T029] [P1] [US1] Verify `specs/030-ch3-ai-runtime/contracts/ch3-ai-runtime.yaml` exists:
  - Check that file contains AI runtime integration contract
  - Check that runtime flow is documented
  - Check that subagent responsibilities are documented
  - Check that placeholder schemas are documented
  - Expected content: Complete contract file with all required documentation
  - Dependencies: Contract file created in spec phase
  - Acceptance test: File exists, contains required documentation

**Phase Completion**: Contract file verified, contains required documentation

---

## PHASE G — Validation Tasks

**Purpose**: Final validation to ensure all scaffolding is in place and backend starts successfully.

### Backend Validation

- [ ] [T030] [P1] [VALIDATION] Verify all imports resolve: Run `cd backend && python -c "from app.api.ai_blocks import router; from app.ai.runtime.engine import run_ai_block; from app.ai.subagents.ch3_ask_question_agent import ch3_ask_question_agent; from app.ai.subagents.ch3_explain_el10_agent import ch3_explain_el10_agent; from app.ai.subagents.ch3_quiz_agent import ch3_quiz_agent; from app.ai.subagents.ch3_diagram_agent import ch3_diagram_agent; from app.ai.skills.prompt_builder_skill import build_prompt; from app.ai.skills.retrieval_skill import retrieve_content; from app.ai.rag.ch3_pipeline import run_ch3_rag_pipeline; print('All imports successful')"` - should complete without errors

- [ ] [T031] [P1] [VALIDATION] Verify backend starts successfully: Run `cd backend && python -c "from app.main import app; print('Backend startup OK')"` - should complete without errors

- [ ] [T032] [P1] [VALIDATION] Verify no syntax errors: Run `cd backend && python -m py_compile app/api/ai_blocks.py app/ai/runtime/engine.py app/ai/subagents/ch3_ask_question_agent.py app/ai/subagents/ch3_explain_el10_agent.py app/ai/subagents/ch3_quiz_agent.py app/ai/subagents/ch3_diagram_agent.py app/ai/skills/prompt_builder_skill.py app/ai/skills/retrieval_skill.py app/ai/rag/ch3_pipeline.py` - should complete without errors

### File Existence Validation

- [ ] [T033] [P1] [VALIDATION] Verify all updated files exist:
  - `backend/app/api/ai_blocks.py` (updated with 4 new endpoints)
  - `backend/app/ai/runtime/engine.py` (updated with Chapter 3 routing)
  - `backend/app/ai/subagents/ch3_ask_question_agent.py` (NEW)
  - `backend/app/ai/subagents/ch3_explain_el10_agent.py` (NEW)
  - `backend/app/ai/subagents/ch3_quiz_agent.py` (NEW)
  - `backend/app/ai/subagents/ch3_diagram_agent.py` (NEW)
  - `backend/app/ai/skills/prompt_builder_skill.py` (updated with Chapter 3 TODOs)
  - `backend/app/ai/skills/retrieval_skill.py` (updated with Chapter 3 TODOs)
  - `backend/app/ai/rag/ch3_pipeline.py` (updated with runtime engine integration)
  - `specs/030-ch3-ai-runtime/contracts/ch3-ai-runtime.yaml` (verified)

### TODO Validation

- [ ] [T034] [P1] [VALIDATION] Verify all functions have TODO comments:
  - `ch3_ask_question()` endpoint has TODO comments
  - `ch3_explain_el10()` endpoint has TODO comments
  - `ch3_quiz()` endpoint has TODO comments
  - `ch3_diagram()` endpoint has TODO comments
  - `run_ai_block()` has Chapter 3 routing TODO comments
  - `ch3_ask_question_agent()` has TODO comments
  - `ch3_explain_el10_agent()` has TODO comments
  - `ch3_quiz_agent()` has TODO comments
  - `ch3_diagram_agent()` has TODO comments
  - `build_prompt()` has Chapter 3 TODO comments
  - `retrieve_content()` has Chapter 3 TODO comments
  - `run_ch3_rag_pipeline()` has runtime engine integration TODO comments

**Acceptance Test**: 
- All imports resolve without errors
- Backend starts successfully
- All files exist and are updated/created
- All functions have appropriate TODO comments
- No real AI logic implemented (only placeholders)
- Contract file exists and contains required documentation

---

## Summary

**Total Tasks**: 34 tasks across 7 phases
- Phase 0 (Setup): 8 tasks
- Phase A (API Routing): 5 tasks
- Phase B (Runtime Engine): 5 tasks
- Phase C (Subagents): 5 tasks
- Phase D (Skills): 3 tasks
- Phase E (Pipeline): 2 tasks
- Phase F (Contract): 1 task (already done)
- Phase G (Validation): 5 tasks

**Estimated Effort**: ~2-3 hours (mostly adding TODO comments, creating new files, and verifying imports)

**Dependencies**: Feature 005 (AI Runtime Engine), Feature 017/020 (Chapter 2 AI Runtime), Feature 028 (Chapter 3 AI Blocks), Feature 029 (Chapter 3 RAG Prep)

**Next Step**: Run `/sp.implement` to execute these tasks

