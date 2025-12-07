---
id: 0001
title: Chapter 2 Backend Runtime Wiring Specification
stage: spec
date: 2025-01-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: 024-ch2-runtime-wiring
branch: 003-chapter-1-content
user: Leo
command: /sp.specify
labels: ["chapter-2", "backend", "runtime", "wiring", "integration", "specification"]
links:
  spec: specs/024-ch2-runtime-wiring/spec.md
  plan: null
  tasks: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/024-ch2-runtime-wiring/spec.md
  - specs/024-ch2-runtime-wiring/contracts/runtime-flow.yaml
  - specs/024-ch2-runtime-wiring/research.md
  - specs/024-ch2-runtime-wiring/data-model.md
  - specs/024-ch2-runtime-wiring/quickstart.md
  - specs/024-ch2-runtime-wiring/checklists/requirements.md
tests:
  - Specification completeness validation
  - Contract documentation validation
---

## Prompt

User requested: `/sp.specify` following instructions from DOCUMENTATION.md (365-429)

Feature details:
- feature-id: 024-ch2-runtime-wiring
- title: "Chapter 2 — Backend Runtime Wiring for AI Blocks"
- type: backend-integration
- goal: Connect all Chapter 2 interactive blocks (Ask Question, Explain Like I'm 10, Quiz Generator, Diagram Generator) to the AI Runtime Engine created in Feature 006. This is a pure scaffolding feature with NO real AI logic.

Requirements:
1. API Layer Updates: Update backend/app/api/ai_blocks.py so each POST request includes chapterId=2 and routes into run_ai_block, add routing comments
2. Runtime Engine Awareness: Update backend/app/ai/runtime/engine.py with placeholder routing for chapterId=2, add comments describing expected flows
3. RAG Layer: Create backend/app/content/chapters/chapter_2_chunks.py with get_chapter_chunks() → TODO placeholder list, ensure parity with chapter_1_chunks structure
4. Subagent Draft Files: Create empty scaffolds (ch2_ask_question_agent.py, ch2_explain_el10_agent.py, ch2_quiz_agent.py, ch2_diagram_agent.py) with TODO comments
5. Skills Layer Extension: Update retrieval_skill.py, prompt_builder_skill.py, formatting_skill.py with Chapter 2 placeholder routing (no logic)
6. Contracts: Create specs/024-ch2-runtime-wiring/contracts/runtime-flow.yaml documenting expected runtime flow for Chapter 2
7. Stability + Build: Backend must start without errors, all new modules must import correctly

Acceptance Criteria:
- Chapter 2 has complete scaffolding for backend runtime
- All subagent files exist
- Runtime engine references Chapter 2 correctly
- No AI logic exists—only placeholders and structure
- Backend compiles and runs

## Response snapshot

Successfully created comprehensive specification for Chapter 2 Backend Runtime Wiring:

**Created Files:**
1. `specs/024-ch2-runtime-wiring/spec.md` - Complete specification with:
   - User Scenarios & Testing (2 user stories, edge cases)
   - Functional Requirements (7 FRs across 7 categories)
   - Assumptions, Dependencies, Out of Scope
   - Success Criteria, Acceptance Criteria
   
2. `specs/024-ch2-runtime-wiring/contracts/runtime-flow.yaml` - Complete contract documentation with:
   - Runtime Flow Diagram
   - API Layer Contract (4 endpoints)
   - Runtime Engine Contract (Chapter 2 routing)
   - RAG Layer Contract (Chapter 2 chunks file)
   - Subagent Contract (4 subagent files)
   - Skills Layer Contract (3 skills files)
   - Validation Contract
   - Error Handling Contract
   
3. `specs/024-ch2-runtime-wiring/research.md` - Research notes with:
   - Problem Context
   - Industry References (Runtime Engine Patterns, Subagent Architecture, Skills Layer Extension)
   - Observations (Current Architecture)
   - Technical Decisions (3 decisions with rationale)
   - Implementation Notes
   - Risks and Mitigations
   
4. `specs/024-ch2-runtime-wiring/data-model.md` - Data model documentation with:
   - Entities (4 entities: Runtime Routing, Chunks File, Subagent Files, Skills Extensions)
   - Relationships (4 relationships)
   - Data Flow (Request Flow)
   - Validation Rules Summary
   
5. `specs/024-ch2-runtime-wiring/quickstart.md` - Quickstart guide with:
   - Prerequisites (6 features)
   - Phase 1: API Layer Updates (10 minutes)
   - Phase 2: Runtime Engine Updates (10 minutes)
   - Phase 3: RAG Layer - Chapter 2 Chunks (15 minutes)
   - Phase 4: Subagent Scaffold Files (15 minutes)
   - Phase 5: Skills Layer Extensions (10 minutes)
   - Phase 6: Validation (10 minutes)
   - Troubleshooting
   - Completion Checklist
   
6. `specs/024-ch2-runtime-wiring/checklists/requirements.md` - Specification quality checklist:
   - Content Quality: PASS
   - Requirement Completeness: PASS
   - Feature Readiness: PASS
   - All validation checks: PASS

**Key Specification Details:**
- User Stories: 2 user stories (P1 priority)
  - User Story 1: Developer Wires Chapter 2 into Backend Runtime (13 acceptance scenarios)
  - User Story 2: System Routes Chapter 2 AI Block Requests (5 acceptance scenarios)
- Functional Requirements: 7 FRs
  - FR-001: API Layer Updates
  - FR-002: Runtime Engine Awareness of Chapter 2
  - FR-003: RAG Layer for Chapter 2
  - FR-004: Subagent Draft Files (4 files)
  - FR-005: Skills Layer Extension (3 files)
  - FR-006: Contracts
  - FR-007: Stability + Build Requirements
- Edge Cases: 5 edge cases documented
- Dependencies: 5 features (F006, F023, Chapter 1 chunks, existing subagents, skills layer)
- Out of Scope: 9 items clearly defined (no real AI logic, no RAG implementation, no subagent logic)

**Contract Details:**
- Runtime Flow: API → Runtime Engine → Chapter 2 Subagent → Skills → Response
- API Endpoints: 4 endpoints (ask-question, explain-like-10, quiz, diagram) with chapterId=2
- Runtime Engine: Chapter 2 routing with placeholder comments
- RAG Layer: chapter_2_chunks.py with placeholder function
- Subagents: 4 empty scaffold files (ch2_*_agent.py)
- Skills: 3 skills files with Chapter 2 placeholder comments

**Pattern Consistency:**
- Follows Feature 022 (Chapter 2 Runtime Wiring) patterns
- Same specification structure and format
- Adapted for focused backend wiring (no RAG pipeline changes)
- Includes comprehensive contract documentation
- Focused on scaffolding only (no real AI logic)

## Outcome

- ✅ Impact: Complete specification ready for planning. All backend runtime wiring points covered (API layer, runtime engine, RAG layer, subagents, skills). All requirements grouped into clear sections. Each requirement specifies file path, expected content (TODO-level), dependencies, and acceptance test. Specification is comprehensive and ready for architecture planning.
- 🧪 Tests: Specification completeness validation - PASS, Contract documentation validation - PASS
- 📁 Files: 6 files created (spec.md, contracts/runtime-flow.yaml, research.md, data-model.md, quickstart.md, checklists/requirements.md)
- 🔁 Next prompts: `/sp.plan` to create architecture plan
- 🧠 Reflection: Specification follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures comprehensive coverage. API layer tasks are straightforward (add routing comments). Runtime engine tasks verify/add placeholder routing. RAG layer tasks create chapter_2_chunks.py with placeholder function. Subagent tasks create empty scaffold files. Skills tasks add placeholder routing comments. All requirements specify exact expected content at TODO-level. All requirements include dependencies and acceptance tests. Note: This is a wiring/scaffolding extension - no actual AI logic, RAG implementation, or subagent logic should be done, only scaffolding with TODO placeholders.

## Evaluation notes (flywheel)

- Failure modes observed: None - specification phase completed successfully
- Graders run and results (PASS/FAIL): Specification completeness - PASS, Contract documentation - PASS
- Prompt variant (if applicable): Standard /sp.specify workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.plan` to create architecture plan

