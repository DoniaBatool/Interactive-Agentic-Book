# Research: AI Runtime Engine Extension for Chapter 2

**Feature**: 020-chapter-2-ai-runtime
**Date**: 2025-12-05
**Purpose**: Document research findings for extending the AI Runtime Engine (Feature 005) to support Chapter 2 content with RAG collection setup, embedding pipeline extension, runtime routing, subagents, skills reuse, and ChatKit integration

## Overview

This document captures research findings for extending the existing AI Runtime Engine (Feature 005) to support Chapter 2 content. Research focuses on RAG collection setup, embedding pipeline extension, runtime routing patterns, subagent architecture, skills reuse, and ChatKit integration. Since this is a scaffolding phase, research focuses on architectural patterns and placeholder design.

## Technology Decisions

### 1. RAG Collection Setup: Chapter-Specific Collections

**Decision**: Create Chapter 2-specific RAG collection module (`ch2_collection.py`) with TODO stubs for collection operations

**Rationale**:
- **Isolation**: Each chapter has its own Qdrant collection
- **Scalability**: Easy to add more chapters (chapter_3, chapter_4, etc.)
- **Performance**: Separate collections allow independent optimization
- **Maintenance**: Clear separation of concerns

**Collection Pattern**:
```python
# backend/app/ai/rag/collections/ch2_collection.py
CH2_COLLECTION_NAME = "chapter_2"

def create_collection():
    """TODO: Create Qdrant collection for Chapter 2"""
    pass

def upsert_vectors(chunks, embeddings):
    """TODO: Upsert vectors to Chapter 2 collection"""
    pass

def search(query_embedding, top_k):
    """TODO: Search Chapter 2 collection"""
    pass
```

**Alternatives Considered**:
- **Single Collection with Metadata**: Harder to manage, no clear boundaries
- **Dynamic Collection Names**: Adds complexity, constant simpler

### 2. Embedding Pipeline Extension: Chapter-Aware Embeddings

**Decision**: Extend embedding client to support chapter=2 parameter with TODO stubs

**Rationale**:
- **Flexibility**: Different chapters may use different embedding models
- **Consistency**: Same pattern as Chapter 1
- **Future-Proof**: Supports chapter-specific embedding strategies

**Extension Pattern**:
```python
# backend/app/ai/embeddings/embedding_client.py
def generate_embedding(text: str, chapter_id: int = 1) -> List[float]:
    """TODO: Add chapter_id parameter support"""
    pass

def batch_embed_ch2(chunks: List[str]) -> List[List[float]]:
    """TODO: Batch embedding for Chapter 2 chunks"""
    pass
```

**Alternatives Considered**:
- **Separate Embedding Clients**: Too much duplication
- **Config-Based**: Adds complexity, parameter simpler

### 3. Runtime Routing Extension: Chapter ID-Based Routing

**Decision**: Extend runtime engine to route chapterId=2 calls to CH2 RAG with placeholder handlers

**Rationale**:
- **Consistency**: Same pattern as Chapter 1
- **Scalability**: Easy to add more chapters
- **Clear Separation**: Each chapter has its own routing logic

**Routing Pattern**:
```python
# backend/app/ai/runtime/engine.py
chapter_id = request_data.get("chapterId", 1)
if chapter_id == 2:
    # TODO: Route to CH2 RAG
    # TODO: Call CH2 subagents
    # TODO: Use CH2 context
```

**Alternatives Considered**:
- **Separate Runtime Engines**: Too complex, unnecessary separation
- **Config-Based Routing**: Adds overhead, chapterId simpler

### 4. Subagents Extension: Verify and Extend Existing Subagents

**Decision**: Verify Chapter 2 subagents exist (from Feature 013) or create if missing, with TODO blueprints

**Rationale**:
- **Reusability**: Subagents from Feature 013 can be extended
- **Consistency**: Same pattern as Chapter 1
- **Maintainability**: Clear separation between chapters

**Subagent Structure**:
```python
# backend/app/ai/subagents/ch2_ask_question_agent.py
async def ch2_ask_question_agent(question: str, context: Dict) -> Dict:
    """
    Input schema placeholder
    Output schema placeholder
    TODO: orchestrate provider + RAG
    """
    return {"answer": "", "sources": []}
```

**Alternatives Considered**:
- **Shared Subagents**: Less clear, harder to maintain
- **Single Subagent with Switch**: Too monolithic

### 5. Skills Reuse: Chapter-Aware Skills

**Decision**: Update skills to support Chapter 2 with TODO comments

**Rationale**:
- **Reusability**: Same skills work for all chapters
- **Flexibility**: Skills can adapt to chapter-specific context
- **Maintainability**: Single skill file per capability

**Skills Extension**:
```python
# backend/app/ai/skills/retrieval_skill.py
# TODO: support CH2 collection name

# backend/app/ai/skills/prompt_builder_skill.py
# TODO: templates for CH2
```

**Alternatives Considered**:
- **Separate Skills**: Too much duplication
- **Config-Based**: Adds complexity

### 6. ChatKit Session Support: Multi-Chapter Sessions

**Decision**: Extend session manager to track chapterId=2 with TODO stubs

**Rationale**:
- **Context**: Sessions can track multiple chapters
- **Memory**: Chapter-specific memory nodes improve context
- **Future-Proof**: Supports cross-chapter conversations

**Session Extension**:
```python
# backend/app/ai/chatkit/session_manager.py
# TODO: Extend session_manager to track chapterId=2
# TODO: attach CH2 memory nodes
```

**Alternatives Considered**:
- **Separate Session Managers**: Too complex
- **Single Session**: Less context, harder to manage

### 7. Configuration: Chapter-Specific Settings

**Decision**: Add Chapter 2-specific settings to settings.py and .env.example

**Rationale**:
- **Flexibility**: Different chapters may use different models
- **Deployment**: Easy to configure per environment
- **Maintainability**: Clear configuration structure

**Configuration Pattern**:
```python
# backend/app/config/settings.py
QDRANT_COLLECTION_CH2: Optional[str] = None
CH2_EMBEDDING_MODEL: Optional[str] = None
CH2_LLM_MODEL: Optional[str] = None
```

**Alternatives Considered**:
- **Single Configuration**: Less flexible
- **Config Files**: Adds complexity, env vars simpler

## Industry References

- **RAG Architecture**: LangChain RAG patterns, LlamaIndex retrieval patterns
- **Multi-Chapter Systems**: Textbook AI systems, educational AI platforms
- **Vector Database Best Practices**: Qdrant documentation, Pinecone best practices
- **LLM Routing**: OpenAI function calling, Anthropic tool use patterns

## Observations

### Key Points

1. **Scaffolding First**: All extensions are scaffolding only (TODO placeholders)
2. **Pattern Replication**: Follows Feature 005 and Feature 013 patterns
3. **Chapter Isolation**: Each chapter has its own collection, subagents, context
4. **Skills Reuse**: Skills are chapter-aware but reusable
5. **Configuration**: Chapter-specific settings for flexibility

### Challenges

1. **Verification**: Need to verify what Feature 013 already created
2. **Consistency**: Ensure all extensions follow same patterns
3. **Documentation**: Clear TODO comments for future implementation

### Technical Considerations

1. **Import Stability**: All new modules must import without errors
2. **Backward Compatibility**: Must not break Chapter 1 functionality
3. **Configuration**: All new settings must be optional

## Technology Stack

- **Backend**: Python 3.8+, FastAPI
- **Vector Database**: Qdrant (future)
- **Embeddings**: OpenAI text-embedding-3-small (future)
- **LLM**: OpenAI GPT-4o-mini (future)
- **Architecture**: RAG pipeline, runtime engine, subagents, skills

## Next Steps

1. Create architecture plan (`/sp.plan`)
2. Generate implementation tasks (`/sp.tasks`)
3. Implement scaffolding (`/sp.implement`)
