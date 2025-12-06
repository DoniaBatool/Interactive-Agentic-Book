# Data Model: Chapter 2 Written Content

**Feature**: 010-chapter-2-content
**Date**: 2025-12-05
**Purpose**: Define data structures and entities for Chapter 2 ROS 2 content system

## Entity Definitions

### 1. Chapter Content (Primary Entity)

**Description**: Represents the complete written educational material for Chapter 2 covering ROS 2 fundamentals

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
## Section 1: Introduction to ROS 2
[Content paragraphs]
<!-- DIAGRAM: ros2-ecosystem-overview -->
<!-- AI-BLOCK: ask-question -->

## Section 2: Nodes and Node Communication
[Content paragraphs]
<!-- DIAGRAM: node-communication-architecture -->
<!-- AI-BLOCK: generate-diagram -->

## Section 3: Topics and Messages
[Content paragraphs]
<!-- DIAGRAM: topic-pubsub-flow -->
<!-- AI-BLOCK: explain-like-i-am-10 -->

## Section 4: Services and Actions
[Content paragraphs]
<!-- DIAGRAM: services-actions-comparison -->
<!-- AI-BLOCK: interactive-quiz -->

## Section 5: ROS 2 Packages
[Content paragraphs]

## Section 6: Launch Files and Workflows
[Content paragraphs]

## Section 7: Learning Objectives
[Bullet points]

## Section 8: Summary
[6-8 line recap]

## Section 9: Glossary
[Term definitions]
```

**Validation Rules**:
- Title MUST start with "Chapter 2 — " format
- Description MUST be 10-250 characters
- sidebar_position MUST be 2
- MUST contain exactly 7 H2 sections in specified order
- MUST contain exactly 4 `<!-- DIAGRAM: -->` placeholders
- MUST contain exactly 4 `<!-- AI-BLOCK: -->` placeholders
- Reading level MUST be 7th-8th grade (Flesch-Kincaid)
- MUST follow Chapter 1 content patterns (sentence length, paragraph structure, tone)

**State**: Static (no state transitions - content is published or not)

---

### 2. Section (Sub-entity of Chapter Content)

**Description**: A major division within Chapter 2 focusing on a specific ROS 2 topic

**Structure**:
```markdown
## Section Title

[Introductory paragraph with topic sentence]

[Explanation paragraphs (3-4 sentences each)]

[Examples or applications - ROS 2 real-world examples]

[Optional diagram placeholder]
[Optional AI-block placeholder]
```

**Attributes**:
- **Heading**: H2 markdown heading (`## Section Title`)
- **Order**: Position within chapter (1-7)
- **Content**: Body paragraphs in markdown
- **Placeholders**: 0-2 diagram or AI-block placeholders
- **ROS 2 Focus**: Uses real-world ROS 2 examples (turtlebot, navigation stacks)

**Relationships**:
- **Parent**: Chapter Content (1:N - one chapter has many sections)
- **Order**: Sequential within parent
- **Prerequisite**: Chapter 1 concepts (assumed knowledge)

**Validation Rules**:
- Section heading MUST be H2 level (not H1 or H3)
- Content MUST be at least 2 paragraphs (minimum 200 words)
- Paragraphs MUST be 3-4 sentences maximum
- Sentences MUST average 15-20 words
- Examples MUST use real-world ROS 2 applications

**Required Sections (Chapter 2)**:
1. Introduction to ROS 2
2. Nodes and Node Communication
3. Topics and Messages
4. Services and Actions
5. ROS 2 Packages
6. Launch Files and Workflows
7. Learning Objectives
8. Summary
9. Glossary

---

### 3. Glossary Term (Sub-entity of Chapter Content)

**Description**: A key ROS 2 vocabulary word with beginner-friendly definition

**Structure**:
```markdown
**Term Name**: Definition text explaining the concept in accessible language.
```

**Attributes**:
- **Term**: ROS 2 technical vocabulary (e.g., "ROS 2", "Node", "Topic")
- **Definition**: 1-3 sentence explanation suitable for 12+ age group
- **Context**: Optional usage example or analogy (post office, restaurant, phone calls)

**Required Terms (Chapter 2)**:
1. ROS 2
2. Node
3. Topic
4. Service
5. Action
6. Package
7. Launch File

**Relationships**:
- **Parent**: Chapter Content (1:N - one chapter has many terms)
- **Section**: Cross-references sections where term is introduced

**Validation Rules**:
- Term MUST be bold formatted (`**Term:**`)
- Definition MUST follow immediately after colon
- Definition MUST be 10-100 words
- Language MUST avoid circular definitions
- MUST use analogies or concrete examples (post office, restaurant, phone calls)

---

### 4. Diagram Placeholder (Sub-entity of Chapter Content)

**Description**: A marker indicating where a visual diagram should be rendered (future feature)

**Structure**:
```html
<!-- DIAGRAM: placeholder-name -->
```

**Attributes**:
- **Name**: Kebab-case identifier (e.g., "ros2-ecosystem-overview")
- **Type**: Inferred from name (overview, architecture, flow, comparison)
- **Section**: Parent section where placeholder appears
- **Position**: Line number or relative position in section

**Required Placeholders (Chapter 2)**:
1. `ros2-ecosystem-overview` (Section 1)
2. `node-communication-architecture` (Section 2)
3. `topic-pubsub-flow` (Section 3)
4. `services-actions-comparison` (Section 4)

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

**Required Block Types (Chapter 2)**:
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

**Description**: Structured information about Chapter 2 used by backend systems for RAG, analytics, and personalization

**Storage**: Python module at `backend/app/content/chapters/chapter_2.py`

**Structure**:
```python
from typing import List

CHAPTER_METADATA = {
    # Core identification
    "id": int,                    # Unique chapter number (2)
    "title": str,                 # Full chapter title
    "summary": str,               # 2-3 sentence description

    # Structure information
    "section_count": int,         # Number of H2 sections (7 for Ch 2)
    "sections": List[str],        # Section titles in order

    # Placeholder tracking
    "ai_blocks": List[str],       # AI-block types present
    "diagram_placeholders": List[str],  # Diagram names present

    # Versioning
    "last_updated": str,          # ISO 8601 timestamp

    # RAG-specific metadata (future use)
    "difficulty_level": str,      # beginner | intermediate | advanced
    "prerequisites": List[int],   # Chapter IDs of prerequisites ([1] for Ch 2)
    "learning_outcomes": List[str],  # Measurable learning objectives
    "glossary_terms": List[str],  # Terms defined in glossary
}
```

**Validation Rules**:
- `id` MUST be 2
- `title` MUST match MDX frontmatter title exactly
- `section_count` MUST match actual number of H2 sections (7)
- `sections` list MUST match H2 headings in order
- `ai_blocks` MUST contain exactly 4 items matching placeholder types
- `diagram_placeholders` MUST contain exactly 4 items matching placeholder names
- `prerequisites` MUST contain [1] (Chapter 1 is prerequisite)
- `last_updated` MUST be valid ISO 8601 format

**Relationships**:
- **Source**: Derived from Chapter Content (MDX file)
- **Prerequisite**: Chapter 1 metadata (dependency relationship)
- **Consumers**: RAG pipeline (future), analytics (future), API endpoints (future)

**State**: Static (manually updated when chapter content changes)

---

## Data Relationships Diagram

```
Chapter Content (MDX)
├── Frontmatter (YAML metadata)
│   ├── title: "Chapter 2 — ROS 2 Fundamentals"
│   ├── description
│   ├── sidebar_position: 2
│   ├── sidebar_label
│   └── tags[]
│
└── Body Content
    ├── Section 1: Introduction to ROS 2 (H2)
    │   ├── Paragraphs (markdown)
    │   ├── Diagram Placeholder: ros2-ecosystem-overview
    │   └── AI-BLOCK: ask-question
    │
    ├── Section 2: Nodes and Node Communication (H2)
    │   ├── Paragraphs
    │   ├── Diagram Placeholder: node-communication-architecture
    │   └── AI-BLOCK: generate-diagram
    │
    ├── Section 3: Topics and Messages (H2)
    │   ├── Paragraphs
    │   ├── Diagram Placeholder: topic-pubsub-flow
    │   └── AI-BLOCK: explain-like-i-am-10
    │
    ├── Section 4: Services and Actions (H2)
    │   ├── Paragraphs
    │   ├── Diagram Placeholder: services-actions-comparison
    │   └── AI-BLOCK: interactive-quiz
    │
    ├── Section 5: ROS 2 Packages (H2)
    ├── Section 6: Launch Files and Workflows (H2)
    ├── Section 7: Learning Objectives (H2)
    ├── Section 8: Summary (H2)
    │
    └── Section 9: Glossary (H2)
        ├── Glossary Term: ROS 2
        ├── Glossary Term: Node
        ├── Glossary Term: Topic
        ├── Glossary Term: Service
        ├── Glossary Term: Action
        ├── Glossary Term: Package
        └── Glossary Term: Launch File

Chapter Metadata (Python)
├── Core fields (id=2, title, summary)
├── Structure (section_count=7, sections[])
├── Placeholders (ai_blocks[], diagram_placeholders[])
└── RAG fields (difficulty_level="beginner", prerequisites=[1], learning_outcomes[], glossary_terms[])
```

**Relationship Types**:
- **Composition**: Chapter Content contains Sections, Placeholders, Glossary Terms (delete chapter → delete all children)
- **Derivation**: Chapter Metadata derived from Chapter Content (1:1 relationship, manually synced)
- **Dependency**: Chapter 2 requires Chapter 1 (prerequisites=[1])
- **Future Reference**: Placeholders will reference generated assets (diagrams, React components)

---

## Data Integrity Constraints

### Consistency Rules

1. **Metadata Synchronization**:
   - Chapter Metadata `title` MUST match MDX frontmatter `title`
   - Chapter Metadata `section_count` MUST match number of H2 sections in MDX (7)
   - Chapter Metadata `sections[]` MUST match H2 headings in order

2. **Placeholder Completeness**:
   - Number of `<!-- DIAGRAM: -->` in MDX MUST equal length of `diagram_placeholders[]` in metadata (4)
   - Number of `<!-- AI-BLOCK: -->` in MDX MUST equal length of `ai_blocks[]` in metadata (4)
   - Placeholder names in metadata MUST match placeholder values in MDX

3. **Glossary Completeness**:
   - Section 9 (Glossary) MUST contain exactly 7 glossary terms
   - Each term in metadata `glossary_terms[]` MUST have definition in Section 9

4. **Prerequisites Validation**:
   - `prerequisites` field MUST contain [1] (Chapter 1 is required)
   - Chapter 1 content MUST exist before Chapter 2 can be accessed

### Validation Approach

**During Implementation** (Manual):
- Content writer ensures section count matches spec (7 sections)
- Content writer places placeholders at positions specified in research.md
- Code reviewer verifies metadata fields match MDX content
- Reviewer verifies prerequisites field contains [1]

**Future Automation** (Out of Scope for This Feature):
- Parser script to extract sections, placeholders, glossary terms from MDX
- Validation script to compare extracted data with metadata
- Pre-commit hook to enforce consistency before committing changes
- Prerequisites validation (ensure Chapter 1 exists before Chapter 2)

---

## Future Extensions (Out of Scope)

### Not Implemented in This Feature:

1. **Database Storage**: Metadata remains as Python module (no Postgres/Qdrant storage yet)
2. **Embedding Generation**: No vector embeddings created for RAG (placeholder fields only)
3. **Dynamic Content**: Content is static markdown (no personalization or translation)
4. **Versioning**: No change tracking or history (relies on git commits)
5. **Cross-Chapter References**: No automatic linking or prerequisite enforcement
6. **Asset Management**: No diagram image files or AI component implementations
7. **Code Examples**: No ROS 2 code snippets (content scaffolding only)

### Planned for Future Features:

- **Feature 011+**: RAG pipeline - Store embeddings in Qdrant with metadata
- **Feature 012+**: Personalization - Dynamic content rendering based on user profile
- **Feature 013+**: Translation - Urdu translations with cache in Postgres
- **Feature 014+**: Diagram generation - AI-generated diagrams replacing placeholders
- **Feature 015+**: AI interactions - React components replacing AI-block placeholders
- **Feature 016+**: Code examples - ROS 2 Python/C++ code snippets in chapters

---

## Implementation Notes

### File Locations:
- **Chapter Content**: `frontend/docs/chapters/chapter-2.mdx` (new file)
- **Chapter Metadata**: `backend/app/content/chapters/chapter_2.py` (new file)
- **Metadata Directory**: `backend/app/content/chapters/` (already exists from Chapter 1)

### Dependencies:
- Docusaurus 3.x (already installed) - parses MDX and renders as HTML
- Python 3.11+ (already installed) - executes metadata module
- Chapter 1 content (prerequisite) - must exist before Chapter 2
- No new external dependencies required

### Validation Tools (Future):
- Flesch-Kincaid readability checker (manual or external tool)
- MDX linter (Docusaurus build provides basic validation)
- Custom validation script (future enhancement - not in this feature)
- Prerequisites validator (future - ensure Chapter 1 exists)

---

## Summary

This feature introduces **6 entity types** (same as Chapter 1, Chapter 2-specific values):
1. **Chapter Content** (MDX file) - primary deliverable
2. **Section** (H2 headings) - structural subdivisions (7 sections for Chapter 2)
3. **Glossary Term** (markdown definitions) - vocabulary reference (7 ROS 2 terms)
4. **Diagram Placeholder** (HTML comments) - future diagram locations (4 ROS 2 diagrams)
5. **AI-Interactive Block Placeholder** (HTML comments) - future interactivity locations (4 blocks)
6. **Chapter Metadata** (Python dict) - backend data structure (with prerequisites=[1])

**Key Characteristics**:
- **Simplicity**: Static files, no database, no complex state
- **Extensibility**: Placeholder and metadata fields ready for future integration
- **Traceability**: Clear mapping from spec requirements to data structures
- **Validation**: Manual review with clear rules (automated validation in future features)
- **Consistency**: Follows Chapter 1 pattern for maintainability
- **Prerequisites**: Chapter 1 dependency properly tracked

**Next Phase**: Generate quickstart documentation for developers implementing this feature.
