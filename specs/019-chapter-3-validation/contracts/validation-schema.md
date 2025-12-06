# Validation Schema: Chapter 3 — Validation, Testing & Build Stability Layer

**Feature**: 019-chapter-3-validation
**Date**: 2025-12-05
**Purpose**: Define validation rules and schemas for Chapter 3 structure, metadata, placeholders, chunk markers, and build stability

## MDX Structure Validation Schema

**File**: `frontend/docs/chapters/chapter-3.mdx`

### Frontmatter Validation Rules

**Required Fields**:
```yaml
title: string              # Must match: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
description: string        # 10-250 characters, non-empty
sidebar_position: integer  # Must be 3
sidebar_label: string      # Must match: "Chapter 3: Physical AI Perception Systems"
tags: string[]            # Must include: ["physical-ai", "sensors", "perception", "signal-processing"]
```

**Validation Rules**:
- Title MUST start with "Chapter 3 — " format
- Description MUST be 10-250 characters
- sidebar_position MUST be 3 (matches chapter number)
- All fields MUST be valid YAML (no unescaped special characters)
- Frontmatter MUST be enclosed by `---` delimiters at start and end

---

### Section Structure Validation Rules

**Required Sections** (exactly 7 H2 sections in order):
1. `## What Is Perception in Physical AI? {#what-is-perception-in-physical-ai}`
2. `## Types of Sensors in Robotics {#types-of-sensors-in-robotics}`
3. `## Computer Vision & Depth Perception {#computer-vision-depth-perception}`
4. `## Signal Processing Basics for AI {#signal-processing-basics-for-ai}`
5. `## Feature Extraction & Interpretation {#feature-extraction-interpretation}`
6. `## Learning Objectives {#learning-objectives}`
7. `## Glossary {#glossary}`

**Validation Rules**:
- MUST have exactly 7 H2 sections
- Section titles MUST match metadata `sections` list exactly (in order)
- Section IDs (anchor links) MUST be kebab-case
- Section order MUST match specification exactly
- All sections MUST have chunk markers (CHUNK: START / CHUNK: END)

---

### Reading Level Validation Rules

**Rules** (for future content validation):
- **Sentence length**: 15-20 words per sentence
- **Paragraph length**: 3-4 sentences per paragraph
- **Reading level**: Grade 7-8
- **Vocabulary**: Define all technical terms clearly on first use

**Validation Rules**:
- Reading level rules apply when actual content is written
- Structure validation always applies (sections, placeholders, chunk markers)

---

## Placeholder Validation Schema

### Diagram Placeholder Validation Rules

**Required Placeholders** (exactly 4):
1. `<!-- DIAGRAM: perception-overview -->`
2. `<!-- DIAGRAM: sensor-types -->`
3. `<!-- DIAGRAM: cv-depth-flow -->`
4. `<!-- DIAGRAM: feature-extraction-pipeline -->`

**Validation Rules**:
- MUST have exactly 4 diagram placeholders
- All placeholders MUST use kebab-case naming
- All placeholders MUST match metadata `diagram_placeholders` list exactly
- All placeholders MUST be placed within appropriate sections
- Format MUST be `<!-- DIAGRAM: {name} -->` (with spaces)

**Placement**:
- Section 1: perception-overview
- Section 2: sensor-types
- Section 3: cv-depth-flow
- Section 4: feature-extraction-pipeline

---

### AI-Block Placeholder Validation Rules

**Required Placeholders** (exactly 4 HTML comments):
1. `<!-- AI-BLOCK: ask-question -->`
2. `<!-- AI-BLOCK: explain-like-i-am-10 -->`
3. `<!-- AI-BLOCK: interactive-quiz -->`
4. `<!-- AI-BLOCK: generate-diagram -->`

**Validation Rules**:
- MUST have exactly 4 AI-block placeholders
- All placeholders MUST use HTML comment format
- All placeholders MUST match metadata `ai_blocks` list exactly
- Format MUST be `<!-- AI-BLOCK: {type} -->` (with spaces, uppercase AI-BLOCK)
- All placeholders MUST be placed within appropriate sections

**Placement**:
- Section 1: ask-question
- Section 2: generate-diagram
- Section 3: explain-like-i-am-10
- Section 4: interactive-quiz

**Allowed Types**:
- ask-question
- explain-like-i-am-10
- interactive-quiz
- generate-diagram

---

## Chunk Marker Validation Schema

### Chunk Marker Format

**Format**: HTML comment format
```html
<!-- CHUNK: START -->
[Section content]
<!-- CHUNK: END -->
```

**Validation Rules**:
- MUST have exactly 7 chunk marker pairs (7 START, 7 END)
- Chunk markers MUST be properly paired (START with END)
- Chunk markers MUST align with H2 section boundaries
- Chunk markers MUST be placed at logical semantic boundaries
- Format MUST be `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` (with spaces, uppercase CHUNK)

**Placement**:
- Each H2 section MUST have one chunk marker pair
- CHUNK: START at beginning of section content
- CHUNK: END at end of section content

**Chunk Count Validation**:
- Chunk count MUST meet RAG guidelines (3-15 logical chunks)
- Each chunk MUST contain meaningful text (when content is written)
- Chunk boundaries MUST respect semantic meaning

---

## Metadata Validation Schema

**File**: `backend/app/content/chapters/chapter_3.py`

### Required Fields

```python
CHAPTER_METADATA = {
    # Core identification
    "id": 3,                    # MUST be 3
    "title": str,               # MUST match MDX frontmatter exactly
    "summary": str,             # MUST be non-empty (placeholder acceptable)

    # Structure information
    "section_count": 7,         # MUST be 7
    "sections": List[str],      # MUST be list of exactly 7 strings matching MDX H2 sections

    # Placeholder tracking
    "ai_blocks": List[str],    # MUST be list of exactly 4 strings
    "diagram_placeholders": List[str],  # MUST be list of exactly 4 strings (Feature 018 names)

    # Versioning
    "last_updated": str,       # MUST be ISO 8601 timestamp format

    # RAG-specific metadata
    "difficulty_level": str,   # MUST be "intermediate"
    "prerequisites": List[int],  # MUST be [1, 2]
    "learning_outcomes": List[str],  # MUST be list of 3-10 items (placeholder acceptable)
    "glossary_terms": List[str],  # MUST be list of exactly 7 items (placeholder acceptable)
}
```

### Field Validation Rules

**Core Identification**:
- `id`: MUST be 3 (integer)
- `title`: MUST match MDX frontmatter `title` exactly
- `summary`: MUST be non-empty (placeholder acceptable for now)

**Structure Information**:
- `section_count`: MUST be 7 (integer)
- `sections`: MUST be list of exactly 7 strings matching MDX H2 section titles in order

**Placeholder Tracking**:
- `ai_blocks`: MUST be list of exactly 4 strings:
  - "ask-question"
  - "explain-like-i-am-10"
  - "interactive-quiz"
  - "generate-diagram"
- `diagram_placeholders`: MUST be list of exactly 4 strings (Feature 018 names):
  - "perception-overview"
  - "sensor-types"
  - "cv-depth-flow"
  - "feature-extraction-pipeline"

**Versioning**:
- `last_updated`: MUST be ISO 8601 timestamp string (e.g., "2025-12-05T00:00:00Z")

**RAG-Specific Metadata**:
- `difficulty_level`: MUST be "intermediate" (string)
- `prerequisites`: MUST be [1, 2] (list of integers)
- `learning_outcomes`: MUST be list of 3-10 strings (placeholder acceptable)
- `glossary_terms`: MUST be list of exactly 7 strings (placeholder acceptable)

### Cross-Validation Rules (MDX ↔ Metadata)

1. MDX `title` MUST match metadata `title` exactly
2. MDX H2 section count MUST match metadata `section_count` (7)
3. MDX H2 section titles MUST match metadata `sections` list exactly (in order)
4. MDX diagram placeholders MUST match metadata `diagram_placeholders` list exactly
5. MDX AI-block placeholders MUST match metadata `ai_blocks` list

---

## RAG Prep Validation Schema

**File**: `backend/app/content/chapters/chapter_3_chunks.py`

### Chunk File Validation Rules

**Function Signature**:
```python
def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
```

**Validation Rules**:
- Function MUST exist with correct signature
- Function MUST return `List[Dict[str, Any]]`
- Function MUST have `chapter_id: int = 3` parameter
- Function MUST be importable without errors
- Function docstring MUST mention chunk marker support

### Chunk Marker Support Validation

**Validation Rules**:
- Chunk file docstring MUST mention chunk marker support
- TODO comments MUST include chunk marker strategy
- Chunk metadata structure MUST include `chunk_markers: bool` flag

### Future Embedding Pipeline Compatibility

**Validation Rules**:
- Chunk markers MUST exist for future embedding pipeline integration
- Chunk file structure MUST support future embedding generation
- Chunk metadata MUST support future Qdrant storage

---

## Frontend Build Validation Schema

### Build Command

**Command**: `cd frontend && npm run build`

**Validation Rules**:
- Build MUST complete with exit code 0
- No MDX errors or warnings
- Chapter 3 page MUST be generated in build output
- No broken links or missing content

### Rendering Validation

**Validation Rules**:
- AI-block HTML comment placeholders MUST NOT break rendering
- Diagram placeholders MUST NOT break rendering
- Chunk markers MUST NOT break rendering
- All sections MUST render correctly

### Page Validation

**Validation Rules**:
- Chapter 3 page MUST be accessible at `/docs/chapters/chapter-3`
- All sections MUST be visible and navigable
- No broken links or missing content

---

## Backend Validation Schema

### Import Validation

**Files to Validate**:
1. `backend/app/content/chapters/chapter_3.py`
2. `backend/app/content/chapters/chapter_3_chunks.py`

**Validation Rules**:
- Both files MUST import without errors
- No missing imports or circular dependencies
- All imports MUST resolve correctly

### Runtime Engine Compatibility (Future)

**Validation Rules** (for future integration):
- Runtime engine (Feature 005) MUST be able to load Chapter 3 metadata
- Runtime engine MUST recognize chapter_id=3
- All four AI block types MUST be routable

### RAG Integration Readiness (Future)

**Validation Rules** (for future integration):
- Placeholders for RAG + LLM MUST be present
- Chunk file structure MUST support future RAG integration
- Metadata structure MUST support future embedding pipeline

---

## Validation Table

| Validation Category | Check | Expected Result | Status |
|---------------------|-------|-----------------|--------|
| **MDX Structure** | File exists | `frontend/docs/chapters/chapter-3.mdx` exists | ⏳ |
| | H2 section count | Exactly 7 sections | ⏳ |
| | Section order | Matches specification exactly | ⏳ |
| | Frontmatter | All required fields present | ⏳ |
| **Placeholders** | Diagram count | Exactly 4 placeholders | ⏳ |
| | Diagram names | Feature 018 names (kebab-case) | ⏳ |
| | AI-block count | Exactly 4 HTML comments | ⏳ |
| | AI-block format | HTML comment format | ⏳ |
| **Chunk Markers** | START count | Exactly 7 markers | ⏳ |
| | END count | Exactly 7 markers | ⏳ |
| | Pairing | All properly paired | ⏳ |
| | Alignment | Aligned with section boundaries | ⏳ |
| **Metadata** | File exists | `backend/app/content/chapters/chapter_3.py` exists | ⏳ |
| | Import | Imports without errors | ⏳ |
| | Field completeness | All required fields present | ⏳ |
| | Cross-validation | MDX ↔ metadata consistency | ⏳ |
| **RAG Prep** | Chunk file exists | `backend/app/content/chapters/chapter_3_chunks.py` exists | ⏳ |
| | Chunk function | Function exists with correct signature | ⏳ |
| | Chunk marker support | Docstring mentions chunk markers | ⏳ |
| **Frontend Build** | Build command | `npm run build` succeeds | ⏳ |
| | MDX compilation | No errors or warnings | ⏳ |
| | Page rendering | Chapter 3 page renders correctly | ⏳ |
| **Backend** | Import validation | All imports resolve | ⏳ |
| | Runtime compatibility | Runtime engine can load metadata (future) | ⏳ |
| | RAG readiness | Placeholders for RAG exist (future) | ⏳ |

**Status Legend**:
- ⏳ = Pending validation (to be checked during implementation)
- ✅ = Pass
- ❌ = Fail

---

## Validation Checklist

- [ ] MDX file exists at `frontend/docs/chapters/chapter-3.mdx`
- [ ] Exactly 7 H2 sections exist in correct order
- [ ] Frontmatter complete and valid
- [ ] Exactly 4 diagram placeholders (Feature 018 names)
- [ ] Exactly 4 AI-block HTML comment placeholders
- [ ] Exactly 7 chunk marker pairs (7 START, 7 END)
- [ ] All chunk markers properly paired
- [ ] Metadata file exists and imports without errors
- [ ] All metadata fields present and valid
- [ ] Cross-validation passes (MDX ↔ metadata)
- [ ] Chunk file exists and imports without errors
- [ ] Chunk function has correct signature
- [ ] Frontend build passes (`npm run build`)
- [ ] Backend imports without errors
- [ ] Validation report generated

---

## Notes

- This validation schema validates the structure created in Feature 018
- Feature 018 uses HTML comment format for AI-blocks (not React components)
- Feature 018 uses different diagram names (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
- Feature 018 requires chunk markers (CHUNK: START / CHUNK: END) for RAG preparation
- All validation rules must be testable and measurable
- Validation report must indicate pass/fail status for each category
