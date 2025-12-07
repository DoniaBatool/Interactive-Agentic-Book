# Implementation Plan: Chapter 2 — AI Blocks Integration Layer

**Branch**: `034-chapter-2-ai-blocks` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/034-chapter-2-ai-blocks/spec.md`

## Summary

This feature connects Chapter 2's AI Blocks to the global AI Runtime Engine by creating scaffolding for API endpoint routing, runtime engine routing, subagents, skills extensions, and pipeline connection. The implementation establishes the architectural foundation for Chapter 2 runtime engine integration with API endpoints, Chapter 2-specific routing, subagents, chapter-aware skills, and pipeline integration. **No real AI logic is implemented**—only scaffolding, function signatures, TODO placeholders, and architectural blueprints to prepare for future AI implementation.

**Primary Deliverable**: Complete Chapter 2 runtime engine integration scaffolding (API endpoints, runtime routing, subagents, skills, pipeline connection, contract)
**Validation**: All files exist, imports resolve, backend starts, no runtime errors

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- No new runtime dependencies required (scaffolding only)
- Existing runtime engine, RAG pipeline, skills from Feature 005
- Existing Chapter 3 runtime patterns from Feature 030 (for reference)
- Chapter 2 content from Feature 033 (MDX file and metadata)

**Storage**: 
- No persistent storage (scaffolding only)
- Future: Qdrant for Chapter 2 vectors, Postgres for sessions

**Testing**:
- Manual: File existence verification, import resolution, backend startup
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)

**Project Type**: Backend AI runtime infrastructure integration scaffolding

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (no API calls, no LLM calls, no RAG execution)
- MUST maintain compatibility with Feature 005 (Chapter 1 runtime must still work)
- MUST maintain compatibility with Feature 030 (Chapter 3 runtime must still work)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality
- MUST follow Chapter 3 AI runtime patterns exactly

**Scale/Scope**:
- 4 new API endpoints (Chapter 2 endpoints)
- 1 runtime engine file to update (add chapterId=2 routing)
- 4 subagent files to create (ch2_*_agent.py)
- 2 skills files to update (add Chapter 2 TODOs)
- 1 pipeline file to update (add Chapter 2 routing)
- 1 contract file to create
- ~200-300 lines of scaffolding code (mostly signatures, TODOs, and comments)

---

## 1. Folder Structure

### 1.1 New Files

**Directory**: `backend/app/ai/subagents/`
- **Status**: Already exists (from Feature 005)
- **Files to Create**:
  - `ch2_ask_agent.py` (NEW - Chapter 2 ask question agent)
  - `ch2_explain_agent.py` (NEW - Chapter 2 ELI10 agent)
  - `ch2_quiz_agent.py` (NEW - Chapter 2 quiz agent)
  - `ch2_diagram_agent.py` (NEW - Chapter 2 diagram agent)

### 1.2 Existing Directories (To Be Extended)

**Directory**: `backend/app/api/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `ai_blocks.py` (add 4 new Chapter 2 endpoints)

**Directory**: `backend/app/ai/runtime/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `engine.py` (extend with chapterId=2 routing)

**Directory**: `backend/app/ai/skills/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `prompt_builder_skill.py` (add Chapter 2 TODOs)
  - `formatting_skill.py` (add Chapter 2 TODOs)

**Directory**: `backend/app/ai/rag/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `pipeline.py` (add Chapter 2 routing)

**Directory**: `specs/034-chapter-2-ai-blocks/contracts/`
- **Status**: Already exists (from spec phase)
- **Files to Verify**:
  - `ai-block-runtime.yaml` (verify exists from spec phase)

---

## 2. Runtime Flow Design

### 2.1 Chapter 2 Runtime Flow

**Flow**: CH2 Query → API Endpoint → Runtime Engine → RAG Pipeline → Subagent → LLM Provider → Response

```
Frontend Component (Chapter 2)
    │
    ▼
API Endpoint (ai_blocks.py) - Chapter 2 endpoints
    ├─► POST /ai/ch2/ask
    ├─► POST /ai/ch2/explain
    ├─► POST /ai/ch2/quiz
    └─► POST /ai/ch2/diagram
    │
    ▼
Runtime Engine (engine.py)
    │
    ├─► Router: Determine block type → Select Chapter 2 subagent
    │   ├─► If chapterId=2:
    │   │   ├─► Route to ch2_ask_agent
    │   │   ├─► Route to ch2_explain_agent
    │   │   ├─► Route to ch2_quiz_agent
    │   │   └─► Route to ch2_diagram_agent
    │
    ├─► RAG Pipeline (pipeline.py)
    │   ├─► Load Chapter 2 chunks (chapter_2_chunks.py)
    │   ├─► Embed user query (embedding_client.py with chapter=2)
    │   ├─► Qdrant similarity search (collection="chapter_2")
    │   └─► Construct retrieval context
    │
    ├─► Skills System (chapter-aware)
    │   ├─► Retrieval Skill (retrieval_skill.py) - Chapter 2 context
    │   ├─► Prompt Builder Skill (prompt_builder_skill.py) - Mechanical Systems prompts
    │   └─► Formatting Skill (formatting_skill.py) - Chapter 2 formatting
    │
    ├─► Chapter 2 Subagent
    │   ├─► ch2_ask_agent.py
    │   ├─► ch2_explain_agent.py
    │   ├─► ch2_quiz_agent.py
    │   └─► ch2_diagram_agent.py
    │   └─► Uses skills + RAG context → Generates Mechanical Systems response
    │
    ├─► LLM Provider (base_llm.py → openai_provider.py | gemini_provider.py)
    │   └─► Generates response with Mechanical Systems context
    │
    └─► Response Formatting → Return to API → Frontend
```

### 2.2 Data Flow

1. **Request**: Frontend sends request with chapterId=2 → API endpoint receives
2. **Routing**: Runtime engine identifies chapterId=2 → routes to Chapter 2 subagent
3. **RAG Pipeline**: RAG pipeline retrieves Chapter 2 context from Qdrant
4. **Embedding**: Embedding client generates embeddings with chapter=2 support
5. **Skills**: Skills assemble Mechanical Systems context + user input into prompts
6. **Subagent**: Chapter 2 subagent processes with Mechanical Systems context
7. **LLM**: LLM provider generates response with Mechanical Systems context
8. **Formatting**: Skills format response for frontend
9. **Response**: API returns formatted response → Frontend displays

---

## 3. Module-Level Design

### 3.1 API Endpoint Routing

**File**: `backend/app/api/ai_blocks.py`

**Purpose**: Add 4 new endpoints for Chapter 2

**Current State**: Has existing endpoints for Chapter 1 and Chapter 3

**Updates Required**:
- Add 4 new endpoints:
  - `POST /ai/ch2/ask`
  - `POST /ai/ch2/explain`
  - `POST /ai/ch2/quiz`
  - `POST /ai/ch2/diagram`
- Each endpoint should call: `run_ai_block(block_type="...", request_data=...)` where `request_data` includes `chapterId=2`
- No logic. Only call + placeholder.

**Input/Output Schemas** (Text Description):

**ch2_ask(request)**:
- **Input**: `AskQuestionRequest` with `question`, `chapterId=2`, `sectionId` (optional)
- **Output**: `AIBlockResponse` with placeholder message
- **Purpose**: Route Chapter 2 ask-question requests to runtime engine
- **TODO**: Call `run_ai_block("ask-question", request.model_dump())` where `request.model_dump()` includes `chapterId=2`

**ch2_explain(request)**:
- **Input**: `ExplainLike10Request` with `concept`, `chapterId=2`
- **Output**: `AIBlockResponse` with placeholder message
- **Purpose**: Route Chapter 2 explain-el10 requests to runtime engine
- **TODO**: Call `run_ai_block("explain-like-i-am-10", request.model_dump())` where `request.model_dump()` includes `chapterId=2`

**ch2_quiz(request)**:
- **Input**: `QuizRequest` with `chapterId=2`, `numQuestions`, `learningObjectives` (optional)
- **Output**: `AIBlockResponse` with placeholder message
- **Purpose**: Route Chapter 2 quiz requests to runtime engine
- **TODO**: Call `run_ai_block("interactive-quiz", request.model_dump())` where `request.model_dump()` includes `chapterId=2`

**ch2_diagram(request)**:
- **Input**: `DiagramRequest` with `diagramType`, `chapterId=2`, `concepts`
- **Output**: `AIBlockResponse` with placeholder message
- **Purpose**: Route Chapter 2 diagram requests to runtime engine
- **TODO**: Call `run_ai_block("generate-diagram", request.model_dump())` where `request.model_dump()` includes `chapterId=2`

**Dependencies**:
- Internal: `app.ai.runtime.engine` (for `run_ai_block`)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses existing request/response models from Feature 005
- Follows same endpoint pattern as Chapter 1 and Chapter 3
- Uses same routing logic

---

### 3.2 Runtime Engine Extensions

**File**: `backend/app/ai/runtime/engine.py`

**Purpose**: Extend runtime engine to route chapterId=2 calls to Chapter 2 subagents and RAG pipeline

**Current State**: Has Chapter 1 and Chapter 3 routing (from Feature 005 and Feature 030)

**Updates Required**:
- Add chapterId=2 routing logic with placeholder comments
- Add placeholder flow for:
  - Provider selection for Chapter 2
  - RAG invocation for Chapter 2 (call pipeline.py with chapter_id=2)
  - Subagent selection for Chapter 2
  - Formatting layer for Chapter 2
- NO business logic (only placeholders and TODOs)
- Ensure existing Chapter 1 and Chapter 3 routing remains unchanged

**Input/Output Schemas** (Text Description):

**run_ai_block(block_type, request_data)** (Extended):
- **Input**:
  - `block_type`: str - Type of AI block ("ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram")
  - `request_data`: Dict[str, Any] - Request payload with chapterId=2
- **Output**: Dict[str, Any] - Formatted response for frontend
- **Purpose**: Route Chapter 2 requests to appropriate subagents and RAG pipeline
- **TODO**: 
  - Check chapterId in request_data
  - If chapterId=2, route to Chapter 2 subagent
  - Load Chapter 2 RAG context via pipeline.py with chapter_id=2
  - Call Chapter 2 subagent with context
  - Format response

**Chapter 2 Routing Logic** (Placeholder):
```python
chapter_id = request_data.get("chapterId", 1)
if chapter_id == 2:
    # TODO: Route to Chapter 2 subagent
    # TODO: Call pipeline with chapter_id=2 for RAG context
    # TODO: Select provider for Chapter 2
    # TODO: Call appropriate Chapter 2 subagent
    # TODO: Format response
```

**Dependencies**:
- Internal: `app.ai.subagents.ch2_*`, `app.ai.rag.pipeline`, `app.ai.providers.*`, `app.ai.skills.*`
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same runtime engine structure from Feature 005
- Extends existing routing logic rather than creating new engine
- Uses same subagent, RAG, and LLM provider patterns

---

### 3.3 Subagent Stubs

**Files**: 
- `backend/app/ai/subagents/ch2_ask_agent.py`
- `backend/app/ai/subagents/ch2_explain_agent.py`
- `backend/app/ai/subagents/ch2_quiz_agent.py`
- `backend/app/ai/subagents/ch2_diagram_agent.py`

**Purpose**: Chapter 2-specific subagents for Mechanical Systems knowledge

**Status**: Create new files (do not exist yet)

**Structure** (each subagent):
- Class structure: `class <AgentName>: def run(self, input): ...`
- TODO comments: `# TODO: implement model prompting in future feature`
- Placeholder return values
- Expected input/output signatures in docstrings
- No logic (placeholder only)

**Input/Output Schemas** (Text Description):

**ch2_ask_agent.run(input)**:
- **Input**:
  - `input`: Dict[str, Any] - Request with `question`, `context` (RAG context from Chapter 2)
- **Output**: Dict[str, Any] - Answer with sources and confidence
- **Purpose**: Process Mechanical Systems question with Chapter 2 context
- **TODO**: Orchestrate provider + RAG, use Mechanical Systems concepts, return formatted answer

**ch2_explain_agent.run(input)**:
- **Input**:
  - `input`: Dict[str, Any] - Request with `concept`, `context` (RAG context from Chapter 2)
- **Output**: Dict[str, Any] - Explanation with examples and analogies
- **Purpose**: Generate Mechanical Systems explanation with Chapter 2 context
- **TODO**: Orchestrate provider + RAG, use age-appropriate analogies, return formatted explanation

**ch2_quiz_agent.run(input)**:
- **Input**:
  - `input`: Dict[str, Any] - Request with `chapter_id=2`, `num_questions`, `context` (RAG context from Chapter 2)
- **Output**: Dict[str, Any] - Quiz questions with answers
- **Purpose**: Generate Mechanical Systems quiz questions with Chapter 2 context
- **TODO**: Orchestrate provider + RAG, use Mechanical Systems learning objectives, return formatted quiz

**ch2_diagram_agent.run(input)**:
- **Input**:
  - `input`: Dict[str, Any] - Request with `diagram_type`, `concepts`, `context` (RAG context from Chapter 2)
- **Output**: Dict[str, Any] - Diagram with description
- **Purpose**: Generate Mechanical Systems diagram with Chapter 2 context
- **TODO**: Orchestrate provider + RAG, use Mechanical Systems concepts, return formatted diagram

**Dependencies**:
- Internal: `app.ai.providers.*`, `app.ai.rag.pipeline`, `app.ai.skills.*`
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same subagent structure as Chapter 1 and Chapter 3 (from Feature 005 and Feature 030)
- Follows same input/output patterns
- Uses same orchestration patterns (provider + RAG)

---

### 3.4 Skills Extensions

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Purpose**: Extend prompt builder skill to support Chapter 2 prompts

**Current State**: Has `build_prompt()` function with chapter-aware TODOs (from Feature 005 and Feature 030)

**Updates Required**:
- Add TODO comments for building prompts for Chapter 2 blocks
- Add placeholder functions for Chapter 2 prompt building (if needed)
- No implementation (TODO only)

**Input/Output Schemas** (Text Description):

**build_prompt(block_type, user_input, context, chapter_id)** (Extended):
- **Input**:
  - `block_type`: str - Type of AI block
  - `user_input`: str - User's question or concept
  - `context`: List[Dict[str, Any]] - Retrieved context chunks
  - `chapter_id`: int - Chapter identifier (1, 2, or 3)
- **Output**: str - Constructed prompt string for LLM
- **Purpose**: Build prompt with chapter-aware templates
- **TODO**: 
  - If chapter_id == 2, use Mechanical Systems prompt templates
  - Include Mechanical Systems concepts (forces, motion, energy, work, simple machines)
  - Format context with Mechanical Systems-specific instructions

**Dependencies**:
- Internal: None (standalone skill)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same prompt builder skill structure from Feature 005
- Extends existing function rather than creating new one
- Uses same prompt construction patterns

---

**File**: `backend/app/ai/skills/formatting_skill.py`

**Purpose**: Extend formatting skill to support Chapter 2 responses

**Current State**: Has formatting functions with chapter-aware TODOs (from Feature 005 and Feature 030)

**Updates Required**:
- Add TODO placeholders for quiz formatting + explanations for Chapter 2
- No implementation (TODO only)

**Input/Output Schemas** (Text Description):

**format_response(response, block_type, chapter_id)** (Extended):
- **Input**:
  - `response`: Dict[str, Any] - Raw LLM response
  - `block_type`: str - Type of AI block
  - `chapter_id`: int - Chapter identifier (1, 2, or 3)
- **Output**: Dict[str, Any] - Formatted response for frontend
- **Purpose**: Format response with chapter-aware structure
- **TODO**: 
  - If chapter_id == 2, format with Mechanical Systems structure
  - Format quiz responses for Chapter 2
  - Format explanations for Chapter 2

**Dependencies**:
- Internal: None (standalone skill)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same formatting skill structure from Feature 005
- Extends existing function rather than creating new one
- Uses same formatting patterns

---

### 3.5 Pipeline Connection

**File**: `backend/app/ai/rag/pipeline.py`

**Purpose**: Add routing for chapter_2

**Current State**: Has RAG pipeline functions (from Feature 005)

**Updates Required**:
- Add routing for chapter_2:
  - `if chapter_id == 2: load chapter_2_chunks`
- Add comments about retrieval steps
- No business logic (placeholder only)

**Input/Output Schemas** (Text Description):

**run_rag_pipeline(query, chapter_id, top_k)** (Extended):
- **Input**:
  - `query`: str - User query text
  - `chapter_id`: int - Chapter identifier (1, 2, or 3)
  - `top_k`: int - Number of chunks to retrieve (default: 5)
- **Output**: Dict[str, Any] - Context dictionary with chunks and embedding
- **Purpose**: Execute RAG pipeline for specified chapter and return context
- **TODO**: 
  - If chapter_id == 2, load Chapter 2 chunks
  - Embed query for Chapter 2
  - Search Chapter 2 collection
  - Return Chapter 2 context

**Dependencies**:
- Internal: `app.content.chapters.chapter_2_chunks` (for Chapter 2 chunks)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same RAG pipeline structure from Feature 005
- Extends existing function rather than creating new one
- Uses same RAG pipeline interface

---

## 4. Routing Architecture

### 4.1 API Endpoint Routing Table

| Endpoint | Block Type | Request Model | Calls |
|----------|------------|---------------|-------|
| `POST /ai/ch2/ask` | ask-question | AskQuestionRequest | `run_ai_block("ask-question", {..., chapterId: 2})` |
| `POST /ai/ch2/explain` | explain-like-i-am-10 | ExplainLike10Request | `run_ai_block("explain-like-i-am-10", {..., chapterId: 2})` |
| `POST /ai/ch2/quiz` | interactive-quiz | QuizRequest | `run_ai_block("interactive-quiz", {..., chapterId: 2})` |
| `POST /ai/ch2/diagram` | generate-diagram | DiagramRequest | `run_ai_block("generate-diagram", {..., chapterId: 2})` |

### 4.2 Runtime Engine Routing Table

| chapterId | Block Type | Subagent | RAG Pipeline |
|-----------|------------|----------|--------------|
| 2 | ask-question | ch2_ask_agent | pipeline.py (chapter_id=2) |
| 2 | explain-like-i-am-10 | ch2_explain_agent | pipeline.py (chapter_id=2) |
| 2 | interactive-quiz | ch2_quiz_agent | pipeline.py (chapter_id=2) |
| 2 | generate-diagram | ch2_diagram_agent | pipeline.py (chapter_id=2) |

---

## 5. Subagent Responsibilities Table

| Subagent | Input | Output | Responsibilities |
|----------|-------|--------|------------------|
| ch2_ask_agent | question, context | answer, sources, confidence | Answer questions about Mechanical Systems using Chapter 2 context |
| ch2_explain_agent | concept, context | explanation, examples, analogies | Explain Mechanical Systems concepts in simple terms using Chapter 2 context |
| ch2_quiz_agent | chapter_id, num_questions, context | questions, learning_objectives | Generate quiz questions about Mechanical Systems using Chapter 2 context |
| ch2_diagram_agent | diagram_type, concepts, context | diagram_url, metadata | Generate diagrams for Mechanical Systems concepts using Chapter 2 context |

---

## 6. Skills Integration Map

### Prompt Builder Skill

| Function | Chapter 2 Support | Status |
|----------|-------------------|--------|
| `build_ask_prompt_ch2()` | Build Mechanical Systems ask prompts | TODO |
| `build_explain_prompt_ch2()` | Build Mechanical Systems explain prompts | TODO |
| `build_quiz_prompt_ch2()` | Build Mechanical Systems quiz prompts | TODO |
| `build_diagram_prompt_ch2()` | Build Mechanical Systems diagram prompts | TODO |

### Formatting Skill

| Function | Chapter 2 Support | Status |
|----------|-------------------|--------|
| `format_ask_response_ch2()` | Format ask responses for Chapter 2 | TODO |
| `format_explain_response_ch2()` | Format explain responses for Chapter 2 | TODO |
| `format_quiz_response_ch2()` | Format quiz responses for Chapter 2 | TODO |
| `format_diagram_response_ch2()` | Format diagram responses for Chapter 2 | TODO |

---

## 7. RAG Retrieval Flow for Chapter 2

**Flow**: Runtime Engine → RAG Pipeline → Chapter 2 Chunks → Embedding → Qdrant Search → Context

1. **Runtime Engine**: Calls `run_rag_pipeline(query, chapter_id=2, top_k=5)`
2. **RAG Pipeline**: Routes to Chapter 2 handling:
   - `if chapter_id == 2: load chapter_2_chunks`
3. **Chapter 2 Chunks**: Load from `app.content.chapters.chapter_2_chunks`
4. **Embedding**: Generate embedding for query (chapter=2)
5. **Qdrant Search**: Search collection="chapter_2"
6. **Context**: Return context dictionary with chunks and embedding

---

## 8. API Contract Summary

**Endpoints**: 4 new endpoints for Chapter 2
- All endpoints follow same pattern as Chapter 1 and Chapter 3
- All endpoints call `run_ai_block()` with `chapterId=2`
- All endpoints return placeholder responses

**Request Models**: Reuse existing models from Feature 005
**Response Models**: Reuse existing models from Feature 005

---

## 9. File Outputs List

### Files to Create:
1. `backend/app/ai/subagents/ch2_ask_agent.py`
2. `backend/app/ai/subagents/ch2_explain_agent.py`
3. `backend/app/ai/subagents/ch2_quiz_agent.py`
4. `backend/app/ai/subagents/ch2_diagram_agent.py`
5. `specs/034-chapter-2-ai-blocks/contracts/ai-block-runtime.yaml` (already created in spec phase)

### Files to Update:
1. `backend/app/api/ai_blocks.py` (add 4 endpoints)
2. `backend/app/ai/runtime/engine.py` (add chapterId=2 routing)
3. `backend/app/ai/skills/prompt_builder_skill.py` (add Chapter 2 TODOs)
4. `backend/app/ai/skills/formatting_skill.py` (add Chapter 2 TODOs)
5. `backend/app/ai/rag/pipeline.py` (add Chapter 2 routing)

---

## 10. Validation & Error Prevention Steps

### Pre-Implementation Validation:
- [ ] Verify Chapter 2 content exists (Feature 033)
- [ ] Verify runtime engine structure exists (Feature 005)
- [ ] Verify Chapter 3 patterns exist (Feature 030) for reference

### During Implementation Validation:
- [ ] Verify all imports resolve without errors
- [ ] Verify all files are created at correct paths
- [ ] Verify all TODO comments are clear and actionable

### Post-Implementation Validation:
- [ ] Backend starts without errors
- [ ] All API endpoints are registered
- [ ] All subagent files exist with class structure
- [ ] All skills files updated with Chapter 2 TODOs
- [ ] RAG pipeline has Chapter 2 routing comments
- [ ] Contract file exists and documents runtime flow

---

## 11. Success Criteria

- ✅ All Chapter 2 AI routes exist and run without import errors
- ✅ Runtime engine handles chapter_id=2 paths with placeholder flow
- ✅ Subagents + skills updated with TODO blocks
- ✅ RAG pipeline aware of chapter_2
- ✅ Contract file exists and documents the runtime
- ✅ Backend starts successfully without errors
- ✅ All required files exist at specified paths

---

## 12. Dependencies + Risks

### Dependencies:
- Feature 001: Base Project Initialization
- Feature 033: Chapter 2 Content (MDX file and metadata)
- Feature 005: AI Runtime Engine (base structure)
- Feature 030: Chapter 3 AI Runtime (reference pattern)

### Risks:
1. **Risk**: Import errors if file paths are incorrect
   - **Mitigation**: Verify all paths match existing structure
2. **Risk**: Breaking existing Chapter 1 or Chapter 3 functionality
   - **Mitigation**: Ensure all changes are additive, no modifications to existing logic
3. **Risk**: Subagent naming conflicts with existing files
   - **Mitigation**: Use exact naming specified in requirements (ch2_ask_agent.py, etc.)

---

## Summary

This plan establishes the complete architecture for Chapter 2 AI block integration scaffolding. The implementation follows Chapter 3 patterns exactly, creates all necessary files with placeholders, and ensures consistency across chapters. All components are scaffolding only—no business logic is implemented.

**Estimated Implementation Time**: 1-2 hours (scaffolding only, no business logic)
**Complexity**: Low (scaffolding, following existing patterns)
**Dependencies**: Feature 001, Feature 033, Feature 005, Feature 030
**Out of Scope**: Actual AI logic, RAG implementation, LLM calls, response formatting logic

