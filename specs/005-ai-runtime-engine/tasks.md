# Tasks: AI Runtime Engine for Chapter 1 — LLM, RAG, ChatKit Integration

**Feature**: 005-ai-runtime-engine | **Branch**: `005-ai-runtime-engine` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating AI runtime infrastructure scaffolding (providers, RAG pipeline, subagents, skills, ChatKit, runtime engine). All tasks are scaffolding only—no real AI logic implementation.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category**: SETUP (Initial setup), MODULE (Module creation), CONNECT (Integration), VALIDATE (Validation), DOCS (Documentation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prepare directory structure before creating modules.

- [ ] [T001] [P1] [SETUP] Verify Feature 001 (Base Project) is complete: Backend structure exists, FastAPI setup functional, `backend/app/` directory structure in place
- [ ] [T002] [P1] [SETUP] Verify Feature 004 (Chapter 1 Interactive Blocks) is complete: `backend/app/api/ai_blocks.py` exists with 4 endpoints (ask-question, explain-like-10, quiz, diagram)
- [ ] [T003] [P1] [SETUP] Create directory structure: `backend/app/ai/` and all subdirectories (providers, embeddings, rag, runtime, subagents, skills, chatkit)
- [ ] [T004] [P1] [SETUP] Verify backend starts successfully: Run `cd backend && uvicorn app.main:app` to confirm no errors before adding new modules

**Success Criteria**:
- All prerequisite features complete
- Directory structure ready
- Backend starts without errors

**Dependencies**: Feature 001 (Base Project) and Feature 004 (Interactive Blocks) must be complete

---

## Phase 1: Providers Module Tasks

**Purpose**: Create LLM provider abstraction layer with base interface and provider scaffolds.

### Base LLM Provider

- [ ] [T005] [P1] [MODULE] Create `backend/app/ai/providers/__init__.py` with package initialization
- [ ] [T006] [P1] [MODULE] Create `backend/app/ai/providers/base_llm.py` with:
  - Import statements: `from abc import ABC, abstractmethod`, `from typing import Optional, List, Dict, Any`
  - Abstract base class `BaseLLMProvider(ABC)` with abstract method `async def generate(prompt: str, system: Optional[str] = None, messages: Optional[List[Dict[str, str]]] = None, temperature: float = 0.7) -> Dict[str, Any]`
  - Docstring explaining interface contract
  - TODO comment: `# TODO: Implement in provider subclasses`

### OpenAI Provider

- [ ] [T007] [P1] [MODULE] Create `backend/app/ai/providers/openai_provider.py` with:
  - Import: `from app.ai.providers.base_llm import BaseLLMProvider`
  - Class `OpenAIProvider(BaseLLMProvider)` implementing base interface
  - Method `async def generate(...)` with TODO placeholder: `# TODO: Implement OpenAI API calls using openai library`
  - Placeholder return: `return {"text": "placeholder", "metadata": {}}`
  - Docstring explaining OpenAI-specific implementation

### Gemini Provider

- [ ] [T008] [P1] [MODULE] Create `backend/app/ai/providers/gemini_provider.py` with:
  - Import: `from app.ai.providers.base_llm import BaseLLMProvider`
  - Class `GeminiProvider(BaseLLMProvider)` implementing base interface
  - Method `async def generate(...)` with TODO placeholder: `# TODO: Implement Gemini API calls using google-generativeai library`
  - Placeholder return: `return {"text": "placeholder", "metadata": {}}`
  - Docstring explaining Gemini-specific implementation

**Acceptance Test**: All provider files exist, imports resolve, backend starts without errors

---

## Phase 2: Embeddings Module Tasks

**Purpose**: Create embedding client for text-to-vector conversion.

- [ ] [T009] [P1] [MODULE] Create `backend/app/ai/embeddings/__init__.py` with package initialization
- [ ] [T010] [P1] [MODULE] Create `backend/app/ai/embeddings/embedding_client.py` with:
  - Import statements: `from typing import List`
  - Function `def generate_embedding(text: str) -> List[float]` with:
    - Type hints for parameters and return value
    - Docstring: "Generate embedding vector for text. TODO: Implement using configured embedding model"
    - TODO placeholder: `# TODO: Implement embedding generation using configured model`
    - Placeholder return: `return []` (empty list)
  - Function `def batch_embed(chunks: List[str]) -> List[List[float]]` with:
    - Type hints for parameters and return value
    - Docstring: "Generate embeddings for multiple text chunks. TODO: Implement batch processing"
    - TODO placeholder: `# TODO: Implement batch embedding generation`
    - Placeholder return: `return []` (empty list)

**Acceptance Test**: Embedding client file exists, function signatures correct, imports resolve

---

## Phase 3: RAG Infrastructure Tasks

**Purpose**: Create RAG pipeline and Qdrant store scaffolding.

### Qdrant Store

- [ ] [T011] [P1] [MODULE] Create `backend/app/ai/rag/__init__.py` with package initialization
- [ ] [T012] [P1] [MODULE] Create `backend/app/ai/rag/qdrant_store.py` with:
  - Import statements: `from typing import List, Dict, Any`
  - Function `def create_collection(collection_name: str) -> bool` with:
    - Type hints and docstring
    - TODO placeholder: `# TODO: Implement Qdrant collection creation`
    - Placeholder return: `return False`
  - Function `def upsert_vectors(collection_name: str, vectors: List[Dict[str, Any]]) -> bool` with:
    - Type hints and docstring explaining vector document structure
    - TODO placeholder: `# TODO: Implement vector upsert operation`
    - Placeholder return: `return False`
  - Function `def similarity_search(collection_name: str, query: str, top_k: int = 5) -> List[Dict[str, Any]]` with:
    - Type hints and docstring explaining return structure
    - TODO placeholder: `# TODO: Implement similarity search operation`
    - Placeholder return: `return []` (empty list)

### RAG Pipeline

- [ ] [T013] [P1] [MODULE] Create `backend/app/ai/rag/pipeline.py` with:
  - Import statements: `from typing import Dict, Any`
  - Function `async def run_rag_pipeline(query: str, chapter_id: int, top_k: int = 5) -> Dict[str, Any]` with:
    - Type hints for all parameters and return value
    - Docstring explaining RAG pipeline purpose
    - Step-by-step TODO comments:
      - `# Step 1: Retrieve chapter chunks (TODO)`
      - `# Step 2: Embed user query (TODO)`
      - `# Step 3: Perform Qdrant search (TODO)`
      - `# Step 4: Construct retrieval context (TODO)`
      - `# Step 5: Pass into provider LLM (TODO)`
    - Placeholder return: `return {"context": "", "chunks": [], "query_embedding": []}`

**Acceptance Test**: RAG files exist, function signatures correct, imports resolve

---

## Phase 4: Knowledge Source Tasks

**Purpose**: Create chapter chunks module for RAG retrieval.

- [ ] [T014] [P1] [MODULE] Create `backend/app/content/chapters/chapter_1_chunks.py` with:
  - Import statements: `from typing import List, Dict, Any`
  - Function `def get_chapter_chunks(chapter_id: int = 1) -> List[Dict[str, Any]]` with:
    - Type hints and docstring: "Return list of text chunks from Chapter 1 with metadata. TODO: Implement chunking from Chapter 1 MDX content"
    - TODO placeholder: `# TODO: Load Chapter 1 content, chunk by section/paragraph, return with metadata`
    - Placeholder return: `return []` (empty list)
  - Docstring explaining future chunking strategy (by section, by paragraph, semantic)

**Acceptance Test**: Chapter chunks file exists, function signature correct, imports resolve

---

## Phase 5: Runtime Engine Tasks

**Purpose**: Create unified runtime engine entry point.

- [ ] [T015] [P1] [MODULE] Create `backend/app/ai/runtime/__init__.py` with package initialization
- [ ] [T016] [P1] [MODULE] Create `backend/app/ai/runtime/engine.py` with:
  - Import statements: `from typing import Dict, Any`
  - Function `async def run_ai_block(block_type: str, request_data: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints for all parameters and return value
    - Docstring explaining unified runtime entry point
    - Flow comments (all TODO):
      - `# Step 1: Router - Determine which subagent to use (TODO)`
      - `# Step 2: RAG - Retrieve relevant context (TODO)`
      - `# Step 3: LLM Selection - Choose provider based on config (TODO)`
      - `# Step 4: Subagent - Call appropriate subagent (TODO)`
      - `# Step 5: Response Formatting - Format output for frontend (TODO)`
    - Placeholder return: `return {"message": "placeholder", "data": {}}`
  - Subagent mapping dictionary (placeholder): `SUBAGENT_MAP = {"ask-question": None, ...}` with TODO comment

**Acceptance Test**: Runtime engine file exists, function signature correct, imports resolve

---

## Phase 6: Subagent Tasks

**Purpose**: Create specialized agent scaffolds for each AI block type.

### Ask Question Agent

- [ ] [T017] [P1] [MODULE] Create `backend/app/ai/subagents/__init__.py` with package initialization
- [ ] [T018] [P1] [MODULE] Create `backend/app/ai/subagents/ask_question_agent.py` with:
  - Import statements: `from typing import Dict, Any`
  - Function `async def ask_question_agent(question: str, context: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints and docstring explaining expected input/output
    - Expected input documented: `question: str`, `context: Dict[str, Any]`
    - Expected output documented: `{answer: str, sources: List[str], confidence: float}`
    - TODO blueprint: `# TODO: Implement question-answering logic using skills + RAG + LLM`
    - Placeholder return: `return {"answer": "placeholder", "sources": [], "confidence": 0.0}`

### Explain ELI10 Agent

- [ ] [T019] [P1] [MODULE] Create `backend/app/ai/subagents/explain_el10_agent.py` with:
  - Import statements: `from typing import Dict, Any`
  - Function `async def explain_el10_agent(concept: str, context: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints and docstring
    - Expected input/output documented
    - TODO blueprint: `# TODO: Implement ELI10 explanation logic`
    - Placeholder return: `return {"explanation": "placeholder", "examples": [], "analogies": []}`

### Quiz Agent

- [ ] [T020] [P1] [MODULE] Create `backend/app/ai/subagents/quiz_agent.py` with:
  - Import statements: `from typing import Dict, Any, List`
  - Function `async def quiz_agent(chapter_id: int, num_questions: int, context: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints and docstring
    - Expected input/output documented
    - TODO blueprint: `# TODO: Implement quiz generation logic`
    - Placeholder return: `return {"questions": [], "learning_objectives": []}`

### Diagram Agent

- [ ] [T021] [P1] [MODULE] Create `backend/app/ai/subagents/diagram_agent.py` with:
  - Import statements: `from typing import Dict, Any, List`
  - Function `async def diagram_agent(diagram_type: str, concepts: List[str], context: Dict[str, Any]) -> Dict[str, Any]` with:
    - Type hints and docstring
    - Expected input/output documented
    - TODO blueprint: `# TODO: Implement diagram generation logic`
    - Placeholder return: `return {"diagram_url": "", "metadata": {}}`

**Acceptance Test**: All 4 subagent files exist, function signatures correct, imports resolve

---

## Phase 7: Skills Tasks

**Purpose**: Create reusable skill scaffolds.

### Retrieval Skill

- [ ] [T022] [P1] [MODULE] Create `backend/app/ai/skills/__init__.py` with package initialization
- [ ] [T023] [P1] [MODULE] Create `backend/app/ai/skills/retrieval_skill.py` with:
  - Import statements: `from typing import List, Dict, Any`
  - Function `async def retrieve_content(query: str, chapter_id: int, top_k: int = 5) -> List[Dict[str, Any]]` with:
    - Type hints and docstring
    - Expected input/output documented
    - TODO blueprint: `# TODO: Implement content retrieval logic`
    - Placeholder return: `return []`

### Formatting Skill

- [ ] [T024] [P1] [MODULE] Create `backend/app/ai/skills/formatting_skill.py` with:
  - Import statements: `from typing import Dict, Any`
  - Function `def format_response(raw_response: Dict[str, Any], block_type: str) -> Dict[str, Any]` with:
    - Type hints and docstring
    - Expected input/output documented
    - TODO blueprint: `# TODO: Implement response formatting logic`
    - Placeholder return: `return {}`

### Prompt Builder Skill

- [ ] [T025] [P1] [MODULE] Create `backend/app/ai/skills/prompt_builder_skill.py` with:
  - Import statements: `from typing import List, Dict, Any`
  - Function `def build_prompt(block_type: str, user_input: str, context: List[Dict[str, Any]]) -> str` with:
    - Type hints and docstring
    - Expected input/output documented
    - TODO blueprint: `# TODO: Implement prompt building logic`
    - Placeholder return: `return ""`

**Acceptance Test**: All 3 skill files exist, function signatures correct, imports resolve

---

## Phase 8: ChatKit Tasks

**Purpose**: Create ChatKit integration scaffolds.

### Session Manager

- [ ] [T026] [P1] [MODULE] Create `backend/app/ai/chatkit/__init__.py` with package initialization
- [ ] [T027] [P1] [MODULE] Create `backend/app/ai/chatkit/session_manager.py` with:
  - Import statements: `from typing import Dict, Any, List`
  - Function `def create_session(user_id: str) -> str` with:
    - Type hints and docstring: "Create new chat session. TODO: Implement session creation"
    - TODO placeholder: `# TODO: Implement session creation, return session_id`
    - Placeholder return: `return ""`
  - Function `def append_message(session_id: str, message: Dict[str, Any]) -> bool` with:
    - Type hints and docstring: "Append message to session history. TODO: Implement message appending"
    - TODO placeholder: `# TODO: Implement message appending`
    - Placeholder return: `return False`
  - Function `def get_history(session_id: str) -> List[Dict[str, Any]]` with:
    - Type hints and docstring: "Retrieve session message history. TODO: Implement history retrieval"
    - TODO placeholder: `# TODO: Implement history retrieval`
    - Placeholder return: `return []`

### Tools

- [ ] [T028] [P1] [MODULE] Create `backend/app/ai/chatkit/tools.py` with:
  - Documentation comments explaining tools needed later:
    - `# diagram_tool: Generate visual diagrams`
    - `# quiz_tool: Generate interactive quizzes`
    - `# explanation_tool: Generate simplified explanations`
  - TODO placeholders: `# TODO: Implement tool definitions when ChatKit integrated`
  - Tool structure documentation (input/output contracts)

**Acceptance Test**: ChatKit files exist, function signatures correct, imports resolve

---

## Phase 9: Config & Environment Tasks

**Purpose**: Update configuration files with AI runtime settings.

### Settings.py Updates

- [ ] [T029] [P1] [CONNECT] Update `backend/app/config/settings.py`:
  - Add to Settings class:
    - `ai_provider: str = "openai"` with docstring: "AI provider selection (openai, gemini, deepseek)"
    - `qdrant_collection_ch1: Optional[str] = None` with docstring: "Qdrant collection name for Chapter 1"
    - `embedding_model: Optional[str] = None` with docstring: "Embedding model identifier (e.g., text-embedding-3-small)"
    - `llm_model: Optional[str] = None` with docstring: "LLM model identifier (e.g., gpt-4o, gemini-pro)"
  - Verify no syntax errors: Run `python -m py_compile backend/app/config/settings.py`

### .env.example Updates

- [ ] [T030] [P1] [CONNECT] Update `.env.example`:
  - Add section: `# AI Runtime Engine Configuration`
  - Add `AI_PROVIDER=openai` with comment: `# Options: openai, gemini, deepseek`
  - Add `QDRANT_COLLECTION_CH1=chapter_1_content` with comment: `# Qdrant collection name for Chapter 1`
  - Add `EMBEDDING_MODEL=text-embedding-3-small` with comment: `# Embedding model identifier`
  - Add `LLM_MODEL=gpt-4o` with comment: `# LLM model identifier (e.g., gpt-4o, gemini-pro)`

**Acceptance Test**: Settings.py includes all new variables, .env.example updated, backend reads config without errors

---

## Phase 10: API Layer Integration Tasks

**Purpose**: Update API endpoints to route through runtime engine.

- [ ] [T031] [P1] [CONNECT] Update `backend/app/api/ai_blocks.py`:
  - Add import: `from app.ai.runtime.engine import run_ai_block`
  - Update `ask_question` endpoint:
    - Replace placeholder return with: `result = await run_ai_block("ask-question", request.model_dump())`
    - Return: `return AIBlockResponse(**result)` (or handle response format)
    - Add TODO comment: `# TODO: Update response model when real AI logic implemented`
  - Update `explain_like_10` endpoint:
    - Replace placeholder return with: `result = await run_ai_block("explain-like-10", request.model_dump())`
    - Return formatted response
  - Update `quiz` endpoint:
    - Replace placeholder return with: `result = await run_ai_block("quiz", request.model_dump())`
    - Return formatted response
  - Update `diagram` endpoint:
    - Replace placeholder return with: `result = await run_ai_block("diagram", request.model_dump())`
    - Return formatted response
  - Verify no syntax errors: Run `python -m py_compile backend/app/api/ai_blocks.py`

**Acceptance Test**: All 4 endpoints updated, imports resolve, backend starts without errors

---

## Phase 11: Validation Tasks

**Purpose**: Verify all modules exist, imports resolve, and backend starts successfully.

### File Existence Validation

- [ ] [T032] [P1] [VALIDATE] Verify all provider files exist:
  - Check `backend/app/ai/providers/base_llm.py` exists
  - Check `backend/app/ai/providers/openai_provider.py` exists
  - Check `backend/app/ai/providers/gemini_provider.py` exists

- [ ] [T033] [P1] [VALIDATE] Verify all RAG files exist:
  - Check `backend/app/ai/rag/qdrant_store.py` exists
  - Check `backend/app/ai/rag/pipeline.py` exists

- [ ] [T034] [P1] [VALIDATE] Verify runtime engine exists:
  - Check `backend/app/ai/runtime/engine.py` exists

- [ ] [T035] [P1] [VALIDATE] Verify all subagent files exist:
  - Check `backend/app/ai/subagents/ask_question_agent.py` exists
  - Check `backend/app/ai/subagents/explain_el10_agent.py` exists
  - Check `backend/app/ai/subagents/quiz_agent.py` exists
  - Check `backend/app/ai/subagents/diagram_agent.py` exists

- [ ] [T036] [P1] [VALIDATE] Verify all skill files exist:
  - Check `backend/app/ai/skills/retrieval_skill.py` exists
  - Check `backend/app/ai/skills/formatting_skill.py` exists
  - Check `backend/app/ai/skills/prompt_builder_skill.py` exists

- [ ] [T037] [P1] [VALIDATE] Verify ChatKit files exist:
  - Check `backend/app/ai/chatkit/session_manager.py` exists
  - Check `backend/app/ai/chatkit/tools.py` exists

- [ ] [T038] [P1] [VALIDATE] Verify chapter chunks file exists:
  - Check `backend/app/content/chapters/chapter_1_chunks.py` exists

### Import Resolution Validation

- [ ] [T039] [P1] [VALIDATE] Test provider imports:
  - Run: `python -c "from app.ai.providers.base_llm import BaseLLMProvider; print('OK')"`
  - Run: `python -c "from app.ai.providers.openai_provider import OpenAIProvider; print('OK')"`
  - Run: `python -c "from app.ai.providers.gemini_provider import GeminiProvider; print('OK')"`

- [ ] [T040] [P1] [VALIDATE] Test embedding imports:
  - Run: `python -c "from app.ai.embeddings.embedding_client import generate_embedding, batch_embed; print('OK')"`

- [ ] [T041] [P1] [VALIDATE] Test RAG imports:
  - Run: `python -c "from app.ai.rag.qdrant_store import create_collection, upsert_vectors, similarity_search; print('OK')"`
  - Run: `python -c "from app.ai.rag.pipeline import run_rag_pipeline; print('OK')"`

- [ ] [T042] [P1] [VALIDATE] Test runtime engine import:
  - Run: `python -c "from app.ai.runtime.engine import run_ai_block; print('OK')"`

- [ ] [T043] [P1] [VALIDATE] Test subagent imports:
  - Run: `python -c "from app.ai.subagents.ask_question_agent import ask_question_agent; print('OK')"`
  - Run: `python -c "from app.ai.subagents.explain_el10_agent import explain_el10_agent; print('OK')"`
  - Run: `python -c "from app.ai.subagents.quiz_agent import quiz_agent; print('OK')"`
  - Run: `python -c "from app.ai.subagents.diagram_agent import diagram_agent; print('OK')"`

- [ ] [T044] [P1] [VALIDATE] Test skill imports:
  - Run: `python -c "from app.ai.skills.retrieval_skill import retrieve_content; print('OK')"`
  - Run: `python -c "from app.ai.skills.formatting_skill import format_response; print('OK')"`
  - Run: `python -c "from app.ai.skills.prompt_builder_skill import build_prompt; print('OK')"`

- [ ] [T045] [P1] [VALIDATE] Test ChatKit imports:
  - Run: `python -c "from app.ai.chatkit.session_manager import create_session, append_message, get_history; print('OK')"`

- [ ] [T046] [P1] [VALIDATE] Test chapter chunks import:
  - Run: `python -c "from app.content.chapters.chapter_1_chunks import get_chapter_chunks; print('OK')"`

### Backend Startup Validation

- [ ] [T047] [P1] [VALIDATE] Start backend server: Run `cd backend && uvicorn app.main:app --reload`
  - Verify: Server starts without ImportError
  - Verify: Server starts without ModuleNotFoundError
  - Verify: Server starts without syntax errors
  - Verify: Health endpoint responds: `curl http://localhost:8000/health`

- [ ] [T048] [P1] [VALIDATE] Test API endpoints route to runtime engine:
  - Test `POST /api/ai/ask-question` with `{"question": "test", "chapterId": 1}`
  - Verify: Endpoint responds (even if placeholder response)
  - Verify: No 500 Internal Server Error
  - Verify: Response format is valid JSON

### Module Dependency Validation

- [ ] [T049] [P1] [VALIDATE] Verify no circular imports:
  - Check all imports are forward references or top-level
  - Verify runtime engine imports subagents without circular dependency
  - Verify subagents import skills without circular dependency

- [ ] [T050] [P1] [VALIDATE] Verify all TODO placeholders present:
  - Check all functions contain TODO comments
  - Check all modules have docstrings explaining purpose
  - Verify no real AI logic (no OpenAI, Gemini, Qdrant API calls)

---

## Phase 12: Documentation Tasks

**Purpose**: Ensure all documentation files are complete (already created in /sp.plan phase).

**Note**: These files were already created during `/sp.plan` phase:
- ✅ `specs/005-ai-runtime-engine/research.md` - Technology decisions
- ✅ `specs/005-ai-runtime-engine/data-model.md` - Function signatures and data contracts
- ✅ `specs/005-ai-runtime-engine/quickstart.md` - Verification guide
- ✅ `specs/005-ai-runtime-engine/contracts/content-schema.md` - Schema definitions
- ✅ `specs/005-ai-runtime-engine/checklists/requirements.md` - Quality checklist

- [ ] [T051] [P2] [DOCS] Verify all documentation files exist and are complete:
  - Review research.md for completeness
  - Review data-model.md for all function signatures
  - Review quickstart.md for verification steps
  - Review contracts/content-schema.md for schema definitions

---

## Task Summary

**Total Tasks**: 51 tasks
- **Phase 0 (Setup)**: 4 tasks
- **Phase 1 (Providers)**: 4 tasks
- **Phase 2 (Embeddings)**: 2 tasks
- **Phase 3 (RAG)**: 3 tasks
- **Phase 4 (Knowledge Source)**: 1 task
- **Phase 5 (Runtime Engine)**: 2 tasks
- **Phase 6 (Subagents)**: 5 tasks
- **Phase 7 (Skills)**: 4 tasks
- **Phase 8 (ChatKit)**: 3 tasks
- **Phase 9 (Config)**: 2 tasks
- **Phase 10 (API Integration)**: 1 task
- **Phase 11 (Validation)**: 18 tasks
- **Phase 12 (Documentation)**: 1 task

**Critical Path**: T001-T004 → T005-T008 → T009-T010 → T011-T013 → T014 → T015-T016 → T017-T021 → T022-T025 → T026-T028 → T029-T030 → T031 → T032-T050

**Estimated Time**: 3-4 hours (file creation + function signatures + imports + validation)

---

## Success Criteria Validation

### Spec Success Criteria → Task Mapping

| Success Criteria | Task IDs | Validation Method |
|------------------|----------|-------------------|
| **SC-001**: All required files exist at specified paths | T032-T038 | File existence checks |
| **SC-002**: ai_blocks.py updated to call run_ai_block() | T031 | Code review + import test |
| **SC-003**: settings.py includes all new AI-related env vars | T029 | Code review |
| **SC-004**: .env.example updated with all new variables | T030 | File review |
| **SC-005**: Backend starts successfully | T047 | Backend startup test |
| **SC-006**: All modules contain TODO placeholders | T050 | Code review |
| **SC-007**: API contract stub exists | ✅ Already exists | File existence |
| **SC-008**: All function signatures have type hints | T005-T028 | Code review |
| **SC-009**: No real AI logic implemented | T050 | Code review |

---

## Dependencies & Risks

### Internal Dependencies
- ✅ Feature 001 (Base Project) complete
- ✅ Feature 004 (Chapter 1 Interactive Blocks) complete

### External Dependencies
- ✅ Python 3.11+, FastAPI 0.109+, Pydantic 2.x (already installed)
- ✅ No new runtime dependencies required (scaffolding only)

### Risks & Mitigations

**Risk 1**: Import resolution failures
- **Mitigation**: Test imports incrementally (T039-T046), fix errors immediately

**Risk 2**: Breaking Feature 004 compatibility
- **Mitigation**: Update ai_blocks.py carefully (T031), test endpoints after update

**Risk 3**: Missing __init__.py files
- **Mitigation**: Create all __init__.py files in Phase 0 (T003)

**Risk 4**: Circular import issues
- **Mitigation**: Validate dependencies (T049), use forward references if needed

---

**Task Generation Complete**: 2025-12-05
**Ready for Implementation**: Yes ✅
**Next Command**: `/sp.implement` (or manual task-by-task execution)

