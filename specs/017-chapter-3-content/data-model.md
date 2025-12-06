# Data Model: Chapter 3 Written Content — Structure, Metadata, Schema & Contracts

**Feature**: 017-chapter-3-content
**Date**: 2025-12-05
**Purpose**: Define data structures and entities for Chapter 3 content structure system

## Entity Definitions

### 1. Chapter Content (Primary Entity)

**Description**: Represents the complete written educational material structure for Chapter 3 (Physical AI Perception Systems)

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

# Body Content (Markdown + JSX - structure only, placeholders)
## Section 1: What Is Perception in Physical AI?
<!-- Content placeholder: ... -->
<!-- DIAGRAM: physical-ai-sensing-overview -->
<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />

## Section 2: Types of Sensors in Robotics
<!-- Content placeholder: ... -->
<!-- DIAGRAM: sensor-categories-diagram -->
<GenerateDiagramBlock diagramType="sensor-categories-diagram" chapterId={3} />

## Section 3: Computer Vision & Depth Perception
<!-- Content placeholder: ... -->
<ExplainLike10Block concept="computer-vision" chapterId={3} />
<!-- DIAGRAM: depth-perception-flow -->

## Section 4: Signal Processing Basics for AI
<!-- Content placeholder: ... -->
<!-- DIAGRAM: signal-processing-pipeline -->
<InteractiveQuizBlock chapterId={3} numQuestions={5} />

## Section 5: Feature Extraction & Interpretation
<!-- Content placeholder: ... -->

## Section 6: Learning Objectives
<!-- Content placeholder: 3-8 learning objectives -->

## Section 7: Glossary
<!-- Content placeholder: 7 glossary terms -->
```

**Validation Rules**:
- Title MUST start with "Chapter 3 — " format
- Description MUST be 10-250 characters
- sidebar_position MUST be 3
- MUST contain exactly 7 H2 sections in specified order
- MUST contain exactly 4 `<!-- DIAGRAM: -->` placeholders
- MUST contain exactly 4 AI-block React components (chapterId={3})
- All content MUST be placeholder comments (no actual text)

**State**: Static structure (content will be written in future feature)

---

### 2. Section (Sub-entity of Chapter Content)

**Description**: A major division within Chapter 3 focusing on a specific Physical AI perception topic

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
    "summary": "placeholder",

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
        "physical-ai-sensing-overview",
        "sensor-categories-diagram",
        "depth-perception-flow",
        "signal-processing-pipeline"
    ],

    # Versioning
    "last_updated": "2025-12-05T00:00:00Z",

    # RAG-specific metadata
    "difficulty_level": "intermediate",
    "prerequisites": [1, 2],
    "learning_outcomes": ["placeholder list"],
    "glossary_terms": ["placeholder list"]
}
```

**Validation Rules**:
- `id` MUST be 3
- `title` MUST match MDX frontmatter exactly
- `section_count` MUST be 7
- `sections` list MUST match MDX H2 sections exactly
- `ai_blocks` MUST have exactly 4 items
- `diagram_placeholders` MUST have exactly 4 items
- `difficulty_level` MUST be "intermediate"
- `prerequisites` MUST be [1, 2]
- `glossary_terms` MUST have exactly 7 items

**State**: Static metadata (content will be written in future feature)

---

### 4. Glossary Term (Sub-entity of Chapter Content)

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

### 5. Diagram Placeholder (Sub-entity of Chapter Content)

**Description**: A placeholder for a visual diagram to be generated in Chapter 3

**Storage**: MDX file as HTML comment

**Structure**:
```html
<!-- DIAGRAM: physical-ai-sensing-overview -->
<!-- DIAGRAM: sensor-categories-diagram -->
<!-- DIAGRAM: depth-perception-flow -->
<!-- DIAGRAM: signal-processing-pipeline -->
```

**Attributes**:
- **Name**: Kebab-case identifier (string)
- **Type**: Diagram type (overview, categories, flow, pipeline)
- **Section**: Section where diagram appears (1-5)
- **Order**: Position within section

**Relationships**:
- **Parent**: Section (1:N - one section can have multiple diagrams)
- **Order**: Sequential within section

**Validation Rules**:
- Name MUST use kebab-case
- Name MUST match metadata `diagram_placeholders` list exactly
- MUST have exactly 4 diagram placeholders

**Chapter 3 Diagram Placeholders** (4 total):
1. physical-ai-sensing-overview
2. sensor-categories-diagram
3. depth-perception-flow
4. signal-processing-pipeline

---

### 6. AI-Block Placeholder (Sub-entity of Chapter Content)

**Description**: A placeholder for an AI-interactive block component in Chapter 3

**Storage**: MDX file as React component

**Structure**:
```jsx
<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />
<GenerateDiagramBlock diagramType="sensor-categories-diagram" chapterId={3} />
<ExplainLike10Block concept="computer-vision" chapterId={3} />
<InteractiveQuizBlock chapterId={3} numQuestions={5} />
```

**Attributes**:
- **Type**: AI-block type (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
- **Chapter ID**: Chapter identifier (3)
- **Section ID**: Section identifier (optional, string)
- **Concept**: Concept to explain (optional, string)
- **Diagram Type**: Diagram type to generate (optional, string)
- **Num Questions**: Number of quiz questions (optional, integer)

**Relationships**:
- **Parent**: Section (1:N - one section can have multiple AI blocks)
- **Order**: Sequential within section

**Validation Rules**:
- Type MUST match metadata `ai_blocks` list
- Chapter ID MUST be 3
- MUST have exactly 4 AI-block components

**Chapter 3 AI-Block Placeholders** (4 total):
1. ask-question
2. explain-like-i-am-10
3. interactive-quiz
4. generate-diagram

---

### 7. RAG Chunk File (Supporting Entity)

**Description**: Python function that will provide content chunks for RAG pipeline

**Storage**: Python file at `backend/app/content/chapters/chapter_3_chunks.py`

**Structure**:
```python
def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 3 with metadata.
    
    Args:
        chapter_id: Chapter identifier (default: 3 for Chapter 3)
    
    Returns:
        List of chunk dictionaries with structure:
        [
            {
                "id": str,
                "text": str,
                "chapter_id": 3,
                "section_id": str,
                "position": int,
                "word_count": int,
                "metadata": dict
            },
            ...
        ]
    """
    # Placeholder return - no real chunking implementation
    return []
```

**Attributes**:
- **Function Name**: `get_chapter_chunks`
- **Parameters**: `chapter_id: int = 3`
- **Return Type**: `List[Dict[str, Any]]`
- **State**: Placeholder (no real implementation)

**Relationships**:
- **Parent**: Chapter Content (1:1 - one chapter has one chunk file)

**Validation Rules**:
- Function MUST exist with correct signature
- Function MUST return `List[Dict[str, Any]]`
- Function MUST have `chapter_id: int = 3` parameter
- Function MUST be importable without errors

---

## Data Relationships

### Entity Relationship Diagram

```
Chapter Content (1)
    ├── Section (N) [1-7]
    │   ├── Diagram Placeholder (0-1)
    │   └── AI-Block Placeholder (0-1)
    ├── Glossary Term (N) [7]
    └── RAG Chunk File (1)
    
Chapter Metadata (1)
    └── References Chapter Content (1:1)
```

### Relationship Details

1. **Chapter Content → Section**: One-to-Many (1 chapter has 7 sections)
2. **Section → Diagram Placeholder**: One-to-Many (1 section can have 0-1 diagrams)
3. **Section → AI-Block Placeholder**: One-to-Many (1 section can have 0-1 AI blocks)
4. **Chapter Content → Glossary Term**: One-to-Many (1 chapter has 7 glossary terms)
5. **Chapter Content → RAG Chunk File**: One-to-One (1 chapter has 1 chunk file)
6. **Chapter Metadata → Chapter Content**: One-to-One (1 metadata references 1 content)

---

## Data Flow

### Current State (Scaffolding Phase)

1. **MDX File Creation**: Create `chapter-3.mdx` with structure and placeholders
2. **Metadata File Creation**: Create `chapter_3.py` with `CHAPTER_METADATA` dictionary
3. **Chunk File Creation**: Create `chapter_3_chunks.py` with placeholder function
4. **Validation**: Validate structure matches contracts and schemas

### Future State (Content Writing Phase)

1. **Content Writing**: Write actual content in MDX file
2. **Metadata Update**: Update metadata with actual content information
3. **Chunk Implementation**: Implement chunking function with real logic
4. **Validation**: Validate content quality and structure

---

## Validation Summary

### Structure Validation
- ✅ MDX file has exactly 7 H2 sections
- ✅ MDX file has exactly 4 diagram placeholders
- ✅ MDX file has exactly 4 AI-block components
- ✅ MDX file has exactly 7 glossary terms
- ✅ Metadata matches MDX structure exactly

### Content Validation (Future)
- ⏳ Content follows 7th-8th grade reading level
- ⏳ Content uses analogies and simplified examples
- ⏳ Content defines all technical terms clearly
- ⏳ Content aligns with course outline PDF

### Integration Validation (Future)
- ⏳ AI blocks integrate correctly with runtime engine
- ⏳ RAG chunks integrate correctly with pipeline
- ⏳ Diagrams integrate correctly with generation system
