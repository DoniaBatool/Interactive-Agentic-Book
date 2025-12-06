# Data Model: Chapter 2 Written Content — Structure, Metadata, Schema & Contracts

**Feature**: 014-chapter-2-content
**Date**: 2025-12-05
**Purpose**: Define data structures and entities for Chapter 2 content structure system

## Entity Definitions

### 1. Chapter Content (Primary Entity)

**Description**: Represents the complete written educational material structure for Chapter 2 (ROS 2 Fundamentals)

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

# Body Content (Markdown + JSX - structure only, placeholders)
## Section 1: Introduction to ROS 2
<!-- Content placeholder: ... -->
<!-- DIAGRAM: ros2-ecosystem-overview -->
<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />

## Section 2: Nodes and Node Communication
<!-- Content placeholder: ... -->
<!-- DIAGRAM: node-communication-architecture -->
<GenerateDiagramBlock diagramType="node-communication-architecture" chapterId={2} />

## Section 3: Topics and Messages
<!-- Content placeholder: ... -->
<ExplainLike10Block concept="topics" chapterId={2} />
<!-- DIAGRAM: topic-pubsub-flow -->

## Section 4: Services and Actions
<!-- Content placeholder: ... -->
<!-- DIAGRAM: services-actions-comparison -->
<InteractiveQuizBlock chapterId={2} numQuestions={5} />

## Section 5: ROS 2 Packages
<!-- Content placeholder: ... -->

## Section 6: Launch Files and Workflows
<!-- Content placeholder: ... -->

## Section 7: Glossary
<!-- Content placeholder: 7 glossary terms -->
```

**Validation Rules**:
- Title MUST start with "Chapter 2 — " format
- Description MUST be 10-250 characters
- sidebar_position MUST be 2
- MUST contain exactly 7 H2 sections in specified order
- MUST contain exactly 4 `<!-- DIAGRAM: -->` placeholders
- MUST contain exactly 4 AI-block React components (chapterId={2})
- All content MUST be placeholder comments (no actual text)

**State**: Static structure (content will be written in future feature)

---

### 2. Section (Sub-entity of Chapter Content)

**Description**: A major division within Chapter 2 focusing on a specific ROS 2 topic

**Structure**:
```markdown
## Section Title

<!-- Content placeholder: Description of what content should be written here. Min 200 words, 7th-8th grade level. -->

[Optional diagram placeholder]
[Optional AI-block component]
```

**Attributes**:
- **Heading**: H2 markdown heading (`## Section Title`)
- **Order**: Position within chapter (1-7)
- **Content**: Placeholder comments only (no actual text)
- **Placeholders**: 0-2 diagram or AI-block placeholders

**Relationships**:
- **Parent**: Chapter Content (1:N - one chapter has many sections)
- **Order**: Sequential within parent

**Validation Rules**:
- Section heading MUST be H2 level (not H1 or H3)
- Content MUST be placeholder comments only
- Section order MUST match spec requirements

**Chapter 2 Sections** (7 total):
1. Introduction to ROS 2
2. Nodes and Node Communication
3. Topics and Messages
4. Services and Actions
5. ROS 2 Packages
6. Launch Files and Workflows
7. Glossary

---

### 3. Diagram Placeholder (Sub-entity of Section)

**Description**: HTML comment marking where a diagram should be generated/displayed

**Storage**: Embedded in MDX file as HTML comment

**Structure**:
```html
<!-- DIAGRAM: {placeholder-name} -->
```

**Attributes**:
- **Format**: HTML comment
- **Name**: Kebab-case identifier
- **Position**: Within section content

**Chapter 2 Diagram Placeholders** (4 total):
1. `ros2-ecosystem-overview` - ROS 2 ecosystem diagram
2. `node-communication-architecture` - Node communication diagram
3. `topic-pubsub-flow` - Topic publish/subscribe flow
4. `services-actions-comparison` - Services vs actions comparison

**Validation Rules**:
- Format MUST be `<!-- DIAGRAM: {name} -->`
- Name MUST be kebab-case (lowercase, hyphens only)
- Name MUST be unique within chapter

---

### 4. AI-Interactive Block Component (Sub-entity of Section)

**Description**: React component marking where an AI-interactive block should be rendered

**Storage**: Embedded in MDX file as JSX component

**Structure**:
```jsx
<AskQuestionBlock chapterId={2} sectionId="section-id" />
<ExplainLike10Block concept="concept-name" chapterId={2} />
<InteractiveQuizBlock chapterId={2} numQuestions={5} />
<GenerateDiagramBlock diagramType="diagram-type" chapterId={2} />
```

**Attributes**:
- **Component**: React component from Feature 011
- **chapterId**: Must be `2` for Chapter 2
- **sectionId**: Must match section anchor ID (kebab-case)
- **concept**: ROS 2 concept name (for ELI10)
- **diagramType**: Must match diagram placeholder name

**Chapter 2 AI Blocks** (4 total):
1. `<AskQuestionBlock />` - Section 1 (introduction-to-ros2)
2. `<GenerateDiagramBlock />` - Section 2 (node-communication-architecture)
3. `<ExplainLike10Block />` - Section 3 (concept="topics")
4. `<InteractiveQuizBlock />` - Section 4 (numQuestions={5})

**Validation Rules**:
- Component MUST be valid React component
- chapterId MUST be `2`
- sectionId/concept/diagramType MUST match section/diagram names
- Type MUST be one of 4 allowed values

---

### 5. Glossary Term (Sub-entity of Glossary Section)

**Description**: A term definition in the Glossary section

**Storage**: Embedded in Section 7 (Glossary) of MDX file

**Structure**:
```markdown
**Term Name**: Definition text explaining the concept in accessible language using ROS 2 analogies.
```

**Attributes**:
- **Term**: Bold formatted (`**...**`), Title Case
- **Definition**: 10-100 words, uses analogies (post office, restaurant, radio, phone calls, package delivery)

**Chapter 2 Glossary Terms** (7 total):
1. **ROS 2** - Robot Operating System 2 definition
2. **Node** - Node concept with restaurant analogy
3. **Topic** - Topic concept with radio broadcast analogy
4. **Service** - Service concept with phone call analogy
5. **Action** - Action concept with package delivery analogy
6. **Package** - Package structure and organization
7. **Launch File** - Launch file purpose and usage

**Validation Rules**:
- Format MUST be `**Term**: Definition`
- Definition MUST be 10-100 words
- MUST use ROS 2 analogies where appropriate
- MUST be beginner-friendly (12+ age level)

---

### 6. Chapter Metadata (Backend Entity)

**Description**: Structured information about Chapter 2 used by backend systems for RAG, analytics, and personalization

**Storage**: Python module at `backend/app/content/chapters/chapter_2.py`

**Structure**:
```python
from typing import List

CHAPTER_METADATA = {
    # Core identification
    "id": int,                    # Chapter number (2)
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

    # RAG-specific metadata
    "difficulty_level": str,      # beginner | intermediate | advanced
    "prerequisites": List[int],   # Chapter IDs ([1] for Ch 2)
    "learning_outcomes": List[str],  # Measurable learning objectives
    "glossary_terms": List[str],  # Terms defined in glossary (7 items)
}
```

**Validation Rules**:
- `id` MUST be 2 (Chapter 2)
- `title` MUST match MDX frontmatter title exactly
- `section_count` MUST be 7
- `sections` list MUST match H2 headings in order
- `ai_blocks` MUST contain exactly 4 items matching component types
- `diagram_placeholders` MUST contain exactly 4 items matching placeholder names
- `prerequisites` MUST be `[1]` (Chapter 1 is prerequisite)
- `glossary_terms` MUST contain exactly 7 items

**Relationships**:
- **Source**: Derived from Chapter Content (MDX file)
- **Consumers**: RAG pipeline (Feature 012), runtime engine (Feature 013), API endpoints (future)

**State**: Static (manually updated when chapter structure changes)

---

### 7. Chapter Chunks (Backend Entity)

**Description**: Placeholder function for future chunking implementation

**Storage**: Python module at `backend/app/content/chapters/chapter_2_chunks.py`

**Structure**:
```python
from typing import List

def get_chapter_chunks(chapter_id: int = 2) -> List[str]:
    """
    Return list of text chunks from Chapter 2 with metadata.
    TODO: Implement chunking from Chapter 2 MDX content
    """
    return ["TODO: chunk 1", "TODO: chunk 2"]
```

**Validation Rules**:
- Function MUST exist and be importable
- Function MUST return List[str] (placeholder list)
- Function MUST have comprehensive TODO comments

**Relationships**:
- **Source**: Will be derived from Chapter Content (MDX file) in future feature
- **Consumers**: RAG pipeline (Feature 012) for semantic search

**State**: Placeholder (real implementation in future feature)

---

## Data Relationships Diagram

```
Chapter Content (MDX)
├── Frontmatter (YAML metadata)
│   ├── title: "Chapter 2 — ROS 2 Fundamentals"
│   ├── description
│   ├── sidebar_position: 2
│   ├── sidebar_label
│   └── tags: ["ros2", "robotics", "programming", "beginner"]
│
└── Body Content (Structure only - placeholders)
    ├── Section 1: Introduction to ROS 2
    │   ├── Content placeholder
    │   ├── Diagram: ros2-ecosystem-overview
    │   └── AI Block: AskQuestionBlock
    │
    ├── Section 2: Nodes and Node Communication
    │   ├── Content placeholder
    │   ├── Diagram: node-communication-architecture
    │   └── AI Block: GenerateDiagramBlock
    │
    ├── Section 3: Topics and Messages
    │   ├── Content placeholder
    │   ├── AI Block: ExplainLike10Block
    │   └── Diagram: topic-pubsub-flow
    │
    ├── Section 4: Services and Actions
    │   ├── Content placeholder
    │   ├── Diagram: services-actions-comparison
    │   └── AI Block: InteractiveQuizBlock
    │
    ├── Section 5: ROS 2 Packages
    │   └── Content placeholder
    │
    ├── Section 6: Launch Files and Workflows
    │   └── Content placeholder
    │
    └── Section 7: Glossary
        └── 7 glossary term placeholders

Chapter Metadata (Python)
├── Core fields (id: 2, title, summary)
├── Structure (section_count: 7, sections[])
├── Placeholders (ai_blocks[], diagram_placeholders[])
└── RAG fields (difficulty_level, prerequisites: [1], learning_outcomes[], glossary_terms[])

Chapter Chunks (Python)
└── get_chapter_chunks() -> List[str] (placeholder)
```

**Relationship Types**:
- **Composition**: Chapter Content contains Sections, Placeholders, Glossary Terms
- **Derivation**: Chapter Metadata derived from Chapter Content (1:1 relationship, manually synced)
- **Future Reference**: Placeholders will reference generated assets (diagrams, React components)
- **Dependency**: Chapter 2 depends on Chapter 1 (prerequisites: [1])

---

## Data Flow

### Current State (Structure Only)
```
MDX File (Structure)
    ↓
Manual Review
    ↓
Metadata File (Python)
    ↓
Chunk File (Placeholder)
```

### Future State (With Content)
```
MDX File (Content)
    ↓
Parse & Extract
    ↓
Metadata File (Python) ←→ Chunk File (Real Implementation)
    ↓
RAG Pipeline (Feature 012)
    ↓
Runtime Engine (Feature 013)
    ↓
AI Blocks (Feature 011)
```

---

## Validation Summary

### MDX File Validation
- [ ] Frontmatter has all required fields
- [ ] Exactly 7 H2 sections
- [ ] Exactly 4 diagram placeholders (kebab-case)
- [ ] Exactly 4 AI-block components (chapterId={2})
- [ ] Exactly 7 glossary term placeholders
- [ ] All content is placeholder comments (no actual text)

### Metadata File Validation
- [ ] `id` is 2
- [ ] `title` matches MDX frontmatter exactly
- [ ] `section_count` is 7
- [ ] `sections` list has 7 items matching MDX order
- [ ] `ai_blocks` has 4 items matching component types
- [ ] `diagram_placeholders` has 4 items matching placeholder names
- [ ] `prerequisites` is `[1]`
- [ ] `glossary_terms` has 7 items
- [ ] File imports without errors

### Chunk File Validation
- [ ] Function `get_chapter_chunks()` exists
- [ ] Function returns List[str] (placeholder)
- [ ] Function has comprehensive TODO comments
- [ ] File imports without errors

---

## Summary

This document defines **7 entities**:
1. **Chapter Content** - MDX file structure
2. **Section** - H2 section with placeholders
3. **Diagram Placeholder** - HTML comment for diagrams
4. **AI-Interactive Block Component** - React component for AI blocks
5. **Glossary Term** - Term definition in glossary
6. **Chapter Metadata** - Python dictionary structure
7. **Chapter Chunks** - Placeholder function for chunking

**Key Principles**:
- **Structure Only**: No actual content text (only placeholders)
- **Consistency**: Matches Chapter 1 pattern (Feature 003)
- **ROS 2-Specific**: Analogies, examples, and concepts focused on ROS 2
- **Future-Ready**: Structure prepared for content writing and RAG integration

**Next Steps**: Create quickstart.md documentation for implementing this feature.
