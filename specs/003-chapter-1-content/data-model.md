# Data Model: Chapter 1 Written Content

**Feature**: 003-chapter-1-content
**Date**: 2025-12-05
**Purpose**: Define data structures and entities for chapter content system

## Entity Definitions

### 1. Chapter Content (Primary Entity)

**Description**: Represents the complete written educational material for a single chapter

**Storage**: MDX file at `frontend/docs/chapters/chapter-1.mdx`

**Structure**:
```yaml
# Frontmatter (YAML metadata)
---
title: string              # Full chapter title
description: string        # SEO-optimized summary (150-160 chars)
sidebar_position: integer  # Navigation order (1 for Chapter 1)
sidebar_label: string      # Abbreviated title for sidebar
tags: string[]            # Categorization tags
---

# Body Content (Markdown + JSX)
## Section 1: What is Physical AI?
[Content paragraphs]
<!-- DIAGRAM: physical-ai-overview -->
<!-- AI-BLOCK: ask-question -->

## Section 2: What is a Robot?
[Content paragraphs]
<!-- DIAGRAM: robot-anatomy -->
<!-- AI-BLOCK: generate-diagram -->

## Section 3: AI + Robotics = Physical AI Systems
[Content paragraphs]
<!-- DIAGRAM: ai-robotics-stack -->
<!-- AI-BLOCK: explain-like-i-am-10 -->

## Section 4: Core Concepts Introduced in This Book
[Content paragraphs]
<!-- DIAGRAM: core-concepts-flow -->
<!-- AI-BLOCK: interactive-quiz -->

## Section 5: Learning Objectives
[Bullet points]

## Section 6: Summary
[6-8 line recap]

## Section 7: Glossary
[Term definitions]
```

**Validation Rules**:
- Title MUST start with "Chapter N — " format
- Description MUST be 10-250 characters
- sidebar_position MUST be positive integer
- MUST contain exactly 7 H2 sections in specified order
- MUST contain exactly 4 `<!-- DIAGRAM: -->` placeholders
- MUST contain exactly 4 `<!-- AI-BLOCK: -->` placeholders
- Reading level MUST be 7th-8th grade (Flesch-Kincaid)

**State**: Static (no state transitions - content is published or not)

---

### 2. Section (Sub-entity of Chapter Content)

**Description**: A major division within a chapter focusing on a specific topic

**Structure**:
```markdown
## Section Title

[Introductory paragraph with topic sentence]

[Explanation paragraphs (3-4 sentences each)]

[Examples or applications]

[Optional diagram placeholder]
[Optional AI-block placeholder]
```

**Attributes**:
- **Heading**: H2 markdown heading (`## Section Title`)
- **Order**: Position within chapter (1-7)
- **Content**: Body paragraphs in markdown
- **Placeholders**: 0-2 diagram or AI-block placeholders

**Relationships**:
- **Parent**: Chapter Content (1:N - one chapter has many sections)
- **Order**: Sequential within parent

**Validation Rules**:
- Section heading MUST be H2 level (not H1 or H3)
- Content MUST be at least 2 paragraphs (minimum 200 words)
- Paragraphs MUST be 3-4 sentences maximum
- Sentences MUST average 15-20 words

---

### 3. Glossary Term (Sub-entity of Chapter Content)

**Description**: A key vocabulary word with beginner-friendly definition

**Structure**:
```markdown
**Term Name**: Definition text explaining the concept in accessible language.
```

**Attributes**:
- **Term**: Technical vocabulary (e.g., "Physical AI", "Sensor")
- **Definition**: 1-3 sentence explanation suitable for 12+ age group
- **Context**: Optional usage example or analogy

**Required Terms (Chapter 1)**:
1. Physical AI
2. Robot
3. Sensor
4. Actuator
5. Autonomy
6. Perception
7. Control System

**Relationships**:
- **Parent**: Chapter Content (1:N - one chapter has many terms)
- **Section**: Cross-references sections where term is introduced

**Validation Rules**:
- Term MUST be bold formatted (`**Term:**`)
- Definition MUST follow immediately after colon
- Definition MUST be 10-100 words
- Language MUST avoid circular definitions (defining term with itself)
- MUST use analogies or concrete examples for abstract concepts

---

### 4. Diagram Placeholder (Sub-entity of Chapter Content)

**Description**: A marker indicating where a visual diagram should be rendered (future feature)

**Structure**:
```html
<!-- DIAGRAM: placeholder-name -->
```

**Attributes**:
- **Name**: Kebab-case identifier (e.g., "physical-ai-overview")
- **Type**: Inferred from name (overview, anatomy, stack, flow)
- **Section**: Parent section where placeholder appears
- **Position**: Line number or relative position in section

**Required Placeholders (Chapter 1)**:
1. `physical-ai-overview` (Section 1)
2. `robot-anatomy` (Section 2)
3. `ai-robotics-stack` (Section 3)
4. `core-concepts-flow` (Section 4)

**Relationships**:
- **Parent**: Section (N:1 - each placeholder belongs to one section)
- **Future**: Will link to generated diagram assets (images or SVG)

**Validation Rules**:
- Format MUST be `<!-- DIAGRAM: {name} -->`
- Name MUST be lowercase with hyphens only (kebab-case)
- Name MUST be unique within chapter
- MUST appear logically within section content (not at start/end of file)

---

### 5. AI-Interactive Block Placeholder (Sub-entity of Chapter Content)

**Description**: A marker indicating where interactive AI features will be integrated (future feature)

**Structure**:
```html
<!-- AI-BLOCK: block-type -->
```

**Attributes**:
- **Type**: One of 4 allowed types (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
- **Section**: Parent section where block appears
- **Position**: Strategic placement following pedagogical principles

**Required Block Types (Chapter 1)**:
1. `ask-question` - Encourages active recall
2. `explain-like-i-am-10` - Simplified alternative explanation
3. `interactive-quiz` - Self-assessment
4. `generate-diagram` - On-demand visual generation

**Relationships**:
- **Parent**: Section (N:1 - each block belongs to one section)
- **Future**: Will link to React components implementing interactivity

**Validation Rules**:
- Format MUST be `<!-- AI-BLOCK: {type} -->`
- Type MUST be one of 4 allowed values (kebab-case)
- Type MUST be unique within chapter (no duplicates)
- Positioning MUST follow research guidelines (see research.md)

---

### 6. Chapter Metadata (Backend Entity)

**Description**: Structured information about a chapter used by backend systems for RAG, analytics, and personalization

**Storage**: Python module at `backend/app/content/chapters/chapter_1.py`

**Structure**:
```python
from typing import List

CHAPTER_METADATA = {
    # Core identification
    "id": int,                    # Unique chapter number
    "title": str,                 # Full chapter title
    "summary": str,               # 2-3 sentence description

    # Structure information
    "section_count": int,         # Number of H2 sections (7 for Ch 1)
    "sections": List[str],        # Section titles in order

    # Placeholder tracking
    "ai_blocks": List[str],       # AI-block types present
    "diagram_placeholders": List[str],  # Diagram names present

    # Versioning
    "last_updated": str,          # ISO 8601 timestamp

    # RAG-specific metadata (future use)
    "difficulty_level": str,      # beginner | intermediate | advanced
    "prerequisites": List[int],   # Chapter IDs of prerequisites
    "learning_outcomes": List[str],  # Measurable learning objectives
    "glossary_terms": List[str],  # Terms defined in glossary
}
```

**Validation Rules**:
- `id` MUST be positive integer matching chapter number
- `title` MUST match MDX frontmatter title exactly
- `section_count` MUST match actual number of H2 sections
- `sections` list MUST match H2 headings in order
- `ai_blocks` MUST contain exactly 4 items matching placeholder types
- `diagram_placeholders` MUST contain exactly 4 items matching placeholder names
- `last_updated` MUST be valid ISO 8601 format

**Relationships**:
- **Source**: Derived from Chapter Content (MDX file)
- **Consumers**: RAG pipeline (future), analytics (future), API endpoints (future)

**State**: Static (manually updated when chapter content changes)

---

## Data Relationships Diagram

```
Chapter Content (MDX)
├── Frontmatter (YAML metadata)
│   ├── title
│   ├── description
│   ├── sidebar_position
│   ├── sidebar_label
│   └── tags[]
│
└── Body Content
    ├── Section 1 (H2)
    │   ├── Paragraphs (markdown)
    │   ├── Diagram Placeholder (HTML comment)
    │   └── AI-Block Placeholder (HTML comment)
    │
    ├── Section 2 (H2)
    │   ├── Paragraphs
    │   ├── Diagram Placeholder
    │   └── AI-Block Placeholder
    │
    ├── ... (Sections 3-6)
    │
    └── Section 7: Glossary (H2)
        ├── Glossary Term 1
        ├── Glossary Term 2
        └── ... (7 terms total)

Chapter Metadata (Python)
├── Core fields (id, title, summary)
├── Structure (section_count, sections[])
├── Placeholders (ai_blocks[], diagram_placeholders[])
└── RAG fields (difficulty_level, learning_outcomes[], glossary_terms[])
```

**Relationship Types**:
- **Composition**: Chapter Content contains Sections, Placeholders, Glossary Terms (delete chapter → delete all children)
- **Derivation**: Chapter Metadata derived from Chapter Content (1:1 relationship, manually synced)
- **Future Reference**: Placeholders will reference generated assets (diagrams, React components)

---

## Data Integrity Constraints

### Consistency Rules

1. **Metadata Synchronization**:
   - Chapter Metadata `title` MUST match MDX frontmatter `title`
   - Chapter Metadata `section_count` MUST match number of H2 sections in MDX
   - Chapter Metadata `sections[]` MUST match H2 headings in order

2. **Placeholder Completeness**:
   - Number of `<!-- DIAGRAM: -->` in MDX MUST equal length of `diagram_placeholders[]` in metadata
   - Number of `<!-- AI-BLOCK: -->` in MDX MUST equal length of `ai_blocks[]` in metadata
   - Placeholder names in metadata MUST match placeholder values in MDX

3. **Glossary Completeness**:
   - Section 7 MUST contain exactly 7 glossary terms (Chapter 1 requirement)
   - Each term in metadata `glossary_terms[]` MUST have definition in Section 7

### Validation Approach

**During Implementation** (Manual):
- Content writer ensures section count matches spec
- Content writer places placeholders at positions specified in research.md
- Code reviewer verifies metadata fields match MDX content

**Future Automation** (Out of Scope for This Feature):
- Parser script to extract sections, placeholders, glossary terms from MDX
- Validation script to compare extracted data with metadata
- Pre-commit hook to enforce consistency before committing changes

---

## Future Extensions (Out of Scope)

### Not Implemented in This Feature:

1. **Database Storage**: Metadata remains as Python module (no Postgres/Qdrant storage yet)
2. **Embedding Generation**: No vector embeddings created for RAG (placeholder fields only)
3. **Dynamic Content**: Content is static markdown (no personalization or translation)
4. **Versioning**: No change tracking or history (relies on git commits)
5. **Relationships**: No cross-chapter references or prerequisites enforced
6. **Asset Management**: No diagram image files or AI component implementations

### Planned for Future Features:

- **Feature 004+**: RAG pipeline - Store embeddings in Qdrant with metadata
- **Feature 005+**: Personalization - Dynamic content rendering based on user profile
- **Feature 006+**: Translation - Urdu translations with cache in Postgres
- **Feature 007+**: Diagram generation - AI-generated diagrams replacing placeholders
- **Feature 008+**: AI interactions - React components replacing AI-block placeholders

---

## Implementation Notes

### File Locations:
- **Chapter Content**: `frontend/docs/chapters/chapter-1.mdx` (new file)
- **Chapter Metadata**: `backend/app/content/chapters/chapter_1.py` (new file)
- **Metadata Directory**: `backend/app/content/chapters/` (create if doesn't exist)

### Dependencies:
- Docusaurus 3.x (already installed) - parses MDX and renders as HTML
- Python 3.11+ (already installed) - executes metadata module
- No new external dependencies required

### Validation Tools (Future):
- Flesch-Kincaid readability checker (manual or external tool)
- MDX linter (Docusaurus build provides basic validation)
- Custom validation script (future enhancement - not in this feature)

---

## Summary

This feature introduces **6 entity types**:
1. **Chapter Content** (MDX file) - primary deliverable
2. **Section** (H2 headings) - structural subdivisions
3. **Glossary Term** (markdown definitions) - vocabulary reference
4. **Diagram Placeholder** (HTML comments) - future diagram locations
5. **AI-Interactive Block Placeholder** (HTML comments) - future interactivity locations
6. **Chapter Metadata** (Python dict) - backend data structure

**Key Characteristics**:
- **Simplicity**: Static files, no database, no complex state
- **Extensibility**: Placeholder and metadata fields ready for future integration
- **Traceability**: Clear mapping from spec requirements to data structures
- **Validation**: Manual review with clear rules (automated validation in future features)

**Next Phase**: Generate contracts (API schemas) and quickstart documentation.
