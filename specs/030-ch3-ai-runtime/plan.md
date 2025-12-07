# Implementation Plan: Chapter 3 — AI Runtime Engine Integration

**Branch**: `030-ch3-ai-runtime` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/030-ch3-ai-runtime/spec.md`

## Summary

This feature connects Chapter 3's AI Blocks to the global AI Runtime Engine by creating scaffolding for API endpoint routing, runtime engine routing, subagents, skills extensions, and pipeline connection. The implementation establishes the architectural foundation for Chapter 3 runtime engine integration with API endpoints, Chapter 3-specific routing, subagents, chapter-aware skills, and pipeline integration. **No real AI logic is implemented**—only scaffolding, function signatures, TODO placeholders, and architectural blueprints to prepare for future AI implementation.

**Primary Deliverable**: Complete Chapter 3 runtime engine integration scaffolding (API endpoints, runtime routing, subagents, skills, pipeline connection, contract)
**Validation**: All files exist, imports resolve, backend starts, no runtime errors

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- No new runtime dependencies required (scaffolding only)
- Existing runtime engine, RAG pipeline, skills from Feature 005
- Existing Chapter 2 runtime patterns from Feature 017 or 020 (for reference)
- Chapter 3 RAG pipeline from Feature 029 (ch3_pipeline.py)

**Storage**: 
- No persistent storage (scaffolding only)
- Future: Qdrant for Chapter 3 vectors, Postgres for sessions

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
- MUST maintain compatibility with Feature 017/020 (Chapter 2 runtime must still work)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality
- MUST follow Chapter 2 AI runtime patterns exactly

**Scale/Scope**:
- 4 new API endpoints (Chapter 3 endpoints)
- 1 runtime engine file to update (add chapterId=3 routing)
- 4 subagent files to create (ch3_*)
- 2 skills files to update (add Chapter 3 TODOs)
- 1 pipeline file to update (ch3_pipeline.py integration)
- 1 contract file to create
- ~200-300 lines of scaffolding code (mostly signatures, TODOs, and comments)

---

## 1. Folder Structure

### 1.1 New Files

**Directory**: `backend/app/ai/subagents/`
- **Status**: Already exists (from Feature 005)
- **Files to Create**:
  - `ch3_ask_question_agent.py` (NEW - Chapter 3 ask question agent)
  - `ch3_explain_el10_agent.py` (NEW - Chapter 3 ELI10 agent)
  - `ch3_quiz_agent.py` (NEW - Chapter 3 quiz agent)
  - `ch3_diagram_agent.py` (NEW - Chapter 3 diagram agent)

### 1.2 Existing Directories (To Be Extended)

**Directory**: `backend/app/api/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `ai_blocks.py` (add 4 new Chapter 3 endpoints)

**Directory**: `backend/app/ai/runtime/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `engine.py` (extend with chapterId=3 routing)

**Directory**: `backend/app/ai/skills/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `prompt_builder_skill.py` (add Chapter 3 TODOs)
  - `retrieval_skill.py` (add Chapter 3 TODOs)

**Directory**: `backend/app/ai/rag/`
- **Status**: Already exists (from Feature 005)
- **Files to Update**:
  - `ch3_pipeline.py` (add placeholder call to engine pipeline)

**Directory**: `specs/030-ch3-ai-runtime/contracts/`
- **Status**: Already exists (from spec phase)
- **Files to Verify**:
  - `ch3-ai-runtime.yaml` (verify exists from spec phase)

---

## 2. Runtime Flow Design

### 2.1 Chapter 3 Runtime Flow

**Flow**: CH3 Query → API Endpoint → Runtime Engine → RAG Pipeline → Subagent → LLM Provider → Response

```
Frontend Component (Chapter 3)
    │
    ▼
API Endpoint (ai_blocks.py) - Chapter 3 endpoints
    ├─► POST /ai/ch3/ask-question
    ├─► POST /ai/ch3/explain-el10
    ├─► POST /ai/ch3/quiz
    └─► POST /ai/ch3/diagram
    │
    ▼
Runtime Engine (engine.py)
    │
    ├─► Router: Determine block type → Select Chapter 3 subagent
    │   ├─► If chapterId=3:
    │   │   ├─► Route to ch3_ask_question_agent
    │   │   ├─► Route to ch3_explain_el10_agent
    │   │   ├─► Route to ch3_quiz_agent
    │   │   └─► Route to ch3_diagram_agent
    │
    ├─► RAG Pipeline (ch3_pipeline.py)
    │   ├─► Load Chapter 3 chunks (chapter_3_chunks.py)
    │   ├─► Embed user query (embedding_client.py with chapter=3)
    │   ├─► Qdrant similarity search (collection="chapter3")
    │   └─► Construct retrieval context
    │
    ├─► Skills System (chapter-aware)
    │   ├─► Retrieval Skill (retrieval_skill.py) - Chapter 3 context
    │   ├─► Prompt Builder Skill (prompt_builder_skill.py) - Physical AI prompts
    │   └─► Formatting Skill (formatting_skill.py) - Chapter 3 formatting
    │
    ├─► Chapter 3 Subagent
    │   ├─► ch3_ask_question_agent.py
    │   ├─► ch3_explain_el10_agent.py
    │   ├─► ch3_quiz_agent.py
    │   └─► ch3_diagram_agent.py
    │   └─► Uses skills + RAG context → Generates Physical AI response
    │
    ├─► LLM Provider (base_llm.py → openai_provider.py | gemini_provider.py)
    │   └─► Generates response with Physical AI context
    │
    └─► Response Formatting → Return to API → Frontend
```

### 2.2 Data Flow

1. **Request**: Frontend sends request with chapterId=3 → API endpoint receives
2. **Routing**: Runtime engine identifies chapterId=3 → routes to Chapter 3 subagent
3. **RAG Pipeline**: RAG pipeline retrieves Chapter 3 context from Qdrant (via ch3_pipeline.py)
4. **Embedding**: Embedding client generates embeddings with chapter=3 support
5. **Skills**: Skills assemble Physical AI context + user input into prompts
6. **Subagent**: Chapter 3 subagent processes with Physical AI context
7. **LLM**: LLM provider generates response with Physical AI context
8. **Formatting**: Skills format response for frontend
9. **Response**: API returns formatted response → Frontend displays

---

## 3. Module-Level Design

### 3.1 API Endpoint Routing

**File**: `backend/app/api/ai_blocks.py`

**Purpose**: Add 4 new endpoints for Chapter 3

**Current State**: Has existing endpoints for Chapter 1 and Chapter 2

**Updates Required**:
- Add 4 new endpoints:
  - `POST /ai/ch3/ask-question`
  - `POST /ai/ch3/explain-el10`
  - `POST /ai/ch3/quiz`
  - `POST /ai/ch3/diagram`
- Each endpoint should call: `run_ai_block(block_type="...", chapter=3, payload=...)`
- No logic. Only call + placeholder.

**Input/Output Schemas** (Text Description):

**ch3_ask_question(request)**:
- **Input**: `AskQuestionRequest` with `question`, `chapterId=3`, `sectionId` (optional)
- **Output**: `AIBlockResponse` with placeholder message
- **Purpose**: Route Chapter 3 ask-question requests to runtime engine
- **TODO**: Call `run_ai_block("ask-question", request.model_dump())`

**ch3_explain_el10(request)**:
- **Input**: `ExplainLike10Request` with `concept`, `chapterId=3`
- **Output**: `AIBlockResponse` with placeholder message
- **Purpose**: Route Chapter 3 explain-el10 requests to runtime engine
- **TODO**: Call `run_ai_block("explain-like-10", request.model_dump())`

**ch3_quiz(request)**:
- **Input**: `QuizRequest` with `chapterId=3`, `numQuestions`, `learningObjectives` (optional)
- **Output**: `AIBlockResponse` with placeholder message
- **Purpose**: Route Chapter 3 quiz requests to runtime engine
- **TODO**: Call `run_ai_block("quiz", request.model_dump())`

**ch3_diagram(request)**:
- **Input**: `DiagramRequest` with `diagramType`, `chapterId=3`, `concepts`
- **Output**: `AIBlockResponse` with placeholder message
- **Purpose**: Route Chapter 3 diagram requests to runtime engine
- **TODO**: Call `run_ai_block("diagram", request.model_dump())`

**Dependencies**:
- Internal: `app.ai.runtime.engine` (for `run_ai_block`)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses existing request/response models from Feature 005
- Follows same endpoint pattern as Chapter 1 and Chapter 2
- Uses same routing logic

---

### 3.2 Runtime Engine Extensions

**File**: `backend/app/ai/runtime/engine.py`

**Purpose**: Extend runtime engine to route chapterId=3 calls to Chapter 3 subagents and RAG pipeline

**Current State**: Has Chapter 1 and Chapter 2 routing (from Feature 005 and Feature 017/020)

**Updates Required**:
- Add chapterId=3 routing logic with placeholder comments
- Add placeholder flow for:
  - Provider selection for Chapter 3
  - RAG invocation for Chapter 3 (call ch3_pipeline.py)
  - Subagent selection for Chapter 3
  - Formatting layer for Chapter 3
- NO business logic (only placeholders and TODOs)
- Ensure existing Chapter 1 and Chapter 2 routing remains unchanged

**Input/Output Schemas** (Text Description):

**run_ai_block(block_type, request_data)** (Extended):
- **Input**:
  - `block_type`: str - Type of AI block ("ask-question", "explain-like-10", "quiz", "diagram")
  - `request_data`: Dict[str, Any] - Request payload with chapterId=3
- **Output**: Dict[str, Any] - Formatted response for frontend
- **Purpose**: Route Chapter 3 requests to appropriate subagents and RAG pipeline
- **TODO**: 
  - Check chapterId in request_data
  - If chapterId=3, route to Chapter 3 subagent
  - Load Chapter 3 RAG context via ch3_pipeline.py
  - Call Chapter 3 subagent with context
  - Format response

**Chapter 3 Routing Logic** (Placeholder):
```python
chapter_id = request_data.get("chapterId", 1)
if chapter_id == 3:
    # TODO: Route to Chapter 3 subagent
    # TODO: Call ch3_pipeline.run_ch3_rag_pipeline() for RAG context
    # TODO: Select provider for Chapter 3
    # TODO: Call appropriate Chapter 3 subagent
    # TODO: Format response
```

**Dependencies**:
- Internal: `app.ai.subagents.ch3_*`, `app.ai.rag.ch3_pipeline`, `app.ai.providers.*`, `app.ai.skills.*`
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same runtime engine structure from Feature 005
- Extends existing routing logic rather than creating new engine
- Uses same subagent, RAG, and LLM provider patterns

---

### 3.3 Subagent Stubs

**Files**: 
- `backend/app/ai/subagents/ch3_ask_question_agent.py`
- `backend/app/ai/subagents/ch3_explain_el10_agent.py`
- `backend/app/ai/subagents/ch3_quiz_agent.py`
- `backend/app/ai/subagents/ch3_diagram_agent.py`

**Purpose**: Chapter 3-specific subagents for Physical AI knowledge

**Status**: Create new files (do not exist yet)

**Structure** (each subagent):
- Module docstring
- Expected input/output signatures
- Function stub with TODOs only
- Placeholder return values
- No logic (placeholder only)

**Input/Output Schemas** (Text Description):

**ch3_ask_question_agent(question, context)**:
- **Input**:
  - `question`: str - User question about Physical AI
  - `context`: Dict[str, Any] - RAG context from Chapter 3
- **Output**: Dict[str, Any] - Answer with sources and confidence
- **Purpose**: Process Physical AI question with Chapter 3 context
- **TODO**: Orchestrate provider + RAG, use Physical AI concepts, return formatted answer

**ch3_explain_el10_agent(concept, context)**:
- **Input**:
  - `concept`: str - Physical AI concept to explain
  - `context`: Dict[str, Any] - RAG context from Chapter 3
- **Output**: Dict[str, Any] - Explanation with examples and analogies
- **Purpose**: Generate Physical AI explanation with Chapter 3 context
- **TODO**: Orchestrate provider + RAG, use age-appropriate analogies, return formatted explanation

**ch3_quiz_agent(chapter_id, num_questions, learning_objectives, context)**:
- **Input**:
  - `chapter_id`: int - Chapter identifier (3)
  - `num_questions`: int - Number of questions to generate
  - `learning_objectives`: Optional[List[str]] - Learning objectives to cover
  - `context`: Dict[str, Any] - RAG context from Chapter 3
- **Output**: Dict[str, Any] - Quiz questions with answers
- **Purpose**: Generate Physical AI quiz questions with Chapter 3 context
- **TODO**: Orchestrate provider + RAG, use Physical AI learning objectives, return formatted quiz

**ch3_diagram_agent(diagram_type, concepts, context)**:
- **Input**:
  - `diagram_type`: str - Type of diagram to generate
  - `concepts`: List[str] - Physical AI concepts to include
  - `context`: Dict[str, Any] - RAG context from Chapter 3
- **Output**: Dict[str, Any] - Diagram with description
- **Purpose**: Generate Physical AI diagram with Chapter 3 context
- **TODO**: Orchestrate provider + RAG, use Physical AI concepts, return formatted diagram

**Dependencies**:
- Internal: `app.ai.providers.*`, `app.ai.rag.ch3_pipeline`, `app.ai.skills.*`
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same subagent structure as Chapter 1 and Chapter 2 (from Feature 005 and Feature 017/020)
- Follows same input/output patterns
- Uses same orchestration patterns (provider + RAG)

---

### 3.4 Skills Extensions

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Purpose**: Extend prompt builder skill to support Chapter 3 prompts

**Current State**: Has `build_prompt()` function with chapter-aware TODOs (from Feature 005 and Feature 017/020)

**Updates Required**:
- Add TODO comments for building prompts for Chapter 3 blocks
- Add placeholder functions for Chapter 3 prompt building (if needed)
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
  - If chapter_id == 3, use Physical AI prompt templates
  - Include Physical AI concepts (perception, sensors, vision, signal processing)
  - Format context with Physical AI-specific instructions

**Dependencies**:
- Internal: None (standalone skill)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same prompt builder skill structure from Feature 005
- Extends existing function rather than creating new one
- Uses same prompt construction patterns

---

**File**: `backend/app/ai/skills/retrieval_skill.py`

**Purpose**: Extend retrieval skill to support Chapter 3 chunks

**Current State**: Has `retrieve_content()` function with chapter-aware TODOs (from Feature 005 and Feature 017/020)

**Updates Required**:
- Add TODO comments for integrating Chapter 3 chunks
- Add placeholder routing for chapterId=3
- No implementation (TODO only)

**Input/Output Schemas** (Text Description):

**retrieve_content(query, chapter_id, top_k)** (Extended):
- **Input**:
  - `query`: str - Search query
  - `chapter_id`: int - Chapter identifier (1, 2, or 3)
  - `top_k`: int - Number of results (default: 5)
- **Output**: List[Dict[str, Any]] - Retrieved content chunks
- **Purpose**: Retrieve content with chapter-aware collection selection
- **TODO**: 
  - If chapter_id == 3, use Chapter 3 RAG pipeline
  - Call ch3_pipeline.run_ch3_rag_pipeline() for Chapter 3
  - Return Chapter 3 chunks with Physical AI metadata

**Dependencies**:
- Internal: `app.ai.rag.ch3_pipeline` (for Chapter 3 RAG), `app.ai.rag.pipeline` (for Chapter 1/2 RAG)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same retrieval skill structure from Feature 005
- Extends existing function rather than creating new one
- Uses same RAG pipeline interface

---

### 3.5 Pipeline Connection

**File**: `backend/app/ai/rag/ch3_pipeline.py`

**Purpose**: Add placeholder call to engine pipeline

**Current State**: Has `run_ch3_rag_pipeline()` function from Feature 029

**Updates Required**:
- Add placeholder call to engine pipeline
- Add TODO comments for runtime engine integration
- No logic added (placeholder only)

**Input/Output Schemas** (Text Description):

**run_ch3_rag_pipeline(query, top_k)** (Extended):
- **Input**:
  - `query`: str - User query text
  - `top_k`: int - Number of chunks to retrieve (default: 5)
- **Output**: Dict[str, Any] - Context dictionary with chunks and embedding
- **Purpose**: Execute RAG pipeline for Chapter 3 and return context
- **TODO**: 
  - Runtime engine integration
  - Called from engine.py when chapterId=3
  - Return context for subagents

**Dependencies**:
- Internal: `app.ai.runtime.engine` (for future integration)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Reuses same pipeline structure from Feature 029
- Follows same RAG pipeline patterns as Chapter 1 and Chapter 2
- Uses same context structure

---

## 4. Integration Points

### 4.1 Feature 005 (AI Runtime Engine)

**Integration**: Extends existing runtime engine structure
- Reuses runtime engine, subagents, skills patterns
- Extends existing functions rather than creating new ones
- Maintains compatibility with Chapter 1 functionality

### 4.2 Feature 017 or 020 (Chapter 2 AI Runtime)

**Integration**: Follows Chapter 2 patterns exactly
- Uses same routing patterns
- Uses same subagent structure
- Uses same skills extension approach

### 4.3 Feature 028 (Chapter 3 AI Blocks Integration)

**Integration**: Uses Chapter 3 MDX and metadata
- Verifies Chapter 3 MDX exists
- Uses Chapter 3 metadata structure
- Connects to Chapter 3 AI blocks

### 4.4 Feature 029 (Chapter 3 RAG Prep)

**Integration**: Uses ch3_pipeline.py from Feature 029
- Verifies ch3_pipeline.py exists
- Uses `run_ch3_rag_pipeline()` function
- Extends pipeline with runtime engine integration

---

## 5. File Creation Diagram

### 5.1 Files to Create

```
backend/app/ai/subagents/
├── ch3_ask_question_agent.py      # NEW - Chapter 3 ask question agent
├── ch3_explain_el10_agent.py      # NEW - Chapter 3 ELI10 agent
├── ch3_quiz_agent.py              # NEW - Chapter 3 quiz agent
└── ch3_diagram_agent.py           # NEW - Chapter 3 diagram agent
```

### 5.2 Files to Update

```
backend/app/api/
└── ai_blocks.py                   # UPDATE - Add 4 new Chapter 3 endpoints

backend/app/ai/runtime/
└── engine.py                      # UPDATE - Add chapterId=3 routing

backend/app/ai/skills/
├── prompt_builder_skill.py       # UPDATE - Add Chapter 3 TODOs
└── retrieval_skill.py            # UPDATE - Add Chapter 3 TODOs

backend/app/ai/rag/
└── ch3_pipeline.py               # UPDATE - Add placeholder call to engine
```

### 5.3 Files to Verify

```
specs/030-ch3-ai-runtime/contracts/
└── ch3-ai-runtime.yaml           # VERIFY - Exists from spec phase
```

---

## 6. Risks

### 6.1 Risk Assessment

#### Risk 1: No Real Logic Allowed at This Stage
**Severity**: Low
**Probability**: Low
**Mitigation**: Clear TODO comments, placeholder returns, validation checks

#### Risk 2: Breaking Existing Functionality
**Severity**: Medium
**Probability**: Low
**Mitigation**: Careful extension of existing code, no modification of Chapter 1/2 logic

#### Risk 3: Import Errors
**Severity**: Medium
**Probability**: Low
**Mitigation**: Validate all imports resolve, test backend startup

#### Risk 4: Pattern Inconsistency with Chapter 2
**Severity**: Low
**Probability**: Low
**Mitigation**: Follow Chapter 2 patterns exactly, review consistency

### 6.2 Mitigation Strategies

1. **Validation**: Test all imports and backend startup after each file update
2. **Pattern Consistency**: Follow Chapter 2 AI runtime patterns exactly
3. **Documentation**: Comprehensive TODO comments explain future implementation
4. **Testing**: Manual validation of file existence, imports, backend startup

---

## 7. Validation Steps

### 7.1 File Existence Validation

```bash
# Check all files exist
ls backend/app/api/ai_blocks.py
ls backend/app/ai/runtime/engine.py
ls backend/app/ai/subagents/ch3_ask_question_agent.py
ls backend/app/ai/subagents/ch3_explain_el10_agent.py
ls backend/app/ai/subagents/ch3_quiz_agent.py
ls backend/app/ai/subagents/ch3_diagram_agent.py
ls backend/app/ai/skills/prompt_builder_skill.py
ls backend/app/ai/skills/retrieval_skill.py
ls backend/app/ai/rag/ch3_pipeline.py
ls specs/030-ch3-ai-runtime/contracts/ch3-ai-runtime.yaml
```

### 7.2 Import Resolution Validation

```bash
cd backend
python -c "from app.api.ai_blocks import router; print('API imports OK')"
python -c "from app.ai.runtime.engine import run_ai_block; print('Engine imports OK')"
python -c "from app.ai.subagents.ch3_ask_question_agent import ch3_ask_question_agent; print('Subagents import OK')"
python -c "from app.ai.skills.prompt_builder_skill import build_prompt; print('Skills import OK')"
python -c "from app.ai.rag.ch3_pipeline import run_ch3_rag_pipeline; print('Pipeline imports OK')"
```

### 7.3 Backend Startup Validation

```bash
cd backend
python -c "from app.main import app; print('Backend startup OK')"
```

### 7.4 Endpoint Validation

```bash
# Check endpoints are registered (manual verification)
# All 4 Chapter 3 endpoints should be accessible
```

---

## 8. Success Criteria

- ✅ All 4 Chapter 3 API endpoints exist and route correctly
- ✅ Runtime engine handles Chapter 3 stub routing
- ✅ All 4 Chapter 3 subagents created with correct signatures
- ✅ Skills extended with Chapter 3 TODOs
- ✅ Pipeline connection added to ch3_pipeline.py
- ✅ Contract file exists and documents structure
- ✅ No actual AI or RAG logic implemented
- ✅ Backend runs without errors
- ✅ All files created at exact paths
- ✅ All imports resolve correctly

---

## 9. Next Steps

1. Run `/sp.tasks` to generate implementation tasks
2. Review tasks.md for atomic task breakdown
3. Run `/sp.implement` to implement scaffolding
4. Validate all files exist and imports resolve
5. Test backend startup

