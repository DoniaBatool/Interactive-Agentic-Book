# Tasks: Chapter 2 — AI Blocks Integration Layer

**Feature**: 034-chapter-2-ai-blocks | **Branch**: `034-chapter-2-ai-blocks` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for connecting Chapter 2's AI Blocks to the global AI Runtime Engine (scaffolding only, no real AI logic).

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

**Purpose**: Verify dependencies and prerequisites before implementing Chapter 2 runtime engine integration scaffolding.

- [ ] [T001] [P1] [SETUP] Verify Feature 005 is complete: Check that `backend/app/ai/runtime/engine.py` exists with runtime engine structure
- [ ] [T002] [P1] [SETUP] Verify Feature 033 is complete: Check that `backend/app/content/chapters/chapter_2.py` exists with Chapter 2 metadata
- [ ] [T003] [P1] [SETUP] Verify Feature 030 is complete: Check that Chapter 3 runtime patterns exist for reference
- [ ] [T004] [P1] [SETUP] Verify API file exists: Check that `backend/app/api/ai_blocks.py` exists
- [ ] [T005] [P1] [SETUP] Verify skills exist: Check that `backend/app/ai/skills/prompt_builder_skill.py` and `formatting_skill.py` exist
- [ ] [T006] [P1] [SETUP] Verify subagents directory exists: Check that `backend/app/ai/subagents/` directory exists
- [ ] [T007] [P1] [SETUP] Verify RAG pipeline exists: Check that `backend/app/ai/rag/pipeline.py` exists
- [ ] [T008] [P1] [SETUP] Verify backend imports work: Run `cd backend && python -c "from app.main import app; print('Backend imports OK')"` - should complete without errors

**Success Criteria**:
- All prerequisite files exist
- Backend imports resolve without errors
- Ready to implement scaffolding

**Dependencies**: Feature 005 (AI Runtime Engine), Feature 033 (Chapter 2 Content), Feature 030 (Chapter 3 AI Runtime for reference)

---

## PHASE A — API Routing Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by adding Chapter 2 endpoints and verifying imports work.

### Add Chapter 2 Ask Endpoint

- [ ] [T009] [P1] [US1] Add `POST /ai/ch2/ask` endpoint to `backend/app/api/ai_blocks.py`:
  - Add endpoint function: `async def ch2_ask(request: AskQuestionRequest) -> AIBlockResponse:`
  - Add docstring explaining Chapter 2 ask-question endpoint
  - Add TODO comment: `# TODO: Chapter 2 ask-question routing`
  - Ensure request includes `chapterId=2`: `request_data = request.model_dump(); request_data["chapterId"] = 2`
  - Add call: `result = await run_ai_block("ask-question", request_data)`
  - Add placeholder return: `return AIBlockResponse(message="AI block placeholder", received=request_data)`
  - Expected content: New endpoint that routes to runtime engine with chapterId=2
  - Dependencies: Existing `run_ai_block()` function, `AskQuestionRequest` model
  - Acceptance test: Endpoint exists, imports work, no syntax errors

### Add Chapter 2 Explain Endpoint

- [ ] [T010] [P1] [US1] Add `POST /ai/ch2/explain` endpoint to `backend/app/api/ai_blocks.py`:
  - Add endpoint function: `async def ch2_explain(request: ExplainLike10Request) -> AIBlockResponse:`
  - Add docstring explaining Chapter 2 explain-el10 endpoint
  - Add TODO comment: `# TODO: Chapter 2 explain-like-i-am-10 routing`
  - Ensure request includes `chapterId=2`: `request_data = request.model_dump(); request_data["chapterId"] = 2`
  - Add call: `result = await run_ai_block("explain-like-i-am-10", request_data)`
  - Add placeholder return: `return AIBlockResponse(message="AI block placeholder", received=request_data)`
  - Expected content: New endpoint that routes to runtime engine with chapterId=2
  - Dependencies: Existing `run_ai_block()` function, `ExplainLike10Request` model
  - Acceptance test: Endpoint exists, imports work, no syntax errors

### Add Chapter 2 Quiz Endpoint

- [ ] [T011] [P1] [US1] Add `POST /ai/ch2/quiz` endpoint to `backend/app/api/ai_blocks.py`:
  - Add endpoint function: `async def ch2_quiz(request: QuizRequest) -> AIBlockResponse:`
  - Add docstring explaining Chapter 2 quiz endpoint
  - Add TODO comment: `# TODO: Chapter 2 interactive-quiz routing`
  - Ensure request includes `chapterId=2`: `request_data = request.model_dump(); request_data["chapterId"] = 2`
  - Add call: `result = await run_ai_block("interactive-quiz", request_data)`
  - Add placeholder return: `return AIBlockResponse(message="AI block placeholder", received=request_data)`
  - Expected content: New endpoint that routes to runtime engine with chapterId=2
  - Dependencies: Existing `run_ai_block()` function, `QuizRequest` model
  - Acceptance test: Endpoint exists, imports work, no syntax errors

### Add Chapter 2 Diagram Endpoint

- [ ] [T012] [P1] [US1] Add `POST /ai/ch2/diagram` endpoint to `backend/app/api/ai_blocks.py`:
  - Add endpoint function: `async def ch2_diagram(request: DiagramRequest) -> AIBlockResponse:`
  - Add docstring explaining Chapter 2 diagram endpoint
  - Add TODO comment: `# TODO: Chapter 2 generate-diagram routing`
  - Ensure request includes `chapterId=2`: `request_data = request.model_dump(); request_data["chapterId"] = 2`
  - Add call: `result = await run_ai_block("generate-diagram", request_data)`
  - Add placeholder return: `return AIBlockResponse(message="AI block placeholder", received=request_data)`
  - Expected content: New endpoint that routes to runtime engine with chapterId=2
  - Dependencies: Existing `run_ai_block()` function, `DiagramRequest` model
  - Acceptance test: Endpoint exists, imports work, no syntax errors

### Verify API Imports

- [ ] [T013] [P1] [US1] Verify `backend/app/api/ai_blocks.py` imports correctly:
  - Run: `cd backend && python -c "from app.api.ai_blocks import router; print('API imports OK')"`
  - Expected: Import succeeds without errors
  - Dependencies: All updated code in ai_blocks.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: All 4 Chapter 2 API endpoints added, imports work

---

## PHASE B — Runtime Engine Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by updating runtime engine and verifying imports work.

### Add Chapter 2 Routing Logic

- [ ] [T014] [P1] [US1] Update `backend/app/ai/runtime/engine.py` function `run_ai_block()`:
  - Add TODO comment block: `# TODO: Chapter 2 routing`
  - Add code: `chapter_id = request_data.get("chapterId", 1)` (if not already present)
  - Add conditional: `if chapter_id == 2:`
  - Add TODO: `#     # TODO: Route to Chapter 2 subagent`
  - Add TODO: `#     # TODO: Call pipeline with chapter_id=2 for RAG context`
  - Add TODO: `#     # TODO: Select provider for Chapter 2`
  - Add TODO: `#     # TODO: Call appropriate Chapter 2 subagent`
  - Add TODO: `#     # TODO: Format response`
  - Expected content: Chapter 2 routing logic with TODO comments
  - Dependencies: Existing `run_ai_block()` function from Feature 005
  - Acceptance test: Code added, imports work, no syntax errors

### Add Chapter 2 RAG Integration Comments

- [ ] [T015] [P1] [US1] Add Chapter 2 RAG integration comments to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Import pipeline for Chapter 2 RAG operations`
  - Add TODO comment: `# TODO: from app.ai.rag.pipeline import run_rag_pipeline`
  - Add TODO comment: `# TODO: Use run_rag_pipeline(query, chapter_id=2) when chapter_id=2`
  - Add TODO comment: `# TODO: Pass RAG context to Chapter 2 subagents`
  - Expected content: TODO comments for Chapter 2 RAG integration
  - Dependencies: pipeline.py (from Feature 005)
  - Acceptance test: Comments added, no syntax errors

### Add Chapter 2 Subagent Routing Comments

- [ ] [T016] [P1] [US1] Add Chapter 2 subagent routing comments to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Import Chapter 2 subagents`
  - Add TODO comment: `# TODO: from app.ai.subagents.ch2_ask_agent import Ch2AskAgent`
  - Add TODO comment: `# TODO: from app.ai.subagents.ch2_explain_agent import Ch2ExplainAgent`
  - Add TODO comment: `# TODO: from app.ai.subagents.ch2_quiz_agent import Ch2QuizAgent`
  - Add TODO comment: `# TODO: from app.ai.subagents.ch2_diagram_agent import Ch2DiagramAgent`
  - Add TODO comment: `# TODO: CH2_SUBAGENT_MAP = {"ask-question": Ch2AskAgent(), "explain-like-i-am-10": Ch2ExplainAgent(), "interactive-quiz": Ch2QuizAgent(), "generate-diagram": Ch2DiagramAgent()}`
  - Expected content: TODO comments for Chapter 2 subagent routing
  - Dependencies: Chapter 2 subagent files (from Phase C)
  - Acceptance test: Comments added, no syntax errors

### Add Chapter 2 Provider Selection Comments

- [ ] [T017] [P1] [US1] Add Chapter 2 provider selection comments to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Select provider for Chapter 2`
  - Add TODO comment: `# TODO: Use settings.ch2_llm_model for Chapter 2 (if configured)`
  - Add TODO comment: `# TODO: Fallback to default provider if Chapter 2 model not configured`
  - Expected content: TODO comments for Chapter 2 provider selection
  - Dependencies: settings.py (for Chapter 2 model configuration)
  - Acceptance test: Comments added, no syntax errors

### Verify Engine Imports

- [ ] [T018] [P1] [US1] Verify `backend/app/ai/runtime/engine.py` imports correctly:
  - Run: `cd backend && python -c "from app.ai.runtime.engine import run_ai_block; print('Engine import OK')"`
  - Expected: Import succeeds without errors
  - Dependencies: All updated code in engine.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: Runtime engine extended with Chapter 2 routing logic, imports work

---

## PHASE C — Subagent Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by creating subagent files and verifying imports work.

### Create ch2_ask_agent.py

- [ ] [T019] [P1] [US1] Create `backend/app/ai/subagents/ch2_ask_agent.py`:
  - Add module docstring: `"""Chapter 2 Ask Question Agent - Specialized agent for answering questions about Mechanical Systems concepts using Chapter 2 context."""`
  - Add class: `class Ch2AskAgent:`
  - Add method: `def run(self, input: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Expected input/output signatures
    - Agent flow comments (5 steps: retrieve → build prompt → call LLM → format → return)
    - Mechanical Systems-specific considerations
  - Add TODO comments for each step
  - Add placeholder return: `return {"answer": "", "sources": [], "confidence": 0.0}`
  - Expected content: Complete subagent file with class structure
  - Dependencies: `typing` module (Dict, Any)
  - Acceptance test: File exists, imports work, class is instantiable

### Create ch2_explain_agent.py

- [ ] [T020] [P1] [US1] Create `backend/app/ai/subagents/ch2_explain_agent.py`:
  - Add module docstring: `"""Chapter 2 Explain Like I'm 10 Agent - Specialized agent for explaining Mechanical Systems concepts in simple terms using Chapter 2 context."""`
  - Add class: `class Ch2ExplainAgent:`
  - Add method: `def run(self, input: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Expected input/output signatures
    - Agent flow comments (5 steps: retrieve → build prompt → call LLM → format → return)
    - Mechanical Systems-specific considerations
  - Add TODO comments for each step
  - Add placeholder return: `return {"explanation": "", "examples": [], "analogies": []}`
  - Expected content: Complete subagent file with class structure
  - Dependencies: `typing` module (Dict, Any)
  - Acceptance test: File exists, imports work, class is instantiable

### Create ch2_quiz_agent.py

- [ ] [T021] [P1] [US1] Create `backend/app/ai/subagents/ch2_quiz_agent.py`:
  - Add module docstring: `"""Chapter 2 Quiz Agent - Specialized agent for generating quiz questions about Mechanical Systems using Chapter 2 context."""`
  - Add class: `class Ch2QuizAgent:`
  - Add method: `def run(self, input: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Expected input/output signatures
    - Agent flow comments (5 steps: retrieve → build prompt → call LLM → format → return)
    - Mechanical Systems-specific considerations
  - Add TODO comments for each step
  - Add placeholder return: `return {"questions": [], "learning_objectives": []}`
  - Expected content: Complete subagent file with class structure
  - Dependencies: `typing` module (Dict, Any)
  - Acceptance test: File exists, imports work, class is instantiable

### Create ch2_diagram_agent.py

- [ ] [T022] [P1] [US1] Create `backend/app/ai/subagents/ch2_diagram_agent.py`:
  - Add module docstring: `"""Chapter 2 Diagram Agent - Specialized agent for generating diagrams for Mechanical Systems concepts using Chapter 2 context."""`
  - Add class: `class Ch2DiagramAgent:`
  - Add method: `def run(self, input: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Expected input/output signatures
    - Agent flow comments (5 steps: retrieve → build prompt → call LLM → format → return)
    - Mechanical Systems-specific considerations
  - Add TODO comments for each step
  - Add placeholder return: `return {"diagram_url": "", "metadata": {}}`
  - Expected content: Complete subagent file with class structure
  - Dependencies: `typing` module (Dict, Any)
  - Acceptance test: File exists, imports work, class is instantiable

### Verify Subagent Imports

- [ ] [T023] [P1] [US1] Verify all Chapter 2 subagent files import correctly:
  - Run: `cd backend && python -c "from app.ai.subagents.ch2_ask_agent import Ch2AskAgent; from app.ai.subagents.ch2_explain_agent import Ch2ExplainAgent; from app.ai.subagents.ch2_quiz_agent import Ch2QuizAgent; from app.ai.subagents.ch2_diagram_agent import Ch2DiagramAgent; print('Subagent imports OK')"`
  - Expected: All imports succeed without errors
  - Dependencies: All subagent files created
  - Acceptance test: All imports work, no syntax errors

**Phase Completion**: All 4 Chapter 2 subagent files created, imports work

---

## PHASE D — Skills Layer Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by updating skills files and verifying imports work.

### Update Prompt Builder Skill

- [ ] [T024] [P1] [US1] Update `backend/app/ai/skills/prompt_builder_skill.py`:
  - Add TODO comment block: `# TODO: Chapter 2 prompt building functions`
  - Add TODO function: `# def build_ask_prompt_ch2(question: str, context: List[Dict[str, Any]]) -> str:`
  - Add TODO comment: `#     # TODO: Build Mechanical Systems ask prompt with Chapter 2 context`
  - Add TODO function: `# def build_explain_prompt_ch2(concept: str, context: List[Dict[str, Any]]) -> str:`
  - Add TODO comment: `#     # TODO: Build Mechanical Systems explain prompt with Chapter 2 context`
  - Add TODO function: `# def build_quiz_prompt_ch2(num_questions: int, context: List[Dict[str, Any]]) -> str:`
  - Add TODO comment: `#     # TODO: Build Mechanical Systems quiz prompt with Chapter 2 context`
  - Add TODO function: `# def build_diagram_prompt_ch2(diagram_type: str, concepts: List[str], context: List[Dict[str, Any]]) -> str:`
  - Add TODO comment: `#     # TODO: Build Mechanical Systems diagram prompt with Chapter 2 context`
  - Expected content: TODO comments for Chapter 2 prompt building functions
  - Dependencies: Existing prompt_builder_skill.py from Feature 005
  - Acceptance test: Comments added, imports work, no syntax errors

### Update Formatting Skill

- [ ] [T025] [P1] [US1] Update `backend/app/ai/skills/formatting_skill.py`:
  - Add TODO comment block: `# TODO: Chapter 2 formatting functions`
  - Add TODO function: `# def format_ask_response_ch2(raw_response: Dict[str, Any]) -> Dict[str, Any]:`
  - Add TODO comment: `#     # TODO: Format ask response for Chapter 2`
  - Add TODO function: `# def format_explain_response_ch2(raw_response: Dict[str, Any]) -> Dict[str, Any]:`
  - Add TODO comment: `#     # TODO: Format explain response for Chapter 2`
  - Add TODO function: `# def format_quiz_response_ch2(raw_response: Dict[str, Any]) -> Dict[str, Any]:`
  - Add TODO comment: `#     # TODO: Format quiz response for Chapter 2`
  - Add TODO function: `# def format_diagram_response_ch2(raw_response: Dict[str, Any]) -> Dict[str, Any]:`
  - Add TODO comment: `#     # TODO: Format diagram response for Chapter 2`
  - Expected content: TODO comments for Chapter 2 formatting functions
  - Dependencies: Existing formatting_skill.py from Feature 005
  - Acceptance test: Comments added, imports work, no syntax errors

### Verify Skills Imports

- [ ] [T026] [P1] [US1] Verify skills files import correctly:
  - Run: `cd backend && python -c "from app.ai.skills.prompt_builder_skill import *; from app.ai.skills.formatting_skill import *; print('Skills imports OK')"`
  - Expected: All imports succeed without errors
  - Dependencies: All updated skills files
  - Acceptance test: All imports work, no syntax errors

**Phase Completion**: Skills files updated with Chapter 2 TODOs, imports work

---

## PHASE E — RAG Integration Tasks

**User Story**: US1 - Developer Extends AI Runtime for Chapter 2

**Test Strategy**: Can be tested by updating RAG pipeline and verifying imports work.

### Add Chapter 2 Routing to RAG Pipeline

- [ ] [T027] [P1] [US1] Update `backend/app/ai/rag/pipeline.py`:
  - Add TODO comment block: `# TODO: Chapter 2 RAG routing`
  - Add conditional: `if chapter_id == 2:`
  - Add TODO comment: `#     # TODO: Load chapter_2_chunks`
  - Add TODO comment: `#     # TODO: from app.content.chapters.chapter_2_chunks import get_chapter_chunks`
  - Add TODO comment: `#     # TODO: chunks = get_chapter_chunks(chapter_id=2)`
  - Add TODO comment: `#     # TODO: Embed query for Chapter 2`
  - Add TODO comment: `#     # TODO: Search Chapter 2 collection in Qdrant`
  - Add TODO comment: `#     # TODO: Return Chapter 2 context`
  - Expected content: TODO comments for Chapter 2 RAG routing
  - Dependencies: Existing pipeline.py from Feature 005
  - Acceptance test: Comments added, imports work, no syntax errors

### Verify RAG Pipeline Imports

- [ ] [T028] [P1] [US1] Verify `backend/app/ai/rag/pipeline.py` imports correctly:
  - Run: `cd backend && python -c "from app.ai.rag.pipeline import *; print('RAG pipeline imports OK')"`
  - Expected: Import succeeds without errors
  - Dependencies: All updated code in pipeline.py
  - Acceptance test: Import works, no syntax errors

**Phase Completion**: RAG pipeline updated with Chapter 2 routing comments, imports work

---

## PHASE F — Validation Tasks

**User Story**: US2 - System Administrator Verifies Chapter 2 Routing

**Test Strategy**: Can be tested by verifying all files exist, imports work, and backend starts.

### Verify All Files Exist

- [ ] [T029] [P1] [US2] Verify all required files exist:
  - Check: `backend/app/api/ai_blocks.py` (updated with 4 endpoints)
  - Check: `backend/app/ai/runtime/engine.py` (updated with Chapter 2 routing)
  - Check: `backend/app/ai/subagents/ch2_ask_agent.py` (exists)
  - Check: `backend/app/ai/subagents/ch2_explain_agent.py` (exists)
  - Check: `backend/app/ai/subagents/ch2_quiz_agent.py` (exists)
  - Check: `backend/app/ai/subagents/ch2_diagram_agent.py` (exists)
  - Check: `backend/app/ai/skills/prompt_builder_skill.py` (updated with Chapter 2 TODOs)
  - Check: `backend/app/ai/skills/formatting_skill.py` (updated with Chapter 2 TODOs)
  - Check: `backend/app/ai/rag/pipeline.py` (updated with Chapter 2 routing)
  - Expected: All files exist at specified paths
  - Dependencies: All previous phases complete
  - Acceptance test: All files exist, no missing files

### Verify Backend Starts

- [ ] [T030] [P1] [US2] Verify backend starts without errors:
  - Run: `cd backend && python -m uvicorn app.main:app --reload --port 8000`
  - Expected: Backend starts successfully, no import errors, no runtime exceptions
  - Dependencies: All files created and updated
  - Acceptance test: Backend starts, no errors in logs

### Verify API Endpoints Registered

- [ ] [T031] [P1] [US2] Verify all Chapter 2 API endpoints are registered:
  - Check backend logs or API documentation for:
    - `POST /ai/ch2/ask`
    - `POST /ai/ch2/explain`
    - `POST /ai/ch2/quiz`
    - `POST /ai/ch2/diagram`
  - Expected: All 4 endpoints appear in API router
  - Dependencies: Backend running, API file updated
  - Acceptance test: All endpoints registered, accessible

### Verify Contract File Exists

- [ ] [T032] [P1] [US2] Verify contract file exists:
  - Check: `specs/034-chapter-2-ai-blocks/contracts/ai-block-runtime.yaml` exists
  - Expected: Contract file exists and documents runtime flow
  - Dependencies: Spec phase complete
  - Acceptance test: Contract file exists, readable

**Phase Completion**: All validation tasks complete, backend ready for future AI implementation

---

## Summary

**Total Tasks**: 32 tasks across 6 phases
**Estimated Time**: 1-2 hours (scaffolding only, no business logic)
**Complexity**: Low (following existing patterns, no new logic)

**Success Criteria**:
- ✅ All Chapter 2 AI routes exist and run without import errors
- ✅ Runtime engine handles chapter_id=2 paths with placeholder flow
- ✅ Subagents + skills updated with TODO blocks
- ✅ RAG pipeline aware of chapter_2
- ✅ Contract file exists and documents the runtime
- ✅ Backend starts successfully without errors

**Next Steps**: Proceed to `/sp.implement` to execute all tasks in order.

