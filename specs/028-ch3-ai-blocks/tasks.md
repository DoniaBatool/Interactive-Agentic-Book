# Tasks: Chapter 3 — AI Blocks Integration Layer

**Feature**: 028-ch3-ai-blocks | **Branch**: `028-ch3-ai-blocks` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for integrating AI blocks into Chapter 3 MDX file by reusing existing components from Chapter 1 (MDX integration only, no backend logic).

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

**Purpose**: Verify dependencies and prerequisites before integrating AI blocks into Chapter 3 MDX.

- [ ] [T001] [P1] [SETUP] Verify Chapter 3 MDX file exists at `frontend/docs/chapters/chapter-3.mdx` and is readable
- [ ] [T002] [P1] [SETUP] Verify AI block components exist from Feature 004: Check that `frontend/src/components/ai/AskQuestionBlock.tsx`, `ExplainLike10Block.tsx`, `InteractiveQuizBlock.tsx`, `GenerateDiagramBlock.tsx` all exist
- [ ] [T003] [P1] [SETUP] Verify Chapter 1 and Chapter 2 AI blocks are functional: Navigate to `/docs/chapters/chapter-1` and `/docs/chapters/chapter-2` and confirm all AI block components render correctly (if frontend is running)
- [ ] [T004] [P1] [SETUP] Verify Docusaurus 3.x frontend builds successfully: Run `cd frontend && npm run build` to confirm no errors before making changes
- [ ] [T005] [P1] [SETUP] Verify backend metadata file exists: Check that `backend/app/content/chapters/chapter_3.py` exists and is importable

**Success Criteria**:
- Chapter 3 MDX file exists and is readable
- All AI block components exist (from Feature 004)
- Frontend builds without errors
- Backend metadata file exists

**Dependencies**: Feature 004 (Chapter 1 Interactive AI Blocks), Feature 023 (Chapter 2 AI Blocks) must be complete

---

## PHASE 1 — MDX File Update

**User Story**: US1 - Learner Sees AI Blocks Rendered in Chapter 3

**Test Strategy**: Can be tested by adding imports and replacing placeholders with components, then verifying MDX compiles.

### Component Import Addition

- [ ] [T006] [P1] [US1] Add import statements at top of `frontend/docs/chapters/chapter-3.mdx` (after frontmatter, before content):
  ```mdx
  import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
  import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
  import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
  import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
  ```

### Placeholder Replacement

- [ ] [T007] [P1] [US1] Replace `<!-- AI-BLOCK: ask-question -->` in `frontend/docs/chapters/chapter-3.mdx` (after "What Is Perception in Physical AI?" section) with:
  ```mdx
  <AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />
  ```

- [ ] [T008] [P1] [US1] Replace `<!-- AI-BLOCK: generate-diagram -->` in `frontend/docs/chapters/chapter-3.mdx` (after "Types of Sensors in Robotics" section) with:
  ```mdx
  <GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />
  ```

- [ ] [T009] [P1] [US1] Replace `<!-- AI-BLOCK: explain-like-i-am-10 -->` in `frontend/docs/chapters/chapter-3.mdx` (inside "Computer Vision & Depth Perception" section) with:
  ```mdx
  <ExplainLike10Block concept="computer-vision" chapterId={3} />
  ```

- [ ] [T010] [P1] [US1] Replace `<!-- AI-BLOCK: interactive-quiz -->` in `frontend/docs/chapters/chapter-3.mdx` (after "Signal Processing Basics for AI" section) with:
  ```mdx
  <InteractiveQuizBlock chapterId={3} numQuestions={5} />
  ```

### Frontmatter Verification

- [ ] [T011] [P1] [US1] Verify frontmatter in `frontend/docs/chapters/chapter-3.mdx` matches contract:
  - `title`: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
  - `description`: SEO-optimized summary (150-160 chars)
  - `sidebar_position`: 3
  - `sidebar_label`: "Chapter 3: Physical AI Perception Systems"
  - `tags`: ["physical-ai", "sensors", "perception", "signal-processing"]

### RAG Chunking Markers Verification

- [ ] [T012] [P1] [US1] Verify RAG chunking markers are present in `frontend/docs/chapters/chapter-3.mdx`:
  - Each section should have `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` markers
  - Markers should wrap section content including AI blocks and diagrams

**Acceptance Test**: All 4 placeholders replaced with components, imports added, frontmatter verified, chunking markers present, MDX compiles successfully

---

## PHASE 2 — Component Mapping Verification

**User Story**: US2 - Developer Verifies MDX Component Integration

**Test Strategy**: Can be tested by verifying component mapping file and imports.

### MDX Component Mapping

- [ ] [T013] [P1] [US2] Verify `frontend/src/mdx-components.ts` exists and exports all 4 AI block components:
  - Check that `AskQuestionBlock`, `ExplainLike10Block`, `InteractiveQuizBlock`, `GenerateDiagramBlock` are all exported
  - Verify export structure: `export default { AskQuestionBlock, ExplainLike10Block, InteractiveQuizBlock, GenerateDiagramBlock };`

- [ ] [T014] [P1] [US2] Validate imports in `frontend/src/mdx-components.ts`: Verify all 4 components are imported from `@site/src/components/ai/` paths correctly

- [ ] [T015] [P2] [US2] Add comments in `frontend/src/mdx-components.ts` explaining Chapter 3 compatibility:
  - Add comment: `// Components support Chapter 1 (chapterId=1), Chapter 2 (chapterId=2), and Chapter 3 (chapterId=3)`
  - Add comment: `// Chapter 3 usage: <AskQuestionBlock chapterId={3} sectionId="..." />`

**Acceptance Test**: Component mapping file exports all 4 components correctly, imports are valid

---

## PHASE 3 — Backend Metadata Verification

**User Story**: US1 - Learner Sees AI Blocks Rendered in Chapter 3

**Test Strategy**: Can be tested by verifying metadata file matches MDX structure exactly.

### Metadata Structure Verification

- [ ] [T016] [P1] [US1] Verify `backend/app/content/chapters/chapter_3.py` exists and contains `CHAPTER_METADATA` dictionary

- [ ] [T017] [P1] [US1] Verify `id` field in `backend/app/content/chapters/chapter_3.py`: Check that `"id": 3` is set correctly

- [ ] [T018] [P1] [US1] Verify `title` field in `backend/app/content/chapters/chapter_3.py`: Check that `"title"` matches MDX frontmatter exactly: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"

- [ ] [T019] [P1] [US1] Verify `sections` list in `backend/app/content/chapters/chapter_3.py`: Check that list contains exactly 7 section titles matching MDX H2 headings in order:
  1. "What Is Perception in Physical AI?"
  2. "Types of Sensors in Robotics"
  3. "Computer Vision & Depth Perception"
  4. "Signal Processing Basics for AI"
  5. "Feature Extraction & Interpretation"
  6. "Learning Objectives"
  7. "Glossary"

- [ ] [T020] [P1] [US1] Verify `ai_blocks` list in `backend/app/content/chapters/chapter_3.py`: Check that list contains exactly 4 block types in order:
  - "ask-question"
  - "explain-like-i-am-10"
  - "interactive-quiz"
  - "generate-diagram"

- [ ] [T021] [P1] [US1] Verify `diagram_placeholders` list in `backend/app/content/chapters/chapter_3.py`: Check that list contains exactly 4 diagram names in order:
  - "perception-overview"
  - "sensor-types"
  - "cv-depth-flow"
  - "feature-extraction-pipeline"

- [ ] [T022] [P1] [US1] Update metadata if needed: If any field doesn't match MDX structure, update `backend/app/content/chapters/chapter_3.py` to match exactly

- [ ] [T023] [P1] [US1] Verify metadata file imports successfully: Run `cd backend && python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA; print('Import successful')"` - should complete without errors

**Acceptance Test**: Metadata file exists, all fields match MDX structure exactly, file imports successfully

---

## PHASE 4 — RAG Chunks File Creation

**User Story**: US1 - Learner Sees AI Blocks Rendered in Chapter 3

**Test Strategy**: Can be tested by verifying chunks file exists with placeholder function.

### Chunks File Creation

- [ ] [T024] [P1] [US1] Create `backend/app/content/chapters/chapter_3_chunks.py` with placeholder function:
  ```python
  from typing import List, Dict, Any

  def get_chapter3_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
      """
      Get Chapter 3 chunks for RAG pipeline.
      
      Args:
          chapter_id: Chapter identifier (default: 3 for Chapter 3)
      
      Returns:
          List of chunk dictionaries with structure:
          [
              {
                  "id": str,
                  "text": str,
                  "chapter_id": 3,
                  "section_id": str,
                  "position": int,
                  "word_count": int,
                  "metadata": Dict[str, Any]
              },
              ...
          ]
      
      TODO: Implement chunking from Chapter 3 MDX content
      TODO: Load Chapter 3 content from frontend/docs/chapters/chapter-3.mdx
      TODO: Implement chunking strategy (by section, by paragraph, or semantic)
      TODO: Extract metadata (section titles, positions, word counts)
      TODO: Generate unique chunk IDs (format: "ch3-s{section}-c{chunk}")
      TODO: Handle special content (glossary, diagrams, AI blocks)
      TODO: Cache chunks for performance
      TODO: Include Physical AI Perception-specific metadata
      """
      # Placeholder return - no real chunking implementation
      return []
  ```

- [ ] [T025] [P1] [US1] Verify chunks file imports successfully: Run `cd backend && python -c "from app.content.chapters.chapter_3_chunks import get_chapter3_chunks; print('Import successful')"` - should complete without errors

**Acceptance Test**: Chunks file exists, function signature is correct, function has TODO comments, function returns empty list (placeholder), file imports successfully

---

## PHASE 5 — Build Validation

**User Story**: US1 - Learner Sees AI Blocks Rendered in Chapter 3, US2 - Developer Verifies MDX Component Integration

**Test Strategy**: Can be tested by running frontend build and verifying components render correctly.

### Frontend Build Test

- [ ] [T026] [P1] [VALIDATION] Run frontend build: Execute `cd frontend && npm run build` - should complete without errors

- [ ] [T027] [P1] [VALIDATION] Verify no TypeScript compilation errors: Check build output for any TypeScript errors related to AI block components

- [ ] [T028] [P1] [VALIDATION] Verify no MDX parsing errors: Check build output for any MDX parsing errors

- [ ] [T029] [P1] [VALIDATION] Verify all imports resolve: Check build output for any missing import errors

### Component Rendering Test

- [ ] [T030] [P1] [VALIDATION] Start dev server: Run `cd frontend && npm run start` (or verify dev server is running)

- [ ] [T031] [P1] [VALIDATION] Navigate to Chapter 3: Open browser to `/docs/chapters/chapter-3`

- [ ] [T032] [P1] [VALIDATION] Verify Ask Question block renders: Check that `<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />` renders after "What Is Perception in Physical AI?" section

- [ ] [T033] [P1] [VALIDATION] Verify Generate Diagram block renders: Check that `<GenerateDiagramBlock diagramType="sensor-types" chapterId={3} />` renders after "Types of Sensors in Robotics" section

- [ ] [T034] [P1] [VALIDATION] Verify Explain Like 10 block renders: Check that `<ExplainLike10Block concept="computer-vision" chapterId={3} />` renders inside "Computer Vision & Depth Perception" section

- [ ] [T035] [P1] [VALIDATION] Verify Interactive Quiz block renders: Check that `<InteractiveQuizBlock chapterId={3} numQuestions={5} />` renders after "Signal Processing Basics for AI" section

- [ ] [T036] [P1] [VALIDATION] Verify no React errors: Check browser console for any React errors related to AI block components

- [ ] [T037] [P1] [VALIDATION] Verify Chapter 3 visible in sidebar: Check that Chapter 3 appears in Docusaurus sidebar at position 3 (after Chapter 2)

### Backend Import Test

- [ ] [T038] [P1] [VALIDATION] Verify backend metadata imports: Run `cd backend && python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA; print('Metadata import: OK')"` - should complete without errors

- [ ] [T039] [P1] [VALIDATION] Verify backend chunks imports: Run `cd backend && python -c "from app.content.chapters.chapter_3_chunks import get_chapter3_chunks; print('Chunks import: OK')"` - should complete without errors

**Acceptance Test**: Frontend build succeeds, all components render correctly, no console errors, Chapter 3 visible in sidebar, backend imports succeed

---

## PHASE 6 — Contract Verification

**User Story**: US2 - Developer Verifies MDX Component Integration

**Test Strategy**: Can be tested by verifying contract file exists and documents usage patterns.

### Contract Documentation

- [ ] [T040] [P1] [US2] Verify `specs/028-ch3-ai-blocks/contracts/ch3-content-contract.yaml` exists (already created in spec phase)

- [ ] [T041] [P1] [US2] Verify contract documents MDX usage patterns:
  - Block names (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
  - Import statement format
  - Component usage syntax

- [ ] [T042] [P1] [US2] Verify contract documents required component props:
  - AskQuestionBlock: `chapterId`, `sectionId`
  - ExplainLike10Block: `chapterId`, `concept`
  - InteractiveQuizBlock: `chapterId`, `numQuestions`
  - GenerateDiagramBlock: `chapterId`, `diagramType`

- [ ] [T043] [P1] [US2] Verify contract documents Chapter 3 placement positions:
  - Ask Question Block: After "What Is Perception in Physical AI?" section
  - Generate Diagram Block: After "Types of Sensors in Robotics" section
  - Explain Like 10 Block: Inside "Computer Vision & Depth Perception" section
  - Interactive Quiz Block: After "Signal Processing Basics for AI" section

- [ ] [T044] [P1] [US2] Verify contract documents frontmatter schema requirements

- [ ] [T045] [P1] [US2] Verify contract documents RAG chunking markers format

**Acceptance Test**: Contract file exists, documents all usage patterns, component props, placement positions, frontmatter schema, and RAG markers

---

## Summary

**Total Tasks**: 45 tasks across 6 phases
- **Phase 0**: 5 setup tasks
- **Phase 1**: 7 MDX file update tasks
- **Phase 2**: 3 component mapping tasks
- **Phase 3**: 8 backend metadata tasks
- **Phase 4**: 2 RAG chunks file tasks
- **Phase 5**: 14 build validation tasks
- **Phase 6**: 6 contract verification tasks

**Estimated Time**: 30-45 minutes (scaffolding only, no real AI logic)

**Next Step**: Run `/sp.implement` to execute tasks in order

---

## Notes

- All tasks are scaffolding only—no real AI logic implementation
- All components reuse existing implementations from Feature 004
- All props match Chapter 3 metadata structure from chapter_3.py
- RAG chunking markers are already present in MDX (from Feature 017/018)
- Backend metadata file already exists (may need updates to match MDX exactly)
- Follow Feature 023 (Chapter 2 AI Blocks) patterns exactly for consistency

