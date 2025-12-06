# Content Schema: Chapter 2 Written Content

**Feature**: 014-chapter-2-content
**Date**: 2025-12-05
**Purpose**: Define data contracts and validation schemas for Chapter 2 content structure

## MDX Frontmatter Schema

**Format**: YAML
**Location**: Top of `frontend/docs/chapters/chapter-2.mdx`

```yaml
# Required fields
title: string              # Pattern: "Chapter 2 — Title"
                          # Example: "Chapter 2 — ROS 2 Fundamentals"
                          # Constraints: 10-100 characters

description: string        # SEO-optimized summary
                          # Constraints: 10-250 characters
                          # Purpose: Meta tags, search results, page summaries

sidebar_position: integer  # Navigation order
                          # Example: 2
                          # Constraints: Positive integer, must be unique in docs/chapters/

sidebar_label: string      # Abbreviated title for sidebar
                          # Example: "Chapter 2: ROS 2 Fundamentals"
                          # Constraints: 10-50 characters

# Optional fields
tags: string[]            # Categorization tags
                          # Example: ["ros2", "robotics", "programming", "beginner"]
                          # Constraints: Lowercase, kebab-case, 1-20 characters per tag
```

**Validation Rules**:
- Title MUST start with "Chapter 2 — " followed by title
- sidebar_position MUST be 2 (matches chapter number)
- All fields MUST be valid YAML (no unescaped special characters)
- Frontmatter MUST be enclosed by `---` delimiters at start and end

---

## Chapter Metadata Schema (Python)

**Format**: Python dictionary
**Location**: `backend/app/content/chapters/chapter_2.py`

```python
from typing import List

CHAPTER_METADATA = {
    # Core identification (REQUIRED)
    "id": int,                    # Chapter number (2)
    "title": str,                 # Must match MDX frontmatter title exactly
    "summary": str,               # 2-3 sentence description (50-300 characters)

    # Structure information (REQUIRED)
    "section_count": int,         # Number of H2 sections (7 for Chapter 2)
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
    "prerequisites": List[int],   # Chapter IDs ([1] for Chapter 2 - Chapter 1 is prerequisite)
    "learning_outcomes": List[str],  # Measurable learning objectives (3-10 items)
    "glossary_terms": List[str],  # Terms defined in glossary (7 items for Chapter 2)
}
```

**Field Specifications**:

### `id` (Required)
- **Type**: `int`
- **Constraints**: Must be 2 (Chapter 2)
- **Example**: `2`

### `title` (Required)
- **Type**: `str`
- **Constraints**: Must match MDX frontmatter title exactly (character-for-character including em dash)
- **Example**: `"Chapter 2 — ROS 2 Fundamentals"`

### `summary` (Required)
- **Type**: `str`
- **Constraints**: 50-300 characters, 2-3 sentences, written at 7th-8th grade level
- **Purpose**: Used for RAG embedding, search results, chapter cards
- **Example**: `"An introductory chapter covering ROS 2 fundamentals including nodes, topics, services, actions, packages, and launch files. Suitable for beginners with Chapter 1 prerequisite."`

### `section_count` (Required)
- **Type**: `int`
- **Constraints**: Must equal 7 (exactly 7 H2 sections for Chapter 2)
- **Example**: `7`

### `sections` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal 7, order must match MDX file exactly
- **Example**:
  ```python
  [
      "Introduction to ROS 2",
      "Nodes and Node Communication",
      "Topics and Messages",
      "Services and Actions",
      "ROS 2 Packages",
      "Launch Files and Workflows",
      "Glossary"
  ]
  ```

### `ai_blocks` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal 4, values must match placeholder types in MDX
- **Allowed Values**: `["ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram"]`
- **Example**: `["ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram"]`

### `diagram_placeholders` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal 4, values must match placeholder names in MDX, kebab-case format
- **Example**: `["ros2-ecosystem-overview", "node-communication-architecture", "topic-pubsub-flow", "services-actions-comparison"]`

### `last_updated` (Required)
- **Type**: `str`
- **Format**: ISO 8601 timestamp (`YYYY-MM-DDTHH:MM:SSZ`)
- **Constraints**: Must be valid ISO 8601, timezone must be UTC (Z suffix)
- **Example**: `"2025-12-05T00:00:00Z"`

### `difficulty_level` (Required)
- **Type**: `str`
- **Constraints**: Must be one of: `"beginner"`, `"intermediate"`, `"advanced"`
- **Purpose**: Used for personalization filtering and content recommendations
- **Example**: `"beginner"`

### `prerequisites` (Required)
- **Type**: `List[int]`
- **Constraints**: Must be `[1]` (Chapter 1 is prerequisite for Chapter 2)
- **Purpose**: Track knowledge dependencies for learning path recommendations
- **Example**: `[1]`

### `learning_outcomes` (Required)
- **Type**: `List[str]`
- **Constraints**: 3-10 items, each must start with action verb (Define, Explain, Distinguish, etc.)
- **Purpose**: Used for RAG embedding, quiz generation, progress tracking
- **Example**:
  ```python
  [
      "Define ROS 2 and explain its role in robotics development",
      "Explain how nodes communicate in a ROS 2 system",
      "Distinguish between topics, services, and actions",
      "Identify when to use each communication mechanism"
  ]
  ```

### `glossary_terms` (Required)
- **Type**: `List[str]`
- **Constraints**: Must match terms defined in Glossary section of MDX file, exactly 7 items
- **Purpose**: Used for semantic search expansion and term highlighting
- **Example**: `["ROS 2", "Node", "Topic", "Service", "Action", "Package", "Launch File"]`

---

## Content Structure Contract

### MDX Body Content Requirements

**Section Format**:
```markdown
## Section Title

<!-- Content placeholder: Description of what content should be written here. Min 200 words, 7th-8th grade level. -->

<!-- DIAGRAM: placeholder-name -->
<!-- AI-BLOCK: block-type -->
```

**Global Content Rules**:
1. **Heading Hierarchy**: Only H2 headings allowed (H1 is implicit from title)
2. **Section Count**: Exactly 7 H2 sections for Chapter 2
3. **Section Order**: Must follow spec requirements
4. **Placeholder Format**: All content must be placeholder comments (no actual text)
5. **Reading Level**: Target 7th-8th grade (Flesch-Kincaid grade 7-8)

---

## Placeholder Format Contracts

### Diagram Placeholder Contract

**Format**:
```html
<!-- DIAGRAM: {placeholder-name} -->
```

**Rules**:
- **Prefix**: `<!-- DIAGRAM: ` (note space after colon)
- **Name**: Kebab-case identifier (lowercase, hyphens only, no spaces/underscores)
- **Suffix**: ` -->` (space before closing)
- **Regex Pattern**: `^<!-- DIAGRAM: [a-z]+(-[a-z]+)* -->$`

**Valid Examples**:
- `<!-- DIAGRAM: ros2-ecosystem-overview -->`
- `<!-- DIAGRAM: node-communication-architecture -->`
- `<!-- DIAGRAM: topic-pubsub-flow -->`
- `<!-- DIAGRAM: services-actions-comparison -->`

**Invalid Examples**:
- `<!--DIAGRAM: no-space-->` ❌ (missing spaces)
- `<!-- DIAGRAM: CamelCase -->` ❌ (not kebab-case)
- `<!-- DIAGRAM: with_underscore -->` ❌ (snake_case not allowed)

### AI-Interactive Block Placeholder Contract

**Format**: React component (not HTML comment - already implemented in Feature 011)
```jsx
<AskQuestionBlock chapterId={2} sectionId="section-id" />
<ExplainLike10Block concept="concept-name" chapterId={2} />
<InteractiveQuizBlock chapterId={2} numQuestions={5} />
<GenerateDiagramBlock diagramType="diagram-type" chapterId={2} />
```

**Rules**:
- **Component**: Must use React component (not HTML comment)
- **chapterId**: Must be `2` for Chapter 2
- **sectionId**: Must match section anchor ID (kebab-case)
- **concept**: Must be ROS 2 concept name (for ELI10)
- **diagramType**: Must match diagram placeholder name

**Valid Examples**:
- `<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />`
- `<ExplainLike10Block concept="topics" chapterId={2} />`
- `<InteractiveQuizBlock chapterId={2} numQuestions={5} />`
- `<GenerateDiagramBlock diagramType="node-communication-architecture" chapterId={2} />`

---

## Glossary Term Format Contract

**Format**:
```markdown
**Term Name**: Definition text explaining the concept in accessible language.
```

**Rules**:
- **Term**: Bold formatted (`**...**`), Title Case for proper nouns
- **Separator**: Colon immediately after closing `**` (no space before colon)
- **Definition**: Space after colon, then definition text
- **Length**: 10-100 words per definition
- **Style**: Accessible to 12+ age group, uses analogies (post office, restaurant, phone calls, package delivery)
- **Tone**: Friendly but precise, avoids circular definitions

**Valid Example**:
```markdown
**ROS 2**: Robot Operating System 2, a communication framework that helps robots share information. Think of it like a post office system where different parts of a robot (nodes) can send messages (topics) to each other, make requests (services), or coordinate long tasks (actions).
```

**Invalid Examples**:
```markdown
ROS 2: No bold formatting ❌
**ROS 2** : Space before colon ❌
**ROS 2** Definition with no colon ❌
**ROS 2**: Robot OS (too short, < 10 words) ❌
```

---

## Validation Checklist

### Pre-Implementation (Planning):
- [ ] MDX frontmatter schema defined
- [ ] Python metadata schema defined
- [ ] Content structure rules documented
- [ ] Placeholder format contracts specified
- [ ] Glossary format contract specified

### During Implementation (Manual Review):
- [ ] MDX frontmatter matches schema (all required fields present)
- [ ] Python metadata matches MDX content (title, section_count, sections order)
- [ ] Exactly 7 H2 sections in correct order
- [ ] Exactly 4 diagram placeholders with correct naming (kebab-case)
- [ ] Exactly 4 AI-block components with correct props (chapterId=2)
- [ ] Exactly 7 glossary terms with proper formatting
- [ ] All content is placeholder comments (no actual text)

### Post-Implementation (Build Validation):
- [ ] `npm run build` in frontend completes without errors
- [ ] Python import of metadata module succeeds: `from app.content.chapters.chapter_2 import CHAPTER_METADATA`
- [ ] MDX file renders correctly in browser at `/docs/chapters/chapter-2`
- [ ] Glossary section displays all 7 placeholder terms

---

## Summary

This document defines **5 data contracts**:
1. **MDX Frontmatter Schema** - YAML metadata at top of MDX file
2. **Chapter Metadata Schema** - Python dictionary structure
3. **Content Structure Contract** - Section format and content rules
4. **Placeholder Format Contracts** - Diagram and AI-block component syntax
5. **Glossary Term Format Contract** - Term definition syntax

**Key Principles**:
- **Explicit Validation**: Clear rules with examples of valid and invalid formats
- **Future-Proof**: Contracts designed for machine parsing (regex patterns provided)
- **Human-Readable**: Formats remain readable in source view
- **Tool-Friendly**: Standard formats (YAML, Python dicts, React components) compatible with existing tools

**Next Steps**: Create quickstart.md documentation for developers implementing this feature.
