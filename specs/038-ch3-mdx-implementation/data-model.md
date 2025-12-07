# Data Model: Chapter 3 MDX + Metadata Implementation

**Feature**: 038-ch3-mdx-implementation
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 3 MDX and metadata implementation

## Entity Definitions

### 1. MDX File Structure (Primary Entity)

**Description**: Represents the MDX file structure for Chapter 3 with frontmatter, sections, placeholders, and chunk boundaries

**Storage**: MDX file at `frontend/docs/chapters/chapter-3.mdx`

**Structure**:
```yaml
# Frontmatter (YAML metadata)
---
title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
description: "Learn how Physical AI systems perceive the world..."
sidebar_position: 3
sidebar_label: "Chapter 3: Physical AI Perception Systems"
tags: ["physical-ai", "sensors", "perception", "signal-processing"]
---

# Body Content (Markdown + HTML comments)
<!-- CHUNK: start -->
## Section 1: What Is Perception in Physical AI?
<!-- Content placeholder -->
<!-- DIAGRAM: perception-overview -->
<!-- AI-BLOCK: ask-question -->
<!-- CHUNK: end -->

<!-- CHUNK: start -->
## Section 2: Types of Sensors in Robotics
<!-- Content placeholder -->
<!-- DIAGRAM: sensor-types -->
<!-- AI-BLOCK: generate-diagram -->
<!-- CHUNK: end -->

[... Sections 3-7 ...]
```

**Validation Rules**:
- Title MUST match Feature 037 specification exactly
- MUST contain exactly 7 H2 sections
- MUST contain exactly 4 diagram placeholders
- MUST contain exactly 4 AI-block placeholders
- Each section MUST be wrapped in chunk boundaries

---

### 2. Python Metadata Dictionary (Primary Entity)

**Description**: Represents structured metadata for Chapter 3 stored in Python dictionary format

**Storage**: Python file at `backend/app/content/chapters/chapter_3.py`

**Structure**:
```python
CHAPTER_METADATA = {
    "id": 3,
    "title": "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)",
    "summary": "TODO: 2-3 sentence overview",
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
    "ai_blocks": [
        "ask-question",
        "generate-diagram",
        "explain-like-i-am-10",
        "interactive-quiz"
    ],
    "diagram_placeholders": [
        "perception-overview",
        "sensor-types",
        "cv-depth-flow",
        "feature-extraction-pipeline"
    ],
    "last_updated": "2025-01-27T00:00:00Z",
    "difficulty_level": "intermediate",
    "prerequisites": [1, 2],
    "learning_outcomes": ["TODO: 3-8 learning outcomes"],
    "glossary_terms": ["TODO: 6-10 glossary terms"]
}

def get_chapter_3_chunks() -> List[Dict[str, Any]]:
    """TODO: Implement chunking from Chapter 3 MDX content."""
    return []
```

**Validation Rules**:
- All fields MUST match Feature 037 specification
- Title MUST match MDX frontmatter exactly
- Section count MUST match number of H2 sections in MDX
- Placeholder lists MUST match placeholders in MDX

---

### 3. Section (Sub-entity)

**Description**: A single H2 section within the MDX file

**Structure**:
```markdown
<!-- CHUNK: start -->
## Section Title
<!-- Content placeholder -->
<!-- DIAGRAM: placeholder-name --> (optional)
<!-- AI-BLOCK: block-type --> (optional)
<!-- CHUNK: end -->
```

**Attributes**:
- Heading: H2 markdown heading
- Order: Position within chapter (1-7)
- Content: Placeholder comment (no actual content)
- Placeholders: 0-2 placeholders (diagram and/or AI-block)
- Chunk boundaries: Wrapped in start/end comments

---

### 4. Placeholder (Sub-entity)

**Description**: A marker for future diagram or AI-block integration

**Types**:
- Diagram placeholder: `<!-- DIAGRAM: placeholder-name -->`
- AI-block placeholder: `<!-- AI-BLOCK: block-type -->`

**Attributes**:
- Type: "diagram" or "ai-block"
- Name: Kebab-case identifier
- Section: Parent section number
- Position: "middle" or "end"

---

## Relationships

- MDX File Structure → Sections (1:N)
- MDX File Structure → Python Metadata Dictionary (1:1, manually synced)
- Section → Placeholders (1:N)
- Python Metadata Dictionary → get_chapter_3_chunks() function (1:1)

---

## Data Integrity Constraints

1. **Metadata Synchronization**:
   - Metadata `title` MUST match MDX frontmatter `title` exactly
   - Metadata `section_count` MUST match number of H2 sections in MDX
   - Metadata `sections[]` MUST match H2 headings in order

2. **Placeholder Completeness**:
   - Number of `<!-- DIAGRAM: -->` in MDX MUST equal length of `diagram_placeholders[]` in metadata
   - Number of `<!-- AI-BLOCK: -->` in MDX MUST equal length of `ai_blocks[]` in metadata
   - Placeholder names in metadata MUST match placeholder values in MDX

3. **Chunk Boundary Completeness**:
   - Each section MUST have exactly one `<!-- CHUNK: start -->` and one `<!-- CHUNK: end -->`
   - Chunk boundaries MUST wrap entire section content

---

## Summary

All structures are implementation scaffolding. No actual content is written—only structure, placeholders, and metadata stubs are implemented.

