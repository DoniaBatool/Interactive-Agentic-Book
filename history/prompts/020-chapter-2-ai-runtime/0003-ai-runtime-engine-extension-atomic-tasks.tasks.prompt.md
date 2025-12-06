---
id: 0003
title: AI Runtime Engine Extension Atomic Tasks for Chapter 2
stage: tasks
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 020-chapter-2-ai-runtime
branch: 020-chapter-2-ai-runtime
user: Leo
command: /sp.tasks
labels: ["chapter-2", "ai-runtime", "rag", "llm", "subagents", "tasks", "atomic-tasks"]
links:
  spec: specs/020-chapter-2-ai-runtime/spec.md
  plan: specs/020-chapter-2-ai-runtime/plan.md
  tasks: specs/020-chapter-2-ai-runtime/tasks.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/020-chapter-2-ai-runtime/tasks.md
tests:
  - Tasks completeness validation
  - Tasks actionability validation
---

## Prompt

User requested: `/sp.tasks` following instructions from DOCUMENTATION.md (516-546)

Feature details:
- feature-id: 020-chapter-2-ai-runtime
- title: "Chapter 2 AI Runtime Tasks"
- goal: Generate atomic check-box tasks for implementing scaffolding only, grouped into sections A-K

Requirements:
1. Group tasks into sections A-K as specified in DOCUMENTATION.md
2. Each task must specify: file path, exact expected content (TODO-level), dependencies, acceptance test
3. End with "Tasks complete — ready for /sp.implement."

## Response snapshot

Successfully created comprehensive atomic tasks for AI Runtime Engine Extension for Chapter 2:

**Created Files:**
1. `specs/020-chapter-2-ai-runtime/tasks.md` - Complete tasks document with:
   - Task format and legend
   - Phase 0: Setup & Prerequisites (10 tasks)
   - Phase A: RAG Infrastructure Tasks (3 tasks)
     - Create collections directory
     - Create collections __init__.py
     - Create ch2_collection.py with TODO stubs
   - Phase B: Embedding Pipeline Tasks (2 tasks)
     - Extend generate_embedding function
     - Add batch_embed_ch2 function
   - Phase C: Chapter Knowledge Source Tasks (3 tasks)
     - Verify chapter_2_chunks.py exists
     - Verify get_chapter_chunks function
     - Add TODO comments if needed
   - Phase D: Runtime Engine Extension Tasks (4 tasks)
     - Add Chapter 2 routing logic
     - Add Chapter 2 handler functions
     - Add Chapter 2 RAG integration comments
     - Verify engine imports
   - Phase E: Subagent Tasks (CH2) (5 tasks)
     - Verify or create ch2_ask_question_agent.py
     - Verify or create ch2_el10_agent.py
     - Verify or create ch2_quiz_agent.py
     - Verify or create ch2_diagram_agent.py
     - Verify all subagents import
   - Phase F: Skills Extension Tasks (3 tasks)
     - Extend retrieval_skill.py
     - Extend prompt_builder_skill.py
     - Verify skills import
   - Phase G: ChatKit Extension Tasks (2 tasks)
     - Extend session_manager.py
     - Verify ChatKit import
   - Phase H: Config + ENV Tasks (3 tasks)
     - Update settings.py
     - Update .env.example
     - Verify settings load
   - Phase I: API Routing Tasks (3 tasks)
     - Verify ai_blocks.py routes Chapter 2
     - Add Chapter 2 routing comment
     - Verify API imports
   - Phase J: Validation Tasks (4 tasks)
     - Verify all files exist
     - Verify all imports resolve
     - Verify backend starts
     - Verify no breaking changes
   - Phase K: Contract + Checklist Generation Tasks (2 tasks)
     - Verify contract files exist
     - Verify checklist files exist
   - Summary (44 tasks across 11 phases)

**Key Task Details:**
- Total tasks: 44 tasks across 11 phases
- Priority distribution: P1 (Critical) - 44 tasks, P2 (Important) - 0 tasks
- Task format: `- [ ] [TaskID] [Priority] [Story] Description with explicit file path`
- All tasks use strict checkbox format
- Each task specifies: file path, exact expected content (TODO-level), dependencies, acceptance test
- All tasks grouped into sections A-K as specified

**Differences from Feature 013:**
- Feature 020 adds RAG Infrastructure Tasks (Phase A) - ch2_collection.py creation
- Feature 020 adds Embedding Pipeline Tasks (Phase B) - chapter=2 support
- Feature 020 adds Config + ENV Tasks (Phase H) - Chapter 2 settings
- Feature 013 focused on runtime routing and subagents
- Feature 020 is a more complete extension

**Pattern Consistency:**
- Follows Feature 005 (AI Runtime Engine) and Feature 013 (Chapter 2 Runtime Engine) task patterns
- Same task structure and format
- Adapted for Chapter 2 content (ROS 2)
- Includes RAG collection setup and embedding pipeline extension tasks

## Outcome

- ✅ Impact: Complete atomic tasks ready for implementation. All extension points covered (RAG infrastructure, embedding pipeline, knowledge source, runtime engine, subagents, skills, ChatKit, config, API routing, validation). All tasks grouped into sections A-K as specified. Each task specifies file path, exact expected content (TODO-level), dependencies, and acceptance test. All tasks use strict checkbox format. Tasks are actionable and ready for direct execution.
- 🧪 Tests: Tasks completeness validation - PASS, Tasks actionability validation - PASS
- 📁 Files: 1 tasks file created (tasks.md with 44 atomic tasks across 11 phases)
- 🔁 Next prompts: `/sp.implement` to implement scaffolding
- 🧠 Reflection: Tasks follow established patterns for maintainability. Clear separation between phases ensures comprehensive coverage. RAG infrastructure and embedding pipeline tasks are new additions. All tasks specify exact expected content at TODO-level. All tasks include dependencies and acceptance tests. Note: This is a scaffolding extension - no actual AI logic implementation should be done, only scaffolding with TODO placeholders. Feature 013 may have created some subagents - verify and extend if needed.

## Evaluation notes (flywheel)

- Failure modes observed: None - tasks phase completed successfully
- Graders run and results (PASS/FAIL): Tasks completeness - PASS, Tasks actionability - PASS
- Prompt variant (if applicable): Standard /sp.tasks workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.implement` to implement scaffolding
