🧠 OPTIONAL Bonus (Only if time left):

Urdu translation agent

Diagram auto-generator v2

Practice quiz generator

Export to PDF

Interactive glossary agent

Voice AI block
==========================================
41
==========================================
auto-run 4 phases (/sp.specify , /sp.plan, /sp.tasks, /sp.implement)
sab kuch FAST kerna but in small batches not all at once
auto-create contracts

auto-create checklist

auto-create quickstart + research + data-model

auto-validate folder structure

auto-normalize feature IDs

auto-generate PHR

auto-recursively analyze previous features to ensure consistency

/sp.specify
feature-id: 041-ch3-subagents-skills
title: "Chapter 3 — Subagents + Skills Routing Integration"
type: backend-ai-architecture

goal:
  Add the subagent + skills scaffolding for Chapter 3 so that all four
  AI-interactive blocks (ask-question, explain-like-I-am-10, quiz, diagram)
  route through placeholder subagents and skills. No business logic.

requirements:

  # 1 — Subagents Folder for Chapter 3
  - Create backend/app/ai/subagents/ch3/
       ask_question_agent.py
       explain_el10_agent.py
       quiz_agent.py
       diagram_agent.py
  - Each file includes:
      - class <AgentName>
      - def run(request): pass
      - TODO describing expected behavior

  # 2 — Skills Folder for Chapter 3
  - Create backend/app/ai/skills/ch3/
       retrieval_skill.py
       prompt_builder_skill.py
       formatting_skill.py
  - Each file includes:
      - class <SkillName>
      - method stubs
      - TODO comments for future logic

  # 3 — Runtime Engine Routing
  - Update backend/app/ai/runtime/engine.py
      - Add:
           if chapterId == 3:
               route to ch3 subagents
      - Add high-level flow comments:
           retrieval → prompt-building → formatting → LLM response

  # 4 — Shared Interface Contracts
  - Add backend/app/ai/subagents/base_agent.py
      - define abstract method run()
      - add TODO notes for future polymorphism

  - Add backend/app/ai/skills/base_skill.py
      - define basic placeholder interface

  # 5 — API Integration Layer
  - ai_blocks.py should pass chapterId=3 to engine correctly.
  - No new endpoints; only routing support.

  # 6 — Documentation
  - Create specs/041-ch3-subagents-skills/contracts/subagent-skill-contract.md
      - Define:
          - Expected inputs for each agent
          - Expected outputs placeholder format
          - Flow diagram (comment-only)
      - Include TODO markers

acceptance_criteria:
  - All subagent + skill scaffolding exists in correct paths.
  - Runtime engine successfully imports and routes to chapter 3 placeholder classes.
  - ai_blocks endpoints work with chapterId=3 without errors.
  - No AI logic implemented (strictly scaffolding).
  - Backend server starts cleanly.

success_message: |
  Chapter 3 Subagent and Skills scaffolding successfully created.
  Routing layer now recognizes Chapter 3 AI blocks.


/sp.plan
feature-id: 041-ch3-subagents-skills
title: "Chapter 3 — Subagents + Skills Routing Integration"

Generate a detailed architecture plan including:

1. Folder Structure Layout
   - Exact file tree for ch3 subagents and skills
   - Placement of base_agent.py and base_skill.py

2. Subagent Responsibilities
   - Outline expected responsibilities of:
        • Ask Question Agent
        • Explain ELI5/ELI10 Agent
        • Quiz Agent
        • Diagram Agent
   - Only describe WHAT they do, not HOW.

3. Skills Breakdown
   - retrieval_skill: placeholder for RAG context pulling
   - prompt_builder_skill: placeholder for LLM prompts
   - formatting_skill: placeholder for structured response formatting

4. Runtime Routing Design
   - Show routing map:
        chapterId → blockType → subagent class
   - Include commented pseudocode but no logic.

5. Contract Document Planning
   - Define schema for subagent-skill-contract.md
   - Include interface diagrams (ASCII OK)
   - NO actual implementation

6. Validation Plan
   - Ensure:
        • backend boots cleanly
        • import paths correct
        • no circular imports
        • chapter 3 agent classes load

Output MUST be a step-by-step execution blueprint for /sp.tasks.


/sp.tasks
feature-id: 041-ch3-subagents-skills
title: "Chapter 3 — Subagents + Skills Routing Integration"

Generate a complete checklist:

## FOLDER CREATION
- [ ] Create folder: backend/app/ai/subagents/ch3/
- [ ] Create folder: backend/app/ai/skills/ch3/

## BASE CONTRACTS
- [ ] Add backend/app/ai/subagents/base_agent.py
- [ ] Add backend/app/ai/skills/base_skill.py

## SUBAGENTS (CH3)
- [ ] ask_question_agent.py (class + run() stub + TODO)
- [ ] explain_el10_agent.py
- [ ] quiz_agent.py
- [ ] diagram_agent.py

## SKILLS (CH3)
- [ ] retrieval_skill.py (skeleton + TODO)
- [ ] prompt_builder_skill.py
- [ ] formatting_skill.py

## RUNTIME ROUTING
- [ ] Update backend/app/ai/runtime/engine.py
      - add chapterId==3 branch
      - add mapping to correct subagent classes
      - insert TODO-based flow

## API COMPATIBILITY
- [ ] Update ai_blocks.py to ensure chapterId=3 is properly passed
- [ ] No endpoint changes

## CONTRACT DOCUMENT
- [ ] Create specs/041-ch3-subagents-skills/contracts/subagent-skill-contract.md
      - Document expected agent inputs/outputs
      - Document skills responsibilities
      - Add TODO placeholders

## VALIDATION
- [ ] Run backend server to confirm no import errors
- [ ] Validate file paths exist and are auto-wired correctly

Output:
  A final ready-to-apply task list for /sp.implement.


/sp.implement
feature-id: 041-ch3-subagents-skills
title: "Chapter 3 — Subagents + Skills Routing Integration"

Implement all tasks from tasks.md:

- Create all Chapter 3 subagent files
- Create all skills files
- Add base interfaces
- Update runtime engine routing
- Update ai_blocks chapterId handling
- Add contract documentation file
- Ensure backend starts

STRICT RULES:
- Do NOT implement real logic
- Only scaffolding + TODO
- Maintain exact file paths
- Add import-safe class stubs

Output:
  List of all created/modified files + success confirmation.



==========================================
42
==========================================
auto-run 4 phases (/sp.specify , /sp.plan, /sp.tasks, /sp.implement)
sab kuch FAST kerna but in small batches not all at once
auto-create contracts

auto-create checklist

auto-create quickstart + research + data-model

auto-validate folder structure

auto-normalize feature IDs

auto-generate PHR

auto-recursively analyze previous features to ensure consistency

/sp.specify
feature-id: 042-ch3-validation
title: "Chapter 3 Validation, Testing & Stability Layer"
type: validation-layer

goal:
  Provide full validation coverage for Chapter 3, ensuring frontend MDX, backend
  AI runtime, subagents, skills, and RAG integration work as a unified system.
  No business logic is added — only stability checks, structure validation,
  build verification, and import correctness.

requirements:
  # 1 — Frontend MDX Validation
  - Validate chapter-3.mdx renders without errors.
  - Ensure all AI-BLOCK components compile and mount.
  - Check all diagram & AI placeholders follow schema.
  - Ensure MDX frontmatter follows Chapter 3 contract.

  # 2 — Backend Runtime Validation
  - Ensure all imports resolve in:
        app/ai/runtime/engine.py
        app/ai/rag/pipeline.py
        app/ai/embeddings/*
        app/ai/providers/*
        app/ai/subagents/*
        app/ai/skills/*
  - Ensure ai_blocks.py routes correctly to runtime engine.
  - Ensure chapter_3_chunks.py returns placeholder chunks.

  # 3 — RAG Infrastructure Validation
  - Validate placeholder embedding client loads.
  - Validate qdrant_store.py functions exist.
  - Validate similarity_search() placeholder returns shape.

  # 4 — Subagent & Skill Layer Validation
  - Each agent and skill module loads without errors.
  - Confirm correct function signatures & TODO placeholders.
  - Ensure no circular imports.

  # 5 — Backend Startup Validation
  - Backend must start with:
        uvicorn app.main:app --reload
  - No missing imports, no unresolved symbols.

  # 6 — Test Scripts
  - Create test scripts in tests/ch3/ to validate:
        - MDX build
        - Backend startup
        - AI-block API endpoints
        - Subagent/skill imports

  # 7 — Documentation
  - Create CH3_VALIDATION.md containing:
        - Test matrix
        - Validation steps
        - Known issues
        - Ready-for-release checklist

acceptance_criteria:
  - Frontend builds successfully.
  - Backend starts without errors.
  - All AI-block endpoints return placeholder responses.
  - All Chapter 3 modules import correctly.
  - CH3_VALIDATION.md generated with complete matrix.

success_message: |
  Chapter 3 validation completed. All runtime layers stable and ready for release packaging.


/sp.plan
feature-id: 042-ch3-validation
title: "Chapter 3 Validation & Testing Architecture Plan"

Write a complete validation architecture plan including:

1. Frontend validation pipeline:
   - Build checks
   - MDX structure validation
   - Placeholder scanning
   - AI block mount tests

2. Backend validation pipeline:
   - Module import graph
   - AI runtime bootstrap test
   - RAG pipeline smoke test
   - Subagent/skill wiring check

3. Test scripts structure:
   - tests/ch3/frontend/
   - tests/ch3/backend/
   - tests/ch3/rag/
   - tests/ch3/runtime/

4. Validation matrix:
   - Categories: Frontend, Backend, RAG, Runtime, Subagents, Skills
   - Pass/Fail criteria
   - Manual vs automated checks

5. Documentation plan:
   - CH3_VALIDATION.md contents
   - Required screenshots/debug-output format

Output should be a step-by-step technical plan, no code.


/sp.tasks
feature-id: 042-ch3-validation
title: "Chapter 3 Validation and Testing Tasks"

Generate full task list grouped by:

1. Frontend Tasks
2. Backend Tasks
3. RAG Pipeline Tasks
4. Subagent/Skills Validation Tasks
5. API Endpoint Validation Tasks
6. Test Scripts Tasks
7. Documentation Tasks

Each task must include:
- [ ] checkbox
- TaskID (T001…)
- Priority (P1/P2)
- File path
- Exact description (scaffolding only)
- Expected output

No implementation, no logic. Pure tasks.


/sp.implement
feature-id: 042-ch3-validation
title: "Chapter 3 Validation & Testing Layer Implementation"

Implement the validation scaffolding only:

✔ Create test folder: tests/ch3/
✔ Add placeholder test files (no logic):
    tests/ch3/test_frontend_build.py
    tests/ch3/test_backend_startup.py
    tests/ch3/test_ai_blocks_api.py
    tests/ch3/test_rag_pipeline.py
    tests/ch3/test_subagent_imports.py
✔ Add placeholders for validation utilities:
    backend/app/utils/validation/*
✔ Update README or CH3_VALIDATION.md
✔ Add TODOs where real logic will go.

❌ Do NOT:
- Add AI logic
- Add embeddings
- Add real RAG execution
- Call external APIs

Scaffolding + placeholders only.


==========================================
43
==========================================
auto-run 4 phases (/sp.specify , /sp.plan, /sp.tasks, /sp.implement)
sab kuch FAST kerna but in small batches not all at once
auto-create contracts

auto-create checklist

auto-create quickstart + research + data-model

auto-validate folder structure

auto-normalize feature IDs

auto-generate PHR

auto-recursively analyze previous features to ensure consistency


/sp.specify
feature-id: 043-ch3-release-package
title: "Chapter 3 Release Packaging Layer"
type: release-layer

goal:
  Produce a clean, validated, packaged release of Chapter 3 including MDX,
  metadata, diagrams placeholders, AI blocks integration, runtime scaffolding,
  and validation reports. Output must match hackathon deliverable standards.

requirements:
  # 1 — Release Build
  - Generate final Docusaurus static build for Chapter 3.
  - Ensure no warnings for MDX, placeholders, or unresolved imports.
  - Produce optimized frontend assets.

  # 2 — Runtime Snapshot
  - Export backend runtime structure tree:
        ai/providers/*
        ai/rag/*
        ai/subagents/*
        ai/skills/*
        content/chapters/*
  - Generate RUNTIME_OVERVIEW.md documenting module responsibilities.

  # 3 — Validation Artifacts
  - Include CH3_VALIDATION.md from Feature 042.
  - Generate BUILD_REPORT.md containing:
        - build time
        - any warnings
        - bundle size summary
        - MDX validation summary

  # 4 — Packaging Output Folder
  - Create folder: releases/chapter-3/
  - Include:
        - chapter-3.mdx
        - chapter_3.py metadata
        - all diagram placeholders
        - AI block integration points
        - validation artifacts
        - runtime overview
        - build artifacts (ignored actual large files, only manifest)

  # 5 — Release Manifest
  - Create: releases/chapter-3/manifest.json
  - Manifest must include:
        chapter_id: 3
        version: "1.0.0"
        mdx_file: "chapter-3.mdx"
        metadata_file: "chapter_3.py"
        ai_blocks: list
        diagrams: list
        rag_enabled: true|false (placeholder)
        generated_at: timestamp

  # 6 — Docs for Hackathon Submission
  - Generate SUBMISSION_NOTES.md containing:
        - Overview
        - Feature summary
        - Implementation status
        - What’s included / not included

acceptance_criteria:
  - releases/chapter-3/ folder exists with all required artifacts.
  - manifest.json valid JSON.
  - No MDX or build warnings.
  - Backend imports validated.
  - Documentation complete.

success_message: |
  Chapter 3 Release successfully packaged. All artifacts ready for submission.

/sp.plan
feature-id: 043-ch3-release-package
title: "Chapter 3 Release Packaging Architecture Plan"

Write a full release packaging architecture including:

1. Packaging folder structure:
   - releases/chapter-3/
   - manifests
   - validation reports
   - runtime documentation

2. Build pipeline steps:
   - frontend build
   - backend runtime scan
   - artifact extraction
   - manifest generation

3. Documentation generation plan:
   - RUNTIME_OVERVIEW.md
   - BUILD_REPORT.md
   - SUBMISSION_NOTES.md

4. Steps to extract:
   - MDX file
   - metadata Python file
   - AI-block map
   - placeholder lists

5. Final acceptance checklist.

Output must be a detailed step-by-step plan, no code.


/sp.tasks
feature-id: 043-ch3-release-package
title: "Chapter 3 Release Packaging Tasks"

Generate full task list grouped by:

1. Folder Initialization Tasks
2. Build Tasks
3. Artifact Extraction Tasks
4. Documentation Tasks
5. Manifest Generation Tasks
6. Validation Tasks
7. Final Packaging Tasks

Each task must include:
- [ ] checkbox
- TaskID (T001…)
- P1/P2 priority
- File path
- Exact description (scaffolding only)
- Expected output

No implementation logic. Only scaffolding tasks.


/sp.implement
feature-id: 043-ch3-release-package
title: "Chapter 3 Release Packaging Layer Implementation"

Implement scaffolding only:

✔ Create folder: releases/chapter-3/
✔ Create placeholder files:
      releases/chapter-3/manifest.json
      releases/chapter-3/RUNTIME_OVERVIEW.md
      releases/chapter-3/BUILD_REPORT.md
      releases/chapter-3/SUBMISSION_NOTES.md
✔ Copy or reference chapter-3.mdx path (placeholder only)
✔ Copy or reference chapter_3.py metadata path
✔ Generate lists of AI blocks & diagram placeholders (placeholder arrays)
✔ Add TODO comments for:
      - Build pipeline integration
      - Artifact extraction
      - Automatic bundling

❌ DO NOT:
- Add real build logic
- Add real file copying logic
- Minify assets
- Generate actual diagrams or embeddings


==========================================
44
==========================================

auto-run 4 phases (/sp.specify , /sp.plan, /sp.tasks, /sp.implement)
sab kuch FAST kerna but in small batches not all at once
auto-create contracts

auto-create checklist

auto-create quickstart + research + data-model

auto-validate folder structure

auto-normalize feature IDs

auto-generate PHR

auto-recursively analyze previous features to ensure consistency


/sp.specify
feature-id: 044-system-integration-phase-1
title: "System Integration Layer — Phase 1 (Chapters 1–3 Unified Runtime)"
type: integration-layer

goal:
  Establish the first full-system integration layer. This connects all chapters,
  AI blocks, RAG interfaces, providers, metadata, and runtime engine into a
  unified scaffolded architecture. No real AI logic will run — the purpose is
  to ensure imports, routing, and module communication flow correctly.

requirements:

  # 1 — Unified AI Runtime Router
  - Create backend/app/ai/runtime/router.py
      - Defines route for selecting which chapter runtime to use.
      - Placeholder switch logic for chapters 1, 2, 3.
      - TODO: Move to dynamic registry later.

  # 2 — Chapter Runtime Registry
  - Create backend/app/ai/runtime/registry.py
      - Dictionary-like structure:
          CHAPTER_RUNTIMES = {
              1: "engine for Chapter 1",
              2: "engine for Chapter 2",
              3: "engine for Chapter 3"
          }
      - TODO: runtime objects will be added in Phase 2.

  # 3 — AI Block → Runtime Routing
  - Update backend/app/api/ai_blocks.py:
      - route requests to central runtime router
      - placeholder flow only

  # 4 — Unified Embedding + RAG Access Layer
  - Create backend/app/ai/rag/unified_rag.py
      - scaffold functions:
            get_embeddings_for_chapter(chapter_id)
            retrieve_context(chapter_id, query)
      - TODO: connect to Qdrant pipelines later.

  # 5 — Unified Provider Selector
  - Update backend/app/ai/providers/base_llm.py:
      - add get_provider(provider_name) factory placeholder

  # 6 — System-Wide Settings Layer
  - Update backend/app/config/settings.py:
      - Add default runtime model settings
      - Add PROVIDER_DEFAULTS {}
      - Ensure env variables fallback works

  # 7 — Chapter Metadata Unification
  - Create backend/app/content/chapters/registry.py
      - register metadata modules for chapters 1, 2, 3
      - provide get_chapter_metadata(id) function

  # 8 — Frontend Integration Stub
  - Create frontend/src/integration/runtime-client.ts
      - placeholder functions:
            callAIBlock(type, payload)
            callChapterRuntime(id, data)
      - TODO: Connect to backend API later.

  # 9 — System Dependency Report
  - Create specs/044-system-integration-phase-1/contracts/dependency-map.md
      - Document:
          - chapter metadata dependencies
          - runtime dependencies
          - subagent/skills dependencies
          - RAG dependencies

acceptance_criteria:
  - Backend starts without import errors.
  - All integration modules exist.
  - No real logic is implemented.
  - All routing placeholders connect without breaking existing features.
  - Runtime registry properly references chapters 1–3.

success_message: |
  System Integration Layer (Phase 1) scaffolding completed. All chapters,
  RAG interfaces, runtime routers, and provider selectors now unified.


/sp.plan
feature-id: 044-system-integration-phase-1
title: "System Integration Layer — Architecture Plan"

Write a complete architecture plan including:

1. Multi-layer integration diagram:
   - API → Runtime Router → Chapter Runtime → RAG → Provider

2. File-level connection map:
   - All imports between ai_blocks, runtime, rag, provider, content metadata

3. Chapter Runtime Registry Plan:
   - Scalable approach for adding chapters automatically later

4. Provider selection flow:
   - How default provider resolves from settings/env

5. Unified client approach:
   - How frontend runtime-client.ts interacts with backend

6. Risk analysis:
   - Circular imports
   - Namespace overlaps
   - Incomplete TODO placeholders

Do not write code. Only a deep architectural plan.


/sp.tasks
feature-id: 044-system-integration-phase-1
title: "System Integration Layer Tasks"

Generate full task list in categories:

1. Runtime Router Tasks
2. Registry Tasks
3. Provider Selector Tasks
4. RAG Integration Tasks
5. Metadata Integration Tasks
6. Frontend Runtime Client Tasks
7. Validation Tasks
8. Documentation Tasks

Each task must include:
- [ ] checkbox
- TaskID T001...
- Priority P1/P2
- File path
- Exact placeholder to add

NO real logic. Only scaffolding + TODO comments.


/sp.implement
feature-id: 044-system-integration-phase-1
title: "System Integration Layer Implementation"

Implement scaffolding only:

✔ Create all runtime integration files
✔ Add placeholder switch statements
✔ Add registry dictionaries
✔ Update ai_blocks router to call runtime router
✔ Add empty unified RAG functions
✔ Update provider base to include factory TODO
✔ Create frontend runtime-client.ts with placeholder functions
✔ Create dependency-map.md scaffold

❌ Do NOT:
- Implement LLM logic
- Implement RAG search logic
- Call Qdrant
- Call Gemini/OpenAI
- Add business logic

Only create structure exactly per plan/tasks.



==========================================
45
==========================================
auto-run 4 phases (/sp.specify , /sp.plan, /sp.tasks, /sp.implement)
sab kuch FAST kerna but in small batches not all at once
auto-create contracts

auto-create checklist

auto-create quickstart + research + data-model

auto-validate folder structure

auto-normalize feature IDs

auto-generate PHR

auto-recursively analyze previous features to ensure consistency


/sp.specify
feature-id: 045-system-integration-phase-2
title: "System Integration Layer — Phase 2 (Real AI Logic Activation)"
type: ai-logic-activation

goal:
  Enable the FIRST working version of the full AI runtime:
  - Real LLM calls (OpenAI, Gemini, DeepSeek)
  - Real text-embedding generation
  - Real Qdrant similarity search
  - Real chapter-specific RAG context building
  - Real output generation for AI Blocks
  This is the activation of ACTUAL intelligence across Chapters 1–3.

requirements:

  # 1 — Activate Providers (LLM)
  - Update backend/app/ai/providers/openai_provider.py:
        Implement real call() using OpenAI SDK
  - Update backend/app/ai/providers/gemini_provider.py:
        Implement real call() using Gemini SDK
  - Add minimal error handling + TODO logging

  # 2 — Activate Embeddings
  - Update backend/app/ai/embeddings/embedding_client.py:
        Implement:
          generate_embedding(text)
          batch_embed(list_of_chunks)
        using provider-specific embeddings

  # 3 — Qdrant Real Search Integration
  - Update backend/app/ai/rag/qdrant_store.py:
        Implement:
          create_collection()
          upsert_vectors()
          similarity_search(query_vector, top_k)
        using Qdrant client SDK

  # 4 — Real RAG Pipeline
  - Update backend/app/ai/rag/pipeline.py:
        Steps:
          1. Load chapter metadata + chunks
          2. Embed user query
          3. Perform Qdrant search
          4. Build context window
          5. Prepare final prompt
        Implement minimal, safe logic (no advanced ranking)

  # 5 — AI Block Real Logic Activation
  - Update backend/app/ai/runtime/engine.py:
        Implement real flow for:
          ask-question
          el10 explanation
          quiz
          diagram
        Connect to:
          - RAG pipeline
          - LLM provider call
          - output formatters

  # 6 — Skill-Based Real Implementations
  - Update backend/app/ai/skills/retrieval_skill.py
  - Update backend/app/ai/skills/formatting_skill.py
  - Update backend/app/ai/skills/prompt_builder_skill.py
        Add minimal real logic

  # 7 — Subagent Activation
  - Activate real logic in:
        ask_question_agent.py
        explain_el10_agent.py
        quiz_agent.py
        diagram_agent.py
      using:
        - retrieval_skill
        - prompt_builder_skill
        - formatting_skill

  # 8 — Chapter RAG Indexing Command
  - Create:
        backend/app/cli/index_chapter.py
        Function: index_chapter(chapter_id)
        - reads chapter chunks
        - generates embeddings
        - upserts into Qdrant

acceptance_criteria:
  - Real LLM responses returned through runtime engine
  - Real embeddings and Qdrant search working
  - Real AI Block results produced
  - CLI script indexes all chapters successfully
  - No broken imports, no missing modules

success_message: |
  System Integration Phase 2 successfully activated. AI Blocks now produce real
  intelligent responses using LLM + Embeddings + Qdrant RAG pipelines.


/sp.plan
feature-id: 045-system-integration-phase-2
title: "System Integration Phase 2 — Real AI Logic Plan"

Write a detailed execution plan including:

1. Provider activation architecture
   - How each provider (OpenAI, Gemini, DeepSeek) is selected
   - Input/Output contract formats

2. Embedding Strategy
   - How embedding_client chooses model
   - Batch vs single embedding logic

3. RAG pipeline architecture
   - Query embedding
   - Similarity search
   - Context window building
   - Future improvement hooks

4. Subagents Activation Flow
   - How each subagent calls skills
   - How skills call RAG and providers

5. Error Handling Plan
   - Provider failure fallback
   - Empty context fallback
   - Rate limit behavior

6. CLI Indexer Plan
   - End-to-end embedding + upsert flow
   - Logging & durability

Do NOT write code. Only architecture.


/sp.tasks
feature-id: 045-system-integration-phase-2
title: "System Integration Phase 2 — Implementation Tasks"

Generate tasks in categories:

1. Provider Activation Tasks
2. Embedding Tasks
3. Qdrant Integration Tasks
4. RAG Pipeline Tasks
5. Subagent Logic Tasks
6. Skills Real Logic Tasks
7. Runtime Engine Logic Tasks
8. CLI Indexer Tasks
9. Testing + Validation Tasks

Each task must include:
- [ ] checkbox
- Txxx ID
- Priority P1/P2
- File path
- Exact TODO logic required


/sp.implement
feature-id: 045-system-integration-phase-2
title: "System Integration Phase 2 — Implementation"

Implement ONLY:

✔ Real provider call() logic
✔ Real embedding logic
✔ Real Qdrant connection + search
✔ Real RAG pipeline steps
✔ Real skill logic
✔ Real subagent logic
✔ Real runtime engine logic
✔ CLI indexer (full working)

❌ Do NOT:
- Implement complex ranking
- Implement caching
- Implement parallelization
- Implement diagram generation logic
- Implement advanced quiz logic
- Add any business-critical optimization

The goal is a **minimal but fully functional AI runtime**.

