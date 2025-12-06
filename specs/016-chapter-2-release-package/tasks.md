# Tasks: Chapter 2 Release Packaging Layer

**Feature**: 016-chapter-2-release-package | **Branch**: `016-chapter-2-release-package` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for packaging Chapter 2 content, metadata, RAG chunks, AI-block runtime stubs, validation artifacts, and contracts into a release directory. No new features; only packaging (copy-only operations).

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), US3 (User Story 3), SETUP (Initial setup), PACKAGING (Packaging tasks)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before packaging.

- [ ] [T001] [P1] [SETUP] Verify Feature 014 is complete: Check that `frontend/docs/chapters/chapter-2.mdx` exists with 7 sections
- [ ] [T002] [P1] [SETUP] Verify Feature 011 is complete: Check that AI-block React components exist in `frontend/src/components/ai/`
- [ ] [T003] [P1] [SETUP] Verify Feature 012 is complete: Check that `backend/app/content/chapters/chapter_2_chunks.py` exists
- [ ] [T004] [P1] [SETUP] Verify Feature 013 is complete: Check that `backend/app/ai/subagents/ch2_*.py` files exist (4 files)
- [ ] [T005] [P1] [SETUP] Verify Feature 015 is complete: Check that `specs/015-chapter-2-validation/checklists/validation-report.md` exists
- [ ] [T006] [P1] [SETUP] Verify releases directory exists: Check that `releases/` directory exists (create if needed)
- [ ] [T007] [P1] [SETUP] Verify write permissions: Check that `releases/` directory is writable

**Success Criteria**:
- All prerequisite files and directories exist
- All dependent features (010-015) are complete
- Ready to create release package

**Dependencies**: Feature 010, 011, 012, 013, 014, 015 (all must be complete)

---

## PHASE 1 — Folder Setup

**User Story**: US1 - Release Manager Packages Chapter 2 for Distribution

**Test Strategy**: Can be tested by verifying all folders exist at specified paths.

### Root Directory Creation

- [ ] [T008] [P1] [US1] Create `releases/chapter-2/` root directory:
  - Create folder if it doesn't exist
  - Verify folder creation succeeds
  - Document result

### Subfolder Creation

- [ ] [T009] [P1] [US1] Create `releases/chapter-2/content/` subfolder:
  - Create folder
  - Verify folder exists

- [ ] [T010] [P1] [US1] Create `releases/chapter-2/metadata/` subfolder:
  - Create folder
  - Verify folder exists

- [ ] [T011] [P1] [US1] Create `releases/chapter-2/rag/` subfolder:
  - Create folder
  - Verify folder exists

- [ ] [T012] [P1] [US1] Create `releases/chapter-2/ai-blocks/` subfolder:
  - Create folder
  - Verify folder exists

- [ ] [T013] [P1] [US1] Create `releases/chapter-2/contracts/` subfolder:
  - Create folder
  - Verify folder exists

- [ ] [T014] [P1] [US1] Create `releases/chapter-2/diagrams/` subfolder:
  - Create folder
  - Verify folder exists

- [ ] [T015] [P1] [US1] Create `releases/chapter-2/validation/` subfolder:
  - Create folder
  - Verify folder exists

**Phase Completion**: All 7 subfolders created and verified

---

## PHASE 2 — Content Packaging

**User Story**: US1 - Release Manager Packages Chapter 2 for Distribution

**Test Strategy**: Can be tested by verifying MDX file is copied correctly and contents are preserved.

### MDX File Copy

- [ ] [T016] [P1] [US1] Copy `frontend/docs/chapters/chapter-2.mdx` → `releases/chapter-2/content/chapter-2.mdx`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file size matches source
  - Document result

### Frontmatter Preservation

- [ ] [T017] [P1] [US1] Ensure frontmatter is intact in `releases/chapter-2/content/chapter-2.mdx`:
  - Check YAML frontmatter exists (title, description, sidebar_position, sidebar_label, tags)
  - Verify frontmatter values match source
  - Verify no modifications made
  - Document result

### Content Completeness

- [ ] [T018] [P1] [US1] Verify content completeness in `releases/chapter-2/content/chapter-2.mdx`:
  - Check 7 H2 sections are present
  - Check 4 diagram placeholders are present
  - Check 4 AI-block components are present
  - Check 7 glossary terms are present
  - Verify all content preserved
  - Document result

**Phase Completion**: MDX file copied correctly, frontmatter preserved, all content included

---

## PHASE 3 — Metadata Packaging

**User Story**: US1 - Release Manager Packages Chapter 2 for Distribution

**Test Strategy**: Can be tested by verifying metadata files are copied correctly and contents are preserved.

### Chapter Metadata Copy

- [ ] [T019] [P1] [US1] Copy `backend/app/content/chapters/chapter_2.py` → `releases/chapter-2/metadata/chapter_2.py`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Verify no modifications made
  - Document result

### Chunk File Copy

- [ ] [T020] [P1] [US1] Copy `backend/app/content/chapters/chapter_2_chunks.py` → `releases/chapter-2/rag/chapter_2_chunks.py`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Verify function signature preserved
  - Verify no modifications made
  - Document result

**Phase Completion**: Both metadata files copied correctly, contents preserved

---

## PHASE 4 — AI Runtime Packaging

**User Story**: US1 - Release Manager Packages Chapter 2 for Distribution

**Test Strategy**: Can be tested by verifying all AI runtime files are copied correctly.

### AI Blocks API Copy

- [ ] [T021] [P1] [US1] Copy `backend/app/api/ai_blocks.py` → `releases/chapter-2/ai-blocks/ai_blocks.py`:
  - Copy file from source to destination (or copy Chapter 2 excerpts if file is large)
  - Verify file exists at destination
  - Verify Chapter 2 routing logic present (TODOs acceptable)
  - Verify file contents preserved
  - Document result

### Subagent Files Copy

- [ ] [T022] [P1] [US1] Copy `backend/app/ai/subagents/ch2_ask_question_agent.py` → `releases/chapter-2/ai-blocks/ch2_ask_question_agent.py`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Document result

- [ ] [T023] [P1] [US1] Copy `backend/app/ai/subagents/ch2_explain_el10_agent.py` → `releases/chapter-2/ai-blocks/ch2_explain_el10_agent.py`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Document result

- [ ] [T024] [P1] [US1] Copy `backend/app/ai/subagents/ch2_quiz_agent.py` → `releases/chapter-2/ai-blocks/ch2_quiz_agent.py`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Document result

- [ ] [T025] [P1] [US1] Copy `backend/app/ai/subagents/ch2_diagram_agent.py` → `releases/chapter-2/ai-blocks/ch2_diagram_agent.py`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Document result

### Skills Copy (if Chapter 2-specific)

- [ ] [T026] [P2] [US1] Check for Chapter 2-specific skills in `backend/app/ai/skills/`:
  - Check if any skills are Chapter 2-specific
  - If found, copy to `releases/chapter-2/ai-blocks/`
  - Verify file contents preserved
  - Document result (or note "No Chapter 2-specific skills found")

**Phase Completion**: All AI runtime files copied correctly (5 files: ai_blocks.py + 4 subagents)

---

## PHASE 5 — Contracts Packaging

**User Story**: US1 - Release Manager Packages Chapter 2 for Distribution

**Test Strategy**: Can be tested by verifying all contract files are copied correctly.

### Specification Files Copy

- [ ] [T027] [P1] [US1] Copy `specs/014-chapter-2-content/spec.md` → `releases/chapter-2/contracts/spec.md`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Document result

- [ ] [T028] [P1] [US1] Copy `specs/014-chapter-2-content/plan.md` → `releases/chapter-2/contracts/plan.md`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Document result

- [ ] [T029] [P1] [US1] Copy `specs/014-chapter-2-content/tasks.md` → `releases/chapter-2/contracts/tasks.md`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Document result

### Content Schema Copy

- [ ] [T030] [P1] [US1] Copy `specs/014-chapter-2-content/contracts/content-schema.md` → `releases/chapter-2/contracts/content-schema.md`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Document result

**Phase Completion**: All 4 contract files copied correctly

---

## PHASE 6 — Validation Packaging

**User Story**: US1 - Release Manager Packages Chapter 2 for Distribution

**Test Strategy**: Can be tested by verifying validation files are copied correctly.

### Validation Report Copy

- [ ] [T031] [P1] [US1] Copy `specs/015-chapter-2-validation/checklists/validation-report.md` → `releases/chapter-2/validation/validation-report.md`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Verify validation results are included (7 categories, all PASS)
  - Document result

### Validation Schema Copy

- [ ] [T032] [P1] [US1] Copy `specs/015-chapter-2-validation/contracts/validation-schema.md` → `releases/chapter-2/validation/validation-schema.md`:
  - Copy file from source to destination
  - Verify file exists at destination
  - Verify file contents preserved
  - Document result

**Phase Completion**: Both validation files copied correctly

---

## PHASE 7 — README

**User Story**: US1, US2, US3 - All User Stories

**Test Strategy**: Can be tested by verifying README.md exists and contains all required sections.

### README Generation

- [ ] [T033] [P1] [US1] Generate `releases/chapter-2/README.md`:
  - Create file with comprehensive documentation
  - Include all required sections (see plan.md Section 5 for structure)
  - Verify file exists
  - Document result

### Overview Section

- [ ] [T034] [P1] [US1] Add Overview section to `releases/chapter-2/README.md`:
  - Chapter 2 purpose and overview
  - What Chapter 2 covers (ROS 2 fundamentals)
  - Target audience (beginners with Chapter 1 prerequisite)
  - Learning objectives (from metadata)
  - Verify section is complete

### File Structure Section

- [ ] [T035] [P1] [US1] Add File Structure Overview section to `releases/chapter-2/README.md`:
  - Directory layout diagram
  - Description of each folder
  - Description of key files
  - File organization rationale
  - Verify section is complete

### AI-Block Runtime Section

- [ ] [T036] [P1] [US1] Add "How AI-Block Runtime Works" section to `releases/chapter-2/README.md`:
  - Explanation of Chapter 2 AI-block integration
  - How AI blocks are structured (4 types)
  - How subagents work (ch2_* agents)
  - How runtime engine routes Chapter 2 requests
  - Placeholder responses (scaffolding phase)
  - Verify section is complete

### RAG Pipeline Section

- [ ] [T037] [P1] [US1] Add "How RAG Pipeline Consumes Chapter 2" section to `releases/chapter-2/README.md`:
  - Explanation of RAG integration for Chapter 2
  - How chunk file provides content
  - How embeddings will be generated (future)
  - How Qdrant collection stores Chapter 2 chunks
  - Pipeline flow for Chapter 2
  - Verify section is complete

### Build Instructions Section

- [ ] [T038] [P1] [US1] Add Build Instructions section to `releases/chapter-2/README.md`:
  - Frontend build steps (npm install, npm run build)
  - Backend startup steps (pip install, uvicorn)
  - Environment setup
  - Dependencies
  - Verify section is complete

### Testing Instructions Section

- [ ] [T039] [P1] [US1] Add Testing Instructions section to `releases/chapter-2/README.md`:
  - How to run validation tests
  - How to run API tests
  - How to verify package completeness
  - Verify section is complete

### Integration Instructions Section

- [ ] [T040] [P1] [US1] Add Integration Instructions section to `releases/chapter-2/README.md`:
  - Standalone usage (for judges)
  - Integrated usage (full book)
  - Import path considerations
  - Integration steps
  - Verify section is complete

**Phase Completion**: README.md generated with all 7 required sections

---

## PHASE 8 — Final Consistency Check

**User Story**: US1, US2, US3 - All User Stories

**Test Strategy**: Can be tested by verifying all files exist and package is complete.

### File Existence Check

- [ ] [T041] [P1] [US1] Ensure all expected files present in `releases/chapter-2/`:
  - Check `content/chapter-2.mdx` exists
  - Check `metadata/chapter_2.py` exists
  - Check `rag/chapter_2_chunks.py` exists
  - Check `ai-blocks/` contains 5 files (ai_blocks.py + 4 subagents)
  - Check `contracts/` contains 4 files (spec.md, plan.md, tasks.md, content-schema.md)
  - Check `validation/` contains 2 files (validation-report.md, validation-schema.md)
  - Check `README.md` exists
  - Document result

### Content Validation

- [ ] [T042] [P1] [US1] Validate content in `releases/chapter-2/content/chapter-2.mdx`:
  - Verify 7 H2 sections present
  - Verify 4 diagram placeholders present
  - Verify 4 AI-block components present
  - Verify 7 glossary terms present
  - Verify frontmatter complete
  - Document result

### Metadata Validation

- [ ] [T043] [P1] [US1] Validate metadata in `releases/chapter-2/metadata/chapter_2.py`:
  - Verify all required fields present
  - Verify section_count: 7
  - Verify ai_blocks: 4 items
  - Verify diagram_placeholders: 4 items
  - Verify glossary_terms: 7 items
  - Document result

### Consistency Check

- [ ] [T044] [P1] [US1] Ensure placeholders in MDX match metadata:
  - Extract diagram placeholders from MDX
  - Compare with metadata diagram_placeholders
  - Extract AI-block components from MDX
  - Compare with metadata ai_blocks
  - Extract glossary terms from MDX
  - Compare with metadata glossary_terms
  - Verify all match
  - Document result

### RAG Chunks Validation

- [ ] [T045] [P1] [US1] Ensure RAG chunks exist in `releases/chapter-2/rag/chapter_2_chunks.py`:
  - Verify file exists
  - Verify function `get_chapter_chunks(chapter_id: int = 2)` exists
  - Verify function signature is correct
  - Verify return type is `List[Dict[str, Any]]`
  - Document result

### Runtime Engine References Validation

- [ ] [T046] [P1] [US1] Ensure runtime engine references exist:
  - Verify all 4 subagent files exist in `ai-blocks/`
  - Verify `ai_blocks.py` has Chapter 2 routing (TODOs acceptable)
  - Verify all files reference Chapter 2
  - Document result

### Import Path Validation

- [ ] [T047] [P2] [US1] Ensure no missing imports or filenames in packaged structure:
  - Check for import statements in copied files
  - Document import path differences (if any)
  - Note in README.md that imports may need adjustment for standalone usage
  - Document result

### Standalone Package Validation

- [ ] [T048] [P1] [US1] Validate that chapter can be delivered as standalone package:
  - Review README.md for standalone context
  - Verify all required files present
  - Verify validation reports provide context
  - Verify contracts provide specifications
  - Verify package is self-contained
  - Document result

**Phase Completion**: All consistency checks pass, package is complete and ready for distribution

---

## Summary

**Total Tasks**: 48 tasks across 8 phases
- Phase 0: Setup & Prerequisites (7 tasks)
- Phase 1: Folder Setup (8 tasks)
- Phase 2: Content Packaging (3 tasks)
- Phase 3: Metadata Packaging (2 tasks)
- Phase 4: AI Runtime Packaging (6 tasks)
- Phase 5: Contracts Packaging (4 tasks)
- Phase 6: Validation Packaging (2 tasks)
- Phase 7: README (8 tasks)
- Phase 8: Final Consistency Check (8 tasks)

**Estimated Time**: ~1-2 hours (file copying and README generation)

**Success Criteria**:
- Release folder structure created with all 7 subfolders
- All content files copied correctly (MDX with frontmatter preserved)
- All metadata files copied correctly (chapter_2.py, chapter_2_chunks.py)
- All AI runtime files copied correctly (5 files: ai_blocks.py + 4 subagents)
- All contracts copied correctly (4 files)
- All validation reports copied correctly (2 files)
- README.md generated with all 7 required sections
- Release consistency check passes
- No missing components
- No code modifications made (copy-only)

**Next Step**: Run `/sp.implement` to execute all packaging tasks
