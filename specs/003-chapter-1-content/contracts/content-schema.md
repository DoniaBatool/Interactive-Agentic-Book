# Content Schema: Chapter 1 Written Content

**Feature**: 003-chapter-1-content
**Date**: 2025-12-05
**Purpose**: Define data contracts and validation schemas for chapter content

## MDX Frontmatter Schema

**Format**: YAML
**Location**: Top of `frontend/docs/chapters/chapter-1.mdx`

```yaml
# Required fields
title: string              # Pattern: "Chapter N — Title"
                          # Example: "Chapter 1 — Introduction to Physical AI & Robotics"
                          # Constraints: 10-100 characters

description: string        # SEO-optimized summary
                          # Constraints: 10-250 characters
                          # Purpose: Meta tags, search results, page summaries

sidebar_position: integer  # Navigation order
                          # Example: 1
                          # Constraints: Positive integer, must be unique in docs/chapters/

sidebar_label: string      # Abbreviated title for sidebar
                          # Example: "Chapter 1: Intro to Physical AI"
                          # Constraints: 10-50 characters

# Optional fields
tags: string[]            # Categorization tags
                          # Example: ["physical-ai", "robotics", "introduction", "beginner"]
                          # Constraints: Lowercase, kebab-case, 1-20 characters per tag
```

**Validation Rules**:
- Title MUST start with "Chapter " followed by number and em dash " — "
- sidebar_position MUST match chapter number
- All fields MUST be valid YAML (no unescaped special characters)
- Frontmatter MUST be enclosed by `---` delimiters at start and end

---

## Chapter Metadata Schema (Python)

**Format**: Python dictionary
**Location**: `backend/app/content/chapters/chapter_1.py`

```python
from typing import List

CHAPTER_METADATA = {
    # Core identification (REQUIRED)
    "id": int,                    # Chapter number (1, 2, 3, ...)
    "title": str,                 # Must match MDX frontmatter title exactly
    "summary": str,               # 2-3 sentence description (50-300 characters)

    # Structure information (REQUIRED)
    "section_count": int,         # Number of H2 sections (7 for Chapter 1)
    "sections": List[str],        # Section titles in order

    # Placeholder tracking (REQUIRED)
    "ai_blocks": List[str],       # AI-block types present
                                  # Allowed values: ["ask-question", "explain-like-i-am-10",
                                  #                  "interactive-quiz", "generate-diagram"]
    "diagram_placeholders": List[str],  # Diagram placeholder names

    # Versioning (REQUIRED)
    "last_updated": str,          # ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SSZ)

    # RAG-specific metadata (REQUIRED for Chapter 1, OPTIONAL for future chapters)
    "difficulty_level": str,      # Enum: "beginner" | "intermediate" | "advanced"
    "prerequisites": List[int],   # Chapter IDs (empty list for Chapter 1)
    "learning_outcomes": List[str],  # Measurable learning objectives (3-10 items)
    "glossary_terms": List[str],  # Terms defined in glossary (7 items for Chapter 1)
}
```

**Field Specifications**:

### `id` (Required)
- **Type**: `int`
- **Constraints**: Positive integer, must match chapter number
- **Example**: `1`

### `title` (Required)
- **Type**: `str`
- **Constraints**: Must match MDX frontmatter title exactly (character-for-character including em dash)
- **Example**: `"Chapter 1 — Introduction to Physical AI & Robotics"`

### `summary` (Required)
- **Type**: `str`
- **Constraints**: 50-300 characters, 2-3 sentences, written at 7th-8th grade level
- **Purpose**: Used for RAG embedding, search results, chapter cards
- **Example**: `"An introductory chapter covering fundamental concepts of Physical AI, robotics components, and how AI enables autonomous physical systems. Suitable for beginners with no prior robotics knowledge."`

### `section_count` (Required)
- **Type**: `int`
- **Constraints**: Must equal the number of H2 (`##`) sections in MDX file
- **Example**: `7`

### `sections` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal `section_count`, order must match MDX file exactly
- **Example**:
  ```python
  [
      "What is Physical AI?",
      "What is a Robot?",
      "AI + Robotics = Physical AI Systems",
      "Core Concepts Introduced in This Book",
      "Learning Objectives",
      "Summary",
      "Glossary"
  ]
  ```

### `ai_blocks` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal number of `<!-- AI-BLOCK: -->` placeholders in MDX, values must match placeholder types
- **Allowed Values**: `["ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram"]`
- **Example**: `["ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram"]`

### `diagram_placeholders` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal number of `<!-- DIAGRAM: -->` placeholders in MDX, values must match placeholder names
- **Format**: Kebab-case strings
- **Example**: `["physical-ai-overview", "robot-anatomy", "ai-robotics-stack", "core-concepts-flow"]`

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
- **Constraints**: List of chapter IDs (can be empty for introductory chapters)
- **Purpose**: Track knowledge dependencies for learning path recommendations
- **Example**: `[]` (Chapter 1 has no prerequisites)

### `learning_outcomes` (Required)
- **Type**: `List[str]`
- **Constraints**: 3-10 items, each must start with action verb (Define, Identify, Explain, etc.), suitable for quiz generation
- **Purpose**: Used for RAG embedding, quiz generation, progress tracking
- **Example**:
  ```python
  [
      "Define Physical AI and distinguish it from Digital AI",
      "Identify key components of robotic systems (sensors, actuators, controllers)",
      "Explain how AI enables robot autonomy",
      "Recognize core concepts: embodiment, perception, decision-making, control, interaction"
  ]
  ```

### `glossary_terms` (Required)
- **Type**: `List[str]`
- **Constraints**: Must match terms defined in Section 7 (Glossary) of MDX file, 7 items for Chapter 1
- **Purpose**: Used for semantic search expansion and term highlighting
- **Example**: `["Physical AI", "Robot", "Sensor", "Actuator", "Autonomy", "Perception", "Control System"]`

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
2. **Section Count**: Exactly 7 H2 sections for Chapter 1
3. **Section Order**: Must follow spec requirements (see data-model.md)
4. **Paragraph Length**: Maximum 4 sentences per paragraph
5. **Sentence Length**: Average 15-20 words (7th-8th grade level)
6. **Reading Level**: Flesch-Kincaid grade 7-8 (target: 60-70 Flesch Reading Ease score)

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
- `<!-- DIAGRAM: physical-ai-overview -->`
- `<!-- DIAGRAM: robot-anatomy -->`
- `<!-- DIAGRAM: ai-robotics-stack -->`

**Invalid Examples**:
- `<!--DIAGRAM: no-space-->` ❌ (missing spaces)
- `<!-- DIAGRAM: CamelCase -->` ❌ (not kebab-case)
- `<!-- DIAGRAM: with_underscore -->` ❌ (snake_case not allowed)
- `<!-- DIAGRAM: has spaces -->` ❌ (spaces in name)

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

**Invalid Examples**:
- `<!--AI-BLOCK: no-space-->` ❌ (missing spaces)
- `<!-- AI-BLOCK: custom-type -->` ❌ (not in allowed list)
- `<!-- AI-BLOCK: askQuestion -->` ❌ (CamelCase not allowed)

---

## Glossary Term Format Contract

**Format**:
```markdown
**Term Name**: Definition text explaining the concept in accessible language.
```

**Rules**:
- **Term**: Bold formatted (`**...**`), Title Case for proper nouns, Sentence case otherwise
- **Separator**: Colon immediately after closing `**` (no space before colon)
- **Definition**: Space after colon, then definition text
- **Length**: 10-100 words per definition
- **Style**: Accessible to 12+ age group, uses analogies or concrete examples
- **Tone**: Friendly but precise, avoids circular definitions

**Valid Example**:
```markdown
**Physical AI**: Artificial intelligence systems that can sense, understand, and act in the physical world through robotic bodies or embodied systems. Unlike digital AI that exists only in software, Physical AI can pick up objects, navigate spaces, and interact with people and environments.
```

**Invalid Examples**:
```markdown
Physical AI: No bold formatting ❌
**Physical AI** : Space before colon ❌
**Physical AI** Definition with no colon ❌
**Physical AI**: AI for robots (too short, < 10 words) ❌
**Physical AI**: Physical AI is AI that is physical (circular definition) ❌
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
- [ ] Exactly 4 diagram placeholders with correct naming
- [ ] Exactly 4 AI-block placeholders with correct types
- [ ] Exactly 7 glossary terms with proper formatting
- [ ] Reading level appropriate for 12+ age group

### Post-Implementation (Build Validation):
- [ ] `npm run build` in frontend completes without errors
- [ ] Python import of metadata module succeeds without errors
- [ ] MDX file renders correctly in browser at `/docs/chapters/chapter-1`
- [ ] Glossary section displays all 7 terms

---

## Future API Contracts (Out of Scope)

**Not Implemented in This Feature**:
- No REST API endpoints for chapter content
- No GraphQL schema for querying chapters
- No WebSocket events for real-time updates
- No database schema (content is static files)

**Planned for Future Features**:
- `GET /api/chapters/{id}` - Retrieve chapter metadata
- `GET /api/chapters/{id}/content` - Retrieve formatted content
- `POST /api/chapters/{id}/translate` - Request translation
- RAG query endpoints for semantic search over chapters

---

## Summary

This document defines **5 data contracts**:
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

**Next Steps**: Create quickstart.md documentation for developers implementing this feature.
