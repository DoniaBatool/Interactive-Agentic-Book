# Research Notes: Chapter 1 Diagram Generator Runtime

**Date**: 2025-12-05
**Feature**: 008-chapter-1-diagram-runtime

## Problem Context

This feature establishes the scaffolding for AI-powered diagram generation runtime for Chapter 1. The system needs to generate diagrams using LLM reasoning + structured outputs, supporting future integrations with SVG generators, JSON diagram structures, ChatKit tools, Skill-based agents, and the AI Runtime Engine.

## Technology Decisions

### Diagram Generation Approaches

**Option 1: LLM Reasoning + Structured Outputs**
- **Pros**: Flexible, can generate complex diagrams, natural language input
- **Cons**: May require prompt engineering, quality varies
- **Decision**: Scaffold runtime with LLM reasoning pipeline

**Option 2: Template-Based Generation**
- **Pros**: Consistent output, predictable structure
- **Cons**: Less flexible, requires predefined templates
- **Decision**: Support structured diagram schemas (nodes, edges)

**Option 3: SVG Direct Generation**
- **Pros**: Direct visual output, standard format
- **Cons**: Complex to generate, requires SVG knowledge
- **Decision**: Scaffold SVG conversion skill for future implementation

### Runtime Architecture

**Pipeline Flow**:
1. Validate input (diagramType, chapterId, concepts)
2. Retrieve contextual chunks (RAG)
3. Use Diagram Agent (plan → create → generate)
4. Format final diagram output structure

**Agent Methods**:
- `plan_diagram()` - Plan diagram structure using LLM reasoning
- `create_structure()` - Create diagram structure (nodes, edges)
- `generate_svg_stub()` - Generate SVG stub or code

### Schema Design

**Structured Models**:
- `DiagramRequest` - Input validation
- `DiagramNode` - Node structure (id, label, type, position)
- `DiagramEdge` - Edge structure (source, target, label, type)
- `DiagramResponse` - Output structure (nodes, edges, svg, metadata)

### Skills Architecture

**Three Core Skills**:
- `extraction_skill` - Extract diagram elements from context
- `layout_skill` - Layout diagram structure (positions, relationships)
- `svg_conversion_skill` - Convert structured diagram to SVG

## Implementation Patterns

### Scaffolding Pattern

All modules follow the scaffolding pattern:
- Function signatures with type hints
- TODO placeholders for real implementation
- Placeholder return values
- Comprehensive docstrings

### Integration Pattern

Diagram runtime integrates with:
- RAG pipeline for context retrieval
- Diagram agent for generation
- Skills for processing
- API layer for requests

### Schema Pattern

Pydantic models for type safety:
- Request/response validation
- Structured data contracts
- Optional fields for flexibility

## Validation Checklist

- [x] Runtime pipeline designed
- [x] Diagram agent methods defined
- [x] Schema models designed
- [x] Skills architecture planned
- [x] RAG integration points identified
- [x] API integration planned

## Future Enhancements

1. **Real AI Implementation**: Add LLM calls for diagram generation
2. **SVG Generation**: Implement actual SVG creation
3. **Layout Algorithms**: Add automatic layout algorithms
4. **Diagram Types**: Support multiple diagram types (flowchart, concept map, etc.)
5. **Caching**: Cache generated diagrams for performance

