---
id: 0001
title: Chapter 2 Interactive Quiz Runtime Engine Specification
stage: spec
date: 2025-01-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: 027-ch2-quiz-runtime
branch: 003-chapter-1-content
user: Leo
command: /sp.specify
labels: ["chapter-2", "backend", "quiz", "runtime", "scaffolding", "specification"]
links:
  spec: specs/027-ch2-quiz-runtime/spec.md
  plan: null
  tasks: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/027-ch2-quiz-runtime/spec.md
  - specs/027-ch2-quiz-runtime/contracts/quiz-contract.yaml
  - specs/027-ch2-quiz-runtime/research.md
  - specs/027-ch2-quiz-runtime/data-model.md
  - specs/027-ch2-quiz-runtime/quickstart.md
  - specs/027-ch2-quiz-runtime/checklists/requirements.md
tests:
  - Specification completeness validation
  - Contract documentation validation
---

## Prompt

User requested: `/sp.specify` following instructions from DOCUMENTATION.md (185-261)

Feature details:
- feature-id: 027-ch2-quiz-runtime
- title: "Chapter 2 — Interactive Quiz Runtime Engine"
- type: backend-ai-runtime
- goal: Build the Quiz Runtime Engine scaffolding for Chapter 2. This includes runtime module, routing, quiz prompt templates, stub skill functions, contract definition, API updates. No AI logic or quiz generation logic must be implemented.

Requirements:
1. Runtime Module: Create backend/app/ai/quiz/ch2_quiz_runtime.py with run() function and TODO placeholders (validate request, build prompt, retrieve chapter context, call RAG pipeline, call LLM provider, format output) - must contain no executable AI logic
2. Prompt Template: Create backend/app/ai/prompts/quiz/ch2_quiz_prompt.txt with variables ({{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}}) and TODO for future difficulty-level tuning
3. Runtime Engine Routing: Update backend/app/ai/runtime/engine.py with route: if block_type == "interactive-quiz" AND chapterId == 2 → call ch2_quiz_runtime.run(), routing logic must be comment-only placeholder
4. API Integration: Update backend/app/api/ai_blocks.py quiz endpoint to add CH2-specific handling comments, ensure request model supports chapterId=2, must call runtime engine for CH2
5. Contracts: Create specs/027-ch2-quiz-runtime/contracts/quiz-contract.yaml with high-level description of quiz runtime pipeline, define placeholder behavior, no real question schema
6. Skills Extensions: Update prompt_builder_skill.py (add build_quiz_prompt_ch2()), update formatting_skill.py (add format_quiz_output_ch2())
7. Knowledge Source Preparation: Update backend/app/content/chapters/chapter_2_chunks.py with TODO function get_chapter2_quiz_chunks()
8. Stability + Environment: All imports must resolve, backend must start, no real AI or quiz generation logic allowed

Acceptance Criteria:
- Runtime module exists with TODO-only scaffolding
- Prompt template exists
- Engine routing added for CH2 quiz
- API quiz endpoint supports CH2
- Contract YAML created
- Skills extended
- No real AI logic implemented
- Backend must start without errors

## Response snapshot

Successfully created comprehensive specification for Chapter 2 Interactive Quiz Runtime Engine:

**Created Files:**
1. `specs/027-ch2-quiz-runtime/spec.md` - Complete specification with:
   - User Scenarios & Testing (2 user stories with acceptance scenarios, edge cases)
   - Functional Requirements (8 FRs: Quiz Runtime Module, Prompt Template, Runtime Engine Routing, API Integration, Contract, Skills Extensions, Knowledge Source Preparation, Stability)
   - Assumptions (7 assumptions)
   - Key Entities (5 entities: Quiz Runtime, Prompt Template, Routing, Skills, Quiz Chunks)
   - Success Criteria (9 criteria)
   - Constraints (6 constraints)
   - Dependencies (5 dependencies: Feature 026, Feature 024, Skills layer, Runtime engine, Chapter 2 chunks)
   - Out of Scope (8 items clearly defined)

2. `specs/027-ch2-quiz-runtime/contracts/quiz-contract.yaml` - Complete contract documentation with:
   - Chapter 2 Quiz Runtime Flow Contract (6-step pipeline)
   - Prompt Template Contract (4 variables: {{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}})
   - Runtime Engine Routing Contract (comments only)
   - API Layer Contract (chapterId=2 routing)
   - Skills Extension Contract (2 functions: build_quiz_prompt_ch2, format_quiz_output_ch2)
   - Knowledge Source Contract (get_chapter2_quiz_chunks function)
   - Validation Contract (backend startup, module importability)
   - Error Handling Contract

3. `specs/027-ch2-quiz-runtime/research.md` - Research notes with:
   - Problem Context (scaffolding for ROS 2 quiz generation)
   - Industry References (Feature 026 patterns, LLM reasoning + quiz generation)
   - Observations (Chapter 1 vs Chapter 2 differences and similarities)
   - Technical Decisions (4 decisions: Chapter 2-specific runtime module, Chapter 2 prompt template, placeholder-only implementation, quiz-specific chunk retrieval)
   - Implementation Notes (file creation strategy)
   - Risks and Mitigations (3 risks: import errors, breaking existing functionality, incomplete scaffolding)

4. `specs/027-ch2-quiz-runtime/data-model.md` - Data model documentation with:
   - Entities (5 entities: Quiz Runtime Module, Prompt Template, Quiz Routing, Quiz Skills, Quiz Chunks)
   - Relationships (4 relationships: API → Runtime Engine → Quiz Runtime, Quiz Runtime → Prompt Template, Quiz Runtime → Skills, Quiz Runtime → Quiz Chunks)
   - Data Flow (Quiz Generation Flow: 4 steps)
   - Validation Rules Summary

5. `specs/027-ch2-quiz-runtime/quickstart.md` - Quickstart guide with:
   - Prerequisites (6 items)
   - Phase 1: Quiz Runtime Module (10 minutes)
   - Phase 2: Prompt Template (5 minutes)
   - Phase 3: Runtime Engine Routing (5 minutes)
   - Phase 4: API Layer Update (5 minutes)
   - Phase 5: Skills Extension (10 minutes)
   - Phase 6: Knowledge Source Preparation (5 minutes)
   - Phase 7: Validation (5 minutes)
   - Completion Checklist (9 items)
   - Troubleshooting

6. `specs/027-ch2-quiz-runtime/checklists/requirements.md` - Specification quality checklist:
   - Content Quality: PASS
   - Requirement Completeness: PASS
   - Feature Readiness: PASS
   - All validation checks: PASS

**Key Specification Details:**
- User Stories: 2 user stories (P1 priority)
  - User Story 1: Developer Sets Up Chapter 2 Quiz Runtime Infrastructure (9 acceptance scenarios)
  - User Story 2: System Routes Chapter 2 Quiz Requests (3 acceptance scenarios)
- Functional Requirements: 8 FRs
  - FR-001: Chapter 2 Quiz Runtime Module (ch2_quiz_runtime.py with 6-step blueprint)
  - FR-002: Quiz Prompt Template (ch2_quiz_prompt.txt with 4 variables)
  - FR-003: Runtime Engine Routing (if block_type == "interactive-quiz" AND chapterId == 2)
  - FR-004: API Integration (quiz endpoint supports chapterId=2)
  - FR-005: Chapter 2 Quiz Placeholder Contract (quiz-contract.yaml)
  - FR-006: Skills Extensions (2 functions: build_quiz_prompt_ch2, format_quiz_output_ch2)
  - FR-007: Knowledge Source Preparation (get_chapter2_quiz_chunks function)
  - FR-008: Stability Requirement (backend compiles, imports resolve)
- Edge Cases: 5 edge cases documented
- Dependencies: 5 dependencies (Feature 026, Feature 024, Skills layer, Runtime engine, Chapter 2 chunks)
- Out of Scope: 8 items clearly defined (no real AI logic, no RAG implementation, no LLM calls, no quiz generation)

**Contract Details:**
- Runtime Flow: 6-step pipeline (Validate → Build Prompt → Retrieve Context → Call RAG → Call LLM → Format)
- Prompt Template: 4 variables ({{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}})
- Routing: Runtime engine routes `block_type == "interactive-quiz" AND chapterId == 2` to ch2_quiz_runtime
- Skills: 2 placeholder functions (build_quiz_prompt_ch2, format_quiz_output_ch2)
- Knowledge Source: Quiz-specific chunk retrieval function (get_chapter2_quiz_chunks)

**Pattern Consistency:**
- Follows Feature 026 (Chapter 2 ELI10 Runtime) patterns
- Same specification structure and format
- Adapted for Chapter 2 ROS 2 quiz generation
- Includes comprehensive contract documentation
- Focused on scaffolding only (no real AI logic)

## Outcome

- ✅ Impact: Complete specification ready for planning. All Chapter 2 quiz runtime scaffolding points covered (runtime module, prompt template, routing, API layer, skills, contract, knowledge source). All requirements grouped into clear sections. Each requirement specifies file path, expected content (TODO-level), dependencies, and acceptance test. Specification is comprehensive and ready for architecture planning.
- 🧪 Tests: Specification completeness validation - PASS, Contract documentation validation - PASS
- 📁 Files: 6 files created (spec.md, contracts/quiz-contract.yaml, research.md, data-model.md, quickstart.md, checklists/requirements.md)
- 🔁 Next prompts: `/sp.plan` to create architecture plan
- 🧠 Reflection: Specification follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures comprehensive coverage. Runtime module tasks create ch2_quiz_runtime.py with 6-step blueprint. Prompt template tasks create ch2_quiz_prompt.txt with ROS 2 variables. Runtime engine tasks add Chapter 2 quiz routing (comments only). API layer tasks add Chapter 2 routing comments. Skills tasks add placeholder functions. Knowledge source tasks add quiz chunks function. All requirements specify exact expected content at TODO-level. All requirements include dependencies and acceptance tests. Note: This is a scaffolding extension - no actual AI logic, RAG implementation, or LLM calls should be done, only scaffolding with TODO placeholders. Mirrors Feature 026 structure for consistency.

## Evaluation notes (flywheel)

- Failure modes observed: None - specification phase completed successfully
- Graders run and results (PASS/FAIL): Specification completeness - PASS, Contract documentation - PASS
- Prompt variant (if applicable): Standard /sp.specify workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.plan` to create architecture plan

