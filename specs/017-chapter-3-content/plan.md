# Implementation Plan: Chapter 3 Written Content — Structure, Metadata, Schema & Contracts

**Branch**: `017-chapter-3-content` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/017-chapter-3-content/spec.md`

## Summary

This feature establishes the complete Chapter 3 content framework: MDX structure with placeholders, metadata schema, glossary items, AI-block markers, diagram placeholders, and backend metadata file. **NO real text content is written**—only structure and placeholders. The implementation creates an MDX skeleton with exactly 7 H2 sections, 4 diagram placeholders, 4 AI-block React components, and a glossary section with 7 placeholder terms. A backend metadata file provides structured information for future RAG integration, and comprehensive contracts document validation rules and content writing guidelines.

**Primary Deliverable**: `frontend/docs/chapters/chapter-3.mdx` (MDX skeleton with structure only)
**Secondary Deliverable**: `backend/app/content/chapters/chapter_3.py` (Python metadata dictionary)
**Tertiary Deliverable**: Contract files (content-schema.md, checklists, research.md, quickstart.md, data-model.md)
**Validation**: Manual structure review + Docusaurus build test + Python import test

## Technical Context

**Language/Version**:
- Frontend: MDX (Markdown + JSX) compatible with Docusaurus 3.x
- Backend: Python 3.11+

**Primary Dependencies**:
- Frontend: Docusaurus 3.x (already installed)
- Backend: Python 3.11+ standard library (no new dependencies)
- Feature 003 (Chapter 1 Content): Template pattern reference
- Feature 014 (Chapter 2 Content): Template pattern reference
- Feature 011 (Chapter 2 AI Blocks): React components available

**Storage**: Static files (MDX content, Python module) - no database

**Testing**:
- Frontend: `npm run build` validation (Docusaurus build process)
- Backend: Python import test (`python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"`)
- Manual: Structure validation (section count, placeholder count, naming conventions)

**Target Platform**:
- Frontend: Web browsers (Chrome, Firefox, Safari) via Docusaurus static site
- Backend: Server-side Python (Uvicorn/FastAPI environment)

**Project Type**: Web application (frontend MDX structure + backend metadata scaffold)

**Performance Goals**:
- Page load time: < 2 seconds for Chapter 3 page (structure only, no content)
- Build time: Incremental build < 5 seconds
- No performance-critical operations (static structure only)

**Constraints**:
- MUST NOT write actual content text (only placeholders)
- MUST have exactly 7 H2 sections
- MUST follow Chapter 1 and Chapter 2 structure pattern
- MUST use kebab-case for diagram placeholders
- MUST use valid AI-block component types (from Feature 011)
- Backend metadata MUST remain simple Python dictionary (no Pydantic model, no database)
- Chapter 3 is intermediate difficulty (requires Chapters 1 and 2 as prerequisites)

**Scale/Scope**:
- 1 chapter (Chapter 3 only)
- 7 H2 sections (structure only, no content)
- 7 glossary term placeholders
- 4 diagram placeholders (kebab-case)
- 4 AI-block React components (chapterId={3})
- 1 backend metadata file
- 5 contract files

---

## 1. File Structure to be Created

### 1.1 Frontend Files

**File**: `frontend/docs/chapters/chapter-3.mdx`
- **Purpose**: MDX content file with structure and placeholders only
- **Content**: YAML frontmatter, 7 H2 sections, 4 diagram placeholders, 4 AI-block components, glossary section
- **Status**: New file (does not exist yet)
- **Validation**: Docusaurus build test, structure validation

### 1.2 Backend Files

**File**: `backend/app/content/chapters/chapter_3.py`
- **Purpose**: Python metadata dictionary for Chapter 3
- **Content**: `CHAPTER_METADATA` dictionary with all required fields
- **Status**: New file (does not exist yet)
- **Validation**: Python import test, field validation

**File**: `backend/app/content/chapters/chapter_3_chunks.py`
- **Purpose**: RAG chunk file with placeholder function
- **Content**: `get_chapter_chunks(chapter_id: int = 3)` function
- **Status**: New file (does not exist yet)
- **Validation**: Python import test, function signature validation

### 1.3 Contract Files (Already Created in Spec Phase)

**File**: `specs/017-chapter-3-content/contracts/content-schema.md`
- **Purpose**: Content schema contract with validation rules
- **Status**: Already created in spec phase
- **Validation**: Manual review

**File**: `specs/017-chapter-3-content/checklists/requirements.md`
- **Purpose**: Specification quality checklist
- **Status**: Already created in spec phase
- **Validation**: Manual review

**File**: `specs/017-chapter-3-content/research.md`
- **Purpose**: Research document with writing guidelines
- **Status**: Already created in spec phase
- **Validation**: Manual review

**File**: `specs/017-chapter-3-content/data-model.md`
- **Purpose**: Data model with entity definitions
- **Status**: Already created in spec phase
- **Validation**: Manual review

**File**: `specs/017-chapter-3-content/quickstart.md`
- **Purpose**: Quickstart guide for implementation
- **Status**: Already created in spec phase
- **Validation**: Manual review

---

## 2. MDX Composition Plan

### 2.1 Section Headings (Exactly 7 H2 Sections)

**Decision**: Use exactly 7 H2 sections matching spec requirements

**Section Structure**:
```markdown
## Section 1: What Is Perception in Physical AI? {#what-is-perception-in-physical-ai}
## Section 2: Types of Sensors in Robotics {#types-of-sensors-in-robotics}
## Section 3: Computer Vision & Depth Perception {#computer-vision-depth-perception}
## Section 4: Signal Processing Basics for AI {#signal-processing-basics-for-ai}
## Section 5: Feature Extraction & Interpretation {#feature-extraction-interpretation}
## Section 6: Learning Objectives {#learning-objectives}
## Section 7: Glossary {#glossary}
```

**Rationale**:
- **7 sections**: Matches spec requirement (FR1)
- **Anchor IDs**: Kebab-case section IDs for linking and AI-block integration
- **Consistent naming**: Matches Chapter 1 and Chapter 2 pattern (H2 headings with descriptive titles)
- **Section 6 (Learning Objectives)**: Included as separate section per spec (unlike Chapter 2 which merged it)

**Section Order**:
1. **What Is Perception in Physical AI?** - Introduction to perception concept
2. **Types of Sensors in Robotics** - Sensor categorization
3. **Computer Vision & Depth Perception** - Vision systems
4. **Signal Processing Basics for AI** - Signal processing fundamentals
5. **Feature Extraction & Interpretation** - Pattern recognition
6. **Learning Objectives** - Summary of learning outcomes
7. **Glossary** - Term definitions

---

### 2.2 AI-Block Placement Rules

**Decision**: Place AI blocks at strategic points following pedagogical principles, using React components from Feature 011

**Placement Strategy**:

1. **`<AskQuestionBlock />`** - End of Section 1 (What Is Perception in Physical AI?)
   - **Position**: After content placeholder, after diagram placeholder
   - **Props**: `chapterId={3}`, `sectionId="what-is-perception-in-physical-ai"`
   - **Why**: Encourages active recall after new concept introduction
   - **Learning Theory**: Retrieval practice strengthens memory formation
   - **Physical AI Context**: Questions about perception definition, sensor types, real-world applications

2. **`<GenerateDiagramBlock />`** - Within Section 2 (Types of Sensors in Robotics)
   - **Position**: After content placeholder, before or after diagram placeholder
   - **Props**: `diagramType="sensor-categories-diagram"`, `chapterId={3}`
   - **Why**: Visual representation most valuable for sensor categorization
   - **Learning Theory**: Dual coding theory - combining text + visuals improves retention
   - **Physical AI Context**: Diagram showing sensor categories and their applications

3. **`<ExplainLike10Block />`** - Within Section 3 (Computer Vision & Depth Perception)
   - **Position**: After content placeholder, before diagram placeholder
   - **Props**: `concept="computer-vision"`, `chapterId={3}`
   - **Why**: Provides alternative explanation for complex vision concepts
   - **Learning Theory**: Multiple representations aid comprehension for diverse learners
   - **Physical AI Context**: Simplified explanation of computer vision and depth perception

4. **`<InteractiveQuizBlock />`** - End of Section 4 (Signal Processing Basics for AI)
   - **Position**: After content placeholder, after diagram placeholder
   - **Props**: `chapterId={3}`, `numQuestions={5}`
   - **Why**: Tests understanding of key signal processing concepts
   - **Learning Theory**: Formative assessment provides feedback on learning progress
   - **Physical AI Context**: Quiz covering sensors, vision, signal processing, and feature extraction

**Component Format**:
```jsx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';

// In section:
<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />
```

**Validation Rules**:
- All components MUST have `chapterId={3}`
- `sectionId` MUST match section anchor ID (kebab-case)
- `concept` MUST be Physical AI concept name (for ELI10)
- `diagramType` MUST match diagram placeholder name
- Components MUST be imported at top of MDX file

---

### 2.3 Diagram Placeholder Placement Rules

**Decision**: Place diagrams at strategic points using kebab-case HTML comments

**Placement Strategy**:

1. **`physical-ai-sensing-overview`** - Section 1 (What Is Perception in Physical AI?)
   - **Position**: After content placeholder, before AI block
   - **Why**: Provides high-level overview of perception system
   - **Content**: Shows how sensors, vision, and signal processing work together
   - **Learning Theory**: Visual overview aids schema formation

2. **`sensor-categories-diagram`** - Section 2 (Types of Sensors in Robotics)
   - **Position**: After content placeholder, before or after AI block
   - **Why**: Visual categorization of sensor types
   - **Content**: Shows different sensor categories (vision, LiDAR, motion, etc.)
   - **Learning Theory**: Visual categorization improves memory organization

3. **`depth-perception-flow`** - Section 3 (Computer Vision & Depth Perception)
   - **Position**: After content placeholder, after AI block
   - **Why**: Visualizes depth perception process
   - **Content**: Shows how depth information is extracted and processed
   - **Learning Theory**: Process diagrams aid understanding of complex workflows

4. **`signal-processing-pipeline`** - Section 4 (Signal Processing Basics for AI)
   - **Position**: After content placeholder, before AI block
   - **Why**: Visualizes signal processing workflow
   - **Content**: Shows signal processing steps (filtering, feature extraction, interpretation)
   - **Learning Theory**: Pipeline diagrams show data flow and transformation

**Placeholder Format**:
```html
<!-- DIAGRAM: physical-ai-sensing-overview -->
<!-- DIAGRAM: sensor-categories-diagram -->
<!-- DIAGRAM: depth-perception-flow -->
<!-- DIAGRAM: signal-processing-pipeline -->
```

**Validation Rules**:
- All placeholders MUST use kebab-case naming
- Placeholder names MUST match metadata `diagram_placeholders` list exactly
- Placeholders MUST be placed within appropriate sections
- Exactly 4 diagram placeholders required

---

### 2.4 Heading Anchor Rules

**Decision**: Use kebab-case anchor IDs matching section titles

**Anchor ID Format**:
- Section 1: `{#what-is-perception-in-physical-ai}`
- Section 2: `{#types-of-sensors-in-robotics}`
- Section 3: `{#computer-vision-depth-perception}`
- Section 4: `{#signal-processing-basics-for-ai}`
- Section 5: `{#feature-extraction-interpretation}`
- Section 6: `{#learning-objectives}`
- Section 7: `{#glossary}`

**Validation Rules**:
- Anchor IDs MUST be kebab-case (lowercase, hyphens for spaces)
- Anchor IDs MUST match section titles (converted to kebab-case)
- Anchor IDs MUST be unique within chapter
- Anchor IDs MUST be used in AI-block `sectionId` props

---

### 2.5 Glossary Formatting Rules

**Decision**: Use placeholder comments with list of 7 terms

**Glossary Format**:
```markdown
## Glossary {#glossary}

<!-- Content placeholder: Exactly 7 glossary terms with beginner-friendly definitions (10-100 words each, uses analogies):
- Perception
- Sensor
- Computer Vision
- Depth Perception
- Signal Processing
- Feature Extraction
- LiDAR (or alternative term)
-->
```

**Validation Rules**:
- MUST have exactly 7 glossary terms
- Terms MUST match metadata `glossary_terms` list exactly
- Terms MUST be listed in placeholder comment
- Definitions will be written in future feature (not in this feature)

**Glossary Terms** (7 total):
1. Perception
2. Sensor
3. Computer Vision
4. Depth Perception
5. Signal Processing
6. Feature Extraction
7. LiDAR (or alternative term)

---

### 2.6 Frontmatter Structure

**Decision**: Use standard Docusaurus frontmatter matching Chapter 1 and Chapter 2 pattern

**Frontmatter Format**:
```yaml
---
title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
description: "Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"
sidebar_position: 3
sidebar_label: "Chapter 3: Physical AI Perception Systems"
tags: ["physical-ai", "sensors", "perception", "signal-processing"]
---
```

**Validation Rules**:
- Title MUST start with "Chapter 3 — "
- Description MUST be 10-250 characters
- sidebar_position MUST be 3 (matches chapter number)
- sidebar_label MUST be abbreviated for sidebar navigation
- tags MUST include "physical-ai", "sensors", "perception", "signal-processing"

---

## 3. Metadata Plan

### 3.1 Required Python Dictionary Keys

**Decision**: Use Python dictionary matching Chapter 1 and Chapter 2 pattern

**Dictionary Structure**:
```python
CHAPTER_METADATA = {
    # Core identification (REQUIRED)
    "id": 3,
    "title": "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)",
    "summary": "placeholder",  # 2-3 sentence overview

    # Structure information (REQUIRED)
    "section_count": 7,
    "sections": [
        "What Is Perception in Physical AI?",
        "Types of Sensors in Robotics",
        "Computer Vision & Depth Perception",
        "Signal Processing Basics for AI",
        "Feature Extraction & Interpretation",
        "Learning Objectives",
        "Glossary"
    ],

    # Placeholder tracking (REQUIRED)
    "ai_blocks": [
        "ask-question",
        "explain-like-i-am-10",
        "interactive-quiz",
        "generate-diagram"
    ],
    "diagram_placeholders": [
        "physical-ai-sensing-overview",
        "sensor-categories-diagram",
        "depth-perception-flow",
        "signal-processing-pipeline"
    ],

    # Versioning (REQUIRED)
    "last_updated": "2025-12-05T00:00:00Z",

    # RAG-specific metadata (REQUIRED)
    "difficulty_level": "intermediate",
    "prerequisites": [1, 2],
    "learning_outcomes": ["placeholder list"],  # 3-8 items
    "glossary_terms": ["placeholder list"]  # 7 items
}
```

**Field Specifications**:

**Core Identification**:
- `id`: MUST be 3 (integer)
- `title`: MUST match MDX frontmatter `title` exactly (string)
- `summary`: 2-3 sentence overview (50-300 characters, string)

**Structure Information**:
- `section_count`: MUST be 7 (integer)
- `sections`: MUST be list of exactly 7 strings matching MDX H2 section titles in order

**Placeholder Tracking**:
- `ai_blocks`: MUST be list of exactly 4 strings (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
- `diagram_placeholders`: MUST be list of exactly 4 strings (physical-ai-sensing-overview, sensor-categories-diagram, depth-perception-flow, signal-processing-pipeline)

**Versioning**:
- `last_updated`: ISO 8601 timestamp string (e.g., "2025-12-05T00:00:00Z")

**RAG-Specific Metadata**:
- `difficulty_level`: MUST be "intermediate" (string)
- `prerequisites`: MUST be [1, 2] (list of integers)
- `learning_outcomes`: List of 3-8 strings (measurable learning objectives)
- `glossary_terms`: List of exactly 7 strings matching MDX glossary terms

---

### 3.2 Validation Expectations

**Decision**: Validate metadata structure matches MDX exactly

**Validation Rules**:
1. **Section Count Validation**: `section_count` MUST equal length of `sections` list (7)
2. **Section Title Validation**: `sections` list MUST match MDX H2 section titles exactly
3. **AI Block Validation**: `ai_blocks` count MUST match MDX AI-block components (4)
4. **Diagram Validation**: `diagram_placeholders` count MUST match MDX diagram placeholders (4)
5. **Glossary Validation**: `glossary_terms` count MUST match MDX glossary terms (7)
6. **Title Validation**: `title` MUST match MDX frontmatter `title` exactly
7. **Difficulty Validation**: `difficulty_level` MUST be "intermediate"
8. **Prerequisites Validation**: `prerequisites` MUST be [1, 2]

**Validation Script** (Python):
```python
from app.content.chapters.chapter_3 import CHAPTER_METADATA

assert CHAPTER_METADATA["id"] == 3
assert CHAPTER_METADATA["section_count"] == 7
assert len(CHAPTER_METADATA["sections"]) == 7
assert len(CHAPTER_METADATA["ai_blocks"]) == 4
assert len(CHAPTER_METADATA["diagram_placeholders"]) == 4
assert CHAPTER_METADATA["difficulty_level"] == "intermediate"
assert CHAPTER_METADATA["prerequisites"] == [1, 2]
assert len(CHAPTER_METADATA["glossary_terms"]) == 7
```

---

### 3.3 How Metadata Aligns to MDX Structure

**Decision**: Metadata MUST match MDX structure exactly

**Alignment Rules**:

1. **Section Alignment**:
   - MDX H2 section titles → `sections` list (exact match, same order)
   - MDX section count → `section_count` (must be 7)

2. **Placeholder Alignment**:
   - MDX diagram placeholders → `diagram_placeholders` list (exact match)
   - MDX AI-block components → `ai_blocks` list (exact match)

3. **Glossary Alignment**:
   - MDX glossary terms → `glossary_terms` list (exact match)

4. **Title Alignment**:
   - MDX frontmatter `title` → `title` field (exact match)

**Cross-Validation**:
- Extract section titles from MDX → Compare with `sections` list
- Extract diagram placeholders from MDX → Compare with `diagram_placeholders` list
- Extract AI-block components from MDX → Compare with `ai_blocks` list
- Extract glossary terms from MDX → Compare with `glossary_terms` list

---

## 4. RAG Chunking Preparation

### 4.1 Insert Markers Inside MDX

**Decision**: Use placeholder comments to mark future chunk boundaries

**Chunk Marker Strategy**:
- Content placeholders in each section will serve as chunk boundaries
- Section headings (H2) will be natural chunk boundaries
- Diagram placeholders will mark visual content chunks
- AI-block components will mark interactive content chunks

**Placeholder Format** (in MDX):
```markdown
## Section Title {#section-id}

<!-- Content placeholder: Description of what content should be written here. Min 200 words, 7th-8th grade level. -->

<!-- DIAGRAM: diagram-name -->

<AIBlockComponent chapterId={3} ... />
```

**Future Chunking Strategy** (documented in chunk file):
- Chunk by section (respect H2 boundaries)
- Max token size: 512 tokens per chunk
- Semantic segmentation by section
- Heading-aware slicing
- Overlapping window strategy (50 tokens overlap)

---

### 4.2 Define Chunk Strategy (Semantic Boundaries)

**Decision**: Document chunk strategy in chunk file with TODO comments

**Chunk Strategy** (in `chapter_3_chunks.py`):
```python
def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 3 with metadata.
    
    TODO: Implement chunking from Chapter 3 MDX content
    TODO: Load Chapter 3 content from frontend/docs/chapters/chapter-3.mdx
    TODO: Implement chunking strategy:
        - Max token size constraints (e.g., 512 tokens per chunk)
        - Semantic segmentation by section
        - Heading-aware slicing (respect H2 boundaries)
        - Overlapping window strategy (e.g., 50 tokens overlap)
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch3-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Include Physical AI-specific metadata (concepts: perception, sensors, vision, signal processing)
    """
    # Placeholder return - no real chunking implementation
    return []
```

**Semantic Boundaries**:
- **Section Boundaries**: Each H2 section is a natural semantic boundary
- **Concept Boundaries**: Each major concept (perception, sensors, vision, signal processing) is a semantic boundary
- **Visual Boundaries**: Diagram placeholders mark visual content boundaries
- **Interactive Boundaries**: AI-block components mark interactive content boundaries

**Chunk Metadata** (future implementation):
- `id`: Unique chunk ID (e.g., "ch3-s1-c0")
- `text`: Chunk text content
- `chapter_id`: 3
- `section_id`: Section identifier (e.g., "what-is-perception-in-physical-ai")
- `position`: Position in chapter (0-based)
- `word_count`: Word count
- `metadata`: Additional metadata (heading, type, has_diagram, has_ai_block)

---

## 5. Documentation Deliverables

### 5.1 Content Schema Template Usage

**File**: `specs/017-chapter-3-content/contracts/content-schema.md`
**Status**: Already created in spec phase
**Purpose**: Define data contracts and validation schemas for Chapter 3 content structure

**Key Sections**:
- MDX frontmatter schema
- Chapter metadata schema (Python)
- Glossary schema
- AI-block placeholder schema
- Diagram placeholder schema
- Section structure schema
- RAG chunk file schema
- Writing style constraints schema
- Cross-validation rules

**Usage**: Reference during implementation to ensure structure matches contracts

---

### 5.2 Requirements Checklist Usage

**File**: `specs/017-chapter-3-content/checklists/requirements.md`
**Status**: Already created in spec phase
**Purpose**: Validate spec completeness and quality

**Key Sections**:
- Content quality check
- Requirement completeness check
- Feature readiness check
- Validation results

**Usage**: Verify all requirements are met before moving to implementation

---

### 5.3 Quickstart Guide Usage

**File**: `specs/017-chapter-3-content/quickstart.md`
**Status**: Already created in spec phase
**Purpose**: Step-by-step implementation guide

**Key Sections**:
- Prerequisites
- Implementation overview (4 phases)
- Step-by-step instructions
- Validation steps
- Success criteria
- Troubleshooting guide

**Usage**: Follow during implementation to ensure all steps are completed

---

### 5.4 Research Document Usage

**File**: `specs/017-chapter-3-content/research.md`
**Status**: Already created in spec phase
**Purpose**: Document research findings and writing guidelines

**Key Sections**:
- Research questions & resolutions
- Industry references
- Observations
- Technology stack
- Content writing strategy

**Usage**: Reference during content writing (future feature) for writing style and guidelines

---

### 5.5 Data Model Usage

**File**: `specs/017-chapter-3-content/data-model.md`
**Status**: Already created in spec phase
**Purpose**: Define data structures and entities

**Key Sections**:
- Entity definitions (7 entities)
- Data relationships diagram
- Data flow (current and future state)
- Validation summary

**Usage**: Reference during implementation to understand data structures

---

## 6. Acceptance Checks

### 6.1 MDX Builds Successfully

**Check**: Docusaurus build test
**Command**: `cd frontend && npm run build`
**Expected Result**: Build succeeds without errors
**Validation**:
- No MDX syntax errors
- Frontmatter is valid YAML
- All React components import correctly
- All section headings are valid Markdown

**Failure Handling**: Fix syntax errors, validate frontmatter, check component imports

---

### 6.2 Metadata Schema Imports Without Error

**Check**: Python import test
**Command**: `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"`
**Expected Result**: Import succeeds without errors
**Validation**:
- File exists at correct path
- Python syntax is valid
- Dictionary structure is correct
- All required fields are present

**Failure Handling**: Fix Python syntax errors, validate dictionary structure, check field names

---

### 6.3 All Placeholders Present and Valid

**Check**: Manual structure validation
**Command**: Manual review + grep commands
**Expected Result**: All placeholders match spec requirements
**Validation**:
- Exactly 7 H2 sections
- Exactly 4 diagram placeholders (kebab-case)
- Exactly 4 AI-block components (chapterId={3})
- Exactly 7 glossary terms
- All placeholders use correct naming conventions

**Validation Commands**:
```bash
# Count H2 sections
grep -c "^## " frontend/docs/chapters/chapter-3.mdx
# Expected: 7

# Count diagram placeholders
grep -c "<!-- DIAGRAM:" frontend/docs/chapters/chapter-3.mdx
# Expected: 4

# Count AI-block components
grep -c "chapterId={3}" frontend/docs/chapters/chapter-3.mdx
# Expected: 4
```

**Failure Handling**: Add missing placeholders, fix naming conventions, verify counts

---

### 6.4 Metadata Matches MDX Structure

**Check**: Cross-validation test
**Command**: Python validation script
**Expected Result**: All metadata fields match MDX structure exactly
**Validation**:
- `section_count` matches MDX H2 count (7)
- `sections` list matches MDX H2 titles exactly
- `ai_blocks` count matches MDX AI-block count (4)
- `diagram_placeholders` count matches MDX diagram count (4)
- `glossary_terms` count matches MDX glossary count (7)
- `title` matches MDX frontmatter `title` exactly

**Validation Script**:
```python
from app.content.chapters.chapter_3 import CHAPTER_METADATA

# Extract from MDX (manual or automated)
mdx_sections = ["What Is Perception in Physical AI?", ...]  # 7 items
mdx_diagrams = ["physical-ai-sensing-overview", ...]  # 4 items
mdx_ai_blocks = ["ask-question", ...]  # 4 items
mdx_glossary = ["Perception", ...]  # 7 items

# Validate
assert CHAPTER_METADATA["section_count"] == len(mdx_sections)
assert CHAPTER_METADATA["sections"] == mdx_sections
assert CHAPTER_METADATA["diagram_placeholders"] == mdx_diagrams
assert CHAPTER_METADATA["ai_blocks"] == mdx_ai_blocks
assert CHAPTER_METADATA["glossary_terms"] == mdx_glossary
```

**Failure Handling**: Update metadata to match MDX, or update MDX to match metadata

---

### 6.5 Chunk File Function Exists

**Check**: Python import and function signature test
**Command**: `python -c "from app.content.chapters.chapter_3_chunks import get_chapter_chunks; assert callable(get_chapter_chunks)"`
**Expected Result**: Function exists with correct signature
**Validation**:
- Function exists
- Function signature is correct: `get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]`
- Function is callable
- Function returns empty list (placeholder)

**Failure Handling**: Fix function signature, ensure function exists, validate return type

---

## File & Folder Plan

### Files to Create

1. **`frontend/docs/chapters/chapter-3.mdx`**
   - New file
   - MDX structure with placeholders only
   - 7 H2 sections, 4 diagrams, 4 AI blocks, 7 glossary terms

2. **`backend/app/content/chapters/chapter_3.py`**
   - New file
   - Python metadata dictionary
   - All required fields matching MDX structure

3. **`backend/app/content/chapters/chapter_3_chunks.py`**
   - New file
   - RAG chunk file with placeholder function
   - Function signature: `get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]`

### Files Already Created (Spec Phase)

1. **`specs/017-chapter-3-content/contracts/content-schema.md`** - Already created
2. **`specs/017-chapter-3-content/checklists/requirements.md`** - Already created
3. **`specs/017-chapter-3-content/research.md`** - Already created
4. **`specs/017-chapter-3-content/data-model.md`** - Already created
5. **`specs/017-chapter-3-content/quickstart.md`** - Already created

---

## Risks / Constraints

### Risk 1: Section Count Mismatch
**Description**: MDX might have different number of sections than metadata
**Mitigation**: Cross-validation script to ensure `section_count` matches MDX H2 count
**Impact**: Low (caught during validation)

### Risk 2: Placeholder Naming Inconsistency
**Description**: Diagram placeholders might not use kebab-case consistently
**Mitigation**: Validation script to check naming conventions
**Impact**: Low (caught during validation)

### Risk 3: AI-Block Component Import Errors
**Description**: React components might not import correctly
**Mitigation**: Docusaurus build test will catch import errors
**Impact**: Medium (caught during build)

### Risk 4: Metadata Field Mismatch
**Description**: Metadata fields might not match MDX structure exactly
**Mitigation**: Cross-validation script to ensure all fields match
**Impact**: Medium (caught during validation)

---

## Acceptance Criteria Mapping

### AC1: Structure Complete
- ✅ MDX file has exactly 7 H2 sections
- ✅ MDX file has exactly 4 diagram placeholders
- ✅ MDX file has exactly 4 AI-block components
- ✅ MDX file has exactly 7 glossary terms
- ✅ Frontmatter is complete and valid

### AC2: Metadata Complete
- ✅ Python metadata file has all required fields
- ✅ `section_count` matches MDX (7)
- ✅ `sections` list matches MDX exactly
- ✅ `ai_blocks` count matches MDX (4)
- ✅ `diagram_placeholders` count matches MDX (4)
- ✅ `difficulty_level` is "intermediate"
- ✅ `prerequisites` is [1, 2]

### AC3: Contracts Complete
- ✅ All contract files exist (already created in spec phase)
- ✅ All documentation files exist (already created in spec phase)

### AC4: Validation Ready
- ✅ Structure can be validated against contracts
- ✅ Docusaurus build succeeds
- ✅ Python imports succeed

---

## Dependencies & Next Steps

### Dependencies
- Feature 003 (Chapter 1 Content): Template pattern reference
- Feature 014 (Chapter 2 Content): Template pattern reference
- Feature 011 (Chapter 2 AI Blocks): React components available
- Docusaurus 3.x: Frontend framework
- Python 3.11+: Backend runtime

### Next Steps
1. **Task Generation**: Run `/sp.tasks` to create implementation tasks
2. **Implementation**: Run `/sp.implement` to create actual structure files
3. **Content Writing**: Write actual content (future feature)
4. **Validation**: Validate content quality and structure (future feature)

---

## Notes

- This feature creates structure only (no actual content)
- Content writing will be done in future features
- All placeholders must use consistent naming conventions
- Chapter 3 is intermediate difficulty (requires Chapters 1 and 2)
- Focus on Physical AI perception systems: sensors, vision, signal processing
- Follow Chapter 1 and Chapter 2 patterns for consistency
