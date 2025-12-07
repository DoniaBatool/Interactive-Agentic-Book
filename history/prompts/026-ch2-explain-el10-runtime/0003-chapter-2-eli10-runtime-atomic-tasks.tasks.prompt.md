---
id: 0003
title: Chapter 2 Explain-Like-I'm-10 (ELI10) Runtime Atomic Tasks
stage: tasks
date: 2025-01-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: 026-ch2-explain-el10-runtime
branch: 003-chapter-1-content
user: Leo
command: /sp.tasks
labels: ["chapter-2", "backend", "eli10", "runtime", "tasks", "implementation"]
links:
  spec: specs/026-ch2-explain-el10-runtime/spec.md
  plan: specs/026-ch2-explain-el10-runtime/plan.md
  tasks: specs/026-ch2-explain-el10-runtime/tasks.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/026-ch2-explain-el10-runtime/tasks.md
tests:
  - Task completeness validation
  - Task atomicity validation
---

## Prompt

User requested: `/sp.tasks` following instructions from DOCUMENTATION.md (120-158)

Feature details:
- feature-id: 026-ch2-explain-el10-runtime
- Requirements:
  - RUNTIME MODULE: Create ch2_el10_runtime.py, add run() method with TODO-only flow (validate input, build prompt, call RAG, call LLM provider, format output)
  - PROMPT TEMPLATE: Create ch2_el10_prompt.txt, add variable placeholders ({{concept}}, {{chapter_id}}, {{context}})
  - ENGINE ROUTING: Update engine.py: if block_type == "explain-like-i-am-10" AND chapterId == 2 → call ch2_el10_runtime.run(), add comments describing routing behavior
  - API INTEGRATION: Update ai_blocks.py explain endpoint to support CH2
  - CONTRACTS: Create el10-contract.yaml, document placeholder rules + high-level flow
  - SKILLS: Update prompt_builder_skill.py (add build_el10_prompt_ch2()), update formatting_skill.py (add format_el10_output_ch2())
  - VALIDATION: Run backend to ensure no import errors, confirm all new files are recognized

## Response snapshot

Successfully created comprehensive atomic tasks for Chapter 2 Explain-Like-I'm-10 (ELI10) Runtime:

**Created Files:**
1. `specs/026-ch2-explain-el10-runtime/tasks.md` - Complete task list with:
   - Task Format and Legend
   - Phase 0: Setup & Prerequisites (6 tasks)
   - Phase 1: ELI10 Runtime Module (3 tasks)
   - Phase 2: Prompt Template (3 tasks)
   - Phase 3: Runtime Engine Routing (3 tasks)
   - Phase 4: API Layer Update (3 tasks)
   - Phase 5: Contracts (2 tasks)
   - Phase 6: Skills Extension (4 tasks)
   - Phase 7: Validation (5 tasks)
   - Task Summary (29 total tasks)
   - Completion Checklist
   - Next Steps

**Key Task Details:**
- **Total Tasks**: 29 tasks
  - Phase 0 (Setup): 6 tasks
  - Phase 1 (Runtime Module): 3 tasks
  - Phase 2 (Prompt Template): 3 tasks
  - Phase 3 (Runtime Engine Routing): 3 tasks
  - Phase 4 (API Layer): 3 tasks
  - Phase 5 (Contracts): 2 tasks
  - Phase 6 (Skills Extension): 4 tasks
  - Phase 7 (Validation): 5 tasks
- **Priority Breakdown**:
  - P1 (Critical): 27 tasks
  - P2 (Important): 2 tasks
  - P3 (Nice-to-have): 0 tasks
- **User Stories Covered**:
  - US1: Developer Sets Up Chapter 2 ELI10 Runtime Infrastructure (Phases 1, 2, 5, 6, 7)
  - US2: System Routes Chapter 2 ELI10 Requests (Phases 3, 4)
- **Estimated Time**: 30-45 minutes (scaffolding only, no real AI logic)

**Task Categories:**
- **Setup Tasks**: Verify dependencies (Feature 025, Feature 024), check file existence, validate prerequisites
- **Runtime Module Tasks**: Create ch2_el10_runtime.py with 5-step pipeline blueprint (all TODO)
- **Prompt Template Tasks**: Create ch2_el10_prompt.txt with 3 variables ({{concept}}, {{chapter_id}}, {{context}})
- **Routing Tasks**: Add Chapter 2 ELI10 routing to engine.py and ai_blocks.py (comments only)
- **Skills Tasks**: Add build_el10_prompt_ch2() and format_el10_output_ch2() placeholder functions
- **Validation Tasks**: Test backend startup, verify imports, check no real logic exists

**5-Step Pipeline Blueprint (All TODO):**
1. Validate input (TODO)
2. Build prompt (placeholder)
3. RAG retrieve (placeholder)
4. Call LLM (placeholder)
5. Format output (placeholder)

**Key Implementation Details:**
- **ch2_el10_runtime.py**: Function signature `async def run(concept: str, chapter_id: int, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]` with 5-step blueprint
- **ch2_el10_prompt.txt**: Template with 3 variables and TODO comments for future ELI10 style tuning
- **engine.py**: Comment-only routing: `if block_type == "explain-like-i-am-10" AND chapterId == 2`
- **ai_blocks.py**: Comment-only routing for chapterId=2 ELI10 requests
- **Skills**: 2 placeholder functions with TODO comments, no real logic

**Pattern Consistency:**
- Follows Feature 025 (Chapter 2 Diagram Runtime) task structure
- Same 5-step pipeline pattern
- Same placeholder-only implementation approach
- Same comment-only routing strategy
- Mirrors Chapter 1 structure for consistency

## Outcome

- ✅ Impact: Complete atomic task list ready for implementation. All Chapter 2 ELI10 runtime scaffolding points covered (runtime module, prompt template, routing, API layer, skills, contract). All tasks grouped into clear phases. Each task specifies file paths, expected content (TODO-level), validation steps, and acceptance criteria. Task list is comprehensive and ready for implementation.
- 🧪 Tests: Task completeness validation - PASS, Task atomicity validation - PASS
- 📁 Files: 1 file created (tasks.md)
- 🔁 Next prompts: `/sp.implement` to execute implementation tasks
- 🧠 Reflection: Task list follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures comprehensive coverage. Runtime module tasks create ch2_el10_runtime.py with 5-step blueprint. Prompt template tasks create ch2_el10_prompt.txt with ROS 2 variables. Routing tasks add Chapter 2 ELI10 routing (comments only). Skills tasks add placeholder functions. All tasks specify exact expected content at TODO-level. All tasks include validation steps. Note: This is a scaffolding extension - no actual AI logic, RAG implementation, or LLM calls should be done, only scaffolding with TODO placeholders. Mirrors Feature 025 structure for consistency. All 29 tasks are atomic and testable.

## Evaluation notes (flywheel)

- Failure modes observed: None - task generation phase completed successfully
- Graders run and results (PASS/FAIL): Task completeness - PASS, Task atomicity - PASS
- Prompt variant (if applicable): Standard /sp.tasks workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.implement` to execute implementation tasks

