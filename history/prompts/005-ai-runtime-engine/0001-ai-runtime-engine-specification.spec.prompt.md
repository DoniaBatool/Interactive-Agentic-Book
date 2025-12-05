---
id: 0001
title: AI Runtime Engine Specification
stage: spec
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 005-ai-runtime-engine
branch: 005-ai-runtime-engine
user: Leo
command: /sp.specify
labels: ["ai-runtime", "llm", "rag", "chatkit", "scaffolding", "backend"]
links:
  spec: specs/005-ai-runtime-engine/spec.md
  plan: null
  tasks: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/005-ai-runtime-engine/spec.md
  - specs/005-ai-runtime-engine/contracts/content-schema.md
  - specs/005-ai-runtime-engine/checklists/requirements.md
tests:
  - Manual: Specification completeness review
  - Manual: Requirements validation checklist
---

## Prompt

/sp.specify

feature-id: 005-ai-runtime-engine

title: "AI Runtime Engine for Chapter 1 — LLM, RAG, ChatKit Integration"

type: backend-ai-architecture

goal:
  Build the complete AI Runtime Engine that powers all Chapter 1 interactive blocks.
  This feature connects the frontend AI components to real LLM calls, adds the full RAG
  pipeline (embeddings, Qdrant collections, retrieval), configures ChatKit, defines
  subagents and reusable skills, and provides a unified inference interface.

requirements:
  # 1 — AI Provider Integration (Gemini, OpenAI, or DeepSeek)
  - Create backend/app/ai/providers/base_llm.py (abstract interface)
  - Create backend/app/ai/providers/openai_provider.py (scaffold only)
  - Create backend/app/ai/providers/gemini_provider.py (scaffold only)
  - Provider must support: prompt: str, system: str | None, messages: list | None, temperature: float, return full response

  # 2 — Embeddings + RAG Infrastructure
  - Create backend/app/ai/embeddings/embedding_client.py
      - TODO placeholders for: generate_embedding(text), batch_embed(chunks)
  - Create backend/app/ai/rag/qdrant_store.py
      - TODO placeholders: create_collection(), upsert_vectors(), similarity_search(query)
  - RAG Pipeline Module: backend/app/ai/rag/pipeline.py
      - Steps: 1. Retrieve chapter chunks, 2. Embed user query, 3. Perform Qdrant search, 4. Construct retrieval context, 5. Pass into provider LLM
      - All steps placeholder only, no real logic.

  # 3 — Chapter Knowledge Source
  - Create backend/app/content/chapters/chapter_1_chunks.py
  - Add TODO: function "get_chapter_chunks()" returns list of text chunks (placeholder).

  # 4 — AI Block Runtime API
  - Update backend/app/api/ai_blocks.py so all 4 endpoints call: from app.ai.runtime.engine import run_ai_block
  - Create backend/app/ai/runtime/engine.py
      - router → RAG → LLM selection → response formatting
      - No real logic, only placeholder flow comments.

  # 5 — Subagents + Skills Architecture
  - Create folder backend/app/ai/subagents/
        - ask_question_agent.py
        - explain_el10_agent.py
        - quiz_agent.py
        - diagram_agent.py
  - Create folder backend/app/ai/skills/
        - retrieval_skill.py
        - formatting_skill.py
        - prompt_builder_skill.py
  - Each file contains: TODO blueprint, Expected input/output signature, No business logic

  # 6 — ChatKit Integration Scaffold
  - Create backend/app/ai/chatkit/session_manager.py
      - TODO: create session, append messages, store history
  - Create backend/app/ai/chatkit/tools.py
      - Document tools needed later (diagram, quiz, explanation)

  # 7 — Config & Environment
  - Update backend/app/config/settings.py:
      - Add ENV vars: AI_PROVIDER (default=openai), QDRANT_COLLECTION_CH1, EMBEDDING_MODEL, LLM_MODEL
  - Update .env.example with these new variables.

  # 8 — API Contract Stub
  - Create specs/005-ai-runtime-engine/contracts/ai-block-runtime.yaml
      - Describe high-level runtime flow.
      - No schemas for actual AI outputs.

acceptance_criteria:
  - All modules exist exactly at the required paths.
  - No AI logic implemented; only scaffold + TODO comments.
  - All imports resolve; backend must start without runtime errors.
  - ai_blocks.py now routes to runtime engine module.
  - RAG pipeline, subagents, skills, ChatKit all exist as placeholder frameworks.
  - .env.example updated.

success_message: |
  AI Runtime Engine scaffolding created successfully. All modules, providers,
  RAG pipeline files, subagents, skills, and ChatKit scaffolding are ready.

## Response snapshot

Successfully created comprehensive specification for Feature 005: AI Runtime Engine for Chapter 1.

**Specification Created**:
- ✅ `specs/005-ai-runtime-engine/spec.md` - Complete specification with:
  - 3 User Stories (Developer Setup, System Admin Config, Future Developer)
  - 16 Functional Requirements (FR-001 through FR-016)
  - 9 Success Criteria (SC-001 through SC-009)
  - 7 Constraints (C-001 through C-007)
  - Dependencies and Assumptions documented
  - 10 Out of Scope items clearly defined

**Standard Files Created**:
- ✅ `contracts/content-schema.md` - Complete schema definitions:
  - AI Provider Interface Schema
  - Embedding Client Schema
  - RAG Pipeline Schema
  - Runtime Engine Schema
  - Subagent Schemas (4 agents)
  - Skill Schemas (3 skills)
  - ChatKit Schema
  - Configuration Schema
  - Validation Checklist

- ✅ `checklists/requirements.md` - Specification quality checklist:
  - Content Quality validation (PASS)
  - Requirement Completeness validation (PASS)
  - Feature Readiness validation (PASS)
  - All items pass, ready for planning

**Key Highlights**:
- Comprehensive scaffolding specification covering all 8 requirement areas
- Clear separation: providers, RAG, runtime, subagents, skills, ChatKit
- Explicit "no real AI logic" constraint maintained
- All file paths and function signatures specified
- Ready for `/sp.plan` phase

## Outcome

- ✅ Impact: Complete AI Runtime Engine scaffolding specification ready for architectural planning
- 🧪 Tests: Manual specification review completed - all requirements testable, success criteria measurable
- 📁 Files: 3 files created (spec.md, content-schema.md, requirements.md)
- 🔁 Next prompts: `/sp.plan` to create architecture plan, then `/sp.tasks` for implementation tasks
- 🧠 Reflection: Specification follows SDD workflow strictly. All scaffolding requirements clearly defined with explicit constraints. Architecture foundation established for future AI implementation.

## Evaluation notes (flywheel)

- Failure modes observed: None - specification creation successful
- Graders run and results (PASS/FAIL): Manual specification review PASS - all requirements complete, testable, and properly scoped
- Prompt variant (if applicable): Standard /sp.specify command with detailed requirements
- Next experiment (smallest change to try): Proceed to `/sp.plan` to create detailed architecture plan for AI Runtime Engine scaffolding

