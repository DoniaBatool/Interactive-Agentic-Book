🧠 OPTIONAL Bonus (Only if time left):

Urdu translation agent

Diagram auto-generator v2

Practice quiz generator

Export to PDF

Interactive glossary agent

Voice AI block
==========================================
46
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
feature-id: 046-ai-block-global-standardization
title: "Global AI Block Standardization Across All Chapters"
type: runtime-consolidation

goal:
  Ensure all Chapters (1, 2, 3) use a single unified AI Block Runtime.
  Standardize AI block inputs, outputs, schemas, subagents, skills, and
  pipeline behavior across the entire project.
  Guarantee identical performance, formatting, and RAG-context delivery.

requirements:

  # 1 — Global AI Block Contract
  - Create specs/046-ai-block-global-standardization/contracts/ai-blocks.yaml
  - Define global contract for:
        ask-question
        explain-like-el10
        interactive-quiz
        diagram-generator
  - Include:
      - required inputs
      - required outputs
      - error format
      - RAG context usage rules

  # 2 — Global Runtime Router
  - Update backend/app/ai/runtime/engine.py:
      - Implement ai_block_router(block_type, chapter_id, user_input)
      - Standardize:
          - RAG invocation order
          - Subagent selection
          - Prompt formatting
          - Provider selection

  # 3 — Global Subagent Registry
  - Create backend/app/ai/subagents/registry.py
      - Map AI block → subagent class
      - Ensure future chapters auto-register

  # 4 — Shared Skills Upgrade
  - Update skills:
        retrieval_skill.py
        formatting_skill.py
        prompt_builder_skill.py
    to support multiple chapters using same logic

  # 5 — Unified Output Formatting
  - Add backend/app/ai/runtime/output_formatter.py
      - Standardize:
          - answer blocks
          - diagrams
          - quizzes (MCQ, open-ended, true/false)
      - Guarantee all chapters look identical

  # 6 — Chapter Overrides (optional)
  - Add optional override path:
        backend/app/content/overrides/chapter_{id}.py
    Each chapter can override:
        - tone
        - difficulty
        - formatting style

  # 7 — API Layer Update
  - Update backend/app/api/ai_blocks.py:
        All endpoints must call the new global router

  # 8 — Documentation
  - Create specs/046-ai-block-global-standardization/README.md
        - Explain architecture
        - Explain override system
        - Explain global contract

acceptance_criteria:
  - All chapters use the SAME AI block interfaces
  - All AI block endpoints produce identical formatting styles
  - Subagents follow a single registry
  - Skills do not need chapter-specific forks
  - No chapter breaks the flow when switching inputs

success_message: |
  AI Block Global Standardization complete. All chapters now share a unified,
  predictable, scalable AI runtime architecture.


/sp.plan
feature-id: 046-ai-block-global-standardization
title: "Global AI Block Standardization — Architecture Plan"

Write a detailed architecture plan covering:

1. Global Contract Design:
   - Inputs/outputs
   - Error handling
   - Shared context window rules

2. Runtime Routing:
   - How ai_block_router routes between agents
   - Cross-chapter RAG selection

3. Subagent Registry:
   - Design pattern for registering and extending subagents

4. Skills Enhancements:
   - How skills adapt to multi-chapter context
   - How formatting becomes universal

5. Override System:
   - Tiered fallback model (chapter override → global default)

6. Migration Strategy:
   - How to refactor Chapter 1/2/3 AI blocks into unified system


/sp.tasks
feature-id: 046-ai-block-global-standardization
title: "Global AI Block Standardization — Tasks"

Organize tasks under:

1. Contract Tasks
2. Runtime Tasks
3. Subagent Tasks
4. Skills Tasks
5. Formatter Tasks
6. API Integration Tasks
7. Documentation Tasks
8. Validation Tasks

Use:
- checkboxes
- Txxx numbering
- P1 / P2 prioritization
- Exact file paths
- Clear scaffolding instructions


/sp.implement
feature-id: 046-ai-block-global-standardization
title: "Global AI Block Standardization — Implementation"

Implement ONLY scaffolding:

✔ ai-blocks.yaml contract  
✔ ai_block_router() skeleton  
✔ Subagent registry file  
✔ Updated skill function placeholders  
✔ output_formatter.py with TODO sections  
✔ Updated API endpoints routing  
✔ Override folder + sample override file  

DO NOT:
- write real AI logic
- change existing runtime logic
- modify RAG logic
- modify diagram or quiz engines

Goal:
Create a unified architecture ready for real logic.



==========================================
47
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
feature-id: 047-global-llm-guardrails
title: "Global LLM Safety, Guardrails & Prompt Governance Layer"
type: ai-governance

goal:
  Introduce a unified, global safety middleware for all LLM calls across
  Chapters 1, 2, and 3. Standardize tone, age-appropriate content,
  hallucination prevention, fact-checking placeholders, and prompt governance.
  Ensure all AI Blocks route through a shared compliance layer before LLM output.

requirements:

  # 1 — Global Guardrail Contract
  - Create specs/047-global-llm-guardrails/contracts/llm-guardrails.yaml
  - Must define:
        allowed_content
        disallowed_content
        age-appropriate rules (12+)
        tone rules (educational, safe, non-political)
        complexity rules
        hallucination rules
        fallback strategies

  # 2 — Guardrail Engine
  - Create backend/app/ai/guardrails/engine.py
      - process_input_safely()
      - enforce_output_rules()
      - strip_disallowed_content()
      - inject_safety_prefix()
      - inject_safety_suffix()

  # 3 — Prompt Governance Layer
  - Add backend/app/ai/prompt/policy.py
      - define_prompt_policy(block_type, chapter_id)
      - include:
          tone rules
          explanation style
          scaffolded learning
          error messages
          safety reminders

  # 4 — Integration with Runtime Engine
  - Update backend/app/ai/runtime/engine.py:
        - run_ai_block() MUST call guardrail engine before LLM provider
        - RAG context must pass through hallucination-check placeholder

  # 5 — Global Hallucination Prevention
  - Create backend/app/ai/guardrails/hallucination_filter.py
      - TODO functions:
          detect_low-confidence()
          require_citation_for_facts()
          fallback_to_neutral_explanation()

  # 6 — Safety Logging
  - Add backend/app/ai/logging/safety_logger.py
      - record_triggered_rules()
      - record_blocking_events()
      - record_override_events()

  # 7 — Provider-Level Safety Hooks
  - Update all providers:
        openai_provider.py
        gemini_provider.py
        deepseek_provider.py (optional)
      - Add placeholder for native safety settings

  # 8 — Documentation
  - Create specs/047-global-llm-guardrails/README.md
        - describe safety architecture
        - diagram of LLM → RAG → Guardrails → Output
        - best practices

acceptance_criteria:
  - Runtime engine passes ALL LLM inputs & outputs through guardrails
  - All AI blocks obey global prompt governance rules
  - Hallucination filter integrated (placeholder logic only)
  - Safety logging works (stub only)
  - Spec + plan + tasks + contracts generated correctly

success_message: |
  Global LLM Guardrails + Prompt Governance Layer successfully scaffolded.
  All chapters and AI blocks now share a unified educational-safe AI model.


/sp.plan
feature-id: 047-global-llm-guardrails
title: "Global LLM Guardrails — Architecture Plan"

Write a full architecture plan covering:

1. Guardrail Engine Architecture
   - flow diagram: input → guardrails → RAG → LLM → guardrails → output
   - rules engine structure

2. Prompt Governance Policy
   - chapter-level overrides
   - block-level rules
   - tone / complexity guidance

3. Hallucination Filter
   - placeholder strategy
   - citation requirement rules
   - fallback behavior

4. Integration with Runtime
   - how engine.py calls guardrails
   - middleware structure

5. Safety Logging
   - what gets logged
   - how logs will be used later

6. Extensibility
   - how future chapters or AI blocks plug into the same guardrail layer


/sp.tasks
feature-id: 047-global-llm-guardrails
title: "Global LLM Safety Layer — Tasks"

GROUPS:
  - Contract Tasks
  - Guardrail Engine Tasks
  - Prompt Governance Tasks
  - Hallucination Filter Tasks
  - Runtime Integration Tasks
  - Provider Update Tasks
  - Safety Logging Tasks
  - Documentation Tasks

Create:
  - checkbox tasks
  - T000 numbering
  - P1/P2 priority markers
  - exact file paths
  - TODO placeholders only


/sp.implement
feature-id: 047-global-llm-guardrails
title: "Implement Global LLM Safety + Prompt Governance"

Implement ONLY scaffolding:

✔ engine.py structure  
✔ hallucination_filter.py  
✔ prompt policy file  
✔ safety logger file  
✔ updated runtime engine imports & calls  
✔ provider files updated with TODO for safety options  
✔ contract + docs folder created  

Do NOT:
- implement real safety logic
- write filtering rules
- write validation logic
- add real guardrail algorithms
- modify model behavior

Goal:
Ship a full skeleton that enforces safety architecture.


==========================================
48
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
feature-id: 048-e2e-system-test-harness
title: "End-to-End System Test Harness for All Chapters"
type: testing-architecture

goal:
  Build a unified automated test harness that validates the entire AI Textbook System
  (Chapters 1, 2, and 3). Tests must cover MDX compilation, AI Blocks routing, RAG
  retrieval pipelines, runtime engine stability, metadata correctness, build integrity,
  and end-to-end flow validation.

requirements:

  # 1 — Test Infrastructure Setup
  - Create backend/tests/e2e/ folder
  - Add conftest.py with shared fixtures (placeholder only)
  - Add TestClient setup for FastAPI (placeholder)

  # 2 — Chapter Content Validation Tests
  - Create tests for:
      backend/tests/e2e/test_chapter_1_content.py
      backend/tests/e2e/test_chapter_2_content.py
      backend/tests/e2e/test_chapter_3_content.py
  - Validate:
      MDX file exists
      Metadata file exists
      Section count correct
      Placeholder count correct (AI-BLOCK, DIAGRAM)
      Metadata field rules (ID, title match, glossary count)

  # 3 — RAG Pipeline E2E Tests
  - Create backend/tests/e2e/test_rag_pipeline.py
  - Validate placeholder flow:
      chunk loader → embed → search → return context
  - Ensure no crash when embeddings provider or Qdrant is mocked

  # 4 — AI Block Runtime Tests
  - Create backend/tests/e2e/test_ai_blocks.py
  - Test 4 block types:
      ask-question
      explain-like-i-am-10
      interactive-quiz
      generate-diagram
  - Validate correct routing to runtime engine (structure only)

  # 5 — Guardrail Layer Tests
  - Add backend/tests/e2e/test_guardrails.py
  - Validate:
      guardrails receive input/output
      prohibited content returns fallback
      hallucination filter invoked (placeholder)

  # 6 — Build Stability Tests
  - Create scripts/build_test.sh (placeholder)
      - run: npm run build
      - run: backend server startup check

  # 7 — Test Reports
  - Create specs/048-e2e-system-test-harness/contracts/test-report-format.md
      - Define report structure for judges
      - No real logic

acceptance_criteria:
  - All required test files created
  - All tests run without logic (placeholders OK)
  - Entire project builds cleanly under test harness
  - No import/runtime error in RAG, runtime engine, metadata modules
  - All chapters validated as per specification

success_message: |
  End-to-End System Test Harness scaffolding completed successfully.
  All chapters, AI blocks, RAG runtime, and guardrail layers now have
  unified system-level validation.


/sp.plan
feature-id: 048-e2e-system-test-harness
title: "System-Level Test Harness Architecture Plan"

Write a complete test architecture plan including:

1. Overview of testing goals  
2. Folder & file structure for test harness  
3. Fixtures needed for backend AI engine, RAG pipeline, and guardrails  
4. Mocking strategy (LLM providers, embeddings client, Qdrant)  
5. Validation rules for all three chapters  
6. E2E flow diagrams:
      request → guardrails → runtime → provider → output
7. Build stability pipeline plan  
8. Test report output plan (for hackathon judges)


/sp.tasks
feature-id: 048-e2e-system-test-harness
title: "End-to-End Test Harness — Task List"

GROUP: TEST INFRASTRUCTURE
  - [ ] T048-001 – Create backend/tests/e2e folder
  - [ ] T048-002 – Add conftest.py with shared fixtures
  - [ ] T048-003 – Add FastAPI TestClient placeholder

GROUP: CHAPTER VALIDATION TESTS
  - [ ] T048-010 – test_chapter_1_content.py
  - [ ] T048-011 – test_chapter_2_content.py
  - [ ] T048-012 – test_chapter_3_content.py

GROUP: RAG PIPELINE TESTS
  - [ ] T048-020 – test_rag_pipeline.py (mocked search + embeddings)

GROUP: AI BLOCK RUNTIME TESTS
  - [ ] T048-030 – test_ai_blocks.py (routing validation)

GROUP: GUARDRAIL TESTS
  - [ ] T048-040 – test_guardrails.py

GROUP: BUILD & STABILITY TESTS
  - [ ] T048-050 – Create scripts/build_test.sh

GROUP: REPORT CONTRACT
  - [ ] T048-060 – Create test-report-format.md in contracts/

All tasks must create scaffolding only — no real logic.


/sp.implement
feature-id: 048-e2e-system-test-harness
title: "Implement End-to-End Test Harness"

Implement the full scaffolding:

✔ Create all test files  
✔ Add placeholder assertions  
✔ Create build_test.sh  
✔ Add imports that match project structure  
✔ Add contracts/test-report-format.md  
✔ Ensure backend launches without test errors  

Do NOT:
- implement real tests
- mock real LLM providers
- generate embeddings or run Qdrant

Goal: full test harness structure only, ready for future test implementation.







==========================================
49
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
feature-id: 049-translation-engine
title: "Multilingual Translation Engine — Urdu, Arabic, English, Roman Urdu"
type: backend-ai-translation-architecture

goal:
  Add a translation engine that enables all chapter content (MDX sections,
  glossary terms, explanations, quizzes, diagrams descriptions) to be translated
  into:
    - English (default)
    - Urdu
    - Roman Urdu
    - Arabic

  Create translation APIs, provider abstraction, translation pipeline,
  translation glossary scaffolding, and runtime integration for future
  frontend UI usage.

requirements:

  # 1 — Provider Architecture
  - Create backend/app/translation/providers/base_translation.py
  - Create backend/app/translation/providers/openai_translation.py (placeholder)
  - Create backend/app/translation/providers/gemini_translation.py (placeholder)
  - Interface must support:
      translate_text(text, target_language)
      translate_batch(list_of_texts, target_language)
      supported_languages()

  # 2 — Translation Pipeline
  - Create backend/app/translation/pipeline.py
      - TODO steps:
          1. Normalize chapter content
          2. Chunk paragraphs for translation
          3. Route to provider
          4. Reconstruct translated chapter
          5. Return structured dict

  # 3 — Translation Contracts
  - Create specs/049-translation-engine/contracts/translation-schema.yaml
      - Define allowed language codes: en, ur, ru, ar
      - Define shape for translation output:
          {
            "source": "...",
            "translated": "...",
            "language": "ur"
          }

  # 4 — Glossary Translation Support
  - Create backend/app/translation/glossary_mapper.py
      - TODO map glossary terms to translated definitions
      - Create placeholder dictionary structure

  # 5 — API Endpoints
  - Create backend/app/api/translation.py
      - POST /api/translate/chapter/{chapter_id}
      - POST /api/translate/snippet
      - GET /api/translation/languages

  # 6 — Environment Variables
  - Update backend/app/config/settings.py:
        TRANSLATION_PROVIDER
        TRANSLATION_MODEL
  - Update .env.example

  # 7 — Runtime Integration Stub
  - Update backend/app/ai/runtime/engine.py:
        - Add TODO: "If translation needed, call translation pipeline before response"

acceptance_criteria:
  - All required modules exist
  - No real translation logic is implemented (placeholders only)
  - All imports resolve
  - API endpoints respond successfully with mocked data
  - Contracts/spec folder includes translation-schema.yaml

success_message: |
  Translation Engine scaffolding completed. Urdu, Arabic, English, and Roman Urdu
  translation pipelines, providers, contracts, glossary scaffolding, and API
  endpoints created successfully.


/sp.plan
feature-id: 049-translation-engine
title: "Translation Engine Architecture Plan"

Write a complete detailed plan including:

1. Multi-provider architecture (OpenAI / Gemini)
2. Language code rules (en, ur, ru, ar)
3. Pipeline flow: MDX → chunker → provider → merge → output
4. Translation storage strategy (none yet — placeholder only)
5. Glossary translation process
6. API architecture design
7. Runtime integration with AI Engine
8. Future UI usage (Language switcher)
9. Error-handling strategies for provider failure
10. Testability plan for Feature 049


/sp.tasks
feature-id: 049-translation-engine
title: "Multilingual Translation Engine – Task List"

GROUP: PROVIDERS
  - [ ] T049-001 – Create base_translation.py
  - [ ] T049-002 – Create openai_translation.py
  - [ ] T049-003 – Create gemini_translation.py

GROUP: PIPELINE
  - [ ] T049-010 – Create translation/pipeline.py

GROUP: GLOSSARY SUPPORT
  - [ ] T049-020 – Create glossary_mapper.py

GROUP: API ENDPOINTS
  - [ ] T049-030 – Create translation.py API file
  - [ ] T049-031 – Add routes to main FastAPI router

GROUP: CONFIG
  - [ ] T049-040 – Add env variables
  - [ ] T049-041 – Update .env.example

GROUP: CONTRACTS
  - [ ] T049-050 – Create translation-schema.yaml

GROUP: RUNTIME INTEGRATION
  - [ ] T049-060 – Add TODO in ai/runtime/engine.py for translation hook


/sp.implement
feature-id: 049-translation-engine
title: "Implement Translation Engine Scaffolding"

Implement all placeholder modules:
  - Providers
  - Pipeline
  - Glossary mapper
  - API endpoints
  - Config updates
  - Contracts folder

Rules:
  - No real translation logic
  - Only scaffolding + TODO comments
  - Ensure backend runs without translation errors
  - Keep structure clean and future-ready



==========================================
50
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
feature-id: 050-live-ai-interaction
title: "Real-Time AI Interaction Layer — Streaming + Live AI Blocks"
type: backend-frontend-ai-interaction

goal:
  Implement a real-time AI interaction framework so that all AI Blocks
  (ask-question, explain-like-I-am-10, diagram generator, quiz engine, etc.)
  respond with STREAMING updates instead of static responses.
  
  Add streaming APIs, frontend event consumers, and runtime hooks.
  No business logic implemented — only scaffolding.

requirements:

  # 1 — Streaming Backend Infrastructure
  - Create backend/app/ai/streaming/stream_manager.py
      - TODO: manage Server-Sent Events (SSE) or WebSockets
      - TODO: attach to runtime engine pipeline
  - Update runtime engine (engine.py):
      - Add TODO: "If streaming mode enabled, yield tokens"

  # 2 — Streaming API Endpoints
  - Create backend/app/api/streaming.py
      - GET /api/stream/ai-block/{block_type}
      - Should return mocked streaming chunks
  - Add router integration in main FastAPI router

  # 3 — Frontend Streaming Client (Docusaurus)
  - Create frontend/src/ai/streamClient.ts
      - TODO: SSE/WebSocket connector
      - TODO: event handlers for chunk, error, complete
  - Create frontend/src/ai/streamHooks.ts
      - React hooks for:
          useAIStreaming()
          useAIBlockStreaming(blockType)

  # 4 — Frontend Component Integration
  - Update AI Block components:
      - AskQuestionBlock.tsx
      - ExplainELI10Block.tsx
      - QuizBlock.tsx
      - DiagramBlock.tsx
    Add:
      - Placeholder streaming UI
      - TODO comments for streaming output

  # 5 — Config
  - Update backend/app/config/settings.py:
        AI_STREAMING_ENABLED=true|false
        STREAMING_BACKEND=sse|websocket
  - Update .env.example

  # 6 — Contracts
  - Create specs/050-live-ai-interaction/contracts/stream-schema.yaml
      - Define streaming chunk schema:
          { "token": "...", "seq": 0 }
      - Define SSE/WebSocket compatibility expectations

  # 7 — Acceptance
  - Project must start without errors
  - Streaming endpoints must return mocked chunked responses
  - Frontend components must compile and contain streaming hooks
  - No actual LLM streaming logic (placeholders only)

success_message: |
  Live AI Interaction Layer scaffolding created. Backend streaming modules,
  streaming API endpoints, frontend streaming hooks, and AI block integrations
  are ready for future real-time AI output.


/sp.plan
feature-id: 050-live-ai-interaction
title: "Streaming Interaction Architecture Plan"

Generate a highly detailed plan explaining:

1. Why streaming mode is essential for responsive AI Blocks
2. Architecture choice: SSE vs WebSockets (placeholder)
3. Streaming manager responsibilities
4. Required FastAPI changes
5. Frontend streaming flow:
     component → hook → streamClient → event listener → UI updates
6. Compatibility with existing AI Runtime Engine
7. Token-by-token output planning
8. How future LLM providers will enable real streaming
9. Testing strategy:
     - Mock streaming provider
     - Frontend fake stream simulator
10. Integration path into final release for bonus marks



/sp.tasks
feature-id: 050-live-ai-interaction
title: "Real-Time Streaming Layer — Task List"

BACKEND — STREAMING CORE
  - [ ] T050-001 Create stream_manager.py
  - [ ] T050-002 Add SSE/WebSocket TODO logic
  - [ ] T050-003 Update runtime engine with streaming hook

BACKEND — API
  - [ ] T050-010 Create streaming.py
  - [ ] T050-011 Add streaming endpoints
  - [ ] T050-012 Integrate into backend router

FRONTEND — STREAM CLIENT
  - [ ] T050-020 Create streamClient.ts
  - [ ] T050-021 Create streamHooks.ts

FRONTEND — COMPONENT UPDATES
  - [ ] T050-030 Update all AI Block components to support streaming
  - [ ] T050-031 Add placeholder loaders + token UI

CONFIG + ENV
  - [ ] T050-040 Add streaming config vars
  - [ ] T050-041 Update .env.example

CONTRACTS
  - [ ] T050-050 Create stream-schema.yaml


/sp.implement
feature-id: 050-live-ai-interaction
title: "Implement Streaming Interaction Scaffolding"

Implement:

- stream_manager.py (placeholder)
- streaming.py API with mocked chunk output
- runtime engine streaming TODO hook
- frontend streamClient + streamHooks
- updates to AI Block components
- environment variable updates
- streaming schema in contracts folder

NO business logic.
Only scaffolding, placeholders, and mocked streaming.

Ensure the whole project still compiles.
