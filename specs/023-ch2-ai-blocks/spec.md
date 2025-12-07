# Feature Specification: Chapter 2 — AI Block Rendering + MDX Integration

**Feature Branch**: `023-ch2-ai-blocks`
**Created**: 2025-01-27
**Status**: Draft
**Input**: User description: "Enable interactive AI blocks inside Chapter 2. This includes MDX placeholders, component mapping, AI-block insertion, and validating that Chapter 2 renders correctly with all blocks. sab kuch FAST kerna but in small batches not all at once"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learner Sees AI Blocks Rendered in Chapter 2 (Priority: P1)

As a learner reading Chapter 2, I want to see all 4 AI block components rendered correctly in their designated positions, so I can see where interactive features will be available and the UI foundation is ready.

**Why this priority**: This is the primary user-facing deliverable. Without visible components, learners cannot see where interactive features will be available. This establishes the UI foundation for future AI logic integration.

**Independent Test**: Can be fully tested by navigating to `/docs/chapters/chapter-2` in the Docusaurus frontend and verifying that all 4 AI block components render correctly in their designated locations.

**Acceptance Scenarios**:

1. **Given** the frontend is running, **When** I navigate to `/docs/chapters/chapter-2`, **Then** I see 4 interactive AI block components rendered where placeholders were designated
2. **Given** I am viewing the Ask Question block (after "Introduction to ROS 2" section), **When** I see the component, **Then** it displays with `chapterId={2}` and `sectionId="introduction-to-ros2"`
3. **Given** I am viewing the Generate Diagram block (after "Nodes and Node Communication" section), **When** I see the component, **Then** it displays with `diagramType="node-communication-architecture"` and `chapterId={2}`
4. **Given** I am viewing the Explain Like I'm 10 block (inside "Topics and Messages" section), **When** I see the component, **Then** it displays with `concept="topics"` and `chapterId={2}`
5. **Given** I am viewing the Interactive Quiz block (after "Services and Actions" section), **When** I see the component, **Then** it displays with `chapterId={2}` and `numQuestions={6}`
6. **Given** I run `npm run build` in the frontend directory, **When** the build completes, **Then** there are no compilation errors related to AI block components

---

### User Story 2 - Developer Verifies MDX Component Integration (Priority: P1)

As a developer, I need to verify that MDX component mapping correctly loads AI block components for Chapter 2, so I can ensure the integration between Docusaurus MDX and React components works properly.

**Why this priority**: Critical for ensuring the technical foundation is correct. Without proper MDX integration, components won't render at all, blocking all future development.

**Independent Test**: Can be fully tested by checking `frontend/src/mdx-components.ts` and verifying that AI block components are mapped correctly, then running Docusaurus build to confirm no compilation errors.

**Acceptance Scenarios**:

1. **Given** the MDX components file exists, **When** I open `frontend/src/mdx-components.ts`, **Then** I see all 4 AI block components exported: `AskQuestionBlock`, `ExplainLike10Block`, `InteractiveQuizBlock`, `GenerateDiagramBlock`
2. **Given** the Chapter 2 MDX file contains AI block components, **When** Docusaurus processes the MDX, **Then** it renders all components in their designated locations
3. **Given** I run `npm run build` in the frontend directory, **When** the build completes, **Then** there are no compilation errors related to AI block components
4. **Given** I check the Chapter 2 MDX file, **When** I review `frontend/docs/chapters/chapter-2.mdx`, **Then** I see all 4 components imported and used with correct props

---

### Edge Cases

- What happens when an AI block component receives invalid props for Chapter 2?
  - Components should handle missing or invalid props gracefully, using default values or showing an error message
- What happens when MDX file has malformed component syntax?
  - Docusaurus should still compile successfully, but components may not render (acceptable for this scaffolding phase)
- What happens when multiple AI blocks of the same type appear on the same Chapter 2 page?
  - Each component instance should work independently with its own state and Chapter 2 context
- What happens when component imports are missing or incorrect?
  - Docusaurus build should fail with clear error messages indicating missing imports

## Requirements *(mandatory)*

### Functional Requirements

#### Chapter 2 MDX File

- **FR-001**: System MUST ensure `frontend/docs/chapters/chapter-2.mdx` exists
- **FR-002**: System MUST insert the following AI block placeholders at correct pedagogical positions:
  - `<!-- AI-BLOCK: ask-question -->` - After "Introduction to ROS 2" section
  - `<!-- AI-BLOCK: explain-like-i-am-10 -->` - Inside "Topics and Messages" section
  - `<!-- AI-BLOCK: interactive-quiz -->` - After "Services and Actions" section
  - `<!-- AI-BLOCK: generate-diagram -->` - After "Nodes and Node Communication" section
- **FR-003**: System MUST replace placeholders with actual React components:
  - `<!-- AI-BLOCK: ask-question -->` → `<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />`
  - `<!-- AI-BLOCK: explain-like-i-am-10 -->` → `<ExplainLike10Block concept="topics" chapterId={2} />`
  - `<!-- AI-BLOCK: interactive-quiz -->` → `<InteractiveQuizBlock chapterId={2} numQuestions={6} />`
  - `<!-- AI-BLOCK: generate-diagram -->` → `<GenerateDiagramBlock diagramType="node-communication-architecture" chapterId={2} />`
- **FR-004**: System MUST add import statements at top of chapter-2.mdx:
  - `import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';`
  - `import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';`
  - `import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';`
  - `import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';`
- **FR-005**: Exact content values (sectionId, concept, diagramType) MAY remain TODO placeholders if not yet determined

#### Component Mapping

- **FR-006**: System MUST ensure `frontend/src/mdx-components.ts` exports all 4 AI block components:
  - `AskQuestionBlock`
  - `ExplainLike10Block`
  - `InteractiveQuizBlock`
  - `GenerateDiagramBlock`
- **FR-007**: System MUST ensure mapping includes Chapter 2 usage (components work with chapterId=2)
- **FR-008**: Component mapping MUST allow components to be used directly in MDX without additional configuration

#### MDX Rendering Layer

- **FR-009**: System MUST ensure Chapter 2 MDX file uses actual React components (not just HTML comments)
- **FR-010**: System MUST ensure all components receive correct props:
  - `chapterId={2}` for all components
  - Appropriate `sectionId`, `concept`, `diagramType`, `numQuestions` as specified
- **FR-011**: System MUST ensure Docusaurus can compile and render the MDX file with AI block components

#### Build Validation

- **FR-012**: System MUST run Docusaurus build validation (placeholder command: `npm run build`)
- **FR-013**: System MUST ensure all imports resolve correctly
- **FR-014**: System MUST ensure no TypeScript compilation errors
- **FR-015**: System MUST ensure no missing component errors

#### Documentation Contract

- **FR-016**: System MUST create `specs/023-ch2-ai-blocks/contracts/ai-block-mdx.yaml` documenting:
  - Block names (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
  - MDX usage patterns
  - Component interface (props, chapterId, sectionId, concept, diagramType, numQuestions)

### Assumptions

- **Assumption 1**: AI block React components already exist from Feature 004 (Chapter 1 AI blocks)
- **Assumption 2**: Chapter 2 MDX file exists (from Feature 010 or 014)
- **Assumption 3**: Docusaurus MDX component mapping already configured (from Feature 004)
- **Assumption 4**: No new AI logic needs to be implemented (only MDX integration and rendering)
- **Assumption 5**: Component props values (sectionId, concept, diagramType) may use TODO placeholders if exact values not yet determined

### Key Entities

**Chapter 2 AI Block Component**:
- Component name (e.g., "AskQuestionBlock")
- Props interface (chapterId=2, sectionId, concept, diagramType, numQuestions)
- MDX usage (import statement + component call)
- Rendering location (pedagogical position in chapter)

**MDX Component Mapping**:
- File: `frontend/src/mdx-components.ts`
- Exported components: AskQuestionBlock, ExplainLike10Block, InteractiveQuizBlock, GenerateDiagramBlock
- Usage: Direct component calls in MDX

## Success Criteria *(mandatory)*

- **SC-001**: Chapter 2 MDX renders with all 4 AI blocks at designated positions
- **SC-002**: Frontend build passes without errors (`npm run build`)
- **SC-003**: Components imported correctly in chapter-2.mdx
- **SC-004**: All components receive correct props (chapterId=2, appropriate sectionId/concept/diagramType)
- **SC-005**: No real AI logic added (only MDX integration and rendering scaffolding)
- **SC-006**: MDX component mapping includes all 4 AI block components
- **SC-007**: Docusaurus can compile and render Chapter 2 with AI blocks

## Constraints *(mandatory)*

- **Constraint 1**: Must reuse existing AI block components from Feature 004 (no new component creation)
- **Constraint 2**: Must not implement real AI logic (only MDX integration and rendering)
- **Constraint 3**: Must not break existing Chapter 1 AI block functionality
- **Constraint 4**: Must follow same patterns used in Chapter 1 AI blocks integration
- **Constraint 5**: Must work with existing Docusaurus MDX configuration

## Dependencies *(mandatory)*

- **Dependency 1**: Feature 004 (Chapter 1 Interactive AI Blocks) - Required for existing components and MDX mapping patterns
- **Dependency 2**: Feature 010 or 014 (Chapter 2 Content) - Required for Chapter 2 MDX file existence
- **Dependency 3**: Docusaurus MDX Configuration - Required for component rendering

## Out of Scope

- ❌ Implementing real AI logic for Chapter 2
- ❌ Creating new AI block components
- ❌ Backend API integration
- ❌ RAG pipeline integration
- ❌ Runtime engine updates
- ❌ Subagent modifications
- ❌ Implementing diagram generation logic
- ❌ Creating quiz question generation logic
- ❌ Adding authentication or personalization

