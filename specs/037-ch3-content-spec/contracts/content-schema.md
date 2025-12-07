# Content Schema Contract: Chapter 3 Content Specification

**Feature**: 037-ch3-content-spec
**Created**: 2025-01-27
**Status**: Draft

## Overview

This contract defines the content schema for Chapter 3: Physical AI Perception Systems. It specifies frontmatter structure, Python metadata rules, placeholder formats, glossary requirements, and validation rules. This is a specification contract—no actual content is written.

---

## Frontmatter Schema

### MDX Frontmatter Structure

**Location**: `frontend/docs/chapters/chapter-3.mdx`

**Required Fields**:
```yaml
---
title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
description: "Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"
sidebar_position: 3
sidebar_label: "Chapter 3: Physical AI Perception Systems"
tags: ["physical-ai", "sensors", "perception", "signal-processing"]
---
```

**Field Specifications**:

### `title` (Required)
- **Type**: `string`
- **Constraints**: Must start with "Chapter 3 — " format
- **Purpose**: Full chapter title displayed on page
- **Example**: `"Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"`

### `description` (Required)
- **Type**: `string`
- **Constraints**: 10-250 characters, SEO-optimized
- **Purpose**: Meta description for search engines and previews
- **Example**: `"Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"`

### `sidebar_position` (Required)
- **Type**: `integer`
- **Constraints**: Must be 3
- **Purpose**: Navigation order in Docusaurus sidebar
- **Example**: `3`

### `sidebar_label` (Required)
- **Type**: `string`
- **Constraints**: Abbreviated title for sidebar
- **Purpose**: Display name in navigation sidebar
- **Example**: `"Chapter 3: Physical AI Perception Systems"`

### `tags` (Required)
- **Type**: `List[string]`
- **Constraints**: Array of categorization tags
- **Purpose**: Content categorization and filtering
- **Example**: `["physical-ai", "sensors", "perception", "signal-processing"]`

---

## Python Metadata Schema

### Chapter Metadata Dictionary Structure

**Location**: `backend/app/content/chapters/chapter_3.py`

**Required Structure**:
```python
from typing import List

CHAPTER_METADATA = {
    # Core identification (REQUIRED)
    "id": int,                    # Chapter number (3)
    "title": str,                 # Must match MDX frontmatter title exactly
    "summary": str,               # 2-3 sentence description (50-300 characters)

    # Structure information (REQUIRED)
    "section_count": int,         # Number of H2 sections (7 for Chapter 3)
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
                                  # Value: "intermediate" for Chapter 3
    "prerequisites": List[int],   # Chapter IDs ([1, 2] for Chapter 3)
    "learning_outcomes": List[str],  # Measurable learning objectives (3-8 items)
    "glossary_terms": List[str],  # Terms defined in glossary (6-10 items for Chapter 3)
}
```

**Field Specifications**:

### Core Identification
- `id`: MUST be 3 (integer)
- `title`: MUST match MDX frontmatter `title` exactly
- `summary`: 2-3 sentence overview (50-300 characters)

### Structure Information
- `section_count`: MUST be 7 (integer)
- `sections`: MUST be list of exactly 7 strings matching MDX H2 section titles in order:
  1. "What Is Perception in Physical AI?"
  2. "Types of Sensors in Robotics"
  3. "Computer Vision & Depth Perception"
  4. "Signal Processing Basics for AI"
  5. "Feature Extraction & Interpretation"
  6. "Learning Objectives"
  7. "Glossary"

### Placeholder Tracking
- `ai_blocks`: MUST contain exactly 4 items: ["ask-question", "generate-diagram", "explain-like-i-am-10", "interactive-quiz"]
- `diagram_placeholders`: MUST contain 4 items: ["perception-overview", "sensor-types", "cv-depth-flow", "feature-extraction-pipeline"]

### RAG-Specific Metadata
- `difficulty_level`: MUST be "intermediate" (string)
- `prerequisites`: MUST be [1, 2] (List[int])
- `learning_outcomes`: MUST contain 3-8 items (List[str])
- `glossary_terms`: MUST contain 6-10 items (List[str])

---

## Content Structure Contract

### MDX Body Content Requirements

**Section Format**:
```markdown
## Section Title

[Content paragraphs - 3-4 sentences per paragraph, 15-20 words per sentence]

<!-- DIAGRAM: placeholder-name -->
<!-- AI-BLOCK: block-type -->
```

**Global Content Rules**:
1. **Heading Hierarchy**: Only H1 (implicit from title) and H2 headings allowed, no H3+
2. **Section Count**: Exactly 7 H2 sections for Chapter 3
3. **Section Order**: Must follow spec requirements (see spec.md)
4. **Paragraph Length**: Maximum 4 sentences per paragraph
5. **Sentence Length**: Average 15-20 words (7th-8th grade level)
6. **Reading Level**: Flesch-Kincaid grade 7-8 (target: 60-70 Flesch Reading Ease score)

---

## AI-Block Contract

### AI-Block Types

**Required AI Blocks** (4 total):
- `ask-question` - Section 1 (end)
- `generate-diagram` - Section 2 (middle)
- `explain-like-i-am-10` - Section 3 (middle)
- `interactive-quiz` - Section 4 (end)

**Placement Rules**:
- AI blocks MUST be positioned at logical points in content
- AI blocks MUST use HTML comment format: `<!-- AI-BLOCK: block-type -->`
- AI blocks MUST be invisible to readers (HTML comments)

---

## Diagram Placeholder Contract

### Diagram Placeholder Names

**Required Diagrams** (4 total):
- `perception-overview` - Section 1
- `sensor-types` - Section 2
- `cv-depth-flow` - Section 3
- `feature-extraction-pipeline` - Section 4

**Naming Rules**:
- MUST use kebab-case (lowercase with hyphens)
- MUST be descriptive of diagram purpose
- MUST NOT contain spaces or special characters
- MUST use HTML comment format: `<!-- DIAGRAM: placeholder-name -->`

---

## Glossary Contract

### Glossary Term Requirements

**Required Terms** (6-10 total):
- Perception
- Sensor
- Computer Vision
- Depth Perception
- Signal Processing
- Feature Extraction
- LiDAR (or alternative term)

**Definition Style Rules**:
- **Word Count**: 10-100 words per definition
- **Language Level**: Plain language (7th-8th grade)
- **Style**: Use analogies where appropriate
- **Format**: `**Term**: Definition text.`
- **No Circular Definitions**: Terms must not reference themselves

---

## Validation Checklist

### Content Structure Validation

- [ ] Exactly 7 H2 sections
- [ ] Section order matches specification
- [ ] All section titles match specification exactly
- [ ] No H3+ headings present

### Placeholder Validation

- [ ] Exactly 4 diagram placeholders present
- [ ] All diagram placeholders use kebab-case naming
- [ ] All diagram placeholders use correct HTML comment format
- [ ] Exactly 4 AI-block placeholders present
- [ ] All AI-block placeholders use correct HTML comment format
- [ ] AI-block placement matches specification

### Glossary Validation

- [ ] 6-10 glossary terms defined
- [ ] All terms have definitions (10-100 words)
- [ ] Definitions use plain language (7th-8th grade)
- [ ] Definitions use analogies where appropriate
- [ ] No circular definitions

### Metadata Validation

- [ ] All required metadata fields present
- [ ] Field types match specification
- [ ] Field values match MDX content
- [ ] Section count matches sections list length
- [ ] AI blocks list matches MDX placeholders
- [ ] Diagram placeholders list matches MDX placeholders

### Content Quality Validation

- [ ] Reading level: Grade 7-8 (Flesch-Kincaid)
- [ ] Paragraphs: 3-4 sentences maximum
- [ ] Sentences: 15-20 words average
- [ ] Tone: Conversational-educational
- [ ] Language: Clear and accessible

---

## Summary

This contract defines the complete content schema for Chapter 3. All rules, formats, and validation requirements are specified. No actual content is written—only the specification structure is defined.

