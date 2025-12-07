# Tasks: Chapter 2 — AI Block Rendering + MDX Integration

**Feature**: 023-ch2-ai-blocks | **Branch**: `023-ch2-ai-blocks` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for integrating AI blocks into Chapter 2 MDX file by reusing existing components from Chapter 1 (MDX integration only, no backend logic).

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), SETUP (Initial setup), VALIDATION (Testing/validation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before integrating AI blocks into Chapter 2 MDX.

- [ ] [T001] [P1] [SETUP] Verify Chapter 2 MDX file exists at `frontend/docs/chapters/chapter-2.mdx` and is readable
- [ ] [T002] [P1] [SETUP] Verify AI block components exist from Feature 004: Check that `frontend/src/components/ai/AskQuestionBlock.tsx`, `ExplainLike10Block.tsx`, `InteractiveQuizBlock.tsx`, `GenerateDiagramBlock.tsx` all exist
- [ ] [T003] [P1] [SETUP] Verify Chapter 1 AI blocks are functional: Navigate to `/docs/chapters/chapter-1` and confirm all 4 AI block components render correctly (if frontend is running)
- [ ] [T004] [P1] [SETUP] Verify Docusaurus 3.x frontend builds successfully: Run `cd frontend && npm run build` to confirm no errors before making changes

**Success Criteria**:
- Chapter 2 MDX file exists and is readable
- All AI block components exist (from Feature 004)
- Frontend builds without errors

**Dependencies**: Feature 004 (Chapter 1 Interactive AI Blocks) must be complete

---

## PHASE 1 — Frontend MDX Setup

**User Story**: US1 - Learner Sees AI Blocks Rendered in Chapter 2

**Test Strategy**: Can be tested by adding placeholders and verifying MDX file structure is correct.

### MDX File Structure

- [ ] [T005] [P1] [US1] Confirm `frontend/docs/chapters/chapter-2.mdx` has proper frontmatter structure (title, description, sidebar_position, sidebar_label, tags)
- [ ] [T006] [P1] [US1] Identify sections in `frontend/docs/chapters/chapter-2.mdx` where AI blocks should be placed:
  - After "Introduction to ROS 2" section (for AskQuestionBlock)
  - After "Nodes and Node Communication" section (for GenerateDiagramBlock)
  - Inside "Topics and Messages" section (for ExplainLike10Block)
  - After "Services and Actions" section (for InteractiveQuizBlock)
- [ ] [T007] [P1] [US1] Insert or verify 4 AI-BLOCK placeholder comments in `frontend/docs/chapters/chapter-2.mdx` at pedagogically correct positions:
  - `<!-- AI-BLOCK: ask-question -->` after "Introduction to ROS 2" section
  - `<!-- AI-BLOCK: generate-diagram -->` after "Nodes and Node Communication" section
  - `<!-- AI-BLOCK: explain-like-i-am-10 -->` inside "Topics and Messages" section
  - `<!-- AI-BLOCK: interactive-quiz -->` after "Services and Actions" section
- [ ] [T008] [P2] [US1] Add TODO notes in `frontend/docs/chapters/chapter-2.mdx` where exact prop values are not yet determined (e.g., `<!-- TODO: Determine exact sectionId for AskQuestionBlock -->`)

**Acceptance Test**: Chapter 2 MDX file has 4 AI-BLOCK placeholder comments at correct positions

---

## PHASE 2 — Component Mapping

**User Story**: US2 - Developer Verifies MDX Component Integration

**Test Strategy**: Can be tested by verifying component mapping file and imports.

### MDX Component Mapping

- [ ] [T009] [P1] [US2] Verify `frontend/src/mdx-components.ts` exists and exports all 4 AI block components:
  - Check that `AskQuestionBlock`, `ExplainLike10Block`, `InteractiveQuizBlock`, `GenerateDiagramBlock` are all exported
  - Verify export structure: `export default { AskQuestionBlock, ExplainLike10Block, InteractiveQuizBlock, GenerateDiagramBlock };`
- [ ] [T010] [P1] [US2] Validate imports in `frontend/src/mdx-components.ts`: Verify all 4 components are imported from `@site/src/components/ai/` paths correctly
- [ ] [T011] [P2] [US2] Add comments in `frontend/src/mdx-components.ts` explaining Chapter 2 compatibility:
  - Add comment: `// Components support Chapter 2 (chapterId=2) and Chapter 1 (chapterId=1)`
  - Add comment: `// Chapter 2 usage: <AskQuestionBlock chapterId={2} sectionId="..." />`

**Acceptance Test**: Component mapping file exports all 4 components correctly, imports are valid

---

## PHASE 3 — MDX Rendering

**User Story**: US1 - Learner Sees AI Blocks Rendered in Chapter 2

**Test Strategy**: Can be tested by replacing placeholders with components and verifying MDX compiles.

### Component Import Addition

- [ ] [T012] [P1] [US1] Add import statements at top of `frontend/docs/chapters/chapter-2.mdx` (after frontmatter, before content):
  ```mdx
  import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
  import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
  import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
  import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
  ```

### Placeholder Replacement

- [ ] [T013] [P1] [US1] Replace `<!-- AI-BLOCK: ask-question -->` in `frontend/docs/chapters/chapter-2.mdx` (after "Introduction to ROS 2" section) with:
  ```mdx
  <AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />
  ```
  (Use `sectionId="TODO"` if exact value not yet determined)

- [ ] [T014] [P1] [US1] Replace `<!-- AI-BLOCK: generate-diagram -->` in `frontend/docs/chapters/chapter-2.mdx` (after "Nodes and Node Communication" section) with:
  ```mdx
  <GenerateDiagramBlock chapterId={2} diagramType="node-communication-architecture" />
  ```
  (Use `diagramType="TODO"` if exact value not yet determined)

- [ ] [T015] [P1] [US1] Replace `<!-- AI-BLOCK: explain-like-i-am-10 -->` in `frontend/docs/chapters/chapter-2.mdx` (inside "Topics and Messages" section) with:
  ```mdx
  <ExplainLike10Block chapterId={2} concept="topics" />
  ```
  (Use `concept="TODO"` if exact value not yet determined)

- [ ] [T016] [P1] [US1] Replace `<!-- AI-BLOCK: interactive-quiz -->` in `frontend/docs/chapters/chapter-2.mdx` (after "Services and Actions" section) with:
  ```mdx
  <InteractiveQuizBlock chapterId={2} numQuestions={6} />
  ```

### MDX Compilation Verification

- [ ] [T017] [P1] [US1] Verify MDX compiles: Run `cd frontend && npm run build` - should complete without errors, no TypeScript compilation errors, no MDX parsing errors

**Acceptance Test**: All 4 placeholders replaced with components, MDX compiles successfully

---

## PHASE 4 — Contracts

**User Story**: US2 - Developer Verifies MDX Component Integration

**Test Strategy**: Can be tested by verifying contract file exists and documents usage patterns.

### Contract Documentation

- [ ] [T018] [P1] [US2] Verify `specs/023-ch2-ai-blocks/contracts/ai-block-mdx.yaml` exists (already created in spec phase)
- [ ] [T019] [P1] [US2] Verify contract documents MDX usage patterns:
  - Block names (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
  - Import statement format
  - Component usage syntax
- [ ] [T020] [P1] [US2] Verify contract documents required component props:
  - AskQuestionBlock: `chapterId`, `sectionId`
  - ExplainLike10Block: `chapterId`, `concept`
  - InteractiveQuizBlock: `chapterId`, `numQuestions`
  - GenerateDiagramBlock: `chapterId`, `diagramType`
- [ ] [T021] [P2] [US2] Verify contract documents Chapter 2-specific usage:
  - All components use `chapterId={2}`
  - Section IDs match Chapter 2 section anchors
  - Concepts are ROS 2-specific (topics, nodes, services, actions)
  - Diagram types match Chapter 2 diagram placeholders

**Acceptance Test**: Contract file exists and documents all MDX usage patterns and component props

---

## PHASE 5 — Validation

**User Story**: US1 - Learner Sees AI Blocks Rendered in Chapter 2

**Test Strategy**: Can be tested by running build, checking for errors, and verifying components render.

### Build Validation

- [ ] [T022] [P1] [VALIDATION] Run Docusaurus build: Execute `cd frontend && npm run build` - should complete successfully without errors
- [ ] [T023] [P1] [VALIDATION] Ensure no React/TypeScript errors: Check build output for any React or TypeScript compilation errors - should be none
- [ ] [T024] [P1] [VALIDATION] Ensure no MDX parsing errors: Check build output for any MDX syntax errors - should be none
- [ ] [T025] [P1] [VALIDATION] Verify all imports resolve: Check build output for any missing import errors - should be none

### Component Rendering Validation

- [ ] [T026] [P1] [VALIDATION] Test component rendering: Run `cd frontend && npm start`, navigate to `/docs/chapters/chapter-2` in browser, verify:
  - All 4 AI block components render in their designated locations
  - No React errors in browser console
  - Components display minimal UI (input fields, buttons, placeholders)
  - AskQuestionBlock has `chapterId={2}` and `sectionId` prop (check in DevTools)
  - GenerateDiagramBlock has `diagramType` and `chapterId={2}` props (check in DevTools)
  - ExplainLike10Block has `concept` and `chapterId={2}` props (check in DevTools)
  - InteractiveQuizBlock has `chapterId={2}` and `numQuestions={6}` props (check in DevTools)

### Frontend Load Validation

- [ ] [T027] [P1] [VALIDATION] Verify frontend loads Chapter 2 without failing: Navigate to `/docs/chapters/chapter-2`, confirm page loads completely, no JavaScript errors in console
- [ ] [T028] [P2] [VALIDATION] Verify component placement: Check that components appear at pedagogically correct positions in the chapter content flow

**Acceptance Test**: 
- Docusaurus build succeeds
- No React/TypeScript errors
- All 4 components render correctly in Chapter 2
- Frontend loads Chapter 2 without failing
- Components have correct props

---

## Task Summary

**Total Tasks**: 28 tasks
- **Phase 0 (Setup)**: 4 tasks
- **Phase 1 (MDX Setup)**: 4 tasks
- **Phase 2 (Component Mapping)**: 3 tasks
- **Phase 3 (MDX Rendering)**: 6 tasks
- **Phase 4 (Contracts)**: 4 tasks
- **Phase 5 (Validation)**: 7 tasks

**Priority Breakdown**:
- **P1 (Critical)**: 24 tasks
- **P2 (Important)**: 4 tasks
- **P3 (Nice-to-have)**: 0 tasks

**Estimated Time**: 30-45 minutes (MDX integration only, no backend logic)

---

## Dependencies

- **Dependency 1**: Feature 004 (Chapter 1 Interactive AI Blocks) - Required for existing components
- **Dependency 2**: Feature 010 or 014 (Chapter 2 Content) - Required for Chapter 2 MDX file
- **Dependency 3**: Docusaurus MDX Configuration - Required for component rendering

---

## Success Criteria

- ✅ All 4 AI block components render in Chapter 2 MDX
- ✅ Docusaurus build passes without errors
- ✅ Components imported correctly
- ✅ No React/TypeScript errors
- ✅ Frontend loads Chapter 2 without failing
- ✅ Contract documentation complete

---

## Notes

- All components reuse existing implementations from Feature 004
- No new component creation required
- Focus is on MDX integration only (no backend logic)
- Some props may use TODO placeholders if exact values not yet determined
- Build validation is critical before considering feature complete

