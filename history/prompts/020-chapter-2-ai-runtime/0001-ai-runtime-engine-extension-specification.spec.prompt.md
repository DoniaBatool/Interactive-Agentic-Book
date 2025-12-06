---
id: 0001
title: AI Runtime Engine Extension Specification for Chapter 2
stage: spec
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 020-chapter-2-ai-runtime
branch: 020-chapter-2-ai-runtime
user: Leo
command: /sp.specify
labels: ["chapter-2", "ai-runtime", "rag", "llm", "subagents", "specification", "backend-ai-architecture"]
links:
  spec: specs/020-chapter-2-ai-runtime/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/020-chapter-2-ai-runtime/spec.md
  - specs/020-chapter-2-ai-runtime/contracts/runtime-extension.yaml
  - specs/020-chapter-2-ai-runtime/checklists/requirements.md
  - specs/020-chapter-2-ai-runtime/research.md
  - specs/020-chapter-2-ai-runtime/data-model.md
  - specs/020-chapter-2-ai-runtime/quickstart.md
tests:
  - Specification quality checklist validation (ALL PASS)
---

## Prompt

User requested: `/sp.specify` following instructions from DOCUMENTATION.md (393-473)

Feature details:
- feature-id: 020-chapter-2-ai-runtime
- title: "AI Runtime Engine Extension — RAG + LLM + Subagent Integration for Chapter 2"
- type: backend-ai-architecture
- goal: Extend the existing AI Runtime Engine (Feature 005) so that Chapter 2 content becomes fully AI-powered. This includes retrieval, embeddings, LLM reasoning, diagram generation, ELI10 explanations, quizzes, and question-answering for all of Chapter 2. No new logic. Only scaffolding, connections, routing, and reuse of existing skills + subagent templates.

Requirements:
1. RAG Collection Setup for Chapter 2: Create ch2_collection.py with TODO stubs
2. Embedding Pipeline Extension: Add chapter=2 support to embedding client
3. Chapter 2 Knowledge Source: Verify chapter_2_chunks.py exists
4. AI Block Runtime Routing Extension: Route chapterId=2 calls to CH2 RAG
5. Subagents Extension: Verify or create Chapter 2 subagents
6. Skills Reuse: Add TODO comments for CH2 support
7. ChatKit Session Support: Extend session manager to track chapterId=2
8. Environment & Config: Add Chapter 2 settings to settings.py and .env.example
9. API Stability: Verify ai_blocks.py routes chapterId=2 correctly

## Response snapshot

Successfully created comprehensive specification for AI Runtime Engine Extension for Chapter 2:

**Created Files:**
1. `specs/020-chapter-2-ai-runtime/spec.md` - Complete specification with:
   - 3 user stories (Developer Extends AI Runtime, System Administrator Configures Settings, Future Developer Implements Logic)
   - 9 functional requirements (RAG Collection Setup, Embedding Pipeline Extension, Knowledge Source, Runtime Routing, Subagents, Skills Reuse, ChatKit, Config, API Stability)
   - Edge cases (5 scenarios)
   - Non-functional requirements (4 categories)
   - Assumptions (6 assumptions)
   - Dependencies (internal: Feature 005, 012, 013; external: Qdrant, Embedding API, LLM API)
   - Out of scope (7 items)
   - Success criteria (7 criteria)
   - Acceptance criteria (8 criteria)

2. `specs/020-chapter-2-ai-runtime/contracts/runtime-extension.yaml` - Runtime extension contract with:
   - RAG Collection Setup (ch2_collection.py structure)
   - Embedding Pipeline Extension (chapter=2 support)
   - Runtime Routing Extension (chapterId=2 routing)
   - Subagents Extension (4 subagent files)
   - Skills Reuse (retrieval_skill.py, prompt_builder_skill.py)
   - ChatKit Session Support (session_manager.py extension)
   - Configuration (settings.py and .env.example)
   - API Stability (ai_blocks.py routing)

3. `specs/020-chapter-2-ai-runtime/checklists/requirements.md` - Specification quality checklist with:
   - Content quality check (ALL PASS)
   - Requirement completeness check (ALL PASS)
   - Feature readiness check (ALL PASS)
   - Validation results (ALL PASS)

4. `specs/020-chapter-2-ai-runtime/research.md` - Research document with:
   - Technology decisions (7 decisions: RAG Collection, Embedding Pipeline, Runtime Routing, Subagents, Skills, ChatKit, Configuration)
   - Industry references (RAG architecture, multi-chapter systems, vector databases, LLM routing)
   - Observations (key points, challenges, technical considerations)
   - Technology stack
   - Next steps

5. `specs/020-chapter-2-ai-runtime/data-model.md` - Data model with:
   - 7 entity definitions (RAG Collection Setup, Embedding Pipeline Extension, Runtime Routing Extension, Chapter 2 Subagents, Skills Reuse, ChatKit Session Support, Configuration)
   - Data relationships diagram
   - Data flow (current scaffolding flow, future implementation flow)
   - Validation summary

6. `specs/020-chapter-2-ai-runtime/quickstart.md` - Quickstart guide with:
   - Prerequisites (Feature 005, 012, 013)
   - Commands (SDD workflow)
   - Folder structure
   - Feature overview (9 extension points)
   - Key files to create/modify (14 files)
   - Implementation steps (5 steps)
   - Success criteria
   - Troubleshooting guide

**Key Specification Details:**
- Extension of Feature 005 (AI Runtime Engine) for Chapter 2
- RAG collection setup: ch2_collection.py with TODO stubs
- Embedding pipeline extension: chapter=2 support
- Runtime routing: chapterId=2 routing to CH2 RAG
- Subagents: Verify or create 4 Chapter 2 subagents
- Skills reuse: Add TODO comments for CH2 support
- ChatKit: Extend session manager to track chapterId=2
- Configuration: Add Chapter 2 settings (QDRANT_COLLECTION_CH2, CH2_EMBEDDING_MODEL, CH2_LLM_MODEL)
- API stability: Verify ai_blocks.py routes chapterId=2 correctly

**Differences from Feature 013:**
- Feature 020 is a more complete extension focusing on RAG collection setup and embedding pipeline extension
- Feature 013 focused on runtime routing and subagents
- Feature 020 adds RAG collection module, embedding pipeline extension, and configuration settings

**Pattern Consistency:**
- Follows Feature 005 (AI Runtime Engine) and Feature 013 (Chapter 2 Runtime Engine) patterns
- Same scaffolding structure and format
- Adapted for Chapter 2 content (ROS 2)
- Includes RAG collection setup and embedding pipeline extension

## Outcome

- ✅ Impact: Complete specification ready for planning phase. All user stories covered with testable requirements. AI Runtime Engine extension architecture clearly defined (RAG collection, embedding pipeline, runtime routing, subagents, skills, ChatKit, configuration). All requirements are testable and measurable. All contract files created.
- 🧪 Tests: Specification quality checklist validation - ALL PASS (content quality, requirement completeness, feature readiness)
- 📁 Files: 6 files created (spec.md, runtime-extension.yaml, requirements.md, research.md, data-model.md, quickstart.md)
- 🔁 Next prompts: `/sp.plan` to create extension plan
- 🧠 Reflection: Specification follows established patterns for maintainability. Clear separation between extension points ensures comprehensive coverage. RAG collection setup and embedding pipeline extension are new additions. All requirements are testable and measurable. Note: This is a scaffolding extension - no actual AI logic implementation should be done, only scaffolding with TODO placeholders. Feature 013 may have created some subagents - verify and extend if needed.

## Evaluation notes (flywheel)

- Failure modes observed: None - specification phase completed successfully
- Graders run and results (PASS/FAIL): Specification quality checklist - ALL PASS
- Prompt variant (if applicable): Standard /sp.specify workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.plan` to create extension plan
