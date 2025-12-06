# Implementation Plan: Chapter 3 — Planning Layer (Content Architecture, Metadata, Validation, RAG-Prep)

**Branch**: `018-chapter-3-plan` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/018-chapter-3-plan/spec.md`

## Summary

This feature establishes the complete Chapter 3 planning layer architecture: MDX structure with placeholders, metadata schema, glossary items, AI-block markers (HTML comment format), diagram placeholders, chunk markers for RAG preparation, and backend metadata file. **NO real text content is written**—only structure and placeholders. The implementation creates an MDX skeleton with exactly 7 H2 sections, 4 diagram placeholders (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline), 4 AI-block HTML comment placeholders, chunk markers (CHUNK: START / CHUNK: END), and a glossary section with 7 placeholder terms. A backend metadata file provides structured information for future RAG integration, and comprehensive contracts document validation rules and content writing guidelines.

**Primary Deliverable**: `frontend/docs/chapters/chapter-3.mdx` (MDX skeleton with structure only, including chunk markers)
**Secondary Deliverable**: `backend/app/content/chapters/chapter_3.py` (Python metadata dictionary)
**Tertiary Deliverable**: Contract files (content-schema.md, checklists, research.md, quickstart.md, data-model.md)
**Validation**: Manual structure review + Docusaurus build test + Python import test + chunk marker validation

**Note**: Feature 017-chapter-3-content has already been completed with different diagram names and React component format. This plan (Feature 018) uses HTML comment format for AI-blocks and different diagram names, and includes chunk markers for RAG preparation.

## Technical Context

**Language/Version**:
- Frontend: MDX (Markdown + JSX) compatible with Docusaurus 3.x
- Backend: Python 3.11+

**Primary Dependencies**:
- Frontend: Docusaurus 3.x (already installed)
- Backend: Python 3.11+ standard library (no new dependencies)
- Feature 003 (Chapter 1 Content): Template pattern reference
- Feature 010 (Chapter 2 Content): Template pattern reference
- Feature 017 (Chapter 3 Content): Already completed (note differences in diagram names and AI-block format)

**Storage**: Static files (MDX content, Python module) - no database

**Testing**:
- Frontend: `npm run build` validation (Docusaurus build process)
- Backend: Python import test (`python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"`)
- Manual: Structure validation (section count, placeholder count, naming conventions, chunk marker pairing)

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
- MUST use HTML comment format for AI-block placeholders (`<!-- AI-BLOCK: type -->`)
- MUST include chunk markers (CHUNK: START / CHUNK: END) for RAG preparation
- Backend metadata MUST remain simple Python dictionary (no Pydantic model, no database)
- Chapter 3 is intermediate difficulty (requires Chapters 1 and 2 as prerequisites)
- Chunk markers MUST be properly paired (START with END)

**Scale/Scope**:
- 1 chapter (Chapter 3 only)
- 7 H2 sections (structure only, no content)
- 7 glossary term placeholders
- 4 diagram placeholders (kebab-case: perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
- 4 AI-block HTML comment placeholders (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
- Chunk markers (CHUNK: START / CHUNK: END) for RAG preparation
- 1 backend metadata file
- 5 contract files (already created in spec phase)

---

## 1. File Structure to be Created

### 1.1 Frontend Files

**File**: `frontend/docs/chapters/chapter-3.mdx`
- **Purpose**: MDX content file with structure and placeholders only, including chunk markers
- **Content**: YAML frontmatter, 7 H2 sections, 4 diagram placeholders, 4 AI-block HTML comment placeholders, chunk markers (CHUNK: START / CHUNK: END), glossary section
- **Status**: New file (does not exist yet) OR update existing if Feature 017 already created it
- **Validation**: Docusaurus build test, structure validation, chunk marker pairing validation

### 1.2 Backend Files

**File**: `backend/app/content/chapters/chapter_3.py`
- **Purpose**: Python metadata dictionary for Chapter 3
- **Content**: `CHAPTER_METADATA` dictionary with all required fields
- **Status**: New file (does not exist yet) OR update existing if Feature 017 already created it
- **Validation**: Python import test, field validation

**File**: `backend/app/content/chapters/chapter_3_chunks.py`
- **Purpose**: RAG chunk file with placeholder function
- **Content**: `get_chapter_chunks(chapter_id: int = 3)` function with chunk marker support
- **Status**: New file (does not exist yet) OR update existing if Feature 017 already created it
- **Validation**: Python import test, function signature validation

### 1.3 Contract Files (Already Created in Spec Phase)

**File**: `specs/018-chapter-3-plan/contracts/content-schema.md`
- **Purpose**: Content schema contract with validation rules
- **Status**: Already created in spec phase
- **Validation**: Manual review

**File**: `specs/018-chapter-3-plan/checklists/requirements.md`
- **Purpose**: Specification quality checklist
- **Status**: Already created in spec phase
- **Validation**: Manual review

**File**: `specs/018-chapter-3-plan/research.md`
- **Purpose**: Research document with planning guidelines
- **Status**: Already created in spec phase
- **Validation**: Manual review

**File**: `specs/018-chapter-3-plan/data-model.md`
- **Purpose**: Data model with entity definitions
- **Status**: Already created in spec phase
- **Validation**: Manual review

**File**: `specs/018-chapter-3-plan/quickstart.md`
- **Purpose**: Quickstart guide for implementation
- **Status**: Already created in spec phase
- **Validation**: Manual review

---

## 2. MDX Composition Plan

### 2.1 Frontmatter Structure

**Location**: Top of `frontend/docs/chapters/chapter-3.mdx`

**Required Fields**:
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
- Title MUST start with "Chapter 3 — " format
- Description MUST be 10-250 characters
- sidebar_position MUST be 3 (matches chapter number)
- All fields MUST be valid YAML (no unescaped special characters)
- Frontmatter MUST be enclosed by `---` delimiters at start and end

### 2.2 Section Structure (Exactly 7 H2 Sections)

**Section Order** (MUST match this exact order):

1. **What Is Perception in Physical AI?** `{#what-is-perception-in-physical-ai}`
   - Content placeholder: Definition of perception in Physical AI, why perception is essential for autonomous systems, how sensors enable perception, and at least 3 real-world examples (autonomous vehicles, robotics, drones). Use eyes and ears analogy for sensors. Min 200 words, Grade 7-8 level.
   - Diagram placeholder: `<!-- DIAGRAM: perception-overview -->`
   - AI-block placeholder: `<!-- AI-BLOCK: ask-question -->`
   - Chunk markers: `<!-- CHUNK: START -->` at beginning, `<!-- CHUNK: END -->` at end

2. **Types of Sensors in Robotics** `{#types-of-sensors-in-robotics}`
   - Content placeholder: Explanation of different sensor types (vision, LiDAR, motion, etc.), sensor categories, and how each type contributes to perception. Use categorization analogy. Min 200 words.
   - Diagram placeholder: `<!-- DIAGRAM: sensor-types -->`
   - AI-block placeholder: `<!-- AI-BLOCK: generate-diagram -->`
   - Chunk markers: `<!-- CHUNK: START -->` at beginning, `<!-- CHUNK: END -->` at end

3. **Computer Vision & Depth Perception** `{#computer-vision-depth-perception}`
   - Content placeholder: Explanation of computer vision, depth perception, how machines interpret visual information, and 3D spatial understanding. Use human vision analogy. Min 200 words.
   - Diagram placeholder: `<!-- DIAGRAM: cv-depth-flow -->`
   - AI-block placeholder: `<!-- AI-BLOCK: explain-like-i-am-10 -->`
   - Chunk markers: `<!-- CHUNK: START -->` at beginning, `<!-- CHUNK: END -->` at end

4. **Signal Processing Basics for AI** `{#signal-processing-basics-for-ai}`
   - Content placeholder: Explanation of signal processing, filtering noise, cleaning sensor data, and how signal processing enables better decision-making. Use filtering analogy. Min 200 words.
   - Diagram placeholder: `<!-- DIAGRAM: feature-extraction-pipeline -->`
   - AI-block placeholder: `<!-- AI-BLOCK: interactive-quiz -->`
   - Chunk markers: `<!-- CHUNK: START -->` at beginning, `<!-- CHUNK: END -->` at end

5. **Feature Extraction & Interpretation** `{#feature-extraction-interpretation}`
   - Content placeholder: Explanation of feature extraction, pattern recognition, identifying important information from raw data, and how features enable decision-making. Use pattern recognition analogy. Min 200 words.
   - No diagram placeholder
   - No AI-block placeholder
   - Chunk markers: `<!-- CHUNK: START -->` at beginning, `<!-- CHUNK: END -->` at end

6. **Learning Objectives** `{#learning-objectives}`
   - Content placeholder: 3-8 learning objectives covering:
     - Define perception in Physical AI
     - Identify sensor types
     - Explain computer vision and depth perception
     - Describe signal processing basics
     - Understand feature extraction
     - Explain how perception enables autonomous decision-making
   - No diagram placeholder
   - No AI-block placeholder
   - Chunk markers: `<!-- CHUNK: START -->` at beginning, `<!-- CHUNK: END -->` at end

7. **Glossary** `{#glossary}`
   - Content placeholder: Exactly 7 glossary terms with beginner-friendly definitions (10-100 words each, uses analogies):
     - Perception
     - Sensor
     - Computer Vision
     - Depth Perception
     - Signal Processing
     - Feature Extraction
     - LiDAR (or alternative term)
   - No diagram placeholder
   - No AI-block placeholder
   - Chunk markers: `<!-- CHUNK: START -->` at beginning, `<!-- CHUNK: END -->` at end

### 2.3 Diagram Placeholder Placement Rules

**Total Count**: Exactly 4 diagram placeholders

**Placement**:
1. `<!-- DIAGRAM: perception-overview -->` - Section 1 (What Is Perception in Physical AI?)
2. `<!-- DIAGRAM: sensor-types -->` - Section 2 (Types of Sensors in Robotics)
3. `<!-- DIAGRAM: cv-depth-flow -->` - Section 3 (Computer Vision & Depth Perception)
4. `<!-- DIAGRAM: feature-extraction-pipeline -->` - Section 4 (Signal Processing Basics for AI)

**Format**: HTML comment format
```html
<!-- DIAGRAM: perception-overview -->
```

**Validation Rules**:
- All diagram placeholders MUST use kebab-case naming
- All diagram placeholders MUST match metadata `diagram_placeholders` list exactly
- All diagram placeholders MUST be placed within appropriate sections
- Format MUST be `<!-- DIAGRAM: {name} -->` (with spaces)

**Note**: These diagram names differ from Feature 017:
- Feature 017: physical-ai-sensing-overview, sensor-categories-diagram, depth-perception-flow, signal-processing-pipeline
- Feature 018: perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline

### 2.4 AI-Block Placeholder Placement Rules

**Total Count**: Exactly 4 AI-block placeholders

**Placement**:
1. `<!-- AI-BLOCK: ask-question -->` - Section 1 (What Is Perception in Physical AI?)
2. `<!-- AI-BLOCK: generate-diagram -->` - Section 2 (Types of Sensors in Robotics)
3. `<!-- AI-BLOCK: explain-like-i-am-10 -->` - Section 3 (Computer Vision & Depth Perception)
4. `<!-- AI-BLOCK: interactive-quiz -->` - Section 4 (Signal Processing Basics for AI)

**Format**: HTML comment format
```html
<!-- AI-BLOCK: ask-question -->
```

**Validation Rules**:
- All AI-block placeholders MUST use HTML comment format
- All AI-block placeholders MUST match metadata `ai_blocks` list exactly
- Format MUST be `<!-- AI-BLOCK: {type} -->` (with spaces, uppercase AI-BLOCK)
- All AI-block placeholders MUST be placed within appropriate sections

**Note**: Feature 017 uses React components (`<AskQuestionBlock chapterId={3} />`). Feature 018 uses HTML comments for planning layer clarity.

### 2.5 Chunk Marker Placement Rules

**Total Count**: 7 chunk marker pairs (one pair per section)

**Placement**:
- Each H2 section MUST have a chunk marker pair:
  - `<!-- CHUNK: START -->` at beginning of section content
  - `<!-- CHUNK: END -->` at end of section content

**Format**: HTML comment format
```html
<!-- CHUNK: START -->
[Section content]
<!-- CHUNK: END -->
```

**Validation Rules**:
- Chunk markers MUST be properly paired (START with END)
- Chunk markers MUST align with concept boundaries
- Chunk markers MUST respect H2 section boundaries
- Format MUST be `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` (with spaces, uppercase CHUNK)
- Chunk markers MUST be placed at logical semantic boundaries

**Chunking Strategy**:
- Section-based logical chunks: Each H2 section is a natural chunk boundary
- Concept boundaries: Chunk markers align with concept boundaries
- Semantic segmentation: Chunks respect semantic meaning and context
- No cross-section chunks: Chunks do not cross H2 section boundaries

### 2.6 Glossary Section Structure

**Location**: Section 7 (Glossary)

**Content**: Exactly 7 glossary terms with placeholder definitions:
1. Perception
2. Sensor
3. Computer Vision
4. Depth Perception
5. Signal Processing
6. Feature Extraction
7. LiDAR (or alternative term)

**Format**: Placeholder comments only (no actual definitions)
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
- Each term MUST have placeholder definition (10-100 words)
- Definitions MUST use analogies when possible
- Terms MUST match metadata `glossary_terms` list

### 2.7 Reading Level Constraints

**Target Reading Level**: Grade 7-8

**Sentence Structure**:
- Average 15-20 words per sentence
- Mix simple and compound sentences for rhythm
- Avoid complex subordinate clauses stacked deeply
- Break dense Physical AI concepts into 2-3 shorter sentences

**Paragraph Structure**:
- 3-4 sentences per paragraph maximum
- One main idea per paragraph
- Use transition sentences to connect concepts
- Break long explanations into multiple paragraphs

**Vocabulary**:
- Introduce Physical AI terms with immediate context
- Use analogies from daily life (eyes and ears for sensors, filtering noise for signal processing)
- Define technical terms on first use with simple explanations

**Tone**:
- Conversational-educational
- Second-person ("you") to create direct connection with learner
- Friendly but not condescending
- Enthusiastic about Physical AI without being overly casual

---

## 3. Metadata Architecture Plan

### 3.1 Python Metadata File Structure

**File**: `backend/app/content/chapters/chapter_3.py`

**Structure**:
```python
"""
Chapter 3 metadata for RAG integration and content management.

This module contains structured metadata for Chapter 3: "Physical AI Perception Systems"
including section information, placeholder tracking, and learning objectives.

TODO: Future RAG Integration Points
- [ ] Create Pydantic model for ChapterMetadata with validation rules
- [ ] Implement embedding generation for chapter content (OpenAI/local models)
- [ ] Store embeddings in Qdrant vector database with metadata
- [ ] Create API endpoint GET /api/chapters/3 to serve this metadata
- [ ] Add semantic search capability across all chapters
- [ ] Implement chapter recommendation based on prerequisites and difficulty
- [ ] Validate prerequisites (ensure Chapters 1 and 2 exist before Chapter 3)
"""

from typing import List

CHAPTER_METADATA = {
    # Core identification
    "id": 3,
    "title": "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)",
    "summary": "placeholder",  # 2-3 sentence overview

    # Structure information
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

    # Placeholder tracking
    "ai_blocks": [
        "ask-question",
        "explain-like-i-am-10",
        "interactive-quiz",
        "generate-diagram"
    ],
    "diagram_placeholders": [
        "perception-overview",
        "sensor-types",
        "cv-depth-flow",
        "feature-extraction-pipeline"
    ],

    # Versioning
    "last_updated": "2025-12-05T00:00:00Z",

    # RAG-specific metadata
    "difficulty_level": "intermediate",
    "prerequisites": [1, 2],  # Chapters 1 and 2 are prerequisites
    "learning_outcomes": ["placeholder list"],  # 3-8 items
    "glossary_terms": ["placeholder list"]  # 7 items
}
```

### 3.2 Field Specifications

**Core Identification**:
- `id`: MUST be 3 (integer)
- `title`: MUST match MDX frontmatter `title` exactly
- `summary`: Placeholder (2-3 sentence overview, 50-300 characters)

**Structure Information**:
- `section_count`: MUST be 7 (integer)
- `sections`: MUST be list of exactly 7 strings matching MDX H2 section titles in order

**Placeholder Tracking**:
- `ai_blocks`: MUST be list of exactly 4 strings:
  - "ask-question"
  - "explain-like-i-am-10"
  - "interactive-quiz"
  - "generate-diagram"
- `diagram_placeholders`: MUST be list of exactly 4 strings (kebab-case):
  - "perception-overview"
  - "sensor-types"
  - "cv-depth-flow"
  - "feature-extraction-pipeline"

**Versioning**:
- `last_updated`: ISO 8601 timestamp string (e.g., "2025-12-05T00:00:00Z")

**RAG-Specific Metadata**:
- `difficulty_level`: MUST be "intermediate" (string)
- `prerequisites`: MUST be [1, 2] (list of integers)
- `learning_outcomes`: List of 3-8 strings (measurable learning objectives) - placeholder list
- `glossary_terms`: List of exactly 7 strings matching MDX glossary terms - placeholder list

### 3.3 MDX → Metadata Validation Mapping

**Cross-Validation Rules**:
1. MDX `title` MUST match metadata `title` exactly
2. MDX H2 section count MUST match metadata `section_count` (7)
3. MDX H2 section titles MUST match metadata `sections` list exactly (in order)
4. MDX diagram placeholders MUST match metadata `diagram_placeholders` list exactly
5. MDX AI-block placeholders MUST match metadata `ai_blocks` list
6. MDX glossary terms MUST match metadata `glossary_terms` list exactly (7 items)

**Validation Process**:
1. Extract MDX frontmatter `title` and compare with metadata `title`
2. Count MDX H2 sections and compare with metadata `section_count`
3. Extract MDX H2 section titles and compare with metadata `sections` list (order-sensitive)
4. Extract MDX diagram placeholders and compare with metadata `diagram_placeholders` list
5. Extract MDX AI-block placeholders and compare with metadata `ai_blocks` list
6. Extract MDX glossary terms and compare with metadata `glossary_terms` list

---

## 4. RAG Prep Plan

### 4.1 Chunking Strategy

**Approach**: Section-based logical chunks with chunk markers

**Chunk Boundaries**:
- Each H2 section is a natural chunk boundary
- Chunk markers (`<!-- CHUNK: START -->` / `<!-- CHUNK: END -->`) define explicit chunk boundaries
- Chunks respect semantic meaning and context
- Chunks do not cross H2 section boundaries

**Chunk Marker Format**:
```html
<!-- CHUNK: START -->
[Section content - paragraphs, placeholders, etc.]
<!-- CHUNK: END -->
```

**Chunking Rules**:
1. **Section-based**: Each H2 section is a natural chunk boundary
2. **Concept boundaries**: Chunk markers align with concept boundaries
3. **Semantic segmentation**: Chunks respect semantic meaning and context
4. **No cross-section chunks**: Chunks do not cross H2 section boundaries

### 4.2 Chunk File Structure

**File**: `backend/app/content/chapters/chapter_3_chunks.py`

**Function Signature**:
```python
from typing import List, Dict, Any

def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 3 with metadata.
    
    Chunks respect chunk markers (CHUNK: START / CHUNK: END).
    
    Args:
        chapter_id: Chapter identifier (default: 3 for Chapter 3)
    
    Returns:
        List of chunk dictionaries with structure:
        [
            {
                "id": str,                    # Unique chunk ID (e.g., "ch3-s1-c0")
                "text": str,                  # Chunk text content
                "chapter_id": 3,              # Chapter identifier
                "section_id": str,            # Section identifier (e.g., "what-is-perception-in-physical-ai")
                "position": int,              # Position in chapter (0-based)
                "word_count": int,            # Word count
                "metadata": {                 # Additional metadata
                    "heading": str,          # Section heading
                    "type": str,             # "paragraph", "heading", "glossary", etc.
                    "has_diagram": bool,     # True if section has diagram placeholder
                    "has_ai_block": bool,    # True if section has AI block
                    "chunk_markers": bool     # True if chunk has START/END markers
                }
            },
            ...
        ]
    
    TODO: Implement chunking from Chapter 3 MDX content
    TODO: Load Chapter 3 content from frontend/docs/chapters/chapter-3.mdx
    TODO: Implement chunking strategy:
        - Respect chunk markers (CHUNK: START / CHUNK: END)
        - Section-based logical chunks
        - Semantic segmentation by section
        - Heading-aware slicing (respect H2 boundaries)
        - Max token size constraints (e.g., 512 tokens per chunk)
        - Overlapping window strategy (e.g., 50 tokens overlap)
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch3-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Include Physical AI-specific metadata (concepts: perception, sensors, vision, signal processing)
    TODO: Future: Generate embeddings for each chunk using embedding model
    TODO: Future: Store embeddings in Qdrant collection "chapter_3"
    TODO: Future: Include chunk metadata for semantic search
    """
    # Placeholder return - no real chunking implementation
    return []
```

**Validation Rules**:
- Function MUST exist with correct signature
- Function MUST return `List[Dict[str, Any]]`
- Function MUST have `chapter_id: int = 3` parameter
- Function MUST be importable without errors
- Function MUST respect chunk markers when implemented

### 4.3 RAG Integration Planning

**Embedding Pipeline Integration** (Feature 020):
- Chunks will be embedded using embedding model (e.g., text-embedding-3-small)
- Embedding generation will respect chunk boundaries defined by chunk markers
- Chunk metadata will be included in embedding generation

**Qdrant Upsert Strategy**:
- Chunks will be stored in Qdrant collection "chapter_3"
- Each chunk will include:
  - Vector embedding (from embedding model)
  - Metadata (section_id, position, word_count, has_diagram, has_ai_block, chunk_markers)
  - Text content (for retrieval context assembly)

**Retrieval Context Format**:
- Chunks will be retrieved with metadata for context assembly
- Context will include:
  - Chunk text content
  - Section heading
  - Position in chapter
  - Related concepts (perception, sensors, vision, signal processing)

**Chunk Marker Support**:
- Chunk markers (CHUNK: START / CHUNK: END) will guide chunking implementation
- Chunking function will respect chunk marker boundaries
- Chunk metadata will include `chunk_markers: bool` flag

---

## 5. Validation Plan

### 5.1 Frontend Build Test

**Command**: `npm run build` (in `frontend/` directory)

**Validation Steps**:
1. Navigate to `frontend/` directory
2. Run `npm run build`
3. Verify build completes without errors
4. Verify no warnings about Chapter 3 MDX file
5. Verify Chapter 3 page is generated in build output

**Success Criteria**:
- Build completes with exit code 0
- No errors or warnings related to Chapter 3 MDX file
- Chapter 3 page exists in build output

### 5.2 Section Count Test

**Validation Steps**:
1. Open `frontend/docs/chapters/chapter-3.mdx`
2. Count H2 sections (lines starting with `## `)
3. Verify count equals 7
4. Verify section titles match metadata `sections` list exactly

**Success Criteria**:
- Exactly 7 H2 sections found
- Section titles match metadata `sections` list exactly (in order)

### 5.3 Placeholder Validation

**Diagram Placeholder Validation**:
1. Search for `<!-- DIAGRAM: ` in MDX file
2. Count occurrences (should be 4)
3. Verify all diagram placeholders use kebab-case naming
4. Verify diagram names match metadata `diagram_placeholders` list exactly:
   - perception-overview
   - sensor-types
   - cv-depth-flow
   - feature-extraction-pipeline

**AI-Block Placeholder Validation**:
1. Search for `<!-- AI-BLOCK: ` in MDX file
2. Count occurrences (should be 4)
3. Verify all AI-block placeholders use HTML comment format
4. Verify AI-block types match metadata `ai_blocks` list exactly:
   - ask-question
   - explain-like-i-am-10
   - interactive-quiz
   - generate-diagram

**Chunk Marker Validation**:
1. Search for `<!-- CHUNK: START -->` in MDX file
2. Count occurrences (should be 7)
3. Search for `<!-- CHUNK: END -->` in MDX file
4. Count occurrences (should be 7)
5. Verify all chunk markers are properly paired (START with END)
6. Verify chunk markers align with H2 section boundaries

**Success Criteria**:
- Exactly 4 diagram placeholders found
- Exactly 4 AI-block placeholders found
- Exactly 7 chunk marker pairs found (7 START, 7 END)
- All placeholders match metadata lists exactly
- All chunk markers are properly paired

### 5.4 Metadata Import Test

**Command**: `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"`

**Validation Steps**:
1. Navigate to project root
2. Run Python import command
3. Verify import succeeds without errors
4. Verify `CHAPTER_METADATA` dictionary is accessible
5. Verify all required fields are present

**Success Criteria**:
- Import succeeds with exit code 0
- `CHAPTER_METADATA` dictionary is accessible
- All required fields are present (id, title, summary, section_count, sections, ai_blocks, diagram_placeholders, difficulty_level, prerequisites, learning_outcomes, glossary_terms, last_updated)

### 5.5 Glossary Validation

**Validation Steps**:
1. Open `frontend/docs/chapters/chapter-3.mdx`
2. Navigate to Glossary section (Section 7)
3. Verify glossary section exists
4. Verify glossary placeholder mentions exactly 7 terms:
   - Perception
   - Sensor
   - Computer Vision
   - Depth Perception
   - Signal Processing
   - Feature Extraction
   - LiDAR (or alternative term)

**Success Criteria**:
- Glossary section exists
- Glossary placeholder mentions exactly 7 terms
- Terms match metadata `glossary_terms` list (when implemented)

### 5.6 Diagram Naming Validation

**Validation Steps**:
1. Extract all diagram placeholder names from MDX file
2. Verify all names use kebab-case format
3. Verify names match metadata `diagram_placeholders` list exactly:
   - perception-overview
   - sensor-types
   - cv-depth-flow
   - feature-extraction-pipeline

**Success Criteria**:
- All diagram names use kebab-case format
- All diagram names match metadata `diagram_placeholders` list exactly

### 5.7 Chunk Marker Pairing Validation

**Validation Steps**:
1. Extract all chunk markers from MDX file
2. Count `<!-- CHUNK: START -->` occurrences (should be 7)
3. Count `<!-- CHUNK: END -->` occurrences (should be 7)
4. Verify each START marker has corresponding END marker
5. Verify chunk markers align with H2 section boundaries
6. Verify chunk markers are placed at logical semantic boundaries

**Success Criteria**:
- Exactly 7 chunk marker pairs found (7 START, 7 END)
- All chunk markers are properly paired
- Chunk markers align with H2 section boundaries
- Chunk markers are placed at logical semantic boundaries

### 5.8 Build Pipeline Steps (Future Features)

**Automated Checks** (to be implemented in future features):
1. **Pre-commit hook**: Run section count validation
2. **CI/CD pipeline**: Run frontend build test
3. **CI/CD pipeline**: Run metadata import test
4. **CI/CD pipeline**: Run placeholder validation
5. **CI/CD pipeline**: Run chunk marker pairing validation
6. **CI/CD pipeline**: Run cross-validation (MDX ↔ metadata)

**Validation Script** (future feature):
- Create `scripts/validate-chapter-3.sh` or `scripts/validate-chapter-3.py`
- Run all validation checks automatically
- Generate validation report
- Fail build if validation fails

---

## 6. Integration Points

### 6.1 Frontend Integration

**Docusaurus Integration**:
- Chapter 3 MDX file will be automatically discovered by Docusaurus
- Chapter 3 will appear in sidebar navigation (position 3)
- Chapter 3 will be accessible at `/docs/chapters/chapter-3`

**React Component Integration** (Future):
- AI-block HTML comment placeholders will be replaced with React components in future features
- Diagram placeholders will be replaced with generated diagrams in future features

### 6.2 Backend Integration

**RAG Pipeline Integration** (Feature 020):
- Chunk file (`chapter_3_chunks.py`) will provide chunks for RAG pipeline
- Chunks will be embedded using embedding model
- Chunks will be stored in Qdrant collection "chapter_3"
- Chunks will be retrieved for context assembly

**Metadata API Integration** (Future):
- Metadata file (`chapter_3.py`) will be used by API endpoints
- API endpoints will serve chapter metadata for frontend consumption
- Metadata will be used for chapter recommendation and progress tracking

### 6.3 Validation Integration

**Build Pipeline Integration** (Future):
- Validation checks will be integrated into CI/CD pipeline
- Validation failures will block deployment
- Validation reports will be generated automatically

---

## 7. Acceptance Checks

### 7.1 Structure Validation

- [ ] MDX file exists at `frontend/docs/chapters/chapter-3.mdx`
- [ ] MDX file has exactly 7 H2 sections
- [ ] MDX file has exactly 4 diagram placeholders (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
- [ ] MDX file has exactly 4 AI-block HTML comment placeholders (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
- [ ] MDX file has exactly 7 chunk marker pairs (CHUNK: START / CHUNK: END)
- [ ] MDX file has glossary section with 7 placeholder terms
- [ ] All diagram placeholders use kebab-case naming
- [ ] All AI-block placeholders use HTML comment format
- [ ] All chunk markers are properly paired

### 7.2 Metadata Validation

- [ ] Metadata file exists at `backend/app/content/chapters/chapter_3.py`
- [ ] Metadata file imports without errors
- [ ] Metadata has `id: 3`
- [ ] Metadata has `section_count: 7`
- [ ] Metadata `sections` list has exactly 7 items matching MDX H2 sections
- [ ] Metadata `ai_blocks` list has exactly 4 items
- [ ] Metadata `diagram_placeholders` list has exactly 4 items (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
- [ ] Metadata has `difficulty_level: "intermediate"`
- [ ] Metadata has `prerequisites: [1, 2]`
- [ ] Metadata `glossary_terms` list has exactly 7 items (placeholder)

### 7.3 Chunk File Validation

- [ ] Chunk file exists at `backend/app/content/chapters/chapter_3_chunks.py`
- [ ] Chunk file imports without errors
- [ ] Chunk file has `get_chapter_chunks(chapter_id: int = 3)` function
- [ ] Chunk function has correct signature and return type
- [ ] Chunk function docstring mentions chunk marker support

### 7.4 Cross-Validation

- [ ] MDX `title` matches metadata `title` exactly
- [ ] MDX H2 section count matches metadata `section_count` (7)
- [ ] MDX H2 section titles match metadata `sections` list exactly (in order)
- [ ] MDX diagram placeholders match metadata `diagram_placeholders` list exactly
- [ ] MDX AI-block placeholders match metadata `ai_blocks` list
- [ ] MDX glossary terms match metadata `glossary_terms` list (when implemented)

### 7.5 Build Validation

- [ ] Frontend build test passes (`npm run build` in `frontend/` directory)
- [ ] No build errors or warnings related to Chapter 3 MDX file
- [ ] Chapter 3 page is generated in build output

### 7.6 Chunk Marker Validation

- [ ] Exactly 7 chunk marker pairs found (7 START, 7 END)
- [ ] All chunk markers are properly paired
- [ ] Chunk markers align with H2 section boundaries
- [ ] Chunk markers are placed at logical semantic boundaries

---

## 8. Implementation Notes

### 8.1 Differences from Feature 017

**Diagram Names**:
- Feature 017: physical-ai-sensing-overview, sensor-categories-diagram, depth-perception-flow, signal-processing-pipeline
- Feature 018: perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline

**AI-Block Format**:
- Feature 017: React components (`<AskQuestionBlock chapterId={3} />`)
- Feature 018: HTML comments (`<!-- AI-BLOCK: ask-question -->`)

**Chunk Markers**:
- Feature 017: Not required
- Feature 018: Required (`<!-- CHUNK: START -->` / `<!-- CHUNK: END -->`)

### 8.2 Chunk Marker Strategy

**Placement**:
- Each H2 section has one chunk marker pair
- Chunk markers align with concept boundaries
- Chunk markers respect H2 section boundaries
- Chunk markers are placed at logical semantic boundaries

**Future Implementation**:
- Chunking function will respect chunk marker boundaries
- Chunk metadata will include `chunk_markers: bool` flag
- RAG pipeline will use chunk markers for semantic segmentation

### 8.3 Content Writing Guidelines

**Reading Level**: Grade 7-8
**Sentence Length**: 15-20 words per sentence
**Paragraph Length**: 3-4 sentences per paragraph
**Tone**: Conversational-educational
**Approach**: Use analogies and simplified examples
**Examples**: Real-world Physical AI applications (autonomous vehicles, robotics, drones)

---

## 9. Success Criteria

1. ✅ MDX file created with exactly 7 H2 sections
2. ✅ MDX file has exactly 4 diagram placeholders (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
3. ✅ MDX file has exactly 4 AI-block HTML comment placeholders (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
4. ✅ MDX file has exactly 7 chunk marker pairs (CHUNK: START / CHUNK: END)
5. ✅ Metadata file created with all required fields
6. ✅ Chunk file created with placeholder function
7. ✅ All validation checks pass
8. ✅ Frontend build test passes
9. ✅ Metadata import test passes
10. ✅ Chunk marker pairing validation passes

---

## 10. Next Steps

After completing this plan:

1. **Task Generation**: Run `/sp.tasks` to create implementation tasks
2. **Implementation**: Run `/sp.implement` to create actual structure files with chunk markers
3. **Content Writing**: Write actual content (future feature)
4. **Validation**: Validate content quality and structure (future feature)
5. **RAG Integration**: Implement chunking and embedding (Feature 020)
