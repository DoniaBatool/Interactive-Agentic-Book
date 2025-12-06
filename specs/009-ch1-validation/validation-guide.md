# Validation Guide: Chapter 1 Validation Layer

**Feature**: 009-ch1-validation
**Created**: 2025-01-27

## Overview

This validation guide documents the validation workflow for Chapter 1 quality assurance. The validation layer provides comprehensive tools to verify MDX structure, AI blocks, diagrams, glossary, links, backend metadata, and RAG readiness.

## Frontend Validators

### MDX Structure Validator

**File**: `frontend/validators/mdx_structure.py`

**Purpose**: Validates MDX structure, headings, sections, glossary, and links.

**Function**: `validate_mdx_structure(mdx_content: str) -> Dict[str, Any]`

**Validation Checks** (all TODO placeholders):
1. Validate heading hierarchy (H1/H2/H3)
2. Ensure required sections present: Introduction, Robot Anatomy, AI+Robotics, Core Concepts, Learning Objectives, Summary, Glossary
3. Validate glossary section contains 7+ terms
4. Validate no broken Markdown syntax
5. Validate internal/external links
6. Validate sidebar_position integrity

**Usage Example** (TODO placeholder):
```python
from validators.mdx_structure import validate_mdx_structure

# TODO: Load MDX content
mdx_content = "# Chapter 1\n..."
result = validate_mdx_structure(mdx_content)
# TODO: Process validation results
```

---

### AI Block Validator

**File**: `frontend/validators/ai_blocks.py`

**Purpose**: Validates AI block presence, placement, and spacing.

**Function**: `validate_ai_blocks(mdx_content: str) -> Dict[str, Any]`

**Validation Checks** (all TODO placeholders):
1. Validate presence of 4 AI blocks: ask-question, explain-el10, interactive-quiz, generate-diagram
2. Validate chapter has 4 AI blocks + correct placement markers
3. Validate spacing rules around placeholders

**Usage Example** (TODO placeholder):
```python
from validators.ai_blocks import validate_ai_blocks

# TODO: Load MDX content
result = validate_ai_blocks(mdx_content)
# TODO: Process validation results
```

---

### Diagram Placeholder Validator

**File**: `frontend/validators/diagrams.py`

**Purpose**: Validates diagram placeholders follow naming contract and syntax.

**Function**: `validate_diagram_placeholders(mdx_content: str) -> Dict[str, Any]`

**Validation Checks** (all TODO placeholders):
1. Validate diagram placeholders follow naming contract
2. Validate placeholder syntax is correct

**Usage Example** (TODO placeholder):
```python
from validators.diagrams import validate_diagram_placeholders

# TODO: Load MDX content
result = validate_diagram_placeholders(mdx_content)
# TODO: Process validation results
```

---

### Glossary Validator

**File**: `frontend/validators/glossary.py`

**Purpose**: Validates glossary section and terms.

**Function**: `validate_glossary_terms(mdx_content: str) -> Dict[str, Any]`

**Validation Checks** (all TODO placeholders):
1. Validate glossary section exists
2. Validate minimum 7+ terms present
3. Validate glossary format is correct

**Usage Example** (TODO placeholder):
```python
from validators.glossary import validate_glossary_terms

# TODO: Load MDX content
result = validate_glossary_terms(mdx_content)
# TODO: Process validation results
```

---

## Backend Validators

### Chapter Metadata Validator

**File**: `backend/validators/chapter_metadata_validator.py`

**Purpose**: Validates chapter metadata loads and matches MDX content.

**Function**: `validate_chapter_metadata(chapter_id: int) -> Dict[str, Any]`

**Validation Checks** (all TODO placeholders):
1. Validate chapter_1.py metadata loads without errors
2. Validate sections length matches section_count
3. Validate ai_blocks array matches MDX blocks

**Usage Example** (TODO placeholder):
```python
from app.validators.chapter_metadata_validator import validate_chapter_metadata

result = validate_chapter_metadata(chapter_id=1)
# TODO: Process validation results
```

---

### RAG Readiness Validator

**File**: `backend/validators/rag_readiness_validator.py`

**Purpose**: Validates RAG chunk readiness for Chapter 1.

**Function**: `validate_rag_readiness(chapter_id: int) -> Dict[str, Any]`

**Validation Checks** (all TODO placeholders):
1. Validate chapter chunks file exists
2. Validate no chunk exceeds safe token limit
3. Validate chunk markers inside MDX

**Usage Example** (TODO placeholder):
```python
from app.validators.rag_readiness_validator import validate_rag_readiness

result = validate_rag_readiness(chapter_id=1)
# TODO: Process validation results
```

---

## Validation Response Structure

All validators return a consistent response structure:

```python
{
    "valid": bool,                    # Validation result
    "errors": List[str],              # List of error messages
    "warnings": List[str],            # List of warning messages
    "details": Dict[str, Any]         # Additional validation details
}
```

## Integration

### CI/CD Integration (Placeholder)

The validation layer includes a CI validation script placeholder at `scripts/validate_ch1.sh` for future CI/CD integration.

**TODO**: Implement full validation pipeline in CI script:
- Run all frontend validators
- Run all backend validators
- Run tests
- Generate validation report

### Build Integration (Placeholder)

**TODO**: Integrate validators into build process:
- Run validators before build
- Fail build on validation errors
- Generate validation reports

---

## Notes

- All validation logic is TODO placeholder only
- No real parsing or checking implemented
- All functions return placeholder structures
- Ready for future implementation
