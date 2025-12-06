# Validation Schema: Chapter 1 Validation Layer

**Feature**: 009-ch1-validation
**Created**: 2025-01-27
**Type**: Quality Assurance / Validation

## Overview

This contract defines the validation schema for Chapter 1 quality assurance. All validators follow a consistent structure with TODO placeholders for future implementation.

## Validation Module Structure

### Frontend Validators

#### MDX Structure Validator
- **File**: `frontend/validators/mdx_structure.py`
- **Function**: `validate_mdx_structure(mdx_content: str) -> Dict[str, Any]`
- **Validations** (TODO):
  - Heading hierarchy (H1/H2/H3)
  - Required sections presence
  - Glossary section with 7+ terms
  - Markdown syntax integrity
  - Link validation (internal/external)
  - Sidebar position integrity

#### AI Block Validator
- **File**: `frontend/validators/ai_blocks.py`
- **Function**: `validate_ai_blocks(mdx_content: str) -> Dict[str, Any]`
- **Validations** (TODO):
  - Presence of 4 AI blocks: ask-question, explain-el10, interactive-quiz, generate-diagram
  - Correct placement markers
  - Spacing rules around placeholders

#### Diagram Placeholder Validator
- **File**: `frontend/validators/diagrams.py`
- **Function**: `validate_diagram_placeholders(mdx_content: str) -> Dict[str, Any]`
- **Validations** (TODO):
  - Diagram placeholder naming contract
  - Placeholder syntax correctness

#### Glossary Validator
- **File**: `frontend/validators/glossary.py`
- **Function**: `validate_glossary_terms(mdx_content: str) -> Dict[str, Any]`
- **Validations** (TODO):
  - Glossary section existence
  - Minimum 7+ terms
  - Glossary format correctness

### Backend Validators

#### Chapter Metadata Validator
- **File**: `backend/validators/chapter_metadata_validator.py`
- **Function**: `validate_chapter_metadata(chapter_id: int) -> Dict[str, Any]`
- **Validations** (TODO):
  - Metadata file loads without errors
  - Sections length matches section_count
  - AI blocks array matches MDX blocks

#### RAG Readiness Validator
- **File**: `backend/validators/rag_readiness_validator.py`
- **Function**: `validate_rag_readiness(chapter_id: int) -> Dict[str, Any]`
- **Validations** (TODO):
  - Chapter chunks file exists
  - No chunk exceeds safe token limit
  - Chunk markers inside MDX

## Validation Response Schema

All validators return a consistent response structure:

```python
{
    "valid": bool,  # TODO: placeholder
    "errors": List[str],  # TODO: placeholder
    "warnings": List[str],  # TODO: placeholder
    "details": Dict[str, Any]  # TODO: placeholder
}
```

## Test Structure

### Frontend Tests
- **File**: `frontend/tests/test_mdx_ch1_structure.js`
- **Tests** (TODO):
  - MDX structure validation
  - AI block validation
  - Diagram placeholder validation
  - Glossary validation
  - Link validation

### Backend Tests
- **File**: `backend/tests/test_chapter_1_validation.py`
- **Tests** (TODO):
  - Chapter metadata validation
  - RAG readiness validation
  - Metadata import without errors

## CI Integration Schema

### Validation Script
- **File**: `scripts/validate_ch1.sh`
- **Structure** (TODO):
  - Run all frontend validators
  - Run all backend validators
  - Run build checks
  - Generate validation report

## Build Checklist Schema

### Build Stability Checks
- Docusaurus build (TODO)
- Backend startup validation (TODO)
- Import resolution checks (TODO)
- Zero warnings requirement (TODO)

## Notes

- All validation logic is TODO placeholder only
- No real parsing or checking implemented
- All functions return placeholder structures
- Ready for future implementation
