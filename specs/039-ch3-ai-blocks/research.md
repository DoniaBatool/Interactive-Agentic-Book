# Research: Chapter 3 AI Blocks Integration

**Feature**: 039-ch3-ai-blocks
**Date**: 2025-01-27
**Purpose**: Document AI block integration approach for Chapter 3

## Overview

This document captures research findings for integrating AI blocks into Chapter 3 MDX file. Research focuses on MDX component integration patterns, React component usage, prop configuration, and validation strategies.

## Technology Decisions

### 1. MDX Component Integration Pattern

**Decision**: Use explicit imports in MDX file (same as Chapter 1 and Chapter 2)

**Rationale**:
- **Consistency**: Maintains consistent pattern across all chapters
- **Reliability**: Explicit imports work reliably across Docusaurus versions
- **Clarity**: Clear dependencies for each MDX file

**Pattern**:
- Import statements at top of MDX file (after frontmatter)
- React components embedded in MDX content
- Props passed using JSX syntax

**Alternatives Considered**:
- **Global Registry**: May require swizzle in Docusaurus 3.x, less explicit
- **HTML Comments**: Not interactive, requires separate integration step

### 2. Component Prop Configuration

**Decision**: Use chapterId={3} for all components, with section-specific props

**Rationale**:
- **Context**: chapterId identifies Chapter 3 context for components
- **Routing**: Enables future runtime routing to Chapter 3 endpoints
- **Consistency**: Matches Chapter 1 and Chapter 2 patterns

**Props**:
- AskQuestionBlock: chapterId={3}, sectionId="what-is-perception-in-physical-ai"
- ExplainLike10Block: chapterId={3}, concept="computer-vision"
- InteractiveQuizBlock: chapterId={3}, numQuestions={5}
- GenerateDiagramBlock: chapterId={3}, diagramType="sensor-types"

### 3. Placement Strategy

**Decision**: Follow Feature 037 specification exactly

**Rationale**:
- **Pedagogical Alignment**: Feature 037 defines optimal placement for learning
- **Consistency**: Ensures consistent placement across chapters
- **Validation**: Easy to validate against specification

**Placement**:
- Section 1: Ask-question at end
- Section 2: Generate-diagram in middle
- Section 3: Explain-like-I-am-10 in middle
- Section 4: Interactive-quiz at end

### 4. Validation Strategy

**Decision**: Build validation + browser verification

**Rationale**:
- **Build Validation**: Catches TypeScript and MDX errors early
- **Browser Verification**: Ensures components render correctly
- **Comprehensive**: Covers both compilation and runtime

**Validation Steps**:
1. Run `npm run build` (catches compilation errors)
2. Run `npm start` and open Chapter 3 page (verifies rendering)
3. Interact with components (verifies placeholder UI)

---

## Component Integration Patterns

### Pattern 1: Import Statements

All MDX files follow same import pattern:
```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
```

### Pattern 2: Component Usage

Components embedded in MDX with JSX syntax:
```mdx
<ComponentName prop1={value1} prop2="value2" />
```

### Pattern 3: Prop Types

- Numbers: Use curly braces `{3}`
- Strings: Use quotes `"value"`
- Required props: Must be provided
- Optional props: Can be omitted

---

## References

- Feature 037: Chapter 3 Content Specification (placement rules)
- Feature 038: Chapter 3 MDX Implementation (MDX file with placeholders)
- Feature 004: Chapter 1 Interactive AI Blocks (component patterns)
- Feature 011/023: Chapter 2 AI Blocks (integration patterns)

---

## Summary

This research establishes:
- Explicit import pattern for MDX component integration
- chapterId={3} for all Chapter 3 components
- Feature 037 as authoritative source for placement
- Build + browser validation strategy

**Key Principles**:
- Frontend UI integration only—no backend changes
- Consistency with Chapter 1 and Chapter 2 patterns
- Feature 037 specification as authoritative source
- Ready for Feature 041 runtime integration

