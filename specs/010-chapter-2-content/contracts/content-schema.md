# Content Schema: Chapter 2 Written Content

**Feature**: 010-chapter-2-content
**Date**: 2025-12-05
**Purpose**: Define data contracts and validation schemas for Chapter 2 ROS 2 content

## MDX Frontmatter Schema

**Format**: YAML
**Location**: Top of `frontend/docs/chapters/chapter-2.mdx`

```yaml
# Required fields
title: string              # Pattern: "Chapter N — Title"
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
- Title MUST start with "Chapter " followed by number and em dash " — "
- sidebar_position MUST match chapter number (2)
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
    "prerequisites": List[int],   # Chapter IDs ([1] for Chapter 2 - requires Chapter 1)
    "learning_outcomes": List[str],  # Measurable learning objectives (4-6 items)
    "glossary_terms": List[str],  # Terms defined in glossary (7 items for Chapter 2)
}
```

**Field Specifications**:

### `id` (Required)
- **Type**: `int`
- **Constraints**: Must equal 2
- **Example**: `2`

### `title` (Required)
- **Type**: `str`
- **Constraints**: Must match MDX frontmatter title exactly (character-for-character including em dash)
- **Example**: `"Chapter 2 — ROS 2 Fundamentals"`

### `summary` (Required)
- **Type**: `str`
- **Constraints**: 50-300 characters, 2-3 sentences, written at 7th-8th grade level
- **Purpose**: Used for RAG embedding, search results, chapter cards
- **Example**: `"An introductory chapter covering ROS 2 fundamentals including nodes, topics, services, actions, packages, and launch files. Explores how robots communicate and coordinate their components using ROS 2 framework. Suitable for beginners with Chapter 1 prerequisite knowledge."`

### `section_count` (Required)
- **Type**: `int`
- **Constraints**: Must equal 7 (number of H2 sections in MDX file)
- **Example**: `7`

### `sections` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal `section_count`, order must match MDX file exactly
- **Example**:
  ```python
  [
      "Introduction to ROS 2",
      "Nodes and Node Communication",
      "Topics and Messages",
      "Services and Actions",
      "ROS 2 Packages",
      "Launch Files and Workflows",
      "Learning Objectives",
      "Summary",
      "Glossary"
  ]
  ```

### `ai_blocks` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal 4, values must match placeholder types
- **Allowed Values**: `["ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram"]`
- **Example**: `["ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram"]`

### `diagram_placeholders` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal 4, values must match placeholder names in MDX
- **Format**: Kebab-case strings
- **Example**: `["ros2-ecosystem-overview", "node-communication-architecture", "topic-pubsub-flow", "services-actions-comparison"]`

### `last_updated` (Required)
- **Type**: `str`
- **Format**: ISO 8601 timestamp (`YYYY-MM-DDTHH:MM:SSZ`)
- **Constraints**: Must be valid ISO 8601, timezone must be UTC (Z suffix)
- **Example**: `"2025-12-05T00:00:00Z"`

### `difficulty_level` (Required)
- **Type**: `str`
- **Constraints**: Must be `"beginner"` for Chapter 2
- **Purpose**: Used for personalization filtering and content recommendations
- **Example**: `"beginner"`

### `prerequisites` (Required)
- **Type**: `List[int]`
- **Constraints**: Must contain `[1]` (Chapter 1 is prerequisite)
- **Purpose**: Track knowledge dependencies for learning path recommendations
- **Example**: `[1]`

### `learning_outcomes` (Required)
- **Type**: `List[str]`
- **Constraints**: 4-6 items, each must start with action verb (Define, Identify, Explain, etc.)
- **Purpose**: Used for RAG embedding, quiz generation, progress tracking
- **Example**:
  ```python
  [
      "Define ROS 2 and explain its purpose in robotics development",
      "Identify the key components of ROS 2: nodes, topics, services, actions",
      "Explain how nodes communicate using topics, services, and actions",
      "Describe the structure and purpose of ROS 2 packages",
      "Recognize how launch files coordinate multiple nodes in robotics workflows"
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

[Introductory paragraph - topic sentence + context]

[Explanation paragraph - 3-4 sentences, 15-20 words per sentence]

[Example or application paragraph]

<!-- DIAGRAM: placeholder-name -->
<!-- AI-BLOCK: block-type -->
```

**Global Content Rules**:
1. **Heading Hierarchy**: Only H1 (implicit from title) and H2 headings allowed, no H3+
2. **Section Count**: Exactly 7 H2 sections for Chapter 2
3. **Section Order**: Must follow spec requirements (see data-model.md)
4. **Paragraph Length**: Maximum 4 sentences per paragraph
5. **Sentence Length**: Average 15-20 words (7th-8th grade level)
6. **Reading Level**: Flesch-Kincaid grade 7-8 (target: 60-70 Flesch Reading Ease score)
7. **ROS 2 Focus**: Use real-world ROS 2 examples but keep explanations accessible

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

**Valid Examples for Chapter 2**:
- `<!-- DIAGRAM: ros2-ecosystem-overview -->`
- `<!-- DIAGRAM: node-communication-architecture -->`
- `<!-- DIAGRAM: topic-pubsub-flow -->`
- `<!-- DIAGRAM: services-actions-comparison -->`

**Invalid Examples**:
- `<!--DIAGRAM: no-space-->` ❌ (missing spaces)
- `<!-- DIAGRAM: ROS2_Ecosystem -->` ❌ (not kebab-case)
- `<!-- DIAGRAM: node communication -->` ❌ (spaces in name)

### AI-Interactive Block Placeholder Contract

**Format**:
```html
<!-- AI-BLOCK: {block-type} -->
```

**Rules**:
- **Prefix**: `<!-- AI-BLOCK: ` (note space after colon)
- **Type**: One of 4 allowed values (kebab-case)
- **Suffix**: ` -->` (space before closing)
- **Regex Pattern**: `^<!-- AI-BLOCK: (ask-question|explain-like-i-am-10|interactive-quiz|generate-diagram) -->$`

**Valid Examples**:
- `<!-- AI-BLOCK: ask-question -->`
- `<!-- AI-BLOCK: explain-like-i-am-10 -->`
- `<!-- AI-BLOCK: interactive-quiz -->`
- `<!-- AI-BLOCK: generate-diagram -->`

---

## Glossary Term Format Contract

**Format**:
```markdown
**Term Name**: Definition text explaining the concept in accessible language.
```

**Rules**:
- **Term**: Bold formatted (`**...**`), Title Case for proper nouns (ROS 2), Sentence case otherwise
- **Separator**: Colon immediately after closing `**` (no space before colon)
- **Definition**: Space after colon, then definition text
- **Length**: 10-100 words per definition
- **Style**: Accessible to 12+ age group, uses analogies or concrete examples
- **Tone**: Friendly but precise, avoids circular definitions

**Valid Example**:
```markdown
**ROS 2**: Robot Operating System 2, a framework that provides tools and libraries for building robot software. ROS 2 helps different parts of a robot (sensors, processors, motors) communicate with each other, making it easier to build complex robotic systems. Think of it as the "nervous system" that connects all the robot's components.
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
- [ ] MDX frontmatter matches schema (all required fields present, sidebar_position=2)
- [ ] Python metadata matches MDX content (title, section_count, sections order)
- [ ] Exactly 7 H2 sections in correct order
- [ ] Exactly 4 diagram placeholders with correct naming
- [ ] Exactly 4 AI-block placeholders with correct types
- [ ] Exactly 7 glossary terms with proper formatting
- [ ] Reading level appropriate for 12+ age group
- [ ] Prerequisites field contains [1]

### Post-Implementation (Build Validation):
- [ ] `npm run build` in frontend completes without errors
- [ ] Python import of metadata module succeeds without errors
- [ ] MDX file renders correctly in browser at `/docs/chapters/chapter-2`
- [ ] Glossary section displays all 7 terms
- [ ] Metadata matches MDX 100% (title, sections, glossary terms)

---

## Summary

This document defines **5 data contracts** for Chapter 2:
1. **MDX Frontmatter Schema** - YAML metadata at top of MDX file
2. **Chapter Metadata Schema** - Python dictionary structure
3. **Content Structure Contract** - Section format and content rules
4. **Placeholder Format Contracts** - Diagram and AI-block comment syntax
5. **Glossary Term Format Contract** - Term definition syntax

**Key Principles**:
- **Explicit Validation**: Clear rules with examples of valid and invalid formats
- **Future-Proof**: Contracts designed for machine parsing (regex patterns provided)
- **Human-Readable**: Formats remain readable in source view (not obfuscated)
- **Tool-Friendly**: Standard formats (YAML, Python dicts, HTML comments) compatible with existing tools
- **Chapter 1 Consistency**: Follows same pattern as Chapter 1 for maintainability

**Next Steps**: Create quickstart.md documentation for developers implementing this feature.
