# Tasks: Chapter 2 — Build Validation + Release Packaging Layer

**Feature**: 036-ch2-build-release | **Branch**: `036-ch2-build-release` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating validation and release packaging scaffolding (validation scripts, build checks, release folder structure, package script). All tasks are scaffolding only—no real validation or packaging logic implementation.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category`: SETUP (Initial setup), FRONTEND (Frontend validation), BACKEND (Backend validation), BUILD (Build stability), RELEASE (Release packaging), CONTRACT (Contracts/checklists), VALIDATION (Final validation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prepare directory structure.

- [ ] [T001] [P1] [SETUP] Verify Feature 033 (Chapter 2 Content) is complete: Check that `frontend/docs/chapters/chapter-2.mdx` and `backend/app/content/chapters/chapter_2.py` exist
- [ ] [T002] [P1] [SETUP] Verify Feature 034 (Chapter 2 AI Blocks) is complete: Check that Chapter 2 subagents exist in `backend/app/ai/subagents/`
- [ ] [T003] [P1] [SETUP] Verify Feature 035 (Chapter 2 RAG Integration) is complete: Check that `backend/app/ai/rag/ch2_pipeline.py` exists
- [ ] [T004] [P1] [SETUP] Create directory structure: `scripts/ch2/` (if not exists)
- [ ] [T005] [P1] [SETUP] Create directory structure: `backend/app/validation/` (if not exists)
- [ ] [T006] [P1] [SETUP] Create directory structure: `release/chapter-2/` (if not exists)
- [ ] [T007] [P1] [SETUP] Verify backend starts successfully: Run `cd backend && python -c "from app.main import app; print('Backend imports OK')"` to confirm no errors
- [ ] [T008] [P1] [SETUP] Verify frontend structure exists: Check `frontend/docs/chapters/` directory exists

**Success Criteria**:
- All prerequisite features complete
- Directory structure ready
- Backend starts without errors

**Dependencies**: Feature 033, Feature 034, Feature 035 must be complete

---

## PHASE 1 — FRONTEND VALIDATION

**User Story**: US1 - Developer Validates Chapter 2 Build

**Test Strategy**: Can be tested by creating validation scripts with placeholder functions and verifying imports work.

### Create MDX Structure Validation Script

- [ ] [T009] [P1] [FRONTEND] Create new file `scripts/ch2/validate_mdx_structure.py`:
  - Add file header comment: `"""Chapter 2 MDX Structure Validation - Validates H2 sections, diagram placeholders, AI-block placeholders, and glossary terms."""`
  - Add imports: `from typing import Dict, Any, List`

- [ ] [T010] [P1] [FRONTEND] Add `validate_mdx_structure()` function to `scripts/ch2/validate_mdx_structure.py`:
  - Function signature: `def validate_mdx_structure(mdx_path: str) -> Dict[str, Any]:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Validate H2 sections count (expected: 7 sections)`
    - `# TODO: Check diagram placeholders exist (expected: 4 placeholders)`
    - `# TODO: Check AI-block placeholders exist (expected: 4 placeholders)`
    - `# TODO: Check glossary terms exist (expected: 7 terms)`
    - `# TODO: Read MDX file from mdx_path`
    - `# TODO: Parse H2 sections`
    - `# TODO: Count diagram placeholders`
    - `# TODO: Count AI-block placeholders`
    - `# TODO: Count glossary terms`
    - `# TODO: Return validation results`
  - Placeholder return: `return {"valid": False, "errors": [], "warnings": [], "sections_count": 0, "diagram_count": 0, "ai_block_count": 0, "glossary_count": 0}`

- [ ] [T011] [P1] [FRONTEND] Verify validate_mdx_structure.py is importable: Run `cd scripts/ch2 && python -c "from validate_mdx_structure import validate_mdx_structure; print('Import successful')"` - should complete without errors

**Acceptance Test**: MDX structure validation script has validate_mdx_structure() function with comprehensive TODO comments, imports work, function returns placeholder dict

---

### Create Frontmatter Validation Script

- [ ] [T012] [P1] [FRONTEND] Create new file `scripts/ch2/validate_frontmatter.py`:
  - Add file header comment: `"""Chapter 2 Frontmatter Validation - Validates frontmatter fields match schema."""`
  - Add imports: `from typing import Dict, Any`

- [ ] [T013] [P1] [FRONTEND] Add `validate_frontmatter()` function to `scripts/ch2/validate_frontmatter.py`:
  - Function signature: `def validate_frontmatter(mdx_path: str) -> Dict[str, Any]:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Verify frontmatter fields match schema`
    - `# TODO: Check required fields: title, description, sidebar_position, sidebar_label, tags`
    - `# TODO: Validate field types and formats`
    - `# TODO: Read MDX file from mdx_path`
    - `# TODO: Parse frontmatter YAML`
    - `# TODO: Check required fields`
    - `# TODO: Validate field types`
    - `# TODO: Return validation results`
  - Placeholder return: `return {"valid": False, "errors": [], "warnings": [], "fields": {}}`

- [ ] [T014] [P1] [FRONTEND] Verify validate_frontmatter.py is importable: Run `cd scripts/ch2 && python -c "from validate_frontmatter import validate_frontmatter; print('Import successful')"` - should complete without errors

**Acceptance Test**: Frontmatter validation script has validate_frontmatter() function with comprehensive TODO comments, imports work, function returns placeholder dict

---

## PHASE 2 — BACKEND VALIDATION

**User Story**: US1 - Developer Validates Chapter 2 Build

**Test Strategy**: Can be tested by creating backend validation script with placeholder function and verifying imports work.

### Create Backend Metadata Validator

- [ ] [T015] [P1] [BACKEND] Create new file `backend/app/validation/ch2_metadata_validator.py`:
  - Add file header comment: `"""Chapter 2 Metadata Validation - Validates metadata consistency between chapter_2.py and chapter-2.mdx."""`
  - Add imports: `from typing import Dict, Any, List`

- [ ] [T016] [P1] [BACKEND] Add `validate_ch2_metadata()` function to `backend/app/validation/ch2_metadata_validator.py`:
  - Function signature: `def validate_ch2_metadata() -> Dict[str, Any]:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Cross-check metadata vs mdx structure`
    - `# TODO: Check sections names match between MDX and chapter_2.py`
    - `# TODO: Check diagram + AI block count matches`
    - `# TODO: Validate metadata imports without errors`
    - `# TODO: Import chapter_2.py metadata`
    - `# TODO: Read chapter-2.mdx file`
    - `# TODO: Compare section counts`
    - `# TODO: Compare section names`
    - `# TODO: Compare placeholder counts`
    - `# TODO: Return validation results`
  - Placeholder return: `return {"valid": False, "errors": [], "warnings": [], "metadata": {}, "mdx_structure": {}}`

- [ ] [T017] [P1] [BACKEND] Verify ch2_metadata_validator.py is importable: Run `cd backend && python -c "from app.validation.ch2_metadata_validator import validate_ch2_metadata; print('Import successful')"` - should complete without errors

**Acceptance Test**: Backend metadata validator has validate_ch2_metadata() function with comprehensive TODO comments, imports work, function returns placeholder dict

---

## PHASE 3 — BUILD STABILITY

**User Story**: US1 - Developer Validates Chapter 2 Build

**Test Strategy**: Can be tested by creating run_all.py script and updating package.json, then verifying command works.

### Create Build Check Orchestration Script

- [ ] [T018] [P1] [BUILD] Create new file `scripts/ch2/run_all.py`:
  - Add file header comment: `"""Chapter 2 Validation Orchestration - Runs all validation checks for Chapter 2."""`
  - Add placeholder imports:
    - `# TODO: from validate_mdx_structure import validate_mdx_structure`
    - `# TODO: from validate_frontmatter import validate_frontmatter`
    - `# TODO: import sys`
    - `# TODO: from pathlib import Path`

- [ ] [T019] [P1] [BUILD] Add placeholder main function to `scripts/ch2/run_all.py`:
  - Function signature: `def main() -> int:`
  - Add comprehensive TODO comments:
    - `# TODO: Run frontend validations`
    - `# TODO:     Run validate_mdx_structure`
    - `# TODO:     Run validate_frontmatter`
    - `# TODO: Run backend validations`
    - `# TODO:     Run validate_ch2_metadata`
    - `# TODO: Check frontend build`
    - `# TODO:     Run npm run build`
    - `# TODO: Check backend startup`
    - `# TODO:     Verify backend starts without errors`
    - `# TODO: Generate validation report`
    - `# TODO: Return exit code (0 for success, 1 for failure)`
  - Placeholder return: `return 0`
  - Add `if __name__ == "__main__":` block with `sys.exit(main())`

- [ ] [T020] [P1] [BUILD] Verify run_all.py is importable: Run `cd scripts/ch2 && python -c "from run_all import main; print('Import successful')"` - should complete without errors

**Acceptance Test**: Build check script has main() function with comprehensive TODO comments, imports work, function returns placeholder exit code

---

### Update Package.json

- [ ] [T021] [P1] [BUILD] Update `package.json` to add validation command:
  - Add command: `"validate:ch2": "python scripts/ch2/run_all.py"`
  - Ensure command is in "scripts" section
  - Verify JSON syntax is valid

- [ ] [T022] [P1] [BUILD] Verify package.json is valid JSON: Run `node -e "JSON.parse(require('fs').readFileSync('package.json', 'utf8')); console.log('Valid JSON')"` - should complete without errors

**Acceptance Test**: package.json has validate:ch2 command, JSON syntax is valid

---

## PHASE 4 — RELEASE PACKAGING

**User Story**: US2 - Release Manager Packages Chapter 2

**Test Strategy**: Can be tested by creating release folder structure and package script, then verifying files exist.

### Create Release Folder Structure

- [ ] [T023] [P1] [RELEASE] Create `release/chapter-2/README.md`:
  - Add placeholder content:
    - `# Chapter 2 Release Package`
    - `## Overview`
    - `This is a placeholder README for Chapter 2 release package.`
    - `## File Structure`
    - `TODO: Document release package structure`
    - `## Usage`
    - `TODO: Document usage instructions`

- [ ] [T024] [P1] [RELEASE] Create `release/chapter-2/CHANGELOG.md`:
  - Add placeholder content:
    - `# Changelog - Chapter 2`
    - `## Version 1.0.0`
    - `TODO: Document version history`
    - `TODO: Document features included`
    - `TODO: Document changes`

- [ ] [T025] [P1] [RELEASE] Create `release/chapter-2/chapter-2-export.json`:
  - Add placeholder JSON structure:
    ```json
    {
      "chapter_id": 2,
      "title": "Chapter 2 — The Foundations of Mechanical Systems",
      "version": "1.0.0",
      "metadata": {},
      "content": {},
      "rag": {},
      "ai_blocks": {},
      "validation": {}
    }
    ```

- [ ] [T026] [P1] [RELEASE] Create `release/chapter-2/assets/` folder:
  - Create empty folder (no files)

**Acceptance Test**: Release folder structure exists with README.md, CHANGELOG.md, chapter-2-export.json, and assets/ folder

---

### Create Package Release Script

- [ ] [T027] [P1] [RELEASE] Create new file `scripts/ch2/package_release.py`:
  - Add file header comment: `"""Chapter 2 Release Packaging - Packages Chapter 2 for release."""`
  - Add imports: `from typing import Dict, Any`
  - Add placeholder imports:
    - `# TODO: from pathlib import Path`
    - `# TODO: import json`

- [ ] [T028] [P1] [RELEASE] Add `package_chapter_2()` function to `scripts/ch2/package_release.py`:
  - Function signature: `def package_chapter_2() -> None:`
  - Add comprehensive docstring with TODO comments:
    - `# TODO: Gather metadata from chapter_2.py`
    - `# TODO: Gather MDX content from chapter-2.mdx`
    - `# TODO: Gather diagrams (future)`
    - `# TODO: Gather RAG chunks (future)`
    - `# TODO: Gather AI block info (future)`
    - `# TODO: Write chapter-2-export.json`
    - `# TODO: Create release folder structure`
    - `# TODO: Copy files to release folder`
  - Placeholder return: `pass`

- [ ] [T029] [P1] [RELEASE] Verify package_release.py is importable: Run `cd scripts/ch2 && python -c "from package_release import package_chapter_2; print('Import successful')"` - should complete without errors

**Acceptance Test**: Package release script has package_chapter_2() function with comprehensive TODO comments, imports work, function returns None

---

## PHASE 5 — CONTRACTS + CHECKLIST

**User Story**: US1 - Developer Validates Chapter 2 Build

**Test Strategy**: Can be tested by verifying contract and checklist files exist.

### Verify Contracts

- [ ] [T030] [P1] [CONTRACT] Verify `specs/036-ch2-build-release/contracts/validation-rules.md` exists:
  - Check file exists (already created in spec phase)
  - Verify documents high-level validation rules
  - Verify documents release packaging rules

**Acceptance Test**: Contract file exists and documents validation rules

---

### Verify Checklists

- [ ] [T031] [P1] [CONTRACT] Verify `specs/036-ch2-build-release/checklists/release.md` exists:
  - Check file exists (already created in spec phase)
  - Verify includes build validation checklist
  - Verify includes metadata validation checklist
  - Verify includes AI-block routing checklist
  - Verify includes RAG pipeline checklist

**Acceptance Test**: Checklist file exists with release checklist

---

## PHASE 6 — VALIDATION

**User Story**: US1 - Developer Validates Chapter 2 Build

**Test Strategy**: Can be tested by verifying all files exist, imports work, backend starts, and frontend builds.

### Final Validation

- [ ] [T032] [P1] [VALIDATION] Verify all files exist:
  - Check: `scripts/ch2/validate_mdx_structure.py` (exists)
  - Check: `scripts/ch2/validate_frontmatter.py` (exists)
  - Check: `backend/app/validation/ch2_metadata_validator.py` (exists)
  - Check: `scripts/ch2/run_all.py` (exists)
  - Check: `scripts/ch2/package_release.py` (exists)
  - Check: `release/chapter-2/README.md` (exists)
  - Check: `release/chapter-2/CHANGELOG.md` (exists)
  - Check: `release/chapter-2/chapter-2-export.json` (exists)
  - Check: `release/chapter-2/assets/` (exists)

- [ ] [T033] [P1] [VALIDATION] Verify backend starts without errors:
  - Run: `cd backend && python -c "from app.main import app; print('Backend starts OK')"`
  - Expected: No import errors or runtime exceptions

- [ ] [T034] [P1] [VALIDATION] Verify frontend builds without errors:
  - Run: `cd frontend && npm run build`
  - Expected: Build completes successfully (or at least no errors from new files)

- [ ] [T035] [P1] [VALIDATION] Verify all imports resolve:
  - Test validate_mdx_structure imports
  - Test validate_frontmatter imports
  - Test ch2_metadata_validator imports
  - Test run_all imports
  - Test package_release imports

- [ ] [T036] [P1] [VALIDATION] Verify package.json command exists:
  - Check: `npm run validate:ch2` command exists
  - Expected: Command is defined in package.json

**Acceptance Test**: All files exist, backend starts without errors, frontend builds without errors, all imports resolve successfully, package.json command exists

---

## Summary

**Total Tasks**: 36 tasks across 6 phases
**Estimated Time**: 1-2 hours (scaffolding only, no business logic)
**Complexity**: Low (scaffolding, following existing patterns)

**Success Criteria**:
- ✅ All validation and release folders exist
- ✅ All scripts contain placeholder logic only
- ✅ package.json updated with validation command
- ✅ Release folder structure created
- ✅ Backend and frontend build without errors
- ✅ No real validation or packaging logic implemented
- ✅ Contract file exists and documents validation rules
- ✅ Checklist file exists with release checklist

**Next Steps**: Proceed to `/sp.implement` to execute all tasks in order.

