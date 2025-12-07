# AI Block MDX Integration Contract: Chapter 3

**Feature**: 039-ch3-ai-blocks
**Created**: 2025-01-27
**Status**: Draft

## Overview

This contract defines the MDX integration patterns for Chapter 3 AI blocks. All components reuse existing patterns from Chapter 1 and Chapter 2 but are configured for Chapter 3 context (chapterId=3, Physical AI Perception Systems concepts, section IDs).

---

## Block Names

**AI Block Types** (4 total):
1. `ask-question` - AskQuestionBlock component
2. `explain-like-i-am-10` - ExplainLike10Block component
3. `interactive-quiz` - InteractiveQuizBlock component
4. `generate-diagram` - GenerateDiagramBlock component

**Validation Rules**:
- Block names MUST match exactly (kebab-case)
- Block names MUST be replaced with React components (not HTML comments)
- Block names MUST map to corresponding React component names (PascalCase)

---

## MDX Usage Patterns

### Import Statements

**Location**: Top of `frontend/docs/chapters/chapter-3.mdx` (after frontmatter)

**Format**:
```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
```

**Validation Rules**:
- Import paths MUST use `@site/src/components/ai/` prefix
- Component names MUST match exported component names exactly
- Imports MUST be placed after frontmatter and before content

---

### Component Usage in MDX

**Format**: React JSX component calls embedded in MDX content

**Ask Question Block**:
```mdx
<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />
```

**Explain Like 10 Block**:
```mdx
<ExplainLike10Block concept="computer-vision" chapterId={3} />
```

**Interactive Quiz Block**:
```mdx
<InteractiveQuizBlock chapterId={3} numQuestions={5} />
```

**Generate Diagram Block**:
```mdx
<GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />
```

---

## Component Placement Map

### Section 1: What Is Perception in Physical AI?

**Placement**: End of section
**Component**: `<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />`
**Replaces**: `<!-- AI-BLOCK: ask-question -->`

### Section 2: Types of Sensors in Robotics

**Placement**: Middle of section (after diagram placeholder)
**Component**: `<GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />`
**Replaces**: `<!-- AI-BLOCK: generate-diagram -->`

### Section 3: Computer Vision & Depth Perception

**Placement**: Middle of section (before diagram placeholder)
**Component**: `<ExplainLike10Block concept="computer-vision" chapterId={3} />`
**Replaces**: `<!-- AI-BLOCK: explain-like-i-am-10 -->`

### Section 4: Signal Processing Basics for AI

**Placement**: End of section
**Component**: `<InteractiveQuizBlock chapterId={3} numQuestions={5} />`
**Replaces**: `<!-- AI-BLOCK: interactive-quiz -->`

---

## Component Props Contract

### AskQuestionBlock Props

**Required Props**:
- `chapterId`: number (3)
- `sectionId`: string ("what-is-perception-in-physical-ai")

**Example**:
```mdx
<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />
```

### ExplainLike10Block Props

**Required Props**:
- `chapterId`: number (3)
- `concept`: string ("computer-vision")

**Example**:
```mdx
<ExplainLike10Block concept="computer-vision" chapterId={3} />
```

### InteractiveQuizBlock Props

**Required Props**:
- `chapterId`: number (3)
- `numQuestions`: number (5)

**Example**:
```mdx
<InteractiveQuizBlock chapterId={3} numQuestions={5} />
```

### GenerateDiagramBlock Props

**Required Props**:
- `chapterId`: number (3)
- `diagramType`: string ("sensor-types")

**Example**:
```mdx
<GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />
```

---

## MDX Component Registry

**Location**: `frontend/src/mdx-components.ts`

**Required Exports**:
```typescript
export default {
  AskQuestionBlock,
  ExplainLike10Block,
  InteractiveQuizBlock,
  GenerateDiagramBlock,
};
```

**Note**: Explicit imports in MDX file also work if registry is not used.

---

## Validation Rules

1. **Component Placement**: All components MUST be placed exactly as defined in Feature 037
2. **Props Validation**: All required props MUST be provided with correct types
3. **Import Validation**: All components MUST be imported from correct paths
4. **Build Validation**: Docusaurus build MUST succeed without errors
5. **Render Validation**: All components MUST render visually in browser

---

## Summary

This contract defines the complete MDX integration pattern for Chapter 3 AI blocks. All components follow Chapter 1 and Chapter 2 patterns, configured for Chapter 3 context. No backend changes required—only frontend UI component placement.

