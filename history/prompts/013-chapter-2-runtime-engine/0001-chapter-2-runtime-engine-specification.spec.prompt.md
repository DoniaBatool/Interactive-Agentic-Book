---
id: 0001
title: Chapter 2 AI Runtime Engine Integration Specification
stage: spec
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 013-chapter-2-runtime-engine
branch: 013-chapter-2-runtime-engine
user: Leo
command: /sp.specify
labels: ["chapter-2", "runtime-engine", "llm", "rag", "subagents", "chatkit", "specification"]
links:
  spec: specs/013-chapter-2-runtime-engine/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/013-chapter-2-runtime-engine/spec.md
  - specs/013-chapter-2-runtime-engine/contracts/runtime-flow.yaml
  - specs/013-chapter-2-runtime-engine/contracts/chapter-2-blocks.yaml
  - specs/013-chapter-2-runtime-engine/research.md
  - specs/013-chapter-2-runtime-engine/data-model.md
  - specs/013-chapter-2-runtime-engine/checklists/requirements.md
  - specs/013-chapter-2-runtime-engine/quickstart.md
tests:
  - Specification quality checklist validation (ALL PASS)
---

## Prompt

User requested: `/sp.specify` following instructions from DOCUMENTATION.md (111-188)

Feature details:
- feature-id: 013-chapter-2-runtime-engine
- title: "Chapter 2 — AI Runtime Engine Integration (LLM Routing, RAG Wiring, Subagents, ChatKit)"
- type: backend-ai-architecture
- goal: Activate the full runtime pathway for Chapter 2 so all AI Blocks (ask-question, explain-like-i-am-10, quiz, diagram) correctly route through the AI Runtime Engine. The logic remains placeholder-only, similar to Feature 005 for Chapter 1.

Requirements:
1. Runtime Engine Expansion: Add chapter_id=2 routing, placeholder LLM invocation, RAG-context consumption
2. RAG Pipeline Binding: Ensure pipeline resolves chapter_2_chunks, add placeholder flow comments
3. AI Block API Binding: Verify all block types route to run_ai_block with chapterId=2
4. Subagents for Chapter 2: Create 4 Chapter 2-specific subagent files (ch2_*)
5. Reusable Skills Integration: Add Chapter 2 TODOs to skills files
6. ChatKit Integration Scaffold: Add multi-chapter session contexts and Chapter 2 tool definitions
7. Config Updates: Add Chapter 2 runtime settings
8. Contracts: Create runtime-flow.yaml and chapter-2-blocks.yaml

## Response snapshot

Successfully created comprehensive feature specification for Chapter 2 runtime engine integration:

**Created Files:**
1. `specs/013-chapter-2-runtime-engine/spec.md` - Complete specification with:
   - 3 user stories (Developer Setup, System Admin Configuration, Future Developer Implementation)
   - 13 functional requirements (runtime expansion, RAG binding, API binding, subagents, skills, ChatKit, config, contracts)
   - Edge cases and error handling
   - Assumptions and dependencies
   - Success criteria and acceptance criteria

2. `specs/013-chapter-2-runtime-engine/contracts/runtime-flow.yaml` - Runtime flow contract with:
   - Complete runtime flow diagram (API → Runtime Engine → RAG → Skills → Subagents → LLM → Response)
   - Step-by-step flow documentation
   - Chapter 2-specific routing logic
   - Subagent mapping
   - RAG pipeline binding
   - Skills integration
   - LLM provider invocation
   - Response formatting

3. `specs/013-chapter-2-runtime-engine/contracts/chapter-2-blocks.yaml` - Chapter 2 blocks contract with:
   - 4 endpoint contracts (ask-question, explain-like-10, quiz, diagram)
   - 4 subagent contracts (ch2_ask_question_agent, ch2_explain_el10_agent, ch2_quiz_agent, ch2_diagram_agent)
   - Skills integration contracts
   - ChatKit integration contracts
   - Configuration contracts

4. `specs/013-chapter-2-runtime-engine/research.md` - Runtime engine integration research with:
   - Runtime engine routing patterns (chapter ID-based routing)
   - Subagent architecture (Chapter-specific subagents)
   - RAG pipeline binding (Chapter-aware retrieval)
   - Skills integration (Chapter-aware skills)
   - ChatKit integration (Multi-chapter session context)
   - Configuration (Chapter-specific settings)
   - ROS 2 specific considerations
   - Implementation phases
   - Best practices

5. `specs/013-chapter-2-runtime-engine/data-model.md` - Data structures and entities with:
   - Chapter 2 Runtime Engine Request entity
   - Chapter 2 Subagent entities (4 subagents)
   - Chapter 2 RAG Context entity
   - Chapter 2 Skills Integration entities
   - Chapter 2 ChatKit Session entity
   - Chapter 2 ChatKit Tools entity
   - Chapter 2 Configuration Settings entity
   - Entity relationships and data flow
   - Validation rules

6. `specs/013-chapter-2-runtime-engine/checklists/requirements.md` - Specification quality checklist with:
   - Content quality check (ALL PASS)
   - Requirement completeness check (ALL PASS)
   - Feature readiness check (ALL PASS)
   - Validation results

7. `specs/013-chapter-2-runtime-engine/quickstart.md` - Quickstart guide with:
   - Prerequisites
   - Commands
   - Folder structure
   - Feature overview
   - Key files to modify (14 files)
   - Implementation strategy
   - Validation steps
   - Success criteria
   - Next steps

**Key Specification Details:**
- All requirements are scaffolding-focused (no real implementation)
- Clear separation between scaffolding (this feature) and implementation (future features)
- Follows pattern from Feature 005 (AI Runtime Engine) and Feature 012 (Chapter 2 RAG)
- Comprehensive contracts and schemas for future reference
- ROS 2-specific context documented throughout
- Chapter 2-specific subagents follow naming pattern (ch2_*)

**Pattern Consistency:**
- Follows SDD workflow exactly (spec → plan → tasks → implement)
- Same file structure as previous features
- Clear TODO markers and placeholder functions
- No business logic (only scaffolding)

## Outcome

- ✅ Impact: Complete specification ready for planning phase. All user stories covered with testable requirements. Runtime engine integration clearly defined with contracts and schemas. ROS 2-specific context properly documented.
- 🧪 Tests: Specification quality checklist validation - ALL PASS (content quality, requirement completeness, feature readiness)
- 📁 Files: 7 files created (spec.md, 2 contracts, research.md, data-model.md, checklists, quickstart.md)
- 🔁 Next prompts: `/sp.plan` to create architecture plan
- 🧠 Reflection: Specification follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures future developers understand what needs to be built. ROS 2-specific context (concepts, section IDs, subagent patterns) properly documented in contracts and schemas. All requirements are testable and measurable. Chapter 2-specific subagents (ch2_*) provide clear separation from Chapter 1 subagents.

## Evaluation notes (flywheel)

- Failure modes observed: None - specification phase completed successfully
- Graders run and results (PASS/FAIL): Specification quality checklist - ALL PASS
- Prompt variant (if applicable): Standard /sp.specify workflow
- Next experiment (smallest change to proceed): Run `/sp.plan` to create architecture plan
