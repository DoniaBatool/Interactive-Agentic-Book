---
id: 0002
title: Chapter 2 AI Runtime Engine Integration Planning
stage: plan
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 013-chapter-2-runtime-engine
branch: 013-chapter-2-runtime-engine
user: Leo
command: /sp.plan
labels: ["chapter-2", "runtime-engine", "llm", "rag", "subagents", "chatkit", "planning", "architecture"]
links:
  spec: specs/013-chapter-2-runtime-engine/spec.md
  plan: specs/013-chapter-2-runtime-engine/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/013-chapter-2-runtime-engine/plan.md
tests:
  - Architecture plan completeness validation
  - Constitution check validation
---

## Prompt

User requested: `/sp.plan` following instructions from DOCUMENTATION.md (189-224)

Feature details:
- feature-id: 013-chapter-2-runtime-engine
- title: "Chapter 2 — AI Runtime Engine Integration (LLM Routing, RAG Wiring, Subagents, ChatKit)"
- goal: Provide a detailed architecture plan for activating runtime engine routing for Chapter 2

Requirements:
1. Runtime Routing: Explain how chapter_id=2 flows through run_ai_block(), show breakdown: block → runtime → rag pipeline → provider
2. Subagent Architecture: Describe how Chapter 2 has its own subagents but shares skills, define responsibilities, identify parts that stay TODO
3. Skills Reuse Plan: How formatting_skill, retrieval_skill, prompt_builder_skill will gain chapter-aware branches (placeholders only)
4. RAG Pipeline Link: Conceptual flow of embedding user query, placeholder retrieval context injection
5. ChatKit Integration: Session rules for chapter-based history, tool placeholder definitions
6. File & Folder Plan: List all new files + modifications, include contract files structure
7. Risks / Constraints: No real logic allowed, must remain deterministic and simple, prepare for future model swapping

## Response snapshot

Successfully created comprehensive architecture plan for Chapter 2 runtime engine integration:

**Created Files:**
1. `specs/013-chapter-2-runtime-engine/plan.md` - Complete architecture plan with:
   - Summary and technical context
   - High-level architecture overview with flow diagrams
   - Runtime Routing: Chapter ID-based routing, block → runtime → rag pipeline → provider breakdown
   - Subagent Architecture: Chapter-specific subagents (ch2_*) with shared skills, responsibilities defined, TODO parts identified
   - Skills Reuse Plan: Chapter-aware branches for all 5 skills (retrieval, prompt_builder, formatting, quiz_formatting, diagram)
   - RAG Pipeline Link: Conceptual flow of embedding query, placeholder retrieval context injection
   - ChatKit Integration: Multi-chapter session contexts, Chapter 2 tool definitions
   - File & Folder Plan: 4 new files, 10 updated files, contract files structure
   - Risks / Constraints: 6 risks with mitigations (no real logic, deterministic, model swapping, naming, skills complexity, ChatKit overhead)
   - Acceptance criteria mapping
   - Dependencies & next steps

**Key Architecture Decisions:**
- Runtime Routing: Chapter ID-based routing with simple if/elif structure
- Subagent Architecture: 4 Chapter 2-specific subagents (ch2_*) with shared skills
- Skills Reuse: Chapter-aware skills with chapter_id parameter
- RAG Pipeline: Chapter 2 context retrieval from Qdrant collection "chapter_2"
- ChatKit: Multi-chapter session contexts with Chapter 2 tool definitions
- Configuration: Chapter-specific settings (DEFAULT_CH2_MODEL, DEFAULT_CH2_EMBEDDINGS, ENABLE_CHAPTER_2_RUNTIME)

**Flow Diagrams:**
- Architecture Flow: Frontend → API → Runtime Engine → RAG Pipeline → Skills → Subagents → LLM Provider → Response
- Data Flow: Request → Routing → RAG → Skills → Subagent → LLM → Formatting → Response

**Pattern Consistency:**
- Follows Feature 005 (AI Runtime Engine) and Feature 012 (Chapter 2 RAG) patterns
- Scaffolding-only approach (no real implementation)
- Clear TODO markers and placeholder functions
- ROS 2-specific context documented throughout

## Outcome

- ✅ Impact: Complete architecture plan ready for task generation. All technical decisions documented. Runtime routing, subagent architecture, skills reuse, RAG pipeline link, and ChatKit integration clearly defined. ROS 2-specific context properly mapped. Risk assessment complete with mitigations.
- 🧪 Tests: Architecture plan completeness validation - PASS, Constitution check validation - PASS
- 📁 Files: 1 plan file created (plan.md with comprehensive runtime engine architecture)
- 🔁 Next prompts: `/sp.tasks` to generate implementation task list
- 🧠 Reflection: Plan follows established patterns for maintainability. Clear separation between scaffolding and implementation ensures future developers understand what needs to be built. ROS 2-specific context (concepts, section IDs, subagent patterns) properly documented. All flow diagrams and routing logic clearly defined. Risk assessment comprehensive with mitigations. Chapter 2-specific subagents (ch2_*) provide clear separation while maintaining skills reuse.

## Evaluation notes (flywheel)

- Failure modes observed: None - planning phase completed successfully
- Graders run and results (PASS/FAIL): Architecture plan completeness - PASS, Constitution check - PASS
- Prompt variant (if applicable): Standard /sp.plan workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.tasks` to generate implementation task list
