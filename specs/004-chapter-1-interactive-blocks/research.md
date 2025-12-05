# Research: Chapter 1 Interactive AI Blocks

**Feature**: 004-chapter-1-interactive-blocks
**Date**: 2025-12-05
**Purpose**: Document technology choices, best practices, and implementation approaches for AI block component scaffolding

## Overview

This document captures research findings for implementing React components and FastAPI endpoints for AI-interactive blocks in Chapter 1. Since this is a scaffolding phase with no real AI logic, research focuses on component architecture patterns, MDX integration strategies, and API contract design.

## Technology Decisions

### 1. Frontend Component Architecture: React Functional Components with TypeScript

**Decision**: Use functional React components with TypeScript interfaces for type safety

**Rationale**:
- **Docusaurus Compatibility**: Docusaurus 3.x uses React 18+ with functional components as standard
- **Type Safety**: TypeScript interfaces ensure props are correctly typed when used in MDX
- **Minimal Dependencies**: No additional libraries required (React already in Docusaurus)
- **Future-Proof**: Functional components with hooks are the modern React pattern

**Component Pattern**:
```typescript
interface ComponentProps {
  chapterId?: number;
  sectionId?: string;
}

export default function Component({ chapterId, sectionId }: ComponentProps) {
  // Component logic
}
```

**Alternatives Considered**:
- **Class Components**: Legacy pattern, more verbose, harder to integrate with hooks
- **Styled Components**: Adds dependency, overkill for minimal UI scaffolding
- **CSS Modules**: More setup, inline styles sufficient for placeholder UI

**Best Practices**:
- Use optional props (`?`) to allow components to work standalone
- Include JSDoc comments for component purpose and usage
- Add TODO comments for future AI integration points
- Use inline styles for minimal UI (no external CSS dependencies)

### 2. MDX Component Integration: Direct Import Pattern

**Decision**: Use direct import pattern in MDX files rather than global component mapping

**Rationale**:
- **Explicit Dependencies**: Clear which components are used in each MDX file
- **Docusaurus 3.x Support**: Native MDX support for React component imports
- **Type Safety**: TypeScript can validate component usage
- **Flexibility**: Each MDX file can import only needed components

**Integration Pattern**:
```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';

<AskQuestionBlock chapterId={1} sectionId="what-is-physical-ai" />
```

**Alternatives Considered**:
- **Global MDX Components Mapping**: Requires swizzling Docusaurus theme, adds complexity
- **Plugin-Based**: Overkill for simple component integration
- **Runtime Component Loading**: Not supported in static site generation

**Best Practices**:
- Use `@site/src/components/` alias (Docusaurus convention)
- Import components at top of MDX file
- Replace AI-BLOCK comments with actual component usage
- Keep original comments as documentation (optional)

### 3. Backend API Structure: Single Router File with Pydantic Models

**Decision**: Group all AI block endpoints in single router file `backend/app/api/ai_blocks.py`

**Rationale**:
- **Logical Grouping**: All AI block endpoints are related functionality
- **Maintainability**: Single file easier to navigate and modify
- **Consistency**: All endpoints follow same pattern (request/response models)
- **Future Scalability**: Can split into separate files per subagent when needed

**Router Pattern**:
```python
router = APIRouter(prefix="/api/ai", tags=["ai-blocks"])

@router.post("/ask-question", response_model=AIBlockResponse)
async def ask_question(request: AskQuestionRequest) -> AIBlockResponse:
    return AIBlockResponse(message="AI block placeholder", received=request.model_dump())
```

**Alternatives Considered**:
- **Separate Files per Endpoint**: Too granular for 4 related endpoints
- **Nested Routers**: Adds complexity without benefit at this scale
- **Monolithic Router**: All endpoints in main.py - harder to maintain

**Best Practices**:
- Use Pydantic models for request/response validation
- Include comprehensive docstrings with TODO notes
- Use consistent response format (message + received payload)
- Add router to main.py with single include statement

### 4. Request/Response Schema Design: Minimal Placeholder Pattern

**Decision**: Use minimal request/response schemas that accept context but return placeholder responses

**Rationale**:
- **Future-Proof**: Request models include all fields needed for future AI integration
- **Type Safety**: Pydantic validates request structure
- **Consistency**: All endpoints return same response format
- **Clarity**: Placeholder responses clearly indicate scaffolding phase

**Schema Pattern**:
```python
class AskQuestionRequest(BaseModel):
    question: str
    chapterId: Optional[int] = None
    sectionId: Optional[str] = None

class AIBlockResponse(BaseModel):
    message: str
    received: dict
```

**Alternatives Considered**:
- **Empty Requests**: Too restrictive, doesn't prepare for future integration
- **Complex Responses**: Overkill for placeholder phase
- **Different Response Types**: Inconsistent, harder to test

**Best Practices**:
- Make context fields optional (chapterId, sectionId) for flexibility
- Include all fields that will be needed for AI integration
- Use descriptive field names matching frontend component props
- Document future response structure in TODO comments

### 5. Component Props Design: Optional Context Fields

**Decision**: Make all component props optional to allow standalone usage

**Rationale**:
- **Flexibility**: Components can be used with or without context
- **Progressive Enhancement**: Can add context later without breaking existing usage
- **Testing**: Easier to test components in isolation
- **MDX Usage**: Some blocks may not need all props in all contexts

**Props Pattern**:
```typescript
interface AskQuestionBlockProps {
  chapterId?: number;  // Optional context
  sectionId?: string;  // Optional context
}
```

**Alternatives Considered**:
- **Required Props**: Too rigid, breaks flexibility
- **No Props**: Can't pass context for future AI integration
- **Complex Props Objects**: Overkill for simple scaffolding

**Best Practices**:
- Use optional props (`?`) for all context fields
- Provide sensible defaults when props missing
- Document prop purposes in JSDoc comments
- Match prop names with backend request model fields

## Implementation Patterns

### Frontend Component Structure

**Component Template**:
```typescript
import React, { useState } from 'react';

/**
 * ComponentName Component
 * 
 * Purpose and usage description
 * 
 * @param prop1 - Description
 * @param prop2 - Description
 * 
 * @example
 * ```mdx
 * <ComponentName prop1={value1} prop2={value2} />
 * ```
 * 
 * TODO: Future AI integration notes
 */
interface ComponentNameProps {
  prop1?: type1;
  prop2?: type2;
}

export default function ComponentName({ prop1, prop2 }: ComponentNameProps) {
  const [state, setState] = useState(initialValue);

  const handleAction = () => {
    console.log('ComponentName: Action triggered', { prop1, prop2 });
    // TODO: Call API endpoint
  };

  return (
    <div style={{ /* inline styles */ }}>
      {/* Minimal UI */}
    </div>
  );
}
```

**Key Elements**:
- JSDoc comments for documentation
- TypeScript interface for props
- useState for component state (if needed)
- Event handlers with console.log placeholders
- TODO comments for future integration
- Inline styles for minimal UI

### Backend Endpoint Structure

**Endpoint Template**:
```python
@router.post("/endpoint-name", response_model=AIBlockResponse)
async def endpoint_name(request: RequestModel) -> AIBlockResponse:
    """
    Placeholder endpoint description.
    
    This endpoint will [future purpose].
    
    Args:
        request: RequestModel with fields
    
    Returns:
        AIBlockResponse with placeholder message and received payload
    
    TODO: Implementation notes
    """
    return AIBlockResponse(
        message="AI block placeholder",
        received=request.model_dump()
    )
```

**Key Elements**:
- Comprehensive docstrings
- Pydantic request/response models
- Placeholder response format
- TODO comments for future implementation
- Type hints for all parameters

### MDX Integration Pattern

**Chapter 1 MDX Update**:
```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';

## Section Title

Content here...

<AskQuestionBlock chapterId={1} sectionId="section-id" />

More content...

<ExplainLike10Block concept="concept-name" chapterId={1} />
```

**Key Elements**:
- Import statements at top of file
- Replace AI-BLOCK comments with component usage
- Pass appropriate props based on context
- Keep content flow natural

## Validation & Success Criteria

### Component Validation

**Checklist**:
1. ✅ All 4 components compile without TypeScript errors
2. ✅ Components render in Chapter 1 MDX without React errors
3. ✅ Event handlers log to console (no API calls)
4. ✅ Props are correctly typed and optional
5. ✅ JSDoc comments present and accurate

### Backend Validation

**Checklist**:
1. ✅ All 4 endpoints respond with placeholder JSON
2. ✅ Request models validate input correctly
3. ✅ Response models return consistent format
4. ✅ Router integrated in main.py
5. ✅ No real AI logic present (only TODO comments)

### Integration Validation

**Checklist**:
1. ✅ Docusaurus build succeeds
2. ✅ Components render in correct locations
3. ✅ No console errors in browser
4. ✅ MDX imports resolve correctly
5. ✅ No real API calls made (only console.log)

## Risks & Mitigations

### Risk 1: MDX Component Import Failures

**Probability**: Medium (Docusaurus 3.x import path resolution)
**Impact**: High (components won't render)

**Mitigation**:
- Use `@site/src/components/` alias (Docusaurus standard)
- Test build process early
- Document fallback to swizzle approach if needed

### Risk 2: TypeScript Compilation Errors

**Probability**: Low (simple component structure)
**Impact**: Medium (blocks build process)

**Mitigation**:
- Use strict TypeScript interfaces
- Test build after each component creation
- Fix type errors incrementally

### Risk 3: Backend Router Integration Issues

**Probability**: Low (standard FastAPI pattern)
**Impact**: Medium (endpoints won't be accessible)

**Mitigation**:
- Follow FastAPI router best practices
- Test endpoints immediately after integration
- Verify router included in main.py

### Risk 4: Component Props Mismatch

**Probability**: Medium (frontend/backend coordination)
**Impact**: Low (optional props allow flexibility)

**Mitigation**:
- Use consistent naming between frontend props and backend request fields
- Document prop purposes clearly
- Make all context props optional

## Next Steps (Future Features)

After this scaffolding phase is complete, future features will:

1. **RAG Integration**: Add Qdrant vector search and OpenAI API calls
2. **Real AI Logic**: Implement actual question answering, explanation generation, quiz creation, diagram generation
3. **User Authentication**: Add BetterAuth integration for personalized responses
4. **Error Handling**: Add proper error states and loading indicators
5. **Testing**: Add unit tests and integration tests for components and endpoints

## References

- Docusaurus MDX Documentation: https://docusaurus.io/docs/markdown-features/mdx
- React TypeScript Patterns: https://react-typescript-cheatsheet.netlify.app/
- FastAPI Router Patterns: https://fastapi.tiangolo.com/tutorial/bigger-applications/
- Pydantic Models: https://docs.pydantic.dev/latest/concepts/models/

