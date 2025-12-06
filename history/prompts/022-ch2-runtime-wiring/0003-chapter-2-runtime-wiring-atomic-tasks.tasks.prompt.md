---
id: 0003
title: Chapter 2 Runtime Wiring Atomic Tasks
stage: tasks
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 022-ch2-runtime-wiring
branch: 022-ch2-runtime-wiring
user: Leo
command: /sp.tasks
labels: ["chapter-2", "runtime", "rag", "wiring", "routing", "tasks", "atomic-tasks"]
links:
  spec: specs/022-ch2-runtime-wiring/spec.md
  plan: specs/022-ch2-runtime-wiring/plan.md
  tasks: specs/022-ch2-runtime-wiring/tasks.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/022-ch2-runtime-wiring/tasks.md
tests:
  - Tasks completeness validation
  - Tasks actionability validation
---

## Prompt

User requested: `/sp.tasks` following instructions from DOCUMENTATION.md (134-182)

Feature details:
- feature-id: 022-ch2-runtime-wiring
- title: "Chapter 2 — RAG Pipeline Wiring, Runtime Routing & AI Block Integration"
- goal: Generate the full task list for implementing runtime wiring scaffolding

Requirements:
1. FRONTEND — None
2. BACKEND — RAG PIPELINE: Add CHAPTER_2_COLLECTION constant, add TODO stubs for embed_chapter_2(), retrieve_ch2_chunks(), build_context_ch2(), validate imports
3. BACKEND — RUNTIME ENGINE: Update engine.py with chapter 2 routing, add TODO: call CH2 RAG pipeline, add TODO: provider selection, add TODO: context generation
4. BACKEND — AI BLOCK ROUTING: Modify ai_blocks.py, add chapter_id=2 support, add TODO: load CH2 context
5. BACKEND — SUBAGENTS: Add CH2 TODO branches in ask_question_agent.py, explain_el10_agent.py, quiz_agent.py, diagram_agent.py
6. BACKEND — KNOWLEDGE SOURCE MODULE: Update chapter_2_chunks.py, add TODO for chunk_count, section_map, embedding_ready flag
7. CONTRACTS: Create runtime-wiring.yaml (already created), document flow diagram, document RAG → LLM routing rules
8. VALIDATION: Backend starts without errors, all imports resolve, no business logic implemented

## Response snapshot

Successfully created comprehensive atomic tasks for Chapter 2 Runtime Wiring:

**Created Files:**
1. `specs/022-ch2-runtime-wiring/tasks.md` - Complete tasks document with:
   - Task format and legend
   - Phase 0: Setup & Prerequisites (8 tasks)
   - Phase A: BACKEND — RAG Pipeline (5 tasks)
     - Add CHAPTER_2_COLLECTION_NAME constant
     - Add embed_chapter_2() function stub
     - Add retrieve_chapter_2_relevant_chunks() function stub
     - Add build_context_for_ch2() function stub
     - Validate RAG pipeline imports
   - Phase B: BACKEND — Runtime Engine (4 tasks)
     - Update engine.py with chapter 2 routing
     - Add TODO: call CH2 RAG pipeline
     - Add TODO: provider selection
     - Add TODO: context generation
   - Phase C: BACKEND — AI Block Routing (3 tasks)
     - Modify ai_blocks.py to support Chapter 2
     - Add chapter_id=2 support
     - Add TODO: load CH2 context
   - Phase D: BACKEND — Subagents (4 tasks)
     - Add CH2 TODO branch in ask_question_agent.py
     - Add CH2 TODO branch in explain_el10_agent.py
     - Add CH2 TODO branch in quiz_agent.py
     - Add CH2 TODO branch in diagram_agent.py
   - Phase E: BACKEND — Knowledge Source Module (4 tasks)
     - Update chapter_2_chunks.py with structural TODOs
     - Add TODO for chunk_count
     - Add TODO for section_map
     - Add TODO for embedding_ready flag
   - Phase F: CONTRACTS (3 tasks)
     - Verify runtime-wiring.yaml exists
     - Verify flow diagram documentation
     - Verify RAG → LLM routing rules documentation
   - Phase G: VALIDATION (4 tasks)
     - Validate backend starts without errors
     - Validate all imports resolve
     - Validate no business logic implemented
     - Validate runtime engine aware of Chapter 2
   - Summary (35 tasks across 7 phases)

**Key Task Details:**
- Total tasks: 35 tasks across 7 phases
- Priority distribution: P1 (Critical) - 35 tasks, P2 (Important) - 0 tasks
- Task format: `- [ ] [TaskID] [Priority] [Story] Description with explicit file path`
- All tasks use strict checkbox format
- Each task specifies: file path, exact expected content (TODO-level), dependencies, acceptance test
- All tasks grouped into sections as specified in DOCUMENTATION.md

**RAG Pipeline Tasks:**
- 1 constant to add (CHAPTER_2_COLLECTION_NAME)
- 3 function stubs to add (embed_chapter_2, retrieve_chapter_2_relevant_chunks, build_context_for_ch2)
- All functions with TODO comments and proper type hints

**Runtime Engine Tasks:**
- chapter_id=2 handling path registration
- TODO comments for RAG pipeline call
- TODO comments for provider selection
- TODO comments for context merging

**AI Block Routing Tasks:**
- All 4 endpoints support chapterId=2
- TODO comments for Chapter 2 context loading in all endpoints

**Subagent Tasks:**
- 4 subagents with Chapter 2 handling path TODOs
- Each subagent has chapter_id=2 branch with TODO comments

**Knowledge Source Tasks:**
- 3 structural metadata placeholders (chunk_count, expected_section_map, embedding_ready)
- All placeholders with TODO comments

**Pattern Consistency:**
- Follows Feature 020 (Chapter 2 AI Runtime Extension) and Feature 021 (Chapter 2 RAG Preparation) task patterns
- Same task structure and format
- Adapted for runtime wiring (connecting pieces together)
- Includes comprehensive validation tasks

## Outcome

- ✅ Impact: Complete atomic tasks ready for implementation. All extension points covered (RAG pipeline hooks, runtime engine routing, API endpoint hooks, subagent connectors, knowledge source structure). All tasks grouped into sections as specified in DOCUMENTATION.md. Each task specifies file path, exact expected content (TODO-level), dependencies, and acceptance test. All tasks use strict checkbox format. Tasks are actionable and ready for direct execution.
- 🧪 Tests: Tasks completeness validation - PASS, Tasks actionability validation - PASS
- 📁 Files: 1 tasks file created (tasks.md with 35 atomic tasks across 7 phases)
- 🔁 Next prompts: `/sp.implement` to implement scaffolding
- 🧠 Reflection: Tasks follow established patterns for maintainability. Clear separation between phases ensures comprehensive coverage. RAG pipeline tasks are straightforward (add constant and 3 function stubs). Runtime engine tasks register chapter_id=2 handling path with comprehensive TODO comments. AI block routing tasks add Chapter 2 context loading TODOs to all 4 endpoints. Subagent tasks add Chapter 2 handling path comments to all 4 subagents. Knowledge source tasks add structural metadata placeholders. All tasks specify exact expected content at TODO-level. All tasks include dependencies and acceptance tests. Note: This is a wiring/scaffolding extension - no actual RAG, routing, or AI logic implementation should be done, only scaffolding with TODO placeholders.

## Evaluation notes (flywheel)

- Failure modes observed: None - tasks phase completed successfully
- Graders run and results (PASS/FAIL): Tasks completeness - PASS, Tasks actionability - PASS
- Prompt variant (if applicable): Standard /sp.tasks workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.implement` to implement scaffolding
