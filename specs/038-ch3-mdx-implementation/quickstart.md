# Quickstart Guide: Chapter 3 MDX + Metadata Implementation

**Feature**: 038-ch3-mdx-implementation
**Branch**: `038-ch3-mdx-implementation`
**Estimated Time**: 1-2 hours (structure implementation only, no content writing)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 001 (Base Project Initialization) completed
- [x] Feature 037 (Chapter 3 Content Specification) completed - Source for structure
- [x] Feature 003 (Chapter 1 Content) completed - Reference for MDX pattern
- [x] Feature 032 (Chapter 2 Content) completed - Reference for MDX pattern
- [x] Git branch `038-ch3-mdx-implementation` checked out
- [x] Read `specs/038-ch3-mdx-implementation/spec.md`
- [x] Read `specs/037-ch3-content-spec/spec.md` (Feature 037 specification)

## Implementation Overview

**Total Steps**: 3 phases
**Primary Deliverable**: `frontend/docs/chapters/chapter-3.mdx` (structure with placeholders)
**Secondary Deliverable**: `backend/app/content/chapters/chapter_3.py` (metadata with TODOs)
**Validation**: MDX compiles, Python imports, placeholder counts match Feature 037

---

## Phase 1: MDX File Structure (45 minutes)

### Step 1.1: Update Frontmatter

**Action**: Update or create `frontend/docs/chapters/chapter-3.mdx` with correct YAML frontmatter:
```yaml
---
title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
description: "Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"
sidebar_position: 3
sidebar_label: "Chapter 3: Physical AI Perception Systems"
tags: ["physical-ai", "sensors", "perception", "signal-processing"]
---
```

### Step 1.2: Add All 7 Sections

**Action**: Add all 7 H2 sections in exact order from Feature 037:
1. What Is Perception in Physical AI?
2. Types of Sensors in Robotics
3. Computer Vision & Depth Perception
4. Signal Processing Basics for AI
5. Feature Extraction & Interpretation
6. Learning Objectives
7. Glossary

### Step 1.3: Add Diagram Placeholders

**Action**: Add 4 diagram placeholders in correct positions:
- Section 1: `<!-- DIAGRAM: perception-overview -->` (middle)
- Section 2: `<!-- DIAGRAM: sensor-types -->` (middle)
- Section 3: `<!-- DIAGRAM: cv-depth-flow -->` (end)
- Section 4: `<!-- DIAGRAM: feature-extraction-pipeline -->` (middle)

### Step 1.4: Add AI-Block Placeholders

**Action**: Add 4 AI-block placeholders in correct positions:
- Section 1: `<!-- AI-BLOCK: ask-question -->` (end)
- Section 2: `<!-- AI-BLOCK: generate-diagram -->` (middle)
- Section 3: `<!-- AI-BLOCK: explain-like-i-am-10 -->` (middle)
- Section 4: `<!-- AI-BLOCK: interactive-quiz -->` (end)

### Step 1.5: Add Chunk Boundaries

**Action**: Wrap each section in chunk boundaries:
- `<!-- CHUNK: start -->` at section start
- `<!-- CHUNK: end -->` at section end
- One pair per section

---

## Phase 2: Metadata Module (30 minutes)

### Step 2.1: Update Metadata Dictionary

**Action**: Update `backend/app/content/chapters/chapter_3.py` with all required fields:
- id: 3
- title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
- summary: "TODO: 2-3 sentence overview"
- section_count: 7
- sections: List of 7 section titles
- ai_blocks: ["ask-question", "generate-diagram", "explain-like-i-am-10", "interactive-quiz"]
- diagram_placeholders: ["perception-overview", "sensor-types", "cv-depth-flow", "feature-extraction-pipeline"]
- last_updated: ISO 8601 timestamp
- difficulty_level: "intermediate"
- prerequisites: [1, 2]
- learning_outcomes: ["TODO: 3-8 learning outcomes"]
- glossary_terms: ["TODO: 6-10 glossary terms"]

### Step 2.2: Add Chunking Function

**Action**: Add TODO function `get_chapter_3_chunks()`:
```python
def get_chapter_3_chunks() -> List[Dict[str, Any]]:
    """
    TODO: Implement chunking from Chapter 3 MDX content.
    Returns list of chunks with metadata for RAG integration.
    """
    return []
```

---

## Phase 3: Validation (15 minutes)

### Step 3.1: MDX Build Validation

**Action**: Run `npm run build` in frontend directory
**Expected**: Build succeeds with no errors

### Step 3.2: Python Import Validation

**Action**: Run `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"`
**Expected**: Import succeeds with no errors

### Step 3.3: Integrity Validation

**Action**: Verify:
- section_count (7) matches number of H2 sections
- All placeholder names match Feature 037
- Metadata title matches MDX frontmatter title exactly
- Metadata sections match MDX section order

---

## Success Criteria

- ✅ MDX file created with correct frontmatter, headings, placeholders
- ✅ Metadata file created with correct schema + TODOs
- ✅ All placeholders inserted exactly as defined in Feature 037
- ✅ Project builds cleanly (`npm run build` succeeds)
- ✅ Python file imports cleanly
- ✅ No business logic added (scaffolding only)

---

## Troubleshooting

### MDX Build Fails
- Check YAML frontmatter syntax (no tabs, proper indentation)
- Verify all sections are H2 (## not ###)
- Check for unclosed HTML comments

### Python Import Fails
- Check Python syntax (no typos, proper indentation)
- Verify all required fields are present
- Check for missing imports

### Placeholder Count Mismatch
- Count placeholders in MDX manually
- Compare with metadata lists
- Verify all placeholders from Feature 037 are present

---

## Notes

- This is structure implementation only—no actual content writing
- All placeholders must match Feature 037 specification exactly
- Metadata must match MDX structure exactly
- Chunk boundaries are required for future RAG integration

