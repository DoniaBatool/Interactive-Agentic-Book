# Feature Specification: Chapter 3 — AI Blocks Integration Layer

**Feature Branch**: `028-ch3-ai-blocks`
**Created**: 2025-01-27
**Status**: Draft
**Type**: frontend-integration
**Input**: User description: "Connect all Chapter 3 interactive blocks (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram) into the MDX content file and prepare all scaffolding required for future AI logic. No AI behavior must be added."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learner Sees AI Blocks Rendered in Chapter 3 (Priority: P1)

As a learner reading Chapter 3, I want to see all 4 AI block components rendered correctly in their designated positions, so I can see where interactive features will be available and the UI foundation is ready.

**Why this priority**: This is the primary user-facing deliverable. Without visible components, learners cannot see where interactive features will be available. This establishes the UI foundation for future AI logic integration.

**Independent Test**: Can be fully tested by navigating to `/docs/chapters/chapter-3` in the Docusaurus frontend and verifying that all 4 AI block components render correctly in their designated locations.

**Acceptance Scenarios**:

1. **Given** the frontend is running, **When** I navigate to `/docs/chapters/chapter-3`, **Then** I see 4 interactive AI block components rendered where placeholders were designated
2. **Given** I am viewing the Ask Question block (after "What Is Perception in Physical AI?" section), **When** I see the component, **Then** it displays with `chapterId={3}` and `sectionId="what-is-perception-in-physical-ai"`
3. **Given** I am viewing the Generate Diagram block (after "Types of Sensors in Robotics" section), **When** I see the component, **Then** it displays with `diagramType="sensor-types"` and `chapterId={3}`
4. **Given** I am viewing the Explain Like I'm 10 block (inside "Computer Vision & Depth Perception" section), **When** I see the component, **Then** it displays with `concept="computer-vision"` and `chapterId={3}`
5. **Given** I am viewing the Interactive Quiz block (after "Signal Processing Basics for AI" section), **When** I see the component, **Then** it displays with `chapterId={3}` and `numQuestions={5}`
6. **Given** I run `npm run build` in the frontend directory, **When** the build completes, **Then** there are no compilation errors related to AI block components

---

### User Story 2 - Developer Verifies MDX Component Integration (Priority: P1)

As a developer, I need to verify that MDX component mapping correctly loads AI block components for Chapter 3, so I can ensure the integration between Docusaurus MDX and React components works properly.

**Why this priority**: Critical for ensuring the technical foundation is correct. Without proper MDX integration, components won't render at all, blocking all future development.

**Independent Test**: Can be fully tested by checking `frontend/src/mdx-components.ts` and verifying that AI block components are mapped correctly, then running Docusaurus build to confirm no compilation errors.

**Acceptance Scenarios**:

1. **Given** the MDX components file exists, **When** I open `frontend/src/mdx-components.ts`, **Then** I see all 4 AI block components exported: `AskQuestionBlock`, `ExplainLike10Block`, `InteractiveQuizBlock`, `GenerateDiagramBlock`
2. **Given** the Chapter 3 MDX file contains AI block components, **When** Docusaurus processes the MDX, **Then** it renders all components in their designated locations
3. **Given** I run `npm run build` in the frontend directory, **When** the build completes, **Then** there are no compilation errors related to AI block components
4. **Given** I check the Chapter 3 MDX file, **When** I review `frontend/docs/chapters/chapter-3.mdx`, **Then** I see all 4 components imported and used with correct props

---

### Edge Cases

- What happens when an AI block component receives invalid props for Chapter 3?
  - Components should handle missing or invalid props gracefully, using default values or showing an error message
- What happens when MDX file has malformed component syntax?
  - Docusaurus should still compile successfully, but components may not render (acceptable for this scaffolding phase)
- What happens when multiple AI blocks of the same type appear on the same Chapter 3 page?
  - Each component instance should work independently with its own state and Chapter 3 context
- What happens when component imports are missing or incorrect?
  - Docusaurus build should fail with clear error messages indicating missing imports

## Requirements *(mandatory)*

### Functional Requirements

#### Chapter 3 MDX File

- **FR-001**: System MUST ensure `frontend/docs/chapters/chapter-3.mdx` exists
- **FR-002**: System MUST replace AI block placeholders with actual React components:
  - `<!-- AI-BLOCK: ask-question -->` → `<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />`
  - `<!-- AI-BLOCK: explain-like-i-am-10 -->` → `<ExplainLike10Block concept="computer-vision" chapterId={3} />`
  - `<!-- AI-BLOCK: interactive-quiz -->` → `<InteractiveQuizBlock chapterId={3} numQuestions={5} />`
  - `<!-- AI-BLOCK: generate-diagram -->` → `<GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />`
- **FR-003**: System MUST add import statements at top of chapter-3.mdx (after frontmatter):
  - `import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';`
  - `import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';`
  - `import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';`
  - `import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';`
- **FR-004**: System MUST ensure frontmatter follows content-schema.md contract:
  - `title`: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
  - `description`: SEO-optimized summary (150-160 chars)
  - `sidebar_position`: 3
  - `sidebar_label`: "Chapter 3: Physical AI Perception Systems"
  - `tags`: ["physical-ai", "sensors", "perception", "signal-processing"]
- **FR-005**: System MUST ensure all AI block components use `chapterId={3}`

#### Component Mapping

- **FR-006**: System MUST ensure `frontend/src/mdx-components.ts` exports all 4 AI block components:
  - `AskQuestionBlock`
  - `ExplainLike10Block`
  - `InteractiveQuizBlock`
  - `GenerateDiagramBlock`
- **FR-007**: System MUST ensure mapping includes Chapter 3 usage (components work with chapterId=3)
- **FR-008**: Component mapping MUST allow components to be used directly in MDX without additional configuration

#### MDX Rendering Layer

- **FR-009**: System MUST ensure Chapter 3 MDX file uses actual React components (not just HTML comments)
- **FR-010**: System MUST ensure all components receive correct props:
  - `chapterId={3}` for all components
  - Appropriate `sectionId`, `concept`, `diagramType`, `numQuestions` as specified
- **FR-011**: System MUST ensure Docusaurus can compile and render the MDX file with AI block components

#### Backend Metadata

- **FR-012**: System MUST ensure `backend/app/content/chapters/chapter_3.py` exists and contains:
  - `id`: 3
  - `title`: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
  - `sections`: List of 7 section titles matching MDX
  - `ai_blocks`: ["ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram"]
  - `diagram_placeholders`: ["perception-overview", "sensor-types", "cv-depth-flow", "feature-extraction-pipeline"]
- **FR-013**: System MUST ensure metadata matches MDX structure exactly

#### RAG Preparation

- **FR-014**: System MUST ensure Chapter 3 MDX contains `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` markers for RAG chunking boundaries
- **FR-015**: System MUST create `backend/app/content/chapters/chapter_3_chunks.py` with placeholder function:
  - `get_chapter3_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]`
  - Function contains TODO comments only (no real implementation)

#### Build Validation

- **FR-016**: System MUST run Docusaurus build validation (placeholder command: `npm run build`)
- **FR-017**: System MUST ensure all imports resolve correctly
- **FR-018**: System MUST ensure no TypeScript compilation errors
- **FR-019**: System MUST ensure no missing component errors

#### Documentation Contract

- **FR-020**: System MUST create `specs/028-ch3-ai-blocks/contracts/ch3-content-contract.yaml` documenting:
  - Block names (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
  - MDX usage patterns
  - Component interface (props, chapterId, sectionId, concept, diagramType, numQuestions)
  - Frontmatter schema requirements
  - RAG chunking markers

### Assumptions

- **Assumption 1**: AI block React components already exist from Feature 004 (Chapter 1 AI blocks)
- **Assumption 2**: Chapter 3 MDX file exists (from Feature 017 or 018)
- **Assumption 3**: Docusaurus MDX component mapping already configured (from Feature 004)
- **Assumption 4**: No new AI logic needs to be implemented (only MDX integration and rendering)
- **Assumption 5**: Component props values (sectionId, concept, diagramType) match Chapter 3 metadata

### Key Entities

**Chapter 3 AI Block Component**:
- Component name (e.g., "AskQuestionBlock")
- Props interface (chapterId=3, sectionId, concept, diagramType, numQuestions)
- MDX usage (import statement + component call)
- Rendering location (pedagogical position in chapter)

**MDX Component Mapping**:
- File: `frontend/src/mdx-components.ts`
- Exported components: AskQuestionBlock, ExplainLike10Block, InteractiveQuizBlock, GenerateDiagramBlock
- Usage: Direct component calls in MDX

**Chapter 3 Metadata**:
- File: `backend/app/content/chapters/chapter_3.py`
- Structure: Dictionary with id, title, sections, ai_blocks, diagram_placeholders
- Relationship: 1:1 with Chapter 3 MDX content

## Success Criteria *(mandatory)*

- **SC-001**: Chapter 3 MDX renders with all 4 AI blocks at designated positions
- **SC-002**: Frontend build passes without errors (`npm run build`)
- **SC-003**: Components imported correctly in chapter-3.mdx
- **SC-004**: All components receive correct props (chapterId=3, appropriate sectionId/concept/diagramType)
- **SC-005**: No real AI logic added (only MDX integration and rendering scaffolding)
- **SC-006**: MDX component mapping includes all 4 AI block components
- **SC-007**: Docusaurus can compile and render Chapter 3 with AI blocks
- **SC-008**: Backend metadata file exists and matches MDX structure
- **SC-009**: RAG chunking markers present in MDX
- **SC-010**: Chapter 3 chunks file created with placeholder function

## Constraints *(mandatory)*

- **Constraint 1**: Must reuse existing AI block components from Feature 004 (no new component creation)
- **Constraint 2**: Must not implement real AI logic (only MDX integration and rendering)
- **Constraint 3**: Must not break existing Chapter 1 or Chapter 2 AI block functionality
- **Constraint 4**: Must follow same patterns used in Chapter 1 and Chapter 2 AI blocks integration
- **Constraint 5**: Must work with existing Docusaurus MDX configuration
- **Constraint 6**: Must ensure Chapter 3 appears in sidebar after Chapter 2 (sidebar_position: 3)

## Dependencies

- **Feature 004**: Chapter 1 AI Blocks (provides React components)
- **Feature 017 or 018**: Chapter 3 Content (provides MDX file structure)
- **Feature 023**: Chapter 2 AI Blocks (reference for integration patterns)

## Out of Scope

- Writing actual Chapter 3 content (content placeholders remain)
- Implementing AI logic for quiz generation, question answering, explanations, or diagrams
- Creating new React components (reuses existing components)
- Implementing RAG pipeline for Chapter 3 (only placeholder chunks file)
- Backend runtime logic for Chapter 3 AI blocks (future feature)

