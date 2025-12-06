# Data Model: Chapter 1 Validation, Testing & Build Stability Layer

**Generated**: 2025-01-27
**Feature**: 009-ch1-validation

## Function Signatures

### Frontend Validators

#### MDX Structure Validator

```python
def validate_mdx_structure(mdx_content: str) -> Dict[str, Any]:
    """
    Validate MDX structure, headings, sections, and links.
    
    Expected Input:
        mdx_content: str                       # MDX file content
    
    Expected Output:
        {
            "valid": bool,                      # TODO: placeholder
            "errors": List[str],               # TODO: placeholder
            "warnings": List[str],              # TODO: placeholder
            "details": {
                "heading_hierarchy": Dict,     # TODO: placeholder
                "sections": Dict,               # TODO: placeholder
                "glossary_terms": int,          # TODO: placeholder
                "links": Dict                   # TODO: placeholder
            }
        }
    
    Validation Checks (all TODO):
    1. Validate heading hierarchy (H1/H2/H3)
    2. Ensure required sections present
    3. Validate glossary section contains 7+ terms
    4. Validate no broken Markdown syntax
    5. Validate internal/external links
    6. Validate sidebar_position integrity
    """
    # TODO: Implement validation
    return {}
```

#### AI Block Validator

```python
def validate_ai_blocks(mdx_content: str) -> Dict[str, Any]:
    """
    Validate AI blocks presence and placement.
    
    Expected Input:
        mdx_content: str                       # MDX file content
    
    Expected Output:
        {
            "valid": bool,                      # TODO: placeholder
            "errors": List[str],               # TODO: placeholder
            "warnings": List[str],              # TODO: placeholder
            "details": {
                "blocks_found": List[str],      # TODO: placeholder
                "blocks_required": List[str],   # ["ask-question", "explain-el10", "interactive-quiz", "generate-diagram"]
                "placement_markers": Dict,      # TODO: placeholder
                "spacing_issues": List[str]     # TODO: placeholder
            }
        }
    
    Validation Checks (all TODO):
    1. Validate presence of 4 AI blocks
    2. Validate correct placement markers
    3. Validate spacing rules around placeholders
    """
    # TODO: Implement validation
    return {}
```

#### Diagram Placeholder Validator

```python
def validate_diagram_placeholders(mdx_content: str) -> Dict[str, Any]:
    """
    Validate diagram placeholders follow naming contract.
    
    Expected Input:
        mdx_content: str                       # MDX file content
    
    Expected Output:
        {
            "valid": bool,                      # TODO: placeholder
            "errors": List[str],               # TODO: placeholder
            "warnings": List[str],              # TODO: placeholder
            "details": {
                "placeholders_found": List[str], # TODO: placeholder
                "naming_contract": Dict,        # TODO: placeholder
                "syntax_errors": List[str]      # TODO: placeholder
            }
        }
    
    Validation Checks (all TODO):
    1. Validate diagram placeholders follow naming contract
    2. Validate placeholder syntax is correct
    """
    # TODO: Implement validation
    return {}
```

#### Glossary Validator

```python
def validate_glossary_terms(mdx_content: str) -> Dict[str, Any]:
    """
    Validate glossary section and terms.
    
    Expected Input:
        mdx_content: str                       # MDX file content
    
    Expected Output:
        {
            "valid": bool,                      # TODO: placeholder
            "errors": List[str],               # TODO: placeholder
            "warnings": List[str],              # TODO: placeholder
            "details": {
                "glossary_exists": bool,        # TODO: placeholder
                "term_count": int,              # TODO: placeholder (minimum 7)
                "terms": List[str],            # TODO: placeholder
                "format_errors": List[str]      # TODO: placeholder
            }
        }
    
    Validation Checks (all TODO):
    1. Validate glossary section exists
    2. Validate minimum 7+ terms present
    3. Validate glossary format is correct
    """
    # TODO: Implement validation
    return {}
```

### Backend Validators

#### Chapter Metadata Validator

```python
def validate_chapter_metadata(chapter_id: int) -> Dict[str, Any]:
    """
    Validate chapter metadata loads and matches MDX content.
    
    Expected Input:
        chapter_id: int                        # Chapter identifier (1 for Chapter 1)
    
    Expected Output:
        {
            "valid": bool,                      # TODO: placeholder
            "errors": List[str],               # TODO: placeholder
            "warnings": List[str],              # TODO: placeholder
            "details": {
                "metadata_loaded": bool,        # TODO: placeholder
                "sections_match": bool,         # TODO: placeholder
                "ai_blocks_match": bool,        # TODO: placeholder
                "section_count": int,          # TODO: placeholder
                "sections_length": int         # TODO: placeholder
            }
        }
    
    Validation Checks (all TODO):
    1. Validate chapter_1.py metadata loads without errors
    2. Validate sections length matches section_count
    3. Validate ai_blocks array matches MDX blocks
    """
    # TODO: Implement validation
    return {}
```

#### RAG Readiness Validator

```python
def validate_rag_readiness(chapter_id: int) -> Dict[str, Any]:
    """
    Validate RAG chunk readiness for Chapter 1.
    
    Expected Input:
        chapter_id: int                        # Chapter identifier (1 for Chapter 1)
    
    Expected Output:
        {
            "valid": bool,                      # TODO: placeholder
            "errors": List[str],               # TODO: placeholder
            "warnings": List[str],              # TODO: placeholder
            "details": {
                "chunks_file_exists": bool,     # TODO: placeholder
                "chunk_count": int,            # TODO: placeholder
                "chunks_over_limit": List[int], # TODO: placeholder
                "chunk_markers_found": bool,    # TODO: placeholder
                "token_limit": int              # TODO: placeholder (safe limit)
            }
        }
    
    Validation Checks (all TODO):
    1. Validate chapter chunks file exists
    2. Validate no chunk exceeds safe token limit
    3. Validate chunk markers inside MDX
    """
    # TODO: Implement validation
    return {}
```

## Test Function Signatures

### Frontend Tests

```javascript
// test_mdx_ch1_structure.js
describe('MDX Structure Validation', () => {
    test('should validate heading hierarchy', () => {
        // TODO: Implement test
    });
    
    test('should validate AI blocks', () => {
        // TODO: Implement test
    });
    
    test('should validate diagram placeholders', () => {
        // TODO: Implement test
    });
    
    test('should validate glossary terms', () => {
        // TODO: Implement test
    });
    
    test('should validate links', () => {
        // TODO: Implement test
    });
});
```

### Backend Tests

```python
# test_chapter_1_validation.py
def test_chapter_metadata_validation():
    """Test chapter metadata validation."""
    # TODO: Implement test
    pass

def test_rag_readiness_validation():
    """Test RAG readiness validation."""
    # TODO: Implement test
    pass

def test_metadata_import():
    """Test metadata import without errors."""
    # TODO: Implement test
    pass
```

## Validation Response Schema

All validators return a consistent response structure:

```python
{
    "valid": bool,                    # Validation result
    "errors": List[str],              # List of error messages
    "warnings": List[str],            # List of warning messages
    "details": Dict[str, Any]         # Additional validation details
}
```

## Data Flow Contracts

### Validation Flow

1. **Input**: MDX content or chapter_id
2. **Validator**: Runs validation checks (TODO placeholders)
3. **Response**: Returns validation result with errors, warnings, details
4. **Test**: Test scaffolding validates structure (TODO placeholders)

### CI Integration Flow

1. **Script**: `scripts/validate_ch1.sh` runs all validators
2. **Validators**: Execute validation checks (TODO placeholders)
3. **Report**: Generate validation report (TODO placeholder)
4. **CI**: Integrate into CI pipeline (TODO placeholder)

## Notes

- All validation logic is TODO placeholder only
- No real parsing or checking implemented
- All functions return placeholder structures
- Ready for future implementation
