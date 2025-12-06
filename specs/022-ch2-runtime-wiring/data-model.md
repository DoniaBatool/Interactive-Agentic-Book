# Data Model: Chapter 2 Runtime Wiring

**Feature**: 022-ch2-runtime-wiring
**Generated**: 2025-12-05

## Entities

### 1. RAG Pipeline Functions

**Entity**: `embed_chapter_2()`, `retrieve_chapter_2_relevant_chunks()`, `build_context_for_ch2()`

**Location**: `backend/app/ai/rag/pipeline.py`

**Structure**:
```python
# Placeholder functions (TODO stubs)
async def embed_chapter_2() -> None:
    """Embed Chapter 2 chunks into vector database."""
    # TODO: Implement embedding batch processing
    pass

async def retrieve_chapter_2_relevant_chunks(
    query: str, 
    top_k: int = 5
) -> List[Dict[str, Any]]:
    """Retrieve relevant Chapter 2 chunks for a given query."""
    # TODO: Implement semantic search
    return []

async def build_context_for_ch2(query: str) -> Dict[str, Any]:
    """Build retrieval context for Chapter 2 requests."""
    # TODO: Implement context assembly
    return {
        "context": "",
        "chunks": [],
        "query_embedding": []
    }
```

**Metadata**:
- `CHAPTER_2_COLLECTION_NAME`: Constant for collection name ("chapter_2")

### 2. Runtime Engine Routing

**Entity**: `run_ai_block()` with chapter_id=2 handling

**Location**: `backend/app/ai/runtime/engine.py`

**Structure**:
```python
async def run_ai_block(
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Unified AI block runtime entry point."""
    chapter_id = request_data.get("chapterId", 1)
    
    if chapter_id == 2:
        # TODO: Check ENABLE_CHAPTER_2_RUNTIME flag
        # TODO: Import Chapter 2 subagents
        # TODO: Route to Chapter 2 subagent
        # TODO: Load Chapter 2 RAG context
        # TODO: Call Chapter 2 subagent with context
        # TODO: Format response
        pass
```

**Metadata**:
- `knowledge_sources`: Mapping of chapter_id to knowledge source name
- Chapter 2 routing logic (TODO placeholders)

### 3. API Endpoint Routing

**Entity**: AI block endpoints with chapterId=2 support

**Location**: `backend/app/api/ai_blocks.py`

**Structure**:
```python
@router.post("/api/ai/ask-question")
async def ask_question(request: AskQuestionRequest):
    """Placeholder endpoint for asking questions."""
    # TODO: Load Chapter 2 context
    result = await run_ai_block("ask-question", request.model_dump())
    return AIBlockResponse(...)

@router.post("/api/ai/explain-like-10")
async def explain_like_10(request: ExplainLike10Request):
    """Placeholder endpoint for generating explanations."""
    # TODO: Load Chapter 2 context
    result = await run_ai_block("explain-like-10", request.model_dump())
    return AIBlockResponse(...)

@router.post("/api/ai/quiz")
async def quiz(request: QuizRequest):
    """Placeholder endpoint for generating quizzes."""
    # TODO: Load Chapter 2 context
    result = await run_ai_block("quiz", request.model_dump())
    return AIBlockResponse(...)

@router.post("/api/ai/diagram")
async def diagram(request: DiagramRequest):
    """Placeholder endpoint for generating diagrams."""
    # TODO: Load Chapter 2 context
    result = await run_ai_block("diagram", request.model_dump())
    return AIBlockResponse(...)
```

**Metadata**:
- Request models with optional `chapterId` parameter
- Routing to runtime engine with chapter_id support

### 4. Subagent Connectors

**Entity**: Subagent files with Chapter 2 TODO comments

**Location**: `backend/app/ai/subagents/`

**Structure**:
```python
# ask_question_agent.py, explain_el10_agent.py, quiz_agent.py, diagram_agent.py
async def process_request(request_data: Dict[str, Any], context: Dict[str, Any]):
    """Process AI block request."""
    chapter_id = request_data.get("chapterId", 1)
    
    if chapter_id == 2:
        # TODO: Chapter 2 handling path
        # TODO: Process Chapter 2 requests with ROS 2 context
        # TODO: Use Chapter 2 RAG context in prompts
        # TODO: Format Chapter 2 responses
        pass
```

**Metadata**:
- Chapter 2 handling path (TODO placeholders)
- Context integration (TODO placeholders)

### 5. Knowledge Source Structure

**Entity**: Chapter 2 chunks module with structural metadata

**Location**: `backend/app/content/chapters/chapter_2_chunks.py`

**Structure**:
```python
# Structural TODO placeholders
chunk_count: int = 0  # TODO: Calculate chunk count from MDX content
expected_section_map: Dict[str, List[int]] = {}  # TODO: Build section map
embedding_ready: bool = False  # TODO: Set based on chunk availability

def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """Return list of text chunks from Chapter 2 with metadata."""
    # TODO: Implement chunking from MDX content
    return []
```

**Metadata**:
- `chunk_count`: Expected number of chunks
- `expected_section_map`: Section ID to chunk range mapping
- `embedding_ready`: Flag for embedding readiness

## Relationships

### 1. API Endpoints → Runtime Engine

**Relationship**: All API endpoints route to `run_ai_block()` with chapter_id support

**Flow**:
```
API Endpoint (chapterId=2) 
  → run_ai_block(block_type, request_data)
  → Runtime Engine (chapter_id=2 routing)
```

### 2. Runtime Engine → RAG Pipeline

**Relationship**: Runtime engine calls RAG pipeline for Chapter 2 context

**Flow**:
```
Runtime Engine (chapter_id=2)
  → build_context_for_ch2(query)
  → RAG Pipeline (Chapter 2 operations)
  → Context Dictionary
```

### 3. Runtime Engine → Subagents

**Relationship**: Runtime engine routes to Chapter 2 subagents

**Flow**:
```
Runtime Engine (chapter_id=2, block_type)
  → Chapter 2 Subagent (ch2_ask_question_agent, etc.)
  → Subagent Processing (with context)
  → Formatted Response
```

### 4. RAG Pipeline → Knowledge Source

**Relationship**: RAG pipeline retrieves chunks from knowledge source

**Flow**:
```
RAG Pipeline (Chapter 2 operations)
  → get_chapter_chunks(chapter_id=2)
  → Knowledge Source (chapter_2_chunks.py)
  → Chunk List with Metadata
```

## Data Flow

### Request Flow (Chapter 2)

```
1. User Request (chapterId=2)
   ↓
2. API Endpoint (/api/ai/ask-question)
   ↓
3. Runtime Engine (run_ai_block with chapter_id=2)
   ↓
4. RAG Pipeline (build_context_for_ch2)
   ↓
5. Knowledge Source (get_chapter_chunks)
   ↓
6. Context Assembly (build_context_for_ch2)
   ↓
7. Chapter 2 Subagent (ch2_ask_question_agent)
   ↓
8. Response Formatting
   ↓
9. API Response
```

### Context Building Flow

```
1. User Query
   ↓
2. retrieve_chapter_2_relevant_chunks(query, top_k)
   ↓
3. Query Embedding (CH2_EMBEDDING_MODEL)
   ↓
4. Semantic Search (Chapter 2 collection)
   ↓
5. Top-k Chunks Retrieved
   ↓
6. Context String Assembly
   ↓
7. Context Dictionary (context, chunks, query_embedding)
```

## Notes

- All entities are placeholders (TODO stubs) with no real implementation
- All relationships are documented but not implemented
- All data flows are architectural blueprints for future implementation
- Structural metadata (chunk_count, section_map, embedding_ready) are TODO placeholders
