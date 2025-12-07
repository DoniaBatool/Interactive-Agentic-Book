# Tasks: Chapter 3 — AI Blocks Integration

**Feature**: 039-ch3-ai-blocks | **Branch**: `039-ch3-ai-blocks` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for integrating AI blocks into Chapter 3 MDX file. All tasks are frontend UI integration only—no backend changes.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category`: SETUP (Initial setup), FRONTEND (MDX updates), REGISTRY (Registry verification), VALIDATION (Validation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prepare for implementation.

- [ ] [T001] [P1] [SETUP] Verify Feature 037 (Chapter 3 Content Specification) is complete: Check that specification exists with AI block placement rules
- [ ] [T002] [P1] [SETUP] Verify Feature 038 (Chapter 3 MDX Implementation) is complete: Check that chapter-3.mdx exists with HTML comment placeholders
- [ ] [T003] [P1] [SETUP] Verify Feature 004 (Chapter 1 Interactive AI Blocks) is complete: Check that AI block components exist in frontend/src/components/ai/
- [ ] [T004] [P1] [SETUP] Verify Docusaurus frontend is functional: Check that `npm run build` works in frontend directory
- [ ] [T005] [P1] [SETUP] Verify mdx-components.ts exists: Check that frontend/src/mdx-components.ts exists and exports components

**Success Criteria**:
- All prerequisite features complete
- Frontend environment ready
- Components available

**Dependencies**: Feature 037, Feature 038, Feature 004 must be complete

---

## PHASE 1 — FRONTEND: MDX UPDATE

**User Story**: US1 - Learner Interacts with Chapter 3 AI Blocks

**Test Strategy**: Can be tested by verifying MDX file has component imports and all placeholders are replaced with React components.

### Add Component Imports

- [ ] [T006] [P1] [FRONTEND] Locate `frontend/docs/chapters/chapter-3.mdx`: Open file in editor

- [ ] [T007] [P1] [FRONTEND] Add component imports to `frontend/docs/chapters/chapter-3.mdx`:
  - Add import: `import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';`
  - Add import: `import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';`
  - Add import: `import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';`
  - Add import: `import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';`
  - Place imports after frontmatter, before content

### Replace Placeholders with Components

- [ ] [T008] [P1] [FRONTEND] Identify all `<!-- AI-BLOCK: ... -->` placeholders in `frontend/docs/chapters/chapter-3.mdx`:
  - Find: `<!-- AI-BLOCK: ask-question -->` (Section 1, end)
  - Find: `<!-- AI-BLOCK: generate-diagram -->` (Section 2, middle)
  - Find: `<!-- AI-BLOCK: explain-like-i-am-10 -->` (Section 3, middle)
  - Find: `<!-- AI-BLOCK: interactive-quiz -->` (Section 4, end)

- [ ] [T009] [P1] [FRONTEND] Replace ask-question placeholder in `frontend/docs/chapters/chapter-3.mdx`:
  - Find: `<!-- AI-BLOCK: ask-question -->` (Section 1, end)
  - Replace with: `<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />`

- [ ] [T010] [P1] [FRONTEND] Replace generate-diagram placeholder in `frontend/docs/chapters/chapter-3.mdx`:
  - Find: `<!-- AI-BLOCK: generate-diagram -->` (Section 2, middle)
  - Replace with: `<GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />`

- [ ] [T011] [P1] [FRONTEND] Replace explain-like-i-am-10 placeholder in `frontend/docs/chapters/chapter-3.mdx`:
  - Find: `<!-- AI-BLOCK: explain-like-i-am-10 -->` (Section 3, middle)
  - Replace with: `<ExplainLike10Block concept="computer-vision" chapterId={3} />`

- [ ] [T012] [P1] [FRONTEND] Replace interactive-quiz placeholder in `frontend/docs/chapters/chapter-3.mdx`:
  - Find: `<!-- AI-BLOCK: interactive-quiz -->` (Section 4, end)
  - Replace with: `<InteractiveQuizBlock chapterId={3} numQuestions={5} />`

**Acceptance Test**: All 4 HTML comment placeholders replaced with React components, all components have correct props (chapterId={3}, sectionId, concept, diagramType, numQuestions)

---

## PHASE 2 — FRONTEND: REGISTRY FILE

**User Story**: US2 - Developer Verifies Component Integration

**Test Strategy**: Can be tested by verifying mdx-components.ts exports all components or explicit imports work.

### Verify Component Registry

- [ ] [T013] [P2] [REGISTRY] Open `frontend/src/mdx-components.ts`: Check file exists

- [ ] [T014] [P2] [REGISTRY] Verify exports in `frontend/src/mdx-components.ts`:
  - Verify AskQuestionBlock is exported
  - Verify ExplainLike10Block is exported
  - Verify InteractiveQuizBlock is exported
  - Verify GenerateDiagramBlock is exported
  - Note: Explicit imports in MDX also work if registry is not used

- [ ] [T015] [P2] [REGISTRY] Verify import paths in `frontend/src/mdx-components.ts`:
  - Verify imports use `@site/src/components/ai/` prefix
  - Verify component names match exported names

**Acceptance Test**: Registry file exports all 4 components (or explicit imports in MDX work)

---

## PHASE 3 — VALIDATION

**User Story**: US1, US2 - Structure and Component Validation

**Test Strategy**: Can be tested by running build validation, browser verification, and component interaction testing.

### Build Validation

- [ ] [T016] [P1] [VALIDATION] Run MDX linting: Run `npm run build` in frontend directory
- [ ] [T017] [P1] [VALIDATION] Fix any MDX or TSX import errors: Resolve any build errors
- [ ] [T018] [P1] [VALIDATION] Verify build succeeds: Check that build completes without errors or warnings

### Browser Verification

- [ ] [T019] [P1] [VALIDATION] Run npm start and open Chapter 3 page: Start dev server and navigate to `/docs/chapters/chapter-3`
- [ ] [T020] [P1] [VALIDATION] Verify all AI blocks render visually: Check that all 4 components appear in correct positions
- [ ] [T021] [P1] [VALIDATION] Confirm console logs appear on interactions (no API calls): Interact with components and verify placeholder UI appears

**Acceptance Test**: All validation checks pass (build succeeds, components render, placeholder UI appears, no API calls)

---

## Summary

**Total Tasks**: 21 tasks across 3 phases
**Estimated Time**: 30-45 minutes (MDX integration only, no backend logic)
**Complexity**: Low (following existing patterns, explicit component placement)

**Success Criteria**:
- ✅ All AI blocks appear visually in Chapter 3
- ✅ No TypeScript errors
- ✅ Correct ordering of components (matches Feature 037)
- ✅ No missing imports
- ✅ Build runs without warnings
- ✅ Components render with placeholder UI (no API calls)

**Next Steps**: Proceed to `/sp.implement` to execute all tasks in order.

