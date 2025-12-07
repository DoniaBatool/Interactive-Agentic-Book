# Quickstart Guide: Chapter 2 Build Validation + Release Packaging

**Feature**: 036-ch2-build-release
**Branch**: `036-ch2-build-release`
**Estimated Time**: 1-2 hours (scaffolding only, no business logic)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 001 (Base Project Initialization) completed
- [x] Feature 033 (Chapter 2 Content) completed
- [x] Feature 034 (Chapter 2 AI Blocks Integration) completed
- [x] Feature 035 (Chapter 2 RAG Integration) completed
- [x] Backend structure exists at `backend/app/`
- [x] Frontend structure exists at `frontend/docs/`
- [x] Git branch `036-ch2-build-release` checked out
- [x] Read `specs/036-ch2-build-release/spec.md`
- [x] Read `specs/036-ch2-build-release/plan.md`
- [x] Read `specs/036-ch2-build-release/contracts/validation-rules.md`

## Implementation Overview

**Total Steps**: 6 phases
**Primary Deliverable**: Complete validation and release packaging scaffolding
**Validation**: All files exist, imports resolve, backend starts without errors, frontend builds without errors

---

## Phase 1: Frontend Validation Scripts (30 minutes)

### Step 1.1: Create validate_mdx_structure.py

**Location**: `scripts/ch2/validate_mdx_structure.py`

**Action**: Create file with placeholder function:
- `def validate_mdx_structure(mdx_path: str) -> Dict[str, Any]`
- TODO comments for: H2 sections count, diagram placeholders, AI-block placeholders, glossary terms
- Placeholder return: empty dict

### Step 1.2: Create validate_frontmatter.py

**Location**: `scripts/ch2/validate_frontmatter.py`

**Action**: Create file with placeholder function:
- `def validate_frontmatter(mdx_path: str) -> Dict[str, Any]`
- TODO comments for: frontmatter fields match schema
- Placeholder return: empty dict

---

## Phase 2: Backend Validation Scripts (30 minutes)

### Step 2.1: Create ch2_metadata_validator.py

**Location**: `backend/app/validation/ch2_metadata_validator.py`

**Action**: Create file with placeholder function:
- `def validate_ch2_metadata() -> Dict[str, Any]`
- TODO comments for: cross-check metadata vs mdx, check sections match, check placeholder counts
- Placeholder return: empty dict

---

## Phase 3: Build Check Layer (15 minutes)

### Step 3.1: Create run_all.py

**Location**: `scripts/ch2/run_all.py`

**Action**: Create file with placeholder main function:
- Placeholder imports
- TODO steps for running all validations
- Placeholder execution

### Step 3.2: Update package.json

**Action**: Add command:
- `"validate:ch2": "python scripts/ch2/run_all.py"`

---

## Phase 4: Release Packaging Layer (30 minutes)

### Step 4.1: Create Release Folder Structure

**Location**: `release/chapter-2/`

**Action**: Create folder and files:
- `README.md` (placeholder content)
- `CHANGELOG.md` (placeholder content)
- `chapter-2-export.json` (placeholder JSON structure)
- `assets/` (empty folder)

### Step 4.2: Create package_release.py

**Location**: `scripts/ch2/package_release.py`

**Action**: Create file with placeholder function:
- `def package_chapter_2() -> None`
- TODO comments for: gather metadata, mdx, diagrams, write export JSON
- Placeholder return: None

---

## Phase 5: Contracts and Checklists (15 minutes)

### Step 5.1: Verify Contracts

**Action**: Verify `contracts/validation-rules.md` exists (already created)

### Step 5.2: Verify Checklists

**Action**: Verify `checklists/release.md` exists (already created)

---

## Phase 6: Validation (15 minutes)

### Step 6.1: Verify Imports

**Action**: Test that all imports resolve:
```bash
cd backend && python -c "from app.validation.ch2_metadata_validator import validate_ch2_metadata; print('OK')"
```

### Step 6.2: Verify Backend Starts

**Action**: Start backend and verify no errors:
```bash
cd backend && python -m uvicorn app.main:app --reload
```

### Step 6.3: Verify Frontend Builds

**Action**: Build frontend and verify no errors:
```bash
cd frontend && npm run build
```

---

## Success Criteria

- ✅ All validation scripts exist with placeholder functions
- ✅ Backend validation script exists and imports successfully
- ✅ Build check script exists and package.json updated
- ✅ Release folder structure created with all files
- ✅ Package script exists with placeholder function
- ✅ Backend starts without errors
- ✅ Frontend builds without errors
- ✅ All imports resolve successfully

---

## Troubleshooting

### Import Errors
- Verify all file paths are correct
- Check Python path configuration
- Ensure all parent directories have `__init__.py` files

### Backend Startup Errors
- Check for syntax errors in new files
- Verify all imports are correct
- Check for missing dependencies

### Frontend Build Errors
- Check for MDX syntax errors
- Verify frontmatter structure
- Check for missing dependencies

---

## Notes

- This is scaffolding only—no business logic
- All functions return placeholder values
- All logic is marked with TODO comments
- Follow existing patterns from Chapter 1 validation (Feature 009)

