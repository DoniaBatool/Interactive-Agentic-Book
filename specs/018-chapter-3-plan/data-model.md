# Data Model: Chapter 3 — Planning Layer

**Feature**: 018-chapter-3-plan
**Date**: 2025-12-05
**Purpose**: Define data structures and entities for Chapter 3 planning layer system

## Entity Definitions

### 1. Chapter Content (Primary Entity)

**Description**: Represents the complete written educational material structure for Chapter 3 (Physical AI Perception Systems) with planning layer specifications

**Storage**: MDX file at `frontend/docs/chapters/chapter-3.mdx`

**Structure**:
```yaml
# Frontmatter (YAML metadata)
---
title: string              # Full chapter title
description: string        # SEO-optimized summary (150-160 chars)
sidebar_position: integer  # Navigation order (3 for Chapter 3)
sidebar_label: string      # Abbreviated title for sidebar
tags: string[]            # Categorization tags
---

# Body Content (Markdown + HTML comments - structure only, placeholders)
## Section 1: What Is Perception in Physical AI?
<!-- Content placeholder: ... -->
<!-- CHUNK: START -->
<!-- DIAGRAM: perception-overview -->
<!-- AI-BLOCK: ask-question -->
<!-- CHUNK: END -->

## Section 2: Types of Sensors in Robotics
<!-- Content placeholder: ... -->
<!-- CHUNK: START -->
<!-- DIAGRAM: sensor-types -->
<!-- AI-BLOCK: generate-diagram -->
<!-- CHUNK: END -->

## Section 3: Computer Vision & Depth Perception
<!-- Content placeholder: ... -->
<!-- CHUNK: START -->
<!-- AI-BLOCK: explain-like-i-am-10 -->
<!-- DIAGRAM: cv-depth-flow -->
<!-- CHUNK: END -->

## Section 4: Signal Processing Basics for AI
<!-- Content placeholder: ... -->
<!-- CHUNK: START -->
<!-- DIAGRAM: feature-extraction-pipeline -->
<!-- AI-BLOCK: interactive-quiz -->
<!-- CHUNK: END -->

## Section 5: Feature Extraction & Interpretation
<!-- Content placeholder: ... -->
<!-- CHUNK: START -->
<!-- CHUNK: END -->

## Section 6: Learning Objectives
<!-- Content placeholder: 3-8 learning objectives -->
<!-- CHUNK: START -->
<!-- CHUNK: END -->

## Section 7: Glossary
<!-- Content placeholder: 7 glossary terms -->
<!-- CHUNK: START -->
<!-- CHUNK: END -->
```

**Validation Rules**:
- Title MUST start with "Chapter 3 — " format
- Description MUST be 10-250 characters
- sidebar_position MUST be 3
- MUST contain exactly 7 H2 sections in specified order
- MUST contain exactly 4 `<!-- DIAGRAM: -->` placeholders (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
- MUST contain exactly 4 `<!-- AI-BLOCK: -->` placeholders (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
- MUST contain properly paired chunk markers (`<!-- CHUNK: START -->` / `<!-- CHUNK: END -->`)
- All content MUST be placeholder comments (no actual text)

**State**: Static structure (content will be written in future feature)

---

### 2. Section (Sub-entity of Chapter Content)

**Description**: A major division within Chapter 3 focusing on a specific Physical AI perception topic

**Structure**:
```markdown
## Section Title

<!-- Content placeholder: Description of what content should be written here. Min 200 words, Grade 7-8 level. -->

<!-- CHUNK: START -->
[Optional diagram placeholder]
[Optional AI-block placeholder]
<!-- CHUNK: END -->
```

**Attributes**:
- **Heading**: H2 markdown heading (`## Section Title`)
- **Order**: Position within chapter (1-7)
- **Content**: Placeholder comments only (no actual text)
- **Placeholders**: 0-2 diagram or AI-block placeholders
- **Chunk Markers**: Properly paired START/END markers

**Relationships**:
- **Parent**: Chapter Content (1:N - one chapter has many sections)
- **Order**: Sequential within parent

**Validation Rules**:
- Section heading MUST be H2 level (not H1 or H3)
- Content MUST be placeholder comments only
- Section order MUST match spec requirements
- Chunk markers MUST be properly paired

**Chapter 3 Sections** (7 total):
1. What Is Perception in Physical AI?
2. Types of Sensors in Robotics
3. Computer Vision & Depth Perception
4. Signal Processing Basics for AI
5. Feature Extraction & Interpretation
6. Learning Objectives
7. Glossary

---

### 3. Chapter Metadata (Python Dictionary)

**Description**: Structured metadata about Chapter 3 stored in Python dictionary format

**Storage**: Python file at `backend/app/content/chapters/chapter_3.py`

**Structure**:
```python
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
    "prerequisites": [1, 2],
    "learning_outcomes": ["placeholder list"],  # 3-8 items
    "glossary_terms": ["placeholder list"]  # 7 items
}
```

**Validation Rules**:
- `id` MUST be 3
- `title` MUST match MDX frontmatter exactly
- `section_count` MUST be 7
- `sections` list MUST match MDX H2 sections exactly
- `ai_blocks` MUST have exactly 4 items
- `diagram_placeholders` MUST have exactly 4 items (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
- `difficulty_level` MUST be "intermediate"
- `prerequisites` MUST be [1, 2]
- `glossary_terms` MUST have exactly 7 items

**State**: Static metadata (content will be written in future feature)

---

### 4. Diagram Placeholder (Sub-entity of Chapter Content)

**Description**: A placeholder for a visual diagram to be generated in Chapter 3

**Storage**: MDX file as HTML comment

**Structure**:
```html
<!-- DIAGRAM: perception-overview -->
<!-- DIAGRAM: sensor-types -->
<!-- DIAGRAM: cv-depth-flow -->
<!-- DIAGRAM: feature-extraction-pipeline -->
```

**Attributes**:
- **Name**: Kebab-case identifier (string)
- **Type**: Diagram type (overview, types, flow, pipeline)
- **Section**: Section where diagram appears (1-4)
- **Order**: Position within section

**Relationships**:
- **Parent**: Section (1:N - one section can have multiple diagrams)
- **Order**: Sequential within section

**Validation Rules**:
- Name MUST use kebab-case
- Name MUST match metadata `diagram_placeholders` list exactly
- MUST have exactly 4 diagram placeholders

**Chapter 3 Diagram Placeholders** (4 total):
1. perception-overview
2. sensor-types
3. cv-depth-flow
4. feature-extraction-pipeline

---

### 5. AI-Block Placeholder (Sub-entity of Chapter Content)

**Description**: A placeholder for an AI-interactive block component in Chapter 3 (HTML comment format)

**Storage**: MDX file as HTML comment

**Structure**:
```html
<!-- AI-BLOCK: ask-question -->
<!-- AI-BLOCK: explain-like-i-am-10 -->
<!-- AI-BLOCK: interactive-quiz -->
<!-- AI-BLOCK: generate-diagram -->
```

**Attributes**:
- **Type**: AI-block type (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
- **Format**: HTML comment format
- **Section**: Section where AI-block appears (1-4)
- **Order**: Position within section

**Relationships**:
- **Parent**: Section (1:N - one section can have multiple AI blocks)
- **Order**: Sequential within section

**Validation Rules**:
- Type MUST match metadata `ai_blocks` list
- Format MUST be `<!-- AI-BLOCK: {type} -->` (uppercase AI-BLOCK)
- MUST have exactly 4 AI-block placeholders

**Chapter 3 AI-Block Placeholders** (4 total):
1. ask-question
2. explain-like-i-am-10
3. interactive-quiz
4. generate-diagram

**Note**: Feature 017 uses React components (`<AskQuestionBlock chapterId={3} />`). This specification (Feature 018) uses HTML comments for planning layer clarity.

---

### 6. Chunk Marker (Sub-entity of Chapter Content)

**Description**: A marker for RAG chunk boundaries in Chapter 3

**Storage**: MDX file as HTML comment

**Structure**:
```html
<!-- CHUNK: START -->
[Content chunk]
<!-- CHUNK: END -->
```

**Attributes**:
- **Type**: START or END marker
- **Section**: Section where chunk marker appears
- **Position**: Position within section
- **Paired**: Must have corresponding START/END marker

**Relationships**:
- **Parent**: Section (1:N - one section can have multiple chunk pairs)
- **Pair**: START marker must have corresponding END marker

**Validation Rules**:
- Chunk markers MUST be properly paired (START with END)
- Chunk markers MUST align with concept boundaries
- Chunk markers MUST respect H2 section boundaries
- Format MUST be `<!-- CHUNK: START -->` and `<!-- CHUNK: END -->` (uppercase CHUNK)

**Chunking Strategy**:
- Section-based logical chunks
- Each H2 section is a natural chunk boundary
- Chunk markers align with concept boundaries
- Semantic segmentation by concept

---

### 7. Glossary Term (Sub-entity of Chapter Content)

**Description**: A technical term defined in Chapter 3 glossary section

**Storage**: MDX file under `## Glossary` section

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

**Attributes**:
- **Term**: Technical term name (string)
- **Definition**: Beginner-friendly explanation (10-100 words)
- **Analogy**: Simple analogy when applicable (optional)
- **Order**: Position within glossary (1-7)

**Relationships**:
- **Parent**: Chapter Content (1:N - one chapter has many glossary terms)
- **Order**: Sequential within glossary section

**Validation Rules**:
- MUST have exactly 7 glossary terms
- Each term MUST have definition (10-100 words)
- Definitions MUST use analogies when possible
- Terms MUST match metadata `glossary_terms` list

**Chapter 3 Glossary Terms** (7 total):
1. Perception
2. Sensor
3. Computer Vision
4. Depth Perception
5. Signal Processing
6. Feature Extraction
7. LiDAR (or alternative term)

---

### 8. RAG Chunk File (Supporting Entity)

**Description**: Python function that will provide content chunks for RAG pipeline

**Storage**: Python file at `backend/app/content/chapters/chapter_3_chunks.py`

**Structure**:
```python
def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 3 with metadata.
    
    Chunks respect chunk markers (CHUNK: START / CHUNK: END).
    """
    # Placeholder return - no real chunking implementation
    return []
```

**Attributes**:
- **Function Name**: `get_chapter_chunks`
- **Parameters**: `chapter_id: int = 3`
- **Return Type**: `List[Dict[str, Any]]`
- **State**: Placeholder (no real implementation)
- **Chunk Marker Support**: Must respect CHUNK: START / CHUNK: END markers

**Relationships**:
- **Parent**: Chapter Content (1:1 - one chapter has one chunk file)

**Validation Rules**:
- Function MUST exist with correct signature
- Function MUST return `List[Dict[str, Any]]`
- Function MUST have `chapter_id: int = 3` parameter
- Function MUST be importable without errors
- Function MUST respect chunk markers when implemented

---

## Data Relationships

### Entity Relationship Diagram

```
Chapter Content (1)
    ├── Section (N) [1-7]
    │   ├── Diagram Placeholder (0-1)
    │   ├── AI-Block Placeholder (0-1)
    │   └── Chunk Marker Pair (1-N)
    ├── Glossary Term (N) [7]
    └── RAG Chunk File (1)
    
Chapter Metadata (1)
    └── References Chapter Content (1:1)
```

### Relationship Details

1. **Chapter Content → Section**: One-to-Many (1 chapter has 7 sections)
2. **Section → Diagram Placeholder**: One-to-Many (1 section can have 0-1 diagrams)
3. **Section → AI-Block Placeholder**: One-to-Many (1 section can have 0-1 AI blocks)
4. **Section → Chunk Marker Pair**: One-to-Many (1 section can have multiple chunk pairs)
5. **Chapter Content → Glossary Term**: One-to-Many (1 chapter has 7 glossary terms)
6. **Chapter Content → RAG Chunk File**: One-to-One (1 chapter has 1 chunk file)
7. **Chapter Metadata → Chapter Content**: One-to-One (1 metadata references 1 content)

---

## Data Flow

### Current State (Planning Phase)

1. **Specification Creation**: Create planning layer specification
2. **Contract Generation**: Generate contracts and schemas
3. **Validation Rules**: Define validation requirements
4. **Chunking Strategy**: Document chunking strategy and RAG integration

### Future State (Implementation Phase)

1. **MDX Creation**: Create MDX file with chunk markers
2. **Metadata Creation**: Create metadata file with all required fields
3. **Chunk File Creation**: Create chunk file with placeholder function
4. **Validation**: Validate structure matches contracts and schemas

### Future State (RAG Integration Phase)

1. **Chunking Implementation**: Implement chunking function respecting chunk markers
2. **Embedding Generation**: Generate embeddings for chunks (Feature 020)
3. **Qdrant Upsert**: Store chunks in Qdrant collection "chapter_3" (Feature 020)
4. **Retrieval Context**: Assemble retrieval context with chunk metadata

---

## Validation Summary

### Structure Validation
- ✅ MDX file has exactly 7 H2 sections
- ✅ MDX file has exactly 4 diagram placeholders (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
- ✅ MDX file has exactly 4 AI-block placeholders (HTML comment format)
- ✅ MDX file has exactly 7 glossary terms
- ✅ MDX file has properly paired chunk markers
- ✅ Metadata matches MDX structure exactly

### Content Validation (Future)
- ⏳ Content follows Grade 7-8 reading level
- ⏳ Content uses analogies and simplified examples
- ⏳ Content defines all technical terms clearly
- ⏳ Content aligns with course outline PDF

### Chunk Marker Validation
- ✅ All CHUNK: START markers have corresponding CHUNK: END markers
- ✅ Chunk markers align with concept boundaries
- ✅ Chunk markers respect H2 section boundaries

### Integration Validation (Future)
- ⏳ AI blocks integrate correctly with runtime engine
- ⏳ RAG chunks integrate correctly with pipeline (Feature 020)
- ⏳ Diagrams integrate correctly with generation system
