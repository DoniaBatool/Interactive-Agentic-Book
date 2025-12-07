# Tasks: Chapter 3 — MDX + Metadata Implementation

**Feature**: 038-ch3-mdx-implementation | **Branch**: `038-ch3-mdx-implementation` | **Date**: 2025-01-27
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating MDX file structure and Python metadata module. All tasks are structure implementation only—no actual content writing.

---

## Task Format

```
- [ ] [TaskID] [Priority] [Category] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Category**: SETUP (Initial setup), FRONTEND (MDX structure), BACKEND (Metadata module), RAG (RAG prep), VALIDATION (Validation)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prepare for implementation.

- [ ] [T001] [P1] [SETUP] Verify Feature 037 (Chapter 3 Content Specification) is complete: Check that specification exists with all sections and placeholders defined
- [ ] [T002] [P1] [SETUP] Verify Feature 003 (Chapter 1 Content) is complete: Check that Chapter 1 MDX structure exists for reference
- [ ] [T003] [P1] [SETUP] Verify Feature 032 (Chapter 2 Content) is complete: Check that Chapter 2 MDX structure exists for reference
- [ ] [T004] [P1] [SETUP] Verify Docusaurus frontend is functional: Check that `npm run build` works in frontend directory
- [ ] [T005] [P1] [SETUP] Verify backend directory structure exists: Check that `backend/app/content/chapters/` directory exists

**Success Criteria**:
- All prerequisite features complete
- Frontend and backend environments ready
- Reference patterns available

**Dependencies**: Feature 037, Feature 003, Feature 032 must be complete

---

## PHASE 1 — FRONTEND: MDX STRUCTURE

**User Story**: US1 - Developer Implements Chapter 3 Structure

**Test Strategy**: Can be tested by verifying MDX file exists with correct frontmatter, all sections, all placeholders, and chunk boundaries.

### Create/Update MDX File

- [ ] [T006] [P1] [FRONTEND] Create or update `frontend/docs/chapters/chapter-3.mdx` with YAML frontmatter:
  - title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
  - description: "Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"
  - sidebar_position: 3
  - sidebar_label: "Chapter 3: Physical AI Perception Systems"
  - tags: ["physical-ai", "sensors", "perception", "signal-processing"]

- [ ] [T007] [P1] [FRONTEND] Add Section 1 structure in `frontend/docs/chapters/chapter-3.mdx`:
  - Add `<!-- CHUNK: start -->` marker
  - Add H2 heading: `## What Is Perception in Physical AI?`
  - Add content placeholder comment
  - Add diagram placeholder: `<!-- DIAGRAM: perception-overview -->` (middle)
  - Add AI-block placeholder: `<!-- AI-BLOCK: ask-question -->` (end)
  - Add `<!-- CHUNK: end -->` marker

- [ ] [T008] [P1] [FRONTEND] Add Section 2 structure in `frontend/docs/chapters/chapter-3.mdx`:
  - Add `<!-- CHUNK: start -->` marker
  - Add H2 heading: `## Types of Sensors in Robotics`
  - Add content placeholder comment
  - Add diagram placeholder: `<!-- DIAGRAM: sensor-types -->` (middle)
  - Add AI-block placeholder: `<!-- AI-BLOCK: generate-diagram -->` (middle)
  - Add `<!-- CHUNK: end -->` marker

- [ ] [T009] [P1] [FRONTEND] Add Section 3 structure in `frontend/docs/chapters/chapter-3.mdx`:
  - Add `<!-- CHUNK: start -->` marker
  - Add H2 heading: `## Computer Vision & Depth Perception`
  - Add content placeholder comment
  - Add AI-block placeholder: `<!-- AI-BLOCK: explain-like-i-am-10 -->` (middle)
  - Add diagram placeholder: `<!-- DIAGRAM: cv-depth-flow -->` (end)
  - Add `<!-- CHUNK: end -->` marker

- [ ] [T010] [P1] [FRONTEND] Add Section 4 structure in `frontend/docs/chapters/chapter-3.mdx`:
  - Add `<!-- CHUNK: start -->` marker
  - Add H2 heading: `## Signal Processing Basics for AI`
  - Add content placeholder comment
  - Add diagram placeholder: `<!-- DIAGRAM: feature-extraction-pipeline -->` (middle)
  - Add AI-block placeholder: `<!-- AI-BLOCK: interactive-quiz -->` (end)
  - Add `<!-- CHUNK: end -->` marker

- [ ] [T011] [P1] [FRONTEND] Add Section 5 structure in `frontend/docs/chapters/chapter-3.mdx`:
  - Add `<!-- CHUNK: start -->` marker
  - Add H2 heading: `## Feature Extraction & Interpretation`
  - Add content placeholder comment
  - Add `<!-- CHUNK: end -->` marker

- [ ] [T012] [P1] [FRONTEND] Add Section 6 structure in `frontend/docs/chapters/chapter-3.mdx`:
  - Add `<!-- CHUNK: start -->` marker
  - Add H2 heading: `## Learning Objectives`
  - Add content placeholder comment
  - Add `<!-- CHUNK: end -->` marker

- [ ] [T013] [P1] [FRONTEND] Add Section 7 structure in `frontend/docs/chapters/chapter-3.mdx`:
  - Add `<!-- CHUNK: start -->` marker
  - Add H2 heading: `## Glossary`
  - Add content placeholder comment
  - Add `<!-- CHUNK: end -->` marker

- [ ] [T014] [P1] [FRONTEND] Validate MDX compiles: Run `npm run build` in frontend directory and verify no errors

**Acceptance Test**: MDX file created with correct frontmatter, all 7 sections, all 4 diagram placeholders, all 4 AI-block placeholders, chunk boundaries wrapping each section, and MDX compiles without errors

---

## PHASE 2 — BACKEND: METADATA MODULE

**User Story**: US2 - Backend System Provides Chapter 3 Metadata

**Test Strategy**: Can be tested by importing metadata file and verifying all fields are accessible and match Feature 037 specification.

### Create/Update Metadata File

- [ ] [T015] [P1] [BACKEND] Create or update `backend/app/content/chapters/chapter_3.py` with metadata dictionary:
  - Add module docstring with TODO comments for RAG integration
  - Add import: `from typing import List, Dict, Any`

- [ ] [T016] [P1] [BACKEND] Add core identification fields to `backend/app/content/chapters/chapter_3.py`:
  - `id`: 3 (int)
  - `title`: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)" (str)
  - `summary`: "TODO: 2-3 sentence overview" (str with TODO comment)

- [ ] [T017] [P1] [BACKEND] Add structure information fields to `backend/app/content/chapters/chapter_3.py`:
  - `section_count`: 7 (int)
  - `sections`: List of 7 section titles matching MDX exactly:
    - "What Is Perception in Physical AI?"
    - "Types of Sensors in Robotics"
    - "Computer Vision & Depth Perception"
    - "Signal Processing Basics for AI"
    - "Feature Extraction & Interpretation"
    - "Learning Objectives"
    - "Glossary"

- [ ] [T018] [P1] [BACKEND] Add placeholder tracking fields to `backend/app/content/chapters/chapter_3.py`:
  - `ai_blocks`: ["ask-question", "generate-diagram", "explain-like-i-am-10", "interactive-quiz"] (List[str])
  - `diagram_placeholders`: ["perception-overview", "sensor-types", "cv-depth-flow", "feature-extraction-pipeline"] (List[str])

- [ ] [T019] [P1] [BACKEND] Add versioning field to `backend/app/content/chapters/chapter_3.py`:
  - `last_updated`: ISO 8601 timestamp (str, current date)

- [ ] [T020] [P1] [BACKEND] Add RAG-specific metadata fields to `backend/app/content/chapters/chapter_3.py`:
  - `difficulty_level`: "intermediate" (str)
  - `prerequisites`: [1, 2] (List[int])
  - `learning_outcomes`: ["TODO: 3-8 learning outcomes"] (List[str] with TODO)
  - `glossary_terms`: ["TODO: 6-10 glossary terms"] (List[str] with TODO)

- [ ] [T021] [P1] [BACKEND] Add get_chapter_3_chunks() function to `backend/app/content/chapters/chapter_3.py`:
  - Function signature: `def get_chapter_3_chunks() -> List[Dict[str, Any]]:`
  - Function docstring: "TODO: Implement chunking from Chapter 3 MDX content. Returns list of chunks with metadata for RAG integration."
  - Function body: `return []` (placeholder)

- [ ] [T022] [P1] [BACKEND] Validate backend import: Run `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"` and verify no errors

**Acceptance Test**: Metadata file created with all required fields, TODO placeholders for summary/learning_outcomes/glossary_terms, get_chapter_3_chunks() function with TODO, and Python file imports cleanly

---

## PHASE 3 — RAG PREP

**User Story**: US1 - Developer Implements Chapter 3 Structure

**Test Strategy**: Can be tested by verifying chunk boundaries exist in MDX and get_chapter_3_chunks() function exists in metadata file.

### Add RAG Preparation Hooks

- [ ] [T023] [P1] [RAG] Verify chunk boundaries in `frontend/docs/chapters/chapter-3.mdx`:
  - Each section wrapped in `<!-- CHUNK: start -->` and `<!-- CHUNK: end -->`
  - One pair per section
  - Wraps entire section content

- [ ] [T024] [P1] [RAG] Verify get_chapter_3_chunks() function in `backend/app/content/chapters/chapter_3.py`:
  - Function exists with correct signature
  - Function has TODO comment
  - Function returns empty list placeholder

**Acceptance Test**: Chunk boundaries wrap each section in MDX, and get_chapter_3_chunks() function exists in metadata file with TODO

---

## PHASE 4 — VALIDATION

**User Story**: US1, US2 - Structure and Metadata Validation

**Test Strategy**: Can be tested by running build validation, import validation, and integrity checks.

### Validation Tasks

- [ ] [T025] [P1] [VALIDATION] MDX linting: Run `npm run build` in frontend directory and verify no errors or warnings

- [ ] [T026] [P1] [VALIDATION] Python linting: Run `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"` and verify no errors

- [ ] [T027] [P1] [VALIDATION] Title and metadata alignment check:
  - Verify metadata `title` matches MDX frontmatter `title` exactly (character-for-character)
  - Verify metadata `section_count` (7) matches number of H2 sections in MDX
  - Verify metadata `sections[]` matches MDX H2 headings in order

- [ ] [T028] [P1] [VALIDATION] Placeholder count validation:
  - Count `<!-- DIAGRAM: -->` placeholders in MDX (should be 4)
  - Count `<!-- AI-BLOCK: -->` placeholders in MDX (should be 4)
  - Verify metadata `diagram_placeholders[]` length matches MDX count (4)
  - Verify metadata `ai_blocks[]` length matches MDX count (4)

- [ ] [T029] [P1] [VALIDATION] Placeholder name validation:
  - Verify all diagram placeholder names in MDX match metadata `diagram_placeholders[]` exactly
  - Verify all AI-block placeholder names in MDX match metadata `ai_blocks[]` exactly
  - Verify all placeholder names match Feature 037 specification exactly

**Acceptance Test**: All validation checks pass (MDX compiles, Python imports, title matches, section count matches, placeholder counts match, placeholder names match Feature 037)

---

## Summary

**Total Tasks**: 29 tasks across 4 phases
**Estimated Time**: 1-2 hours (structure implementation only, no content writing)
**Complexity**: Low (following existing patterns, Feature 037 as source)

**Success Criteria**:
- ✅ MDX file created with correct frontmatter, headings, placeholders
- ✅ Metadata file created with correct schema + TODOs
- ✅ All placeholders inserted exactly as defined in Feature 037
- ✅ Project builds cleanly (`npm run build` succeeds)
- ✅ Python file imports cleanly
- ✅ No business logic added (scaffolding only)

**Next Steps**: Proceed to `/sp.implement` to execute all tasks in order.

