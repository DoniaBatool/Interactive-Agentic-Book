# Data Model: Chapter 2 Release Packaging Layer

**Feature**: 016-chapter-2-release-package
**Created**: 2025-12-05
**Type**: Release Engineering / Packaging

## Entities

### 1. Release Package

**Description**: Complete release package for Chapter 2.

**Structure**:
```
releases/chapter-2/
├── README.md
├── content/
├── metadata/
├── rag/
├── ai-blocks/
├── contracts/
├── diagrams/
└── validation/
```

**Attributes**:
- `root_path`: `releases/chapter-2/`
- `subfolders`: List of subfolder paths
- `files`: List of all files in package
- `readme_exists`: Boolean (README.md exists)
- `complete`: Boolean (all required files present)

**Validation Rules**:
- All subfolders must exist
- README.md must exist
- All required files must be present

---

### 2. Content Package

**Description**: MDX content file in release package.

**Structure**:
```
releases/chapter-2/content/chapter-2.mdx
```

**Attributes**:
- `source_path`: `frontend/docs/chapters/chapter-2.mdx`
- `destination_path`: `releases/chapter-2/content/chapter-2.mdx`
- `sections`: 7 H2 sections
- `diagrams`: 4 diagram placeholders
- `ai_blocks`: 4 AI-block components
- `glossary_terms`: 7 glossary terms
- `frontmatter`: YAML frontmatter preserved

**Validation Rules**:
- File must exist at destination
- All sections must be included
- All placeholders must be included
- Frontmatter must be preserved

---

### 3. Metadata Package

**Description**: Chapter metadata files in release package.

**Structure**:
```
releases/chapter-2/metadata/chapter_2.py
releases/chapter-2/rag/chapter_2_chunks.py
```

**Attributes**:
- `metadata_source`: `backend/app/content/chapters/chapter_2.py`
- `metadata_destination`: `releases/chapter-2/metadata/chapter_2.py`
- `chunks_source`: `backend/app/content/chapters/chapter_2_chunks.py`
- `chunks_destination`: `releases/chapter-2/rag/chapter_2_chunks.py`
- `metadata_fields`: All required fields present
- `chunk_function`: Function signature preserved

**Validation Rules**:
- Both files must exist at destinations
- File contents must be preserved
- No modifications made

---

### 4. AI Runtime Package

**Description**: AI runtime components in release package.

**Structure**:
```
releases/chapter-2/ai-blocks/
├── ai_blocks.py
├── ch2_ask_question_agent.py
├── ch2_explain_el10_agent.py
├── ch2_quiz_agent.py
└── ch2_diagram_agent.py
```

**Attributes**:
- `ai_blocks_source`: `backend/app/api/ai_blocks.py` (excerpts)
- `ai_blocks_destination`: `releases/chapter-2/ai-blocks/ai_blocks.py`
- `subagents`: List of 4 subagent files
- `subagent_sources`: List of source paths
- `subagent_destinations`: List of destination paths

**Validation Rules**:
- All 4 subagent files must exist
- AI blocks file must exist
- File contents must be preserved
- No modifications made

---

### 5. Contracts Package

**Description**: Specification contracts in release package.

**Structure**:
```
releases/chapter-2/contracts/
├── spec.md
├── plan.md
├── tasks.md
└── content-schema.md
```

**Attributes**:
- `contract_sources`: List of source paths from `specs/014-chapter-2-content/`
- `contract_destinations`: List of destination paths
- `contract_files`: List of contract file names

**Validation Rules**:
- All contract files must exist
- File contents must be preserved
- No modifications made

---

### 6. Validation Package

**Description**: Validation reports in release package.

**Structure**:
```
releases/chapter-2/validation/
├── validation-report.md
└── validation-schema.md
```

**Attributes**:
- `report_source`: `specs/015-chapter-2-validation/checklists/validation-report.md`
- `report_destination`: `releases/chapter-2/validation/validation-report.md`
- `schema_source`: `specs/015-chapter-2-validation/contracts/validation-schema.md`
- `schema_destination`: `releases/chapter-2/validation/validation-schema.md`

**Validation Rules**:
- Both files must exist
- File contents must be preserved
- No modifications made

---

### 7. README Document

**Description**: Package documentation README.

**Structure**:
```
releases/chapter-2/README.md
```

**Attributes**:
- `sections`: List of required sections
- `chapter_purpose`: Chapter overview
- `file_structure`: Directory layout explanation
- `ai_runtime_explanation`: AI-block runtime documentation
- `rag_integration_explanation`: RAG pipeline documentation
- `build_instructions`: Frontend and backend build steps
- `testing_instructions`: Test execution steps
- `integration_instructions`: Standalone vs full book integration

**Validation Rules**:
- All required sections must be present
- Instructions must be clear and actionable
- Examples must be accurate

---

### 8. Release Consistency Check

**Description**: Validation results for release package.

**Structure**:
```python
{
    "package_exists": bool,
    "folders_exist": bool,
    "files_exist": bool,
    "readme_exists": bool,
    "content_complete": bool,
    "metadata_complete": bool,
    "ai_runtime_complete": bool,
    "contracts_complete": bool,
    "validation_complete": bool,
    "missing_files": List[str],
    "errors": List[str]
}
```

**Validation Rules**:
- All checks must pass
- No missing files
- No errors

---

## Data Relationships

```
ReleasePackage
    ├── contains → ContentPackage (1)
    ├── contains → MetadataPackage (2 files)
    ├── contains → AIRuntimePackage (5 files)
    ├── contains → ContractsPackage (4 files)
    ├── contains → ValidationPackage (2 files)
    ├── contains → READMEDocument (1)
    └── validates → ReleaseConsistencyCheck (1)
```

---

## Data Flow

### Current State (Packaging Phase)

```
1. Source Files (Features 010-015)
   ↓
2. Copy Operations
   ├── Content files
   ├── Metadata files
   ├── AI runtime files
   ├── Contracts
   └── Validation reports
   ↓
3. Release Package Structure
   ├── content/
   ├── metadata/
   ├── rag/
   ├── ai-blocks/
   ├── contracts/
   ├── diagrams/
   └── validation/
   ↓
4. README Generation
   ↓
5. Consistency Check
   ↓
6. Release Package (releases/chapter-2/)
```

### Future State (Distribution)

```
1. Release Package
   ↓
2. Distribution Options
   ├── Standalone (judges evaluation)
   └── Integrated (full book)
   ↓
3. Usage
   ├── Read README.md
   ├── Follow build instructions
   ├── Run tests
   └── Integrate as needed
```

---

## Validation Summary

- **Total Entities**: 8
- **Core Entities**: ReleasePackage, ContentPackage, MetadataPackage, AIRuntimePackage
- **Documentation Entities**: READMEDocument, ContractsPackage, ValidationPackage
- **Validation Entities**: ReleaseConsistencyCheck
- **Relationships**: ReleasePackage contains all other entities
- **Data Flow**: Source files → Copy operations → Package structure → README → Consistency check → Release package
