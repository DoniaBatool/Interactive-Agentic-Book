# Quickstart Guide: Implementing Chapter 3 Written Content — Structure, Metadata, Schema & Contracts

**Feature**: 017-chapter-3-content
**Branch**: `017-chapter-3-content`
**Estimated Time**: 1-2 hours (structure creation only, no content writing)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 003 (Chapter 1 Content) completed (template reference)
- [x] Feature 014 (Chapter 2 Content) completed (template reference)
- [x] Feature 011 (Chapter 2 AI Blocks) completed (React components available)
- [x] Docusaurus frontend running at `http://localhost:3000`
- [x] FastAPI backend structure exists at `backend/app/`
- [x] Git branch `017-chapter-3-content` checked out
- [x] Read `specs/017-chapter-3-content/spec.md`
- [x] Read `specs/017-chapter-3-content/research.md` (content writing guidelines)
- [x] Read `specs/017-chapter-3-content/data-model.md` (entity definitions)
- [x] Read `specs/017-chapter-3-content/contracts/content-schema.md` (validation rules)

## Implementation Overview

**Total Steps**: 4 phases
**Primary Deliverable**: MDX file with Chapter 3 structure (placeholders only)
**Secondary Deliverable**: Backend metadata file, chunk file, contracts
**Validation**: Manual review + Docusaurus build test + Python import test

---

## Phase 1: Frontend Structure Creation (30 minutes)

### Step 1.1: Create or Verify MDX File with Frontmatter

**Location**: `frontend/docs/chapters/chapter-3.mdx`

**Action**: Create new file with correct frontmatter:

```yaml
---
title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
description: "Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"
sidebar_position: 3
sidebar_label: "Chapter 3: Physical AI Perception Systems"
tags: ["physical-ai", "sensors", "perception", "signal-processing"]
---
```

**Validation**:
- Title starts with "Chapter 3 — "
- Description is 10-250 characters
- sidebar_position is 3 (matches chapter number)

---

### Step 1.2: Add React Component Imports

**Action**: Add imports for AI block components (from Feature 011):

```jsx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
```

**Validation**:
- All 4 components imported
- Import paths match Feature 011 structure

---

### Step 1.3: Create Section 1 - What Is Perception in Physical AI?

**Action**: Add section structure with placeholders:

```markdown
## What Is Perception in Physical AI? {#what-is-perception-in-physical-ai}

<!-- Content placeholder: Definition of perception in Physical AI, why perception is essential for autonomous systems, how sensors enable perception, and at least 3 real-world examples (autonomous vehicles, robotics, drones). Use eyes and ears analogy for sensors. Min 200 words, 7th-8th grade level. -->

<!-- DIAGRAM: physical-ai-sensing-overview -->

<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />
```

**Validation**:
- H2 heading with anchor ID
- Content placeholder comment
- Diagram placeholder (kebab-case)
- AI block component (chapterId={3})

---

### Step 1.4: Create Section 2 - Types of Sensors in Robotics

**Action**: Add section structure:

```markdown
## Types of Sensors in Robotics {#types-of-sensors-in-robotics}

<!-- Content placeholder: Explanation of different sensor types (vision, LiDAR, motion, etc.), sensor categories, and how each type contributes to perception. Use categorization analogy. Min 200 words. -->

<!-- DIAGRAM: sensor-categories-diagram -->

<GenerateDiagramBlock diagramType="sensor-categories-diagram" chapterId={3} />
```

**Validation**:
- H2 heading with anchor ID
- Content placeholder comment
- Diagram placeholder
- AI block component (chapterId={3})

---

### Step 1.5: Create Section 3 - Computer Vision & Depth Perception

**Action**: Add section structure:

```markdown
## Computer Vision & Depth Perception {#computer-vision-depth-perception}

<!-- Content placeholder: Explanation of computer vision, depth perception, how machines interpret visual information, and 3D spatial understanding. Use human vision analogy. Min 200 words. -->

<ExplainLike10Block concept="computer-vision" chapterId={3} />

<!-- DIAGRAM: depth-perception-flow -->
```

**Validation**:
- H2 heading with anchor ID
- Content placeholder comment
- AI block component (chapterId={3})
- Diagram placeholder

---

### Step 1.6: Create Section 4 - Signal Processing Basics for AI

**Action**: Add section structure:

```markdown
## Signal Processing Basics for AI {#signal-processing-basics-for-ai}

<!-- Content placeholder: Explanation of signal processing, filtering noise, cleaning sensor data, and how signal processing enables better decision-making. Use filtering analogy. Min 200 words. -->

<!-- DIAGRAM: signal-processing-pipeline -->

<InteractiveQuizBlock chapterId={3} numQuestions={5} />
```

**Validation**:
- H2 heading with anchor ID
- Content placeholder comment
- Diagram placeholder
- AI block component (chapterId={3})

---

### Step 1.7: Create Section 5 - Feature Extraction & Interpretation

**Action**: Add section structure:

```markdown
## Feature Extraction & Interpretation {#feature-extraction-interpretation}

<!-- Content placeholder: Explanation of feature extraction, pattern recognition, identifying important information from raw data, and how features enable decision-making. Use pattern recognition analogy. Min 200 words. -->
```

**Validation**:
- H2 heading with anchor ID
- Content placeholder comment
- No diagram or AI block (content-only section)

---

### Step 1.8: Create Section 6 - Learning Objectives

**Action**: Add section structure:

```markdown
## Learning Objectives {#learning-objectives}

<!-- Content placeholder: 3-8 learning objectives covering:
- Define perception in Physical AI
- Identify sensor types
- Explain computer vision and depth perception
- Describe signal processing basics
- Understand feature extraction
- Explain how perception enables autonomous decision-making
-->
```

**Validation**:
- H2 heading with anchor ID
- Content placeholder comment with learning objectives list

---

### Step 1.9: Create Section 7 - Glossary

**Action**: Add section structure:

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

**Validation**:
- H2 heading with anchor ID
- Content placeholder comment with 7 glossary terms

---

## Phase 2: Backend Metadata Creation (20 minutes)

### Step 2.1: Create Chapter Metadata File

**Location**: `backend/app/content/chapters/chapter_3.py`

**Action**: Create file with `CHAPTER_METADATA` dictionary:

```python
"""
Chapter 3 metadata for RAG integration and content management.

This module contains structured metadata for Chapter 3: "Physical AI Perception Systems"
including section information, placeholder tracking, and learning objectives.
"""

from typing import List

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
    "learning_outcomes": ["placeholder list"],  # 3-8 items
    "glossary_terms": ["placeholder list"]  # 7 items
}
```

**Validation**:
- File imports without errors
- All required fields present
- `section_count` matches MDX (7)
- `sections` list matches MDX exactly
- `ai_blocks` count matches MDX (4)
- `diagram_placeholders` count matches MDX (4)
- `difficulty_level` is "intermediate"
- `prerequisites` is [1, 2]

---

### Step 2.2: Create RAG Chunk File

**Location**: `backend/app/content/chapters/chapter_3_chunks.py`

**Action**: Create file with placeholder function:

```python
"""
Chapter 3 Content Chunks

Provides chapter content chunks for RAG pipeline.
Chunks are used for semantic search and context retrieval.
"""

from typing import List, Dict, Any


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
    
    TODO: Implement chunking from Chapter 3 MDX content
    """
    # Placeholder return - no real chunking implementation
    return []
```

**Validation**:
- File imports without errors
- Function exists with correct signature
- Return type annotation is correct

---

## Phase 3: Validation & Testing (20 minutes)

### Step 3.1: Validate MDX Structure

**Action**: Check MDX file structure:

```bash
# Count H2 sections
grep -c "^## " frontend/docs/chapters/chapter-3.mdx
# Expected: 7

# Count diagram placeholders
grep -c "<!-- DIAGRAM:" frontend/docs/chapters/chapter-3.mdx
# Expected: 4

# Count AI-block components
grep -c "chapterId={3}" frontend/docs/chapters/chapter-3.mdx
# Expected: 4
```

**Validation**:
- Exactly 7 H2 sections
- Exactly 4 diagram placeholders
- Exactly 4 AI-block components
- All placeholders use correct naming conventions

---

### Step 3.2: Validate Metadata Structure

**Action**: Check metadata file:

```python
# In Python shell
from app.content.chapters.chapter_3 import CHAPTER_METADATA

assert CHAPTER_METADATA["id"] == 3
assert CHAPTER_METADATA["section_count"] == 7
assert len(CHAPTER_METADATA["sections"]) == 7
assert len(CHAPTER_METADATA["ai_blocks"]) == 4
assert len(CHAPTER_METADATA["diagram_placeholders"]) == 4
assert CHAPTER_METADATA["difficulty_level"] == "intermediate"
assert CHAPTER_METADATA["prerequisites"] == [1, 2]
```

**Validation**:
- All assertions pass
- Metadata structure matches spec requirements

---

### Step 3.3: Test Docusaurus Build

**Action**: Build frontend to verify MDX compiles:

```bash
cd frontend
npm run build
```

**Validation**:
- Build succeeds without errors
- No MDX syntax errors
- Frontmatter is valid YAML

---

## Phase 4: Documentation & Contracts (10 minutes)

### Step 4.1: Verify Contract Files

**Action**: Check that all contract files exist:

- [x] `specs/017-chapter-3-content/contracts/content-schema.md`
- [x] `specs/017-chapter-3-content/checklists/requirements.md`
- [x] `specs/017-chapter-3-content/research.md`
- [x] `specs/017-chapter-3-content/data-model.md`
- [x] `specs/017-chapter-3-content/quickstart.md` (this file)

**Validation**:
- All contract files exist
- All documentation files exist

---

## Success Criteria

### Structure Complete
- [x] MDX file has exactly 7 H2 sections
- [x] MDX file has exactly 4 diagram placeholders
- [x] MDX file has exactly 4 AI-block components
- [x] MDX file has exactly 7 glossary terms
- [x] Frontmatter is complete and valid

### Metadata Complete
- [x] Python metadata file has all required fields
- [x] `section_count` matches MDX (7)
- [x] `sections` list matches MDX exactly
- [x] `ai_blocks` count matches MDX (4)
- [x] `diagram_placeholders` count matches MDX (4)
- [x] `difficulty_level` is "intermediate"
- [x] `prerequisites` is [1, 2]

### Contracts Complete
- [x] All contract files exist
- [x] All documentation files exist

### Validation Ready
- [x] Structure can be validated against contracts
- [x] Docusaurus build succeeds
- [x] Python imports succeed

---

## Troubleshooting

### Issue: MDX Build Fails
**Solution**: Check frontmatter YAML syntax, ensure all fields are valid

### Issue: Python Import Fails
**Solution**: Check metadata file syntax, ensure all required fields present

### Issue: Section Count Mismatch
**Solution**: Verify MDX has exactly 7 H2 sections, update metadata if needed

### Issue: Placeholder Mismatch
**Solution**: Verify MDX placeholders match metadata lists exactly

---

## Next Steps

After completing this quickstart:

1. **Planning Phase**: Run `/sp.plan` to create detailed architecture plan
2. **Task Generation**: Run `/sp.tasks` to create implementation tasks
3. **Implementation**: Run `/sp.implement` to create actual structure files
4. **Content Writing**: Write actual content (future feature)
5. **Validation**: Validate content quality and structure (future feature)

---

## Notes

- This feature creates structure only (no actual content)
- Content writing will be done in future features
- All placeholders must use consistent naming conventions
- Chapter 3 is intermediate difficulty (requires Chapters 1 and 2)
- Focus on Physical AI perception systems: sensors, vision, signal processing
