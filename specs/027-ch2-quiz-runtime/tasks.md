# Tasks: Chapter 2 — Interactive Quiz Runtime Engine

**Feature**: 027-ch2-quiz-runtime | **Branch**: `027-ch2-quiz-runtime` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating Chapter 2 quiz generation runtime infrastructure scaffolding (runtime module, prompt template, routing, skills, knowledge source, API integration). All tasks are scaffolding only—no real AI logic implementation.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category`: SETUP (Initial setup), RUNTIME (Runtime module), PROMPT (Prompt template), ROUTING (Routing integration), API (API integration), SKILLS (Skills module), KNOWLEDGE (Knowledge source), VALIDATE (Validation), DOCS (Documentation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before creating Chapter 2 quiz runtime scaffolding.

- [ ] [T001] [P1] [SETUP] Verify Feature 026 (Chapter 2 ELI10 Runtime) exists: Check that `backend/app/ai/explain/ch2_el10_runtime.py` exists and is importable (for reference structure)
- [ ] [T002] [P1] [SETUP] Verify Feature 024 (Chapter 2 Backend Runtime Wiring) exists: Check that `backend/app/ai/runtime/engine.py` has Chapter 2 routing structure
- [ ] [T003] [P1] [SETUP] Verify API layer exists: Check that `backend/app/api/ai_blocks.py` exists and has quiz endpoint
- [ ] [T004] [P1] [SETUP] Verify skills layer exists: Check that `backend/app/ai/skills/prompt_builder_skill.py` and `formatting_skill.py` exist
- [ ] [T005] [P1] [SETUP] Verify backend starts successfully: Run `cd backend && uvicorn app.main:app` to confirm server starts without errors
- [ ] [T006] [P1] [SETUP] Verify quiz directory exists: Check that `backend/app/ai/quiz/` directory exists (create if needed)
- [ ] [T007] [P1] [SETUP] Verify Chapter 2 chunks file exists: Check that `backend/app/content/chapters/chapter_2_chunks.py` exists

**Success Criteria**:
- All required files and directories exist
- Backend starts without errors
- All imports resolve correctly

**Dependencies**: Feature 026 (Chapter 2 ELI10 Runtime) and Feature 024 (Chapter 2 Backend Runtime Wiring) must be complete

---

## PHASE 1 — Quiz Runtime Module

**User Story**: US1 - Developer Sets Up Chapter 2 Quiz Runtime Infrastructure

**Test Strategy**: Can be tested by verifying runtime module exists, function signature is correct, and all 6 steps have TODO markers.

### Runtime Module Creation

- [ ] [T008] [P1] [RUNTIME] Create `backend/app/ai/quiz/ch2_quiz_runtime.py`:
  - Add module docstring: `"""Chapter 2 Interactive Quiz Runtime - Orchestrates quiz generation flow for ROS 2 concepts"""`
  - Import statements: `from typing import List, Dict, Any, Optional`
  - Function definition: `async def run(chapter_id: int, num_questions: int, learning_objectives: Optional[List[str]] = None) -> Dict[str, Any]:`
  - Function docstring explaining:
    - Args: chapter_id (should be 2), num_questions (number of questions to generate), learning_objectives (optional list)
    - Returns: Dictionary with structured quiz (questions, learning_objectives, metadata)
    - Pipeline steps (all TODO): Validate → Build Prompt → Retrieve Context → Call RAG → Call LLM → Format
  - Add 6-step pipeline blueprint (all TODO):
    1. `# Step 1: Validate request (TODO)`
       - `# TODO: Check chapter_id is 2`
       - `# TODO: Validate num_questions is positive integer`
       - `# TODO: Validate learning_objectives structure if provided`
       - `# TODO: Check learning_objectives are valid ROS 2 concepts`
    2. `# Step 2: Build prompt (placeholder)`
       - `# TODO: Load ch2_quiz_prompt.txt template`
       - `# TODO: Replace template variables ({{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}})`
       - `# TODO: Call build_quiz_prompt_ch2() from prompt_builder_skill`
    3. `# Step 3: Retrieve chapter context (placeholder)`
       - `# TODO: Call get_chapter2_quiz_chunks() from chapter_2_chunks`
       - `# TODO: Filter chunks by learning_objectives if provided`
       - `# TODO: Prepare context for RAG pipeline`
    4. `# Step 4: Call RAG pipeline (placeholder)`
       - `# TODO: Retrieve Chapter 2 context chunks for quiz generation`
       - `# TODO: Use RAG pipeline to get relevant ROS 2 content`
       - `# TODO: Combine context with prompt`
    5. `# Step 5: Call LLM provider (placeholder)`
       - `# TODO: Call LLM provider with prompt and context`
       - `# TODO: Generate quiz questions using LLM reasoning`
       - `# TODO: Ensure questions cover learning_objectives`
    6. `# Step 6: Format output (placeholder)`
       - `# TODO: Call format_quiz_output_ch2() from formatting_skill`
       - `# TODO: Format questions, answers, learning_objectives`
       - `# TODO: Add ROS 2-specific metadata`
  - Placeholder return: `return {"questions": [], "learning_objectives": [], "metadata": {}}`
  - Add TODO comment: `# TODO: Implement orchestration logic`
  - Add TODO comment: `# TODO: Add error handling for each step`
  - Add TODO comment: `# TODO: Add logging for quiz generation flow`
  - Add TODO comment: `# TODO: Add future adaptive difficulty support`

- [ ] [T009] [P1] [RUNTIME] Verify ch2_quiz_runtime.py is importable: Run `cd backend && python -c "from app.ai.quiz.ch2_quiz_runtime import run; print('Import successful')"` - should complete without errors

- [ ] [T010] [P2] [RUNTIME] Verify ch2_quiz_runtime.py structure matches ch2_el10_runtime.py (Chapter 2):
  - Compare function signatures
  - Compare return type structure
  - Ensure parity in structure (same 6-step pipeline pattern with additional context retrieval step)

**Acceptance Test**: Runtime file exists, function signature correct, all 6 steps have TODO markers, imports resolve, no real logic implementation

---

## PHASE 2 — Prompt Template

**User Story**: US1 - Developer Sets Up Chapter 2 Quiz Runtime Infrastructure

**Test Strategy**: Can be tested by verifying prompt template file exists, contains all 4 variables, and has TODO comments.

### Prompt Template Creation

- [ ] [T011] [P1] [PROMPT] Create directory structure if needed: `backend/app/ai/prompts/quiz/` (create if doesn't exist)

- [ ] [T012] [P1] [PROMPT] Create `backend/app/ai/prompts/quiz/ch2_quiz_prompt.txt`:
  - Add header comment: `# TODO: Engineer full quiz prompt template for Chapter 2`
  - Add template variables section:
    - `# Template variables:`
    - `# - {{chapter_id}} - Chapter identifier (should be 2)`
    - `# - {{num_questions}} - Number of questions to generate`
    - `# - {{learning_objectives}} - Learning objectives to cover (e.g., "topics", "nodes", "services", "actions")`
    - `# - {{context}} - RAG context chunks for quiz generation`
  - Add TODO comments for future difficulty-level tuning:
    - `# TODO: Add system instructions for quiz generation`
    - `# TODO: Add context placeholders for RAG chunks`
    - `# TODO: Add ROS 2-specific quiz question examples`
    - `# TODO: Add structured output format instructions (questions, answers, learning_objectives)`
    - `# TODO: Add difficulty-level tuning guidelines (beginner, intermediate, advanced)`
    - `# TODO: Include ROS 2 examples (TurtleBot 3, navigation stack, robot arm control)`
    - `# TODO: Add question type variety (multiple choice, true/false, short answer)`
  - Add placeholder template structure (can be minimal, just showing variable usage)

- [ ] [T013] [P1] [PROMPT] Verify ch2_quiz_prompt.txt is readable: Check that file exists and can be read by Python `open()` function

**Acceptance Test**: Prompt template file exists, all 4 variables are present, TODO comments are present, file is readable

---

## PHASE 3 — Runtime Engine Routing

**User Story**: US2 - System Routes Chapter 2 Quiz Requests

**Test Strategy**: Can be tested by verifying runtime engine has Chapter 2 quiz routing comments and TODO markers.

### Runtime Engine Updates

- [ ] [T014] [P1] [ROUTING] Update `backend/app/ai/runtime/engine.py` with Chapter 2 quiz routing:
  - Locate `run_ai_block()` function
  - Add routing case (comments only, before existing quiz routing if present):
    ```python
    # TODO: Chapter 2 quiz routing
    # if block_type == "interactive-quiz" AND chapterId == 2:
    #     from app.ai.quiz.ch2_quiz_runtime import run as ch2_quiz_run
    #     result = await ch2_quiz_run(
    #         chapter_id=2,
    #         num_questions=request_data.get("numQuestions", 5),
    #         learning_objectives=request_data.get("learningObjectives")
    #     )
    #     return result
    ```
  - Ensure routing condition checks both `block_type == "interactive-quiz"` AND `chapterId == 2`
  - Add comment explaining: `# Routes Chapter 2 quiz requests to ch2_quiz_runtime (placeholder routing)`

- [ ] [T015] [P1] [ROUTING] Verify engine.py still imports correctly: Run `cd backend && python -c "from app.ai.runtime.engine import run_ai_block; print('Import successful')"` - should complete without errors

- [ ] [T016] [P2] [ROUTING] Verify routing structure matches Chapter 2 ELI10 routing pattern:
  - Compare routing condition format
  - Ensure comment-only approach matches Feature 026 pattern

**Acceptance Test**: Routing condition checks both block_type and chapterId, routing is comment-only, TODO comments are present, file still imports correctly

---

## PHASE 4 — API Layer Update

**User Story**: US2 - System Routes Chapter 2 Quiz Requests

**Test Strategy**: Can be tested by verifying quiz endpoint has Chapter 2 routing comments and supports chapterId=2.

### API Layer Updates

- [ ] [T017] [P1] [API] Update `backend/app/api/ai_blocks.py` with Chapter 2 quiz routing:
  - Locate `quiz()` endpoint function
  - Add Chapter 2 routing comment (before existing quiz logic if present):
    ```python
    # TODO: Chapter 2 quiz routing
    # if request.chapterId == 2:
    #     from app.ai.quiz.ch2_quiz_runtime import run as ch2_quiz_run
    #     result = await ch2_quiz_run(
    #         chapter_id=2,
    #         num_questions=request.numQuestions,
    #         learning_objectives=request.learningObjectives
    #     )
    #     return result
    ```
  - Add CH2-specific handling comments:
    - `# Route Chapter 2 quiz requests to ch2_quiz_runtime (placeholder routing)`
    - `# Ensure request model supports chapterId=2`
  - Ensure request model supports chapterId=2 (verify QuizRequest model)
  - Add inline documentation explaining Chapter 2 quiz routing

- [ ] [T018] [P1] [API] Verify ai_blocks.py still imports correctly: Run `cd backend && python -c "from app.api.ai_blocks import router; print('Import successful')"` - should complete without errors

- [ ] [T019] [P2] [API] Verify QuizRequest model supports chapterId=2: Check that request model has chapterId field that accepts value 2

- [ ] [T020] [P2] [API] Verify routing structure matches Chapter 2 ELI10 routing pattern:
  - Compare routing comment format
  - Ensure comment-only approach matches Feature 026 pattern

**Acceptance Test**: Endpoint accepts chapterId=2, routing comments are present, file still imports correctly, no breaking changes to existing functionality

---

## PHASE 5 — Contracts

**User Story**: US1 - Developer Sets Up Chapter 2 Quiz Runtime Infrastructure

**Test Strategy**: Can be tested by verifying contract file exists and documents expected placeholders.

### Contract Validation

- [ ] [T021] [P1] [DOCS] Verify contract file exists: Check that `specs/027-ch2-quiz-runtime/contracts/quiz-contract.yaml` exists (already created in spec phase)

- [ ] [T022] [P1] [DOCS] Verify contract documents runtime scaffold flow: Check that contract describes structure: inputs → rag-retrieve → prompt-build → provider-call → output-format

- [ ] [T023] [P2] [DOCS] Verify contract has no schema for actual quiz questions: Check that contract only documents placeholders, not real question schemas

**Acceptance Test**: Contract file exists, documents expected placeholders, describes structure flow, no schema for actual quiz questions

---

## PHASE 6 — Skills Extension

**User Story**: US1 - Developer Sets Up Chapter 2 Quiz Runtime Infrastructure

**Test Strategy**: Can be tested by verifying skills have Chapter 2 quiz placeholder functions with TODO comments.

### Prompt Builder Skill Updates

- [ ] [T024] [P1] [SKILLS] Update `backend/app/ai/skills/prompt_builder_skill.py` with Chapter 2 quiz prompt building:
  - Add `build_quiz_prompt_ch2()` function:
    ```python
    def build_quiz_prompt_ch2(
        chapter_id: int,
        num_questions: int,
        learning_objectives: Optional[List[str]] = None
    ) -> str:
        """
        Build quiz prompt for Chapter 2.
        
        Args:
            chapter_id: Chapter identifier (should be 2)
            num_questions: Number of questions to generate
            learning_objectives: Optional list of learning objectives to cover
        
        Returns:
            Constructed prompt string for quiz generation
        
        TODO: Implement prompt building for Chapter 2 quizzes
        TODO: Load ch2_quiz_prompt.txt template
        TODO: Replace template variables ({{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}})
        TODO: Add ROS 2-specific context
        TODO: Return constructed prompt string
        """
        return ""  # Placeholder
    ```
  - Add import if needed: `from typing import List, Optional`
  - Ensure function has TODO comments only (no real logic)

- [ ] [T025] [P1] [SKILLS] Verify prompt_builder_skill.py still imports correctly: Run `cd backend && python -c "from app.ai.skills.prompt_builder_skill import build_quiz_prompt_ch2; print('Import successful')"` - should complete without errors

### Formatting Skill Updates

- [ ] [T026] [P1] [SKILLS] Update `backend/app/ai/skills/formatting_skill.py` with Chapter 2 quiz formatting:
  - Add `format_quiz_output_ch2()` function:
    ```python
    def format_quiz_output_ch2(
        raw_response: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Format quiz output for Chapter 2.
        
        Args:
            raw_response: Raw LLM response dictionary
        
        Returns:
            Formatted quiz structure with questions, answers, learning_objectives, metadata
        
        TODO: Implement formatting for Chapter 2 quiz output
        TODO: Parse raw LLM response
        TODO: Extract questions, answers, learning_objectives
        TODO: Format ROS 2-specific metadata
        TODO: Return formatted quiz structure
        """
        return {
            "questions": [],
            "learning_objectives": [],
            "metadata": {}
        }  # Placeholder
    ```
  - Add import if needed: `from typing import Dict, Any`
  - Ensure function has TODO comments only (no real logic)

- [ ] [T027] [P1] [SKILLS] Verify formatting_skill.py still imports correctly: Run `cd backend && python -c "from app.ai.skills.formatting_skill import format_quiz_output_ch2; print('Import successful')"` - should complete without errors

- [ ] [T028] [P2] [SKILLS] Verify skills structure matches Chapter 2 ELI10 skills pattern:
  - Compare function signatures
  - Ensure placeholder approach matches Feature 026 pattern

**Acceptance Test**: Functions are importable, functions have TODO comments, no real logic implementation, files still import correctly

---

## PHASE 7 — Knowledge Source Preparation

**User Story**: US1 - Developer Sets Up Chapter 2 Quiz Runtime Infrastructure

**Test Strategy**: Can be tested by verifying Chapter 2 chunks file has quiz-specific chunk retrieval function with TODO comments.

### Knowledge Source Updates

- [ ] [T029] [P1] [KNOWLEDGE] Update `backend/app/content/chapters/chapter_2_chunks.py` with quiz-specific chunk retrieval:
  - Add `get_chapter2_quiz_chunks()` function:
    ```python
    def get_chapter2_quiz_chunks(
        chapter_id: int = 2,
        learning_objectives: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Get Chapter 2 chunks for quiz generation.
        
        Args:
            chapter_id: Chapter identifier (should be 2)
            learning_objectives: Optional list of learning objectives to filter by
        
        Returns:
            List of chapter chunks relevant for quiz generation
        
        TODO: Implement quiz-specific chunk retrieval
        TODO: Filter chunks by learning_objectives if provided
        TODO: Return chunks relevant for quiz generation
        TODO: Include ROS 2-specific metadata
        TODO: Ensure chunks are appropriate for quiz question generation
        """
        return []  # Placeholder
    ```
  - Add import if needed: `from typing import List, Dict, Any, Optional`
  - Ensure function has TODO comments only (no real logic)

- [ ] [T030] [P1] [KNOWLEDGE] Verify chapter_2_chunks.py still imports correctly: Run `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter2_quiz_chunks; print('Import successful')"` - should complete without errors

- [ ] [T031] [P2] [KNOWLEDGE] Verify knowledge source structure matches Chapter 2 pattern:
  - Compare function signature format
  - Ensure placeholder approach matches Feature 026 pattern

**Acceptance Test**: Function is importable, function has TODO comments, no real logic implementation, file still imports correctly

---

## PHASE 8 — Validation

**User Story**: US1 - Developer Sets Up Chapter 2 Quiz Runtime Infrastructure

**Test Strategy**: Can be tested by verifying backend starts, all imports resolve, and no real AI logic is implemented.

### Backend Startup Validation

- [ ] [T032] [P1] [VALIDATE] Start backend to confirm all imports resolve: Run `cd backend && uvicorn app.main:app` - should start without import errors or runtime exceptions

- [ ] [T033] [P1] [VALIDATE] Verify all new modules are importable:
  - Run `cd backend && python -c "from app.ai.quiz.ch2_quiz_runtime import run; print('ch2_quiz_runtime: OK')"`
  - Run `cd backend && python -c "from app.ai.skills.prompt_builder_skill import build_quiz_prompt_ch2; print('build_quiz_prompt_ch2: OK')"`
  - Run `cd backend && python -c "from app.ai.skills.formatting_skill import format_quiz_output_ch2; print('format_quiz_output_ch2: OK')"`
  - Run `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter2_quiz_chunks; print('get_chapter2_quiz_chunks: OK')"`
  - All should complete without errors

### Logic Verification

- [ ] [T034] [P1] [VALIDATE] Ensure no AI logic implemented: Verify all functions contain only TODO comments and placeholder returns (no real API calls, no RAG calls, no LLM calls)

- [ ] [T035] [P1] [VALIDATE] Verify all 6 steps have TODO markers: Check that ch2_quiz_runtime.py has all 6 steps (Validate, Build Prompt, Retrieve Context, Call RAG, Call LLM, Format) with TODO markers

- [ ] [T036] [P1] [VALIDATE] Verify routing is comment-only: Check that engine.py and ai_blocks.py have comment-only routing (no actual logic)

- [ ] [T037] [P2] [VALIDATE] Verify Chapter 1 quiz functionality still works: Check that existing Chapter 1 quiz functionality is not broken (if testable)

### File Existence Verification

- [ ] [T038] [P1] [VALIDATE] Verify all required files exist:
  - `backend/app/ai/quiz/ch2_quiz_runtime.py` exists
  - `backend/app/ai/prompts/quiz/ch2_quiz_prompt.txt` exists
  - `backend/app/ai/runtime/engine.py` updated with Chapter 2 quiz routing
  - `backend/app/api/ai_blocks.py` updated with Chapter 2 quiz routing
  - `backend/app/ai/skills/prompt_builder_skill.py` updated with build_quiz_prompt_ch2()
  - `backend/app/ai/skills/formatting_skill.py` updated with format_quiz_output_ch2()
  - `backend/app/content/chapters/chapter_2_chunks.py` updated with get_chapter2_quiz_chunks()
  - `specs/027-ch2-quiz-runtime/contracts/quiz-contract.yaml` exists

**Acceptance Test**: Backend starts without errors, all imports resolve correctly, no real AI logic implemented, all files exist at specified paths, all TODO comments are present

---

## Summary

**Total Tasks**: 38 tasks across 8 phases
- **Phase 0**: 7 setup tasks
- **Phase 1**: 3 runtime module tasks
- **Phase 2**: 3 prompt template tasks
- **Phase 3**: 3 routing tasks
- **Phase 4**: 4 API tasks
- **Phase 5**: 3 contract tasks
- **Phase 6**: 5 skills tasks
- **Phase 7**: 3 knowledge source tasks
- **Phase 8**: 7 validation tasks

**Estimated Time**: 30-45 minutes (scaffolding only, no real AI logic)

**Next Step**: Run `/sp.implement` to execute tasks in order

---

## Notes

- All tasks are scaffolding only—no real AI logic implementation
- All routing is comment-only—no actual logic execution
- All functions return placeholder values—no real data processing
- All validation focuses on structure and imports—not functionality
- Follow Feature 026 (Chapter 2 ELI10 Runtime) patterns exactly for consistency

