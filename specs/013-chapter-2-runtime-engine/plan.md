# Implementation Plan: Chapter 2 — AI Runtime Engine Integration (LLM Routing, RAG Wiring, Subagents, ChatKit)

**Branch**: `013-chapter-2-runtime-engine` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/013-chapter-2-runtime-engine/spec.md`

## Summary

This feature activates the full runtime pathway for Chapter 2 AI blocks by creating scaffolding for routing, RAG binding, subagents, skills integration, and ChatKit. The implementation establishes the architectural foundation for Chapter 2 runtime engine integration with LLM routing, RAG context consumption, Chapter 2-specific subagents, chapter-aware skills, and ChatKit scaffolding. **No real AI logic is implemented**—only scaffolding, function signatures, TODO placeholders, and architectural blueprints to prepare for future AI implementation.

**Primary Deliverable**: Complete Chapter 2 runtime engine infrastructure scaffolding (4 subagents, skills updates, ChatKit updates, config updates)
**Validation**: All files exist, imports resolve, backend starts, no runtime errors

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- No new runtime dependencies required (scaffolding only)
- Existing runtime engine, RAG pipeline, skills, ChatKit from Feature 005

**Storage**: 
- No persistent storage (scaffolding only)
- Future: Qdrant for Chapter 2 vectors, Postgres for sessions

**Testing**:
- Manual: File existence verification, import resolution, backend startup
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)

**Project Type**: Backend AI runtime infrastructure scaffolding

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (no API calls, no LLM calls, no RAG execution)
- MUST maintain compatibility with Feature 005 (Chapter 1 runtime must still work)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend functionality
- MUST remain deterministic and simple
- MUST prepare for future model swapping

**Scale/Scope**:
- 4 new subagent files (ch2_*)
- 5 skills files to update (add Chapter 2 TODOs)
- 2 ChatKit files to update (add Chapter 2 scaffolding)
- 3 backend files to update (engine.py, pipeline.py, ai_blocks.py)
- 2 config files to update (settings.py, .env.example)
- ~200-300 lines of scaffolding code (mostly signatures, TODOs, and comments)

---

## 1. High-Level Architecture Overview

The Chapter 2 Runtime Engine provides a unified interface for all Chapter 2 interactive AI blocks. It orchestrates the flow from frontend API requests through RAG retrieval, LLM generation, and response formatting, specifically for ROS 2 knowledge.

### Architecture Flow

```
Frontend Component (Chapter 2)
    │
    ▼
API Endpoint (ai_blocks.py) - chapterId=2
    │
    ▼
Runtime Engine (engine.py)
    │
    ├─► Router: Determine block type → Select Chapter 2 subagent
    │   ├─► If chapterId=2:
    │   │   ├─► Route to ch2_ask_question_agent
    │   │   ├─► Route to ch2_explain_el10_agent
    │   │   ├─► Route to ch2_quiz_agent
    │   │   └─► Route to ch2_diagram_agent
    │
    ├─► RAG Pipeline (pipeline.py)
    │   ├─► Load Chapter 2 chunks (chapter_2_chunks.py)
    │   ├─► Embed user query (embedding_client.py)
    │   ├─► Qdrant similarity search (collection="chapter_2")
    │   └─► Construct retrieval context
    │
    ├─► Skills System (chapter-aware)
    │   ├─► Retrieval Skill (retrieval_skill.py) - Chapter 2 context
    │   ├─► Prompt Builder Skill (prompt_builder_skill.py) - ROS 2 prompts
    │   └─► Formatting Skill (formatting_skill.py) - Chapter 2 formatting
    │
    ├─► Chapter 2 Subagent
    │   ├─► ch2_ask_question_agent.py
    │   ├─► ch2_explain_el10_agent.py
    │   ├─► ch2_quiz_agent.py
    │   └─► ch2_diagram_agent.py
    │   └─► Uses skills + RAG context → Generates ROS 2 response
    │
    ├─► LLM Provider (base_llm.py → openai_provider.py | gemini_provider.py)
    │   └─► Generates response with ROS 2 context (DEFAULT_CH2_MODEL)
    │
    └─► Response Formatting → Return to API → Frontend
```

### Component Responsibilities

1. **Runtime Engine**: Routes Chapter 2 requests to appropriate subagents, coordinates RAG pipeline, selects LLM provider
2. **RAG Pipeline**: Retrieves Chapter 2 context from Qdrant collection "chapter_2"
3. **Chapter 2 Subagents**: Specialized agents for ROS 2 knowledge (question, explanation, quiz, diagram)
4. **Skills**: Chapter-aware reusable capabilities (retrieval, formatting, prompt building)
5. **ChatKit**: Multi-chapter session management and Chapter 2 tool definitions

### Data Flow

1. **Request**: Frontend sends request with chapterId=2 → API endpoint receives
2. **Routing**: Runtime engine identifies chapterId=2 → routes to Chapter 2 subagent
3. **RAG**: RAG pipeline retrieves Chapter 2 context from Qdrant
4. **Skills**: Skills assemble ROS 2 context + user input into prompts
5. **Subagent**: Chapter 2 subagent processes with ROS 2 context
6. **LLM**: LLM provider generates response with ROS 2 context (DEFAULT_CH2_MODEL)
7. **Formatting**: Skills format response for frontend
8. **Response**: API returns formatted response → Frontend displays

---

## 2. Runtime Routing

### 2.1 Routing Architecture: Chapter ID-Based Routing

**Decision**: Use chapter_id parameter to route to appropriate subagents and RAG pipeline in runtime engine

**Rationale**:
- **Scalable**: Easy to add more chapters (chapterId=3, 4, etc.)
- **Generic**: Same routing logic works for all chapters
- **Clear Separation**: Each chapter has its own subagents and context
- **Future-Proof**: Supports cross-chapter queries later

### 2.2 Runtime Engine Flow: block → runtime → rag pipeline → provider

**File**: `backend/app/ai/runtime/engine.py`

**Current State**: Has Chapter 2 knowledge source mapping from Feature 011, RAG integration comments from Feature 012

**Updates Required**:
- Add chapter_id=2 routing logic with placeholder comments
- Add placeholder LLM invocation for Chapter 2
- Add placeholder RAG-context consumption comments
- Add TODO notes for future logic implementation

**Routing Flow** (TODO):
```python
async def run_ai_block(
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Chapter 2 routing
    chapter_id = request_data.get("chapterId", 1)
    
    if chapter_id == 2:
        # TODO: Check ENABLE_CHAPTER_2_RUNTIME flag
        # if not ENABLE_CHAPTER_2_RUNTIME:
        #     return {"error": "Chapter 2 runtime disabled"}
        
        # TODO: Route to Chapter 2 subagent
        # CH2_SUBAGENT_MAP = {
        #     "ask-question": ch2_ask_question_agent,
        #     "explain-like-10": ch2_explain_el10_agent,
        #     "quiz": ch2_quiz_agent,
        #     "diagram": ch2_diagram_agent,
        # }
        # subagent = CH2_SUBAGENT_MAP.get(block_type)
        
        # TODO: Load Chapter 2 RAG context
        # from app.ai.rag.pipeline import run_rag_pipeline
        # query = request_data.get("question") or request_data.get("concept") or ""
        # context = await run_rag_pipeline(query, chapter_id=2, top_k=5)
        
        # TODO: Call Chapter 2 subagent with context
        # result = await subagent(request_data, context)
        
        # TODO: Format response
        # formatted = format_response(result, block_type, chapter_id=2)
        # return formatted
    
    elif chapter_id == 1:
        # Existing Chapter 1 logic
        ...
    """
```

**Breakdown**:
1. **block**: API endpoint receives request with block_type and chapterId=2
2. **runtime**: Runtime engine routes to Chapter 2 subagent based on block_type
3. **rag pipeline**: RAG pipeline retrieves Chapter 2 context from Qdrant
4. **provider**: LLM provider generates response with ROS 2 context (DEFAULT_CH2_MODEL)

### 2.3 Chapter 2 Subagent Mapping

**Mapping Structure** (TODO):
```python
# TODO: Chapter 2 subagent mapping
CH2_SUBAGENT_MAP = {
    "ask-question": ch2_ask_question_agent,
    "explain-like-10": ch2_explain_el10_agent,
    "quiz": ch2_quiz_agent,
    "diagram": ch2_diagram_agent,
}
```

**Routing Logic** (TODO):
```python
# TODO: Route to Chapter 2 subagent
if chapter_id == 2:
    from app.ai.subagents.ch2_ask_question_agent import ch2_ask_question_agent
    from app.ai.subagents.ch2_explain_el10_agent import ch2_explain_el10_agent
    from app.ai.subagents.ch2_quiz_agent import ch2_quiz_agent
    from app.ai.subagents.ch2_diagram_agent import ch2_diagram_agent
    
    subagent = CH2_SUBAGENT_MAP.get(block_type)
    if not subagent:
        return {"error": f"Unknown block type: {block_type}"}
```

---

## 3. Subagent Architecture

### 3.1 Architecture: Chapter-Specific Subagents with Shared Skills

**Decision**: Create Chapter 2-specific subagent files (ch2_*) that mirror Chapter 1 structure but with ROS 2 context, while sharing skills

**Rationale**:
- **Clarity**: Clear separation between Chapter 1 and Chapter 2 logic
- **Maintainability**: Easier to maintain chapter-specific logic
- **ROS 2 Context**: Dedicated subagents can handle ROS 2-specific concepts
- **Skills Reuse**: Skills remain shared and chapter-aware
- **Pattern Replication**: Follows Chapter 1 pattern for consistency

### 3.2 Chapter 2 Subagent Responsibilities

**File**: `backend/app/ai/subagents/ch2_ask_question_agent.py`

**Purpose**: Answer questions about ROS 2 concepts using Chapter 2 context

**Responsibilities**:
- Process ROS 2 questions with Chapter 2 RAG context
- Use ROS 2 concepts, analogies, examples
- Generate formatted answers with source citations
- Return structured response

**Function Signature** (TODO):
```python
async def ch2_ask_question_agent(
    question: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Process ROS 2 question with Chapter 2 context
    TODO: Use retrieval_skill to get additional context if needed
    TODO: Use prompt_builder_skill to construct ROS 2 question-answering prompt
    TODO: Call LLM provider (DEFAULT_CH2_MODEL) with prompt + context
    TODO: Use formatting_skill to format response with source citations
    TODO: Return formatted answer
    """
    return {
        "answer": "",
        "sources": [],
        "confidence": 0.0
    }
```

**Parts That Stay TODO**:
- Real LLM API calls
- Real RAG context processing
- Real source citation extraction
- Real confidence score calculation

---

**File**: `backend/app/ai/subagents/ch2_explain_el10_agent.py`

**Purpose**: Generate simplified explanations for ROS 2 concepts

**Responsibilities**:
- Process ROS 2 concepts with Chapter 2 context
- Generate age-appropriate explanations
- Use ROS 2 analogies (post office, restaurant, phone calls, package delivery)
- Return formatted explanation

**Function Signature** (TODO):
```python
async def ch2_explain_el10_agent(
    concept: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Generate ROS 2 explanation with Chapter 2 context
    TODO: Use prompt_builder_skill to build ELI10 prompt with ROS 2 context
    TODO: Call LLM provider (DEFAULT_CH2_MODEL) with ELI10 instructions
    TODO: Use formatting_skill to extract examples and analogies
    TODO: Return formatted explanation
    """
    return {
        "explanation": "",
        "examples": [],
        "analogies": []
    }
```

**Parts That Stay TODO**:
- Real LLM API calls
- Real explanation generation
- Real analogy extraction
- Real example generation

---

**File**: `backend/app/ai/subagents/ch2_quiz_agent.py`

**Purpose**: Generate interactive quizzes for ROS 2 learning objectives

**Responsibilities**:
- Process Chapter 2 learning objectives
- Generate ROS 2 quiz questions
- Cover ROS 2 concepts (nodes, topics, services, actions)
- Return formatted quiz

**Function Signature** (TODO):
```python
async def ch2_quiz_agent(
    chapter_id: int,
    num_questions: int,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Generate ROS 2 quiz with Chapter 2 context
    TODO: Use retrieval_skill to get learning objectives from Chapter 2 metadata
    TODO: Use prompt_builder_skill to build quiz generation prompt
    TODO: Call LLM provider (DEFAULT_CH2_MODEL) to generate questions
    TODO: Use formatting_skill to structure quiz data
    TODO: Return formatted quiz
    """
    return {
        "questions": [],
        "learning_objectives": []
    }
```

**Parts That Stay TODO**:
- Real LLM API calls
- Real quiz generation
- Real question type distribution
- Real learning objective coverage

---

**File**: `backend/app/ai/subagents/ch2_diagram_agent.py`

**Purpose**: Generate visual diagrams for ROS 2 concepts

**Responsibilities**:
- Process ROS 2 diagram requests
- Generate ROS 2 diagram structures
- Use ROS 2 concepts and relationships
- Return formatted diagram

**Function Signature** (TODO):
```python
async def ch2_diagram_agent(
    diagram_type: str,
    concepts: List[str],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    TODO: Generate ROS 2 diagram with Chapter 2 context
    TODO: Use prompt_builder_skill to build diagram generation prompt
    TODO: Call LLM provider (DEFAULT_CH2_MODEL) or diagram generation API
    TODO: Use formatting_skill to format diagram output
    TODO: Return diagram URL/metadata
    """
    return {
        "diagram_url": "",
        "metadata": {
            "title": "",
            "description": "",
            "concepts": [],
            "format": ""
        }
    }
```

**Parts That Stay TODO**:
- Real LLM API calls
- Real diagram generation
- Real diagram code/image generation
- Real diagram metadata extraction

---

## 4. Skills Reuse Plan

### 4.1 Skills Architecture: Chapter-Aware Skills

**Decision**: Update existing skills to be chapter-aware with Chapter 2-specific TODOs

**Rationale**:
- **Reusability**: Same skills work for all chapters
- **Flexibility**: Skills can adapt to chapter-specific context
- **Maintainability**: Single skill file per capability
- **Consistency**: Follows established pattern

### 4.2 Retrieval Skill: Chapter-Aware Retrieval

**File**: `backend/app/ai/skills/retrieval_skill.py`

**Current State**: Has placeholder function `retrieve_content()`

**Updates Required**:
- Add TODO: chapter-aware retrieval for Chapter 2
- Add placeholder comments for Chapter 2 RAG pipeline usage
- Document Chapter 2-specific retrieval logic

**Function Update** (TODO):
```python
async def retrieve_content(
    query: str,
    chapter_id: int,
    top_k: int = 5
) -> List[Dict[str, Any]]:
    """
    TODO: Chapter-aware retrieval
    TODO: If chapter_id == 2:
    TODO:     Use Chapter 2 RAG pipeline
    TODO:     from app.ai.rag.pipeline import run_rag_pipeline
    TODO:     context = await run_rag_pipeline(query, chapter_id=2, top_k=top_k)
    TODO:     Return Chapter 2 chunks with ROS 2 context
    TODO: Elif chapter_id == 1:
    TODO:     Use Chapter 1 RAG pipeline (existing logic)
    """
    return []
```

---

### 4.3 Prompt Builder Skill: Chapter-Aware Prompt Building

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Current State**: Has placeholder function `build_prompt()`

**Updates Required**:
- Add TODO: chapter-aware prompt builder for Chapter 2
- Add placeholder comments for ROS 2 prompt construction
- Document Chapter 2-specific prompt patterns

**Function Update** (TODO):
```python
def build_prompt(
    block_type: str,
    user_input: str,
    context: List[Dict[str, Any]],
    chapter_id: int = None
) -> str:
    """
    TODO: Chapter-aware prompt builder
    TODO: If chapter_id == 2:
    TODO:     Build ROS 2-specific prompts
    TODO:     Include ROS 2 concepts, analogies, examples
    TODO:     System prompt: "You are a helpful tutor explaining ROS 2 concepts..."
    TODO:     Include ROS 2 context chunks
    TODO:     Add ROS 2 terminology guidelines
    TODO: Elif chapter_id == 1:
    TODO:     Build Chapter 1 prompts (existing logic)
    """
    return ""
```

---

### 4.4 Formatting Skill: Chapter 2 Formatting Rules

**File**: `backend/app/ai/skills/formatting_skill.py`

**Current State**: Has placeholder function `format_response()`

**Updates Required**:
- Add TODO: formatting rules for Chapter 2
- Add placeholder comments for Chapter 2 response formatting
- Document Chapter 2-specific formatting patterns

**Function Update** (TODO):
```python
def format_response(
    raw_response: Dict[str, Any],
    block_type: str,
    chapter_id: int = None
) -> Dict[str, Any]:
    """
    TODO: Chapter 2 formatting rules
    TODO: If chapter_id == 2:
    TODO:     Apply Chapter 2 formatting rules
    TODO:     Include ROS 2-specific metadata
    TODO:     Format ROS 2 source citations
    TODO:     Format ROS 2 examples and analogies
    TODO: Elif chapter_id == 1:
    TODO:     Apply Chapter 1 formatting rules (existing logic)
    """
    return {}
```

---

### 4.5 Additional Skills: Quiz and Diagram Formatting

**File**: `backend/app/ai/skills/quiz_formatting_skill.py`

**Updates Required**:
- Add TODO: Chapter 2 quiz formatting rules
- Document ROS 2 quiz question formatting

**File**: `backend/app/ai/skills/diagram_skill.py`

**Updates Required**:
- Add TODO: Chapter 2 diagram generation rules
- Document ROS 2 diagram structure formatting

---

## 5. RAG Pipeline Link

### 5.1 RAG Pipeline Binding: Chapter-Aware Retrieval

**File**: `backend/app/ai/rag/pipeline.py`

**Current State**: Has Chapter 2 flow comments from Feature 012

**Updates Required**:
- Ensure pipeline resolves chapter_2_chunks when chapter_id=2
- Add placeholder flow comments for embedding query and retrieval context injection
- Document Chapter 2-specific retrieval logic

### 5.2 Conceptual Flow: Embedding User Query

**Step 1: Embed Query** (TODO):
```python
# TODO: Embed user query for Chapter 2
# from app.ai.embeddings.embedding_client import generate_embedding
# query_embedding = generate_embedding(query)
# Returns 1536-dimensional vector for text-embedding-3-small
```

**Step 2: Retrieve Context** (TODO):
```python
# TODO: Retrieve Chapter 2 context
# if chapter_id == 2:
#     from app.content.chapters.chapter_2_chunks import get_chapter_chunks
#     chunks = get_chapter_chunks(chapter_id=2)
#     
#     from app.ai.rag.qdrant_store import similarity_search
#     results = similarity_search(
#         collection_name="chapter_2",
#         query_embedding=query_embedding,
#         top_k=top_k
#     )
```

### 5.3 Placeholder Retrieval Context Injection

**Context Assembly** (TODO):
```python
# TODO: Assemble retrieval context for Chapter 2
# context = {
#     "context": assemble_context_string(results),
#     "chunks": results,
#     "query_embedding": query_embedding
# }
# 
# TODO: Filter by section_id if provided
# if sectionId:
#     context["chunks"] = [c for c in results if c["section_id"] == sectionId]
# 
# TODO: Limit context size (RAG_MAX_CONTEXT env var, default: 4 chunks)
# context["chunks"] = context["chunks"][:RAG_MAX_CONTEXT]
```

**Context Injection into Subagents** (TODO):
```python
# TODO: Pass context to Chapter 2 subagent
# result = await subagent(request_data, context)
# Subagent uses context["context"] in LLM prompts
# Subagent uses context["chunks"] for source citations
```

---

## 6. ChatKit Integration

### 6.1 Session Manager: Multi-Chapter Session Contexts

**File**: `backend/app/ai/chatkit/session_manager.py`

**Current State**: Has placeholder functions for session management

**Updates Required**:
- Add placeholder for multi-chapter session contexts
- Add TODO comments for Chapter 2 session handling
- Document how sessions will track Chapter 2 context

**Function Updates** (TODO):
```python
def create_session(user_id: str) -> str:
    """
    TODO: Multi-chapter session contexts
    TODO: Track Chapter 2 context in session
    TODO: Initialize chapter_context dictionary:
    TODO:     {
    TODO:         2: {
    TODO:             "last_accessed": timestamp,
    TODO:             "message_count": 0,
    TODO:             "topics": []
    TODO:         }
    TODO:     }
    TODO: Support cross-chapter queries
    """
    return ""

def append_message(session_id: str, message: Dict[str, Any]) -> bool:
    """
    TODO: Append message with Chapter 2 context
    TODO: If message has chapterId=2:
    TODO:     Update Chapter 2 context in session
    TODO:     Track ROS 2 topics discussed
    TODO:     Update last_accessed timestamp
    """
    return False

def get_history(session_id: str, chapter_id: int = None) -> List[Dict[str, Any]]:
    """
    TODO: Retrieve session history with Chapter 2 context
    TODO: If chapter_id == 2:
    TODO:     Filter messages by chapterId=2
    TODO:     Include Chapter 2 context metadata
    TODO: Return Chapter 2 message history
    """
    return []
```

### 6.2 Tools: Chapter 2 Block Tool Definitions

**File**: `backend/app/ai/chatkit/tools.py`

**Current State**: Has placeholder tool documentation

**Updates Required**:
- Add tool definitions for Chapter 2 blocks
- Document Chapter 2 tool schemas
- Add TODO comments for Chapter 2 tool implementation

**Tool Definitions** (TODO):
```python
# TODO: Chapter 2 Tool Definitions
# 
# ch2_ask_question_tool:
#   name: "ch2_ask_question"
#   description: "Ask questions about ROS 2 concepts"
#   input: {
#     "question": str,
#     "sectionId": str (optional)
#   }
#   output: {
#     "answer": str,
#     "sources": List[str]
#   }
# 
# ch2_explain_el10_tool:
#   name: "ch2_explain_el10"
#   description: "Explain ROS 2 concepts like I'm 10"
#   input: {
#     "concept": str
#   }
#   output: {
#     "explanation": str,
#     "examples": List[str]
#   }
# 
# ch2_quiz_tool:
#   name: "ch2_quiz"
#   description: "Generate ROS 2 quizzes"
#   input: {
#     "numQuestions": int
#   }
#   output: {
#     "questions": List[Dict],
#     "learning_objectives": List[str]
#   }
# 
# ch2_diagram_tool:
#   name: "ch2_diagram"
#   description: "Generate ROS 2 diagrams"
#   input: {
#     "diagramType": str,
#     "concepts": List[str]
#   }
#   output: {
#     "diagram_url": str,
#     "metadata": Dict
#   }
# 
# TODO: Implement tool definitions when ChatKit integrated
# TODO: Register tools with ChatKit session
# TODO: Handle tool calls from ChatKit
# TODO: Return tool results to ChatKit
```

---

## 7. File & Folder Plan

### 7.1 New Files to Create

```
backend/app/ai/subagents/
├── ch2_ask_question_agent.py      # NEW: Chapter 2 question-answering agent
├── ch2_explain_el10_agent.py      # NEW: Chapter 2 explanation agent
├── ch2_quiz_agent.py              # NEW: Chapter 2 quiz agent
└── ch2_diagram_agent.py           # NEW: Chapter 2 diagram agent
```

### 7.2 Files to Update

```
backend/app/ai/
├── runtime/
│   └── engine.py                  # UPDATE: Add chapter_id=2 routing, LLM invocation, RAG context
├── rag/
│   └── pipeline.py                # UPDATE: Ensure resolves chapter_2_chunks, add flow comments
├── skills/
│   ├── retrieval_skill.py         # UPDATE: Add Chapter 2 TODO
│   ├── prompt_builder_skill.py    # UPDATE: Add Chapter 2 TODO
│   ├── formatting_skill.py         # UPDATE: Add Chapter 2 TODO
│   ├── quiz_formatting_skill.py   # UPDATE: Add Chapter 2 TODO
│   └── diagram_skill.py            # UPDATE: Add Chapter 2 TODO
└── chatkit/
    ├── session_manager.py          # UPDATE: Add multi-chapter session contexts
    └── tools.py                    # UPDATE: Add Chapter 2 tool definitions

backend/app/
├── api/
│   └── ai_blocks.py                # VERIFY: All block types route to run_ai_block with chapterId=2
└── config/
    └── settings.py                 # UPDATE: Add DEFAULT_CH2_MODEL, DEFAULT_CH2_EMBEDDINGS, ENABLE_CHAPTER_2_RUNTIME

.env.example                        # UPDATE: Add 3 new environment variables
```

### 7.3 Contract Files Structure

```
specs/013-chapter-2-runtime-engine/
├── contracts/
│   ├── runtime-flow.yaml           # ✅ EXISTS: Runtime flow contract
│   └── chapter-2-blocks.yaml       # ✅ EXISTS: Chapter 2 blocks contract
```

### 7.4 File Modification Summary

**New Files**: 4 subagent files
- `ch2_ask_question_agent.py` - ~50 lines (signatures, TODOs, docstrings)
- `ch2_explain_el10_agent.py` - ~50 lines
- `ch2_quiz_agent.py` - ~50 lines
- `ch2_diagram_agent.py` - ~50 lines

**Updated Files**: 10 files
- `engine.py` - ~30 new lines (routing comments, TODOs)
- `pipeline.py` - ~10 new lines (Chapter 2 binding comments)
- `ai_blocks.py` - ~5 new lines (verify routing, add comments)
- 5 skills files - ~10 new lines each (Chapter 2 TODOs)
- 2 ChatKit files - ~15 new lines each (Chapter 2 scaffolding)
- `settings.py` - ~10 new lines (Chapter 2 config)
- `.env.example` - ~5 new lines (Chapter 2 env vars)

**Total**: ~200-300 lines of scaffolding code (mostly comments and TODOs)

---

## 8. Risks / Constraints

### 8.1 Risk Assessment

#### Risk 1: No Real Logic Allowed at This Stage
**Severity**: Low
**Probability**: Low
**Impact**: Medium

**Description**: This is a scaffolding-only feature. No real AI logic should be implemented.

**Mitigation**:
- Clear TODO markers in all functions
- Placeholder returns (empty lists, empty dicts, False, empty strings)
- Comprehensive comments explaining future implementation
- Code review to ensure no real API calls

#### Risk 2: Must Remain Deterministic and Simple
**Severity**: Medium
**Probability**: Low
**Impact**: Medium

**Description**: Routing logic must be simple and deterministic, not complex conditional logic.

**Mitigation**:
- Use simple if/elif structure for chapter_id routing
- Avoid nested conditionals
- Keep routing logic linear and easy to follow
- Document routing decisions clearly

#### Risk 3: Prepare for Future Model Swapping
**Severity**: Low
**Probability**: Medium
**Impact**: Low

**Description**: Configuration should support easy model swapping without code changes.

**Mitigation**:
- Use environment variables for model selection
- Make model selection configurable per chapter
- Document model selection logic in TODOs
- Plan for provider abstraction

#### Risk 4: Chapter 2 Subagent Naming Confusion
**Severity**: Low
**Probability**: Low
**Impact**: Low

**Description**: ch2_* naming might be confused with Chapter 1 subagents.

**Mitigation**:
- Clear naming convention (ch2_* for Chapter 2)
- Document naming pattern in comments
- Consistent naming across all Chapter 2 subagents
- Clear separation from Chapter 1 subagents

#### Risk 5: Skills Chapter-Awareness Complexity
**Severity**: Low
**Probability**: Medium
**Impact**: Low

**Description**: Making skills chapter-aware might add complexity.

**Mitigation**:
- Keep skills simple with chapter_id parameter
- Use if/elif structure for chapter-specific logic
- Document chapter-aware patterns clearly
- Maintain skill reusability

#### Risk 6: ChatKit Integration Overhead
**Severity**: Low
**Probability**: Low
**Impact**: Low

**Description**: ChatKit scaffolding might add unnecessary complexity.

**Mitigation**:
- Keep ChatKit scaffolding minimal (placeholders only)
- Document future integration clearly
- Focus on session context tracking
- Tool definitions are documentation only

---

## 9. Acceptance Criteria Mapping

### 9.1 Success Criteria

- ✅ Runtime engine can route chapter 2 requests
- ✅ All subagents + skills scaffolding exists
- ✅ ChatKit placeholder integration exists
- ✅ No real AI logic or real RAG logic implemented
- ✅ Backend starts without errors

### 9.2 Validation Steps

1. **File Existence**:
   - Verify 4 new subagent files exist
   - Verify all updated files have Chapter 2 TODOs

2. **Import Validation**:
   - All imports resolve without errors
   - Backend starts successfully

3. **Routing Validation**:
   - Runtime engine has chapter_id=2 routing comments
   - API endpoints accept chapterId=2

4. **TODO Validation**:
   - All functions have TODO comments
   - No real API calls or logic implemented

---

## 10. Dependencies & Risks

### 10.1 Dependencies

- **Feature 005** (AI Runtime Engine): Provides runtime engine, skills, ChatKit scaffolding
- **Feature 011** (Chapter 2 AI Blocks): Provides Chapter 2 AI blocks integration
- **Feature 012** (Chapter 2 RAG): Provides Chapter 2 RAG foundations

### 10.2 Blocking Dependencies

- None (all dependencies already exist)

### 10.3 Future Dependencies

- Real LLM provider implementation (future feature)
- Real RAG pipeline implementation (future feature)
- Real ChatKit integration (future feature)

---

## 11. Next Steps

1. Run `/sp.tasks` to generate implementation tasks
2. Review tasks.md for atomic task breakdown
3. Run `/sp.implement` to implement scaffolding
4. Validate all files updated correctly
5. Test backend startup and imports

---

**Status**: Plan complete, ready for `/sp.tasks`
