---
id: 0003
title: Chapter 2 AI Runtime Engine Integration Tasks
stage: tasks
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 013-chapter-2-runtime-engine
branch: 013-chapter-2-runtime-engine
user: Leo
command: /sp.tasks
labels: ["chapter-2", "runtime-engine", "llm", "rag", "subagents", "chatkit", "tasks", "implementation"]
links:
  spec: specs/013-chapter-2-runtime-engine/spec.md
  plan: specs/013-chapter-2-runtime-engine/plan.md
  tasks: specs/013-chapter-2-runtime-engine/tasks.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/013-chapter-2-runtime-engine/tasks.md
tests:
  - Task list completeness validation
  - Task atomicity validation
---

## Prompt

User requested: `/sp.tasks` following instructions from DOCUMENTATION.md (227-267)

Feature details:
- feature-id: 013-chapter-2-runtime-engine
- title: "Chapter 2 — AI Runtime Engine Integration (LLM Routing, RAG Wiring, Subagents, ChatKit)"
- goal: Generate atomic, executable tasks for implementing Chapter 2 runtime engine scaffolding

Requirements:
1. PHASE 1 — Runtime Engine Routing: Add chapter_id=2 routing, placeholder LLM handling, TODO notes
2. PHASE 2 — AI Block API Binding: Update ai_blocks.py to pass chapter_id=2
3. PHASE 3 — Subagent Scaffolding: Create 4 ch2_* subagent files with signatures + TODOs
4. PHASE 4 — Skills Updates: Add chapter-aware TODO notes in formatting_skill, retrieval_skill, prompt_builder_skill
5. PHASE 5 — RAG Connection: Update pipeline.py for chapter 2 contextual steps
6. PHASE 6 — ChatKit Integration: Add multi-chapter placeholder notes in session_manager.py, tool entries in tools.py
7. PHASE 7 — Config & ENV: Add new env vars to .env.example, add chapter 2 fields to settings.py
8. PHASE 8 — Contracts: Already created in spec phase (runtime-flow.yaml, chapter-2-blocks.yaml)

## Response snapshot

Successfully created comprehensive task list for Chapter 2 runtime engine integration:

**Created Files:**
1. `specs/013-chapter-2-runtime-engine/tasks.md` - Complete task list with:
   - Phase 0: Setup & Prerequisites (9 tasks)
   - Phase 1: Runtime Engine Routing (8 tasks)
   - Phase 2: AI Block API Binding (7 tasks)
   - Phase 3: Subagent Scaffolding (8 tasks)
   - Phase 4: Skills Updates (13 tasks)
   - Phase 5: RAG Connection (4 tasks)
   - Phase 6: ChatKit Integration (7 tasks)
   - Phase 7: Config & ENV (7 tasks)
   - Phase 8: Validation & Testing (6 tasks)
   - Total: 69 atomic, testable tasks

**Task Breakdown:**
- Each task has TaskID (T001-T069), Priority (P1/P2), Story (US1/US2/SETUP), and explicit file paths
- Tasks are atomic and independently testable
- All tasks focus on scaffolding (no real implementation)
- Clear acceptance criteria for each phase
- Comprehensive validation tasks in Phase 8

**Key Task Categories:**
- Runtime Engine Routing: Chapter 2 routing logic, subagent mapping, RAG context loading, LLM invocation placeholders
- AI Block API Binding: Verify all endpoints accept chapterId parameter
- Subagent Scaffolding: 4 new subagent files (ch2_ask_question_agent, ch2_explain_el10_agent, ch2_quiz_agent, ch2_diagram_agent)
- Skills Updates: Chapter-aware TODOs for all 5 skills (retrieval, prompt_builder, formatting, quiz_formatting, diagram)
- RAG Connection: Chapter 2 binding comments, placeholder context injection
- ChatKit Integration: Multi-chapter session contexts, Chapter 2 tool definitions
- Config & ENV: 3 new settings (DEFAULT_CH2_MODEL, DEFAULT_CH2_EMBEDDINGS, ENABLE_CHAPTER_2_RUNTIME)
- Validation: Import validation, backend startup, placeholder function validation, file existence, TODO comment validation

**Pattern Consistency:**
- Follows Feature 012 tasks.md pattern
- Atomic, testable tasks with explicit file paths
- Clear success criteria for each phase
- Comprehensive validation phase
- Scaffolding-only approach (no real implementation)

## Outcome

- ✅ Impact: Complete task list ready for implementation. All 69 tasks are atomic, testable, and focused on scaffolding. Clear phase organization with acceptance criteria. Comprehensive validation tasks ensure quality.
- 🧪 Tests: Task list completeness validation - PASS, Task atomicity validation - PASS
- 📁 Files: 1 task file created (tasks.md with 69 atomic tasks across 8 phases)
- 🔁 Next prompts: `/sp.implement` to execute all tasks
- 🧠 Reflection: Task list follows established patterns for maintainability. All tasks are atomic and independently testable. Clear separation between scaffolding and implementation ensures future developers understand what needs to be built. ROS 2-specific context properly documented in task descriptions. Chapter 2-specific subagents (ch2_*) clearly identified. All file paths explicit and unambiguous.

## Evaluation notes (flywheel)

- Failure modes observed: None - task generation phase completed successfully
- Graders run and results (PASS/FAIL): Task list completeness - PASS, Task atomicity - PASS
- Prompt variant (if applicable): Standard /sp.tasks workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.implement` to execute all tasks
