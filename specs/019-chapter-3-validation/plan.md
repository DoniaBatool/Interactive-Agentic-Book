# Implementation Plan: Chapter 3 Validation, Testing & Build Stability

**Branch**: `019-chapter-3-validation` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/019-chapter-3-validation/spec.md`

## Summary

This feature implements comprehensive validation for Chapter 3 quality assurance. The implementation validates MDX structure, metadata consistency, chunk markers, chunk files, RAG pipeline readiness, AI runtime routing (future), API contracts (future), and build stability. **No new features are implemented**—only validation checks, test stubs, and validation report generation.

**Primary Deliverable**: Complete validation suite for Chapter 3 (structure validation, metadata consistency, chunk marker validation, RAG readiness, runtime routing, API testing, build stability, validation report)
**Validation**: All validations pass, test stubs run, frontend builds, backend boots, validation report generated

**Note**: Feature 018-chapter-3-plan has already been completed with HTML comment format for AI-blocks, chunk markers, and Feature 018 diagram names. This validation layer validates that structure.

## Technical Context

**Language/Version**:
- Frontend: Docusaurus (MDX parsing, build validation)
- Backend: Python 3.8+ with FastAPI, pytest for testing

**Primary Dependencies**:
- FastAPI, Pydantic (already installed)
- pytest (for test stubs)
- Docusaurus build system (for frontend validation)

**Storage**:
- No persistent storage (validation results in report file only)

**Testing**:
- Manual: Validation checks, build tests, import tests
- Automated: Test stubs for API endpoints (future), import stability tests

**Target Platform**:
- Frontend: Docusaurus build system
- Backend: FastAPI server (localhost:8000)

**Project Type**: Quality Assurance / Validation

**Performance Goals**:
- Validation runs: < 30 seconds total
- Frontend build: < 2 minutes
- Backend boot: < 2 seconds

**Constraints**:
- MUST NOT implement new features (validation only)
- MUST maintain compatibility with Features 017, 018
- MUST use existing placeholder/stub responses
- MUST NOT modify existing Chapter 3 content
- MUST generate validation report
- MUST validate chunk markers (CHUNK: START / CHUNK: END)
- MUST validate HTML comment format for AI-blocks

**Scale/Scope**:
- 7 validation categories
- 5 validator modules (scaffold only, TODO logic)
- 1 test stub file (future)
- 1 validation report
- ~200-300 lines of validation code and test stubs

---

## 1. Folder Structure Plan

### 1.1 Specification Files (Already Created)

**File**: `specs/019-chapter-3-validation/spec.md`
- **Status**: Already created in spec phase
- **Purpose**: Complete validation layer specification

**File**: `specs/019-chapter-3-validation/plan.md` (this file)
- **Status**: Being created
- **Purpose**: Architecture plan for validation implementation

**File**: `specs/019-chapter-3-validation/tasks.md`
- **Status**: To be created in tasks phase
- **Purpose**: Atomic validation tasks

### 1.2 Contract Files (Already Created)

**File**: `specs/019-chapter-3-validation/contracts/validation-schema.md`
- **Status**: Already created in spec phase
- **Purpose**: Validation schema contract with all validation rules

### 1.3 Checklist Files (Already Created)

**File**: `specs/019-chapter-3-validation/checklists/requirements.md`
- **Status**: Already created in spec phase
- **Purpose**: Specification quality checklist

**File**: `specs/019-chapter-3-validation/checklists/validation-report.md`
- **Status**: Already created in spec phase (template)
- **Purpose**: Validation results report (to be populated during implementation)

### 1.4 Documentation Files (Already Created)

**File**: `specs/019-chapter-3-validation/research.md`
- **Status**: Already created in spec phase
- **Purpose**: Research document with validation methodology

**File**: `specs/019-chapter-3-validation/data-model.md`
- **Status**: Already created in spec phase
- **Purpose**: Data model with validation result entities

**File**: `specs/019-chapter-3-validation/quickstart.md`
- **Status**: Already created in spec phase
- **Purpose**: Quickstart guide for validation

### 1.5 Validator Modules (To Be Created)

**File**: `backend/app/validators/mdx_validator.py`
- **Status**: To be created in implementation phase
- **Purpose**: MDX structure validation (scaffold only, TODO logic)

**File**: `backend/app/validators/metadata_validator.py`
- **Status**: To be created in implementation phase
- **Purpose**: Metadata consistency validation (scaffold only, TODO logic)

**File**: `backend/app/validators/placeholder_validator.py`
- **Status**: To be created in implementation phase
- **Purpose**: Placeholder validation (diagrams, AI-blocks, chunk markers) (scaffold only, TODO logic)

**File**: `backend/app/validators/chunk_validator.py`
- **Status**: To be created in implementation phase
- **Purpose**: Chunk marker validation (scaffold only, TODO logic)

**File**: `backend/app/validators/runtime_checks.py`
- **Status**: To be created in implementation phase
- **Purpose**: Runtime and build validation (scaffold only, TODO logic)

### 1.6 Test Files (Future)

**File**: `tests/test_chapter_3_validation.py`
- **Status**: Future (test stubs only)
- **Purpose**: Test stubs for validation checks

---

## 2. Validation Architecture (High-Level)

### 2.1 Validation Pipeline Overview

The validation layer follows a sequential validation approach:

```
Chapter 3 Content (MDX + Backend Metadata + Chunks)
  ↓
Validation Pipeline
  ├── MDX Structure Validation
  ├── Placeholder Validation (Diagrams, AI-blocks, Chunk Markers)
  ├── Frontmatter Validation
  ├── Metadata Validation
  ├── Chunk Marker Validation
  ├── RAG Chunk Validation
  ├── Backend Import Validation
  └── Frontend Build Validation
  ↓
Validation Results
  ↓
Validation Report (validation-report.md)
```

### 2.2 Validation Layers

#### Layer 1: MDX Structure Validation
- **Purpose**: Validate MDX file structure, sections, frontmatter
- **Input**: `frontend/docs/chapters/chapter-3.mdx`
- **Checks**:
  - File exists
  - Exactly 7 H2 sections in correct order
  - Frontmatter completeness and validity
  - Reading level rules (when content is written)
- **Output**: MDX structure validation result

#### Layer 2: Placeholder Validation
- **Purpose**: Validate diagram placeholders, AI-block placeholders, naming conventions
- **Input**: `frontend/docs/chapters/chapter-3.mdx`
- **Checks**:
  - Exactly 4 diagram placeholders (Feature 018 names: perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
  - Exactly 4 AI-block HTML comment placeholders (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
  - Kebab-case naming for diagrams
  - HTML comment format for AI-blocks
- **Output**: Placeholder validation result

#### Layer 3: Frontmatter Validation
- **Purpose**: Validate MDX frontmatter fields
- **Input**: `frontend/docs/chapters/chapter-3.mdx`
- **Checks**:
  - `title`: Matches specification
  - `description`: Non-empty, 10-250 characters
  - `sidebar_position`: 3
  - `sidebar_label`: Matches specification
  - `tags`: Array of strings
  - Valid YAML format
- **Output**: Frontmatter validation result

#### Layer 4: Metadata Validation
- **Purpose**: Validate metadata file structure and consistency with MDX
- **Input**: `backend/app/content/chapters/chapter_3.py`, `frontend/docs/chapters/chapter-3.mdx`
- **Checks**:
  - File exists and imports without errors
  - All required fields present
  - Field values match specifications
  - Cross-validation (MDX ↔ metadata consistency)
- **Output**: Metadata validation result

#### Layer 5: Chunk Marker Validation
- **Purpose**: Validate chunk markers for RAG preparation
- **Input**: `frontend/docs/chapters/chapter-3.mdx`
- **Checks**:
  - Exactly 7 CHUNK: START markers
  - Exactly 7 CHUNK: END markers
  - All chunk markers properly paired
  - Chunk markers align with H2 section boundaries
  - Chunk markers placed at logical semantic boundaries
- **Output**: Chunk marker validation result

#### Layer 6: RAG Chunk Validation
- **Purpose**: Validate chunk file structure and chunk marker support
- **Input**: `backend/app/content/chapters/chapter_3_chunks.py`
- **Checks**:
  - File exists and imports without errors
  - Function `get_chapter_chunks(chapter_id: int = 3)` exists
  - Function signature is correct
  - Docstring mentions chunk marker support
- **Output**: RAG chunk validation result

#### Layer 7: Backend Import Validation
- **Purpose**: Validate backend imports and runtime compatibility
- **Input**: `backend/app/content/chapters/chapter_3.py`, `backend/app/content/chapters/chapter_3_chunks.py`
- **Checks**:
  - All imports resolve without errors
  - No circular dependencies
  - Runtime engine compatibility (future)
  - RAG integration readiness (future)
- **Output**: Backend import validation result

#### Layer 8: Frontend Build Validation
- **Purpose**: Validate frontend build and rendering
- **Input**: `frontend/docs/chapters/chapter-3.mdx`
- **Checks**:
  - `npm run build` succeeds
  - No MDX compilation errors
  - Chapter 3 page renders correctly
  - Placeholders don't break rendering
- **Output**: Frontend build validation result

---

## 3. Component-Level Plan

### 3.1 MDX Validator Module

**File**: `backend/app/validators/mdx_validator.py`

**Structure**:
```python
"""
MDX Structure Validator for Chapter 3

Validates MDX file structure, sections, frontmatter, and reading level rules.
"""

from typing import Dict, Any, List
import re

def validate_mdx_structure(mdx_file_path: str) -> Dict[str, Any]:
    """
    Validate Chapter 3 MDX file structure.
    
    Args:
        mdx_file_path: Path to chapter-3.mdx file
    
    Returns:
        Validation result dictionary with:
        {
            "valid": bool,
            "category": "mdx_structure",
            "section_count": int,
            "diagram_count": int,
            "ai_block_count": int,
            "chunk_marker_start_count": int,
            "chunk_marker_end_count": int,
            "glossary_term_count": int,
            "frontmatter_complete": bool,
            "errors": List[str],
            "warnings": List[str],
            "details": {
                "sections": List[str],
                "diagrams": List[str],
                "ai_blocks": List[str],
                "chunk_markers": List[str],
                "glossary_terms": List[str]
            }
        }
    
    TODO: Implement MDX file parsing
    TODO: Count H2 sections (should be exactly 7)
    TODO: Extract section titles and verify order
    TODO: Validate frontmatter (title, description, sidebar_position=3, sidebar_label, tags)
    TODO: Count diagram placeholders (should be 4, Feature 018 names)
    TODO: Count AI-block HTML comment placeholders (should be 4)
    TODO: Count chunk markers (should be 7 START, 7 END)
    TODO: Count glossary terms (should be 7)
    TODO: Validate reading level rules (when content is written)
    TODO: Return validation result dictionary
    """
    # Placeholder return
    return {
        "valid": False,
        "category": "mdx_structure",
        "section_count": 0,
        "diagram_count": 0,
        "ai_block_count": 0,
        "chunk_marker_start_count": 0,
        "chunk_marker_end_count": 0,
        "glossary_term_count": 0,
        "frontmatter_complete": False,
        "errors": ["TODO: Implement MDX structure validation"],
        "warnings": [],
        "details": {
            "sections": [],
            "diagrams": [],
            "ai_blocks": [],
            "chunk_markers": [],
            "glossary_terms": []
        }
    }
```

**Validation Logic** (TODO):
1. Read MDX file content
2. Parse YAML frontmatter
3. Count H2 sections (regex: `^## `)
4. Extract section titles and verify order
5. Count diagram placeholders (regex: `<!-- DIAGRAM: `)
6. Count AI-block HTML comment placeholders (regex: `<!-- AI-BLOCK: `)
7. Count chunk markers (regex: `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->`)
8. Extract glossary terms
9. Validate frontmatter fields
10. Return validation result

---

### 3.2 Metadata Validator Module

**File**: `backend/app/validators/metadata_validator.py`

**Structure**:
```python
"""
Metadata Consistency Validator for Chapter 3

Validates metadata file structure and consistency with MDX.
"""

from typing import Dict, Any, List

def validate_metadata_consistency(
    metadata_file_path: str,
    mdx_file_path: str
) -> Dict[str, Any]:
    """
    Validate Chapter 3 metadata consistency with MDX.
    
    Args:
        metadata_file_path: Path to chapter_3.py file
        mdx_file_path: Path to chapter-3.mdx file
    
    Returns:
        Validation result dictionary with:
        {
            "valid": bool,
            "category": "metadata_consistency",
            "section_count_match": bool,
            "ai_blocks_match": bool,
            "diagram_placeholders_match": bool,
            "glossary_terms_match": bool,
            "import_successful": bool,
            "errors": List[str],
            "warnings": List[str],
            "details": {
                "metadata_section_count": int,
                "mdx_section_count": int,
                "metadata_ai_blocks": List[str],
                "mdx_ai_blocks": List[str],
                "metadata_diagrams": List[str],
                "mdx_diagrams": List[str],
                "metadata_glossary": List[str],
                "mdx_glossary": List[str]
            }
        }
    
    TODO: Import chapter_3.py metadata
    TODO: Parse MDX file to extract structure
    TODO: Compare section_count (should be 7)
    TODO: Compare sections list (should match MDX exactly)
    TODO: Compare ai_blocks list (should match MDX HTML comments)
    TODO: Compare diagram_placeholders list (should match MDX, Feature 018 names)
    TODO: Compare glossary_terms list (should match MDX)
    TODO: Verify all required fields present
    TODO: Verify field types match specifications
    TODO: Return validation result dictionary
    """
    # Placeholder return
    return {
        "valid": False,
        "category": "metadata_consistency",
        "section_count_match": False,
        "ai_blocks_match": False,
        "diagram_placeholders_match": False,
        "glossary_terms_match": False,
        "import_successful": False,
        "errors": ["TODO: Implement metadata consistency validation"],
        "warnings": [],
        "details": {
            "metadata_section_count": 0,
            "mdx_section_count": 0,
            "metadata_ai_blocks": [],
            "mdx_ai_blocks": [],
            "metadata_diagrams": [],
            "mdx_diagrams": [],
            "metadata_glossary": [],
            "mdx_glossary": []
        }
    }
```

**Validation Logic** (TODO):
1. Import `CHAPTER_METADATA` from `chapter_3.py`
2. Parse MDX file to extract structure
3. Compare `section_count` with MDX section count
4. Compare `sections` list with MDX section titles
5. Compare `ai_blocks` list with MDX AI-block HTML comments
6. Compare `diagram_placeholders` list with MDX diagram placeholders (Feature 018 names)
7. Compare `glossary_terms` list with MDX glossary terms
8. Verify all required fields present
9. Return validation result

---

### 3.3 Placeholder Validator Module

**File**: `backend/app/validators/placeholder_validator.py`

**Structure**:
```python
"""
Placeholder Validator for Chapter 3

Validates diagram placeholders, AI-block placeholders, and naming conventions.
"""

from typing import Dict, Any, List

def validate_placeholders(mdx_file_path: str) -> Dict[str, Any]:
    """
    Validate Chapter 3 placeholders (diagrams, AI-blocks, naming conventions).
    
    Args:
        mdx_file_path: Path to chapter-3.mdx file
    
    Returns:
        Validation result dictionary with:
        {
            "valid": bool,
            "category": "placeholders",
            "diagram_count": int,
            "ai_block_count": int,
            "diagram_names_valid": bool,
            "ai_block_format_valid": bool,
            "naming_conventions_valid": bool,
            "errors": List[str],
            "warnings": List[str],
            "details": {
                "diagrams": List[str],
                "ai_blocks": List[str],
                "expected_diagrams": List[str],
                "expected_ai_blocks": List[str]
            }
        }
    
    TODO: Parse MDX file to extract placeholders
    TODO: Count diagram placeholders (should be 4)
    TODO: Verify diagram names match Feature 018 names:
        - perception-overview
        - sensor-types
        - cv-depth-flow
        - feature-extraction-pipeline
    TODO: Count AI-block HTML comment placeholders (should be 4)
    TODO: Verify AI-block format is HTML comments (`<!-- AI-BLOCK: type -->`)
    TODO: Verify AI-block types match allowed list:
        - ask-question
        - explain-like-i-am-10
        - interactive-quiz
        - generate-diagram
    TODO: Verify all placeholders use kebab-case naming
    TODO: Return validation result dictionary
    """
    # Placeholder return
    return {
        "valid": False,
        "category": "placeholders",
        "diagram_count": 0,
        "ai_block_count": 0,
        "diagram_names_valid": False,
        "ai_block_format_valid": False,
        "naming_conventions_valid": False,
        "errors": ["TODO: Implement placeholder validation"],
        "warnings": [],
        "details": {
            "diagrams": [],
            "ai_blocks": [],
            "expected_diagrams": [
                "perception-overview",
                "sensor-types",
                "cv-depth-flow",
                "feature-extraction-pipeline"
            ],
            "expected_ai_blocks": [
                "ask-question",
                "explain-like-i-am-10",
                "interactive-quiz",
                "generate-diagram"
            ]
        }
    }
```

**Validation Logic** (TODO):
1. Parse MDX file to extract placeholders
2. Count diagram placeholders (regex: `<!-- DIAGRAM: `)
3. Verify diagram names match Feature 018 names exactly
4. Count AI-block HTML comment placeholders (regex: `<!-- AI-BLOCK: `)
5. Verify AI-block format is HTML comments
6. Verify AI-block types match allowed list
7. Verify all placeholders use kebab-case naming
8. Return validation result

---

### 3.4 Chunk Validator Module

**File**: `backend/app/validators/chunk_validator.py`

**Structure**:
```python
"""
Chunk Marker Validator for Chapter 3

Validates chunk markers (CHUNK: START / CHUNK: END) for RAG preparation.
"""

from typing import Dict, Any, List

def validate_chunk_markers(mdx_file_path: str) -> Dict[str, Any]:
    """
    Validate Chapter 3 chunk markers.
    
    Args:
        mdx_file_path: Path to chapter-3.mdx file
    
    Returns:
        Validation result dictionary with:
        {
            "valid": bool,
            "category": "chunk_markers",
            "start_count": int,
            "end_count": int,
            "properly_paired": bool,
            "aligned_with_sections": bool,
            "errors": List[str],
            "warnings": List[str],
            "details": {
                "start_positions": List[int],
                "end_positions": List[int],
                "section_boundaries": List[int],
                "pairing_status": List[Dict[str, Any]]
            }
        }
    
    TODO: Parse MDX file to extract chunk markers
    TODO: Count CHUNK: START markers (should be 7)
    TODO: Count CHUNK: END markers (should be 7)
    TODO: Verify all chunk markers are properly paired (START with END)
    TODO: Verify chunk markers align with H2 section boundaries
    TODO: Verify chunk markers are placed at logical semantic boundaries
    TODO: Return validation result dictionary
    """
    # Placeholder return
    return {
        "valid": False,
        "category": "chunk_markers",
        "start_count": 0,
        "end_count": 0,
        "properly_paired": False,
        "aligned_with_sections": False,
        "errors": ["TODO: Implement chunk marker validation"],
        "warnings": [],
        "details": {
            "start_positions": [],
            "end_positions": [],
            "section_boundaries": [],
            "pairing_status": []
        }
    }
```

**Validation Logic** (TODO):
1. Parse MDX file to extract chunk markers
2. Count CHUNK: START markers (regex: `<!-- CHUNK: START -->`)
3. Count CHUNK: END markers (regex: `<!-- CHUNK: END -->`)
4. Verify all chunk markers are properly paired
5. Verify chunk markers align with H2 section boundaries
6. Verify chunk markers are placed at logical semantic boundaries
7. Return validation result

---

### 3.5 Runtime Checks Module

**File**: `backend/app/validators/runtime_checks.py`

**Structure**:
```python
"""
Runtime and Build Validation Checks for Chapter 3

Validates backend imports, frontend build, and runtime compatibility.
"""

from typing import Dict, Any, List
import subprocess
import sys

def validate_backend_imports() -> Dict[str, Any]:
    """
    Validate backend imports for Chapter 3.
    
    Returns:
        Validation result dictionary with:
        {
            "valid": bool,
            "category": "backend_imports",
            "chapter_3_import_successful": bool,
            "chunk_file_import_successful": bool,
            "no_circular_dependencies": bool,
            "errors": List[str],
            "warnings": List[str],
            "details": {
                "import_errors": List[str],
                "import_warnings": List[str]
            }
        }
    
    TODO: Test import of chapter_3.py
    TODO: Test import of chapter_3_chunks.py
    TODO: Check for circular dependencies
    TODO: Return validation result dictionary
    """
    # Placeholder return
    return {
        "valid": False,
        "category": "backend_imports",
        "chapter_3_import_successful": False,
        "chunk_file_import_successful": False,
        "no_circular_dependencies": False,
        "errors": ["TODO: Implement backend import validation"],
        "warnings": [],
        "details": {
            "import_errors": [],
            "import_warnings": []
        }
    }

def validate_frontend_build() -> Dict[str, Any]:
    """
    Validate frontend build for Chapter 3.
    
    Returns:
        Validation result dictionary with:
        {
            "valid": bool,
            "category": "frontend_build",
            "build_successful": bool,
            "mdx_compilation_errors": List[str],
            "errors": List[str],
            "warnings": List[str],
            "details": {
                "build_output": str,
                "build_time": float
            }
        }
    
    TODO: Run `cd frontend && npm run build`
    TODO: Check build exit code
    TODO: Parse build output for errors
    TODO: Verify Chapter 3 page is generated
    TODO: Return validation result dictionary
    """
    # Placeholder return
    return {
        "valid": False,
        "category": "frontend_build",
        "build_successful": False,
        "mdx_compilation_errors": [],
        "errors": ["TODO: Implement frontend build validation"],
        "warnings": [],
        "details": {
            "build_output": "",
            "build_time": 0.0
        }
    }
```

**Validation Logic** (TODO):
1. Test import of `chapter_3.py`
2. Test import of `chapter_3_chunks.py`
3. Check for circular dependencies
4. Run frontend build command
5. Parse build output
6. Return validation results

---

## 4. Test Strategy

### 4.1 Manual Validation Checks

**Purpose**: Manual validation checks for immediate feedback during development.

**Checks**:
1. **MDX Structure Check**:
   - Open `frontend/docs/chapters/chapter-3.mdx`
   - Count H2 sections (should be 7)
   - Verify section order matches specification
   - Verify frontmatter completeness

2. **Placeholder Check**:
   - Search for diagram placeholders (should be 4, Feature 018 names)
   - Search for AI-block HTML comment placeholders (should be 4)
   - Verify naming conventions (kebab-case)

3. **Chunk Marker Check**:
   - Search for CHUNK: START markers (should be 7)
   - Search for CHUNK: END markers (should be 7)
   - Verify all markers are properly paired

4. **Metadata Check**:
   - Import `chapter_3.py` in Python
   - Verify all required fields present
   - Compare with MDX structure

5. **Build Check**:
   - Run `cd frontend && npm run build`
   - Verify build succeeds
   - Check for errors or warnings

### 4.2 Script-Based Placeholder Checks

**Purpose**: Automated placeholder validation using scripts.

**Scripts**:
1. **PowerShell Script** (Windows):
   ```powershell
   # Count H2 sections
   Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '^## ' | Measure-Object | Select-Object -ExpandProperty Count
   
   # Count diagram placeholders
   Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- DIAGRAM:' | Measure-Object | Select-Object -ExpandProperty Count
   
   # Count AI-block placeholders
   Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- AI-BLOCK:' | Measure-Object | Select-Object -ExpandProperty Count
   
   # Count chunk markers
   Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- CHUNK: START -->' | Measure-Object | Select-Object -ExpandProperty Count
   Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- CHUNK: END -->' | Measure-Object | Select-Object -ExpandProperty Count
   ```

2. **Python Script** (Future):
   - Create `scripts/validate_chapter_3.py`
   - Run all validation checks
   - Generate validation report

### 4.3 Build + Backend Import Tests

**Purpose**: Automated build and import validation.

**Tests**:
1. **Frontend Build Test**:
   - Command: `cd frontend && npm run build`
   - Expected: Exit code 0, no errors
   - Validation: Check build output for errors

2. **Backend Import Test**:
   - Command: `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA; from app.content.chapters.chapter_3_chunks import get_chapter_chunks"`
   - Expected: Import succeeds without errors
   - Validation: Check import output

### 4.4 Logical Rules for Acceptable Failures

**Acceptable Failures**:
1. **Content Validation**: Reading level validation may fail if content is not yet written (acceptable for structure-only phase)
2. **Future Integration**: RAG pipeline and AI runtime validation may fail if features are not yet implemented (acceptable, marked as future)
3. **Test Stubs**: Test stubs may return placeholder responses (acceptable for validation phase)

**Unacceptable Failures**:
1. **Structure Validation**: MDX structure validation must pass (7 sections, 4 diagrams, 4 AI-blocks, 7 chunk marker pairs)
2. **Metadata Validation**: Metadata validation must pass (all fields present, imports succeed)
3. **Build Validation**: Frontend build must pass (no compilation errors)
4. **Chunk Marker Validation**: Chunk marker validation must pass (proper pairing, alignment)

---

## 5. Contracts Mapping

### 5.1 Requirement to File Mapping

| Requirement (from spec.md) | File to Create | Validation Rule | TODO Stub |
|----------------------------|----------------|-----------------|-----------|
| **FR1: MDX Structure Validation** | `backend/app/validators/mdx_validator.py` | Validate 7 H2 sections, frontmatter, reading level | `validate_mdx_structure()` |
| **FR2: Placeholder Validation** | `backend/app/validators/placeholder_validator.py` | Validate 4 diagrams, 4 AI-blocks, naming conventions | `validate_placeholders()` |
| **FR3: Metadata Validation** | `backend/app/validators/metadata_validator.py` | Validate metadata fields, cross-validation | `validate_metadata_consistency()` |
| **FR4: RAG Prep Validation** | `backend/app/validators/chunk_validator.py` | Validate chunk markers, chunk file | `validate_chunk_markers()` |
| **FR5: Frontend Validation** | `backend/app/validators/runtime_checks.py` | Validate frontend build | `validate_frontend_build()` |
| **FR6: Backend Validation** | `backend/app/validators/runtime_checks.py` | Validate backend imports | `validate_backend_imports()` |
| **FR7: Contracts + Checklists** | Already created in spec phase | N/A | N/A |

### 5.2 Validation Rule Details

**MDX Structure Validation**:
- Rule: Exactly 7 H2 sections in correct order
- File: `mdx_validator.py`
- Function: `validate_mdx_structure()`
- TODO: Count sections, verify order, validate frontmatter

**Placeholder Validation**:
- Rule: Exactly 4 diagrams (Feature 018 names), 4 AI-blocks (HTML comments)
- File: `placeholder_validator.py`
- Function: `validate_placeholders()`
- TODO: Count placeholders, verify names, verify format

**Metadata Validation**:
- Rule: All fields present, cross-validation passes
- File: `metadata_validator.py`
- Function: `validate_metadata_consistency()`
- TODO: Import metadata, compare with MDX, verify fields

**Chunk Marker Validation**:
- Rule: 7 pairs (START/END), properly paired, aligned with sections
- File: `chunk_validator.py`
- Function: `validate_chunk_markers()`
- TODO: Count markers, verify pairing, verify alignment

**Build Validation**:
- Rule: Frontend build succeeds, backend imports succeed
- File: `runtime_checks.py`
- Functions: `validate_frontend_build()`, `validate_backend_imports()`
- TODO: Run build command, test imports

---

## 6. Acceptance Plan

### 6.1 Success Criteria

1. ✅ All validation checks pass (MDX structure, placeholders, metadata, chunk markers, build)
2. ✅ Validation report generated with all results
3. ✅ Frontend build passes (`npm run build` succeeds)
4. ✅ Backend imports without errors
5. ✅ All validator modules created (scaffold only, TODO logic)
6. ✅ Test stubs created (future)
7. ✅ Validation report indicates pass/fail status for each category

### 6.2 How to Test MDX Correctness

**Manual Testing**:
1. Open `frontend/docs/chapters/chapter-3.mdx`
2. Count H2 sections (should be 7)
3. Verify section order matches specification
4. Verify frontmatter completeness
5. Count diagram placeholders (should be 4, Feature 018 names)
6. Count AI-block HTML comment placeholders (should be 4)
7. Count chunk markers (should be 7 START, 7 END)
8. Verify all chunk markers are properly paired

**Automated Testing** (Future):
1. Run `validate_mdx_structure()` function
2. Verify validation result indicates all checks pass
3. Check validation report for MDX structure results

### 6.3 How to Test Metadata Correctness

**Manual Testing**:
1. Import `chapter_3.py` in Python
2. Verify all required fields present
3. Compare `section_count` with MDX section count (should be 7)
4. Compare `sections` list with MDX section titles
5. Compare `ai_blocks` list with MDX AI-block HTML comments
6. Compare `diagram_placeholders` list with MDX diagram placeholders (Feature 018 names)
7. Compare `glossary_terms` list with MDX glossary terms

**Automated Testing** (Future):
1. Run `validate_metadata_consistency()` function
2. Verify validation result indicates all checks pass
3. Check validation report for metadata consistency results

### 6.4 How to Ensure Build Stability

**Frontend Build Stability**:
1. Run `cd frontend && npm run build`
2. Verify build completes with exit code 0
3. Check for MDX compilation errors
4. Verify Chapter 3 page is generated in build output
5. Verify no broken links or missing content

**Backend Build Stability**:
1. Test import of `chapter_3.py`
2. Test import of `chapter_3_chunks.py`
3. Verify no circular dependencies
4. Verify backend server boots without errors

**Validation Report**:
1. Generate validation report with all results
2. Verify report indicates pass/fail status for each category
3. Document any acceptable failures (future integrations)

---

## 7. Risks & Mitigations

### Risk 1: Section Mismatch Between MDX and Metadata

**Scenario**: MDX has different number of sections than metadata `section_count`.

**Impact**: High - breaks cross-validation, causes inconsistency

**Mitigation**:
- Validation step must catch this and report error
- Cross-validation must ensure MDX section count matches metadata `section_count` (7)
- Validation report must indicate mismatch clearly

**Detection**: Automated cross-validation check

---

### Risk 2: Wrong Placeholder Names

**Scenario**: Diagram placeholders don't use Feature 018 names or AI-block placeholders don't use HTML comment format.

**Impact**: Medium - breaks validation, causes inconsistency

**Mitigation**:
- Validation step must catch this and report error
- Placeholder validation must verify exact names match Feature 018 names
- Placeholder validation must verify AI-block format is HTML comments
- Validation report must indicate naming/format errors

**Detection**: Automated placeholder validation check

---

### Risk 3: Chunk Marker Pairing Errors

**Scenario**: Chunk markers are missing, improperly paired, or not aligned with section boundaries.

**Impact**: High - breaks RAG preparation, causes chunking issues

**Mitigation**:
- Validation step must catch this and report error
- Chunk marker validation must verify proper pairing (7 START, 7 END)
- Chunk marker validation must verify alignment with H2 section boundaries
- Validation report must indicate pairing/alignment errors

**Detection**: Automated chunk marker validation check

---

### Risk 4: Imports Failing

**Scenario**: Backend imports fail due to syntax errors, missing dependencies, or circular dependencies.

**Impact**: High - breaks backend functionality, prevents validation

**Mitigation**:
- Validation step must catch this and report error
- Backend import validation must test all imports
- Validation report must indicate import errors clearly
- Fix import errors before marking validation complete

**Detection**: Automated import validation check

---

### Risk 5: Build Failures

**Scenario**: Frontend build fails due to MDX errors, syntax issues, or missing dependencies.

**Impact**: High - breaks frontend functionality, prevents deployment

**Mitigation**:
- Validation step must catch this and report error
- Frontend build validation must run build command and check exit code
- Validation report must indicate build errors clearly
- Fix build errors before marking validation complete

**Detection**: Automated build validation check

---

### Risk 6: Metadata Field Mismatch

**Scenario**: Metadata fields don't match MDX structure (e.g., diagram names don't match).

**Impact**: Medium - breaks cross-validation, causes inconsistency

**Mitigation**:
- Validation step must catch this and report error
- Cross-validation must ensure all fields match MDX exactly
- Validation report must indicate field mismatch errors

**Detection**: Automated cross-validation check

---

### Risk 7: Chunk File Structure Issues

**Scenario**: Chunk file doesn't have correct function signature or doesn't mention chunk marker support.

**Impact**: Medium - breaks RAG preparation, causes chunking issues

**Mitigation**:
- Validation step must catch this and report error
- Chunk file validation must verify function signature
- Chunk file validation must verify docstring mentions chunk marker support
- Validation report must indicate chunk file errors

**Detection**: Automated chunk file validation check

---

## 8. Integration Points

### 8.1 Chapter 3 Content Integration

**Feature 017**: Chapter 3 Content (already completed)
- Validates MDX structure created in Feature 017
- Note: Feature 017 uses React components, Feature 018 uses HTML comments

**Feature 018**: Chapter 3 Planning Layer (already completed)
- Validates structure created in Feature 018
- Validates HTML comment format for AI-blocks
- Validates chunk markers (CHUNK: START / CHUNK: END)
- Validates Feature 018 diagram names

### 8.2 Future Integration Points

**Feature 020**: Chapter 3 AI Integration (future)
- Validates RAG pipeline integration readiness
- Validates AI runtime routing readiness
- Validates API endpoint readiness

**Feature 005**: AI Runtime Engine (future)
- Validates runtime engine can load Chapter 3 metadata
- Validates runtime engine recognizes chapter_id=3

---

## 9. Acceptance Checks

### 9.1 Structure Validation

- [ ] MDX file exists at `frontend/docs/chapters/chapter-3.mdx`
- [ ] MDX file has exactly 7 H2 sections
- [ ] MDX file has exactly 4 diagram placeholders (Feature 018 names)
- [ ] MDX file has exactly 4 AI-block HTML comment placeholders
- [ ] MDX file has exactly 7 chunk marker pairs (7 START, 7 END)
- [ ] MDX file has exactly 7 glossary terms
- [ ] All chunk markers are properly paired
- [ ] All chunk markers align with H2 section boundaries

### 9.2 Metadata Validation

- [ ] Metadata file exists at `backend/app/content/chapters/chapter_3.py`
- [ ] Metadata file imports without errors
- [ ] Metadata has `id: 3`
- [ ] Metadata has `section_count: 7`
- [ ] Metadata `sections` list has exactly 7 items matching MDX
- [ ] Metadata `ai_blocks` list has exactly 4 items
- [ ] Metadata `diagram_placeholders` list has exactly 4 items (Feature 018 names)
- [ ] Metadata has `difficulty_level: "intermediate"`
- [ ] Metadata has `prerequisites: [1, 2]`
- [ ] Metadata `glossary_terms` list has exactly 7 items

### 9.3 Chunk Marker Validation

- [ ] Exactly 7 CHUNK: START markers found
- [ ] Exactly 7 CHUNK: END markers found
- [ ] All chunk markers are properly paired
- [ ] Chunk markers align with H2 section boundaries
- [ ] Chunk markers are placed at logical semantic boundaries

### 9.4 Cross-Validation

- [ ] MDX `title` matches metadata `title` exactly
- [ ] MDX H2 section count matches metadata `section_count` (7)
- [ ] MDX H2 section titles match metadata `sections` list exactly (in order)
- [ ] MDX diagram placeholders match metadata `diagram_placeholders` list exactly
- [ ] MDX AI-block placeholders match metadata `ai_blocks` list

### 9.5 Build Validation

- [ ] Frontend build test passes (`npm run build` in `frontend/` directory)
- [ ] No build errors or warnings related to Chapter 3 MDX file
- [ ] Chapter 3 page is generated in build output
- [ ] Backend import test passes (Python import validation)

### 9.6 Validator Modules

- [ ] `backend/app/validators/mdx_validator.py` created (scaffold only, TODO logic)
- [ ] `backend/app/validators/metadata_validator.py` created (scaffold only, TODO logic)
- [ ] `backend/app/validators/placeholder_validator.py` created (scaffold only, TODO logic)
- [ ] `backend/app/validators/chunk_validator.py` created (scaffold only, TODO logic)
- [ ] `backend/app/validators/runtime_checks.py` created (scaffold only, TODO logic)

### 9.7 Validation Report

- [ ] Validation report generated at `specs/019-chapter-3-validation/checklists/validation-report.md`
- [ ] Report includes all validation results
- [ ] Report indicates pass/fail status for each validation category

---

## 10. Next Steps

After completing this plan:

1. **Task Generation**: Run `/sp.tasks` to create validation tasks
2. **Implementation**: Run `/sp.implement` to create validator modules and run validation checks
3. **Report Generation**: Generate comprehensive validation report
4. **Integration**: Validate future AI integration readiness (Feature 020)

---

Plan complete — Ready for /sp.tasks.
