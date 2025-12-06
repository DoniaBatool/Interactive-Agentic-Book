# Content Schema: Chapter 3 Written Content

**Feature**: 017-chapter-3-content
**Date**: 2025-12-05
**Purpose**: Define data contracts and validation schemas for Chapter 3 content structure

## MDX Frontmatter Schema

**Format**: YAML
**Location**: Top of `frontend/docs/chapters/chapter-3.mdx`

```yaml
# Required fields
title: string              # Pattern: "Chapter 3 — Title"
                          # Example: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
                          # Constraints: 10-100 characters

description: string        # SEO-optimized summary
                          # Constraints: 10-250 characters
                          # Purpose: Meta tags, search results, page summaries

sidebar_position: integer  # Navigation order
                          # Example: 3
                          # Constraints: Positive integer, must be unique in docs/chapters/

sidebar_label: string      # Abbreviated title for sidebar
                          # Example: "Chapter 3: Physical AI Perception Systems"
                          # Constraints: 10-50 characters

# Optional fields
tags: string[]            # Categorization tags
                          # Example: ["physical-ai", "sensors", "perception", "signal-processing"]
                          # Constraints: Lowercase, kebab-case, 1-20 characters per tag
```

**Validation Rules**:
- Title MUST start with "Chapter 3 — " followed by title
- sidebar_position MUST be 3 (matches chapter number)
- All fields MUST be valid YAML (no unescaped special characters)
- Frontmatter MUST be enclosed by `---` delimiters at start and end

---

## Chapter Metadata Schema (Python)

**Format**: Python dictionary
**Location**: `backend/app/content/chapters/chapter_3.py`

```python
from typing import List

CHAPTER_METADATA = {
    # Core identification (REQUIRED)
    "id": int,                    # Chapter number (3)
    "title": str,                 # Must match MDX frontmatter title exactly
    "summary": str,               # 2-3 sentence description (50-300 characters)

    # Structure information (REQUIRED)
    "section_count": int,         # Number of H2 sections (7 for Chapter 3)
    "sections": List[str],        # Section titles in order

    # Placeholder tracking (REQUIRED)
    "ai_blocks": List[str],       # AI-block types present
                                  # Allowed values: ["ask-question", "explain-like-i-am-10",
                                  #                  "interactive-quiz", "generate-diagram"]
    "diagram_placeholders": List[str],  # Diagram placeholder names

    # Versioning (REQUIRED)
    "last_updated": str,          # ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SSZ)

    # RAG-specific metadata (REQUIRED)
    "difficulty_level": str,      # Enum: "beginner" | "intermediate" | "advanced"
                                  # Value: "intermediate" for Chapter 3
    "prerequisites": List[int],   # Chapter IDs ([1, 2] for Chapter 3 - Chapters 1 and 2 are prerequisites)
    "learning_outcomes": List[str],  # Measurable learning objectives (3-8 items)
    "glossary_terms": List[str],  # Terms defined in glossary (7 items for Chapter 3)
}
```

**Field Specifications**:

### Core Identification
- `id`: MUST be 3 (integer)
- `title`: MUST match MDX frontmatter `title` exactly
- `summary`: 2-3 sentence overview (50-300 characters)

### Structure Information
- `section_count`: MUST be 7 (integer)
- `sections`: MUST be list of exactly 7 strings matching MDX H2 section titles in order:
  1. "What Is Perception in Physical AI?"
  2. "Types of Sensors in Robotics"
  3. "Computer Vision & Depth Perception"
  4. "Signal Processing Basics for AI"
  5. "Feature Extraction & Interpretation"
  6. "Learning Objectives"
  7. "Glossary"

### Placeholder Tracking
- `ai_blocks`: MUST be list of exactly 4 strings:
  - "ask-question"
  - "explain-like-i-am-10"
  - "interactive-quiz"
  - "generate-diagram"
- `diagram_placeholders`: MUST be list of exactly 4 strings (kebab-case):
  - "physical-ai-sensing-overview"
  - "sensor-categories-diagram"
  - "depth-perception-flow"
  - "signal-processing-pipeline"

### Versioning
- `last_updated`: ISO 8601 timestamp string (e.g., "2025-12-05T00:00:00Z")

### RAG-Specific Metadata
- `difficulty_level`: MUST be "intermediate" (string)
- `prerequisites`: MUST be [1, 2] (list of integers)
- `learning_outcomes`: List of 3-8 strings (measurable learning objectives)
- `glossary_terms`: List of exactly 7 strings matching MDX glossary terms

**Validation Rules**:
- All required fields MUST be present
- `section_count` MUST match length of `sections` list
- `sections` list MUST match MDX H2 section titles exactly
- `ai_blocks` count MUST match MDX AI-block components (4)
- `diagram_placeholders` count MUST match MDX diagram placeholders (4)
- `glossary_terms` count MUST match MDX glossary terms (7)
- `difficulty_level` MUST be "intermediate"
- `prerequisites` MUST be [1, 2]

---

## Glossary Schema

**Format**: Markdown list in MDX file
**Location**: `frontend/docs/chapters/chapter-3.mdx` under `## Glossary` section

**Structure**:
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
- Each term MUST have definition (10-100 words)
- Definitions MUST use analogies when possible
- Terms MUST match `glossary_terms` in metadata

---

## AI-Block Placeholder Schema

**Format**: React component in MDX file
**Location**: `frontend/docs/chapters/chapter-3.mdx` within sections

**Component Types**:
1. **Ask Question**: `<AskQuestionBlock chapterId={3} sectionId="..." />`
2. **Explain Like I'm 10**: `<ExplainLike10Block concept="..." chapterId={3} />`
3. **Interactive Quiz**: `<InteractiveQuizBlock chapterId={3} numQuestions={5} />`
4. **Generate Diagram**: `<GenerateDiagramBlock diagramType="..." chapterId={3} />`

**Validation Rules**:
- MUST have exactly 4 AI-block components
- All components MUST have `chapterId={3}`
- Component types MUST match metadata `ai_blocks` list
- Components MUST be placed within appropriate sections

---

## Diagram Placeholder Schema

**Format**: HTML comment in MDX file
**Location**: `frontend/docs/chapters/chapter-3.mdx` within sections

**Placeholder Format**:
```html
<!-- DIAGRAM: physical-ai-sensing-overview -->
<!-- DIAGRAM: sensor-categories-diagram -->
<!-- DIAGRAM: depth-perception-flow -->
<!-- DIAGRAM: signal-processing-pipeline -->
```

**Validation Rules**:
- MUST have exactly 4 diagram placeholders
- All placeholders MUST use kebab-case naming
- Placeholder names MUST match metadata `diagram_placeholders` list exactly
- Placeholders MUST be placed within appropriate sections

---

## Section Structure Schema

**Format**: Markdown H2 headings in MDX file
**Location**: `frontend/docs/chapters/chapter-3.mdx`

**Required Sections** (exactly 7):
1. `## What Is Perception in Physical AI? {#what-is-perception-in-physical-ai}`
2. `## Types of Sensors in Robotics {#types-of-sensors-in-robotics}`
3. `## Computer Vision & Depth Perception {#computer-vision-depth-perception}`
4. `## Signal Processing Basics for AI {#signal-processing-basics-for-ai}`
5. `## Feature Extraction & Interpretation {#feature-extraction-interpretation}`
6. `## Learning Objectives {#learning-objectives}`
7. `## Glossary {#glossary}`

**Validation Rules**:
- MUST have exactly 7 H2 sections
- Section titles MUST match metadata `sections` list exactly
- Section IDs (anchor links) MUST be kebab-case
- Section order MUST match metadata `sections` list order

---

## RAG Chunk File Schema

**Format**: Python function
**Location**: `backend/app/content/chapters/chapter_3_chunks.py`

**Function Signature**:
```python
from typing import List, Dict, Any

def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 3 with metadata.
    
    Args:
        chapter_id: Chapter identifier (default: 3 for Chapter 3)
    
    Returns:
        List of chunk dictionaries with structure:
        [
            {
                "id": str,                    # Unique chunk ID (e.g., "ch3-s1-c0")
                "text": str,                  # Chunk text content
                "chapter_id": 3,              # Chapter identifier
                "section_id": str,            # Section identifier
                "position": int,              # Position in chapter (0-based)
                "word_count": int,            # Word count
                "metadata": {                 # Additional metadata
                    "heading": str,          # Section heading
                    "type": str,             # "paragraph", "heading", "glossary", etc.
                    "has_diagram": bool,     # True if section has diagram placeholder
                    "has_ai_block": bool     # True if section has AI block
                }
            },
            ...
        ]
    """
    # Placeholder return - no real chunking implementation
    return []
```

**Validation Rules**:
- Function MUST exist with correct signature
- Function MUST return `List[Dict[str, Any]]`
- Function MUST have `chapter_id: int = 3` parameter
- Function MUST be importable without errors

---

## Writing Style Constraints Schema

**Format**: Documentation in research.md
**Location**: `specs/017-chapter-3-content/research.md`

**Constraints**:
- **Reading Level**: 7th-8th grade
- **Sentence Length**: 15-20 words per sentence
- **Paragraph Length**: 3-4 sentences per paragraph
- **Vocabulary**: Define all technical terms clearly on first use
- **Tone**: Conversational-educational
- **Approach**: Use analogies and simplified examples
- **Examples**: Real-world Physical AI applications (autonomous vehicles, robotics, drones)
- **Technical Terms**: Define clearly with analogies when possible

**Validation Rules**:
- Content MUST be accessible to 7th-8th grade reading level
- Technical terms MUST be defined on first use
- Analogies MUST be used for complex concepts
- Examples MUST be real-world Physical AI applications

---

## Cross-Validation Rules

**MDX ↔ Metadata Validation**:
- MDX `title` MUST match metadata `title` exactly
- MDX H2 section count MUST match metadata `section_count`
- MDX H2 section titles MUST match metadata `sections` list exactly
- MDX diagram placeholders MUST match metadata `diagram_placeholders` list exactly
- MDX AI-block components MUST match metadata `ai_blocks` list
- MDX glossary terms MUST match metadata `glossary_terms` list exactly

**Metadata Internal Validation**:
- `section_count` MUST equal length of `sections` list
- `ai_blocks` count MUST be 4
- `diagram_placeholders` count MUST be 4
- `glossary_terms` count MUST be 7
- `difficulty_level` MUST be "intermediate"
- `prerequisites` MUST be [1, 2]

---

## Contract Checklist

- [ ] MDX frontmatter schema defined
- [ ] Chapter metadata schema (Python) defined
- [ ] Glossary schema defined
- [ ] AI-block placeholder schema defined
- [ ] Diagram placeholder schema defined
- [ ] Section structure schema defined
- [ ] RAG chunk file schema defined
- [ ] Writing style constraints schema defined
- [ ] Cross-validation rules defined
