# MDX + Metadata Schema Contract: Chapter 3 Implementation

**Feature**: 038-ch3-mdx-implementation
**Created**: 2025-01-27
**Status**: Draft

## Overview

This contract defines the MDX file structure and Python metadata schema for Chapter 3 implementation. It specifies frontmatter format, section structure, placeholder formats, chunk boundaries, and metadata dictionary structure.

---

## MDX Frontmatter Contract

**Location**: `frontend/docs/chapters/chapter-3.mdx`

**Required Format**:
```yaml
---
title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
description: "Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"
sidebar_position: 3
sidebar_label: "Chapter 3: Physical AI Perception Systems"
tags: ["physical-ai", "sensors", "perception", "signal-processing"]
---
```

**Validation Rules**:
- Title MUST match Feature 037 specification exactly
- Description MUST be 10-250 characters
- sidebar_position MUST be 3
- All fields MUST be valid YAML

---

## MDX Section Structure Contract

**Section Format**:
```markdown
<!-- CHUNK: start -->
## Section Title

<!-- Content placeholder: Description of what content should be written here -->

<!-- DIAGRAM: placeholder-name -->
<!-- AI-BLOCK: block-type -->
<!-- CHUNK: end -->
```

**Required Sections** (7 total, in order):
1. What Is Perception in Physical AI?
2. Types of Sensors in Robotics
3. Computer Vision & Depth Perception
4. Signal Processing Basics for AI
5. Feature Extraction & Interpretation
6. Learning Objectives
7. Glossary

---

## Placeholder Contract

### Diagram Placeholders (4 total)

**Format**: `<!-- DIAGRAM: placeholder-name -->`

**Required Placeholders**:
- `<!-- DIAGRAM: perception-overview -->` (Section 1, middle)
- `<!-- DIAGRAM: sensor-types -->` (Section 2, middle)
- `<!-- DIAGRAM: cv-depth-flow -->` (Section 3, end)
- `<!-- DIAGRAM: feature-extraction-pipeline -->` (Section 4, middle)

**Naming Rules**:
- Kebab-case only (lowercase with hyphens)
- Must match Feature 037 specification exactly

### AI-Block Placeholders (4 total)

**Format**: `<!-- AI-BLOCK: block-type -->`

**Required Placeholders**:
- `<!-- AI-BLOCK: ask-question -->` (Section 1, end)
- `<!-- AI-BLOCK: generate-diagram -->` (Section 2, middle)
- `<!-- AI-BLOCK: explain-like-i-am-10 -->` (Section 3, middle)
- `<!-- AI-BLOCK: interactive-quiz -->` (Section 4, end)

**Placement Rules**:
- Must match Feature 037 specification exactly
- Positioned logically within sections

---

## Chunk Boundary Contract

**Format**:
```markdown
<!-- CHUNK: start -->
[Section content]
<!-- CHUNK: end -->
```

**Rules**:
- Each section MUST be wrapped in chunk boundaries
- One pair per section
- Wraps entire section content including placeholders

---

## Python Metadata Contract

**Location**: `backend/app/content/chapters/chapter_3.py`

**Required Structure**:
```python
from typing import List, Dict, Any

CHAPTER_METADATA = {
    "id": 3,
    "title": "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)",
    "summary": "TODO: 2-3 sentence overview",
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
    "ai_blocks": [
        "ask-question",
        "generate-diagram",
        "explain-like-i-am-10",
        "interactive-quiz"
    ],
    "diagram_placeholders": [
        "perception-overview",
        "sensor-types",
        "cv-depth-flow",
        "feature-extraction-pipeline"
    ],
    "last_updated": "2025-01-27T00:00:00Z",
    "difficulty_level": "intermediate",
    "prerequisites": [1, 2],
    "learning_outcomes": ["TODO: 3-8 learning outcomes"],
    "glossary_terms": ["TODO: 6-10 glossary terms"]
}

def get_chapter_3_chunks() -> List[Dict[str, Any]]:
    """
    TODO: Implement chunking from Chapter 3 MDX content.
    Returns list of chunks with metadata for RAG integration.
    """
    return []
```

**Validation Rules**:
- All fields MUST match Feature 037 specification
- TODO fields MUST have TODO comments
- Title MUST match MDX frontmatter exactly
- Section count MUST match number of H2 sections

---

## Integrity Validation Rules

1. **Section Count**: `section_count` in metadata MUST equal number of H2 sections in MDX (7)
2. **Placeholder Count**: Number of placeholders in MDX MUST match metadata lists
3. **Title Match**: Metadata `title` MUST match MDX frontmatter `title` exactly
4. **Section Order**: Metadata `sections` list MUST match MDX section order exactly

---

## Summary

This contract defines the complete MDX and metadata structure for Chapter 3. All rules, formats, and validation requirements are specified. No actual content is written—only structure and placeholders.

