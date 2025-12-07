# Feature Specification: Chapter 3 — AI Blocks Integration

**Feature Branch**: `039-ch3-ai-blocks`
**Created**: 2025-01-27
**Status**: Draft
**Type**: frontend-integration
**Input**: User description: "Insert all AI-interactive blocks inside the Chapter 3 MDX file at the correct pedagogically aligned positions. Follow the same structural rules used in Chapters 1 and 2. Ensure components compile, paths resolve, and UI renders."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learner Interacts with Chapter 3 AI Blocks (Priority: P1)

As a learner, I want to see and interact with AI blocks in Chapter 3, so I can ask questions, get simplified explanations, take quizzes, and generate diagrams related to Physical AI Perception Systems.

**Why this priority**: This is the primary user-facing deliverable. Without AI blocks integrated, learners cannot interact with Chapter 3 content, reducing engagement and learning effectiveness.

**Independent Test**: Can be fully tested by navigating to `/docs/chapters/chapter-3` in the Docusaurus frontend and verifying all 4 AI blocks render visually with placeholder UI.

**Acceptance Scenarios**:

1. **Given** the frontend is running, **When** I navigate to `/docs/chapters/chapter-3`, **Then** I see all 4 AI blocks rendered in their correct positions
2. **Given** I am viewing Section 1, **When** I scroll to the end, **Then** I see AskQuestionBlock component rendered
3. **Given** I am viewing Section 2, **When** I scroll to the middle, **Then** I see GenerateDiagramBlock component rendered
4. **Given** I am viewing Section 3, **When** I scroll to the middle, **Then** I see ExplainLike10Block component rendered
5. **Given** I am viewing Section 4, **When** I scroll to the end, **Then** I see InteractiveQuizBlock component rendered
6. **Given** I interact with any AI block, **When** I click buttons or input fields, **Then** I see placeholder UI responses (no real API calls)

---

### User Story 2 - Developer Verifies Component Integration (Priority: P2)

As a developer, I want to verify that all AI block components are correctly integrated into Chapter 3 MDX file, so I can ensure the frontend compiles cleanly and components are ready for runtime integration.

**Why this priority**: Ensures frontend integration is complete and ready for backend runtime integration in future features.

**Independent Test**: Can be fully tested by running `npm run build` and verifying no TypeScript or MDX compilation errors.

**Acceptance Scenarios**:

1. **Given** the MDX file is updated, **When** I run `npm run build`, **Then** the build completes without errors
2. **Given** the MDX file is updated, **When** I check for TypeScript errors, **Then** there are no import or component prop errors
3. **Given** the MDX file is updated, **When** I verify component imports, **Then** all 4 components are imported from correct paths
4. **Given** the MDX file is updated, **When** I verify component usage, **Then** all components have correct props (chapterId={3}, sectionId, concept, diagramType)

---

### Edge Cases

- What happens when a component import path is incorrect?
  - **Expected**: TypeScript/Docusaurus build fails with clear error message about missing module
- What happens when a component prop is missing or incorrect?
  - **Expected**: TypeScript compilation error or runtime warning about missing required props
- What happens when mdx-components.ts doesn't export a component?
  - **Expected**: Component may not render, but explicit imports in MDX file should work
- What happens when Docusaurus build fails?
  - **Expected**: Build output shows specific error about MDX syntax or component issues

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: MDX Component Injection

- **FR-001.1**: System MUST modify `frontend/docs/chapters/chapter-3.mdx` to replace HTML comment placeholders with React component calls
- **FR-001.2**: System MUST add import statements at top of chapter-3.mdx (after frontmatter):
  - `import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';`
  - `import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';`
  - `import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';`
  - `import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';`

- **FR-001.3**: System MUST replace placeholder comments with component calls:
  - `<!-- AI-BLOCK: ask-question -->` → `<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />`
  - `<!-- AI-BLOCK: explain-like-i-am-10 -->` → `<ExplainLike10Block concept="computer-vision" chapterId={3} />`
  - `<!-- AI-BLOCK: interactive-quiz -->` → `<InteractiveQuizBlock chapterId={3} numQuestions={5} />`
  - `<!-- AI-BLOCK: generate-diagram -->` → `<GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />`

#### FR-002: AI Block Placement Rules

- **FR-002.1**: System MUST position AI blocks EXACTLY as defined in Feature 037 specification:
  - **Ask-question**: Section 1 (What Is Perception in Physical AI?) at the end, sectionId="what-is-perception-in-physical-ai"
  - **Generate-diagram**: Section 2 (Types of Sensors in Robotics) in the middle, diagramType="sensor-types"
  - **Explain-like-I-am-10**: Section 3 (Computer Vision & Depth Perception) in the middle, concept="computer-vision"
  - **Quiz**: Section 4 (Signal Processing Basics for AI) at the end, numQuestions={5}

- **FR-002.2**: System MUST ensure component props match Feature 037 specification:
  - All components MUST have `chapterId={3}`
  - AskQuestionBlock MUST have `sectionId` prop matching section anchor
  - ExplainLike10Block MUST have `concept` prop
  - GenerateDiagramBlock MUST have `diagramType` prop matching diagram placeholder name
  - InteractiveQuizBlock MUST have `numQuestions` prop

#### FR-003: MDX Component Registry

- **FR-003.1**: System MUST ensure components are exported in `frontend/src/mdx-components.ts`:
  - AskQuestionBlock
  - ExplainLike10Block
  - InteractiveQuizBlock
  - GenerateDiagramBlock

- **FR-003.2**: System MUST verify registry file exists and exports all 4 components (or use explicit imports in MDX)

#### FR-004: Local Verification

- **FR-004.1**: Docusaurus MUST compile cleanly: `npm run build` completes without errors
- **FR-004.2**: Visiting Chapter 3 page MUST render all components with placeholder UI
- **FR-004.3**: No real AI calls should occur (components show placeholder UI only)

#### FR-005: No Runtime Logic

- **FR-005.1**: System MUST NOT add backend AI runtime integration (Feature 041 scope)
- **FR-005.2**: System MUST NOT modify Chapter 1 or Chapter 2 MDX files
- **FR-005.3**: System MUST NOT modify RAG or runtime engine files
- **FR-005.4**: Only frontend UI component placement (no backend changes)

---

## Non-Functional Requirements

- **NFR-001**: All components MUST follow Chapter 1 and Chapter 2 integration patterns
- **NFR-002**: Component props MUST match TypeScript interfaces exactly
- **NFR-003**: Import paths MUST use `@site/src/components/ai/` prefix
- **NFR-004**: No TypeScript errors or warnings
- **NFR-005**: No MDX compilation errors

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All AI blocks appear visually in Chapter 3
- **SC-002**: No TypeScript errors
- **SC-003**: Correct ordering of components (matches Feature 037)
- **SC-004**: No missing imports
- **SC-005**: Build runs without warnings
- **SC-006**: Components render with placeholder UI (no API calls)

---

## Constraints *(mandatory)*

### Technical Constraints

- **C-001**: MUST use React components (not HTML comments)
- **C-002**: MUST follow Chapter 1 and Chapter 2 component integration patterns
- **C-003**: MUST NOT modify backend files
- **C-004**: MUST NOT add real AI runtime logic
- **C-005**: MUST NOT modify Chapter 1 or Chapter 2 MDX files

### Process Constraints

- **C-006**: MUST follow Feature 037 specification exactly for placement
- **C-007**: MUST ensure all component props are correct
- **C-008**: MUST verify build succeeds before marking complete

### Scope Constraints (Out of Scope)

- **OOS-001**: Backend AI runtime integration (Feature 041)
- **OOS-002**: RAG pipeline integration
- **OOS-003**: Real API calls or AI logic
- **OOS-004**: Content writing
- **OOS-005**: Diagram generation

---

## Dependencies *(mandatory)*

### Internal Dependencies

- **D-001**: Feature 001 (Base Project Initialization) MUST be complete
- **D-002**: Feature 037 (Chapter 3 Content Specification) MUST be complete - Source for placement rules
- **D-003**: Feature 038 (Chapter 3 MDX Implementation) MUST be complete - MDX file with placeholders exists
- **D-004**: Feature 004 (Chapter 1 Interactive AI Blocks) MUST be complete - Components exist
- **D-005**: AI block components MUST exist in `frontend/src/components/ai/`

### External Dependencies

- **D-006**: Docusaurus 3.x (already installed)
- **D-007**: React components (already installed)

### Blocking Issues

- None identified. All dependencies resolved.

### Assumptions

- **A-001**: AI block components exist and are functional
- **A-002**: mdx-components.ts registry exists (or explicit imports work)
- **A-003**: Chapter 3 MDX file has HTML comment placeholders ready for replacement

---

## Implementation Notes *(optional guidance)*

### Recommended Implementation Order

1. **Phase 1: Add Component Imports**
   - Add import statements to chapter-3.mdx
   - Verify import paths are correct

2. **Phase 2: Replace Placeholders**
   - Replace ask-question placeholder with AskQuestionBlock
   - Replace generate-diagram placeholder with GenerateDiagramBlock
   - Replace explain-like-i-am-10 placeholder with ExplainLike10Block
   - Replace interactive-quiz placeholder with InteractiveQuizBlock

3. **Phase 3: Verify Registry**
   - Check mdx-components.ts exports all components
   - Verify components are accessible

4. **Phase 4: Validation**
   - Run `npm run build`
   - Fix any TypeScript or MDX errors
   - Verify components render in browser

---

**Next Steps**: Proceed to `/sp.plan` to create architectural plan for AI blocks integration.

