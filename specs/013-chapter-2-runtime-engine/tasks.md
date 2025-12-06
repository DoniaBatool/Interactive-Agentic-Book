# Tasks: Chapter 2 — AI Runtime Engine Integration (LLM Routing, RAG Wiring, Subagents, ChatKit)

**Feature**: 013-chapter-2-runtime-engine | **Branch**: `013-chapter-2-runtime-engine` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for activating Chapter 2 runtime engine pathways (scaffolding only, no real AI logic).

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), SETUP (Initial setup), POLISH (Final touches)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before implementing Chapter 2 runtime engine scaffolding.

- [ ] [T001] [P1] [SETUP] Verify runtime engine exists: Check that `backend/app/ai/runtime/engine.py` exists with knowledge source mapping (from Feature 011)
- [ ] [T002] [P1] [SETUP] Verify RAG pipeline exists: Check that `backend/app/ai/rag/pipeline.py` exists with placeholder function `run_rag_pipeline()` (from Feature 005)
- [ ] [T003] [P1] [SETUP] Verify AI blocks API exists: Check that `backend/app/api/ai_blocks.py` exists with Chapter 2 support comments (from Feature 011)
- [ ] [T004] [P1] [SETUP] Verify skills exist: Check that `backend/app/ai/skills/` directory exists with `retrieval_skill.py`, `prompt_builder_skill.py`, `formatting_skill.py`, `quiz_formatting_skill.py`, `diagram_skill.py` (from Feature 005)
- [ ] [T005] [P1] [SETUP] Verify ChatKit exists: Check that `backend/app/ai/chatkit/` directory exists with `session_manager.py` and `tools.py` (from Feature 005)
- [ ] [T006] [P1] [SETUP] Verify settings exists: Check that `backend/app/config/settings.py` exists (from Feature 005)
- [ ] [T007] [P1] [SETUP] Verify .env.example exists: Check that `.env.example` file exists in project root
- [ ] [T008] [P1] [SETUP] Verify Chapter 2 chunks exists: Check that `backend/app/content/chapters/chapter_2_chunks.py` exists (from Feature 011)
- [ ] [T009] [P1] [SETUP] Verify FastAPI backend is functional: Run `cd backend && python -c "from app.main import app; print('Backend imports OK')"` to confirm server can start without errors

**Success Criteria**:
- All prerequisite files exist
- Backend imports resolve without errors
- No breaking changes to existing functionality

**Dependencies**: Feature 005 (AI Runtime Engine), Feature 011 (Chapter 2 AI Blocks), and Feature 012 (Chapter 2 RAG) must be complete

---

## PHASE 1 — Runtime Engine Routing

**User Story**: US1 - Developer Sets Up Chapter 2 Runtime Engine Infrastructure

**Test Strategy**: Can be tested by updating engine.py with Chapter 2 routing comments and verifying imports still work.

### Update Runtime Engine with Chapter 2 Routing

- [ ] [T010] [P1] [US1] Add Chapter 2 routing logic to `backend/app/ai/runtime/engine.py` in `run_ai_block()` function:
  - Add TODO comment block: `# TODO: Chapter 2 routing`
  - Add placeholder code: `# chapter_id = request_data.get("chapterId", 1)`
  - Add conditional routing: `# if chapter_id == 2:`
  - Add TODO: `#     # TODO: Check ENABLE_CHAPTER_2_RUNTIME flag`
  - Add TODO: `#     # if not ENABLE_CHAPTER_2_RUNTIME:`
  - Add TODO: `#     #     return {"error": "Chapter 2 runtime disabled"}`

- [ ] [T011] [P1] [US1] Add Chapter 2 subagent mapping to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Route to Chapter 2 subagent`
  - Add mapping structure: `# CH2_SUBAGENT_MAP = {`
  - Add mapping entries: `#     "ask-question": ch2_ask_question_agent,`
  - Add mapping entries: `#     "explain-like-10": ch2_explain_el10_agent,`
  - Add mapping entries: `#     "quiz": ch2_quiz_agent,`
  - Add mapping entries: `#     "diagram": ch2_diagram_agent,`
  - Add mapping entries: `# }`

- [ ] [T012] [P1] [US1] Add Chapter 2 subagent imports to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Import Chapter 2 subagents`
  - Add import: `# from app.ai.subagents.ch2_ask_question_agent import ch2_ask_question_agent`
  - Add import: `# from app.ai.subagents.ch2_explain_el10_agent import ch2_explain_el10_agent`
  - Add import: `# from app.ai.subagents.ch2_quiz_agent import ch2_quiz_agent`
  - Add import: `# from app.ai.subagents.ch2_diagram_agent import ch2_diagram_agent`

- [ ] [T013] [P1] [US1] Add Chapter 2 RAG context loading to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Load Chapter 2 RAG context`
  - Add import: `# from app.ai.rag.pipeline import run_rag_pipeline`
  - Add query extraction: `# query = request_data.get("question") or request_data.get("concept") or ""`
  - Add RAG call: `# context = await run_rag_pipeline(query, chapter_id=2, top_k=5)`

- [ ] [T014] [P1] [US1] Add Chapter 2 subagent invocation to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Call Chapter 2 subagent with context`
  - Add subagent selection: `# subagent = CH2_SUBAGENT_MAP.get(block_type)`
  - Add error handling: `# if not subagent:`
  - Add error return: `#     return {"error": f"Unknown block type: {block_type}"}`
  - Add subagent call: `# result = await subagent(request_data, context)`

- [ ] [T015] [P1] [US1] Add Chapter 2 response formatting to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Format response`
  - Add formatting call: `# formatted = format_response(result, block_type, chapter_id=2)`
  - Add return: `# return formatted`

- [ ] [T016] [P1] [US1] Add placeholder LLM invocation comments to `backend/app/ai/runtime/engine.py`:
  - Add TODO comment: `# TODO: Placeholder LLM invocation for Chapter 2`
  - Add comment: `# LLM provider will be selected from DEFAULT_CH2_MODEL setting`
  - Add comment: `# LLM will receive ROS 2 context from RAG pipeline`
  - Add comment: `# LLM will generate response with ROS 2 knowledge`

- [ ] [T017] [P1] [US1] Verify engine.py is importable after updates: Run `cd backend && python -c "from app.ai.runtime.engine import run_ai_block; print('Import successful')"` - should complete without errors

**Acceptance Test**: Runtime engine has Chapter 2 routing logic with comprehensive TODO comments, imports work, no syntax errors

---

## PHASE 2 — AI Block API Binding

**User Story**: US1 - Developer Sets Up Chapter 2 Runtime Engine Infrastructure

**Test Strategy**: Can be tested by verifying ai_blocks.py routes Chapter 2 requests correctly.

### Verify and Update AI Blocks API

- [ ] [T018] [P1] [US1] Verify `backend/app/api/ai_blocks.py` has Chapter 2 support comment in module docstring:
  - Check for: `"Supports Chapter 1 (chapterId=1) and Chapter 2 (chapterId=2)"`

- [ ] [T019] [P1] [US1] Verify `ask_question()` endpoint in `backend/app/api/ai_blocks.py` accepts `chapterId` parameter:
  - Check request model includes `chapterId: int`
  - Check endpoint calls `run_ai_block("ask-question", request_data)` with `chapterId` included

- [ ] [T020] [P1] [US1] Verify `explain_like_10()` endpoint in `backend/app/api/ai_blocks.py` accepts `chapterId` parameter:
  - Check request model includes `chapterId: int`
  - Check endpoint calls `run_ai_block("explain-like-10", request_data)` with `chapterId` included

- [ ] [T021] [P1] [US1] Verify `generate_quiz()` endpoint in `backend/app/api/ai_blocks.py` accepts `chapterId` parameter:
  - Check request model includes `chapterId: int`
  - Check endpoint calls `run_ai_block("quiz", request_data)` with `chapterId` included

- [ ] [T022] [P1] [US1] Verify `generate_diagram()` endpoint in `backend/app/api/ai_blocks.py` accepts `chapterId` parameter:
  - Check request model includes `chapterId: int`
  - Check endpoint calls `run_ai_block("diagram", request_data)` with `chapterId` included

- [ ] [T023] [P1] [US1] Add Chapter 2 routing verification comment to `backend/app/api/ai_blocks.py`:
  - Add comment: `# TODO: For chapterId=2, all block types route to run_ai_block(block_type, chapter_id=2)`
  - Add comment: `# Runtime engine will handle Chapter 2 routing internally`

- [ ] [T024] [P1] [US1] Verify ai_blocks.py is importable: Run `cd backend && python -c "from app.api.ai_blocks import ask_question, explain_like_10, generate_quiz, generate_diagram; print('Import successful')"` - should complete without errors

**Acceptance Test**: All AI block endpoints accept chapterId parameter and route to run_ai_block correctly, imports work

---

## PHASE 3 — Subagent Scaffolding

**User Story**: US1 - Developer Sets Up Chapter 2 Runtime Engine Infrastructure

**Test Strategy**: Can be tested by creating subagent files with placeholder functions and verifying imports work.

### Create Chapter 2 Ask Question Agent

- [ ] [T025] [P1] [US1] Create `backend/app/ai/subagents/ch2_ask_question_agent.py`:
  - Add module docstring: `"""Chapter 2 Ask Question Agent - Answers questions about ROS 2 concepts using Chapter 2 context."""`
  - Add imports: `from typing import Dict, Any`
  - Add function signature: `async def ch2_ask_question_agent(question: str, context: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Description: Process ROS 2 questions with Chapter 2 RAG context
    - TODO: Use retrieval_skill to get additional context if needed
    - TODO: Use prompt_builder_skill to construct ROS 2 question-answering prompt
    - TODO: Call LLM provider (DEFAULT_CH2_MODEL) with prompt + context
    - TODO: Use formatting_skill to format response with source citations
    - TODO: Return formatted answer
  - Add placeholder return: `return {"answer": "", "sources": [], "confidence": 0.0}`

- [ ] [T026] [P1] [US1] Verify ch2_ask_question_agent.py is importable: Run `cd backend && python -c "from app.ai.subagents.ch2_ask_question_agent import ch2_ask_question_agent; print('Import successful')"` - should complete without errors

### Create Chapter 2 Explain ELI10 Agent

- [ ] [T027] [P1] [US1] Create `backend/app/ai/subagents/ch2_explain_el10_agent.py`:
  - Add module docstring: `"""Chapter 2 Explain Like I'm 10 Agent - Generates simplified explanations for ROS 2 concepts."""`
  - Add imports: `from typing import Dict, Any`
  - Add function signature: `async def ch2_explain_el10_agent(concept: str, context: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Description: Generate ROS 2 explanation with Chapter 2 context
    - TODO: Use prompt_builder_skill to build ELI10 prompt with ROS 2 context
    - TODO: Call LLM provider (DEFAULT_CH2_MODEL) with ELI10 instructions
    - TODO: Use formatting_skill to extract examples and analogies
    - TODO: Return formatted explanation
  - Add placeholder return: `return {"explanation": "", "examples": [], "analogies": []}`

- [ ] [T028] [P1] [US1] Verify ch2_explain_el10_agent.py is importable: Run `cd backend && python -c "from app.ai.subagents.ch2_explain_el10_agent import ch2_explain_el10_agent; print('Import successful')"` - should complete without errors

### Create Chapter 2 Quiz Agent

- [ ] [T029] [P1] [US1] Create `backend/app/ai/subagents/ch2_quiz_agent.py`:
  - Add module docstring: `"""Chapter 2 Quiz Agent - Generates interactive quizzes for ROS 2 learning objectives."""`
  - Add imports: `from typing import Dict, Any, List`
  - Add function signature: `async def ch2_quiz_agent(chapter_id: int, num_questions: int, context: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Description: Generate ROS 2 quiz with Chapter 2 context
    - TODO: Use retrieval_skill to get learning objectives from Chapter 2 metadata
    - TODO: Use prompt_builder_skill to build quiz generation prompt
    - TODO: Call LLM provider (DEFAULT_CH2_MODEL) to generate questions
    - TODO: Use formatting_skill to structure quiz data
    - TODO: Return formatted quiz
  - Add placeholder return: `return {"questions": [], "learning_objectives": []}`

- [ ] [T030] [P1] [US1] Verify ch2_quiz_agent.py is importable: Run `cd backend && python -c "from app.ai.subagents.ch2_quiz_agent import ch2_quiz_agent; print('Import successful')"` - should complete without errors

### Create Chapter 2 Diagram Agent

- [ ] [T031] [P1] [US1] Create `backend/app/ai/subagents/ch2_diagram_agent.py`:
  - Add module docstring: `"""Chapter 2 Diagram Agent - Generates visual diagrams for ROS 2 concepts."""`
  - Add imports: `from typing import Dict, Any, List`
  - Add function signature: `async def ch2_diagram_agent(diagram_type: str, concepts: List[str], context: Dict[str, Any]) -> Dict[str, Any]:`
  - Add comprehensive docstring with:
    - Description: Generate ROS 2 diagram with Chapter 2 context
    - TODO: Use prompt_builder_skill to build diagram generation prompt
    - TODO: Call LLM provider (DEFAULT_CH2_MODEL) or diagram generation API
    - TODO: Use formatting_skill to format diagram output
    - TODO: Return diagram URL/metadata
  - Add placeholder return: `return {"diagram_url": "", "metadata": {"title": "", "description": "", "concepts": [], "format": ""}}`

- [ ] [T032] [P1] [US1] Verify ch2_diagram_agent.py is importable: Run `cd backend && python -c "from app.ai.subagents.ch2_diagram_agent import ch2_diagram_agent; print('Import successful')"` - should complete without errors

**Acceptance Test**: All 4 Chapter 2 subagent files exist with placeholder functions, comprehensive TODOs, and correct signatures. All imports work.

---

## PHASE 4 — Skills Updates

**User Story**: US1 - Developer Sets Up Chapter 2 Runtime Engine Infrastructure

**Test Strategy**: Can be tested by adding Chapter 2 TODO comments to skills files and verifying imports still work.

### Update Retrieval Skill

- [ ] [T033] [P1] [US1] Add Chapter 2 TODO comments to `backend/app/ai/skills/retrieval_skill.py` in `retrieve_content()` function:
  - Add TODO: `# TODO: Chapter-aware retrieval`
  - Add TODO: `# TODO: If chapter_id == 2:`
  - Add TODO: `# TODO:     Use Chapter 2 RAG pipeline`
  - Add TODO: `# TODO:     from app.ai.rag.pipeline import run_rag_pipeline`
  - Add TODO: `# TODO:     context = await run_rag_pipeline(query, chapter_id=2, top_k=top_k)`
  - Add TODO: `# TODO:     Return Chapter 2 chunks with ROS 2 context`
  - Add TODO: `# TODO: Elif chapter_id == 1:`
  - Add TODO: `# TODO:     Use Chapter 1 RAG pipeline (existing logic)`

- [ ] [T034] [P1] [US1] Update `retrieve_content()` function signature in `backend/app/ai/skills/retrieval_skill.py`:
  - Add `chapter_id: int` parameter to function signature
  - Update docstring to mention chapter_id parameter

- [ ] [T035] [P1] [US1] Verify retrieval_skill.py is importable: Run `cd backend && python -c "from app.ai.skills.retrieval_skill import retrieve_content; print('Import successful')"` - should complete without errors

### Update Prompt Builder Skill

- [ ] [T036] [P1] [US1] Add Chapter 2 TODO comments to `backend/app/ai/skills/prompt_builder_skill.py` in `build_prompt()` function:
  - Add TODO: `# TODO: Chapter-aware prompt builder`
  - Add TODO: `# TODO: If chapter_id == 2:`
  - Add TODO: `# TODO:     Build ROS 2-specific prompts`
  - Add TODO: `# TODO:     Include ROS 2 concepts, analogies, examples`
  - Add TODO: `# TODO:     System prompt: "You are a helpful tutor explaining ROS 2 concepts..."`
  - Add TODO: `# TODO:     Include ROS 2 context chunks`
  - Add TODO: `# TODO:     Add ROS 2 terminology guidelines`
  - Add TODO: `# TODO: Elif chapter_id == 1:`
  - Add TODO: `# TODO:     Build Chapter 1 prompts (existing logic)`

- [ ] [T037] [P1] [US1] Update `build_prompt()` function signature in `backend/app/ai/skills/prompt_builder_skill.py`:
  - Add `chapter_id: int = None` parameter to function signature
  - Update docstring to mention chapter_id parameter

- [ ] [T038] [P1] [US1] Verify prompt_builder_skill.py is importable: Run `cd backend && python -c "from app.ai.skills.prompt_builder_skill import build_prompt; print('Import successful')"` - should complete without errors

### Update Formatting Skill

- [ ] [T039] [P1] [US1] Add Chapter 2 TODO comments to `backend/app/ai/skills/formatting_skill.py` in `format_response()` function:
  - Add TODO: `# TODO: Chapter 2 formatting rules`
  - Add TODO: `# TODO: If chapter_id == 2:`
  - Add TODO: `# TODO:     Apply Chapter 2 formatting rules`
  - Add TODO: `# TODO:     Include ROS 2-specific metadata`
  - Add TODO: `# TODO:     Format ROS 2 source citations`
  - Add TODO: `# TODO:     Format ROS 2 examples and analogies`
  - Add TODO: `# TODO: Elif chapter_id == 1:`
  - Add TODO: `# TODO:     Apply Chapter 1 formatting rules (existing logic)`

- [ ] [T040] [P1] [US1] Update `format_response()` function signature in `backend/app/ai/skills/formatting_skill.py`:
  - Add `chapter_id: int = None` parameter to function signature
  - Update docstring to mention chapter_id parameter

- [ ] [T041] [P1] [US1] Verify formatting_skill.py is importable: Run `cd backend && python -c "from app.ai.skills.formatting_skill import format_response; print('Import successful')"` - should complete without errors

### Update Quiz Formatting Skill

- [ ] [T042] [P1] [US1] Add Chapter 2 TODO comments to `backend/app/ai/skills/quiz_formatting_skill.py`:
  - Add TODO: `# TODO: Chapter 2 quiz formatting rules`
  - Add TODO: `# TODO: Format ROS 2 quiz questions with ROS 2 terminology`
  - Add TODO: `# TODO: Include ROS 2 examples in quiz questions`

- [ ] [T043] [P1] [US1] Verify quiz_formatting_skill.py is importable: Run `cd backend && python -c "from app.ai.skills.quiz_formatting_skill import *; print('Import successful')"` - should complete without errors

### Update Diagram Skill

- [ ] [T044] [P1] [US1] Add Chapter 2 TODO comments to `backend/app/ai/skills/diagram_skill.py`:
  - Add TODO: `# TODO: Chapter 2 diagram generation rules`
  - Add TODO: `# TODO: Generate ROS 2 diagram structures`
  - Add TODO: `# TODO: Format ROS 2 diagram metadata`

- [ ] [T045] [P1] [US1] Verify diagram_skill.py is importable: Run `cd backend && python -c "from app.ai.skills.diagram_skill import *; print('Import successful')"` - should complete without errors

**Acceptance Test**: All 5 skills files have Chapter 2 TODO comments, function signatures updated with chapter_id parameter, imports work

---

## PHASE 5 — RAG Connection

**User Story**: US1 - Developer Sets Up Chapter 2 Runtime Engine Infrastructure

**Test Strategy**: Can be tested by verifying pipeline.py has Chapter 2 binding comments.

### Update RAG Pipeline for Chapter 2

- [ ] [T046] [P1] [US1] Verify `backend/app/ai/rag/pipeline.py` has Chapter 2 flow comments from Feature 012:
  - Check for: `"TODO: Chapter 2 specific flow (when chapter_id=2)"`
  - Check for: `"Step 1: Call get_chapter_chunks(chapter_id=2)"`
  - Check for: `"Step 2: Call generate_embedding(query)"`
  - Check for: `"Step 3: Call similarity_search(collection="chapter_2", ...)"`

- [ ] [T047] [P1] [US1] Add Chapter 2 contextual step comments to `backend/app/ai/rag/pipeline.py` in `run_rag_pipeline()` function:
  - Add comment: `# TODO: Ensure pipeline resolves chapter_2_chunks when chapter_id=2`
  - Add comment: `# TODO: Chapter 2 chunks are loaded from app.content.chapters.chapter_2_chunks`
  - Add comment: `# TODO: Chapter 2 collection name is "chapter_2" (from QDRANT_COLLECTION_CH2 env var)`

- [ ] [T048] [P1] [US1] Add placeholder retrieval context injection comments to `backend/app/ai/rag/pipeline.py`:
  - Add comment: `# TODO: Assemble retrieval context for Chapter 2`
  - Add comment: `# TODO: context = {`
  - Add comment: `# TODO:     "context": assemble_context_string(results),`
  - Add comment: `# TODO:     "chunks": results,`
  - Add comment: `# TODO:     "query_embedding": query_embedding`
  - Add comment: `# TODO: }`
  - Add comment: `# TODO: Filter by section_id if provided`
  - Add comment: `# TODO: Limit context size (RAG_MAX_CONTEXT env var, default: 4 chunks)`

- [ ] [T049] [P1] [US1] Verify pipeline.py is importable: Run `cd backend && python -c "from app.ai.rag.pipeline import run_rag_pipeline; print('Import successful')"` - should complete without errors

**Acceptance Test**: RAG pipeline has Chapter 2 binding comments, placeholder context injection comments, imports work

---

## PHASE 6 — ChatKit Integration

**User Story**: US1 - Developer Sets Up Chapter 2 Runtime Engine Infrastructure

**Test Strategy**: Can be tested by adding Chapter 2 placeholder comments to ChatKit files and verifying imports work.

### Update Session Manager

- [ ] [T050] [P1] [US1] Add multi-chapter session context placeholder to `backend/app/ai/chatkit/session_manager.py` in `create_session()` function:
  - Add TODO: `# TODO: Multi-chapter session contexts`
  - Add TODO: `# TODO: Track Chapter 2 context in session`
  - Add TODO: `# TODO: Initialize chapter_context dictionary:`
  - Add TODO: `# TODO:     {`
  - Add TODO: `# TODO:         2: {`
  - Add TODO: `# TODO:             "last_accessed": timestamp,`
  - Add TODO: `# TODO:             "message_count": 0,`
  - Add TODO: `# TODO:             "topics": []`
  - Add TODO: `# TODO:         }`
  - Add TODO: `# TODO:     }`
  - Add TODO: `# TODO: Support cross-chapter queries`

- [ ] [T051] [P1] [US1] Add Chapter 2 message appending placeholder to `backend/app/ai/chatkit/session_manager.py` in `append_message()` function:
  - Add TODO: `# TODO: Append message with Chapter 2 context`
  - Add TODO: `# TODO: If message has chapterId=2:`
  - Add TODO: `# TODO:     Update Chapter 2 context in session`
  - Add TODO: `# TODO:     Track ROS 2 topics discussed`
  - Add TODO: `# TODO:     Update last_accessed timestamp`

- [ ] [T052] [P1] [US1] Add Chapter 2 history retrieval placeholder to `backend/app/ai/chatkit/session_manager.py` in `get_history()` function:
  - Add TODO: `# TODO: Retrieve session history with Chapter 2 context`
  - Add TODO: `# TODO: If chapter_id == 2:`
  - Add TODO: `# TODO:     Filter messages by chapterId=2`
  - Add TODO: `# TODO:     Include Chapter 2 context metadata`
  - Add TODO: `# TODO: Return Chapter 2 message history`

- [ ] [T053] [P1] [US1] Verify session_manager.py is importable: Run `cd backend && python -c "from app.ai.chatkit.session_manager import create_session, append_message, get_history; print('Import successful')"` - should complete without errors

### Update Tools

- [ ] [T054] [P1] [US1] Add Chapter 2 tool definitions to `backend/app/ai/chatkit/tools.py`:
  - Add comment: `# TODO: Chapter 2 Tool Definitions`
  - Add tool definition comment block for `ch2_ask_question_tool`:
    - `# ch2_ask_question_tool:`
    - `#   name: "ch2_ask_question"`
    - `#   description: "Ask questions about ROS 2 concepts"`
    - `#   input: {"question": str, "sectionId": str (optional)}`
    - `#   output: {"answer": str, "sources": List[str]}`
  - Add tool definition comment block for `ch2_explain_el10_tool`:
    - `# ch2_explain_el10_tool:`
    - `#   name: "ch2_explain_el10"`
    - `#   description: "Explain ROS 2 concepts like I'm 10"`
    - `#   input: {"concept": str}`
    - `#   output: {"explanation": str, "examples": List[str]}`
  - Add tool definition comment block for `ch2_quiz_tool`:
    - `# ch2_quiz_tool:`
    - `#   name: "ch2_quiz"`
    - `#   description: "Generate ROS 2 quizzes"`
    - `#   input: {"numQuestions": int}`
    - `#   output: {"questions": List[Dict], "learning_objectives": List[str]}`
  - Add tool definition comment block for `ch2_diagram_tool`:
    - `# ch2_diagram_tool:`
    - `#   name: "ch2_diagram"`
    - `#   description: "Generate ROS 2 diagrams"`
    - `#   input: {"diagramType": str, "concepts": List[str]}`
    - `#   output: {"diagram_url": str, "metadata": Dict}`

- [ ] [T055] [P1] [US1] Add Chapter 2 tool implementation TODOs to `backend/app/ai/chatkit/tools.py`:
  - Add TODO: `# TODO: Implement tool definitions when ChatKit integrated`
  - Add TODO: `# TODO: Register tools with ChatKit session`
  - Add TODO: `# TODO: Handle tool calls from ChatKit`
  - Add TODO: `# TODO: Return tool results to ChatKit`

- [ ] [T056] [P1] [US1] Verify tools.py is importable: Run `cd backend && python -c "from app.ai.chatkit.tools import *; print('Import successful')"` - should complete without errors

**Acceptance Test**: ChatKit files have Chapter 2 placeholder comments, tool definitions documented, imports work

---

## PHASE 7 — Config & ENV

**User Story**: US2 - System Administrator Configures Chapter 2 Runtime Settings

**Test Strategy**: Can be tested by adding Chapter 2 settings and env vars, verifying backend can read them.

### Update Settings

- [ ] [T057] [P2] [US2] Add Chapter 2 model setting to `backend/app/config/settings.py`:
  - Add setting: `DEFAULT_CH2_MODEL: str = "gpt-4o-mini"` (or from env var)
  - Add comment: `# Default LLM model for Chapter 2 runtime`
  - Add env var mapping: `os.getenv("DEFAULT_CH2_MODEL", "gpt-4o-mini")`

- [ ] [T058] [P2] [US2] Add Chapter 2 embeddings setting to `backend/app/config/settings.py`:
  - Add setting: `DEFAULT_CH2_EMBEDDINGS: str = "text-embedding-3-small"` (or from env var)
  - Add comment: `# Default embedding model for Chapter 2`
  - Add env var mapping: `os.getenv("DEFAULT_CH2_EMBEDDINGS", "text-embedding-3-small")`

- [ ] [T059] [P2] [US2] Add Chapter 2 runtime enable flag to `backend/app/config/settings.py`:
  - Add setting: `ENABLE_CHAPTER_2_RUNTIME: bool = True` (or from env var)
  - Add comment: `# Enable/disable Chapter 2 runtime engine`
  - Add env var mapping: `os.getenv("ENABLE_CHAPTER_2_RUNTIME", "true").lower() == "true"`

- [ ] [T060] [P2] [US2] Verify settings.py is importable: Run `cd backend && python -c "from app.config.settings import DEFAULT_CH2_MODEL, DEFAULT_CH2_EMBEDDINGS, ENABLE_CHAPTER_2_RUNTIME; print('Import successful')"` - should complete without errors

### Update Environment Variables

- [ ] [T061] [P2] [US2] Add Chapter 2 model env var to `.env.example`:
  - Add variable: `DEFAULT_CH2_MODEL="gpt-4o-mini"`
  - Add description: `# Default LLM model for Chapter 2 runtime (OpenAI)`

- [ ] [T062] [P2] [US2] Add Chapter 2 embeddings env var to `.env.example`:
  - Add variable: `DEFAULT_CH2_EMBEDDINGS="text-embedding-3-small"`
  - Add description: `# Default embedding model for Chapter 2 (OpenAI)`

- [ ] [T063] [P2] [US2] Add Chapter 2 runtime enable flag to `.env.example`:
  - Add variable: `ENABLE_CHAPTER_2_RUNTIME=true`
  - Add description: `# Enable/disable Chapter 2 runtime engine (true/false)`

**Acceptance Test**: Settings file has Chapter 2 configuration options, .env.example has all new variables documented, backend can read settings

---

## PHASE 8 — Validation & Testing

**User Story**: US1, US2, US3 - All User Stories

**Test Strategy**: Comprehensive validation of all scaffolding changes.

### Import Validation

- [ ] [T064] [P1] [US1] Verify all new subagent files are importable:
  - Run: `cd backend && python -c "from app.ai.subagents.ch2_ask_question_agent import ch2_ask_question_agent; from app.ai.subagents.ch2_explain_el10_agent import ch2_explain_el10_agent; from app.ai.subagents.ch2_quiz_agent import ch2_quiz_agent; from app.ai.subagents.ch2_diagram_agent import ch2_diagram_agent; print('All subagents importable')"`

- [ ] [T065] [P1] [US1] Verify all updated files are importable:
  - Run: `cd backend && python -c "from app.ai.runtime.engine import run_ai_block; from app.ai.rag.pipeline import run_rag_pipeline; from app.api.ai_blocks import *; from app.ai.skills import *; from app.ai.chatkit import *; from app.config.settings import *; print('All imports successful')"`

### Backend Startup Validation

- [ ] [T066] [P1] [US1] Verify backend starts without errors:
  - Run: `cd backend && python -c "from app.main import app; print('Backend startup OK')"` - should complete without errors

### Placeholder Function Validation

- [ ] [T067] [P1] [US1] Verify all subagent functions return placeholder values:
  - Run: `cd backend && python -c "from app.ai.subagents.ch2_ask_question_agent import ch2_ask_question_agent; import asyncio; result = asyncio.run(ch2_ask_question_agent('test', {})); assert result == {'answer': '', 'sources': [], 'confidence': 0.0}, f'Unexpected result: {result}'; print('Placeholder return verified')"`

### File Existence Validation

- [ ] [T068] [P1] [US1] Verify all required files exist:
  - Check: `backend/app/ai/subagents/ch2_ask_question_agent.py` exists
  - Check: `backend/app/ai/subagents/ch2_explain_el10_agent.py` exists
  - Check: `backend/app/ai/subagents/ch2_quiz_agent.py` exists
  - Check: `backend/app/ai/subagents/ch2_diagram_agent.py` exists

### TODO Comment Validation

- [ ] [T069] [P1] [US1] Verify all files have comprehensive TODO comments:
  - Check: engine.py has Chapter 2 routing TODOs
  - Check: All subagent files have implementation TODOs
  - Check: All skills files have Chapter 2 TODOs
  - Check: ChatKit files have Chapter 2 TODOs

**Acceptance Test**: All imports work, backend starts, placeholder functions return expected values, all files exist with comprehensive TODOs

---

## Summary

**Total Tasks**: 69 tasks across 8 phases
- Phase 0: Setup & Prerequisites (9 tasks)
- Phase 1: Runtime Engine Routing (8 tasks)
- Phase 2: AI Block API Binding (7 tasks)
- Phase 3: Subagent Scaffolding (8 tasks)
- Phase 4: Skills Updates (13 tasks)
- Phase 5: RAG Connection (4 tasks)
- Phase 6: ChatKit Integration (7 tasks)
- Phase 7: Config & ENV (7 tasks)
- Phase 8: Validation & Testing (6 tasks)

**Estimated Time**: ~2-3 hours (scaffolding only, no real implementation)

**Success Criteria**:
- All 4 Chapter 2 subagent files created with placeholder functions
- Runtime engine has Chapter 2 routing logic (commented)
- All skills have Chapter 2 TODO comments
- ChatKit has Chapter 2 placeholder scaffolding
- Configuration settings added for Chapter 2
- All imports resolve, backend starts successfully
- No real AI logic implemented (scaffolding only)

**Next Step**: Run `/sp.implement` to execute all tasks
