# Tasks: Chapter 1 Quiz Engine — Question Generator, Validator, and Runtime

**Feature**: 007-ch1-quiz-engine | **Branch**: `007-ch1-quiz-engine` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating quiz engine infrastructure scaffolding (generator, validator, runtime, skills, subagent updates, RAG hooks). All tasks are scaffolding only—no real AI logic implementation.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category**: SETUP (Initial setup), MODULE (Module creation), CONNECT (Integration), VALIDATE (Validation), DOCS (Documentation)

---

## Phase 0: Project Setup & Prerequisites

**Purpose**: Verify dependencies and prepare directory structure before creating modules.

- [ ] [T001] [P1] [SETUP] Verify Feature 005 (AI Runtime Engine) is complete: `backend/app/ai/runtime/engine.py`, `backend/app/ai/rag/pipeline.py`, `backend/app/ai/subagents/quiz_agent.py` exist
- [ ] [T002] [P1] [SETUP] Create directory structure: `backend/app/ai/quiz/`
- [ ] [T003] [P1] [SETUP] Verify backend starts successfully: Run `cd backend && uvicorn app.main:app` to confirm no errors before adding new modules

**Success Criteria**:
- All prerequisite features complete
- Directory structure ready
- Backend starts without errors

**Dependencies**: Feature 005 (AI Runtime Engine) must be complete

---

## 1. Quiz Generator Tasks

**Purpose**: Create quiz generator module with functions for different question types.

- [ ] [T004] [P1] [MODULE] Create `backend/app/ai/quiz/__init__.py` with package initialization
- [ ] [T005] [P1] [MODULE] Create `backend/app/ai/quiz/generator.py` with:
  - Import statements: `from typing import List, Dict, Any`
  - Function `def generate_mcq(learning_outcomes: List[str]) -> List[Dict[str, Any]]` with:
    - Type hints for parameters and return value
    - Docstring: "Generate multiple choice questions from learning outcomes. TODO: Implement MCQ generation using LLM"
    - TODO placeholder: `# TODO: Implement MCQ generation using LLM`
    - Placeholder return: `return []` (empty list)
  - Function `def generate_true_false(learning_outcomes: List[str]) -> List[Dict[str, Any]]` with:
    - Type hints and docstring
    - TODO placeholder: `# TODO: Implement true/false generation using LLM`
    - Placeholder return: `return []`
  - Function `def generate_fill_blank(section_text: str) -> List[Dict[str, Any]]` with:
    - Type hints and docstring
    - TODO placeholder: `# TODO: Implement fill-in-the-blank generation using LLM`
    - Placeholder return: `return []`

**Acceptance Test**: Generator file exists, all three functions defined, imports resolve

---

## 2. Quiz Validator Tasks

**Purpose**: Create quiz validator module for answer validation and scoring.

- [ ] [T006] [P1] [MODULE] Create `backend/app/ai/quiz/validator.py` with:
  - Import statements: `from typing import List, Dict, Any`
  - Function `def validate_answer(user_answer: str, correct_answer: str) -> bool` with:
    - Type hints for parameters and return value
    - Docstring: "Validate user answer against correct answer. TODO: Implement answer validation logic"
    - TODO placeholder: `# TODO: Implement answer validation logic`
    - Placeholder return: `return False`
  - Function `def score_quiz(answers_list: List[Dict[str, Any]]) -> Dict[str, Any]` with:
    - Type hints and docstring
    - TODO placeholder: `# TODO: Implement scoring logic`
    - Placeholder return: `return {}`

**Acceptance Test**: Validator file exists, both functions defined, imports resolve

---

## 3. Quiz Runtime Tasks

**Purpose**: Create quiz runtime orchestrator module.

- [ ] [T007] [P1] [MODULE] Create `backend/app/ai/quiz/runtime.py` with:
  - Import statements: `from typing import Dict, Any`
  - Function `async def run_quiz(chapter_id: int, num_questions: int) -> Dict[str, Any]` with:
    - Type hints for all parameters and return value
    - Docstring explaining orchestration flow
    - Step-by-step TODO comments:
      - `# Step 1: Retrieve chapter chunks (RAG) - TODO`
      - `# Step 2: Extract learning outcomes - TODO`
      - `# Step 3: Generate questions (generator) - TODO`
      - `# Step 4: Format questions (skills) - TODO`
      - `# Step 5: Return structured quiz - TODO`
    - Placeholder return: `return {"questions": [], "chapter_id": chapter_id, "num_questions": num_questions, "metadata": {}}`

**Acceptance Test**: Runtime file exists, function signature correct, imports resolve

---

## 4. RAG Pipeline Update Tasks

**Purpose**: Add TODO hooks in RAG pipeline for quiz context retrieval.

- [ ] [T008] [P1] [CONNECT] Update `backend/app/ai/rag/pipeline.py`:
  - Add TODO comment: `# TODO: retrieve_quiz_context(chapter_id) - Function to retrieve chapter context specifically for quiz generation`
  - Add TODO comment: `# TODO: embed_quiz_query(question_text) - Function to embed quiz question text for context matching`
  - Ensure no breaking changes to existing functionality
  - Verify no syntax errors: Run `python -m py_compile backend/app/ai/rag/pipeline.py`

**Acceptance Test**: RAG pipeline updated, TODO hooks added, no breaking changes, backend starts without errors

---

## 5. Subagent Tasks

**Purpose**: Update quiz agent with generator selection and structured results blueprint.

- [ ] [T009] [P1] [CONNECT] Update `backend/app/ai/subagents/quiz_agent.py`:
  - Add TODO blueprint for generator selection: `# TODO: Implement generator selection logic - Select appropriate generator based on question type distribution`
  - Add TODO blueprint for returning structured results: `# TODO: Call quiz runtime orchestrator and return structured quiz results`
  - Add import comment: `# from app.ai.quiz.runtime import run_quiz`
  - Update function to include TODO call to quiz runtime
  - Maintain existing function signature
  - Verify no syntax errors: Run `python -m py_compile backend/app/ai/subagents/quiz_agent.py`

**Acceptance Test**: Quiz agent updated, generator selection blueprint added, structured results blueprint added, no breaking changes

---

## 6. Skill Tasks

**Purpose**: Create quiz formatting skill module.

- [ ] [T010] [P1] [MODULE] Create `backend/app/ai/skills/quiz_formatting_skill.py` with:
  - Import statements: `from typing import Dict, Any`
  - Function `def format_mcq(question_data: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints and docstring: "Format multiple choice question for frontend. TODO: Implement MCQ formatting"
    - TODO placeholder: `# TODO: Implement MCQ formatting`
    - Placeholder return: `return {}`
  - Function `def format_true_false(question_data: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints and docstring
    - TODO placeholder: `# TODO: Implement true/false formatting`
    - Placeholder return: `return {}`
  - Function `def format_fill_blank(question_data: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints and docstring
    - TODO placeholder: `# TODO: Implement fill-in-the-blank formatting`
    - Placeholder return: `return {}`

**Acceptance Test**: Skill file exists, all three formatting functions defined, imports resolve

---

## 7. API Update Tasks

**Purpose**: Update quiz endpoint to route through quiz runtime.

- [ ] [T011] [P1] [CONNECT] Update `backend/app/api/ai_blocks.py`:
  - Add import: `from app.ai.quiz.runtime import run_quiz`
  - Update `quiz` endpoint:
    - Replace placeholder return with: `result = await run_quiz(request.chapterId, request.numQuestions)`
    - Return: `return AIBlockResponse(**result)` (or handle response format)
    - Add TODO comment: `# TODO: Update response model when real AI logic implemented`
  - Verify no syntax errors: Run `python -m py_compile backend/app/api/ai_blocks.py`

**Acceptance Test**: API endpoint updated, routes to quiz runtime, no breaking changes, backend starts without errors

---

## 8. Contract File Tasks

**Purpose**: Verify API contract documentation exists.

- [ ] [T012] [P2] [DOCS] Verify `specs/007-ch1-quiz-engine/contracts/quiz-runtime.yaml` exists:
  - Check file contains quiz flow documentation
  - Check file contains request/response schemas
  - Check file contains placeholder examples

**Acceptance Test**: Contract file exists and is complete (already created in spec phase)

---

## 9. Documentation Tasks

**Purpose**: Verify all documentation files exist and are complete.

- [ ] [T013] [P2] [DOCS] Verify `specs/007-ch1-quiz-engine/research.md` exists and is complete (already created in spec phase)
- [ ] [T014] [P2] [DOCS] Verify `specs/007-ch1-quiz-engine/quickstart.md` exists and is complete (already created in spec phase)
- [ ] [T015] [P2] [DOCS] Verify `specs/007-ch1-quiz-engine/data-model.md` exists and is complete (already created in spec phase)
- [ ] [T016] [P2] [DOCS] Verify `specs/007-ch1-quiz-engine/checklists/requirements.md` exists and is complete (already created in spec phase)

**Acceptance Test**: All documentation files exist and are complete

---

## 10. Validation Tasks

**Purpose**: Verify all modules exist, imports resolve, and backend works correctly.

### File Existence Validation

- [ ] [T017] [P1] [VALIDATE] Verify quiz generator file exists:
  - Check `backend/app/ai/quiz/generator.py` exists

- [ ] [T018] [P1] [VALIDATE] Verify quiz validator file exists:
  - Check `backend/app/ai/quiz/validator.py` exists

- [ ] [T019] [P1] [VALIDATE] Verify quiz runtime file exists:
  - Check `backend/app/ai/quiz/runtime.py` exists

- [ ] [T020] [P1] [VALIDATE] Verify quiz formatting skill file exists:
  - Check `backend/app/ai/skills/quiz_formatting_skill.py` exists

### Import Resolution Validation

- [ ] [T021] [P1] [VALIDATE] Test quiz generator imports:
  - Run: `python -c "from app.ai.quiz.generator import generate_mcq, generate_true_false, generate_fill_blank; print('OK')"`

- [ ] [T022] [P1] [VALIDATE] Test quiz validator imports:
  - Run: `python -c "from app.ai.quiz.validator import validate_answer, score_quiz; print('OK')"`

- [ ] [T023] [P1] [VALIDATE] Test quiz runtime import:
  - Run: `python -c "from app.ai.quiz.runtime import run_quiz; print('OK')"`

- [ ] [T024] [P1] [VALIDATE] Test quiz formatting skill import:
  - Run: `python -c "from app.ai.skills.quiz_formatting_skill import format_mcq, format_true_false, format_fill_blank; print('OK')"`

### Backend Startup Validation

- [ ] [T025] [P1] [VALIDATE] Start backend server: Run `cd backend && uvicorn app.main:app --reload`
  - Verify: Server starts without ImportError
  - Verify: Server starts without ModuleNotFoundError
  - Verify: Server starts without syntax errors
  - Verify: Health endpoint responds: `curl http://localhost:8000/health`

- [ ] [T026] [P1] [VALIDATE] Test API endpoint routes correctly:
  - Test `POST /api/ai/quiz` with `{"chapterId": 1, "numQuestions": 5}`
  - Verify: Endpoint responds (even if placeholder response)
  - Verify: No 500 Internal Server Error
  - Verify: Response format is valid JSON

### Module Dependency Validation

- [ ] [T027] [P1] [VALIDATE] Verify no circular imports:
  - Check all imports are forward references or top-level
  - Verify quiz runtime imports generator/validator without circular dependency

- [ ] [T028] [P1] [VALIDATE] Verify all TODO placeholders present:
  - Check all functions contain TODO comments
  - Check all modules have docstrings explaining purpose
  - Verify no real AI logic (no LLM calls, no quiz generation)

### Folder Structure Validation

- [ ] [T029] [P1] [VALIDATE] Verify folder structure:
  - Check `backend/app/ai/quiz/` directory exists
  - Check `backend/app/ai/quiz/__init__.py` exists
  - Check all required files exist at specified paths

---

## Task Summary

**Total Tasks**: 29 tasks
- **Phase 0 (Setup)**: 3 tasks
- **1. Quiz Generator**: 2 tasks
- **2. Quiz Validator**: 1 task
- **3. Quiz Runtime**: 1 task
- **4. RAG Pipeline Update**: 1 task
- **5. Subagent**: 1 task
- **6. Skill**: 1 task
- **7. API Update**: 1 task
- **8. Contract File**: 1 task
- **9. Documentation**: 4 tasks
- **10. Validation**: 13 tasks

**Critical Path**: T001-T003 → T004-T005 → T006 → T007 → T008 → T009 → T010 → T011 → T012-T016 → T017-T029

**Estimated Time**: 2-3 hours (file creation + function signatures + imports + validation)

---

## Success Criteria Validation

### Spec Success Criteria → Task Mapping

| Success Criteria | Task IDs | Validation Method |
|------------------|----------|-------------------|
| **SC-001**: All scaffold modules exist | T017-T020 | File existence checks |
| **SC-002**: No real AI logic | T028 | Code review |
| **SC-003**: Backend starts successfully | T025 | Backend startup test |
| **SC-004**: API integration complete | T011, T026 | Endpoint routing test |
| **SC-005**: Documentation complete | T012-T016 | File existence |

---

## Dependencies & Risks

### Internal Dependencies
- ✅ Feature 005 (AI Runtime Engine) complete

### External Dependencies
- ✅ Python 3.11+, FastAPI 0.109+, Pydantic 2.x (already installed)
- ✅ No new runtime dependencies required (scaffolding only)

### Risks & Mitigations

**Risk 1**: Import resolution failures
- **Mitigation**: Test imports incrementally (T021-T024), fix errors immediately

**Risk 2**: Breaking Feature 005 compatibility
- **Mitigation**: Update files carefully (T008, T009, T011), test existing endpoints after update

**Risk 3**: Missing __init__.py files
- **Mitigation**: Create all __init__.py files in Phase 0 (T004)

**Risk 4**: Circular import issues
- **Mitigation**: Validate dependencies (T027), use forward references if needed

---

**Task Generation Complete**: 2025-12-05
**Ready for Implementation**: Yes ✅
**Next Command**: `/sp.implement` (or manual task-by-task execution)

