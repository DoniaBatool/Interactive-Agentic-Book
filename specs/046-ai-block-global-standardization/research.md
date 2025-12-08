# Research Notes: Global AI Block Standardization

**Feature**: 046-ai-block-global-standardization
**Date**: 2025-01-27

## Problem Context

Currently, Chapters 1, 2, and 3 have different implementations for AI blocks:
- Different subagent structures
- Different formatting approaches
- Different RAG context handling
- Different error handling

This creates:
- Inconsistent user experience
- Code duplication
- Maintenance burden
- Difficulty adding new chapters

## Industry References

### Registry Pattern
- **Django's App Registry**: Auto-discovery and registration of apps
- **Flask's Blueprint Registry**: Modular component registration
- **FastAPI's Router Registry**: Route registration pattern

### Unified Interface Pattern
- **REST API Standards**: Consistent request/response structures
- **GraphQL Schema**: Unified query interface
- **gRPC Service Definitions**: Contract-first approach

### Override System Pattern
- **Django Settings**: Base settings with environment-specific overrides
- **React Context**: Default values with provider overrides
- **Configuration Hierarchies**: Global → Environment → Local

## Observations

### Current State Analysis

**Chapter 1**:
- Uses `engine.py` with direct subagent calls
- Custom formatting in subagents
- No registry system

**Chapter 2**:
- Uses `ch2_*` prefixed modules
- Separate RAG pipeline
- Chapter-specific formatting

**Chapter 3**:
- Uses `ch3/` subdirectory structure
- Unified RAG pipeline (from Phase 2)
- Skills-based approach

### Standardization Opportunities

1. **Subagent Registry**: All chapters can use same registry pattern
2. **Unified RAG Pipeline**: Already exists in Phase 2, can be used by all
3. **Output Formatter**: Can standardize all response structures
4. **Skills**: Already unified, just need to ensure chapter support

### Override System Design

**Tiered Fallback Model**:
1. Chapter override (if exists)
2. Global default

**Override Scope**:
- Tone (formal, casual, enthusiastic)
- Difficulty (beginner, intermediate, advanced)
- Formatting style (custom rules)
- Prompt modifications (block-specific tweaks)

**Override Constraints**:
- Cannot override input/output structure
- Cannot override error format
- Cannot override RAG context structure

## Best Practices

### Registry Pattern Best Practices
- Use decorators for auto-registration
- Support lazy loading
- Provide discovery mechanisms
- Handle missing registrations gracefully

### Contract-First Approach
- Define contracts before implementation
- Validate against contracts
- Version contracts
- Document contract changes

### Override System Best Practices
- Clear precedence rules
- Validation of overrides
- Documentation of override capabilities
- Testing override scenarios

## Implementation Considerations

### Migration Strategy
1. Create registry and register existing subagents
2. Update runtime engine to use registry
3. Create unified formatter
4. Update skills to support all chapters
5. Migrate API endpoints
6. Add override system (optional)

### Backward Compatibility
- Existing subagents should work without changes
- Gradual migration possible
- Old code paths can coexist during transition

### Testing Strategy
- Test identical response structures across chapters
- Test override system
- Test registry with new chapters
- Test error handling consistency

## Future Considerations

### Extensibility
- Easy to add new AI block types
- Easy to add new chapters
- Easy to add new override capabilities

### Performance
- Registry lookup should be O(1)
- Override loading should be cached
- No performance degradation from standardization

### Maintainability
- Single source of truth for contracts
- Clear separation of concerns
- Easy to understand and modify

