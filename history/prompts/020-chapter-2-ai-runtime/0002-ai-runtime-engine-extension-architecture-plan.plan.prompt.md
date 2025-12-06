---
id: 0002
title: AI Runtime Engine Extension Architecture Plan for Chapter 2
stage: plan
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 020-chapter-2-ai-runtime
branch: 020-chapter-2-ai-runtime
user: Leo
command: /sp.plan
labels: ["chapter-2", "ai-runtime", "rag", "llm", "subagents", "architecture", "plan"]
links:
  spec: specs/020-chapter-2-ai-runtime/spec.md
  plan: specs/020-chapter-2-ai-runtime/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/020-chapter-2-ai-runtime/plan.md
tests:
  - Plan completeness validation
  - Plan actionability validation
---

## Prompt

User requested: `/sp.plan` following instructions from DOCUMENTATION.md (475-514)

Feature details:
- feature-id: 020-chapter-2-ai-runtime
- title: "AI Runtime Engine Extension for Chapter 2"
- goal: Generate a full Claude-style architecture plan including folder structure, runtime flow design, module-level design, subagent orchestration design, skill integration plan, config plan, and API routing plan

Requirements:
1. Folder Structure: All new folders for CH2 rag/collection, subagents, skills extension, chunk files, etc.
2. Runtime Flow Design: CH2 Query → Retrieval Skill (CH2) → RAG Pipeline → Provider → Formatting Skill → Response
3. Module-Level Design: Describe expected files and their TODO-engineered stubs. Define input/output schemas in text (no code). Show how CH2 reuses CH1 modules.
4. Subagent Orchestration Design: ch2_ask_question_agent, ch2_el10_agent, ch2_quiz_agent, ch2_diagram_agent
5. Skill Integration Plan: retrieval_skill extension, prompt_builder_skill extension
6. Config Plan: Env variables, Settings extensions
7. API Routing Plan: ai_blocks → runtime.engine → chapter switch → subagents → TODO return

## Response snapshot

Successfully created comprehensive architecture plan for AI Runtime Engine Extension for Chapter 2:

**Created Files:**
1. `specs/020-chapter-2-ai-runtime/plan.md` - Complete architecture plan with:
   - Summary (extension of Feature 005 for Chapter 2)
   - Technical context (dependencies, constraints, scale/scope)
   - Folder structure (new directories, existing directories to extend)
   - Runtime flow design (CH2 Query → Retrieval Skill → RAG Pipeline → Provider → Formatting Skill → Response)
   - Module-level design (9 modules with input/output schemas):
     1. RAG Collection Setup (ch2_collection.py)
     2. Embedding Pipeline Extension (embedding_client.py)
     3. Chapter 2 Knowledge Source (chapter_2_chunks.py)
     4. AI Block Runtime Routing Extension (engine.py)
     5. Subagents Extension (4 subagent files)
     6. Skills Reuse (retrieval_skill.py, prompt_builder_skill.py)
     7. ChatKit Session Support (session_manager.py)
     8. Configuration (settings.py, .env.example)
     9. API Stability (ai_blocks.py)
   - Subagent orchestration design (4 subagents with orchestration flow)
   - Skill integration plan (retrieval_skill extension, prompt_builder_skill extension)
   - Config plan (environment variables, settings extensions)
   - API routing plan (ai_blocks → runtime.engine → chapter switch → subagents → TODO return)
   - Integration points (Feature 005, 012, 013)
   - Acceptance checks (4 categories)
   - Next steps

**Key Plan Details:**
- Runtime flow: CH2 Query → Retrieval Skill (CH2) → RAG Pipeline → Provider → Formatting Skill → Response
- 9 modules to create/update: RAG collection, embedding extension, knowledge source, runtime routing, subagents, skills, ChatKit, config, API
- 4 subagents: ch2_ask_question_agent, ch2_el10_agent, ch2_quiz_agent, ch2_diagram_agent
- 2 skills to extend: retrieval_skill, prompt_builder_skill
- Configuration: 3 new settings (QDRANT_COLLECTION_CH2, CH2_EMBEDDING_MODEL, CH2_LLM_MODEL)
- API routing: ai_blocks → runtime.engine → chapter switch → subagents → TODO return

**Differences from Feature 013:**
- Feature 020 adds RAG collection module (ch2_collection.py)
- Feature 020 adds embedding pipeline extension (chapter=2 support)
- Feature 020 adds configuration settings (QDRANT_COLLECTION_CH2, CH2_EMBEDDING_MODEL, CH2_LLM_MODEL)
- Feature 013 focused on runtime routing and subagents
- Feature 020 is a more complete extension

**Pattern Consistency:**
- Follows Feature 005 (AI Runtime Engine) and Feature 013 (Chapter 2 Runtime Engine) patterns
- Same scaffolding structure and format
- Adapted for Chapter 2 content (ROS 2)
- Shows how CH2 reuses CH1 modules
- Includes RAG collection setup and embedding pipeline extension

## Outcome

- ✅ Impact: Complete architecture plan ready for task generation. All extension points defined (RAG collection, embedding pipeline, runtime routing, subagents, skills, ChatKit, configuration). Runtime flow clearly designed (CH2 Query → Retrieval Skill → RAG Pipeline → Provider → Formatting Skill → Response). Module-level design comprehensive (9 modules with input/output schemas). Subagent orchestration detailed (4 subagents with orchestration flow). Skill integration plan complete (2 skills to extend). Config plan detailed (environment variables, settings extensions). API routing plan clear (ai_blocks → runtime.engine → chapter switch → subagents → TODO return). Integration points documented. Acceptance checks defined. Plan is actionable and ready for direct conversion into tasks.
- 🧪 Tests: Plan completeness validation - PASS, Plan actionability validation - PASS
- 📁 Files: 1 plan file created (plan.md with comprehensive architecture plan)
- 🔁 Next prompts: `/sp.tasks` to create implementation tasks
- 🧠 Reflection: Plan follows established patterns for maintainability. Clear separation between extension points ensures comprehensive coverage. RAG collection setup and embedding pipeline extension are new additions. All modules show how CH2 reuses CH1 modules. All TODO placeholders are descriptive and actionable. Note: This is a scaffolding extension - no actual AI logic implementation should be done, only scaffolding with TODO placeholders. Feature 013 may have created some subagents - verify and extend if needed.

## Evaluation notes (flywheel)

- Failure modes observed: None - planning phase completed successfully
- Graders run and results (PASS/FAIL): Plan completeness - PASS, Plan actionability - PASS
- Prompt variant (if applicable): Standard /sp.plan workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.tasks` to create implementation tasks
