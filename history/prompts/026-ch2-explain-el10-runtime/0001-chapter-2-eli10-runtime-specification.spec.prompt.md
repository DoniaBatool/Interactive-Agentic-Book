---
id: 0001
title: Chapter 2 Explain-Like-I'm-10 (ELI10) Runtime Specification
stage: spec
date: 2025-01-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: 026-ch2-explain-el10-runtime
branch: 003-chapter-1-content
user: Leo
command: /sp.specify
labels: ["chapter-2", "backend", "eli10", "runtime", "scaffolding", "specification"]
links:
  spec: specs/026-ch2-explain-el10-runtime/spec.md
  plan: null
  tasks: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/026-ch2-explain-el10-runtime/spec.md
  - specs/026-ch2-explain-el10-runtime/contracts/el10-contract.yaml
  - specs/026-ch2-explain-el10-runtime/research.md
  - specs/026-ch2-explain-el10-runtime/data-model.md
  - specs/026-ch2-explain-el10-runtime/quickstart.md
  - specs/026-ch2-explain-el10-runtime/checklists/requirements.md
tests:
  - Specification completeness validation
  - Contract documentation validation
---

## Prompt

User requested: `/sp.specify` following instructions from DOCUMENTATION.md (3-76)

Feature details:
- feature-id: 026-ch2-explain-el10-runtime
- title: "Chapter 2 — Explain-Like-I'm-10 (ELI10) Runtime"
- type: backend-ai-pipeline
- goal: Build the full scaffolding for the Explain-Like-I'm-10 (ELI10) AI runtime specifically for Chapter 2. This includes runtime modules, routing, prompt templates, skill extensions, and contracts. No AI logic must be implemented.

Requirements:
1. Chapter 2 ELI10 Runtime Module: Create backend/app/ai/explain/ch2_el10_runtime.py with run() function and TODO placeholders (validate input, build prompt, RAG retrieve, call LLM, format output) - no implementation logic, comments only
2. Prompt Template: Create backend/app/ai/prompts/explain/ch2_el10_prompt.txt with variables ({{concept}}, {{chapter_id}}, {{context}}) and TODO comment for future ELI10 style tuning
3. Runtime Engine Routing: Update backend/app/ai/runtime/engine.py with route: if block_type == "explain-like-i-am-10" AND chapterId == 2 → call ch2_el10_runtime.run(), comment-only placeholder
4. API Layer Integration: Update backend/app/api/ai_blocks.py so ELI10 endpoint supports chapterId=2, add comments documenting CH2 workflow
5. Contracts: Create specs/026-ch2-explain-el10-runtime/contracts/el10-contract.yaml documenting high-level flow, expected placeholder behavior, no structure for real outputs
6. Skills: Update prompt_builder_skill.py (add build_el10_prompt_ch2()), update formatting_skill.py (add format_el10_output_ch2())
7. Stability + Environment: All imports must resolve, backend must start, no real AI or RAG implementation allowed

Acceptance Criteria:
- CH2 ELI10 runtime module exists with TODO-only scaffolding
- CH2 ELI10 prompt template exists
- Runtime engine routed for CH2 ELI10
- API updated for CH2 ELI10
- Contract spec created
- Skills extended
- No business logic implemented

## Response snapshot

Successfully created comprehensive specification for Chapter 2 Explain-Like-I'm-10 (ELI10) Runtime:

**Created Files:**
1. `specs/026-ch2-explain-el10-runtime/spec.md` - Complete specification with:
   - User Scenarios & Testing (2 user stories with acceptance scenarios, edge cases)
   - Functional Requirements (7 FRs: ELI10 Runtime Module, Prompt Template, Runtime Engine Routing, API Layer Integration, Contract, Skills Extension, Stability)
   - Assumptions (6 assumptions)
   - Key Entities (4 entities: ELI10 Runtime, Prompt Template, Routing, Skills)
   - Success Criteria (8 criteria)
   - Constraints (5 constraints)
   - Dependencies (4 dependencies: Feature 025, Feature 024, Skills layer, Runtime engine)
   - Out of Scope (8 items clearly defined)

2. `specs/026-ch2-explain-el10-runtime/contracts/el10-contract.yaml` - Complete contract documentation with:
   - Chapter 2 ELI10 Runtime Flow Contract (5-step pipeline)
   - Prompt Template Contract (3 variables: {{concept}}, {{chapter_id}}, {{context}})
   - Runtime Engine Routing Contract (comments only)
   - API Layer Contract (chapterId=2 routing)
   - Skills Extension Contract (2 functions: build_el10_prompt_ch2, format_el10_output_ch2)
   - Validation Contract (backend startup, module importability)
   - Error Handling Contract

3. `specs/026-ch2-explain-el10-runtime/research.md` - Research notes with:
   - Problem Context (scaffolding for ROS 2 ELI10 explanations)
   - Industry References (Feature 025 patterns, LLM reasoning + age-appropriate explanations)
   - Observations (Chapter 1 vs Chapter 2 differences and similarities)
   - Technical Decisions (3 decisions: Chapter 2-specific runtime module, Chapter 2 prompt template, placeholder-only implementation)
   - Implementation Notes (file creation strategy)
   - Risks and Mitigations (3 risks: import errors, breaking existing functionality, incomplete scaffolding)

4. `specs/026-ch2-explain-el10-runtime/data-model.md` - Data model documentation with:
   - Entities (4 entities: ELI10 Runtime Module, Prompt Template, ELI10 Routing, ELI10 Skills)
   - Relationships (3 relationships: API → Runtime Engine → ELI10 Runtime, ELI10 Runtime → Prompt Template, ELI10 Runtime → Skills)
   - Data Flow (ELI10 Explanation Flow: 4 steps)
   - Validation Rules Summary

5. `specs/026-ch2-explain-el10-runtime/quickstart.md` - Quickstart guide with:
   - Prerequisites (5 items)
   - Phase 1: ELI10 Runtime Module (10 minutes)
   - Phase 2: Prompt Template (5 minutes)
   - Phase 3: Runtime Engine Routing (5 minutes)
   - Phase 4: API Layer Update (5 minutes)
   - Phase 5: Skills Extension (10 minutes)
   - Phase 6: Validation (5 minutes)
   - Completion Checklist (8 items)
   - Troubleshooting

6. `specs/026-ch2-explain-el10-runtime/checklists/requirements.md` - Specification quality checklist:
   - Content Quality: PASS
   - Requirement Completeness: PASS
   - Feature Readiness: PASS
   - All validation checks: PASS

**Key Specification Details:**
- User Stories: 2 user stories (P1 priority)
  - User Story 1: Developer Sets Up Chapter 2 ELI10 Runtime Infrastructure (8 acceptance scenarios)
  - User Story 2: System Routes Chapter 2 ELI10 Requests (3 acceptance scenarios)
- Functional Requirements: 7 FRs
  - FR-001: Chapter 2 ELI10 Runtime Module (ch2_el10_runtime.py with 5-step blueprint)
  - FR-002: ELI10 Prompt Template (ch2_el10_prompt.txt with 3 variables)
  - FR-003: Runtime Engine Routing (if block_type == "explain-like-i-am-10" AND chapterId == 2)
  - FR-004: API Layer Integration (ELI10 endpoint supports chapterId=2)
  - FR-005: Chapter 2 ELI10 Placeholder Contract (el10-contract.yaml)
  - FR-006: Skills Extension (2 functions: build_el10_prompt_ch2, format_el10_output_ch2)
  - FR-007: Stability Requirement (backend compiles, imports resolve)
- Edge Cases: 5 edge cases documented
- Dependencies: 4 dependencies (Feature 025, Feature 024, Skills layer, Runtime engine)
- Out of Scope: 8 items clearly defined (no real AI logic, no RAG implementation, no LLM calls, no explanation generation)

**Contract Details:**
- Runtime Flow: 5-step pipeline (Validate → Build Prompt → RAG Retrieve → Call LLM → Format)
- Prompt Template: 3 variables ({{concept}}, {{chapter_id}}, {{context}})
- Routing: Runtime engine routes `block_type == "explain-like-i-am-10" AND chapterId == 2` to ch2_el10_runtime
- Skills: 2 placeholder functions (build_el10_prompt_ch2, format_el10_output_ch2)

**Pattern Consistency:**
- Follows Feature 025 (Chapter 2 Diagram Runtime) patterns
- Same specification structure and format
- Adapted for Chapter 2 ROS 2 ELI10 explanations
- Includes comprehensive contract documentation
- Focused on scaffolding only (no real AI logic)

## Outcome

- ✅ Impact: Complete specification ready for planning. All Chapter 2 ELI10 runtime scaffolding points covered (runtime module, prompt template, routing, API layer, skills, contract). All requirements grouped into clear sections. Each requirement specifies file path, expected content (TODO-level), dependencies, and acceptance test. Specification is comprehensive and ready for architecture planning.
- 🧪 Tests: Specification completeness validation - PASS, Contract documentation validation - PASS
- 📁 Files: 6 files created (spec.md, contracts/el10-contract.yaml, research.md, data-model.md, quickstart.md, checklists/requirements.md)
- 🔁 Next prompts: `/sp.plan` to create architecture plan
- 🧠 Reflection: Specification follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures comprehensive coverage. Runtime module tasks create ch2_el10_runtime.py with 5-step blueprint. Prompt template tasks create ch2_el10_prompt.txt with ROS 2 variables. Runtime engine tasks add Chapter 2 ELI10 routing (comments only). API layer tasks add Chapter 2 routing comments. Skills tasks add placeholder functions. All requirements specify exact expected content at TODO-level. All requirements include dependencies and acceptance tests. Note: This is a scaffolding extension - no actual AI logic, RAG implementation, or LLM calls should be done, only scaffolding with TODO placeholders. Mirrors Feature 025 structure for consistency.

## Evaluation notes (flywheel)

- Failure modes observed: None - specification phase completed successfully
- Graders run and results (PASS/FAIL): Specification completeness - PASS, Contract documentation - PASS
- Prompt variant (if applicable): Standard /sp.specify workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.plan` to create architecture plan

