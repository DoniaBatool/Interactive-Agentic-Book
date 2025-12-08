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



==========================================
51
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
feature-id: 051-selection-rag
title: "Selection-Based RAG Engine — Highlight → Context → Answer"
type: backend-rag-runtime

goal:
  Implement the complete scaffolding for selection-based RAG used by the textbook UI.
  When a learner highlights text inside any chapter (MDX), the system extracts that
  text, sends it to the backend, and answers ONLY from that selected content.

requirements:

  # 1 — Frontend Selection Extraction
  - Update frontend/docs/chapters/* MDX layout so text selection is captured.
  - Add a SelectionRAGBar component that appears when user highlights text.
  - Component contains:
      - Selected text preview
      - Textarea for question
      - "Ask" button
  - No AI logic — only UI + event capture.

  # 2 — Frontend → Backend API Contract
  - Create POST /api/rag/selection endpoint.
  - Request model:
        { selected_text: str, question: str, chapter_id: int }
  - Response model:
        { answer: str, context_used: str }
  - No AI logic; return placeholders.

  # 3 — Backend Selection RAG Pipeline (Scaffold Only)
  - Create backend/app/ai/rag/selection_pipeline.py
        - TODO: clean_selected_text()
        - TODO: embed_selected_text()
        - TODO: run_similarity_search_over_selected()
        - TODO: pass_context_to_llm()
        - All placeholders.

  # 4 — Runtime Integration Layer
  - Create backend/app/ai/runtime/selection_engine.py
        - accepts selected_text + question
        - builds prompt template (placeholder)
        - calls placeholder LLM provider
        - returns scaffold response

  # 5 — Subagent for Selection Queries
  - Create backend/app/ai/subagents/selection_agent.py
        - Input schema
        - Output schema
        - TODO: core selection-based reasoning
        - No logic.

  # 6 — Skills Layer
  - Create backend/app/ai/skills/selection_cleaning_skill.py
  - Create backend/app/ai/skills/selection_context_skill.py
  - Both with TODOs only.

  # 7 — Update Chapter Viewer UI
  - Add invisible selection listener to MDX wrapper
  - Trigger SelectionRAGBar when selection.length > N chars
  - No styling complexity — minimal UI

acceptance_criteria:
  - Full pipeline exists: Frontend selection → API endpoint → selection pipeline → runtime engine → subagent
  - No real AI or embedding logic is implemented
  - Backend compiles with no errors
  - Frontend selection bar appears (placeholder)
  - spec.md, plan.md, tasks.md created correctly
success_message: |
  Selection-Based RAG scaffolding created successfully.


/sp.plan
feature-id: 051-selection-rag
title: "Selection-Based RAG Engine — Architecture Plan"

Generate a detailed architecture plan including:

1. Frontend Architecture
   - MDX wrapper selection detection
   - SelectionRAGBar component location
   - Props, events, UI structure
   - Data flow: selection → component → API

2. Backend API Architecture
   - /api/rag/selection endpoint directory + file structure
   - Pydantic request/response models
   - Router integration in main.py

3. RAG Pipeline (Selection Mode)
   - Pipeline responsibilities
   - Placeholder functions
   - Flow diagram: selected_text → embed → retrieval → LLM → answer

4. Subagent Architecture
   - selection_agent input/output schema
   - Responsibility boundary
   - How skills integrate (cleaning skill, context skill)

5. Skills Architecture
   - selection_cleaning_skill
   - selection_context_skill
   - Placeholder methods and expected signatures

6. Filepaths
   - Every file to be created or updated

7. Constraints
   - No real LLM logic
   - No embeddings logic
   - Only scaffolding

8. Acceptance criteria mapping
   - Show which part of the plan fulfills each requirement


/sp.tasks
feature-id: 051-selection-rag
title: "Selection-Based RAG Engine — Tasks List"

Generate the full atomic task list grouped into:

## A. Frontend Tasks
- Create SelectionRAGBar.tsx with UI placeholders
- Add MDX wrapper selection listener
- Wire selection → state → component
- POST request to backend using fetch()

## B. Backend API Tasks
- Create /api/rag/selection router file
- Add POST endpoint with request/response models
- Return placeholder response
- Register router in main.py

## C. RAG Pipeline Tasks
- Create selection_pipeline.py
- Add placeholder functions:
    clean_selected_text
    embed_selected_text
    perform_local_retrieval
    build_context
    call_llm_provider
- Add TODO comments

## D. Runtime Engine Tasks
- Create selection_engine.py
- Accept selected_text + question
- Build prompt template (placeholder)
- Return dummy response

## E. Subagent Tasks
- Create selection_agent.py
- Add input/output schemas
- Add TODO behaviors

## F. Skills Tasks
- Create two skill files with placeholder methods

## G. Validation Tasks
- Backend should start with uvicorn
- Frontend build must pass
- SelectionRAGBar should appear when text is selected

Output strict checklist-style tasks with TaskIDs.


/sp.implement
feature-id: 051-selection-rag
title: "Selection-Based RAG Engine — Scaffolding Implementation"

Implement tasks EXACTLY as defined in tasks.md:

- Create all frontend components with placeholder UI
- Add MDX selection listener
- Create backend endpoint /api/rag/selection
- Create RAG pipeline placeholder modules
- Create runtime engine file
- Create subagent + skills scaffolding
- Insert TODO comments in all non-implemented logic areas

Rules:
- Do NOT add real LLM logic
- Do NOT add real embedding logic
- Only scaffolding + comments
- Modify only allowed files
- Ensure backend imports work

After generating code:
- Output only file diffs + newly created files
- No explanations



==========================================
52
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
feature-id: 052-betterauth
title: "BetterAuth Authentication Layer — Scaffolding & Integration"
type: auth-architecture

goal:
  Add complete scaffolding for BetterAuth-based authentication across the platform.
  This feature introduces:
    - Auth client + server scaffolding
    - Login, signup, logout endpoints (placeholder logic)
    - Session validation middleware
    - Frontend auth UI placeholders
    - Config wiring and env vars
  No real authentication or crypto logic is implemented.

requirements:

  # 1 — Backend Setup (Scaffold Only)
  - Create backend/app/auth/betterauth_client.py
      - TODO: init_client()
      - TODO: get_user()
      - TODO: validate_session()
  - Create backend/app/auth/routes.py
      - POST /auth/signup — placeholder response
      - POST /auth/login — placeholder response
      - POST /auth/logout — placeholder response
      - GET /auth/me — return placeholder user profile
  - Add backend/app/auth/session_middleware.py
      - TODO: extract session cookie
      - TODO: validate via betterauth_client
      - No real logic.

  # 2 — Frontend Integration (Scaffold)
  - Create frontend/src/auth/useAuth.ts
      - login(), signup(), logout(), getSession()
      - All placeholder implementations
  - Create frontend/src/components/auth/LoginForm.tsx
  - Create frontend/src/components/auth/SignupForm.tsx
  - Create frontend/src/components/auth/ProfileBox.tsx
      - Display placeholder user

  # 3 — Shared API Contract
  - Create specs/052-betterauth/contracts/auth-api.yaml
      - Define request/response for signup/login/logout/me
      - Placeholder schemas, no real authentication rules.

  # 4 — .env + Settings Update
  - Modify backend/app/config/settings.py:
      - BETTERAUTH_PUBLIC_KEY
      - BETTERAUTH_SECRET_KEY
      - BETTERAUTH_ISSUER
  - Update .env.example accordingly

  # 5 — Protect API Routes (Scaffold)
  - Add require_auth decorator in backend/app/auth/decorators.py
      - Only logs messages (TODO)
      - No real permission logic

out_of_scope:
  - Real password hashing
  - Session cookies
  - OAuth / SSO
  - Multi-factor authentication
  - JWT signing or verification

acceptance_criteria:
  - All file paths exist
  - Backend starts without errors
  - Frontend builds without errors
  - Auth endpoints return placeholder static responses
  - Middleware + decorators exist with TODOs
  - Env vars present in .env.example

success_message: |
  BetterAuth scaffolding successfully created.

/sp.plan
feature-id: 052-betterauth
title: "BetterAuth Integration — Architecture Plan"

Generate a detailed architecture plan including:

1. Backend Architecture
   - betterauth_client.py → client wrapper (init + validate + get_user)
   - routes.py → /auth/* endpoints
   - session_middleware.py → add scaffold middleware flow
   - decorators.py → require_auth decorator
   - how these integrate with FastAPI app

2. Frontend Architecture
   - useAuth.ts state flow
   - LoginForm.tsx + SignupForm.tsx + ProfileBox.tsx structure
   - How API requests will be sent

3. Directory Structure
   Show exact tree:
      backend/app/auth/
      frontend/src/auth/
      frontend/src/components/auth/

4. API Contract Design
   - signup, login, logout, me endpoints
   - placeholder return examples

5. Configuration Layer
   - settings.py additions
   - required env vars

6. Constraints
   - NO real auth logic
   - TODOs only

7. Acceptance Criteria Mapping


/sp.tasks
feature-id: 052-betterauth
title: "BetterAuth Integration — Tasks List"

Generate atomic implementation tasks grouped into:

## A. Backend Tasks
- Create betterauth_client.py with placeholder class + TODO functions
- Create routes.py with /auth/signup, login, logout, me endpoints
- Add router to main FastAPI app
- Create session_middleware.py with placeholder logic
- Create decorators.py with require_auth (placeholder)
- Update settings.py for new env vars
- Update .env.example

## B. Frontend Tasks
- Create useAuth.ts with placeholder methods
- Create LoginForm.tsx, SignupForm.tsx, ProfileBox.tsx
- Add minimal UI
- Add API request helpers

## C. Contract Tasks
- Create contracts/auth-api.yaml with endpoint schemas

## D. Validation Tasks
- Backend must start with uvicorn
- Frontend must build without errors
- Auth endpoints must return placeholder responses

Format:
- Checkbox style
- TaskIDs (T001, T002…)
- Clear filepath for each task


/sp.implement
feature-id: 052-betterauth
title: "BetterAuth Integration — Implementation"

Implement tasks EXACTLY as defined in tasks.md:

- Create all backend files under backend/app/auth/*
- Add routers, middleware, decorators with placeholder logic + TODOs
- Add frontend auth hook + components
- Update settings.py and .env.example
- Add contracts/auth-api.yaml
- DO NOT implement real authentication
- DO NOT add hashing, cookies, or crypto
- Only scaffolding + placeholders

Output only:
- New files
- Modified files
- File diffs

No explanations.




==========================================
53
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
feature-id: 053-roles-permissions
title: "User Roles & Permission Scaffolding (RBAC v0)"
type: auth-architecture

goal:
  Add a placeholder RBAC (role-based access control) framework to the backend.
  This feature introduces:
    - Static role definitions (admin, educator, student)
    - Permission map structure
    - Decorator-based permission checks (scaffold only)
    - Middleware placeholder for role injection
    - Frontend helper for role-awareness
  No real validation, no secure RBAC logic, only scaffolding.

requirements:

  # 1 — Backend Role Definitions
  - Create backend/app/auth/roles.py
      - ROLE_ADMIN, ROLE_EDUCATOR, ROLE_STUDENT
      - permissions = { ... } mapping (placeholder)
      - TODO markers for real logic

  # 2 — Permission Checking System (Scaffold)
  - backend/app/auth/permissions.py
      - function: has_permission(user_role, action)
      - return placeholder True/False
      - TODO comments explaining expected logic

  - backend/app/auth/decorators.py
      - require_role(role)
      - require_permission(action)
      - Both must do placeholder checks only

  # 3 — Middleware to Attach Role to Request
  - backend/app/auth/role_middleware.py
      - Extract role from placeholder source
      - Inject into request.state.user_role

  # 4 — Update Auth Routes to Demonstrate Role Use
  - Modify backend/app/auth/routes.py
      - /auth/me returns { user: { role: "<placeholder>" } }

  # 5 — API Contract
  - Create specs/053-roles-permissions/contracts/rbac.yaml
      - Document the role model
      - Document how permissions are structured
      - No real enforcement logic

  # 6 — Frontend Role Awareness
  - Create frontend/src/auth/useRole.ts
      - getRole() — placeholder
      - isAdmin(), isEducator(), isStudent()

  # 7 — .env + config
  - No new env vars required
  - Update settings.py to include DEFAULT_USER_ROLE placeholder

out_of_scope:
  - Real RBAC enforcement
  - Database-backed permission storage
  - OAuth scopes
  - User-specific overrides

acceptance_criteria:
  - All RBAC modules exist exactly as described.
  - No endpoint breaks due to missing imports.
  - role_middleware runs but contains only placeholder logic.
  - Frontend compiles successfully.
  - specs/rbac.yaml exists.

success_message: |
  Roles + Permission scaffolding created successfully.
  Placeholder RBAC layer is now ready for future extension.



/sp.plan
feature-id: 053-roles-permissions
title: "Roles & Permission Scaffolding — Architecture Plan"

Generate a detailed architecture plan covering:

1. Backend Architecture
   - roles.py → define roles and placeholder permission maps
   - permissions.py → has_permission logic scaffold
   - decorators.py → require_role + require_permission
   - role_middleware.py → attach user_role to request.state

2. Interaction Flow
   - How middleware attaches role
   - How decorators read request.state.user_role
   - How routes use these decorators

3. Frontend Integration
   - useRole.ts design
   - Role helper functions (isAdmin, etc.)

4. File Tree Structure
   - backend/app/auth/*
   - specs/053-roles-permissions/contracts/*
   - frontend/src/auth/*

5. API Contract
   - Structure of rbac.yaml

6. Constraints
   - Absolutely NO real permission logic
   - Placeholder returns only
   - No database integration

7. Acceptance Criteria Mapping


/sp.tasks
feature-id: 053-roles-permissions
title: "Tasks — Roles & Permission Scaffolding"

Generate atomic tasks grouped as:

## A. Backend Tasks
- T001: Create backend/app/auth/roles.py with role constants + placeholder permissions
- T002: Create backend/app/auth/permissions.py with has_permission() placeholder
- T003: Create backend/app/auth/decorators.py with require_role + require_permission decorators
- T004: Create backend/app/auth/role_middleware.py to attach placeholder role to request.state
- T005: Modify backend/app/auth/routes.py to return role in /auth/me
- T006: Update backend/app/config/settings.py with DEFAULT_USER_ROLE

## B. Frontend Tasks
- T007: Create frontend/src/auth/useRole.ts
- T008: Implement placeholder functions: getRole(), isAdmin(), isEducator(), isStudent()

## C. Contract Tasks
- T009: Create specs/053-roles-permissions/contracts/rbac.yaml

## D. Validation Tasks
- T010: Ensure backend runs without errors
- T011: Ensure frontend builds without errors

Format: checkboxes + Task IDs.


/sp.implement
feature-id: 053-roles-permissions
title: "Implement Roles & Permission Scaffolding"

Implement EXACTLY the tasks defined in tasks.md:

- Create all backend RBAC scaffold files
- Add placeholder permission system
- Add decorators with TODO logic
- Add middleware attaching static role
- Modify /auth/me to include role
- Create frontend role helper
- Add rbac.yaml contract
- Update settings.py
- No real RBAC logic, only placeholders

Output ONLY file diffs and created files.
No explanations.


==========================================
54
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
feature-id: 054-chapter-access-control
title: "Chapter Access Control Scaffolding (RBAC-based Chapter Permissions)"
type: backend-authorization-architecture

goal:
  Add a scaffolding layer that controls which user roles can access specific chapters.
  This feature introduces:
    - Chapter → Role access map
    - Permission check placeholder for chapter access
    - Backend API wrapper enforcing placeholder access
    - Frontend helpers for showing/hiding chapters
  No real RBAC validation. No real auth. Only placeholder structure.

requirements:

  # 1 — Backend Chapter Access Map
  - Create backend/app/auth/chapter_access.py
      - CHAPTER_ACCESS_MAP = { 1: [...roles], 2: [...roles], 3: [...roles] }
      - Default: all roles allowed
      - TODO markers for real policy logic

  # 2 — Access Checking Function
  - Add function to backend/app/auth/permissions.py:
        can_access_chapter(user_role, chapter_number)
      - Placeholder True/False only
      - No real enforcement logic

  # 3 — Decorator for Chapter Protection
  - Update backend/app/auth/decorators.py
      - Add decorator: require_chapter_access(chapter_number)
      - Reads request.state.user_role
      - Placeholder enforcement: pass-through with TODO

  # 4 — API Integration (Scaffold Only)
  - Modify backend/app/api/chapters.py
      - Wrap GET /chapter/{id} with require_chapter_access(id)
      - Placeholder behavior only

  # 5 — Frontend Awareness Layer
  - Create frontend/src/auth/chapterAccess.ts
      - canViewChapter(role, chapterNumber)
      - chaptersAllowed(role)

  # 6 — Contract File
  - Create specs/054-chapter-access-control/contracts/chapter-access.yaml
      - High-level description of access rules
      - No actual enforcement schema

  # 7 — Tests Placeholder
  - Create tests/auth/test_chapter_access.py with placeholder tests:
      - test_student_access_placeholder()
      - test_educator_access_placeholder()

out_of_scope:
  - Real RBAC enforcement
  - Real authorization middleware
  - Database-driven permissions
  - SSO, OAuth, JWT permission tokens

acceptance_criteria:
  - Chapter access map exists.
  - Decorators exist and import correctly.
  - Chapters API is wrapped with placeholder logic.
  - Frontend helpers compile.
  - Contract YAML created.
  - Backend starts without errors.

success_message: |
  Chapter Access Control scaffolding created successfully.
  Placeholder RBAC enforcement for chapter-level access is now structured and ready for real logic later.


/sp.plan
feature-id: 054-chapter-access-control
title: "Chapter Access Control Scaffolding — Architecture Plan"

Generate a detailed technical plan including:

1. Chapter Access Architecture
   - CHAPTER_ACCESS_MAP design
   - How roles connect to permission map
   - What the placeholder access rules look like

2. Permission Flow
   - how can_access_chapter() is called
   - how decorators enforce placeholder logic
   - how API routes attach decorators

3. Data Flow Diagram (text-only)
   request → middleware.role → decorator → chapter_access_map → placeholder result → route

4. Frontend Plan
   - chapterAccess.ts design
   - UI behavior examples

5. File Structure Plan
   backend/app/auth/
   backend/app/api/chapters.py
   frontend/src/auth/
   specs/054-chapter-access-control/contracts/

6. Constraints
   - No real RBAC
   - Only scaffolding

7. Acceptance Criteria Mapping


/sp.tasks
feature-id: 054-chapter-access-control
title: "Tasks — Chapter Access Control Scaffolding"

Generate tasks in checkbox format grouped as:

## A. Backend Tasks
- T001: Create backend/app/auth/chapter_access.py with CHAPTER_ACCESS_MAP
- T002: Add can_access_chapter() to permissions.py
- T003: Add require_chapter_access() decorator
- T004: Modify backend/app/api/chapters.py to use decorator
- T005: Ensure imports resolve

## B. Frontend Tasks
- T006: Create frontend/src/auth/chapterAccess.ts
- T007: Implement canViewChapter() placeholder
- T008: Implement chaptersAllowed() placeholder

## C. Contract Tasks
- T009: Create specs/054-chapter-access-control/contracts/chapter-access.yaml

## D. Testing Scaffold
- T010: Create tests/auth/test_chapter_access.py with placeholder tests

## E. Validation Tasks
- T011: Backend compiles with no runtime errors
- T012: Frontend builds without errors

/sp.implement
feature-id: 054-chapter-access-control
title: "Implement Chapter Access Control Scaffolding"

Implement exactly the tasks from tasks.md:

- Add chapter access map
- Add placeholder access function
- Add decorators
- Wrap chapter route
- Add frontend access helpers
- Add contract YAML
- Add placeholder tests

NO real permission logic.
NO real chapter restriction.
Only scaffolding and TODO comments.

Output only diffs + created files.




==========================================
55
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
feature-id: 055-progress-tracking
title: "Chapter Progress Tracking Layer (Scaffold Only)"
type: backend-progress-architecture

goal:
  Introduce a progress-tracking framework enabling the system to:
    - Mark chapter started
    - Mark chapter completed
    - Retrieve progress state for a user
  NO real database logic, NO real auth integration. Only scaffolding + TODO markers.

requirements:

  # 1 — Progress State Model (Placeholder)
  - Create backend/app/progress/models.py
      - ProgressState enum: NOT_STARTED, IN_PROGRESS, COMPLETED
      - ProgressRecord dataclass with:
          user_id, chapter_id, state, updated_at
      - TODO: persistence layer integration

  # 2 — Progress Service Scaffolding
  - Create backend/app/progress/service.py
      - mark_started(user_id, chapter_id)
      - mark_completed(user_id, chapter_id)
      - get_progress(user_id)
      - All functions contain placeholder logic + TODO

  # 3 — API Endpoints Scaffold
  - Create backend/app/api/progress.py
      - POST /progress/{chapter_id}/start
      - POST /progress/{chapter_id}/complete
      - GET  /progress/
      - All endpoints:
          - Read user from request.state.user_id
          - Call service functions (placeholder only)

  # 4 — Router Registration
  - Update backend/app/main.py:
      - include_router(progress_router)

  # 5 — Frontend Tracking Helper
  - Create frontend/src/progress/progressClient.ts
      - updateProgress(chapterId, state)
      - getProgress()

  # 6 — Contract File
  - Create specs/055-progress-tracking/contracts/progress-api.yaml
      - Document the three endpoints and placeholder responses

  # 7 — Testing Scaffold
  - tests/progress/test_progress.py
      - Placeholder tests with TODOs

constraints:
  - No real DB write/read.
  - No real authentication.
  - No real user session.
  - No analytics, no dashboard yet.

acceptance_criteria:
  - All files exist.
  - Backend starts without errors.
  - API routes compile.
  - Frontend builds.
  - Contract YAML created.

success_message: |
  Progress Tracking Layer scaffolding is ready. Real logic will be added once authentication and persistence features are implemented.


/sp.plan
feature-id: 055-progress-tracking
title: "Architecture Plan — Progress Tracking Layer (Scaffold Only)"

Generate a detailed plan including:

1. Data Flow
   - user_id → API endpoint → service → progress record (placeholder)

2. Model Design
   - ProgressState enum structure
   - ProgressRecord dataclass fields and purpose
   - Notes on future DB integration

3. Service Layer Design
   - How mark_started(), mark_completed(), get_progress() will be structured
   - TODOs for database logic and validation

4. API Design
   - describe each endpoint and request structure
   - placeholder JSON responses

5. Frontend Integration Plan
   - progressClient.ts usage patterns
   - how UI will eventually consume progress states

6. File Structure Plan
   backend/app/progress/
   backend/app/api/progress.py
   frontend/src/progress/
   specs/055-progress-tracking/contracts/

7. Constraints & Future Work
   - real DB logic postponed
   - auth integration postponed

8. Acceptance Criteria Mapping


/sp.tasks
feature-id: 055-progress-tracking
title: "Tasks — Chapter Progress Tracking Layer (Scaffold Only)"

Generate tasks in checkbox format grouped as:

## A. Backend Model Tasks
- T001: Create backend/app/progress/models.py
- T002: Add ProgressState enum
- T003: Add ProgressRecord dataclass
- T004: Add TODO for persistence layer

## B. Progress Service Tasks
- T005: Create backend/app/progress/service.py
- T006: Add mark_started() placeholder
- T007: Add mark_completed() placeholder
- T008: Add get_progress() placeholder

## C. API Tasks
- T009: Create backend/app/api/progress.py
- T010: Add POST /start
- T011: Add POST /complete
- T012: Add GET /progress
- T013: Register router in main.py

## D. Frontend Tasks
- T014: Create frontend/src/progress/progressClient.ts
- T015: Implement updateProgress()
- T016: Implement getProgress()

## E. Contract Tasks
- T017: Create specs/055-progress-tracking/contracts/progress-api.yaml

## F. Testing Tasks
- T018: Create tests/progress/test_progress.py with placeholders

## G. Validation Tasks
- T019: Backend starts without errors
- T020: Frontend compiles successfully


/sp.implement
feature-id: 055-progress-tracking
title: "Implement Chapter Progress Tracking Layer (Scaffold Only)"

Implement exactly the tasks from tasks.md:

- Create models, service, API, router registration
- Create frontend progressClient.ts
- Add placeholder tests
- Add contract file

STRICT RULES:
- NO real persistence logic
- NO authentication logic
- NO business logic
- Only scaffolding + TODO comments

Output only the diffs + newly created files.


==========================================
56
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

/sp.implement
feature-id: 056-global-stabilization
title: "Global Platform Stabilization & Cross-Chapter Consistency Layer"
type: system-infrastructure

goal:
  Ensure the entire AI Textbook Platform functions consistently across all three chapters.
  This includes stabilizing the AI blocks, RAG routing, multi-chapter embeddings,
  LLM runtime formatting, and cross-chapter content rules.

requirements:
  # 1 — Unified AI Block Runtime Rules
  - Create backend/app/ai/runtime/ai_block_rules.py
  - Define placeholder rules for:
      - consistent formatting
      - token usage normalization
      - uniform retry/backoff strategies
      - cross-chapter context limits

  # 2 — Multi-Chapter Semantic Router
  - Update backend/app/ai/rag/pipeline.py with placeholder logic:
      - chapter scoring switch
      - chapter affinity routing
      - fallback retrieval
  - No real logic; only structure + TODOs.

  # 3 — Combined Chapter Embedding Collections
  - Create backend/app/ai/rag/collections.py with:
        - CH1_COLLECTION_NAME
        - CH2_COLLECTION_NAME
        - CH3_COLLECTION_NAME
        - TODO: auto-select collection from query

  # 4 — Global Formatting Layer
  - Create backend/app/ai/formatters/response_formatter.py with:
        - consistent markdown rules
        - diagram formatting placeholders
        - quiz formatting placeholders

  # 5 — Cross-Chapter Content Validation
  - Create backend/app/content/validation/chapter_consistency.py
      - TODO rules for:
          - consistent number of AI blocks
          - consistent section ordering
          - consistent glossary structure

  # 6 — Build Stability Layer
  - Add build pre-check script:
        scripts/pre_build_check.py
      - verify:
          - MDX presence for all chapters
          - metadata presence
          - AI-block placeholder presence
        (Placeholders only, no real logic)

  # 7 — Documentation
  - Add docs/global/stabilization.md
  - Describe:
      - stabilization goals
      - multi-chapter routing rules
      - formatting unification

acceptance_criteria:
  - All scaffolding files created
  - No logic implemented
  - Backend starts successfully
  - MDX validation script exists
  - Documentation added

success_message: |
  Global Stabilization Layer created. All cross-chapter consistency modules and
  formatting pipelines scaffolded successfully.


/sp.plan
feature-id: 056-global-stabilization
title: "Global Platform Stabilization & Cross-Chapter Consistency Layer"

Generate a full engineering plan that covers:

- Multi-chapter RAG routing design
- Formatting pipeline architecture
- AI Block consistency rules
- Cross-chapter content validation strategy
- Build stability sequence
- File-by-file implementation order

Plan MUST match spec.md and MUST remain scaffold-only.


/sp.tasks
feature-id: 056-global-stabilization
title: "Global Platform Stabilization Tasks"

Generate FULL task list grouped into:

- RAG Routing
- Formatting Layer
- AI Block Rules
- Cross-Chapter Validation
- Build Stabilization
- Documentation

Only scaffolding tasks allowed. No logic.

/sp.implement
feature-id: 056-global-stabilization
Implement all tasks from tasks.md.

Rules:
- Only scaffolding
- Add TODOs
- Do not implement business logic
- Create all stabilization and validation modules
- Update imports carefully
- Ensure backend builds with no runtime errors


==========================================
57
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
feature-id: 057-global-search-engine
title: "Global Search + Multi-Chapter Query Engine"
type: ai-infrastructure

goal:
  Build a unified search system that allows users to search across all
  three chapters using embeddings + RAG + ranking score. This feature
  introduces cross-chapter retrieval, relevance scoring, and a single
  query endpoint.

requirements:
  # 1 — Multi-Chapter Retrieval Pipeline
  - Create backend/app/ai/search/router.py
      - placeholder scoring rules
      - chapter ranking logic (TODO)
      - fallback search logic

  # 2 — Search API Endpoint
  - Create backend/app/api/search.py
      - GET /api/search?q=...
      - routes to search router
      - returns placeholder structure

  # 3 — Search Result Formatter
  - Create backend/app/ai/formatters/search_formatter.py
      - TODO: normalize score
      - TODO: return chapter title + snippet + score

  # 4 — Search Ranking Model (stub)
  - Create backend/app/ai/search/ranking.py
      - TODO: BM25-style scoring skeleton
      - TODO: embedding similarity score placeholder

  # 5 — Embedding Fetcher Wrapper
  - Update backend/app/ai/embeddings/embedding_client.py
      - add TODO: fetch embedding for search query

  # 6 — Qdrant Multi-Collection Access
  - Update backend/app/ai/rag/collections.py
      - add list of chapter collections
      - add TODO: iterate over all collections

  # 7 — Frontend Search Box Scaffold
  - Update frontend/src/components/SearchBar/index.tsx
      - add input + submit handler
      - no styling
      - no real logic

acceptance_criteria:
  - Single endpoint: /api/search working with placeholders
  - All files created
  - No real search logic implemented
  - Backend builds without error
  - Frontend search bar renders (non-functional)

success_message: |
  Global Search Engine scaffolding completed. Multi-chapter retrieval,
  ranking stubs, formatter, and API routing successfully created.

/sp.plan
feature-id: 057-global-search-engine
Generate a detailed engineering plan covering:

- Multi-chapter retrieval architecture
- Ranking flow
- Search API routing
- Formatter design
- File-by-file implementation sequence
- Integration points with RAG pipeline

/sp.tasks
feature-id: 057-global-search-engine
Generate FULL scaffold-only task list grouped into:

- Retrieval router
- Ranking model
- API service
- Search formatter
- Collection iterator
- Frontend search bar

/sp.implement
feature-id: 057-global-search-engine
Implement all tasks from tasks.md:

- Create all files
- Add TODO logic only
- Do not implement real search
- Ensure all imports resolve



==========================================
58
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
feature-id: 058-learner-support-system
title: "Learner Support System (LSS) — Hints, Summaries & Progress Helper"
type: backend-ai-support-layer

goal:
  Build a backend-only scaffolding system that provides:
    - Context-aware hints
    - Auto-generated summaries for sections
    - Simple progress helper endpoints
  WITHOUT adding real AI logic.
  This feature must integrate with Chapter metadata and the existing
  runtime engine, using only placeholder functions.

requirements:

  # 1 — LSS Module Structure
  - Create folder: backend/app/ai/lss/
  - Create files:
      backend/app/ai/lss/hints.py
      backend/app/ai/lss/summaries.py
      backend/app/ai/lss/progress.py
  - Each file must include:
      - Placeholder classes
      - Method signatures
      - TODO comments (no logic)

  # 2 — Hints System Scaffolding
  - hints.py must define:
      class HintEngine:
          def get_hint(chapter_id: int, section_id: str, user_state: dict) -> str:
              """Return placeholder hint."""
              # TODO: Use context + runtime later
  - Add allowed hint types: "concept", "example", "definition"

  # 3 — Section Summary Engine
  - summaries.py must define:
      class SummaryEngine:
          def summarize_section(chapter_id: int, section_id: str) -> str:
              """Return placeholder summary."""
  - Add contract comments describing:
      - Expected summary length
      - What metadata fields should be used

  # 4 — Progress Helper Scaffolding
  - progress.py must define:
      class ProgressTracker:
          def get_section_status(user_id: str, chapter_id: int) -> dict
          def mark_section_complete(user_id: str, chapter_id: int, section_id: str) -> None
          # TODO: Replace with DB later (stub only)

  # 5 — LSS Router Layer
  - Create backend/app/api/lss.py
      - POST /api/lss/hint
      - POST /api/lss/summary
      - POST /api/lss/progress/update
      - GET  /api/lss/progress/{user_id}/{chapter_id}
  - Each endpoint returns placeholder JSON.

  # 6 — Integrate Router in backend/app/main.py

  # 7 — Contracts
  - Create file: specs/058-learner-support-system/contracts/lss-api.yaml
  - Describe request/response structure for:
      - hints
      - summaries
      - progress
  - No real schemas for AI output.

acceptance_criteria:
  - All scaffolding files created with method signatures + TODO comments.
  - New API endpoints compile and return placeholder JSON.
  - No AI logic implemented.
  - Backend builds without errors.
  - LSS integrates with existing chapter metadata.

success_message: |
  LSS system scaffolding created. Hints, summaries, and progress helper
  modules are now ready for real AI integration.


/sp.plan
feature-id: 058-learner-support-system
title: "Learner Support System — Architecture Plan"

Generate an architecture plan that includes:

1. Module Architecture
   - Folder structure
   - File responsibilities
   - Class diagrams (text-only)
   - Data flow between modules

2. API Layer Design
   - Endpoints
   - Inputs/outputs (placeholder only)
   - How endpoints call LSS engines

3. Runtime Interaction
   - How LSS will later use:
       - Chapter metadata
       - RAG pipeline
       - Provider LLM
   - No real AI logic yet

4. Data Contracts
   - Hint request/response format
   - Summary request/response format
   - Progress tracker request/response format

5. Non-Functional Requirements
   - Must not break existing runtime
   - Must be fully optional if chapter has no LSS

Output in detailed Markdown.


/sp.tasks
feature-id: 058-learner-support-system
title: "Learner Support System — Tasks"

Generate a fully structured task list with:

Groups:
  - LSS Module Creation
  - API Layer
  - Integration
  - Validation
  - Documentation

Task Format:
  - [ ] [TaskID] [Priority] [Story] description with file path

Requirements:
  - Create placeholders only
  - Ensure backend starts
  - Ensure imports resolve
  - Add TODO comments in all modules

Output ready for /sp.implement.


/sp.implement
feature-id: 058-learner-support-system

Follow tasks.md EXACTLY.
Implement ONLY scaffolding:
  - Empty methods
  - Placeholder return values
  - Class definitions
  - API routes with fake data
  - No AI logic
  - No database
  - No RAG integration

Modify ONLY files listed in tasks.

Create a PHR file after implementation.



==========================================
59
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
feature-id: 059-analytics-telemetry
title: "Analytics & Telemetry Scaffolding Layer"
type: backend-architecture

goal:
  Add a global analytics + telemetry scaffolding layer that logs:
    - AI block usage
    - Chapter visit events
    - Errors (placeholder only)
  WITHOUT implementing real tracking, databases, or external providers.

requirements:

  # 1 — Backend Analytics Module
  - Create folder: backend/app/analytics/
  - Create files:
        event_logger.py
        analytics_models.py
        telemetry_router.py

  # 2 — Event Logger Scaffolding
  - event_logger.py defines:
        class EventLogger:
            def log(event_type: str, payload: dict): 
                """Placeholder logger"""
                # TODO: Replace with real tracking later
  - Allowed event types:
        "ai_block_used", "chapter_visit", "error_event"

  # 3 — Analytics Models (Placeholder)
  - analytics_models.py defines:
        class AnalyticsEvent:
            event_type: str
            payload: dict
            timestamp: str
        # No database storage

  # 4 — Telemetry API Router
  - telemetry_router.py defines:
        POST /api/telemetry/log
        GET /api/telemetry/health
  - Both return placeholder JSON.

  # 5 — Integration
  - In backend/app/main.py include the new router.
  - In app/api/ai_blocks.py add:
        EventLogger.log("ai_block_used", {...})
        (placeholder only)

acceptance_criteria:
  - All modules created and backend compiles.
  - API endpoints return placeholder JSON.
  - No actual telemetry storage.
  - No external services integrated.

success_message: |
  Analytics & Telemetry scaffolding layer created successfully.
  All tracking hooks are ready for future activation.


/sp.plan
feature-id: 059-analytics-telemetry
title: "Analytics & Telemetry — Architecture Plan"

Generate a full plan covering:

1. Module breakdown  
2. Analytics event flow  
3. Telemetry API flow  
4. Integration points with runtime + AI blocks  
5. Non-functional constraints:
   - No DB
   - No external APIs
   - Pure scaffolding only

Output detailed Markdown.


/sp.tasks
feature-id: 059-analytics-telemetry
title: "Analytics & Telemetry — Tasks"

Produce structured tasks grouped as:

- Analytics Module Setup
- Event Logger Scaffold
- Telemetry Router
- Integration Tasks
- Validation Tasks

Format:
  - [ ] [Txxx] [Priority] [Story] Description with file path


/sp.implement
feature-id: 059-analytics-telemetry

Implement EXACT scaffolding defined in tasks.
No real logging, no DB, no external services.
Just placeholder event logger + telemetry endpoints.

Generate a PHR file afterward.


==========================================
60
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
feature-id: 060-final-build-qa
title: "Final Build, QA, Packaging & Deployment Checklist"
type: system-integration

goal:
  Create a final QA and build verification layer that ensures:
    - Frontend build stability
    - Backend stability
    - Chapter content validation
    - AI runtime placeholder validation
    - Build packaging manifest for hackathon submission

requirements:

  # 1 — QA Scripts Folder
  - Create folder: tools/qa/
  - Create files:
        validate_frontend_build.md
        validate_backend_api.md
        validate_chapter_content.md
        release_preflight_checklist.md

  # 2 — Frontend Build Validation Script (Markdown)
  - Steps:
        - npm run build
        - Check MDX warnings
        - Check AI block rendering
        - Check sidebar navigation

  # 3 — Backend API Validation Script
  - Steps:
        - Start uvicorn
        - Test all AI block endpoints
        - Test chapter metadata imports
        - Test runtime engine placeholder responses

  # 4 — Chapter Validation Script
  - Steps:
        - Check section count
        - Check placeholders
        - Check metadata sync

  # 5 — Release Packaging Manifest
  - Create file: RELEASE_PACKAGE.md
  - Must include:
        - Project structure overview
        - Features implemented
        - How to run frontend
        - How to run backend
        - How to demo AI blocks
        - Known limitations (no real AI logic)
        - Hackathon submission instructions

acceptance_criteria:
  - All QA documents created
  - Scripts readable & complete
  - RELEASE_PACKAGE.md usable for judges
  - No code modifications required

success_message: |
  Final QA, build stability checks, and submission packaging created.
  Your project is now fully ready for hackathon submission.


/sp.plan
feature-id: 060-final-build-qa
title: "Final Build & QA Plan"

Generate:
  - QA strategy
  - Build verification plan
  - Chapter validation strategy
  - Release packaging workflow
  - Expected outcomes

Output in detailed Markdown.


/sp.tasks
feature-id: 060-final-build-qa
title: "Final Build & QA — Tasks"

Produce grouped tasks:

- QA Folder Setup
- Frontend Build Validation
- Backend API Validation
- Chapter Validation Tasks
- Release Packaging Tasks
- Final Checks

Task format:
  - [ ] [Txxx] [P1/P2/P3] description with file paths


/sp.implement
feature-id: 060-final-build-qa

Implement ONLY Markdown files & folder structure.
No code execution.
No real tests.

Create:
  - tools/qa/*.md
  - RELEASE_PACKAGE.md

After implementation, generate PHR.
 