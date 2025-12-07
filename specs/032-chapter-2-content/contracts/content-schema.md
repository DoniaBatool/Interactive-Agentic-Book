# Content Schema: Chapter 2 Written Content

**Feature**: 032-chapter-2-content
**Date**: 2025-01-27
**Purpose**: Define data contracts and validation schemas for chapter content

## MDX Frontmatter Schema

**Format**: YAML
**Location**: Top of `frontend/docs/chapters/chapter-2.mdx`

```yaml
# Required fields
title: string              # Pattern: "Chapter N — Title"
                          # Example: "Chapter 2 — Foundations of Robotics Systems"
                          # Constraints: 10-100 characters

description: string        # SEO-optimized summary
                          # Constraints: 10-250 characters
                          # Purpose: Meta tags, search results, page summaries

sidebar_position: integer  # Navigation order
                          # Example: 2
                          # Constraints: Positive integer, must be unique in docs/chapters/

sidebar_label: string      # Abbreviated title for sidebar
                          # Example: "Chapter 2: Robotics Foundations"
                          # Constraints: 10-50 characters

# Optional fields
tags: string[]            # Categorization tags
                          # Example: ["robotics", "sensors", "actuators", "control-systems", "beginner"]
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
    "ai_blocks": List[str],       # AI-block types present (in order of appearance)
                                  # Allowed values: ["ask-question", "explain-like-i-am-10",
                                  #                  "interactive-quiz", "generate-diagram"]
    "diagram_placeholders": List[str],  # Diagram placeholder names

    # Versioning (REQUIRED)
    "last_updated": str,          # ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SSZ)

    # RAG-specific metadata (REQUIRED)
    "difficulty_level": str,      # Enum: "beginner" | "intermediate" | "advanced"
    "prerequisites": List[int],   # Chapter IDs ([1] for Chapter 2)
    "learning_outcomes": List[str],  # Measurable learning objectives (3-10 items)
    "glossary_terms": List[str],  # Terms defined in glossary (7 items for Chapter 2)
}
```

**Field Specifications**:

### `id` (Required)
- **Type**: `int`
- **Constraints**: Must be 2 for Chapter 2
- **Example**: `2`

### `title` (Required)
- **Type**: `str`
- **Constraints**: Must match MDX frontmatter title exactly (character-for-character including em dash)
- **Example**: `"Chapter 2 — Foundations of Robotics Systems"`

### `summary` (Required)
- **Type**: `str`
- **Constraints**: 50-300 characters, 2-3 sentences, written at 7th-8th grade level
- **Purpose**: Used for RAG embedding, search results, chapter cards
- **Example**: `"A foundational chapter covering sensors, actuators, control systems, and robot kinematics. Explores how robots sense their environment, move and manipulate objects, use feedback loops for control, and combine hardware with software. Suitable for beginners who have completed Chapter 1."`

### `section_count` (Required)
- **Type**: `int`
- **Constraints**: Must equal 7 (number of H2 sections in MDX file)
- **Example**: `7`

### `sections` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal 7, order must match MDX file exactly
- **Example**:
  ```python
  [
      "Sensors and Perception Systems",
      "Actuators and Mechanical Systems",
      "Control Systems & Feedback Loops",
      "Robot Kinematics & Motion",
      "Combining Hardware + Software",
      "Applications & Case Studies",
      "Glossary"
  ]
  ```

### `ai_blocks` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal 4, values must match placeholder types in order of appearance
- **Allowed Values**: `["ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram"]`
- **Order**: Must match order in MDX file (ask-question at end of Section 1, explain-like-i-am-10 during Section 3, generate-diagram inside Section 4, interactive-quiz after Section 5)
- **Example**: `["ask-question", "explain-like-i-am-10", "generate-diagram", "interactive-quiz"]`

### `diagram_placeholders` (Required)
- **Type**: `List[str]`
- **Constraints**: Length must equal 4, values must match placeholder names
- **Format**: Kebab-case strings
- **Example**: `["sensor-types-overview", "actuator-types-overview", "feedback-loop-diagram", "robot-kinematics-flow"]`

### `last_updated` (Required)
- **Type**: `str`
- **Format**: ISO 8601 timestamp (`YYYY-MM-DDTHH:MM:SSZ`)
- **Constraints**: Must be valid ISO 8601, timezone must be UTC (Z suffix)
- **Example**: `"2025-01-27T00:00:00Z"`

### `difficulty_level` (Required)
- **Type**: `str`
- **Constraints**: Must be one of: `"beginner"`, `"intermediate"`, `"advanced"`
- **Purpose**: Used for personalization filtering and content recommendations
- **Example**: `"beginner"`

### `prerequisites` (Required)
- **Type**: `List[int]`
- **Constraints**: Must contain `[1]` (Chapter 1 is prerequisite)
- **Purpose**: Track knowledge dependencies for learning path recommendations
- **Example**: `[1]`

### `learning_outcomes` (Required)
- **Type**: `List[str]`
- **Constraints**: 3-10 items, each must start with action verb (Define, Identify, Explain, etc.), suitable for quiz generation
- **Purpose**: Used for RAG embedding, quiz generation, progress tracking
- **Example**:
  ```python
  [
      "Define sensors and explain how they enable robot perception",
      "Identify different types of actuators and their applications",
      "Explain feedback loops and PID control in robotics",
      "Describe robot kinematics and degrees of freedom",
      "Understand how hardware and software integrate in robotic systems"
  ]
  ```

### `glossary_terms` (Required)
- **Type**: `List[str]`
- **Constraints**: Must match terms defined in Section 7 (Glossary) of MDX file, exactly 7 items
- **Purpose**: Used for semantic search expansion and term highlighting
- **Example**: `["Sensor", "Actuator", "Feedback Loop", "PID Control", "Kinematics", "Degrees of Freedom (DOF)", "Perception"]`

---

## Content Structure Contract

### MDX Body Content Requirements

**Section Format**:
```markdown
## Section Title

[Introductory paragraph - topic sentence + context]

[Explanation paragraph - 3-4 sentences, 15-20 words per sentence]

[Example or application paragraph]

<!-- CHUNK: start -->
<!-- DIAGRAM: placeholder-name -->
<!-- AI-BLOCK: block-type -->
<!-- CHUNK: end -->
```

**Global Content Rules**:
1. **Heading Hierarchy**: Only H1 (implicit from title) and H2 headings allowed, no H3+
2. **Section Count**: Exactly 7 H2 sections for Chapter 2
3. **Section Order**: Must follow spec requirements (see data-model.md)
4. **Paragraph Length**: Maximum 4 sentences per paragraph
5. **Sentence Length**: Average 15-20 words (7th-8th grade level)
6. **Reading Level**: Flesch-Kincaid grade 7-8 (target: 60-70 Flesch Reading Ease score)
7. **Chunk Boundaries**: Each section MUST be wrapped in `<!-- CHUNK: start -->` and `<!-- CHUNK: end -->` comments

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
- `<!-- DIAGRAM: sensor-types-overview -->`
- `<!-- DIAGRAM: actuator-types-overview -->`
- `<!-- DIAGRAM: feedback-loop-diagram -->`
- `<!-- DIAGRAM: robot-kinematics-flow -->`

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

### Chunk Boundary Contract

**Format**:
```html
<!-- CHUNK: start -->
[Content section]
<!-- CHUNK: end -->
```

**Rules**:
- **Start Marker**: `<!-- CHUNK: start -->` (exact format, case-sensitive)
- **End Marker**: `<!-- CHUNK: end -->` (exact format, case-sensitive)
- **Placement**: Each H2 section MUST be wrapped in chunk boundaries
- **Purpose**: Enable section-by-section chunking for RAG processing

**Valid Example**:
```markdown
<!-- CHUNK: start -->
## Sensors and Perception Systems

[Section content...]

<!-- DIAGRAM: sensor-types-overview -->
<!-- AI-BLOCK: ask-question -->
<!-- CHUNK: end -->
```

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
**Sensor**: A device that detects and measures physical properties from the environment, such as light, sound, temperature, or motion. Sensors convert these physical signals into electrical signals that robots can process, similar to how your eyes convert light into signals your brain understands.
```

**Invalid Examples**:
```markdown
Sensor: No bold formatting ❌
**Sensor** : Space before colon ❌
**Sensor** Definition with no colon ❌
**Sensor** Device (too short, < 10 words) ❌
**Sensor** Sensor is a sensor (circular definition) ❌
```

---

## Validation Checklist

### Pre-Implementation (Planning):
- [ ] MDX frontmatter schema defined
- [ ] Python metadata schema defined
- [ ] Content structure rules documented
- [ ] Placeholder format contracts specified
- [ ] Glossary format contract specified
- [ ] Chunk boundary contract specified

### During Implementation (Manual Review):
- [ ] MDX frontmatter matches schema (all required fields present)
- [ ] Python metadata matches MDX content (title, section_count, sections order)
- [ ] Exactly 7 H2 sections in correct order
- [ ] Exactly 4 diagram placeholders with correct naming
- [ ] Exactly 4 AI-block placeholders with correct types in correct positions
- [ ] Exactly 7 glossary terms with proper formatting
- [ ] All sections wrapped in chunk boundaries
- [ ] Reading level appropriate for 12+ age group

### Post-Implementation (Build Validation):
- [ ] `npm run build` in frontend completes without errors
- [ ] Python import of metadata module succeeds without errors
- [ ] MDX file renders correctly in browser at `/docs/chapters/chapter-2`
- [ ] Glossary section displays all 7 terms
- [ ] Chunk boundaries are properly formatted

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

This document defines **6 data contracts**:
1. **MDX Frontmatter Schema** - YAML metadata at top of MDX file
2. **Chapter Metadata Schema** - Python dictionary structure
3. **Content Structure Contract** - Section format and content rules
4. **Placeholder Format Contracts** - Diagram and AI-block comment syntax
5. **Chunk Boundary Contract** - RAG chunking markers
6. **Glossary Term Format Contract** - Term definition syntax

**Key Principles**:
- **Explicit Validation**: Clear rules with examples of valid and invalid formats
- **Future-Proof**: Contracts designed for machine parsing (regex patterns provided)
- **Human-Readable**: Formats remain readable in source view (not obfuscated)
- **Tool-Friendly**: Standard formats (YAML, Python dicts, HTML comments) compatible with existing tools

**Next Steps**: Create quickstart.md documentation for developers implementing this feature.

