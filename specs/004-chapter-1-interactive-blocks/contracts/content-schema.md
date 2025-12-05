# Content Schema: Chapter 1 Interactive AI Blocks

**Feature**: 004-chapter-1-interactive-blocks
**Created**: 2025-12-05

## MDX Frontmatter Schema

**Format**: YAML
**Location**: Top of `frontend/docs/chapters/chapter-1.mdx` (already exists from Feature 003)

```yaml
# Existing frontmatter (from Feature 003) - no changes needed
title: "Chapter 1 — Introduction to Physical AI & Robotics"
description: "Learn the fundamentals of Physical AI and how robots become intelligent through AI integration"
sidebar_position: 1
sidebar_label: "Chapter 1: Intro to Physical AI"
tags: ["physical-ai", "robotics", "introduction", "beginner"]
```

**Validation Rules**:
- Frontmatter MUST remain unchanged (managed by Feature 003)
- No new frontmatter fields required for this feature
- AI block components are embedded in MDX body, not frontmatter

---

## Python Metadata Schema

**Format**: Python dictionary
**Location**: `backend/app/api/ai_blocks.py`

### Request Models Schema

```python
from pydantic import BaseModel
from typing import Optional, List

class AskQuestionRequest(BaseModel):
    """Request model for ask-question endpoint."""
    question: str                    # Required: User question text (min 1 char)
    chapterId: Optional[int] = None  # Optional: Chapter ID for context
    sectionId: Optional[str] = None # Optional: Section ID for context

class ExplainLike10Request(BaseModel):
    """Request model for explain-like-10 endpoint."""
    concept: str                     # Required: Concept name to explain (min 1 char)
    chapterId: Optional[int] = None  # Optional: Chapter ID for context

class QuizRequest(BaseModel):
    """Request model for quiz endpoint."""
    chapterId: int                  # Required: Chapter ID (positive integer)
    numQuestions: Optional[int] = 5  # Optional: Number of questions (1-20, default: 5)

class DiagramRequest(BaseModel):
    """Request model for diagram endpoint."""
    diagramType: str                 # Required: Diagram type identifier (min 1 char)
    chapterId: Optional[int] = None  # Optional: Chapter ID for context
    concepts: Optional[List[str]] = [] # Optional: List of concept names
```

### Response Model Schema

```python
class AIBlockResponse(BaseModel):
    """Unified response model for all AI block endpoints (placeholder)."""
    message: str                     # Required: Placeholder message
    received: dict                   # Required: Echo of received request payload
```

**Validation Rules**:
- All request models MUST use Pydantic BaseModel
- Required fields MUST be non-empty (string min length: 1, int min: 1)
- Optional fields MUST have default values
- Response model MUST return consistent format across all endpoints

---

## Component Props Schema (TypeScript)

**Format**: TypeScript interfaces
**Location**: `frontend/src/components/ai/*.tsx`

### AskQuestionBlock Props

```typescript
interface AskQuestionBlockProps {
  chapterId?: number;    // Optional: Chapter ID for context
  sectionId?: string;    // Optional: Section ID for context
}
```

### ExplainLike10Block Props

```typescript
interface ExplainLike10BlockProps {
  concept?: string;      // Optional: Concept name to explain
  chapterId?: number;    // Optional: Chapter ID for context
}
```

### InteractiveQuizBlock Props

```typescript
interface InteractiveQuizBlockProps {
  chapterId?: number;     // Optional: Chapter ID for quiz generation
  numQuestions?: number;  // Optional: Number of questions (default: 5)
}
```

### GenerateDiagramBlock Props

```typescript
interface GenerateDiagramBlockProps {
  diagramType?: string;  // Optional: Diagram type identifier
  chapterId?: number;    // Optional: Chapter ID for context
}
```

**Validation Rules**:
- All props MUST be optional (`?`) to allow standalone usage
- Prop names MUST match backend request model field names (camelCase)
- Props MUST be typed with TypeScript interfaces
- Components MUST accept props without errors when props are undefined

---

## Placeholder Contracts

### AI Block Placeholder Mapping

**Format**: MDX component usage
**Location**: `frontend/docs/chapters/chapter-1.mdx`

```mdx
<!-- Original placeholder (replaced with component) -->
<!-- AI-BLOCK: ask-question -->

<!-- Component usage -->
<AskQuestionBlock chapterId={1} sectionId="what-is-physical-ai" />
```

**Placeholder-to-Component Mapping**:

| Placeholder Comment | Component | Required Props | Optional Props |
|---------------------|-----------|----------------|----------------|
| `<!-- AI-BLOCK: ask-question -->` | `<AskQuestionBlock />` | None | `chapterId`, `sectionId` |
| `<!-- AI-BLOCK: explain-like-i-am-10 -->` | `<ExplainLike10Block />` | None | `concept`, `chapterId` |
| `<!-- AI-BLOCK: interactive-quiz -->` | `<InteractiveQuizBlock />` | None | `chapterId`, `numQuestions` |
| `<!-- AI-BLOCK: generate-diagram -->` | `<GenerateDiagramBlock />` | None | `diagramType`, `chapterId` |

**Validation Rules**:
- All 4 AI-BLOCK placeholders MUST be replaced with component usage
- Component imports MUST be at top of MDX file
- Props MUST match component interface definitions
- Components MUST render without React errors

### API Endpoint Placeholder Responses

**Format**: JSON response
**Location**: `backend/app/api/ai_blocks.py`

```json
{
  "message": "AI block placeholder",
  "received": {
    // Echo of request payload
  }
}
```

**Validation Rules**:
- All endpoints MUST return `AIBlockResponse` format
- `message` field MUST be "AI block placeholder" (scaffolding phase)
- `received` field MUST contain complete request payload
- No real AI logic MUST be present (only TODO comments)

---

## Glossary Term Rules

**Note**: This feature does not add new glossary terms. Glossary terms are managed by Feature 003 (Chapter 1 Content).

**Existing Glossary Terms** (from Feature 003):
- Physical AI
- Robot
- Sensor
- Actuator
- Autonomy
- Perception
- Control System

**Validation Rules**:
- No new glossary terms added in this feature
- AI block components may reference existing glossary terms
- Future features may add AI-specific glossary terms

---

## Validation Checklist

### Frontend Component Validation

- [ ] All 4 components exist at `frontend/src/components/ai/*.tsx`
- [ ] All components have TypeScript interfaces for props
- [ ] All props are optional (`?` syntax)
- [ ] Components render minimal UI without errors
- [ ] Event handlers log to console (no API calls)
- [ ] JSDoc comments present in all components
- [ ] Components compile without TypeScript errors

### MDX Integration Validation

- [ ] `frontend/src/mdx-components.ts` exists and exports all 4 components
- [ ] Chapter 1 MDX imports all 4 components
- [ ] All 4 AI-BLOCK comments replaced with component usage
- [ ] Components render in correct locations in Chapter 1
- [ ] Docusaurus build succeeds: `npm run build`
- [ ] No React errors in browser console

### Backend API Validation

- [ ] `backend/app/api/ai_blocks.py` exists with all 4 endpoints
- [ ] All request models use Pydantic BaseModel
- [ ] All endpoints return `AIBlockResponse` format
- [ ] Router included in `backend/app/main.py`
- [ ] All endpoints respond with placeholder JSON
- [ ] No real AI logic present (only TODO comments)
- [ ] API documentation accessible at `/docs` (Swagger UI)

### Integration Validation

- [ ] Frontend props match backend request field names
- [ ] Component state management uses React hooks only
- [ ] No global state management (Redux, Context) used
- [ ] No persistent storage (database, localStorage) used
- [ ] No external API calls (OpenAI, Qdrant) made
- [ ] All TODO comments present for future implementation

---

**Schema Status**: ✅ **COMPLETE** - All contracts defined for scaffolding phase

