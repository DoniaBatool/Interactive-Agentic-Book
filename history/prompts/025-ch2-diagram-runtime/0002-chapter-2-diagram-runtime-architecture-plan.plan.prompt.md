---
id: 0002
title: Chapter 2 Diagram Generator Runtime Architecture Plan
stage: plan
date: 2025-01-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: 025-ch2-diagram-runtime
branch: 003-chapter-1-content
user: Leo
command: /sp.plan
labels: ["chapter-2", "backend", "diagram", "runtime", "architecture", "planning"]
links:
  spec: specs/025-ch2-diagram-runtime/spec.md
  plan: specs/025-ch2-diagram-runtime/plan.md
  tasks: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/025-ch2-diagram-runtime/plan.md
tests:
  - Architecture plan completeness validation
  - Constitution compliance check
---

## Prompt

User requested: `/sp.plan` following instructions from DOCUMENTATION.md (78-122)

Feature details:
- feature-id: 025-ch2-diagram-runtime
- goal: Build the scaffolding required to generate diagrams for Chapter 2. No diagram generation logic, only structured placeholders.
- plan sections:
  1. Diagram Runtime Module - Create ch2_diagram_runtime.py with run() function and empty steps (validate → prompt → rag → llm → format), all TODO, no logic
  2. Prompt Template - Create ch2_diagram_prompt.txt with placeholder prompt variables ({{diagram_type}}, {{chapter_id}}, {{concepts}})
  3. Runtime Engine - Extend engine.py routing: if block_type == "diagram" and chapterId == 2 → call placeholder diagram runtime
  4. API Layer - Update ai_blocks.py diagram endpoint so chapterId=2 triggers CH2 runtime
  5. Contracts - Create diagram-contract.yaml documenting expected diagram types, placeholder naming rules, runtime flow description
  6. Skills - Extend prompt_builder_skill and formatting_skill with empty CH2 placeholder functions
  7. Validation - Ensure backend runs, ensure no logic exists

## Response snapshot

Successfully created comprehensive architecture plan for Chapter 2 Diagram Generator Runtime:

**Created Files:**
1. `specs/025-ch2-diagram-runtime/plan.md` - Complete architecture plan with:
   - Summary and Technical Context
   - Constitution Check (all 6 principles - 5 PASS, 1 SCAFFOLDING)
   - Architecture Overview (system architecture diagram, key components, integration points)
   - Implementation Phases (7 phases with tasks, deliverables, validation)
   - Key Decisions (4 decisions with rationale)
   - Risk Analysis (3 risks with mitigation strategies)
   - Validation Strategy (pre, during, post implementation)
   - Success Criteria (8 criteria)
   - Next Steps

**Key Architecture Details:**
- **System Architecture**: API Layer → Runtime Engine → Chapter 2 Diagram Runtime → Prompt Template / Skills Layer
- **Request Flow**: API Endpoint → Runtime Engine (if block_type == "diagram" AND chapterId == 2) → ch2_diagram_runtime.run() → 5-Step Pipeline (all TODO) → Response
- **Implementation Phases**: 7 phases
  - Phase 1: Diagram Runtime Module (ch2_diagram_runtime.py with 5-step blueprint)
  - Phase 2: Prompt Template (ch2_diagram_prompt.txt with 3 variables)
  - Phase 3: Runtime Engine Routing (comment-only routing)
  - Phase 4: API Layer Update (chapterId=2 routing comments)
  - Phase 5: Contracts (diagram-contract.yaml already created)
  - Phase 6: Skills Extension (2 placeholder functions)
  - Phase 7: Validation (backend startup, imports, logic verification)
- **Key Decisions**: 4 decisions
  - Decision 1: Create Chapter 2-Specific Runtime Module (chosen: create ch2_diagram_runtime.py as separate module)
  - Decision 2: Create Chapter 2 Prompt Template (chosen: create ch2_diagram_prompt.txt with ROS 2-specific placeholders)
  - Decision 3: Placeholder-Only Implementation (chosen: placeholder-only with TODO comments)
  - Decision 4: Comment-Only Routing (chosen: comment-only routing with TODO markers)
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

**5-Step Pipeline Blueprint:**
1. Validate diagram request (TODO)
2. Build prompt (placeholder)
3. Call RAG (placeholder)
4. Call provider LLM (placeholder)
5. Format response (placeholder)

**Integration Points:**
- AI Runtime Engine (Feature 024): Routes diagram blocks to Chapter 2 diagram runtime
- Chapter 1 Diagram Runtime (Feature 008): Reference structure for Chapter 2 implementation
- Skills Layer: Provides prompt building and formatting capabilities
- API Layer: Receives diagram requests and routes to appropriate runtime

**Pattern Consistency:**
- Follows Feature 008 (Chapter 1 Diagram Engine) patterns exactly
- Same 5-step pipeline structure
- Same placeholder-only implementation approach
- Same comment-only routing strategy
- Mirrors Chapter 1 structure for consistency

## Outcome

- ✅ Impact: Complete architecture plan ready for task generation. All Chapter 2 diagram runtime scaffolding points covered (runtime module, prompt template, routing, API layer, skills, contract). All phases grouped into clear sections. Each phase specifies file paths, expected content (TODO-level), validation steps, and dependencies. Architecture plan is comprehensive and ready for atomic task generation.
- 🧪 Tests: Architecture plan completeness validation - PASS, Constitution compliance check - PASS
- 📁 Files: 1 file created (plan.md)
- 🔁 Next prompts: `/sp.tasks` to generate atomic implementation tasks
- 🧠 Reflection: Architecture plan follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures comprehensive coverage. Runtime module phase creates ch2_diagram_runtime.py with 5-step blueprint. Prompt template phase creates ch2_diagram_prompt.txt with ROS 2 variables. Runtime engine phase adds Chapter 2 diagram routing (comments only). API layer phase adds Chapter 2 routing comments. Skills phase adds placeholder functions. All phases specify exact expected content at TODO-level. All phases include validation steps. Note: This is a scaffolding extension - no actual AI logic, RAG implementation, or LLM calls should be done, only scaffolding with TODO placeholders. Mirrors Feature 008 structure for consistency. Constitution check passed with 5 PASS and 1 SCAFFOLDING (acceptable for scaffolding phase).

## Evaluation notes (flywheel)

- Failure modes observed: None - architecture planning phase completed successfully
- Graders run and results (PASS/FAIL): Architecture plan completeness - PASS, Constitution compliance - PASS
- Prompt variant (if applicable): Standard /sp.plan workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.tasks` to generate atomic implementation tasks

