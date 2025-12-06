---
id: 0001
title: Chapter 2 Runtime Wiring Specification
stage: spec
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 022-ch2-runtime-wiring
branch: 022-ch2-runtime-wiring
user: Leo
command: /sp.specify
labels: ["chapter-2", "runtime", "rag", "wiring", "routing", "specification"]
links:
  spec: specs/022-ch2-runtime-wiring/spec.md
  plan: null
  tasks: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/022-ch2-runtime-wiring/spec.md
  - specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml
  - specs/022-ch2-runtime-wiring/research.md
  - specs/022-ch2-runtime-wiring/data-model.md
  - specs/022-ch2-runtime-wiring/quickstart.md
  - specs/022-ch2-runtime-wiring/checklists/requirements.md
tests:
  - Specification completeness validation
  - Contract documentation validation
---

## Prompt

User requested: `/sp.specify` following instructions from DOCUMENTATION.md (7-80)

Feature details:
- feature-id: 022-ch2-runtime-wiring
- title: "Chapter 2 — RAG Pipeline Wiring, Runtime Routing & AI Block Integration"
- type: backend-ai-architecture
- goal: Connect Chapter 2 into the AI Runtime Engine. This includes RAG pipeline registration, chapter selection logic, context assembly, runtime routing for AI blocks, and placeholder logic hooks. NO real AI implementation; only scaffolding.

Requirements:
1. RAG Pipeline Wiring: Update pipeline.py, add CHAPTER_2_COLLECTION_NAME constant, add TODO stubs for embed_chapter_2(), retrieve_chapter_2_relevant_chunks(), build_context_for_ch2()
2. Runtime Engine Routing: Update engine.py, register chapter_id=2 handling path, route to RAG pipeline functions (placeholders only), add TODO comments for context merging and provider selection
3. AI Block Runtime Hooks: Update ai_blocks.py, ensure each AI block type can target chapter 2, add TODO comments for loading Chapter 2 context, connect to runtime engine
4. Subagent Connectors: Update subagents (ask_question_agent.py, explain_el10_agent.py, quiz_agent.py, diagram_agent.py), add TODO comments for Chapter 2 handling path
5. Chapter 2 Knowledge Source: Update chapter_2_chunks.py, add structural TODO comments for chunk_count, expected_section_map, embedding_ready = False
6. Contracts: Create runtime-wiring.yaml, document chapter selection flow → RAG → LLM → response, required placeholders, API-level routing contract, context-building contract
7. Validation Requirements: Backend starts with no errors, no logic implemented (placeholders ONLY), all import paths valid, runtime engine now "aware" of Chapter 2

## Response snapshot

Successfully created comprehensive specification for Chapter 2 Runtime Wiring:

**Created Files:**
1. `specs/022-ch2-runtime-wiring/spec.md` - Complete specification with:
   - User Scenarios & Testing (2 user stories, edge cases)
   - Functional Requirements (6 FRs, 3 NFRs)
   - Assumptions, Dependencies, Out of Scope
   - Success Criteria, Acceptance Criteria
   
2. `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml` - Complete contract documentation with:
   - Chapter Selection Flow Contract
   - RAG Pipeline Integration Contract (3 functions: embed_chapter_2, retrieve_chapter_2_relevant_chunks, build_context_for_ch2)
   - API-Level Routing Contract (4 endpoints: ask-question, explain-like-10, quiz, diagram)
   - Context-Building Contract
   - Subagent Integration Contract (4 subagents)
   - Knowledge Source Contract
   - Validation Contract
   
3. `specs/022-ch2-runtime-wiring/research.md` - Research notes with:
   - Problem Context
   - Technology Decisions (4 decisions with rationale)
   - Industry References (RAG Pipeline Architecture, Runtime Engine Patterns, Context Assembly)
   - Observations (Current Architecture, Integration Points, Challenges)
   - Technical Considerations
   
4. `specs/022-ch2-runtime-wiring/data-model.md` - Data model documentation with:
   - Entities (5 entities: RAG Pipeline Functions, Runtime Engine Routing, API Endpoints, Subagent Connectors, Knowledge Source)
   - Relationships (4 relationships with flow diagrams)
   - Data Flow (Request Flow, Context Building Flow)
   
5. `specs/022-ch2-runtime-wiring/quickstart.md` - Quickstart guide with:
   - Prerequisites (5 features)
   - Commands (SDD workflow)
   - Folder Structure
   - Feature Overview
   - Key Files to Create/Modify (8 files to modify, 1 file to create)
   - Implementation Steps (4 phases)
   - Success Criteria
   - Troubleshooting
   
6. `specs/022-ch2-runtime-wiring/checklists/requirements.md` - Specification quality checklist:
   - Content Quality: PASS
   - Requirement Completeness: PASS
   - Feature Readiness: PASS
   - All validation checks: PASS

**Key Specification Details:**
- User Stories: 2 user stories (P1 priority)
  - User Story 1: Developer Wires Chapter 2 into Runtime Engine (11 acceptance scenarios)
  - User Story 2: System Integrates Chapter 2 AI Blocks (5 acceptance scenarios)
- Functional Requirements: 6 FRs
  - FR-001: RAG Pipeline Wiring for Chapter 2
  - FR-002: Runtime Engine Routing for Chapter 2
  - FR-003: AI Block Runtime Hooks for Chapter 2
  - FR-004: Subagent Connectors for Chapter 2 (4 subagents)
  - FR-005: Chapter 2 Knowledge Source Structure
  - FR-006: Runtime Wiring Contract
- Non-Functional Requirements: 3 NFRs
  - NFR-001: Code Quality
  - NFR-002: Maintainability
  - NFR-003: Validation
- Edge Cases: 5 edge cases documented
- Dependencies: 5 features (F005, F012, F013, F020, F021)
- Out of Scope: 10 items clearly defined (no real implementation)

**Contract Details:**
- Chapter Selection Flow: Request flow from API → Runtime Engine → RAG → Subagent → Response
- RAG Pipeline Functions: 3 functions (embed_chapter_2, retrieve_chapter_2_relevant_chunks, build_context_for_ch2)
- API Endpoints: 4 endpoints (ask-question, explain-like-10, quiz, diagram)
- Subagents: 4 subagents (ask_question_agent, explain_el10_agent, quiz_agent, diagram_agent)
- Knowledge Source: Structural metadata (chunk_count, expected_section_map, embedding_ready)

**Pattern Consistency:**
- Follows Feature 020 (Chapter 2 AI Runtime Extension) and Feature 021 (Chapter 2 RAG Preparation) patterns
- Same specification structure and format
- Adapted for runtime wiring (connecting pieces together)
- Includes comprehensive contract documentation

## Outcome

- ✅ Impact: Complete specification ready for planning. All extension points covered (RAG pipeline wiring, runtime engine routing, API endpoint hooks, subagent connectors, knowledge source structure). All requirements grouped into clear sections. Each requirement specifies file path, expected content (TODO-level), dependencies, and acceptance test. Specification is comprehensive and ready for architecture planning.
- 🧪 Tests: Specification completeness validation - PASS, Contract documentation validation - PASS
- 📁 Files: 6 files created (spec.md, contracts/runtime-wiring.yaml, research.md, data-model.md, quickstart.md, checklists/requirements.md)
- 🔁 Next prompts: `/sp.plan` to create architecture plan
- 🧠 Reflection: Specification follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures comprehensive coverage. RAG pipeline wiring tasks are straightforward (add TODO stubs). Runtime engine routing tasks register chapter_id=2 handling path. API endpoint tasks add Chapter 2 context loading TODOs. Subagent tasks add Chapter 2 handling path comments. Knowledge source tasks add structural metadata placeholders. All requirements specify exact expected content at TODO-level. All requirements include dependencies and acceptance tests. Note: This is a wiring/scaffolding extension - no actual RAG, routing, or AI logic implementation should be done, only scaffolding with TODO placeholders.

## Evaluation notes (flywheel)

- Failure modes observed: None - specification phase completed successfully
- Graders run and results (PASS/FAIL): Specification completeness - PASS, Contract documentation - PASS
- Prompt variant (if applicable): Standard /sp.specify workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.plan` to create architecture plan
