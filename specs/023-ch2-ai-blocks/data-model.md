# Data Model: Chapter 2 AI Block Rendering + MDX Integration

**Feature**: 023-ch2-ai-blocks
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 2 AI blocks MDX integration

## Overview

This document defines the data structures, entities, and relationships for integrating AI-interactive blocks into Chapter 2 MDX file. All structures reuse patterns from Chapter 1 but include Chapter 2-specific context (chapterId=2, ROS 2 concepts, section IDs).

---

## Entities

### 1. Chapter 2 AI Block Component

**Storage**: React component instances in `frontend/docs/chapters/chapter-2.mdx`

**Structure**:
```typescript
interface Chapter2AIBlockProps {
  chapterId: 2;                    // Fixed: Chapter 2
  sectionId?: string;              // Optional: "introduction-to-ros2", "nodes-and-node-communication", etc.
  concept?: string;                // Optional: "topics", "nodes", "services", "actions"
  diagramType?: string;            // Optional: "node-communication-architecture", etc.
  numQuestions?: number;           // Optional: Default 6
}
```

**Component Types**:
- `AskQuestionBlock` - Props: `{ chapterId: 2, sectionId: string }`
- `ExplainLike10Block` - Props: `{ concept: string, chapterId: 2 }`
- `InteractiveQuizBlock` - Props: `{ chapterId: 2, numQuestions: number }`
- `GenerateDiagramBlock` - Props: `{ diagramType: string, chapterId: 2 }`

**Validation**:
- `chapterId` must be 2
- `sectionId` must match section anchors from chapter-2.mdx (kebab-case)
- `concept` must be valid ROS 2 concept (topics, nodes, services, actions, packages, launch-files)
- `diagramType` must match diagram placeholders from chapter-2.mdx

**Relationship**: N:1 with Chapter 2 MDX Content (4 instances in chapter-2.mdx)

---

### 2. MDX Component Import

**Storage**: Import statements at top of `frontend/docs/chapters/chapter-2.mdx`

**Structure**:
```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
```

**Attributes**:
- **Import Path**: `@site/src/components/ai/{ComponentName}`
- **Component Name**: PascalCase (AskQuestionBlock, etc.)
- **Location**: After frontmatter, before content

**Validation Rules**:
- All 4 imports MUST be present
- Import paths MUST use `@site/src/components/ai/` prefix
- Component names MUST match exported names exactly

**Relationship**: 1:1 with Chapter 2 MDX File

---

### 3. MDX Component Mapping

**Storage**: TypeScript file `frontend/src/mdx-components.ts`

**Structure**:
```typescript
export default {
  AskQuestionBlock,
  ExplainLike10Block,
  InteractiveQuizBlock,
  GenerateDiagramBlock,
};
```

**Attributes**:
- **Export Names**: PascalCase component names
- **Source**: Components imported from `@site/src/components/ai/`
- **Usage**: Allows components to be used in MDX without explicit imports (if configured)

**Validation Rules**:
- All 4 components MUST be exported
- Export names MUST match component names exactly
- Components MUST be importable

**Relationship**: N:1 with AI Block Components (maps all 4 components)

---

### 4. Chapter 2 Section Anchor

**Storage**: H2 headings in `frontend/docs/chapters/chapter-2.mdx`

**Structure**:
```markdown
## Section Title {#section-anchor-id}
```

**Chapter 2 Sections** (relevant for AI blocks):
1. `introduction-to-ros2` - Introduction to ROS 2
2. `nodes-and-node-communication` - Nodes and Node Communication
3. `topics-and-messages` - Topics and Messages
4. `services-and-actions` - Services and Actions

**Attributes**:
- **Anchor ID**: Kebab-case identifier (e.g., "introduction-to-ros2")
- **Section Title**: Human-readable heading
- **Location**: H2 heading with anchor ID

**Validation Rules**:
- Anchor IDs MUST be kebab-case (lowercase, hyphens only)
- Anchor IDs MUST match sectionId props in AI block components
- Sections MUST exist in chapter-2.mdx

**Relationship**: 1:N with AI Block Components (one section can have multiple AI blocks)

---

### 5. Chapter 2 Diagram Placeholder

**Storage**: HTML comments in `frontend/docs/chapters/chapter-2.mdx`

**Structure**:
```html
<!-- DIAGRAM: diagram-type-name -->
```

**Chapter 2 Diagram Types** (relevant for AI blocks):
1. `node-communication-architecture` - Node communication diagram
2. `ros2-ecosystem-overview` - ROS 2 ecosystem overview
3. `topic-pubsub-flow` - Topic publish/subscribe flow
4. `services-actions-comparison` - Services vs actions comparison

**Attributes**:
- **Diagram Type**: Kebab-case identifier (e.g., "node-communication-architecture")
- **Format**: HTML comment `<!-- DIAGRAM: {name} -->`
- **Location**: Within relevant sections

**Validation Rules**:
- Diagram types MUST be kebab-case
- Diagram types MUST match diagramType props in GenerateDiagramBlock
- Diagram placeholders MUST exist in chapter-2.mdx

**Relationship**: 1:1 with GenerateDiagramBlock (one diagram type per block)

---

## Relationships

### Component to MDX File
- **Type**: N:1 (4 components in 1 MDX file)
- **Storage**: Components embedded in `frontend/docs/chapters/chapter-2.mdx`
- **Props**: All components receive `chapterId={2}`

### Component to Section
- **Type**: N:1 (multiple components can reference same section)
- **Storage**: `sectionId` prop in AskQuestionBlock
- **Validation**: sectionId must match section anchor IDs

### Component to Concept
- **Type**: N:1 (multiple components can reference same concept)
- **Storage**: `concept` prop in ExplainLike10Block
- **Validation**: concept must be valid ROS 2 concept

### Component to Diagram Type
- **Type**: 1:1 (one component per diagram type)
- **Storage**: `diagramType` prop in GenerateDiagramBlock
- **Validation**: diagramType must match diagram placeholder names

### Import to Component
- **Type**: 1:1 (one import per component)
- **Storage**: Import statements in chapter-2.mdx
- **Validation**: Import paths must resolve correctly

---

## Data Flow

### MDX Rendering Flow

1. **Docusaurus reads** `frontend/docs/chapters/chapter-2.mdx`
2. **MDX processor parses** import statements
3. **Components are resolved** via `frontend/src/mdx-components.ts` or direct imports
4. **React components render** with provided props
5. **Components display** in designated positions in chapter

### Component Props Flow

1. **Props defined** in MDX: `<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />`
2. **Props passed** to React component
3. **Component receives** props via TypeScript interface
4. **Component uses** props for rendering and context (future: API calls)

---

## Validation Rules Summary

### Component Props
- `chapterId` MUST be 2 for all Chapter 2 components
- `sectionId` MUST match section anchor IDs (kebab-case)
- `concept` MUST be valid ROS 2 concept
- `diagramType` MUST match diagram placeholder names (kebab-case)
- `numQuestions` MUST be positive integer (1-20 recommended)

### Import Statements
- All 4 components MUST be imported
- Import paths MUST use `@site/src/components/ai/` prefix
- Component names MUST match exported names exactly

### Component Placement
- Components MUST be placed at designated pedagogical positions
- Components MUST not break MDX document structure
- Components MUST be properly closed (self-closing or paired tags)

---

## Notes

- This data model focuses on MDX integration only (no backend data structures)
- All components reuse existing implementations from Feature 004
- Chapter 2 context (chapterId=2) is required for all components
- Props values may use TODO placeholders if exact values not yet determined

