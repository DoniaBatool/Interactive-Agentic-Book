# Data Model: Chapter 2 Written Content

**Feature**: 032-chapter-2-content
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for chapter content system

## Entity Definitions

### 1. Chapter Content (Primary Entity)

**Description**: Represents the complete written educational material for a single chapter

**Storage**: MDX file at `frontend/docs/chapters/chapter-2.mdx`

**Structure**:
```yaml
# Frontmatter (YAML metadata)
---
title: string              # Full chapter title
description: string        # SEO-optimized summary (150-160 chars)
sidebar_position: integer  # Navigation order (2 for Chapter 2)
sidebar_label: string      # Abbreviated title for sidebar
tags: string[]            # Categorization tags
---

# Body Content (Markdown + JSX)
<!-- CHUNK: start -->
## Section 1: Sensors and Perception Systems
[Content paragraphs]
<!-- DIAGRAM: sensor-types-overview -->
<!-- AI-BLOCK: ask-question -->
<!-- CHUNK: end -->

<!-- CHUNK: start -->
## Section 2: Actuators and Mechanical Systems
[Content paragraphs]
<!-- DIAGRAM: actuator-types-overview -->
<!-- CHUNK: end -->

<!-- CHUNK: start -->
## Section 3: Control Systems & Feedback Loops
[Content paragraphs]
<!-- DIAGRAM: feedback-loop-diagram -->
<!-- AI-BLOCK: explain-like-i-am-10 -->
<!-- CHUNK: end -->

<!-- CHUNK: start -->
## Section 4: Robot Kinematics & Motion
[Content paragraphs]
<!-- DIAGRAM: robot-kinematics-flow -->
<!-- AI-BLOCK: generate-diagram -->
<!-- CHUNK: end -->

<!-- CHUNK: start -->
## Section 5: Combining Hardware + Software
[Content paragraphs]
<!-- AI-BLOCK: interactive-quiz -->
<!-- CHUNK: end -->

<!-- CHUNK: start -->
## Section 6: Applications & Case Studies
[Content paragraphs]
<!-- CHUNK: end -->

<!-- CHUNK: start -->
## Section 7: Glossary
[Term definitions]
<!-- CHUNK: end -->
```

**Validation Rules**:
- Title MUST start with "Chapter 2 — " format
- Description MUST be 10-250 characters
- sidebar_position MUST be 2
- MUST contain exactly 7 H2 sections in specified order
- MUST contain exactly 4 `<!-- DIAGRAM: -->` placeholders
- MUST contain exactly 4 `<!-- AI-BLOCK: -->` placeholders
- MUST contain chunk boundaries around each section
- Reading level MUST be 7th-8th grade (Flesch-Kincaid)

**State**: Static (no state transitions - content is published or not)

---

### 2. Section (Sub-entity of Chapter Content)

**Description**: A major division within a chapter focusing on a specific topic

**Structure**:
```markdown
<!-- CHUNK: start -->
## Section Title

[Introductory paragraph with topic sentence]

[Explanation paragraphs (3-4 sentences each)]

[Examples or applications]

[Optional diagram placeholder]
[Optional AI-block placeholder]
<!-- CHUNK: end -->
```

**Attributes**:
- **Heading**: H2 markdown heading (`## Section Title`)
- **Order**: Position within chapter (1-7)
- **Content**: Body paragraphs in markdown
- **Placeholders**: 0-2 diagram or AI-block placeholders
- **Chunk Boundaries**: Wrapped in `<!-- CHUNK: start -->` and `<!-- CHUNK: end -->`

**Relationships**:
- **Parent**: Chapter Content (1:N - one chapter has many sections)
- **Order**: Sequential within parent

**Validation Rules**:
- Section heading MUST be H2 level (not H1 or H3)
- Content MUST be at least 2 paragraphs (minimum 200 words)
- MUST be wrapped in chunk boundaries
- Paragraphs MUST be max 4 sentences each
- Sentences MUST be 15-20 words average

---

### 3. Glossary Term (Sub-entity of Chapter Content)

**Description**: A key vocabulary word with beginner-friendly definition

**Storage**: Section 7 (Glossary) of MDX file

**Structure**:
```markdown
**Term Name**: Definition text explaining the concept in accessible language (10-100 words).
```

**Attributes**:
- **Term**: Bold formatted text (`**Term Name**`)
- **Definition**: Plain text after colon (10-100 words)
- **Format**: `**Term**: definition`

**Required Terms for Chapter 2**:
1. Sensor
2. Actuator
3. Feedback Loop
4. PID Control
5. Kinematics
6. Degrees of Freedom (DOF)
7. Perception

**Validation Rules**:
- Term MUST be bold formatted
- Definition MUST be 10-100 words
- Definition MUST use accessible language (12+ age group)
- Definition MUST include analogies or examples
- Definition MUST avoid circular definitions

---

### 4. Diagram Placeholder (Sub-entity of Chapter Content)

**Description**: A marker indicating where a visual diagram should be rendered

**Storage**: HTML comment in MDX file

**Structure**:
```html
<!-- DIAGRAM: placeholder-name -->
```

**Required Placeholders for Chapter 2**:
1. `sensor-types-overview` (Section 1)
2. `actuator-types-overview` (Section 2)
3. `feedback-loop-diagram` (Section 3)
4. `robot-kinematics-flow` (Section 4)

**Attributes**:
- **Format**: HTML comment
- **Naming**: Kebab-case (lowercase, hyphens only)
- **Position**: Within relevant section

**Validation Rules**:
- MUST use exact format: `<!-- DIAGRAM: name -->`
- Name MUST be kebab-case
- MUST be positioned logically within section

---

### 5. AI-Interactive Block Placeholder (Sub-entity of Chapter Content)

**Description**: A marker indicating where interactive AI features will be integrated

**Storage**: HTML comment in MDX file

**Structure**:
```html
<!-- AI-BLOCK: block-type -->
```

**Required Placeholders for Chapter 2**:
1. `ask-question` (end of Section 1)
2. `explain-like-i-am-10` (during Section 3)
3. `generate-diagram` (inside Section 4)
4. `interactive-quiz` (after Section 5)

**Attributes**:
- **Format**: HTML comment
- **Type**: One of 4 allowed values
- **Position**: At specified locations

**Validation Rules**:
- MUST use exact format: `<!-- AI-BLOCK: type -->`
- Type MUST be one of: `ask-question`, `explain-like-i-am-10`, `interactive-quiz`, `generate-diagram`
- MUST be positioned at specified locations

---

### 6. Chapter Metadata (Backend Entity)

**Description**: Structured information about a chapter used by backend systems

**Storage**: Python file at `backend/app/content/chapters/chapter_2.py`

**Structure**:
```python
from typing import List

CHAPTER_METADATA = {
    "id": 2,
    "title": "Chapter 2 — Foundations of Robotics Systems",
    "summary": "2-3 sentence description",
    "section_count": 7,
    "sections": [
        "Sensors and Perception Systems",
        "Actuators and Mechanical Systems",
        "Control Systems & Feedback Loops",
        "Robot Kinematics & Motion",
        "Combining Hardware + Software",
        "Applications & Case Studies",
        "Glossary"
    ],
    "ai_blocks": [
        "ask-question",
        "explain-like-i-am-10",
        "generate-diagram",
        "interactive-quiz"
    ],
    "diagram_placeholders": [
        "sensor-types-overview",
        "actuator-types-overview",
        "feedback-loop-diagram",
        "robot-kinematics-flow"
    ],
    "last_updated": "2025-01-27T00:00:00Z",
    "difficulty_level": "beginner",
    "prerequisites": [1],
    "learning_outcomes": [
        "Define sensors and explain how they enable robot perception",
        "Identify different types of actuators and their applications",
        "Explain feedback loops and PID control in robotics",
        "Describe robot kinematics and degrees of freedom",
        "Understand how hardware and software integrate in robotic systems"
    ],
    "glossary_terms": [
        "Sensor",
        "Actuator",
        "Feedback Loop",
        "PID Control",
        "Kinematics",
        "Degrees of Freedom (DOF)",
        "Perception"
    ]
}
```

**Attributes**:
- **id**: Chapter number (2)
- **title**: Full chapter title
- **summary**: 2-3 sentence description
- **section_count**: Number of sections (7)
- **sections**: List of section titles
- **ai_blocks**: List of AI-block types in order
- **diagram_placeholders**: List of diagram placeholder names
- **last_updated**: ISO 8601 timestamp
- **difficulty_level**: "beginner", "intermediate", or "advanced"
- **prerequisites**: List of chapter IDs ([1])
- **learning_outcomes**: List of learning objectives (3-10 items)
- **glossary_terms**: List of glossary terms (7 items)

**Validation Rules**:
- All fields MUST be present
- `id` MUST be 2
- `section_count` MUST match number of sections
- `sections` MUST match MDX file exactly
- `ai_blocks` MUST match MDX placeholders in order
- `diagram_placeholders` MUST match MDX placeholders
- `prerequisites` MUST be [1]

---

## Relationships

### Chapter Content → Sections
- **Type**: 1:N (one chapter has many sections)
- **Cardinality**: Exactly 7 sections
- **Order**: Sequential (1-7)

### Chapter Content → Glossary Terms
- **Type**: 1:N (one chapter has many glossary terms)
- **Cardinality**: Exactly 7 terms
- **Storage**: All terms in Section 7

### Chapter Content → Diagram Placeholders
- **Type**: 1:N (one chapter has many diagram placeholders)
- **Cardinality**: Exactly 4 placeholders
- **Distribution**: One per section (Sections 1-4)

### Chapter Content → AI-Block Placeholders
- **Type**: 1:N (one chapter has many AI-block placeholders)
- **Cardinality**: Exactly 4 placeholders
- **Distribution**: Sections 1, 3, 4, 5

### Chapter Content → Chunk Boundaries
- **Type**: 1:N (one chapter has many chunks)
- **Cardinality**: Exactly 7 chunks (one per section)
- **Format**: `<!-- CHUNK: start -->` and `<!-- CHUNK: end -->`

---

## Data Flow

### Content Creation Flow

1. **Specification** → Defines structure, sections, placeholders
2. **Content Writing** → Author creates MDX file with content
3. **Metadata Creation** → Backend metadata file created
4. **Validation** → Build test, readability check, structure verification
5. **Publication** → MDX file rendered in Docusaurus

### RAG Processing Flow (Future)

1. **Chunk Extraction** → Parse chunk boundaries from MDX
2. **Section Segmentation** → Each section becomes a chunk
3. **Embedding Generation** → Generate embeddings for each chunk
4. **Storage** → Store chunks in vector database
5. **Retrieval** → Query chunks for semantic search

---

## Validation Rules Summary

### File Existence
- `frontend/docs/chapters/chapter-2.mdx` MUST exist
- `backend/app/content/chapters/chapter_2.py` MUST exist

### Structure Validation
- Exactly 7 H2 sections in correct order
- Exactly 4 diagram placeholders with correct names
- Exactly 4 AI-block placeholders with correct types
- Exactly 7 glossary terms with proper formatting
- All sections wrapped in chunk boundaries

### Content Validation
- Reading level: 7th-8th grade (Flesch-Kincaid)
- Sentences: 15-20 words average
- Paragraphs: Max 4 sentences each
- Tone: Conversational-educational

### Metadata Validation
- All required fields present
- Field values match MDX content
- Types match schema definitions

---

## Notes

- All structures follow Chapter 1 pattern for consistency
- Chunk boundaries enable section-by-section RAG processing
- Metadata structure matches Chapter 1 for consistency
- Content style matches Chapter 1 for learner experience continuity

