---
id: 0003
title: Chapter 2 Interactive Quiz Runtime Engine Atomic Tasks
stage: tasks
date: 2025-01-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: 027-ch2-quiz-runtime
branch: 003-chapter-1-content
user: Leo
command: /sp.tasks
labels: ["chapter-2", "backend", "quiz", "runtime", "tasks", "implementation"]
links:
  spec: specs/027-ch2-quiz-runtime/spec.md
  plan: specs/027-ch2-quiz-runtime/plan.md
  tasks: specs/027-ch2-quiz-runtime/tasks.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/027-ch2-quiz-runtime/tasks.md
tests:
  - Task completeness validation
  - Task structure verification
---

## Prompt

User requested: `/sp.tasks` following instructions from DOCUMENTATION.md (313-351)

Feature details:
- feature-id: 027-ch2-quiz-runtime
- goal: Generate atomic implementation tasks for Chapter 2 Interactive Quiz Runtime Engine scaffolding
- task categories:
  1. RUNTIME MODULE TASKS - Create backend/app/ai/quiz/ch2_quiz_runtime.py, Add run() with placeholder steps, Add TODO for future adaptive difficulty
  2. PROMPT TEMPLATE TASKS - Create backend/app/ai/prompts/quiz/ch2_quiz_prompt.txt, Insert variables: {{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}}
  3. ENGINE ROUTING TASKS - Update backend/app/ai/runtime/engine.py, Add comment-only routing for CH2: block=interactive-quiz AND chapterId=2
  4. API TASKS - Update quiz endpoint in ai_blocks.py, Document behavior for chapterId=2, Ensure request forwarded to runtime engine
  5. CONTRACT TASKS - Create specs/027-ch2-quiz-runtime/contracts/quiz-contract.yaml, Document runtime scaffold flow (already created in spec phase)
  6. SKILLS TASKS - Update prompt_builder_skill: add build_quiz_prompt_ch2(), Update formatting_skill: add format_quiz_output_ch2()
  7. KNOWLEDGE SOURCE TASKS - Update chapter_2_chunks.py with get_chapter2_quiz_chunks()
  8. VALIDATION TASKS - Start backend to confirm all imports resolve, Ensure no AI logic implemented

## Response snapshot

Successfully created comprehensive atomic task list for Chapter 2 Interactive Quiz Runtime Engine:

**Created Files:**
1. `specs/027-ch2-quiz-runtime/tasks.md` - Complete atomic task list with:
   - Task Format and Legend
   - Phase 0: Setup & Prerequisites (7 tasks)
   - Phase 1: Quiz Runtime Module (3 tasks)
   - Phase 2: Prompt Template (3 tasks)
   - Phase 3: Runtime Engine Routing (3 tasks)
   - Phase 4: API Layer Update (4 tasks)
   - Phase 5: Contracts (3 tasks)
   - Phase 6: Skills Extension (5 tasks)
   - Phase 7: Knowledge Source Preparation (3 tasks)
   - Phase 8: Validation (7 tasks)
   - Summary (38 total tasks)

**Key Task Details:**
- **Phase 0 (Setup)**: 7 tasks to verify dependencies (Feature 026, Feature 024, API layer, skills layer, backend startup, quiz directory, Chapter 2 chunks)
- **Phase 1 (Runtime Module)**: 3 tasks
  - T008: Create ch2_quiz_runtime.py with 6-step pipeline blueprint (Validate → Build Prompt → Retrieve Context → Call RAG → Call LLM → Format)
  - T009: Verify importability
  - T010: Verify structure matches Feature 026 pattern
- **Phase 2 (Prompt Template)**: 3 tasks
  - T012: Create ch2_quiz_prompt.txt with 4 variables ({{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}})
  - T013: Verify file readability
- **Phase 3 (Routing)**: 3 tasks
  - T014: Update engine.py with comment-only Chapter 2 quiz routing
  - T015: Verify imports
  - T016: Verify structure matches Feature 026 pattern
- **Phase 4 (API)**: 4 tasks
  - T017: Update ai_blocks.py with Chapter 2 quiz routing comments
  - T018: Verify imports
  - T019: Verify QuizRequest model supports chapterId=2
  - T020: Verify structure matches Feature 026 pattern
- **Phase 5 (Contracts)**: 3 tasks
  - T021-T023: Verify contract file exists and documents expected placeholders (already created in spec phase)
- **Phase 6 (Skills)**: 5 tasks
  - T024: Add build_quiz_prompt_ch2() to prompt_builder_skill.py
  - T025: Verify imports
  - T026: Add format_quiz_output_ch2() to formatting_skill.py
  - T027: Verify imports
  - T028: Verify structure matches Feature 026 pattern
- **Phase 7 (Knowledge Source)**: 3 tasks
  - T029: Add get_chapter2_quiz_chunks() to chapter_2_chunks.py
  - T030: Verify imports
  - T031: Verify structure matches Feature 026 pattern
- **Phase 8 (Validation)**: 7 tasks
  - T032: Backend startup validation
  - T033: Import verification for all new modules
  - T034: Logic verification (no AI logic implemented)
  - T035: Verify all 6 steps have TODO markers
  - T036: Verify routing is comment-only
  - T037: Verify Chapter 1 quiz functionality still works
  - T038: File existence verification

**6-Step Pipeline Blueprint:**
1. Validate request (TODO)
2. Build prompt (placeholder)
3. Retrieve chapter context (placeholder)
4. Call RAG pipeline (placeholder)
5. Call LLM provider (placeholder)
6. Format output (placeholder)

**Pattern Consistency:**
- Follows Feature 026 (Chapter 2 ELI10 Runtime) task structure exactly
- Same 8-phase approach (Setup → Runtime → Prompt → Routing → API → Contracts → Skills → Knowledge → Validation)
- Same placeholder-only implementation approach
- Same comment-only routing strategy
- Mirrors Chapter 1 structure for consistency

**Task Format:**
- TaskID: Sequential identifier (T001-T038)
- Priority: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- Category: SETUP, RUNTIME, PROMPT, ROUTING, API, SKILLS, KNOWLEDGE, VALIDATE, DOCS

## Outcome

- ✅ Impact: Complete atomic task list ready for implementation. All Chapter 2 quiz runtime scaffolding points covered (runtime module, prompt template, routing, API layer, skills, contract, knowledge source). All tasks grouped into 8 clear phases. Each task specifies exact file paths, expected content (TODO-level), validation steps, and dependencies. Task list is comprehensive and ready for execution.
- 🧪 Tests: Task completeness validation - PASS, Task structure verification - PASS
- 📁 Files: 1 file created (tasks.md)
- 🔁 Next prompts: `/sp.implement` to execute tasks in order
- 🧠 Reflection: Task list follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures comprehensive coverage. Runtime module phase creates ch2_quiz_runtime.py with 6-step blueprint. Prompt template phase creates ch2_quiz_prompt.txt with ROS 2 variables. Runtime engine phase adds Chapter 2 quiz routing (comments only). API layer phase adds Chapter 2 routing comments. Skills phase adds placeholder functions. Knowledge source phase adds quiz chunks function. All tasks specify exact expected content at TODO-level. All tasks include validation steps. Note: This is a scaffolding extension - no actual AI logic, RAG implementation, or LLM calls should be done, only scaffolding with TODO placeholders. Mirrors Feature 026 structure for consistency. All 38 tasks are atomic and executable.

## Evaluation notes (flywheel)

- Failure modes observed: None - task generation phase completed successfully
- Graders run and results (PASS/FAIL): Task completeness - PASS, Task structure - PASS
- Prompt variant (if applicable): Standard /sp.tasks workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.implement` to execute tasks in order

