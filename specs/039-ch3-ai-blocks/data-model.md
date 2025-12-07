# Data Model: Chapter 3 AI Blocks Integration

**Feature**: 039-ch3-ai-blocks
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 3 AI blocks integration

## Entity Definitions

### 1. MDX Component Integration (Primary Entity)

**Description**: Represents the integration of React AI block components into Chapter 3 MDX file

**Storage**: MDX file at `frontend/docs/chapters/chapter-3.mdx`

**Structure**:
```mdx
---
title: "Chapter 3 — Physical AI Perception Systems..."
---
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';

## Section 1: What Is Perception in Physical AI?
[Content]
<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />

## Section 2: Types of Sensors in Robotics
[Content]
<GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />

## Section 3: Computer Vision & Depth Perception
[Content]
<ExplainLike10Block concept="computer-vision" chapterId={3} />

## Section 4: Signal Processing Basics for AI
[Content]
<InteractiveQuizBlock chapterId={3} numQuestions={5} />
```

**Validation Rules**:
- All 4 components MUST be imported
- All 4 components MUST be placed as specified in Feature 037
- All components MUST have chapterId={3}
- All components MUST have required props

---

### 2. Component Props (Sub-entity)

**Description**: Props passed to AI block components in Chapter 3

**AskQuestionBlock Props**:
```typescript
{
  chapterId: 3,
  sectionId: "what-is-perception-in-physical-ai"
}
```

**ExplainLike10Block Props**:
```typescript
{
  chapterId: 3,
  concept: "computer-vision"
}
```

**InteractiveQuizBlock Props**:
```typescript
{
  chapterId: 3,
  numQuestions: 5
}
```

**GenerateDiagramBlock Props**:
```typescript
{
  chapterId: 3,
  diagramType: "sensor-types"
}
```

---

### 3. Component Placement (Sub-entity)

**Description**: Placement of AI blocks within Chapter 3 sections

**Placement Map**:
- Section 1 (What Is Perception in Physical AI?): AskQuestionBlock at end
- Section 2 (Types of Sensors in Robotics): GenerateDiagramBlock in middle
- Section 3 (Computer Vision & Depth Perception): ExplainLike10Block in middle
- Section 4 (Signal Processing Basics for AI): InteractiveQuizBlock at end

**Validation Rules**:
- Placement MUST match Feature 037 specification exactly
- Components MUST replace HTML comment placeholders
- Components MUST be positioned logically within sections

---

## Relationships

- MDX File → Component Imports (1:N)
- MDX File → Component Usage (1:N)
- Component Usage → Component Props (1:1)
- Component Placement → Feature 037 Specification (1:1, derived from)

---

## Data Integrity Constraints

1. **Component Completeness**:
   - All 4 AI blocks MUST be integrated
   - No HTML comment placeholders should remain
   - All components MUST have required props

2. **Placement Consistency**:
   - Component placement MUST match Feature 037 exactly
   - Section IDs MUST match section anchors
   - Diagram types MUST match diagram placeholder names

3. **Props Validation**:
   - All required props MUST be provided
   - Props MUST use correct types (numbers vs strings)
   - chapterId MUST be 3 for all components

---

## Summary

All structures are frontend UI integration only. No backend changes required. Components render with placeholder UI until Feature 041 runtime integration.

