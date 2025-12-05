# Research Notes: AI Diagram Generation Engine

**Date**: 2025-12-05
**Feature**: 006-diagram-generation-engine

## Problem Context

This feature establishes the scaffolding for AI-powered diagram generation. The system needs to convert conceptual inputs (robot anatomy, physical AI overview, etc.) into visual diagrams (SVG/PNG/Mermaid) that can be embedded in MDX chapter content.

## Technology Decisions

### Diagram Generation Approaches

**Option 1: LLM Text-to-Diagram (GPT-4o, Gemini)**
- **Pros**: Flexible, can generate various diagram types, natural language input
- **Cons**: May require post-processing, quality varies
- **Decision**: Scaffold OpenAI and Gemini providers for future implementation

**Option 2: Template-Based Generation**
- **Pros**: Consistent output, predictable structure
- **Cons**: Less flexible, requires predefined templates
- **Decision**: Create template files for common diagram types (anatomy_robot, physical_ai_overview, etc.)

**Option 3: Mermaid/PlantUML Code Generation**
- **Pros**: Standard format, easy to render, version control friendly
- **Cons**: Requires LLM to generate code, not visual output
- **Decision**: Support Mermaid as output format (future enhancement)

### Provider Architecture

**Base Provider Interface**: Abstract base class ensures consistent interface across providers (OpenAI, Gemini, future providers).

**Provider Selection**: Environment variable `DIAGRAM_PROVIDER` allows switching between providers without code changes.

### Pipeline Architecture

**5-Step Pipeline**:
1. Validate diagram type
2. Build prompt template
3. Call provider
4. Receive SVG/textual description
5. Format output

This pipeline structure allows for future enhancements (caching, validation, post-processing).

## Implementation Patterns

### Scaffolding Pattern

All modules follow the scaffolding pattern:
- Abstract interfaces/base classes
- TODO placeholders for real implementation
- Placeholder return values
- Comprehensive docstrings

### Template System

Template files contain:
- Placeholder instructions
- Expected field documentation
- TODO guidelines for future implementation

### API Design

RESTful endpoint `/api/diagram/generate` with:
- Request: diagramType, chapterId, concepts[]
- Response: SVG string (placeholder initially)

## Validation Checklist

- [x] All provider interfaces defined
- [x] Pipeline structure documented
- [x] Template system designed
- [x] API contract defined
- [x] Frontend integration planned
- [x] Configuration strategy defined

## Future Enhancements

1. **Real AI Implementation**: Add OpenAI/Gemini API calls
2. **Diagram Rendering**: Implement SVG rendering in frontend
3. **Template Processing**: Add variable substitution and prompt building
4. **Caching**: Cache generated diagrams for performance
5. **Validation**: Add diagram type validation and error handling
6. **Multiple Formats**: Support PNG, Mermaid, PlantUML output formats

