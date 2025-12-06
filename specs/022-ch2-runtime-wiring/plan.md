# Implementation Plan: Chapter 2 — RAG Pipeline Wiring, Runtime Routing & AI Block Integration

**Branch**: `022-ch2-runtime-wiring` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/022-ch2-runtime-wiring/spec.md`

## Summary

This feature wires Chapter 2 into the AI Runtime Engine by adding RAG pipeline entry points, registering chapter_id=2 routing in the runtime engine, adding Chapter 2 context loading hooks to API endpoints, adding Chapter 2 handling path comments to subagents, and adding structural metadata placeholders to the knowledge source. **No actual RAG, routing, or AI logic is implemented**—only scaffolding, TODO placeholders, and architectural blueprints to prepare for future implementation.

**Primary Deliverable**: Complete runtime wiring scaffolding for Chapter 2 (RAG pipeline hooks, runtime engine routing, API endpoint hooks, subagent connectors, knowledge source structure)
**Validation**: Backend starts successfully, all imports resolve, runtime engine aware of Chapter 2, no business logic implemented

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- Feature 005 (AI Runtime Engine): Runtime engine must exist
- Feature 012 (Chapter 2 RAG Collection): ch2_collection.py must exist
- Feature 013 (Chapter 2 Subagents): Chapter 2 subagents must exist (or created in Feature 020)
- Feature 020 (Chapter 2 AI Runtime Extension): Chapter 2 scaffolding must exist
- Feature 021 (Chapter 2 RAG Preparation): Chapter 2 RAG preparation must exist

**Storage**: 
- Static files (Python modules) - no database
- Future: Qdrant for Chapter 2 vectors, embedding cache

**Testing**:
- Manual: Backend startup verification, import resolution, routing validation
- Backend: Python import test (`python -c "from app.ai.runtime.engine import run_ai_block"`)
- Backend: Startup test (`python -c "from app.main import app"`)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)

**Project Type**: Runtime wiring scaffolding (RAG pipeline hooks + runtime engine routing + API endpoint hooks + subagent connectors + knowledge source structure)

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement actual RAG logic (only TODO stubs)
- MUST NOT implement actual routing logic (only TODO comments)
- MUST maintain compatibility with Feature 005 (Chapter 1 functionality must still work)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality

**Scale/Scope**:
- 1 RAG pipeline file to update (pipeline.py)
- 1 runtime engine file to update (engine.py)
- 1 API endpoints file to update (ai_blocks.py)
- 4 subagent files to update (ask_question_agent.py, explain_el10_agent.py, quiz_agent.py, diagram_agent.py)
- 1 knowledge source file to update (chapter_2_chunks.py)
- 1 contract file already created (runtime-wiring.yaml)
- ~100-150 lines of scaffolding code (mostly TODOs, comments, and function stubs)

---

## 1. High-Level Architecture Overview

The runtime wiring for Chapter 2 connects all components together to enable Chapter 2 AI block functionality. It adds RAG pipeline entry points for Chapter 2 operations, registers chapter_id=2 routing in the runtime engine, adds context loading hooks to API endpoints, adds Chapter 2 handling path comments to subagents, and adds structural metadata placeholders to the knowledge source.

### Architecture Flow

```
API Endpoint (chapterId=2)
    │
    ├─► Extract chapterId from request
    │   └─► Route to runtime engine
    │       │
    │       ▼
    │   Runtime Engine (run_ai_block)
    │       │
    │       ├─► Detect chapter_id=2
    │       │   └─► Route to Chapter 2 handling path
    │       │       │
    │       │       ├─► Check ENABLE_CHAPTER_2_RUNTIME flag (TODO)
    │       │       ├─► Import Chapter 2 subagents (TODO)
    │       │       ├─► Route to Chapter 2 subagent (TODO)
    │       │       └─► Load Chapter 2 RAG context (TODO)
    │       │           │
    │       │           ▼
    │       │       RAG Pipeline (build_context_for_ch2)
    │       │           │
    │       │           ├─► Retrieve Chapter 2 chunks (TODO)
    │       │           ├─► Embed user query (TODO)
    │       │           ├─► Perform semantic search (TODO)
    │       │           └─► Assemble context (TODO)
    │       │               │
    │       │               ▼
    │       │           Chapter 2 Subagent
    │       │               │
    │       │               ├─► Process request with context (TODO)
    │       │               ├─► Generate response (TODO)
    │       │               └─► Format response (TODO)
    │       │                   │
    │       │                   ▼
    │       │               API Response
    │       │
    │       └─► Knowledge Source (chapter_2_chunks.py)
    │           ├─► chunk_count (TODO)
    │           ├─► expected_section_map (TODO)
    │           └─► embedding_ready = False (TODO)
```

### Component Responsibilities

1. **RAG Pipeline**: Provides Chapter 2-specific entry points for embedding, retrieval, and context building
2. **Runtime Engine**: Routes Chapter 2 requests to appropriate subagents and RAG pipeline
3. **API Endpoints**: Accept chapterId=2 and route to runtime engine with context loading hooks
4. **Subagents**: Process Chapter 2 requests with ROS 2 context (TODO placeholders)
5. **Knowledge Source**: Provides structural metadata for Chapter 2 chunks

### Data Flow

1. **Request Flow**: API Endpoint → Runtime Engine → RAG Pipeline → Subagent → Response
2. **Context Building**: User Query → RAG Pipeline → Retrieve Chunks → Build Context → Subagent
3. **Routing Flow**: chapterId=2 → Runtime Engine → Chapter 2 Handling Path → Chapter 2 Subagent

---

## 2. RAG Pipeline Architecture

### 2.1 Chapter 2 Collection Name Constant

**Decision**: Add `CHAPTER_2_COLLECTION_NAME` constant to `pipeline.py`

**Rationale**:
- Consistent naming with Chapter 1 pattern
- Can import from ch2_collection.py or define locally
- Clear separation of Chapter 2 operations

**Implementation**:
```python
# Option 1: Import from ch2_collection.py
from app.ai.rag.collections.ch2_collection import CH2_COLLECTION_NAME

# Option 2: Define locally (if import not available)
CHAPTER_2_COLLECTION_NAME = "chapter_2"  # From QDRANT_COLLECTION_CH2 env var
```

**Location**: `backend/app/ai/rag/pipeline.py`
**Placement**: Top of file, after imports, before function definitions

### 2.2 Embed Chapter 2 Function

**Decision**: Add `embed_chapter_2()` function stub with TODO comments

**Rationale**:
- Separate function for Chapter 2 embedding operations
- Clear entry point for future embedding batch processing
- Consistent with Chapter 1 pattern (if exists)

**Function Signature**:
```python
async def embed_chapter_2() -> None:
    """
    Embed Chapter 2 chunks into vector database.
    
    Steps (all TODO):
    1. Load Chapter 2 chunks from chapter_2_chunks.py
    2. Generate embeddings using CH2_EMBEDDING_MODEL
    3. Upsert embeddings into Chapter 2 collection (chapter_2)
    
    TODO: Implement embedding batch processing
    TODO: Implement Qdrant upsert operations
    TODO: Use batch_embed_ch2() from embedding_client.py
    TODO: Process chunks in batches (e.g., 100 chunks per batch)
    """
    pass
```

**Location**: `backend/app/ai/rag/pipeline.py`
**Placement**: After `run_rag_pipeline()` function

### 2.3 Retrieve Chapter 2 Relevant Chunks Function

**Decision**: Add `retrieve_chapter_2_relevant_chunks()` function stub with TODO comments

**Rationale**:
- Separate function for Chapter 2 retrieval operations
- Clear entry point for semantic search
- Consistent with Chapter 1 pattern (if exists)

**Function Signature**:
```python
async def retrieve_chapter_2_relevant_chunks(
    query: str,
    top_k: int = 5
) -> List[Dict[str, Any]]:
    """
    Retrieve relevant Chapter 2 chunks for a given query.
    
    Args:
        query: User query text
        top_k: Number of chunks to retrieve (default: 5)
    
    Returns:
        List of retrieved chunks with metadata
    
    Steps (all TODO):
    1. Embed user query using CH2_EMBEDDING_MODEL
    2. Perform semantic search in Chapter 2 collection (chapter_2)
    3. Return top-k most relevant chunks with metadata
    
    TODO: Implement query embedding
    TODO: Implement Qdrant similarity search
    TODO: Use search() from ch2_collection.py
    TODO: Return chunks with metadata structure
    """
    return []
```

**Location**: `backend/app/ai/rag/pipeline.py`
**Placement**: After `embed_chapter_2()` function

### 2.4 Build Context for Chapter 2 Function

**Decision**: Add `build_context_for_ch2()` function stub with TODO comments

**Rationale**:
- Separate function for Chapter 2 context assembly
- Clear entry point for context building
- Consistent with Chapter 1 pattern (if exists)

**Function Signature**:
```python
async def build_context_for_ch2(query: str) -> Dict[str, Any]:
    """
    Build retrieval context for Chapter 2 requests.
    
    Args:
        query: User query text
    
    Returns:
        Context dictionary with structure:
        {
            "context": str,                    # Assembled context string
            "chunks": List[Dict[str, Any]],   # Retrieved chunks with metadata
            "query_embedding": List[float]    # Query embedding vector
        }
    
    Steps (all TODO):
    1. Retrieve relevant chunks using retrieve_chapter_2_relevant_chunks
    2. Assemble chunks into context string with metadata
    3. Include section context and chunk metadata
    
    TODO: Implement context assembly
    TODO: Implement context formatting
    TODO: Include chunk metadata in context
    TODO: Format context for LLM prompt inclusion
    """
    return {
        "context": "",
        "chunks": [],
        "query_embedding": []
    }
```

**Location**: `backend/app/ai/rag/pipeline.py`
**Placement**: After `retrieve_chapter_2_relevant_chunks()` function

### 2.5 Naming Consistency

**Decision**: Use consistent naming with Chapter 1 (if Chapter 1 functions exist)

**Rationale**:
- Maintains codebase consistency
- Easier to understand and maintain
- Follows established patterns

**Naming Pattern**:
- Chapter 1: `embed_chapter_1()`, `retrieve_chapter_1_relevant_chunks()`, `build_context_for_ch1()`
- Chapter 2: `embed_chapter_2()`, `retrieve_chapter_2_relevant_chunks()`, `build_context_for_ch2()`

**Note**: If Chapter 1 functions don't exist, establish pattern for Chapter 2

---

## 3. Runtime Engine Flow

### 3.1 Chapter ID Detection

**Decision**: Extract chapter_id from request_data in `run_ai_block()` function

**Rationale**:
- Centralized chapter detection
- Consistent with existing Chapter 1 logic
- Clear routing point

**Implementation**:
```python
async def run_ai_block(
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Unified AI block runtime entry point."""
    # Extract chapter_id from request
    chapter_id = request_data.get("chapterId", 1)
    
    # Route based on chapter_id
    if chapter_id == 2:
        # Chapter 2 handling path (TODO)
        pass
    elif chapter_id == 1:
        # Existing Chapter 1 logic
        pass
    else:
        # TODO: Handle unknown chapter_id
        pass
```

**Location**: `backend/app/ai/runtime/engine.py`
**Placement**: Inside `run_ai_block()` function, after block_type routing

### 3.2 Chapter 2 Handling Path

**Decision**: Register chapter_id=2 handling path with comprehensive TODO comments

**Rationale**:
- Clear separation of Chapter 2 logic
- Easy to extend for future chapters
- Maintains existing Chapter 1 functionality

**Implementation**:
```python
if chapter_id == 2:
    # TODO: Check ENABLE_CHAPTER_2_RUNTIME flag
    # from app.config.settings import settings
    # if not settings.enable_chapter_2_runtime:
    #     return {"error": "Chapter 2 runtime disabled"}
    
    # TODO: Import Chapter 2 subagents
    # from app.ai.subagents.ch2_ask_question_agent import ch2_ask_question_agent
    # from app.ai.subagents.ch2_explain_el10_agent import ch2_explain_el10_agent
    # from app.ai.subagents.ch2_quiz_agent import ch2_quiz_agent
    # from app.ai.subagents.ch2_diagram_agent import ch2_diagram_agent
    
    # TODO: Route to Chapter 2 subagent
    # CH2_SUBAGENT_MAP = {
    #     "ask-question": ch2_ask_question_agent,
    #     "explain-like-10": ch2_explain_el10_agent,
    #     "quiz": ch2_quiz_agent,
    #     "diagram": ch2_diagram_agent,
    # }
    # subagent = CH2_SUBAGENT_MAP.get(block_type)
    # if not subagent:
    #     return {"error": f"Unknown block type: {block_type}"}
    
    # TODO: Load Chapter 2 RAG context
    # from app.ai.rag.pipeline import build_context_for_ch2
    # query = request_data.get("question") or request_data.get("concept") or ""
    # context = await build_context_for_ch2(query)
    
    # TODO: Call Chapter 2 subagent with context
    # result = await subagent(request_data, context)
    
    # TODO: Format response
    # from app.ai.skills.formatting_skill import format_response
    # formatted = format_response(result, block_type, chapter_id=2)
    # return formatted
    pass
```

**Location**: `backend/app/ai/runtime/engine.py`
**Placement**: Inside `run_ai_block()` function, in chapter_id=2 branch

### 3.3 Query → RAG Pipeline → Provider Flow

**Decision**: Document flow from query to RAG pipeline to provider

**Rationale**:
- Clear understanding of data flow
- Guides future implementation
- Maintains architectural consistency

**Flow Documentation**:
```python
# Flow: Query → RAG Pipeline → Provider
# 1. Extract query from request_data
#    query = request_data.get("question") or request_data.get("concept") or ""
# 2. Call RAG pipeline for Chapter 2 context
#    context = await build_context_for_ch2(query)
# 3. Pass context to Chapter 2 subagent
#    result = await subagent(request_data, context)
# 4. Subagent uses context in LLM prompt
# 5. LLM provider generates response with ROS 2 context
```

**Location**: `backend/app/ai/runtime/engine.py`
**Placement**: As comments in chapter_id=2 handling path

### 3.4 Context Merging Logic

**Decision**: Add TODO comments for context merging for Chapter 2

**Rationale**:
- Context merging combines RAG context with request data
- Important for subagent processing
- Needs clear documentation

**Implementation**:
```python
# TODO: Context merging for Chapter 2
# Merge RAG context with request_data for subagent processing
# merged_context = {
#     "rag_context": context,  # From build_context_for_ch2
#     "request_data": request_data,  # Original request
#     "chapter_id": 2,
#     "block_type": block_type
# }
# Pass merged_context to subagent
```

**Location**: `backend/app/ai/runtime/engine.py`
**Placement**: In chapter_id=2 handling path, before subagent call

### 3.5 Provider Selection for Chapter 2

**Decision**: Add TODO comments for provider selection for Chapter 2

**Rationale**:
- Chapter 2 may use different LLM provider/model
- Provider selection based on CH2_LLM_MODEL setting
- Needs clear documentation

**Implementation**:
```python
# TODO: Provider selection for Chapter 2
# Select LLM provider based on CH2_LLM_MODEL setting
# from app.config.settings import settings
# provider = get_provider(settings.ch2_llm_model)
# Use provider for Chapter 2 LLM calls
```

**Location**: `backend/app/ai/runtime/engine.py`
**Placement**: In chapter_id=2 handling path, before subagent call

---

## 4. AI Block Runtime Layer

### 4.1 Ask-Question Runtime

**Decision**: Add TODO comment for loading Chapter 2 context in ask-question endpoint

**Rationale**:
- Ask-question endpoint needs Chapter 2 context
- Context loading before routing to runtime engine
- Clear extension point

**Implementation**:
```python
@router.post("/api/ai/ask-question", response_model=AIBlockResponse)
async def ask_question(request: AskQuestionRequest) -> AIBlockResponse:
    """Placeholder endpoint for asking questions."""
    # TODO: Load Chapter 2 context if chapterId=2
    # if request.chapterId == 2:
    #     from app.ai.rag.pipeline import build_context_for_ch2
    #     context = await build_context_for_ch2(request.question)
    #     # Pass context to runtime engine
    
    # Route to runtime engine
    result = await run_ai_block("ask-question", request.model_dump())
    return AIBlockResponse(...)
```

**Location**: `backend/app/api/ai_blocks.py`
**Placement**: In `ask_question()` function, before routing to runtime engine

### 4.2 Explain-Like-10 Runtime

**Decision**: Add TODO comment for loading Chapter 2 context in explain-like-10 endpoint

**Rationale**:
- Explain-like-10 endpoint needs Chapter 2 context
- Context loading before routing to runtime engine
- Clear extension point

**Implementation**:
```python
@router.post("/api/ai/explain-like-10", response_model=AIBlockResponse)
async def explain_like_10(request: ExplainLike10Request) -> AIBlockResponse:
    """Placeholder endpoint for generating explanations."""
    # TODO: Load Chapter 2 context if chapterId=2
    # if request.chapterId == 2:
    #     from app.ai.rag.pipeline import build_context_for_ch2
    #     context = await build_context_for_ch2(request.concept)
    #     # Pass context to runtime engine
    
    # Route to runtime engine
    result = await run_ai_block("explain-like-10", request.model_dump())
    return AIBlockResponse(...)
```

**Location**: `backend/app/api/ai_blocks.py`
**Placement**: In `explain_like_10()` function, before routing to runtime engine

### 4.3 Quiz Runtime

**Decision**: Add TODO comment for loading Chapter 2 context in quiz endpoint

**Rationale**:
- Quiz endpoint needs Chapter 2 context
- Context loading before routing to runtime engine
- Clear extension point

**Implementation**:
```python
@router.post("/api/ai/quiz", response_model=AIBlockResponse)
async def quiz(request: QuizRequest) -> AIBlockResponse:
    """Placeholder endpoint for generating quizzes."""
    # TODO: Load Chapter 2 context if chapterId=2
    # if request.chapterId == 2:
    #     from app.ai.rag.pipeline import build_context_for_ch2
    #     # Quiz context may need different approach (all sections)
    #     context = await build_context_for_ch2("")  # Empty query for full chapter context
    #     # Pass context to runtime engine
    
    # Route to runtime engine
    result = await run_ai_block("quiz", request.model_dump())
    return AIBlockResponse(...)
```

**Location**: `backend/app/api/ai_blocks.py`
**Placement**: In `quiz()` function, before routing to runtime engine

### 4.4 Diagram Runtime

**Decision**: Add TODO comment for loading Chapter 2 context in diagram endpoint

**Rationale**:
- Diagram endpoint needs Chapter 2 context
- Context loading before routing to runtime engine
- Clear extension point

**Implementation**:
```python
@router.post("/api/ai/diagram", response_model=AIBlockResponse)
async def diagram(request: DiagramRequest) -> AIBlockResponse:
    """Placeholder endpoint for generating diagrams."""
    # TODO: Load Chapter 2 context if chapterId=2
    # if request.chapterId == 2:
    #     from app.ai.rag.pipeline import build_context_for_ch2
    #     # Diagram context may need concepts-based query
    #     query = " ".join(request.concepts or [])
    #     context = await build_context_for_ch2(query)
    #     # Pass context to runtime engine
    
    # Route to runtime engine
    result = await run_ai_block("diagram", request.model_dump())
    return AIBlockResponse(...)
```

**Location**: `backend/app/api/ai_blocks.py`
**Placement**: In `diagram()` function, before routing to runtime engine

### 4.5 Chapter 2 Support Verification

**Decision**: Ensure all endpoints can target chapter 2

**Rationale**:
- All AI block types must support Chapter 2
- Consistent behavior across endpoints
- Clear validation point

**Verification**:
- All endpoints accept `chapterId` parameter (optional or required)
- All endpoints route to runtime engine with `chapterId` in request_data
- Runtime engine handles `chapterId=2` correctly

---

## 5. Subagents & Skills

### 5.1 Ask Question Agent

**Decision**: Add TODO comments for Chapter 2 handling path in ask_question_agent.py

**Rationale**:
- Ask question agent needs Chapter 2 handling
- Clear extension point for ROS 2-specific logic
- Maintains consistency with Chapter 1

**Implementation**:
```python
async def ask_question_agent(
    request_data: Dict[str, Any],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """Process ask-question requests."""
    chapter_id = request_data.get("chapterId", 1)
    
    if chapter_id == 2:
        # TODO: Chapter 2 handling path
        # TODO: Process Chapter 2 requests with ROS 2 context
        # TODO: Use Chapter 2 RAG context in prompts
        # TODO: Format Chapter 2 responses
        # TODO: Include ROS 2-specific knowledge (nodes, topics, services, actions)
        pass
    elif chapter_id == 1:
        # Existing Chapter 1 logic
        pass
```

**Location**: `backend/app/ai/subagents/ask_question_agent.py`
**Placement**: In `ask_question_agent()` function, add chapter_id=2 branch

### 5.2 Explain EL10 Agent

**Decision**: Add TODO comments for Chapter 2 handling path in explain_el10_agent.py

**Rationale**:
- Explain EL10 agent needs Chapter 2 handling
- Clear extension point for ROS 2-specific explanations
- Maintains consistency with Chapter 1

**Implementation**:
```python
async def explain_el10_agent(
    request_data: Dict[str, Any],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """Process explain-like-10 requests."""
    chapter_id = request_data.get("chapterId", 1)
    
    if chapter_id == 2:
        # TODO: Chapter 2 handling path
        # TODO: Process Chapter 2 requests with ROS 2 context
        # TODO: Use Chapter 2 RAG context in prompts
        # TODO: Format Chapter 2 responses
        # TODO: Include ROS 2-specific analogies (post office, restaurant, phone calls)
        pass
    elif chapter_id == 1:
        # Existing Chapter 1 logic
        pass
```

**Location**: `backend/app/ai/subagents/explain_el10_agent.py`
**Placement**: In `explain_el10_agent()` function, add chapter_id=2 branch

### 5.3 Quiz Agent

**Decision**: Add TODO comments for Chapter 2 handling path in quiz_agent.py

**Rationale**:
- Quiz agent needs Chapter 2 handling
- Clear extension point for ROS 2-specific quizzes
- Maintains consistency with Chapter 1

**Implementation**:
```python
async def quiz_agent(
    request_data: Dict[str, Any],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """Process quiz requests."""
    chapter_id = request_data.get("chapterId", 1)
    
    if chapter_id == 2:
        # TODO: Chapter 2 handling path
        # TODO: Process Chapter 2 requests with ROS 2 context
        # TODO: Use Chapter 2 RAG context in prompts
        # TODO: Format Chapter 2 responses
        # TODO: Generate ROS 2-specific quiz questions (nodes, topics, services, actions)
        pass
    elif chapter_id == 1:
        # Existing Chapter 1 logic
        pass
```

**Location**: `backend/app/ai/subagents/quiz_agent.py`
**Placement**: In `quiz_agent()` function, add chapter_id=2 branch

### 5.4 Diagram Agent

**Decision**: Add TODO comments for Chapter 2 handling path in diagram_agent.py

**Rationale**:
- Diagram agent needs Chapter 2 handling
- Clear extension point for ROS 2-specific diagrams
- Maintains consistency with Chapter 1

**Implementation**:
```python
async def diagram_agent(
    request_data: Dict[str, Any],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """Process diagram requests."""
    chapter_id = request_data.get("chapterId", 1)
    
    if chapter_id == 2:
        # TODO: Chapter 2 handling path
        # TODO: Process Chapter 2 requests with ROS 2 context
        # TODO: Use Chapter 2 RAG context in prompts
        # TODO: Format Chapter 2 responses
        # TODO: Generate ROS 2-specific diagrams (node communication, topic pubsub, services/actions)
        pass
    elif chapter_id == 1:
        # Existing Chapter 1 logic
        pass
```

**Location**: `backend/app/ai/subagents/diagram_agent.py`
**Placement**: In `diagram_agent()` function, add chapter_id=2 branch

### 5.5 Skills Folder Chapter ID Recognition

**Decision**: Ensure skills folder recognizes chapter_id input

**Rationale**:
- Skills may need chapter-specific logic
- Chapter ID recognition enables chapter-aware processing
- Maintains consistency across skills

**Verification**:
- Skills functions accept `chapter_id` parameter (if needed)
- Skills can handle `chapter_id=2` appropriately
- Skills maintain backward compatibility with `chapter_id=1`

**Note**: Skills folder structure may already support chapter_id (from Feature 020), verify and document

---

## 6. Contracts

### 6.1 Runtime Wiring Contract

**Decision**: Contract already created in `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml`

**Rationale**:
- Contract created during specification phase
- Comprehensive documentation of all contracts
- Ready for reference during implementation

**Contract Sections**:
- Chapter Selection Flow Contract
- RAG Pipeline Integration Contract
- API-Level Routing Contract
- Context-Building Contract
- Subagent Integration Contract
- Knowledge Source Contract
- Validation Contract

**Location**: `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml`
**Status**: Already created, ready for reference

### 6.2 RAG → LLM → Block Response Flow

**Decision**: Document flow in contract (already documented)

**Rationale**:
- Clear understanding of data flow
- Guides implementation
- Maintains architectural consistency

**Flow**:
1. API Endpoint receives request with chapterId=2
2. API Endpoint routes to runtime engine
3. Runtime engine calls RAG pipeline for Chapter 2 context
4. RAG pipeline returns context dictionary
5. Runtime engine passes context to Chapter 2 subagent
6. Subagent uses context in LLM prompt
7. LLM generates response with ROS 2 context
8. Response formatted and returned to API endpoint

**Location**: `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml`
**Section**: Chapter Selection Flow Contract

### 6.3 Required Entrypoints

**Decision**: Document required entrypoints in contract (already documented)

**Rationale**:
- Clear list of required functions
- Guides implementation
- Ensures completeness

**Entrypoints**:
- `embed_chapter_2()` - Embed Chapter 2 chunks
- `retrieve_chapter_2_relevant_chunks()` - Retrieve relevant chunks
- `build_context_for_ch2()` - Build retrieval context
- Chapter 2 handling path in runtime engine
- Chapter 2 context loading in API endpoints
- Chapter 2 handling path in subagents

**Location**: `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml`
**Section**: RAG Pipeline Integration Contract, API-Level Routing Contract, Subagent Integration Contract

### 6.4 Chapter-Aware Behavior

**Decision**: Document chapter-aware behavior in contract (already documented)

**Rationale**:
- Clear understanding of chapter-specific logic
- Guides implementation
- Maintains consistency

**Chapter-Aware Behaviors**:
- Chapter ID detection and routing
- Chapter-specific RAG pipeline calls
- Chapter-specific subagent routing
- Chapter-specific context assembly
- Chapter-specific provider selection

**Location**: `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml`
**Section**: Chapter Selection Flow Contract, Context-Building Contract

---

## 7. Knowledge Source Structure

### 7.1 Chunk Count Placeholder

**Decision**: Add structural TODO comment for `chunk_count` in chapter_2_chunks.py

**Rationale**:
- Chunk count provides metadata for validation
- Useful for embedding pipeline readiness
- Clear extension point

**Implementation**:
```python
# Structural metadata for Chapter 2 chunks
chunk_count: int = 0  # TODO: Calculate chunk count from MDX content
# Expected: ~6-8 chunks based on chunk markers in chapter-2.mdx
```

**Location**: `backend/app/content/chapters/chapter_2_chunks.py`
**Placement**: Top of file, after imports, before function definitions

### 7.2 Expected Section Map Placeholder

**Decision**: Add structural TODO comment for `expected_section_map` in chapter_2_chunks.py

**Rationale**:
- Section map provides metadata for validation
- Useful for chunk-to-section mapping
- Clear extension point

**Implementation**:
```python
# Structural metadata for Chapter 2 chunks
expected_section_map: Dict[str, List[int]] = {}  # TODO: Build section map from MDX structure
# Expected structure:
# {
#     "introduction-to-ros2": [0, 1],
#     "nodes-and-node-communication": [2, 3],
#     "topics-and-messages": [4],
#     "services-and-actions": [5],
#     "ros2-packages": [6],
#     "launch-files-and-workflows": [7],
#     "glossary": [8]
# }
```

**Location**: `backend/app/content/chapters/chapter_2_chunks.py`
**Placement**: After `chunk_count`, before function definitions

### 7.3 Embedding Ready Flag

**Decision**: Add structural TODO comment for `embedding_ready` flag in chapter_2_chunks.py

**Rationale**:
- Embedding ready flag indicates chunk readiness
- Useful for validation and pipeline checks
- Clear extension point

**Implementation**:
```python
# Structural metadata for Chapter 2 chunks
embedding_ready: bool = False  # TODO: Set based on chunk availability
# Set to True when:
# - Chunks are extracted from MDX
# - Chunks have valid metadata
# - Chunks are ready for embedding generation
```

**Location**: `backend/app/content/chapters/chapter_2_chunks.py`
**Placement**: After `expected_section_map`, before function definitions

---

## 8. Validation

### 8.1 Backend Startup Validation

**Decision**: Verify backend starts without errors

**Rationale**:
- Ensures no breaking changes
- Validates import resolution
- Confirms scaffolding is correct

**Validation Steps**:
1. Start backend server: `python -m uvicorn app.main:app --reload`
2. Verify no import errors
3. Verify no runtime exceptions
4. Verify server starts successfully

**Expected Result**: Backend starts without errors

### 8.2 Import Resolution Validation

**Decision**: Verify all imports resolve successfully

**Rationale**:
- Ensures no broken imports
- Validates module structure
- Confirms scaffolding is correct

**Validation Steps**:
1. Test RAG pipeline imports: `python -c "from app.ai.rag.pipeline import embed_chapter_2, retrieve_chapter_2_relevant_chunks, build_context_for_ch2"`
2. Test runtime engine imports: `python -c "from app.ai.runtime.engine import run_ai_block"`
3. Test API endpoints imports: `python -c "from app.api.ai_blocks import router"`
4. Test subagent imports: `python -c "from app.ai.subagents.ask_question_agent import ask_question_agent"`
5. Test knowledge source imports: `python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks"`

**Expected Result**: All imports resolve without errors

### 8.3 Runtime Engine Awareness Validation

**Decision**: Verify runtime engine is "aware" of Chapter 2

**Rationale**:
- Ensures chapter_id=2 routing exists
- Validates Chapter 2 handling path
- Confirms scaffolding is correct

**Validation Steps**:
1. Check `backend/app/ai/runtime/engine.py` for chapter_id=2 handling path
2. Verify TODO comments exist for Chapter 2 operations
3. Verify chapter_id=2 branch exists in `run_ai_block()` function

**Expected Result**: Runtime engine contains chapter_id=2 handling path with TODO comments

### 8.4 No Business Logic Validation

**Decision**: Verify no business logic is implemented (only scaffolding)

**Rationale**:
- Ensures only scaffolding is added
- Validates TODO placeholders exist
- Confirms feature scope is correct

**Validation Steps**:
1. Review all modified files for TODO comments
2. Verify no actual RAG implementation
3. Verify no actual routing implementation
4. Verify no actual subagent logic implementation

**Expected Result**: Only TODO comments and function stubs exist, no business logic

### 8.5 Contract Validation

**Decision**: Verify contract documentation is complete

**Rationale**:
- Ensures contracts are comprehensive
- Validates documentation quality
- Confirms feature completeness

**Validation Steps**:
1. Review `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml`
2. Verify all contract sections exist
3. Verify all placeholders are documented
4. Verify all entrypoints are documented

**Expected Result**: Contract documentation is complete and comprehensive

---

## 9. Integration Points

### 9.1 Feature 005 (AI Runtime Engine)

**Integration**: Runtime engine provides base infrastructure for Chapter 2 routing

**Changes Required**:
- Add chapter_id=2 handling path in `run_ai_block()` function
- Add TODO comments for Chapter 2 operations
- Maintain backward compatibility with Chapter 1

**Location**: `backend/app/ai/runtime/engine.py`

### 9.2 Feature 020 (Chapter 2 AI Runtime Extension)

**Integration**: Chapter 2 scaffolding provides subagents and collection structure

**Changes Required**:
- Use existing Chapter 2 subagents (ch2_ask_question_agent, etc.)
- Use existing Chapter 2 collection (ch2_collection.py)
- Wire subagents into runtime engine routing

**Location**: `backend/app/ai/runtime/engine.py`, `backend/app/ai/rag/pipeline.py`

### 9.3 Feature 021 (Chapter 2 RAG Preparation)

**Integration**: Chapter 2 RAG preparation provides chunking infrastructure

**Changes Required**:
- Use existing chunk markers in MDX
- Use existing chunking blueprint (chapter_2_chunks.py)
- Add structural metadata placeholders

**Location**: `backend/app/content/chapters/chapter_2_chunks.py`

### 9.4 Feature 012 (Chapter 2 RAG Collection)

**Integration**: Chapter 2 RAG collection provides collection structure

**Changes Required**:
- Use existing CH2_COLLECTION_NAME constant
- Use existing collection functions (if any)
- Wire collection into RAG pipeline

**Location**: `backend/app/ai/rag/pipeline.py`

### 9.5 Feature 013 (Chapter 2 Subagents)

**Integration**: Chapter 2 subagents provide agent structure

**Changes Required**:
- Use existing Chapter 2 subagents
- Wire subagents into runtime engine routing
- Add Chapter 2 handling path comments to generic subagents

**Location**: `backend/app/ai/runtime/engine.py`, `backend/app/ai/subagents/`

---

## 10. Acceptance Checks

### 10.1 RAG Pipeline Wiring

- [ ] `CHAPTER_2_COLLECTION_NAME` constant exists in `pipeline.py`
- [ ] `embed_chapter_2()` function stub exists with TODO comments
- [ ] `retrieve_chapter_2_relevant_chunks()` function stub exists with TODO comments
- [ ] `build_context_for_ch2()` function stub exists with TODO comments
- [ ] All function signatures are properly typed
- [ ] All function docstrings are complete

### 10.2 Runtime Engine Routing

- [ ] chapter_id=2 handling path exists in `run_ai_block()` function
- [ ] TODO comments exist for Chapter 2 operations
- [ ] Context merging TODO comments exist
- [ ] Provider selection TODO comments exist
- [ ] Chapter 2 subagent routing TODO comments exist
- [ ] Chapter 2 RAG context loading TODO comments exist

### 10.3 AI Block Runtime Hooks

- [ ] All 4 endpoints have TODO comments for Chapter 2 context loading
- [ ] All endpoints can accept chapterId=2
- [ ] All endpoints route to runtime engine with chapterId support
- [ ] No breaking changes to existing endpoints

### 10.4 Subagent Connectors

- [ ] All 4 subagents have TODO comments for Chapter 2 handling path
- [ ] All subagents have chapter_id=2 branch
- [ ] All subagents maintain backward compatibility with Chapter 1
- [ ] All TODO comments are descriptive and actionable

### 10.5 Knowledge Source Structure

- [ ] `chunk_count` placeholder exists with TODO comment
- [ ] `expected_section_map` placeholder exists with TODO comment
- [ ] `embedding_ready` flag exists with TODO comment
- [ ] All structural metadata is properly documented

### 10.6 Validation

- [ ] Backend starts without errors
- [ ] All imports resolve successfully
- [ ] Runtime engine is "aware" of Chapter 2
- [ ] No business logic implemented (only scaffolding)
- [ ] Contract documentation is complete

---

## 11. Risk Analysis

### 11.1 Import Errors

**Risk**: New imports may cause import errors

**Mitigation**:
- Use conditional imports with try/except
- Verify all imports resolve before committing
- Test imports in isolation

**Impact**: Low (scaffolding only, no real imports needed)

### 11.2 Breaking Changes

**Risk**: Changes may break existing Chapter 1 functionality

**Mitigation**:
- Maintain backward compatibility
- Test Chapter 1 functionality after changes
- Use feature flags if needed

**Impact**: Medium (must maintain Chapter 1 functionality)

### 11.3 Incomplete Scaffolding

**Risk**: Scaffolding may be incomplete or inconsistent

**Mitigation**:
- Follow established patterns from Feature 020/021
- Review all files for consistency
- Validate against contract documentation

**Impact**: Low (scaffolding can be refined)

---

## 12. Next Steps

1. **Tasks Phase**: Generate atomic tasks for implementation (`/sp.tasks`)
2. **Implementation Phase**: Implement scaffolding (`/sp.implement`)
3. **Validation Phase**: Verify all acceptance checks pass
4. **Future Features**: Implement actual RAG, routing, and AI logic

---

## Summary

This architecture plan provides a comprehensive blueprint for wiring Chapter 2 into the AI Runtime Engine. All components are connected through TODO placeholders and scaffolding, ready for future implementation. The plan maintains backward compatibility with Chapter 1, follows established patterns, and provides clear extension points for future development.
