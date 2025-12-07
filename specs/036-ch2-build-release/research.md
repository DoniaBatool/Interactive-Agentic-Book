# Research: Chapter 2 Build Validation + Release Packaging

**Feature**: 036-ch2-build-release
**Date**: 2025-01-27
**Purpose**: Document validation and release packaging approach for Chapter 2

## Overview

This document captures research findings for implementing validation and release packaging scaffolding for Chapter 2. Research focuses on validation patterns, build stability checks, and release packaging structure.

## Technology Decisions

### 1. Validation Script Structure

**Decision**: Create separate validation scripts for frontend (MDX) and backend (metadata) validation

**Rationale**:
- **Separation of Concerns**: Frontend validation focuses on MDX structure, backend validation focuses on metadata consistency
- **Maintainability**: Easier to maintain and extend separate scripts
- **Reusability**: Scripts can be run independently or together

**Structure**:
- Frontend: `scripts/ch2/validate_mdx_structure.py`, `scripts/ch2/validate_frontmatter.py`
- Backend: `backend/app/validation/ch2_metadata_validator.py`
- Orchestration: `scripts/ch2/run_all.py`

**Alternatives Considered**:
- **Single Script**: Too complex, harder to maintain
- **Integrated in Build**: Less flexible, harder to run independently

### 2. Release Packaging Structure

**Decision**: Create `release/chapter-2/` folder with structured files

**Rationale**:
- **Standalone Unit**: Chapter 2 can be distributed as standalone release
- **Clear Structure**: README, CHANGELOG, export JSON provide clear documentation
- **Future-Proof**: Assets folder ready for diagrams and other resources

**Structure**:
- `README.md` - Package overview
- `CHANGELOG.md` - Version history
- `chapter-2-export.json` - Structured export data
- `assets/` - Future assets (diagrams, etc.)

### 3. Build Check Integration

**Decision**: Add validation command to package.json

**Rationale**:
- **Consistency**: Follows npm script patterns
- **Accessibility**: Easy to run from project root
- **CI/CD Ready**: Can be integrated into CI/CD pipelines

**Command**: `"validate:ch2": "python scripts/ch2/run_all.py"`

---

## Validation Patterns

### Pattern 1: MDX Structure Validation

Validation checks:
1. H2 sections count (expected: 7)
2. Diagram placeholders (expected: 4)
3. AI-block placeholders (expected: 4)
4. Glossary terms (expected: 7)

### Pattern 2: Metadata Consistency Validation

Validation checks:
1. Metadata vs MDX structure cross-check
2. Section names match
3. Placeholder counts match
4. Metadata imports successfully

### Pattern 3: Build Stability Validation

Validation checks:
1. Frontend build passes
2. Backend starts without errors
3. All imports resolve
4. No runtime exceptions

---

## Release Packaging Patterns

### Pattern 1: Export JSON Structure

```json
{
  "chapter_id": 2,
  "title": "Chapter 2 — The Foundations of Mechanical Systems",
  "metadata": {},
  "content": {},
  "rag": {},
  "ai_blocks": {},
  "validation": {}
}
```

### Pattern 2: Release Documentation

- README.md: Package overview, usage instructions
- CHANGELOG.md: Version history, changes
- Export JSON: Structured data for programmatic access

---

## References

- Feature 009: Chapter 1 Validation (validation patterns)
- Feature 009.5: Chapter 1 Release Packaging (release structure)
- Feature 015: Chapter 2 Validation (comprehensive validation)
- Feature 016: Chapter 2 Release Package (comprehensive packaging)

---

## Summary

This research establishes:
- Separate validation scripts for frontend and backend
- Release folder structure for standalone distribution
- Build check integration via package.json
- Validation patterns for MDX and metadata
- Release packaging patterns for export

**Key Principles**:
- Scaffolding only—no real validation logic
- Consistency with Chapter 1 patterns
- Standalone release unit capability
- Future-proof structure for assets

