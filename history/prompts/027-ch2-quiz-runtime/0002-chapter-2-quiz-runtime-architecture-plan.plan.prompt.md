---
id: 0002
title: Chapter 2 Interactive Quiz Runtime Engine Architecture Plan
stage: plan
date: 2025-01-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: 027-ch2-quiz-runtime
branch: 003-chapter-1-content
user: Leo
command: /sp.plan
labels: ["chapter-2", "backend", "quiz", "runtime", "architecture", "planning"]
links:
  spec: specs/027-ch2-quiz-runtime/spec.md
  plan: specs/027-ch2-quiz-runtime/plan.md
  tasks: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/027-ch2-quiz-runtime/plan.md
tests:
  - Architecture plan completeness validation
  - Constitution compliance check
---

## Prompt

User requested: `/sp.plan` following instructions from DOCUMENTATION.md (264-311)

Feature details:
- feature-id: 027-ch2-quiz-runtime
- goal: Provide a complete architecture plan for the Chapter 2 Interactive Quiz engine, including folder structure, routing flow, prompt strategy, skills, and contracts.
- plan sections:
  1. File Structure - backend/app/ai/quiz/ch2_quiz_runtime.py, backend/app/ai/prompts/quiz/ch2_quiz_prompt.txt, specs/027-ch2-quiz-runtime/contracts/quiz-contract.yaml
  2. Runtime Flow (scaffold only) - run() with TODO steps: validate input, extract learning objectives, call RAG retrieve for Chapter 2, build quiz prompt, call provider LLM, format output
  3. Engine Routing - engine.py: Add conditional routing if block == interactive-quiz & chapterId=2
  4. API Layer Changes - ai_blocks.py: Update quiz handler to forward CH2 requests to engine, add inline documentation
  5. Skills to Extend - prompt_builder_skill.py (add build_quiz_prompt_ch2()), formatting_skill.py (add format_quiz_output_ch2())
  6. Contracts - quiz-contract.yaml: Describe structure (inputs → rag-retrieve → prompt-build → provider-call → output-format), no schema for actual quiz questions

## Response snapshot

Successfully created comprehensive architecture plan for Chapter 2 Interactive Quiz Runtime Engine:

**Created Files:**
1. `specs/027-ch2-quiz-runtime/plan.md` - Complete architecture plan with:
   - Summary and Technical Context
   - Constitution Check (all 6 principles - 5 PASS, 1 SCAFFOLDING)
   - Architecture Overview (system architecture diagram, key components, integration points)
   - Implementation Phases (8 phases with tasks, deliverables, validation)
   - Key Decisions (5 decisions with rationale)
   - Risk Analysis (3 risks with mitigation strategies)
   - Validation Strategy (pre, during, post implementation)
   - Success Criteria (9 criteria)
   - Next Steps

**Key Architecture Details:**
- **System Architecture**: API Layer → Runtime Engine → Chapter 2 Quiz Runtime → Prompt Template / Skills Layer / Knowledge Source
- **Request Flow**: API Endpoint → Runtime Engine (if block_type == "interactive-quiz" AND chapterId == 2) → ch2_quiz_runtime.run() → 6-Step Pipeline (all TODO) → Response
- **Implementation Phases**: 8 phases
  - Phase 1: Quiz Runtime Module (ch2_quiz_runtime.py with 6-step blueprint)
  - Phase 2: Prompt Template (ch2_quiz_prompt.txt with 4 variables)
  - Phase 3: Runtime Engine Routing (comment-only routing)
  - Phase 4: API Layer Update (chapterId=2 routing comments)
  - Phase 5: Contracts (quiz-contract.yaml already created)
  - Phase 6: Skills Extension (2 placeholder functions)
  - Phase 7: Knowledge Source Preparation (get_chapter2_quiz_chunks function)
  - Phase 8: Validation (backend startup, imports, logic verification)
- **Key Decisions**: 5 decisions
  - Decision 1: Create Chapter 2-Specific Runtime Module (chosen: create ch2_quiz_runtime.py as separate module)
  - Decision 2: Create Chapter 2 Prompt Template (chosen: create ch2_quiz_prompt.txt with ROS 2-specific placeholders)
  - Decision 3: Placeholder-Only Implementation (chosen: placeholder-only with TODO comments)
  - Decision 4: Comment-Only Routing (chosen: comment-only routing with TODO markers)
  - Decision 5: Quiz-Specific Chunk Retrieval (chosen: create get_chapter2_quiz_chunks() placeholder function)
- **Risk Analysis**: 3 risks identified with mitigation strategies
  - Risk 1: Import Errors (Medium probability, High impact) - Mitigated by validation phase
  - Risk 2: Breaking Existing Functionality (Low probability, High impact) - Mitigated by comment-only approach
  - Risk 3: Incomplete Scaffolding (Low probability, Medium impact) - Mitigated by following established patterns
- **Constitution Check**: All 6 principles checked
  - Principle I (SDD Workflow): ✅ PASS
  - Principle II (Docusaurus-First): ✅ PASS
  - Principle III (RAG-First): ⚠️ SCAFFOLDING (acceptable for scaffolding phase)
  - Principle IV (Personalization): ✅ PASS
  - Principle V (Multilingual): ✅ PASS
  - Principle VI (TDD Quality Gates): ✅ PASS
  - Overall: ✅ APPROVED TO PROCEED

**6-Step Pipeline Blueprint:**
1. Validate request (TODO)
2. Build prompt (placeholder)
3. Retrieve chapter context (placeholder)
4. Call RAG pipeline (placeholder)
5. Call LLM provider (placeholder)
6. Format output (placeholder)

**Integration Points:**
- AI Runtime Engine (Feature 024): Routes quiz blocks to Chapter 2 quiz runtime
- Chapter 1 Quiz Runtime: Reference structure for Chapter 2 implementation
- Skills Layer: Provides prompt building and formatting capabilities
- API Layer: Receives quiz requests and routes to appropriate runtime
- Chapter 2 Chunks: Provides quiz-specific content retrieval

**Pattern Consistency:**
- Follows Feature 026 (Chapter 2 ELI10 Runtime) patterns exactly
- Same 6-step pipeline structure (with additional context retrieval step)
- Same placeholder-only implementation approach
- Same comment-only routing strategy
- Mirrors Chapter 1 structure for consistency

## Outcome

- ✅ Impact: Complete architecture plan ready for task generation. All Chapter 2 quiz runtime scaffolding points covered (runtime module, prompt template, routing, API layer, skills, contract, knowledge source). All phases grouped into clear sections. Each phase specifies file paths, expected content (TODO-level), validation steps, and dependencies. Architecture plan is comprehensive and ready for atomic task generation.
- 🧪 Tests: Architecture plan completeness validation - PASS, Constitution compliance check - PASS
- 📁 Files: 1 file created (plan.md)
- 🔁 Next prompts: `/sp.tasks` to generate atomic implementation tasks
- 🧠 Reflection: Architecture plan follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures comprehensive coverage. Runtime module phase creates ch2_quiz_runtime.py with 6-step blueprint. Prompt template phase creates ch2_quiz_prompt.txt with ROS 2 variables. Runtime engine phase adds Chapter 2 quiz routing (comments only). API layer phase adds Chapter 2 routing comments. Skills phase adds placeholder functions. Knowledge source phase adds quiz chunks function. All phases specify exact expected content at TODO-level. All phases include validation steps. Note: This is a scaffolding extension - no actual AI logic, RAG implementation, or LLM calls should be done, only scaffolding with TODO placeholders. Mirrors Feature 026 structure for consistency. Constitution check passed with 5 PASS and 1 SCAFFOLDING (acceptable for scaffolding phase).

## Evaluation notes (flywheel)

- Failure modes observed: None - architecture planning phase completed successfully
- Graders run and results (PASS/FAIL): Architecture plan completeness - PASS, Constitution compliance - PASS
- Prompt variant (if applicable): Standard /sp.plan workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.tasks` to generate atomic implementation tasks

