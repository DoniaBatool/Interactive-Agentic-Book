# Research Notes: Chapter 2 Runtime Wiring

**Feature**: 022-ch2-runtime-wiring
**Date**: 2025-12-05

## Problem Context

Chapter 2 (ROS 2 Fundamentals) needs to be fully integrated into the AI Runtime Engine. While Feature 020 created scaffolding for Chapter 2 AI runtime extension, and Feature 021 prepared RAG chunking infrastructure, the actual wiring between components is missing. This feature connects all the pieces together:

- RAG pipeline needs Chapter 2-specific entry points
- Runtime engine needs Chapter 2 routing logic
- API endpoints need Chapter 2 context loading
- Subagents need Chapter 2 handling paths
- Knowledge source needs structural metadata

## Technology Decisions

### 1. RAG Pipeline Wiring

**Decision**: Add Chapter 2-specific functions to `pipeline.py` as TODO stubs.

**Rationale**: 
- Keeps Chapter 2 operations separate from Chapter 1
- Allows future implementation without refactoring
- Maintains clear separation of concerns

**Alternatives Considered**:
- Single generic function with chapter_id parameter (rejected: less clear, harder to extend)
- Separate pipeline file for Chapter 2 (rejected: unnecessary complexity for scaffolding)

### 2. Runtime Engine Routing

**Decision**: Add chapter_id=2 handling path in `run_ai_block()` function.

**Rationale**:
- Centralized routing logic
- Easy to extend for future chapters
- Clear chapter-specific handling

**Alternatives Considered**:
- Separate runtime engine for Chapter 2 (rejected: unnecessary duplication)
- Plugin-based routing (rejected: over-engineering for current needs)

### 3. Subagent Integration

**Decision**: Add TODO comments to existing subagents for Chapter 2 handling path.

**Rationale**:
- Reuses existing subagent structure
- Clear extension points for future implementation
- Maintains consistency with Chapter 1 approach

**Alternatives Considered**:
- Create separate Chapter 2 subagents (already done in Feature 020/013)
- Generic subagents with chapter_id parameter (rejected: less clear separation)

### 4. Knowledge Source Structure

**Decision**: Add structural TODO comments for chunk_count, expected_section_map, embedding_ready.

**Rationale**:
- Provides clear metadata structure
- Enables validation and readiness checks
- Supports future embedding pipeline

**Alternatives Considered**:
- Separate metadata file (rejected: adds complexity)
- Database storage (rejected: premature optimization)

## Industry References

### RAG Pipeline Architecture

- **LangChain RAG Pipeline**: Multi-step retrieval pipeline (retrieve → embed → search → context)
- **LlamaIndex RAG Pipeline**: Similar pattern with query understanding and context assembly
- **Pattern**: Separate functions for embedding, retrieval, and context building

### Runtime Engine Patterns

- **FastAPI Router Pattern**: Centralized routing with dependency injection
- **Strategy Pattern**: Chapter-specific handling strategies
- **Factory Pattern**: Subagent creation based on block_type and chapter_id

### Context Assembly

- **Context Window Management**: Limit context size to avoid token limits
- **Metadata Inclusion**: Include chunk metadata for better context understanding
- **Context Formatting**: Format context for LLM prompt inclusion

## Observations

### Current Architecture

- Feature 005: AI Runtime Engine (base infrastructure)
- Feature 020: Chapter 2 AI Runtime Extension (scaffolding)
- Feature 021: Chapter 2 RAG Preparation (chunking infrastructure)
- Feature 022: Chapter 2 Runtime Wiring (this feature - connecting pieces)

### Integration Points

1. **RAG Pipeline** → **Runtime Engine**: Context retrieval and assembly
2. **Runtime Engine** → **Subagents**: Request routing and context passing
3. **API Endpoints** → **Runtime Engine**: Request routing with chapter_id
4. **Knowledge Source** → **RAG Pipeline**: Chunk retrieval and metadata

### Challenges

1. **No Real Implementation**: All operations are placeholders (TODO stubs)
2. **Import Dependencies**: Must ensure all imports resolve without errors
3. **Backward Compatibility**: Chapter 1 functionality must remain unchanged
4. **Future Extensibility**: Architecture must support future chapters

## Technical Considerations

### Function Signatures

- All functions use type hints for clarity
- Async functions for RAG pipeline operations
- Consistent return types across functions

### Error Handling

- Placeholder error handling (TODO comments)
- Graceful degradation for missing components
- Clear error messages for debugging

### Testing Strategy

- Import validation (all imports resolve)
- Backend startup validation (no runtime errors)
- Routing validation (chapter_id=2 paths exist)
- Contract validation (all placeholders documented)

## Next Steps

1. Implement specification (this phase)
2. Create architecture plan (next phase)
3. Generate implementation tasks (following phase)
4. Implement scaffolding (final phase)
