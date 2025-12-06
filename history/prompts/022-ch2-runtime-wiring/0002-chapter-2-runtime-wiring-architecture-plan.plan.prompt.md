---
id: 0002
title: Chapter 2 Runtime Wiring Architecture Plan
stage: plan
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 022-ch2-runtime-wiring
branch: 022-ch2-runtime-wiring
user: Leo
command: /sp.plan
labels: ["chapter-2", "runtime", "rag", "wiring", "routing", "architecture-plan"]
links:
  spec: specs/022-ch2-runtime-wiring/spec.md
  plan: specs/022-ch2-runtime-wiring/plan.md
  tasks: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/022-ch2-runtime-wiring/plan.md
tests:
  - Architecture plan completeness validation
  - Integration points validation
---

## Prompt

User requested: `/sp.plan` following instructions from DOCUMENTATION.md (82-132)

Feature details:
- feature-id: 022-ch2-runtime-wiring
- title: "Chapter 2 — RAG Pipeline Wiring, Runtime Routing & AI Block Integration"
- goal: Create the complete architectural plan for connecting Chapter 2 to the AI Runtime Engine, including RAG pipeline hooks, runtime routing, AI-block integration, and knowledge source alignment.

Plan requirements:
1. RAG Pipeline Architecture: Add new constants for CH2 embeddings, define placeholder functions (embed_ch2(), retrieve_ch2_chunks(), build_ch2_context()), ensure consistent naming with CH1
2. Runtime Engine Flow: Detect chapter_id=2, pass query → rag_pipeline → provider, add placeholder context merging logic, add placeholder chapter-specific routing notes
3. AI Block Runtime Layer: Update ai_blocks.py to support CH2, add placeholders for ask-question runtime, explain-like-i-am-10 runtime, quiz runtime, diagram runtime
4. Subagents & Skills: Add CH2 TODO branches in all four subagents, ensure skills folder recognises chapter_id input
5. Contracts: Create runtime-wiring.yaml contract (already created), document RAG → LLM → Block response flow, required entrypoints, chapter-aware behavior
6. Validation: Ensure backend starts, no logic yet (pure structure), imports clean

## Response snapshot

Successfully created comprehensive architecture plan for Chapter 2 Runtime Wiring:

**Created Files:**
1. `specs/022-ch2-runtime-wiring/plan.md` - Complete architecture plan with:
   - Summary and Technical Context
   - High-Level Architecture Overview (architecture flow, component responsibilities, data flow)
   - RAG Pipeline Architecture (4 sections: collection name constant, embed function, retrieve function, build context function, naming consistency)
   - Runtime Engine Flow (5 sections: chapter ID detection, Chapter 2 handling path, query → RAG → provider flow, context merging logic, provider selection)
   - AI Block Runtime Layer (5 sections: ask-question runtime, explain-like-10 runtime, quiz runtime, diagram runtime, Chapter 2 support verification)
   - Subagents & Skills (5 sections: ask question agent, explain EL10 agent, quiz agent, diagram agent, skills folder chapter ID recognition)
   - Contracts (4 sections: runtime wiring contract, RAG → LLM → block response flow, required entrypoints, chapter-aware behavior)
   - Knowledge Source Structure (3 sections: chunk count placeholder, expected section map placeholder, embedding ready flag)
   - Validation (5 sections: backend startup validation, import resolution validation, runtime engine awareness validation, no business logic validation, contract validation)
   - Integration Points (5 sections: Feature 005, Feature 020, Feature 021, Feature 012, Feature 013)
   - Acceptance Checks (6 sections: RAG pipeline wiring, runtime engine routing, AI block runtime hooks, subagent connectors, knowledge source structure, validation)
   - Risk Analysis (3 risks with mitigation strategies)
   - Next Steps

**Key Architecture Details:**
- RAG Pipeline Functions: 3 functions (embed_chapter_2, retrieve_chapter_2_relevant_chunks, build_context_for_ch2)
- Runtime Engine Routing: chapter_id=2 handling path with comprehensive TODO comments
- API Endpoints: 4 endpoints with Chapter 2 context loading TODOs
- Subagents: 4 subagents with Chapter 2 handling path TODOs
- Knowledge Source: 3 structural metadata placeholders (chunk_count, expected_section_map, embedding_ready)
- Integration Points: 5 features (F005, F012, F013, F020, F021)
- Acceptance Checks: 6 categories with detailed checklists

**Architecture Flow:**
- Request Flow: API Endpoint → Runtime Engine → RAG Pipeline → Subagent → Response
- Context Building: User Query → RAG Pipeline → Retrieve Chunks → Build Context → Subagent
- Routing Flow: chapterId=2 → Runtime Engine → Chapter 2 Handling Path → Chapter 2 Subagent

**Pattern Consistency:**
- Follows Feature 020 (Chapter 2 AI Runtime Extension) and Feature 021 (Chapter 2 RAG Preparation) patterns
- Same architecture structure and format
- Adapted for runtime wiring (connecting pieces together)
- Includes comprehensive integration points and acceptance checks

## Outcome

- ✅ Impact: Complete architecture plan ready for tasks generation. All components covered (RAG pipeline hooks, runtime engine routing, API endpoint hooks, subagent connectors, knowledge source structure). All integration points documented. All acceptance checks defined. Architecture plan is comprehensive and ready for implementation tasks generation.
- 🧪 Tests: Architecture plan completeness validation - PASS, Integration points validation - PASS
- 📁 Files: 1 plan file created (plan.md with 12 major sections covering all architecture aspects)
- 🔁 Next prompts: `/sp.tasks` to generate atomic tasks for implementation
- 🧠 Reflection: Architecture plan follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures comprehensive coverage. RAG pipeline architecture adds 3 function stubs with clear entry points. Runtime engine flow registers chapter_id=2 handling path with comprehensive TODO comments. AI block runtime layer adds Chapter 2 context loading TODOs to all 4 endpoints. Subagent connectors add Chapter 2 handling path comments to all 4 subagents. Knowledge source structure adds 3 structural metadata placeholders. All integration points are documented. All acceptance checks are defined. Note: This is a wiring/scaffolding extension - no actual RAG, routing, or AI logic implementation should be done, only scaffolding with TODO placeholders.

## Evaluation notes (flywheel)

- Failure modes observed: None - architecture plan phase completed successfully
- Graders run and results (PASS/FAIL): Architecture plan completeness - PASS, Integration points validation - PASS
- Prompt variant (if applicable): Standard /sp.plan workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.tasks` to generate atomic tasks for implementation
