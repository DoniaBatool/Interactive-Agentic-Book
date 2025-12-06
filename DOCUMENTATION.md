sab kuch FAST kerna but in small batches not all at once

===========
22
==========

/sp.specify
feature-id: 022-ch2-runtime-wiring
title: "Chapter 2 — RAG Pipeline Wiring, Runtime Routing & AI Block Integration"
type: backend-ai-architecture
sab kuch FAST kerna but in small batches not all at once

goal:
  Connect Chapter 2 into the AI Runtime Engine.
  This includes RAG pipeline registration, chapter selection logic,
  context assembly, runtime routing for AI blocks, and placeholder logic hooks.
  NO real AI implementation; only scaffolding.

requirements:

  # 1 — RAG Pipeline Wiring
  - Update backend/app/ai/rag/pipeline.py
      - Add CHAPTER_2_COLLECTION_NAME constant
      - Add TODO: embed_chapter_2()
      - Add TODO: retrieve_chapter_2_relevant_chunks()
      - Add TODO: build_context_for_ch2(query)

  # 2 — Runtime Engine Routing
  - Update backend/app/ai/runtime/engine.py
      - Register chapter_id=2 handling path
      - Route to RAG pipeline functions (placeholders only)
      - Add TODO: context merging for CH2
      - Add TODO: provider selection for chapter 2

  # 3 — AI Block Runtime Hooks
  - Update backend/app/api/ai_blocks.py
      - Ensure each AI block type can target chapter 2
      - Add TODO: load chapter 2 context
      - Connect to runtime engine

  # 4 — Subagent Connectors for CH2
  - Update backend/app/ai/subagents/
        ask_question_agent.py
        explain_el10_agent.py
        quiz_agent.py
        diagram_agent.py
      - Add TODO: chapter 2 handling path comments

  # 5 — Chapter 2 Knowledge Source
  - Update chapter_2_chunks.py
      - Add structural TODO:
            "chunk_count"
            "expected_section_map"
            "embedding_ready = False"

  # 6 — Contracts
  - Create specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml
      - Document:
          chapter selection flow → RAG → LLM → response
          required placeholders
          API-level routing contract
          context-building contract

  # 7 — Validation Requirements
  - Backend starts with no errors
  - No logic implemented — placeholders ONLY
  - All import paths valid
  - Runtime engine now "aware" of Chapter 2

acceptance_criteria:
  - Chapter 2 is fully wired into AI runtime scaffolding
  - RAG pipeline contains CH2 entry points
  - AI block runtime supports CH2 selection
  - All routing and placeholder comments exist
  - No business logic implemented

success_message: |
  Chapter 2 RAG and Runtime Engine wiring completed successfully. All scaffolding
  for routing, retrieval, context building, and provider mapping is now in place.


/sp.plan
feature-id: 022-ch2-runtime-wiring
sab kuch FAST kerna but in small batches not all at once

goal:
  Create the complete architectural plan for connecting Chapter 2 to the
  AI Runtime Engine, including RAG pipeline hooks, runtime routing,
  AI-block integration, and knowledge source alignment.

plan:
  ## 1. RAG Pipeline Architecture
  - Add new constants for CH2 embeddings
  - Define placeholder functions:
      embed_ch2()
      retrieve_ch2_chunks()
      build_ch2_context()
  - Ensure consistent naming with CH1

  ## 2. Runtime Engine Flow
  - Detect chapter_id=2
  - Pass query → rag_pipeline → provider
  - Add placeholder context merging logic
  - Add placeholder chapter-specific routing notes

  ## 3. AI Block Runtime Layer
  - Update ai_blocks.py to support CH2
  - Add placeholders for:
      ask-question runtime
      explain-like-i-am-10 runtime
      quiz runtime
      diagram runtime

  ## 4. Subagents & Skills
  - Add CH2 TODO branches in all four subagents
  - Ensure skills folder recognises chapter_id input

  ## 5. Contracts
  - Create runtime-wiring.yaml contract
  - Document:
      - RAG → LLM → Block response flow
      - required entrypoints
      - chapter-aware behavior

  ## 6. Validation
  - Ensure backend starts
  - No logic yet; pure structure
  - Imports clean

next_steps:
  Run /sp.tasks to generate atomic tasks for implementation.


/sp.tasks
feature-id: 022-ch2-runtime-wiring
sab kuch FAST kerna but in small batches not all at once

FRONTEND — None

BACKEND — RAG PIPELINE
- [ ] Add CHAPTER_2_COLLECTION constant
- [ ] Add TODO: embed_chapter_2()
- [ ] Add TODO: retrieve_ch2_chunks()
- [ ] Add TODO: build_context_ch2()
- [ ] Validate imports

BACKEND — RUNTIME ENGINE
- [ ] Update engine.py with chapter 2 routing
- [ ] Add TODO: call CH2 RAG pipeline
- [ ] Add TODO: provider selection
- [ ] Add TODO: context generation

BACKEND — AI BLOCK ROUTING
- [ ] Modify ai_blocks.py
- [ ] Add chapter_id=2 support
- [ ] Add TODO: load CH2 context

BACKEND — SUBAGENTS
- [ ] Add CH2 TODO branches in:
      ask_question_agent.py
      explain_el10_agent.py
      quiz_agent.py
      diagram_agent.py

BACKEND — KNOWLEDGE SOURCE MODULE
- [ ] Update chapter_2_chunks.py
- [ ] Add TODO for:
      chunk_count
      section_map
      embedding_ready flag

CONTRACTS
- [ ] Create runtime-wiring.yaml
- [ ] Document flow diagram
- [ ] Document RAG → LLM routing rules

VALIDATION
- [ ] Backend starts without errors
- [ ] All imports resolve
- [ ] No business logic implemented


/sp.implement
feature-id: 022-ch2-runtime-wiring
sab kuch FAST kerna but in small batches not all at once

Implement ONLY:
- structural updates
- file creation
- TODO placeholders
- import scaffolding

DO NOT implement:
- real RAG logic
- real embeddings
- real AI responses

After implementing:
Return the list of files created or updated.


============
23
===========

/sp.specify
feature-id: 023-ch2-ai-blocks
title: "Chapter 2 — AI Block Rendering + MDX Integration"
type: frontend-mdx-integration
sab kuch FAST kerna but in small batches not all at once

goal:
  Enable interactive AI blocks inside Chapter 2.
  This includes MDX placeholders, component mapping, AI-block insertion,
  and validating that Chapter 2 renders correctly with all blocks.

requirements:

  # 1 — Chapter 2 MDX File
  - Ensure frontend/docs/chapters/chapter-2.mdx exists
  - Insert the following placeholders:
      <!-- AI-BLOCK: ask-question -->
      <!-- AI-BLOCK: explain-like-i-am-10 -->
      <!-- AI-BLOCK: interactive-quiz -->
      <!-- AI-BLOCK: generate-diagram -->
  - Insert at correct pedagogical positions (TODO markers only)

  # 2 — Component Mapping
  - Update frontend/src/mdx-components.ts
      - Export AskQuestionBlock, ExplainLike10Block,
        InteractiveQuizBlock, GenerateDiagramBlock
      - Ensure mapping includes CH2 usage

  # 3 — MDX Rendering Layer
  - In chapter-2.mdx, replace placeholders with actual components:
        <AskQuestionBlock chapterId={2} sectionId="..." />
        <ExplainLike10Block chapterId={2} concept="..." />
        <InteractiveQuizBlock chapterId={2} numQuestions={6} />
        <GenerateDiagramBlock chapterId={2} diagramType="..." />
  - Exact content values remain TODO placeholders

  # 4 — Build Validation
  - Run Docusaurus build (placeholder command)
  - Ensure imports are correct

  # 5 — Documentation Contract
  - Create specs/023-ch2-ai-blocks/contracts/ai-block-mdx.yaml
    documenting:
      - block names
      - MDX usage
      - component interface

acceptance_criteria:
  - Chapter 2 MDX renders with all 4 AI blocks.
  - Frontend build passes.
  - Components imported correctly.
  - No real AI logic added.

success_message: |
  Chapter 2 AI Block Integration scaffolding is complete. All placeholders,
  components, MDX mappings, and rendering stubs are now added.


/sp.plan
feature-id: 023-ch2-ai-blocks
sab kuch FAST kerna but in small batches not all at once

goal:
  Prepare MDX + Component architecture to enable interactive AI
  blocks in Chapter 2, mirroring the system used for Chapter 1.

plan:

  ## 1. MDX Structure
  - Confirm chapter-2.mdx exists
  - Insert AI-BLOCK placeholders into pedagogically correct sections
  - Maintain same structure as Chapter 1

  ## 2. Component Wiring
  - Ensure AskQuestionBlock, ExplainLike10Block,
    InteractiveQuizBlock, GenerateDiagramBlock are mapped
  - Verify mdx-components.ts exports them
  - Validate fallback swizzle path if needed

  ## 3. MDX Insertion Plan
  - Map each placeholder to its React component
  - Use chapterId={2} for all components
  - Add sectionId or concept as TODO values

  ## 4. Build Validation Plan
  - Docusaurus build must pass
  - No JSX errors
  - No TypeScript errors

  ## 5. Contracts
  - ai-block-mdx.yaml explains:
      - allowed block types
      - required props
      - chapter-specific usage

next_steps:
  Use /sp.tasks to generate atomic task list.


/sp.tasks
feature-id: 023-ch2-ai-blocks
sab kuch FAST kerna but in small batches not all at once

FRONTEND — MDX SETUP
- [ ] Create or confirm chapter-2.mdx
- [ ] Insert 4 placeholders:
      <!-- AI-BLOCK: ask-question -->
      <!-- AI-BLOCK: explain-like-i-am-10 -->
      <!-- AI-BLOCK: interactive-quiz -->
      <!-- AI-BLOCK: generate-diagram -->
- [ ] Add TODO notes where appropriate

FRONTEND — COMPONENT MAPPING
- [ ] Update mdx-components.ts to include all 4 AI blocks
- [ ] Validate imports
- [ ] Add comments explaining CH2 compatibility

FRONTEND — MDX RENDERING
- [ ] Replace placeholders with:
      <AskQuestionBlock chapterId={2} sectionId="TODO" />
      <ExplainLike10Block chapterId={2} concept="TODO" />
      <InteractiveQuizBlock chapterId={2} numQuestions={6} />
      <GenerateDiagramBlock chapterId={2} diagramType="TODO" />
- [ ] Verify MDX compiles

CONTRACTS
- [ ] Create ai-block-mdx.yaml
- [ ] Document the MDX usage patterns
- [ ] Document required component props

VALIDATION
- [ ] Run Docusaurus build (placeholder)
- [ ] Ensure no React/TS errors
- [ ] Frontend loads Chapter 2 without failing


/sp.implement
feature-id: 023-ch2-ai-blocks
sab kuch FAST kerna but in small batches not all at once

Perform ONLY:
- creation of chapter-2.mdx placeholders
- insertion of component calls
- mdx-components.ts updates
- contract file creation

DO NOT:
- generate real content
- implement logic
- call AI providers

After implementation:
Return list of created + modified files.


==============
24
=============

/sp.specify
feature-id: 024-ch2-runtime-wiring
title: "Chapter 2 — Backend Runtime Wiring for AI Blocks"
type: backend-integration
sab kuch FAST kerna but in small batches not all at once

goal:
  Connect all Chapter 2 interactive blocks (Ask Question, Explain Like I'm 10,
  Quiz Generator, Diagram Generator) to the AI Runtime Engine created in Feature 006.
  This is a pure scaffolding feature with NO real AI logic.

requirements:

  # 1 — API Layer Updates
  - Update backend/app/api/ai_blocks.py so each POST request
    includes chapterId=2 and routes into:
        from app.ai.runtime.engine import run_ai_block
  - Add routing comments:
        # TODO: Chapter 2 runtime call

  # 2 — Runtime Engine Awareness of Chapter 2
  - Update backend/app/ai/runtime/engine.py:
        - Add placeholder routing for chapterId=2
        - Add comments describing expected flows
        - No logic implemented

  # 3 — RAG Layer for Chapter 2
  - Create backend/app/content/chapters/chapter_2_chunks.py
        - Define get_chapter_chunks() → TODO placeholder list
        - Ensure parity with chapter_1_chunks structure

  # 4 — Subagent Draft Files (Placeholders)
  - Create empty scaffolds:
        backend/app/ai/subagents/ch2_ask_question_agent.py
        backend/app/ai/subagents/ch2_explain_el10_agent.py
        backend/app/ai/subagents/ch2_quiz_agent.py
        backend/app/ai/subagents/ch2_diagram_agent.py
  - Each file contains:
        # TODO: blueprint for Chapter 2 version of the agent

  # 5 — Skills Layer Extension
  - Update backend/app/ai/skills/retrieval_skill.py
  - Update backend/app/ai/skills/prompt_builder_skill.py
  - Update backend/app/ai/skills/formatting_skill.py
  - Only add Chapter 2 placeholder routing (no logic)

  # 6 — Contracts
  - Create specs/024-ch2-runtime-wiring/contracts/runtime-flow.yaml
        - Document expected runtime flow for Chapter 2

  # 7 — Stability + Build Requirements
  - Backend must start without errors
  - All new modules must import correctly

acceptance_criteria:
  - Chapter 2 has complete scaffolding for backend runtime.
  - All subagent files exist.
  - Runtime engine references Chapter 2 correctly.
  - No AI logic exists—only placeholders and structure.
  - Backend compiles and runs.

success_message: |
  Chapter 2 backend runtime scaffolding is wired successfully. All routing,
  subagents, skills, and chapter chunk files for Chapter 2 now exist.


/sp.plan
feature-id: 024-ch2-runtime-wiring
sab kuch FAST kerna but in small batches not all at once

goal:
  Mirror Chapter 1 backend runtime structure for Chapter 2,
  ensuring all components are wired but logic is not implemented.

plan:

  ## 1. API Layer
  - Update ai_blocks.py so chapterId=2 cases are routed to run_ai_block()
  - Add TODO notes where final logic will go

  ## 2. Runtime Engine Routing
  - Extend engine.py with Chapter 2 branches
  - Document expected request flow:
        request → rag_pipeline → provider → formatter → response

  ## 3. Chapter 2 Chunk Source
  - Add chapter_2_chunks.py
  - Include empty get_chapter_chunks()

  ## 4. Subagent Structure
  - Mirror Feature 006 agents
  - Create 4 placeholder agents for CH2

  ## 5. Skill Layer Extension
  - Add placeholder routing:
        if chapterId == 2: # TODO
  - Keep logic empty

  ## 6. Contracts
  - Document flow requirements inside runtime-flow.yaml

  ## 7. Validation
  - Backend must run (`uvicorn app.main:app`)
  - All imports must work

next_steps:
  Proceed to /sp.tasks to generate the atomic task list.



/sp.tasks
feature-id: 024-ch2-runtime-wiring
sab kuch FAST kerna but in small batches not all at once

API LAYER
- [ ] Update ai_blocks.py to pass chapterId=2 to run_ai_block
- [ ] Add routing comments for all 4 CH2 endpoints

RUNTIME ENGINE
- [ ] Update engine.py with CH2 placeholder routing
- [ ] Add TODO markers for each runtime stage (rag, llm, format)

CHAPTER CONTENT SOURCE
- [ ] Create chapter_2_chunks.py
- [ ] Add stub: get_chapter_chunks() → returns TODO list

SUBAGENTS
- [ ] Create ch2_ask_question_agent.py
- [ ] Create ch2_explain_el10_agent.py
- [ ] Create ch2_quiz_agent.py
- [ ] Create ch2_diagram_agent.py
- [ ] Add minimal docstring explaining purpose

SKILLS LAYER
- [ ] Update retrieval_skill.py with CH2 placeholder
- [ ] Update prompt_builder_skill.py with CH2 placeholder
- [ ] Update formatting_skill.py with CH2 placeholder

CONTRACTS
- [ ] Create contracts/runtime-flow.yaml
- [ ] Document expected flow sequence

VALIDATION
- [ ] Run backend import check
- [ ] Ensure uvicorn starts successfully



/sp.implement
feature-id: 024-ch2-runtime-wiring
sab kuch FAST kerna but in small batches not all at once

Implement only:
- api_blocks routing updates
- engine placeholder updates
- chapter_2_chunks.py
- CH2 subagent files
- Skill-layer placeholder logic
- runtime-flow.yaml contract file

No AI logic allowed.

Return list of created + modified files.



============
25
============
/sp.specify
feature-id: 025-ch2-diagram-runtime
title: "Chapter 2 — Diagram Generator Runtime"
type: backend-ai-pipeline

goal:
  Build the complete scaffolding for the Chapter 2 Diagram Generator.
  This feature mirrors the architecture of Feature 008 (Chapter 1 Diagram Engine),
  but strictly for Chapter 2. No AI logic, only structure, TODO markers,
  contracts, module files, routing, and placeholders.

requirements:

  # 1 — Diagram Runtime Module (CH2)
  - Create backend/app/ai/diagram/ch2_diagram_runtime.py
        - Blueprint for diagram generation flow
        - Steps:
            1. Validate diagram request
            2. Build prompt (placeholder)
            3. Call RAG (placeholder)
            4. Call provider LLM (placeholder)
            5. Format response (placeholder)
        - All steps contain TODO markers only

  # 2 — Diagram Prompt Template
  - Create backend/app/ai/prompts/diagram/ch2_diagram_prompt.txt
        - Include placeholder template with variables:
            {{diagram_type}}, {{chapter_id}}, {{concepts}}
        - Add TODO comments for engineering full prompt later

  # 3 — Runtime Engine Routing
  - Update backend/app/ai/runtime/engine.py
        - Add Case: if block_type == "diagram" AND chapterId == 2
        - Route to ch2_diagram_runtime.run()
        - Comments only, no logic

  # 4 — API Layer Update
  - Update backend/app/api/ai_blocks.py
        - Diagram endpoint must route to chapter 2 runtime when chapterId=2
        - Add TODO documentation tags

  # 5 — Chapter 2 Diagram Placeholder Contract
  - Create specs/025-ch2-diagram-runtime/contracts/diagram-contract.yaml
        - Define expected placeholders for CH2 diagrams
        - No schemas for actual diagram formats

  # 6 — Skills Extension
  - Update backend/app/ai/skills/prompt_builder_skill.py:
        - Add placeholder: build_diagram_prompt_ch2()
  - Update backend/app/ai/skills/formatting_skill.py:
        - Add placeholder: format_diagram_output_ch2()

  # 7 — Stability Requirement
  - Backend must compile
  - All imports must resolve
  - No diagram generation logic implemented

acceptance_criteria:
  - Diagram runtime module for Chapter 2 exists.
  - Prompt template file exists.
  - Engine correctly routes CH2 diagram requests.
  - AI-block diagram endpoint supports chapterId=2.
  - Contracts folder contains diagram-contract.yaml.
  - No LLM or RAG logic implemented.

success_message: |
  Chapter 2 Diagram Runtime scaffolding created successfully.
  All routing, prompt templates, runtime modules, and contract
  definitions for CH2 diagram generation now exist.



/sp.plan
feature-id: 025-ch2-diagram-runtime

goal:
  Build the scaffolding required to generate diagrams for Chapter 2.
  No diagram generation logic, only structured placeholders.

plan:

  ## 1. Diagram Runtime Module
  - Create ch2_diagram_runtime.py
  - Add run() function with empty steps:
        validate → prompt → rag → llm → format
  - All TODO, no logic.

  ## 2. Prompt Template
  - Create ch2_diagram_prompt.txt
  - Insert placeholder prompt with variables:
        {{diagram_type}}, {{chapter_id}}, {{concepts}}

  ## 3. Runtime Engine
  - Extend engine.py routing:
        if block_type == "diagram" and chapterId == 2
            → call placeholder diagram runtime

  ## 4. API Layer
  - Update ai_blocks.py diagram endpoint so chapterId=2 triggers CH2 runtime

  ## 5. Contracts
  - Create diagram-contract.yaml documenting:
        - expected diagram types
        - placeholder naming rules
        - runtime flow description

  ## 6. Skills
  - Extend prompt_builder_skill and formatting_skill
  - Add empty CH2 placeholder functions

  ## 7. Validation
  - Ensure backend runs
  - Ensure no logic exists

next_steps:
  Move to /sp.tasks to generate atomic implementation tasks.


/sp.tasks
feature-id: 025-ch2-diagram-runtime

DIAGRAM RUNTIME
- [ ] Create backend/app/ai/diagram/ch2_diagram_runtime.py
- [ ] Add run() function with placeholder steps:
      - validate request
      - build prompt
      - run rag query
      - call provider
      - format result

PROMPT TEMPLATE
- [ ] Create backend/app/ai/prompts/diagram/ch2_diagram_prompt.txt
- [ ] Add placeholder variables and TODO markers

ENGINE ROUTING
- [ ] Update backend/app/ai/runtime/engine.py to include CH2 diagram routing
- [ ] Add comments explaining future routing

API LAYER
- [ ] Update backend/app/api/ai_blocks.py:
        if chapterId == 2 and block_type == diagram → route to CH2 runtime

CONTRACTS
- [ ] Create specs/025-ch2-diagram-runtime/contracts/diagram-contract.yaml
- [ ] Document placeholder rules and expected diagram types

SKILLS
- [ ] Update prompt_builder_skill.py: add build_diagram_prompt_ch2()
- [ ] Update formatting_skill.py: add format_diagram_output_ch2()

VALIDATION
- [ ] Run backend and confirm no import errors
- [ ] Confirm new modules are recognized


/sp.implement
feature-id: 025-ch2-diagram-runtime

Implement:
- ch2_diagram_runtime.py (placeholders only)
- ch2_diagram_prompt.txt
- Routing updates in engine.py
- Routing updates in ai_blocks.py
- diagram-contract.yaml
- Skills placeholders

Do NOT implement:
- RAG logic
- LLM calls
- Diagram generation

Return list of all created and modified files.


