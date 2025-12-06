# Tasks: Chapter 3 Validation, Testing & Build Stability Layer

**Feature**: 019-chapter-3-validation | **Branch**: `019-chapter-3-validation` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for validating Chapter 3 content, metadata, AI-block integrations (HTML comment format), chunk markers, RAG pipeline readiness, and build stability. No new features; only validation.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), US3 (User Story 3), SETUP (Initial setup), VALIDATION (Validation tasks)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before running validations.

- [ ] [T001] [P1] [SETUP] Verify Feature 017 is complete: Check that `frontend/docs/chapters/chapter-3.mdx` exists with 7 sections
- [ ] [T002] [P1] [SETUP] Verify Feature 018 is complete: Check that `frontend/docs/chapters/chapter-3.mdx` uses HTML comment format for AI-blocks
- [ ] [T003] [P1] [SETUP] Verify Feature 018 is complete: Check that `frontend/docs/chapters/chapter-3.mdx` has chunk markers (CHUNK: START / CHUNK: END)
- [ ] [T004] [P1] [SETUP] Verify Feature 018 is complete: Check that `backend/app/content/chapters/chapter_3.py` has Feature 018 diagram names
- [ ] [T005] [P1] [SETUP] Verify backend directory structure exists: Check that `backend/app/content/chapters/` directory exists
- [ ] [T006] [P1] [SETUP] Verify frontend directory structure exists: Check that `frontend/docs/chapters/` directory exists
- [ ] [T007] [P1] [SETUP] Verify validators directory exists: Check that `backend/app/validators/` directory exists (create if needed)
- [ ] [T008] [P1] [SETUP] Verify tests directory exists: Check that `tests/` directory exists (create if needed)

**Success Criteria**:
- All prerequisite files and directories exist
- All dependent features (017, 018) are complete
- Ready to run validations

**Dependencies**: Feature 017, 018 (both must be complete)

---

## PHASE 1 — MDX STRUCTURE VALIDATION TASKS

**User Story**: US1 - Developer Validates Chapter 3 Structure

**Test Strategy**: Can be tested by running validation commands and verifying results match expected values.

### File Existence Validation

- [ ] [T009] [P1] [US1] Validate MDX file exists at `frontend/docs/chapters/chapter-3.mdx`:
  - Run: `Test-Path frontend/docs/chapters/chapter-3.mdx` (PowerShell) or `test -f frontend/docs/chapters/chapter-3.mdx` (Bash)
  - Expected: File exists
  - Document result in validation report

### Section Count Validation

- [ ] [T010] [P1] [US1] Validate 7 H2 sections in `frontend/docs/chapters/chapter-3.mdx`:
  - Run: `Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '^## ' | Measure-Object | Select-Object -ExpandProperty Count` (PowerShell)
  - Or: `grep -c "^## " frontend/docs/chapters/chapter-3.mdx` (Bash)
  - Expected: 7
  - Document result in validation report

### Section Order Validation

- [ ] [T011] [P1] [US1] Validate section order in `frontend/docs/chapters/chapter-3.mdx`:
  - Extract H2 section titles in order
  - Verify order matches specification:
    1. What Is Perception in Physical AI?
    2. Types of Sensors in Robotics
    3. Computer Vision & Depth Perception
    4. Signal Processing Basics for AI
    5. Feature Extraction & Interpretation
    6. Learning Objectives
    7. Glossary
  - Document result in validation report

### Frontmatter Fields Validation

- [ ] [T012] [P1] [US1] Validate frontmatter format in `frontend/docs/chapters/chapter-3.mdx`:
  - Check `title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"` exists
  - Check `description: "..."` exists and is non-empty (10-250 characters)
  - Check `sidebar_position: 3` exists
  - Check `sidebar_label: "Chapter 3: Physical AI Perception Systems"` exists
  - Check `tags: ["physical-ai", "perception", "sensors", "signal-processing", "intermediate"]` exists
  - Verify YAML frontmatter is valid
  - Document result in validation report

### Paragraph + Sentence Rules Validation

- [ ] [T013] [P2] [US1] Validate reading level rules in `frontend/docs/chapters/chapter-3.mdx` (when content is written):
  - Check paragraphs: max 4 sentences per paragraph
  - Check sentences: 15-20 words per sentence
  - Check reading level: Grade 7-8
  - Note: This validation may be skipped if content is not yet written (acceptable failure)
  - Document result in validation report

**Phase Completion**: All MDX structure validations pass, results documented

---

## PHASE 2 — PLACEHOLDER VALIDATION TASKS

**User Story**: US1 - Developer Validates Chapter 3 Structure

**Test Strategy**: Can be tested by counting placeholders and verifying naming conventions.

### Diagram Placeholder Count Validation

- [ ] [T014] [P1] [US1] Validate 4 DIAGRAM placeholders in `frontend/docs/chapters/chapter-3.mdx`:
  - Run: `Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- DIAGRAM:' | Measure-Object | Select-Object -ExpandProperty Count` (PowerShell)
  - Or: `grep -c "<!-- DIAGRAM:" frontend/docs/chapters/chapter-3.mdx` (Bash)
  - Expected: 4
  - Document result in validation report

### Diagram Placeholder Names Validation

- [ ] [T015] [P1] [US1] Validate diagram placeholder names match Feature 018 names in `frontend/docs/chapters/chapter-3.mdx`:
  - Extract all diagram placeholder names
  - Verify exact names match Feature 018 names:
    - perception-overview
    - sensor-types
    - cv-depth-flow
    - feature-extraction-pipeline
  - Verify all use kebab-case naming
  - Document result in validation report

### AI-BLOCK Placeholder Count Validation

- [ ] [T016] [P1] [US1] Validate 4 AI-BLOCK HTML comment placeholders in `frontend/docs/chapters/chapter-3.mdx`:
  - Run: `Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- AI-BLOCK:' | Measure-Object | Select-Object -ExpandProperty Count` (PowerShell)
  - Or: `grep -c "<!-- AI-BLOCK:" frontend/docs/chapters/chapter-3.mdx` (Bash)
  - Expected: 4
  - Document result in validation report

### AI-BLOCK Placeholder Format Validation

- [ ] [T017] [P1] [US1] Validate AI-BLOCK placeholders use HTML comment format in `frontend/docs/chapters/chapter-3.mdx`:
  - Verify all AI-block placeholders use format: `<!-- AI-BLOCK: type -->`
  - Verify no React component format (`<AskQuestionBlock ... />`) exists
  - Verify allowed types:
    - ask-question
    - explain-like-i-am-10
    - interactive-quiz
    - generate-diagram
  - Document result in validation report

### Regex Validation for Naming

- [ ] [T018] [P1] [US1] Validate naming conventions using regex in `frontend/docs/chapters/chapter-3.mdx`:
  - Verify all diagram placeholders match pattern: `<!-- DIAGRAM: [a-z0-9-]+ -->`
  - Verify all AI-block placeholders match pattern: `<!-- AI-BLOCK: [a-z0-9-]+ -->`
  - Verify all anchor links use kebab-case: `{#section-name}`
  - Document result in validation report

### Invalid Placeholder Types Validation

- [ ] [T019] [P1] [US1] Ensure no invalid placeholder types in `frontend/docs/chapters/chapter-3.mdx`:
  - Check for any DIAGRAM placeholders not in Feature 018 names list
  - Check for any AI-BLOCK placeholders not in allowed types list
  - Check for any React component format (should be none)
  - Document result in validation report

**Phase Completion**: All placeholder validations pass, results documented

---

## PHASE 3 — METADATA VALIDATION TASKS

**User Story**: US1 - Developer Validates Chapter 3 Structure

**Test Strategy**: Can be tested by importing metadata and comparing with MDX structure.

### Python File Existence Validation

- [ ] [T020] [P1] [US1] Validate Python metadata file exists at `backend/app/content/chapters/chapter_3.py`:
  - Run: `Test-Path backend/app/content/chapters/chapter_3.py` (PowerShell) or `test -f backend/app/content/chapters/chapter_3.py` (Bash)
  - Expected: File exists
  - Document result in validation report

### Importability Validation (Python Compile)

- [ ] [T021] [P1] [US1] Validate metadata file imports correctly:
  - Run: `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA; print('Import successful')"`
  - Expected: No import errors, no syntax errors
  - Document result in validation report

### All Fields Validation

- [ ] [T022] [P1] [US1] Validate all required fields exist in `backend/app/content/chapters/chapter_3.py`:
  - Check `id: 3` exists
  - Check `title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"` exists
  - Check `summary: "..."` exists (non-empty)
  - Check `section_count: 7` exists
  - Check `sections: [...]` exists (list with 7 items)
  - Check `ai_blocks: [...]` exists (list with 4 items)
  - Check `diagram_placeholders: [...]` exists (list with 4 items)
  - Check `difficulty_level: "intermediate"` exists
  - Check `prerequisites: [1, 2]` exists
  - Check `learning_outcomes: [...]` exists (non-empty list)
  - Check `glossary_terms: [...]` exists (list with 7 items)
  - Check `last_updated: "..."` exists (ISO 8601 format)
  - Document result in validation report

### Section List Matches MDX Validation

- [ ] [T023] [P1] [US1] Ensure `backend/app/content/chapters/chapter_3.py` sections[] matches MDX:
  - Extract section titles from MDX (from Phase 1)
  - Compare: `CHAPTER_METADATA["sections"]` with MDX section titles
  - Expected: Lists match exactly (same order, same titles)
  - Document result in validation report

### Section Count Match Validation

- [ ] [T024] [P1] [US1] Ensure `backend/app/content/chapters/chapter_3.py` section_count matches MDX:
  - Compare: `CHAPTER_METADATA["section_count"]` with MDX section count (from Phase 1)
  - Expected: Both equal 7
  - Document result in validation report

### AI Blocks Match Validation

- [ ] [T025] [P1] [US1] Ensure `backend/app/content/chapters/chapter_3.py` ai_blocks[] matches MDX:
  - Extract AI-block types from MDX (from Phase 2)
  - Compare: `CHAPTER_METADATA["ai_blocks"]` with MDX AI-block types
  - Expected: Sets match (4 items: ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
  - Document result in validation report

### Diagram Placeholders Match Validation

- [ ] [T026] [P1] [US1] Ensure `backend/app/content/chapters/chapter_3.py` diagram_placeholders[] matches MDX:
  - Extract diagram placeholders from MDX (from Phase 2)
  - Compare: `CHAPTER_METADATA["diagram_placeholders"]` with MDX diagram placeholders
  - Expected: Sets match (4 items: perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline - Feature 018 names)
  - Document result in validation report

### Glossary Count Validation

- [ ] [T027] [P1] [US1] Validate glossary_terms count in `backend/app/content/chapters/chapter_3.py`:
  - Check `CHAPTER_METADATA["glossary_terms"]` exists and has 7 items
  - Compare glossary_terms with MDX glossary terms (from Phase 1)
  - Expected: Sets match (7 terms)
  - Document result in validation report

### RAG Metadata Validation

- [ ] [T028] [P2] [US1] Validate RAG metadata fields in `backend/app/content/chapters/chapter_3.py`:
  - Check metadata structure supports future RAG integration
  - Verify metadata includes fields needed for RAG (sections, glossary_terms, etc.)
  - Note: This is a future integration check (acceptable if not fully implemented)
  - Document result in validation report

**Phase Completion**: All metadata validations pass, results documented

---

## PHASE 4 — RAG CHUNK VALIDATION TASKS

**User Story**: US1 - Developer Validates Chapter 3 Structure

**Test Strategy**: Can be tested by validating chunk markers and chunk file structure.

### Chunk Marker Count Validation

- [ ] [T029] [P1] [US1] Validate chunk marker count in `frontend/docs/chapters/chapter-3.mdx`:
  - Count CHUNK: START markers: `Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- CHUNK: START -->' | Measure-Object | Select-Object -ExpandProperty Count` (PowerShell)
  - Count CHUNK: END markers: `Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- CHUNK: END -->' | Measure-Object | Select-Object -ExpandProperty Count` (PowerShell)
  - Expected: 7 START markers, 7 END markers
  - Document result in validation report

### Chunk Marker Pairing Validation

- [ ] [T030] [P1] [US1] Validate chunk markers are properly paired in `frontend/docs/chapters/chapter-3.mdx`:
  - Verify each CHUNK: START has a corresponding CHUNK: END
  - Verify START markers come before END markers
  - Verify no nested chunk markers
  - Verify chunk markers align with H2 section boundaries
  - Document result in validation report

### Chunk Marker Alignment Validation

- [ ] [T031] [P1] [US1] Validate chunk markers align with section boundaries in `frontend/docs/chapters/chapter-3.mdx`:
  - Verify each H2 section has exactly one CHUNK: START / CHUNK: END pair
  - Verify chunk markers are placed at logical semantic boundaries
  - Verify chunk markers don't break section structure
  - Document result in validation report

### Chunk File Import Validation

- [ ] [T032] [P1] [US1] Ensure `backend/app/content/chapters/chapter_3_chunks.py` imports correctly:
  - Run: `python -c "from app.content.chapters.chapter_3_chunks import get_chapter_chunks; print('Import successful')"`
  - Expected: No import errors
  - Document result in validation report

### Chunk Function Signature Validation

- [ ] [T033] [P1] [US1] Ensure chunk function uses correct signature in `backend/app/content/chapters/chapter_3_chunks.py`:
  - Verify function `get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]` exists
  - Verify return type is `List[Dict[str, Any]]` (placeholder return acceptable)
  - Verify docstring mentions chunk marker support
  - Document result in validation report

### Chunk Content Non-Empty Validation

- [ ] [T034] [P2] [US1] Validate chunk content is non-empty in `frontend/docs/chapters/chapter-3.mdx`:
  - Verify each chunk marker pair contains content (not empty)
  - Verify chunk content is meaningful (not just whitespace)
  - Note: This validation may be skipped if content is not yet written (acceptable failure)
  - Document result in validation report

**Phase Completion**: All RAG chunk validations pass, results documented

---

## PHASE 5 — FRONTEND VALIDATION TASKS

**User Story**: US2 - System Administrator Ensures Build Stability

**Test Strategy**: Can be tested by running frontend build and verifying no errors.

### Run npm run build

- [ ] [T035] [P1] [US2] Run frontend build command:
  - Run: `cd frontend && npm run build`
  - Expected: Build completes with exit code 0
  - Check for any build errors or warnings related to Chapter 3
  - Document result in validation report

### Check MDX Renders

- [ ] [T036] [P1] [US2] Validate Chapter 3 MDX renders correctly:
  - Verify Chapter 3 page is generated in build output
  - Verify no MDX compilation errors
  - Verify page is accessible in build output
  - Document result in validation report

### Validate Components Render

- [ ] [T037] [P2] [US2] Validate components render correctly (when implemented):
  - Verify HTML comment placeholders don't break rendering
  - Verify diagram placeholders don't break rendering
  - Verify chunk markers don't break rendering
  - Note: This validation checks that placeholders don't cause rendering errors
  - Document result in validation report

**Phase Completion**: All frontend validations pass, results documented

---

## PHASE 6 — BACKEND VALIDATION TASKS

**User Story**: US1 - Developer Validates Chapter 3 Structure

**Test Strategy**: Can be tested by importing backend modules and verifying no errors.

### Validate Chapter Imports

- [ ] [T038] [P1] [US1] Validate chapter imports work correctly:
  - Run: `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA; from app.content.chapters.chapter_3_chunks import get_chapter_chunks; print('Import successful')"`
  - Expected: No import errors, no circular dependencies
  - Document result in validation report

### Validate Runtime Engine Can Load CH3 Metadata

- [ ] [T039] [P2] [US1] Validate runtime engine can load Chapter 3 metadata (future integration):
  - Check that `backend/app/ai/runtime/engine.py` can handle `chapter_id=3` parameter
  - Verify runtime engine recognizes Chapter 3 metadata (check comments/TODOs)
  - Note: This is a future integration check (acceptable if not fully implemented)
  - Document result in validation report

**Phase Completion**: All backend validations pass, results documented

---

## PHASE 7 — VALIDATOR MODULE SCAFFOLDING TASKS

**User Story**: US1 - Developer Validates Chapter 3 Structure

**Test Strategy**: Can be tested by verifying validator modules exist with TODO logic only.

### Create MDX Validator Module

- [ ] [T040] [P1] [US1] Create `backend/app/validators/mdx_validator.py`:
  - Create file with module header
  - Add `validate_mdx_structure()` function with TODO logic only
  - Add placeholder return dictionary
  - No implementation, only scaffolding
  - Document in validation report

### Create Metadata Validator Module

- [ ] [T041] [P1] [US1] Create `backend/app/validators/metadata_validator.py`:
  - Create file with module header
  - Add `validate_metadata_consistency()` function with TODO logic only
  - Add placeholder return dictionary
  - No implementation, only scaffolding
  - Document in validation report

### Create Placeholder Validator Module

- [ ] [T042] [P1] [US1] Create `backend/app/validators/placeholder_validator.py`:
  - Create file with module header
  - Add `validate_placeholders()` function with TODO logic only
  - Add placeholder return dictionary
  - No implementation, only scaffolding
  - Document in validation report

### Create Chunk Validator Module

- [ ] [T043] [P1] [US1] Create `backend/app/validators/chunk_validator.py`:
  - Create file with module header
  - Add `validate_chunk_markers()` function with TODO logic only
  - Add placeholder return dictionary
  - No implementation, only scaffolding
  - Document in validation report

### Create Runtime Checks Module

- [ ] [T044] [P1] [US1] Create `backend/app/validators/runtime_checks.py`:
  - Create file with module header
  - Add `validate_backend_imports()` function with TODO logic only
  - Add `validate_frontend_build()` function with TODO logic only
  - Add placeholder return dictionaries
  - No implementation, only scaffolding
  - Document in validation report

**Phase Completion**: All validator modules created with TODO logic only, results documented

---

## PHASE 8 — VALIDATION REPORT GENERATION TASKS

**User Story**: US1 - Developer Validates Chapter 3 Structure

**Test Strategy**: Can be tested by verifying validation report is generated with all results.

### Populate Validation Report

- [ ] [T045] [P1] [US1] Populate validation report at `specs/019-chapter-3-validation/checklists/validation-report.md`:
  - Update validation report template with all validation results from Phases 1-6
  - Include pass/fail status for each validation category
  - Include detailed results for each validation check
  - Include any warnings or acceptable failures
  - Document overall validation status

### Generate Validation Summary

- [ ] [T046] [P1] [US1] Generate validation summary:
  - Count total validations run
  - Count total validations passed
  - Count total validations failed
  - Count total acceptable failures
  - Calculate pass rate
  - Document in validation report

**Phase Completion**: Validation report generated with all results, summary documented

---

## PHASE 9 — FINAL ACCEPTANCE TASKS

**User Story**: US1, US2, US3 - All User Stories

**Test Strategy**: Can be tested by verifying all success criteria from spec.md are met.

### Validate All Success Criteria from spec.md

- [ ] [T047] [P1] [US1] Validate all success criteria from spec.md:
  - Check MDX file compiles with zero warnings (from Phase 5)
  - Check metadata structurally correct (from Phase 3)
  - Check all placeholders match schema contracts (from Phase 2)
  - Check chunking correct and future-compatible (from Phase 4)
  - Check backend imports cleanly (from Phase 6)
  - Check ready for Feature 020 (future integration)
  - Document in validation report

### Validate Folder Structure

- [ ] [T048] [P1] [US1] Validate folder structure:
  - Verify `specs/019-chapter-3-validation/` directory exists
  - Verify `specs/019-chapter-3-validation/contracts/` directory exists
  - Verify `specs/019-chapter-3-validation/checklists/` directory exists
  - Verify `backend/app/validators/` directory exists
  - Verify all validator modules exist (from Phase 7)
  - Document in validation report

### Validate Build Stability

- [ ] [T049] [P1] [US2] Validate build stability:
  - Verify frontend build passes (from Phase 5)
  - Verify backend imports work (from Phase 6)
  - Verify no circular dependencies
  - Verify no broken imports
  - Document in validation report

**Phase Completion**: All acceptance criteria validated, results documented

---

## Summary

**Total Tasks**: 49 tasks across 9 phases

**Phases**:
1. Phase 0: Setup & Prerequisites (8 tasks)
2. Phase 1: MDX Structure Validation (5 tasks)
3. Phase 2: Placeholder Validation (6 tasks)
4. Phase 3: Metadata Validation (9 tasks)
5. Phase 4: RAG Chunk Validation (6 tasks)
6. Phase 5: Frontend Validation (3 tasks)
7. Phase 6: Backend Validation (2 tasks)
8. Phase 7: Validator Module Scaffolding (5 tasks)
9. Phase 8: Validation Report Generation (2 tasks)
10. Phase 9: Final Acceptance (3 tasks)

**Priority Distribution**:
- P1 (Critical): 45 tasks
- P2 (Important): 4 tasks
- P3 (Nice-to-have): 0 tasks

**Dependencies**:
- Feature 017 (Chapter 3 Content) - must be complete
- Feature 018 (Chapter 3 Planning Layer) - must be complete

**Success Criteria**:
- All P1 tasks completed
- All validation checks pass (or acceptable failures documented)
- Validation report generated
- Frontend build passes
- Backend imports work
- Validator modules created (scaffold only)

---

Tasks complete — Ready for /sp.implement.
