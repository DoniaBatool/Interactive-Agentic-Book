# Implementation Plan: Chapter 2 — Build Validation + Release Packaging Layer

**Branch**: `036-ch2-build-release` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/036-ch2-build-release/spec.md`

## Summary

This feature creates all validation, QA checks, and release packaging scaffolding for Chapter 2. The implementation ensures that Chapter 2 content, metadata, RAG integration, and AI blocks compile cleanly in both frontend and backend. The feature adds automated validation placeholders and creates a release package folder for exporting Chapter 2 as a standalone release unit. **No real validation or packaging logic is implemented**—only scaffolding, function signatures, TODO placeholders, and architectural blueprints to prepare for future validation and release implementation.

**Primary Deliverable**: Complete validation and release packaging scaffolding (frontend validation scripts, backend validation scripts, build check layer, release folder structure, package script, contracts, checklists)
**Validation**: All files exist, imports resolve, backend starts, frontend builds, no runtime errors

## Technical Context

**Language/Version**:
- Frontend: MDX (Markdown + JSX) compatible with Docusaurus 3.x
- Backend: Python 3.11+ with FastAPI 0.109+
- Scripts: Python 3.11+

**Primary Dependencies**:
- FastAPI 0.109+, Pydantic 2.x (already installed)
- Docusaurus 3.x (already installed)
- No new runtime dependencies required (scaffolding only)
- Feature 033 (Chapter 2 Content) - MDX file and metadata exist
- Feature 034 (Chapter 2 AI Blocks Integration) - Subagents exist
- Feature 035 (Chapter 2 RAG Integration) - RAG pipeline exists

**Storage**: 
- No persistent storage (scaffolding only)
- Release folder structure for future export

**Testing**:
- Manual: File existence verification, import resolution, backend startup, frontend build
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Frontend: Web browsers via Docusaurus static site
- Backend: Server-side Python (Uvicorn/FastAPI environment)
- Scripts: Command-line Python scripts

**Project Type**: Validation and release packaging scaffolding

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- Frontend build: < 30 seconds (no new content)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real validation logic (no parsing, no checking, no real validation)
- MUST NOT implement real packaging logic (no file copying, no JSON generation)
- MUST maintain compatibility with Feature 033, 034, 035 (Chapter 2 features must still work)
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions
- MUST NOT break existing backend or frontend functionality
- MUST follow Chapter 1 validation patterns (Feature 009) exactly

**Scale/Scope**:
- 3 validation script files to create (2 frontend, 1 backend)
- 1 build check script to create (run_all.py)
- 1 package script to create (package_release.py)
- 1 package.json to update (add validation command)
- 1 release folder structure to create (4 files + assets folder)
- 2 contract/checklist files to create
- ~200-300 lines of scaffolding code (mostly signatures, TODOs, and comments)

---

## 1. Folder Structure Plan

### 1.1 New Files

**Directory**: `scripts/ch2/`
- **Status**: Create new directory
- **Files to Create**:
  - `validate_mdx_structure.py` (NEW - MDX structure validation)
  - `validate_frontmatter.py` (NEW - Frontmatter validation)
  - `run_all.py` (NEW - Orchestration script)
  - `package_release.py` (NEW - Release packaging script)

**Directory**: `backend/app/validation/`
- **Status**: Already exists (from Feature 009) or create if needed
- **Files to Create**:
  - `ch2_metadata_validator.py` (NEW - Backend metadata validation)

**Directory**: `release/chapter-2/`
- **Status**: Create new directory
- **Files to Create**:
  - `README.md` (NEW - Release package overview)
  - `CHANGELOG.md` (NEW - Version history)
  - `chapter-2-export.json` (NEW - Structured export data)
  - `assets/` (NEW - Empty folder for future assets)

### 1.2 Existing Directories (To Be Extended)

**Directory**: `package.json`
- **Status**: Already exists (from Feature 001)
- **Files to Update**:
  - `package.json` (add validate:ch2 command)

**Directory**: `specs/036-ch2-build-release/contracts/`
- **Status**: Already exists (from spec phase)
- **Files to Verify**:
  - `validation-rules.md` (verify exists from spec phase)

**Directory**: `specs/036-ch2-build-release/checklists/`
- **Status**: Already exists (from spec phase)
- **Files to Verify**:
  - `release.md` (verify exists from spec phase)

---

## 2. Frontend Validation Architecture

### 2.1 MDX Structure Validation

**File**: `scripts/ch2/validate_mdx_structure.py`

**Purpose**: Validate Chapter 2 MDX structure

**Status**: Create new file

**Structure**:
- Module docstring
- Placeholder function `validate_mdx_structure(mdx_path: str) -> Dict[str, Any]`
- TODO comments for:
  - Validate H2 sections count (expected: 7)
  - Check diagram placeholders (expected: 4)
  - Check AI-block placeholders (expected: 4)
  - Check glossary terms exist (expected: 7)
- Placeholder return: empty dict
- No real validation logic (placeholder only)

**Input/Output Schemas** (Text Description):

**validate_mdx_structure(mdx_path)**:
- **Input**: `mdx_path: str` - Path to chapter-2.mdx file
- **Output**: `Dict[str, Any]` - Validation results with structure:
  ```python
  {
      "valid": bool,
      "errors": List[str],
      "warnings": List[str],
      "sections_count": int,
      "diagram_count": int,
      "ai_block_count": int,
      "glossary_count": int
  }
  ```
- **Purpose**: Validate MDX structure for Chapter 2
- **TODO**: 
  - Read MDX file
  - Parse H2 sections
  - Count diagram placeholders
  - Count AI-block placeholders
  - Count glossary terms
  - Return validation results

**Dependencies**:
- Internal: None (standalone script)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Follows same pattern as Chapter 1 validation scripts (if exist)
- Uses same validation result structure

---

### 2.2 Frontmatter Validation

**File**: `scripts/ch2/validate_frontmatter.py`

**Purpose**: Validate Chapter 2 MDX frontmatter

**Status**: Create new file

**Structure**:
- Module docstring
- Placeholder function `validate_frontmatter(mdx_path: str) -> Dict[str, Any]`
- TODO comments for:
  - Verify frontmatter fields match schema
  - Check required fields: title, description, sidebar_position, sidebar_label, tags
  - Validate field types and formats
- Placeholder return: empty dict
- No real validation logic (placeholder only)

**Input/Output Schemas** (Text Description):

**validate_frontmatter(mdx_path)**:
- **Input**: `mdx_path: str` - Path to chapter-2.mdx file
- **Output**: `Dict[str, Any]` - Validation results with structure:
  ```python
  {
      "valid": bool,
      "errors": List[str],
      "warnings": List[str],
      "fields": Dict[str, Any]
  }
  ```
- **Purpose**: Validate frontmatter structure for Chapter 2
- **TODO**: 
  - Read MDX file
  - Parse frontmatter YAML
  - Check required fields
  - Validate field types
  - Return validation results

**Dependencies**:
- Internal: None (standalone script)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Follows same pattern as Chapter 1 validation scripts (if exist)
- Uses same validation result structure

---

## 3. Backend Validation Architecture

### 3.1 Metadata Validation

**File**: `backend/app/validation/ch2_metadata_validator.py`

**Purpose**: Validate Chapter 2 metadata consistency

**Status**: Create new file

**Structure**:
- Module docstring
- Placeholder function `validate_ch2_metadata() -> Dict[str, Any]`
- TODO comments for:
  - Cross-check metadata vs mdx structure
  - Check sections names match
  - Check diagram + AI block count
  - Validate metadata imports without errors
- Placeholder return: empty dict
- No real validation logic (placeholder only)

**Input/Output Schemas** (Text Description):

**validate_ch2_metadata()**:
- **Input**: None (reads from chapter_2.py and chapter-2.mdx)
- **Output**: `Dict[str, Any]` - Validation results with structure:
  ```python
  {
      "valid": bool,
      "errors": List[str],
      "warnings": List[str],
      "metadata": Dict[str, Any],
      "mdx_structure": Dict[str, Any]
  }
  ```
- **Purpose**: Validate metadata consistency for Chapter 2
- **TODO**: 
  - Import chapter_2.py metadata
  - Read chapter-2.mdx file
  - Compare section counts
  - Compare section names
  - Compare placeholder counts
  - Return validation results

**Dependencies**:
- Internal: `app.content.chapters.chapter_2` (for metadata)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Follows same pattern as Chapter 1 metadata validator (if exists)
- Uses same validation result structure

---

## 4. Build Stability Checks

### 4.1 Build Check Orchestration

**File**: `scripts/ch2/run_all.py`

**Purpose**: Orchestrate all validation checks

**Status**: Create new file

**Structure**:
- Module docstring
- Placeholder imports
- Placeholder main function
- TODO steps for:
  - Run frontend validations
  - Run backend validations
  - Check frontend build
  - Check backend startup
  - Generate validation report
- No real execution logic (placeholder only)

**Input/Output Schemas** (Text Description):

**main()**:
- **Input**: None (command-line script)
- **Output**: Exit code (0 for success, 1 for failure)
- **Purpose**: Run all validation checks for Chapter 2
- **TODO**: 
  - Import validation scripts
  - Run validate_mdx_structure
  - Run validate_frontmatter
  - Run validate_ch2_metadata
  - Check frontend build
  - Check backend startup
  - Generate report
  - Return exit code

**Dependencies**:
- Internal: Validation scripts (validate_mdx_structure, validate_frontmatter, ch2_metadata_validator)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Follows same pattern as Chapter 1 validation orchestration (if exists)
- Uses same orchestration structure

---

### 4.2 Package.json Integration

**File**: `package.json`

**Purpose**: Add validation command

**Status**: Already exists, update

**Updates Required**:
- Add command: `"validate:ch2": "python scripts/ch2/run_all.py"`
- Ensure command is properly formatted

**Dependencies**:
- Internal: `scripts/ch2/run_all.py` (must exist)
- External: None

**Reuse of Existing Modules**:
- Follows same pattern as other npm scripts
- Uses same command structure

---

## 5. Release Folder + Export Pipeline

### 5.1 Release Folder Structure

**Directory**: `release/chapter-2/`

**Purpose**: Release package for Chapter 2

**Status**: Create new directory

**Structure**:
- `README.md` - Release package overview (placeholder)
- `CHANGELOG.md` - Version history (placeholder)
- `chapter-2-export.json` - Structured export data (placeholder JSON)
- `assets/` - Empty folder for future assets

**Files to Create**:

**README.md**:
- Placeholder content explaining release package structure
- Usage instructions (placeholder)
- File structure overview (placeholder)

**CHANGELOG.md**:
- Placeholder content for version history
- Version: chapter-2-release-v1 (placeholder)
- Features included (placeholder)
- Changes (placeholder)

**chapter-2-export.json**:
- Placeholder JSON structure:
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

**assets/**:
- Empty folder ready for future assets (diagrams, images, etc.)

---

### 5.2 Package Script

**File**: `scripts/ch2/package_release.py`

**Purpose**: Package Chapter 2 for release

**Status**: Create new file

**Structure**:
- Module docstring
- Placeholder function `package_chapter_2() -> None`
- TODO comments for:
  - Gather metadata from chapter_2.py
  - Gather MDX content from chapter-2.mdx
  - Gather diagrams (future)
  - Write chapter-2-export.json
  - Create release folder structure
- Placeholder return: None
- No real packaging logic (placeholder only)

**Input/Output Schemas** (Text Description):

**package_chapter_2()**:
- **Input**: None (reads from chapter files)
- **Output**: None (writes to release/chapter-2/)
- **Purpose**: Package Chapter 2 for release
- **TODO**: 
  - Import chapter_2.py metadata
  - Read chapter-2.mdx content
  - Gather RAG chunks (future)
  - Gather AI block info (future)
  - Gather diagrams (future)
  - Write chapter-2-export.json
  - Create release folder structure
  - Copy files to release folder

**Dependencies**:
- Internal: `app.content.chapters.chapter_2` (for metadata)
- External: None (scaffolding only)

**Reuse of Existing Modules**:
- Follows same pattern as Chapter 1 release packaging (if exists)
- Uses same packaging structure

---

## 6. Contracts + Checklist Plan

### 6.1 Validation Rules Contract

**File**: `specs/036-ch2-build-release/contracts/validation-rules.md`

**Purpose**: Document high-level validation rules

**Status**: Already exists (from spec phase)

**Content**:
- Frontend validation rules (MDX structure, frontmatter)
- Backend validation rules (metadata consistency)
- Build stability rules
- Release packaging rules
- Release folder structure

---

### 6.2 Release Checklist

**File**: `specs/036-ch2-build-release/checklists/release.md`

**Purpose**: Release readiness checklist

**Status**: Already exists (from spec phase)

**Content**:
- Build validation checklist
- Metadata validation checklist
- AI-block routing checklist
- RAG pipeline checklist
- Validation scripts checklist
- Release packaging checklist
- Package.json checklist
- Contracts and documentation checklist

---

## 7. Import Paths Ensuring Backend Boots Cleanly

### 7.1 Validation Module Imports

**File**: `backend/app/validation/ch2_metadata_validator.py`

**Import Strategy**:
- Use relative imports where possible
- Import chapter_2 metadata: `from app.content.chapters.chapter_2 import CHAPTER_METADATA`
- Handle import errors gracefully (placeholder logic)

**Dependencies**:
- Internal: `app.content.chapters.chapter_2`
- External: None (scaffolding only)

---

### 7.2 Script Imports

**Files**: `scripts/ch2/*.py`

**Import Strategy**:
- Use absolute imports from project root
- Handle missing files gracefully (placeholder logic)
- No circular dependencies

**Dependencies**:
- Internal: None (standalone scripts)
- External: None (scaffolding only)

---

## 8. Future-proofing for Chapter 3

### 8.1 Scalability Considerations

- **Chapter-Specific Scripts**: Each chapter has its own validation scripts for clear separation
- **Consistent Patterns**: All chapters follow same validation patterns for maintainability
- **Reusable Structure**: Release folder structure can be replicated for Chapter 3

### 8.2 Extension Points

- **Validation Rules**: Easy to add new validation checks per chapter
- **Release Packaging**: Easy to extend export JSON structure
- **Build Integration**: Easy to add CI/CD integration

### 8.3 Integration Points

- **Package.json**: Centralized validation commands for all chapters
- **Release Folder**: Consistent structure across chapters
- **Validation Scripts**: Consistent interface across chapters

---

## 9. Success Criteria

- ✅ All validation and release folders exist
- ✅ All scripts contain placeholder logic only
- ✅ package.json updated with validation command
- ✅ Release folder structure created
- ✅ Backend and frontend build without errors
- ✅ No real validation or packaging logic implemented
- ✅ Contract file exists and documents validation rules
- ✅ Checklist file exists with release checklist

---

## 10. Dependencies + Risks

### Dependencies:
- Feature 001: Base Project Initialization
- Feature 033: Chapter 2 Content (MDX file and metadata)
- Feature 034: Chapter 2 AI Blocks Integration (Subagents)
- Feature 035: Chapter 2 RAG Integration (RAG pipeline)
- Feature 009: Chapter 1 Validation (reference pattern)

### Risks:
1. **Risk**: Import errors if file paths are incorrect
   - **Mitigation**: Verify all paths match existing structure
2. **Risk**: Breaking existing Chapter 2 functionality
   - **Mitigation**: Ensure all changes are additive, no modifications to existing logic
3. **Risk**: Frontend build failures
   - **Mitigation**: Verify MDX syntax is correct, frontmatter structure is valid

---

## Summary

This plan establishes the complete architecture for Chapter 2 validation and release packaging scaffolding. The implementation follows Chapter 1 validation patterns exactly, creates all necessary files with placeholders, and ensures consistency across chapters. All components are scaffolding only—no business logic is implemented.

**Estimated Implementation Time**: 1-2 hours (scaffolding only, no business logic)
**Complexity**: Low (scaffolding, following existing patterns)
**Dependencies**: Feature 001, Feature 033, Feature 034, Feature 035, Feature 009
**Out of Scope**: Actual validation logic, actual packaging logic, real validation execution, real release export generation

