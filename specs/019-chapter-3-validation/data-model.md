# Data Model: Chapter 3 Validation, Testing & Build Stability

**Feature**: 019-chapter-3-validation
**Created**: 2025-12-05
**Type**: Quality Assurance / Validation

## Entities

### 1. Validation Result

**Description**: Result of a single validation check.

**Structure**:
```python
{
    "valid": bool,              # True if validation passes
    "category": str,            # Validation category (e.g., "mdx_structure", "chunk_markers")
    "errors": List[str],         # List of error messages
    "warnings": List[str],       # List of warning messages
    "details": Dict[str, Any]   # Additional validation details
}
```

**Attributes**:
- `valid`: Boolean indicating if validation passed
- `category`: Validation category identifier
- `errors`: List of error messages (empty if valid)
- `warnings`: List of warning messages (may be non-empty even if valid)
- `details`: Additional validation-specific details

**Validation Rules**:
- `valid` must be boolean
- `errors` must be list of strings
- `warnings` must be list of strings
- `details` must be dictionary

---

### 2. MDX Structure Validation Result

**Description**: Result of MDX structure validation.

**Structure**:
```python
{
    "valid": bool,
    "category": "mdx_structure",
    "section_count": int,           # Actual H2 section count (should be 7)
    "diagram_count": int,           # Actual diagram placeholder count (should be 4)
    "ai_block_count": int,          # Actual AI-block HTML comment count (should be 4)
    "chunk_marker_start_count": int,  # Actual CHUNK: START count (should be 7)
    "chunk_marker_end_count": int,    # Actual CHUNK: END count (should be 7)
    "glossary_term_count": int,     # Actual glossary term count (should be 7)
    "frontmatter_complete": bool,    # True if frontmatter is complete
    "errors": List[str],
    "warnings": List[str],
    "details": {
        "sections": List[str],      # List of section titles
        "diagrams": List[str],       # List of diagram placeholder names (Feature 018 names)
        "ai_blocks": List[str],     # List of AI-block HTML comment types
        "chunk_markers": List[str],  # List of chunk marker positions
        "glossary_terms": List[str]  # List of glossary term names
    }
}
```

**Validation Rules**:
- `section_count` must be 7
- `diagram_count` must be 4
- `ai_block_count` must be 4
- `chunk_marker_start_count` must be 7
- `chunk_marker_end_count` must be 7
- `glossary_term_count` must be 7
- `frontmatter_complete` must be True

---

### 3. Metadata Consistency Validation Result

**Description**: Result of metadata consistency validation.

**Structure**:
```python
{
    "valid": bool,
    "category": "metadata_consistency",
    "section_count_match": bool,        # True if section_count matches MDX
    "ai_blocks_match": bool,             # True if ai_blocks match MDX HTML comments
    "diagram_placeholders_match": bool,  # True if diagram_placeholders match MDX (Feature 018 names)
    "glossary_terms_match": bool,        # True if glossary_terms match MDX
    "import_successful": bool,           # True if metadata imports without errors
    "errors": List[str],
    "warnings": List[str],
    "details": {
        "metadata_section_count": int,
        "mdx_section_count": int,
        "metadata_ai_blocks": List[str],
        "mdx_ai_blocks": List[str],
        "metadata_diagrams": List[str],  # Feature 018 names
        "mdx_diagrams": List[str],      # Feature 018 names
        "metadata_glossary": List[str],
        "mdx_glossary": List[str]
    }
}
```

**Validation Rules**:
- `section_count_match` must be True
- `ai_blocks_match` must be True
- `diagram_placeholders_match` must be True
- `glossary_terms_match` must be True
- `import_successful` must be True

---

### 4. Chunk Marker Validation Result

**Description**: Result of chunk marker validation.

**Structure**:
```python
{
    "valid": bool,
    "category": "chunk_markers",
    "start_count": int,              # Actual CHUNK: START count (should be 7)
    "end_count": int,                # Actual CHUNK: END count (should be 7)
    "properly_paired": bool,         # True if all markers are properly paired
    "aligned_with_sections": bool,    # True if markers align with H2 section boundaries
    "errors": List[str],
    "warnings": List[str],
    "details": {
        "start_positions": List[int],  # Line numbers of CHUNK: START markers
        "end_positions": List[int],    # Line numbers of CHUNK: END markers
        "section_boundaries": List[int],  # Line numbers of H2 section boundaries
        "pairing_status": List[Dict[str, Any]]  # Pairing status for each section
    }
}
```

**Validation Rules**:
- `start_count` must be 7
- `end_count` must be 7
- `properly_paired` must be True
- `aligned_with_sections` must be True

---

### 5. Build Validation Result

**Description**: Result of frontend and backend build validation.

**Structure**:
```python
{
    "valid": bool,
    "category": "build_validation",
    "frontend_build_successful": bool,  # True if npm run build succeeds
    "backend_import_successful": bool,  # True if backend imports without errors
    "mdx_compilation_errors": List[str],  # List of MDX compilation errors
    "backend_import_errors": List[str],   # List of backend import errors
    "errors": List[str],
    "warnings": List[str],
    "details": {
        "frontend_build_output": str,     # Build output log
        "backend_import_output": str,    # Import test output
        "build_time": float,             # Build time in seconds
        "import_time": float             # Import time in seconds
    }
}
```

**Validation Rules**:
- `frontend_build_successful` must be True
- `backend_import_successful` must be True
- `mdx_compilation_errors` must be empty
- `backend_import_errors` must be empty

---

### 6. Validation Report

**Description**: Comprehensive validation report for Chapter 3.

**Structure**:
```python
{
    "chapter_id": 3,
    "validation_date": str,           # ISO 8601 timestamp
    "overall_status": str,            # "pass" | "fail" | "pending"
    "total_checks": int,
    "passed_checks": int,
    "failed_checks": int,
    "pending_checks": int,
    "results": {
        "mdx_structure": ValidationResult,
        "placeholders": ValidationResult,
        "metadata": ValidationResult,
        "chunk_markers": ValidationResult,
        "rag_prep": ValidationResult,
        "frontend_build": ValidationResult,
        "backend": ValidationResult
    },
    "errors": List[str],
    "warnings": List[str],
    "recommendations": List[str]
}
```

**Validation Rules**:
- `chapter_id` must be 3
- `overall_status` must be one of: "pass", "fail", "pending"
- `total_checks` must equal sum of passed, failed, and pending checks
- All validation results must be present

---

## Data Relationships

### Entity Relationship Diagram

```
Validation Report (1)
    ├── MDX Structure Validation Result (1)
    ├── Placeholder Validation Result (1)
    ├── Metadata Consistency Validation Result (1)
    ├── Chunk Marker Validation Result (1)
    ├── RAG Prep Validation Result (1)
    ├── Frontend Build Validation Result (1)
    └── Backend Validation Result (1)
    
MDX Structure Validation Result (1)
    ├── References MDX File (1)
    └── Contains Section/Placeholder Details (N)
    
Metadata Consistency Validation Result (1)
    ├── References MDX File (1)
    └── References Metadata File (1)
    
Chunk Marker Validation Result (1)
    └── References MDX File (1)
```

### Relationship Details

1. **Validation Report → Validation Results**: One-to-Many (1 report has 7 validation results)
2. **MDX Structure Validation → MDX File**: One-to-One (1 validation references 1 MDX file)
3. **Metadata Consistency Validation → MDX File**: One-to-One (1 validation references 1 MDX file)
4. **Metadata Consistency Validation → Metadata File**: One-to-One (1 validation references 1 metadata file)
5. **Chunk Marker Validation → MDX File**: One-to-One (1 validation references 1 MDX file)

---

## Data Flow

### Current State (Specification Phase)

1. **Specification Creation**: Create validation layer specification
2. **Contract Generation**: Generate validation schemas and contracts
3. **Validation Rules**: Define validation rules and success criteria

### Future State (Implementation Phase)

1. **Validation Execution**: Run all validation checks
2. **Result Collection**: Collect validation results
3. **Report Generation**: Generate comprehensive validation report
4. **Error Reporting**: Report all errors and warnings

### Future State (Integration Phase)

1. **CI/CD Integration**: Integrate validation into CI/CD pipeline
2. **Automated Validation**: Run validation automatically on commits
3. **Validation Dashboard**: Display validation results in dashboard

---

## Validation Summary

### Structure Validation
- ✅ MDX file structure validation defined
- ✅ Section count validation (7 sections) defined
- ✅ Placeholder validation (4 diagrams, 4 AI-blocks) defined
- ✅ Chunk marker validation (7 pairs) defined
- ✅ Glossary validation (7 terms) defined

### Metadata Validation
- ✅ Metadata file validation defined
- ✅ Field completeness validation defined
- ✅ Cross-validation (MDX ↔ metadata) defined

### Build Validation
- ✅ Frontend build validation defined
- ✅ Backend import validation defined
- ✅ Rendering validation defined

### Integration Validation (Future)
- ⏳ RAG pipeline validation (future)
- ⏳ AI runtime validation (future)
- ⏳ API endpoint validation (future)

---

## Notes

- This data model supports validation of Feature 018 structure (HTML comment format for AI-blocks, chunk markers, Feature 018 diagram names)
- Chunk marker validation is a new requirement for Chapter 3
- Validation results must be testable and measurable
- Validation report must indicate pass/fail status for each category
