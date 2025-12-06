# Tasks: Chapter 3 Written Content — Structure, Metadata, Schema & Contracts

**Feature**: 017-chapter-3-content | **Branch**: `017-chapter-3-content` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating Chapter 3 content structure (scaffolding only, no real content text).

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), SETUP (Initial setup), POLISH (Final touches)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prerequisites before implementing Chapter 3 content structure.

- [ ] [T001] [P1] [SETUP] Verify Docusaurus frontend is functional: Run `cd frontend && npm run build` to confirm build succeeds
- [ ] [T002] [P1] [SETUP] Verify backend directory structure exists: Check that `backend/app/content/chapters/` directory exists
- [ ] [T003] [P1] [SETUP] Verify Chapter 1 exists: Check that `frontend/docs/chapters/chapter-1.mdx` exists (template reference)
- [ ] [T004] [P1] [SETUP] Verify Chapter 2 exists: Check that `frontend/docs/chapters/chapter-2.mdx` exists (template reference)
- [ ] [T005] [P1] [SETUP] Verify Chapter 1 metadata exists: Check that `backend/app/content/chapters/chapter_1.py` exists (template reference)
- [ ] [T006] [P1] [SETUP] Verify Chapter 2 metadata exists: Check that `backend/app/content/chapters/chapter_2.py` exists (template reference)
- [ ] [T007] [P1] [SETUP] Verify React components exist: Check that `frontend/src/components/ai/AskQuestionBlock.tsx`, `ExplainLike10Block.tsx`, `InteractiveQuizBlock.tsx`, `GenerateDiagramBlock.tsx` exist (from Feature 011)
- [ ] [T008] [P1] [SETUP] Verify contract files exist: Check that `specs/017-chapter-3-content/contracts/content-schema.md` and other contract files exist (created in spec phase)
- [ ] [T009] [P1] [SETUP] Verify documentation files exist: Check that `specs/017-chapter-3-content/research.md`, `quickstart.md`, `data-model.md` exist (created in spec phase)

**Success Criteria**:
- All prerequisite files and directories exist
- Template references available
- Ready to create structure files

**Dependencies**: Feature 003 (Chapter 1 Content), Feature 014 (Chapter 2 Content), Feature 011 (Chapter 2 AI Blocks)

---

## PHASE 1 — File Setup

**User Story**: US1 - Content Developer Creates Chapter 3 Structure

**Test Strategy**: Can be tested by creating files and verifying they exist at specified paths.

### Create Frontend MDX File

- [ ] [T010] [P1] [US1] Create `frontend/docs/chapters/chapter-3.mdx`:
  - Create new file at specified path
  - File should be empty initially (will be populated in Phase 2)
  - Verify file creation succeeds

### Create Backend Metadata File

- [ ] [T011] [P1] [US1] Create `backend/app/content/chapters/chapter_3.py`:
  - Create new file at specified path
  - File should be empty initially (will be populated in Phase 3)
  - Verify file creation succeeds

### Create Backend Chunk File

- [ ] [T012] [P1] [US1] Create `backend/app/content/chapters/chapter_3_chunks.py`:
  - Create new file at specified path
  - File should be empty initially (will be populated in Phase 4)
  - Verify file creation succeeds

### Verify Contract Files (Already Created)

- [ ] [T013] [P2] [US1] Verify `specs/017-chapter-3-content/contracts/content-schema.md` exists (already created in spec phase)
- [ ] [T014] [P2] [US1] Verify `specs/017-chapter-3-content/checklists/requirements.md` exists (already created in spec phase)
- [ ] [T015] [P2] [US1] Verify `specs/017-chapter-3-content/research.md` exists (already created in spec phase)
- [ ] [T016] [P2] [US1] Verify `specs/017-chapter-3-content/quickstart.md` exists (already created in spec phase)
- [ ] [T017] [P2] [US1] Verify `specs/017-chapter-3-content/data-model.md` exists (already created in spec phase)

**Phase Completion**: All 3 new files created, all contract files verified

---

## PHASE 2 — MDX Scaffolding

**User Story**: US1 - Content Developer Creates Chapter 3 Structure

**Test Strategy**: Can be tested by verifying MDX file has correct structure and build succeeds.

### Add Frontmatter

- [ ] [T018] [P1] [US1] Add YAML frontmatter to `frontend/docs/chapters/chapter-3.mdx`:
  - Add: `title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"`
  - Add: `description: "Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"`
  - Add: `sidebar_position: 3`
  - Add: `sidebar_label: "Chapter 3: Physical AI Perception Systems"`
  - Add: `tags: ["physical-ai", "sensors", "perception", "signal-processing"]`
  - Verify frontmatter is valid YAML

- [ ] [T019] [P1] [US1] Add React component imports to `frontend/docs/chapters/chapter-3.mdx`:
  - Add: `import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';`
  - Add: `import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';`
  - Add: `import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';`
  - Add: `import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';`

### Insert 7 Section Headings with Anchor Links

- [ ] [T020] [P1] [US1] Add Section 1 to `frontend/docs/chapters/chapter-3.mdx`:
  - Add H2 heading: `## What Is Perception in Physical AI? {#what-is-perception-in-physical-ai}`
  - Add content placeholder comment: `<!-- Content placeholder: Definition of perception in Physical AI, why perception is essential for autonomous systems, how sensors enable perception, and at least 3 real-world examples (autonomous vehicles, robotics, drones). Use eyes and ears analogy for sensors. Min 200 words, 7th-8th grade level. -->`
  - Add diagram placeholder: `<!-- DIAGRAM: physical-ai-sensing-overview -->`
  - Add AI block component: `<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />`

- [ ] [T021] [P1] [US1] Add Section 2 to `frontend/docs/chapters/chapter-3.mdx`:
  - Add H2 heading: `## Types of Sensors in Robotics {#types-of-sensors-in-robotics}`
  - Add content placeholder comment: `<!-- Content placeholder: Explanation of different sensor types (vision, LiDAR, motion, etc.), sensor categories, and how each type contributes to perception. Use categorization analogy. Min 200 words. -->`
  - Add diagram placeholder: `<!-- DIAGRAM: sensor-categories-diagram -->`
  - Add AI block component: `<GenerateDiagramBlock diagramType="sensor-categories-diagram" chapterId={3} />`

- [ ] [T022] [P1] [US1] Add Section 3 to `frontend/docs/chapters/chapter-3.mdx`:
  - Add H2 heading: `## Computer Vision & Depth Perception {#computer-vision-depth-perception}`
  - Add content placeholder comment: `<!-- Content placeholder: Explanation of computer vision, depth perception, how machines interpret visual information, and 3D spatial understanding. Use human vision analogy. Min 200 words. -->`
  - Add AI block component: `<ExplainLike10Block concept="computer-vision" chapterId={3} />`
  - Add diagram placeholder: `<!-- DIAGRAM: depth-perception-flow -->`

- [ ] [T023] [P1] [US1] Add Section 4 to `frontend/docs/chapters/chapter-3.mdx`:
  - Add H2 heading: `## Signal Processing Basics for AI {#signal-processing-basics-for-ai}`
  - Add content placeholder comment: `<!-- Content placeholder: Explanation of signal processing, filtering noise, cleaning sensor data, and how signal processing enables better decision-making. Use filtering analogy. Min 200 words. -->`
  - Add diagram placeholder: `<!-- DIAGRAM: signal-processing-pipeline -->`
  - Add AI block component: `<InteractiveQuizBlock chapterId={3} numQuestions={5} />`

- [ ] [T024] [P1] [US1] Add Section 5 to `frontend/docs/chapters/chapter-3.mdx`:
  - Add H2 heading: `## Feature Extraction & Interpretation {#feature-extraction-interpretation}`
  - Add content placeholder comment: `<!-- Content placeholder: Explanation of feature extraction, pattern recognition, identifying important information from raw data, and how features enable decision-making. Use pattern recognition analogy. Min 200 words. -->`
  - No diagram or AI block (content-only section)

- [ ] [T025] [P1] [US1] Add Section 6 to `frontend/docs/chapters/chapter-3.mdx`:
  - Add H2 heading: `## Learning Objectives {#learning-objectives}`
  - Add content placeholder comment:
    ```markdown
    <!-- Content placeholder: 3-8 learning objectives covering:
    - Define perception in Physical AI
    - Identify sensor types
    - Explain computer vision and depth perception
    - Describe signal processing basics
    - Understand feature extraction
    - Explain how perception enables autonomous decision-making
    -->
    ```

- [ ] [T026] [P1] [US1] Add Section 7 (Glossary) to `frontend/docs/chapters/chapter-3.mdx`:
  - Add H2 heading: `## Glossary {#glossary}`
  - Add content placeholder comment listing 7 terms:
    ```markdown
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

### Insert 4 Diagram Placeholders

- [ ] [T027] [P1] [US1] Verify all 4 diagram placeholders are present in `frontend/docs/chapters/chapter-3.mdx`:
  - Verify: `<!-- DIAGRAM: physical-ai-sensing-overview -->` (Section 1)
  - Verify: `<!-- DIAGRAM: sensor-categories-diagram -->` (Section 2)
  - Verify: `<!-- DIAGRAM: depth-perception-flow -->` (Section 3)
  - Verify: `<!-- DIAGRAM: signal-processing-pipeline -->` (Section 4)
  - Verify all use kebab-case naming

### Insert 4 AI-Block Placeholders

- [ ] [T028] [P1] [US1] Verify all 4 AI-block components are present in `frontend/docs/chapters/chapter-3.mdx`:
  - Verify: `<AskQuestionBlock chapterId={3} sectionId="what-is-perception-in-physical-ai" />` (Section 1)
  - Verify: `<GenerateDiagramBlock diagramType="sensor-categories-diagram" chapterId={3} />` (Section 2)
  - Verify: `<ExplainLike10Block concept="computer-vision" chapterId={3} />` (Section 3)
  - Verify: `<InteractiveQuizBlock chapterId={3} numQuestions={5} />` (Section 4)
  - Verify all have `chapterId={3}`

### Verify MDX Structure

- [ ] [T029] [P1] [US1] Verify MDX file has exactly 7 H2 sections: Run `grep -c "^## " frontend/docs/chapters/chapter-3.mdx` or manually count H2 headings
- [ ] [T030] [P1] [US1] Verify all content is placeholder comments: Check that no actual text content exists (only `<!-- Content placeholder: ... -->` comments)
- [ ] [T031] [P1] [US1] Verify all anchor links are kebab-case: Check that all section anchor IDs use kebab-case format

**Acceptance Test**: MDX file has correct frontmatter, exactly 7 H2 sections, 4 diagram placeholders, 4 AI-block components, glossary with 7 placeholder terms, all content is placeholder comments

---

## PHASE 3 — Metadata Scaffolding

**User Story**: US1 - Content Developer Creates Chapter 3 Structure

**Test Strategy**: Can be tested by creating metadata file and verifying imports work.

### Add Python Metadata with TODO Placeholders

- [ ] [T032] [P1] [US1] Add Python module header to `backend/app/content/chapters/chapter_3.py`:
  - Add: `"""Chapter 3 metadata for RAG integration and content management."""`
  - Add: `from typing import List`
  - Add: `CHAPTER_METADATA = {` (start dictionary)

- [ ] [T033] [P1] [US1] Add core identification fields to `backend/app/content/chapters/chapter_3.py`:
  - Add: `"id": 3,`
  - Add: `"title": "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)",`
  - Add: `"summary": "placeholder",  # 2-3 sentence overview`

- [ ] [T034] [P1] [US1] Add section_count and sections list to `backend/app/content/chapters/chapter_3.py`:
  - Add: `"section_count": 7,`
  - Add: `"sections": [` (start list)
  - Add: `"What Is Perception in Physical AI?",`
  - Add: `"Types of Sensors in Robotics",`
  - Add: `"Computer Vision & Depth Perception",`
  - Add: `"Signal Processing Basics for AI",`
  - Add: `"Feature Extraction & Interpretation",`
  - Add: `"Learning Objectives",`
  - Add: `"Glossary"` (last item, no comma)
  - Add: `],` (close list)

- [ ] [T035] [P1] [US1] Add ai_blocks list to `backend/app/content/chapters/chapter_3.py`:
  - Add: `"ai_blocks": [` (start list)
  - Add: `"ask-question",`
  - Add: `"explain-like-i-am-10",`
  - Add: `"interactive-quiz",`
  - Add: `"generate-diagram"` (last item, no comma)
  - Add: `],` (close list)

- [ ] [T036] [P1] [US1] Add diagram_placeholders list to `backend/app/content/chapters/chapter_3.py`:
  - Add: `"diagram_placeholders": [` (start list)
  - Add: `"physical-ai-sensing-overview",`
  - Add: `"sensor-categories-diagram",`
  - Add: `"depth-perception-flow",`
  - Add: `"signal-processing-pipeline"` (last item, no comma)
  - Add: `],` (close list)

- [ ] [T037] [P1] [US1] Add versioning field to `backend/app/content/chapters/chapter_3.py`:
  - Add: `"last_updated": "2025-12-05T00:00:00Z",`

- [ ] [T038] [P1] [US1] Add RAG-specific metadata fields to `backend/app/content/chapters/chapter_3.py`:
  - Add: `"difficulty_level": "intermediate",`
  - Add: `"prerequisites": [1, 2],`
  - Add: `"learning_outcomes": ["placeholder list"],  # 3-8 items`
  - Add: `"glossary_terms": ["placeholder list"]  # 7 items` (last field, no comma)
  - Add: `}` (close dictionary)

### Verify Metadata Structure

- [ ] [T039] [P1] [US1] Verify metadata file imports without errors: Run `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"`
- [ ] [T040] [P1] [US1] Verify all required fields are present: Check that id, title, summary, section_count, sections, ai_blocks, diagram_placeholders, last_updated, difficulty_level, prerequisites, learning_outcomes, glossary_terms are all present
- [ ] [T041] [P1] [US1] Verify section_count matches sections list length: Check that `section_count` equals length of `sections` list (7)

**Acceptance Test**: Metadata file imports successfully, all required fields present, section_count matches sections list length

---

## PHASE 4 — RAG Prep

**User Story**: US1 - Content Developer Creates Chapter 3 Structure

**Test Strategy**: Can be tested by verifying chunk file has correct function signature and imports work.

### Add Chunking Markers

- [ ] [T042] [P1] [US1] Add Python module header to `backend/app/content/chapters/chapter_3_chunks.py`:
  - Add: `"""Chapter 3 Content Chunks"`
  - Add: `Provides chapter content chunks for RAG pipeline.`
  - Add: `Chunks are used for semantic search and context retrieval.`
  - Add: `"""`
  - Add: `from typing import List, Dict, Any`

- [ ] [T043] [P1] [US1] Add placeholder function to `backend/app/content/chapters/chapter_3_chunks.py`:
  - Add function signature: `def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:`
  - Add docstring with function description and return structure
  - Add TODO comments for future implementation:
    - `TODO: Implement chunking from Chapter 3 MDX content`
    - `TODO: Load Chapter 3 content from frontend/docs/chapters/chapter-3.mdx`
    - `TODO: Implement chunking strategy:`
    - `TODO: - Max token size constraints (e.g., 512 tokens per chunk)`
    - `TODO: - Semantic segmentation by section`
    - `TODO: - Heading-aware slicing (respect H2 boundaries)`
    - `TODO: - Overlapping window strategy (e.g., 50 tokens overlap)`
    - `TODO: Extract metadata (section titles, positions, word counts)`
    - `TODO: Generate unique chunk IDs (format: "ch3-s{section}-c{chunk}")`
    - `TODO: Handle special content (glossary, diagrams, AI blocks)`
    - `TODO: Include Physical AI-specific metadata (concepts: perception, sensors, vision, signal processing)`
  - Add placeholder return: `return []`

### Add Comments for Future Embedding Logic

- [ ] [T044] [P2] [US1] Add embedding logic comments to `backend/app/content/chapters/chapter_3_chunks.py`:
  - Add comment: `# Future: Generate embeddings for each chunk using embedding model`
  - Add comment: `# Future: Store embeddings in Qdrant collection "chapter_3"`
  - Add comment: `# Future: Include chunk metadata for semantic search`

### Verify Chunk File Structure

- [ ] [T045] [P1] [US1] Verify chunk file imports without errors: Run `python -c "from app.content.chapters.chapter_3_chunks import get_chapter_chunks"`
- [ ] [T046] [P1] [US1] Verify function signature is correct: Check that function has `chapter_id: int = 3` parameter and returns `List[Dict[str, Any]]`
- [ ] [T047] [P1] [US1] Verify function is callable: Run `python -c "from app.content.chapters.chapter_3_chunks import get_chapter_chunks; assert callable(get_chapter_chunks)"`

**Acceptance Test**: Chunk file imports successfully, function exists with correct signature, function is callable

---

## PHASE 5 — Validation

**User Story**: US1, US2 - Content Developer and System Validator

**Test Strategy**: Can be tested by running validation commands and verifying results.

### Ensure MDX Compiles

- [ ] [T048] [P1] [US1] Test Docusaurus build: Run `cd frontend && npm run build` to verify MDX compiles without errors
- [ ] [T049] [P1] [US1] Verify no MDX syntax errors: Check build output for any MDX-related errors
- [ ] [T050] [P1] [US1] Verify frontmatter is valid YAML: Check that frontmatter parses correctly

### Ensure Metadata File Imports Correctly

- [ ] [T051] [P1] [US1] Test Python import: Run `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"`
- [ ] [T052] [P1] [US1] Verify metadata structure: Check that `CHAPTER_METADATA` is a dictionary with all required fields
- [ ] [T053] [P1] [US1] Verify metadata values: Check that `id == 3`, `section_count == 7`, `difficulty_level == "intermediate"`, `prerequisites == [1, 2]`

### Ensure File Structure Matches Planning

- [ ] [T054] [P1] [US1] Verify MDX file exists: Check that `frontend/docs/chapters/chapter-3.mdx` exists
- [ ] [T055] [P1] [US1] Verify metadata file exists: Check that `backend/app/content/chapters/chapter_3.py` exists
- [ ] [T056] [P1] [US1] Verify chunk file exists: Check that `backend/app/content/chapters/chapter_3_chunks.py` exists

### Cross-Validation: MDX ↔ Metadata

- [ ] [T057] [P1] [US2] Verify section count matches: Check that MDX H2 count (7) matches metadata `section_count` (7)
- [ ] [T058] [P1] [US2] Verify section titles match: Check that MDX H2 section titles match metadata `sections` list exactly
- [ ] [T059] [P1] [US2] Verify diagram placeholders match: Check that MDX diagram placeholders match metadata `diagram_placeholders` list exactly
- [ ] [T060] [P1] [US2] Verify AI-block components match: Check that MDX AI-block component types match metadata `ai_blocks` list
- [ ] [T061] [P1] [US2] Verify glossary terms match: Check that MDX glossary terms match metadata `glossary_terms` list (7 items)

### Final Structure Validation

- [ ] [T062] [P1] [US2] Verify exactly 7 H2 sections: Run `grep -c "^## " frontend/docs/chapters/chapter-3.mdx` (expected: 7)
- [ ] [T063] [P1] [US2] Verify exactly 4 diagram placeholders: Run `grep -c "<!-- DIAGRAM:" frontend/docs/chapters/chapter-3.mdx` (expected: 4)
- [ ] [T064] [P1] [US2] Verify exactly 4 AI-block components: Run `grep -c "chapterId={3}" frontend/docs/chapters/chapter-3.mdx` (expected: 4)
- [ ] [T065] [P1] [US2] Verify all placeholders use correct naming: Check that diagram placeholders use kebab-case, AI-block components have `chapterId={3}`, section anchor IDs are kebab-case

**Acceptance Test**: All validation checks pass, MDX compiles successfully, metadata imports correctly, file structure matches planning, cross-validation confirms MDX and metadata alignment

---

## Summary

**Total Tasks**: 65 tasks across 5 phases
- Phase 0: Setup & Prerequisites (9 tasks)
- Phase 1: File Setup (8 tasks)
- Phase 2: MDX Scaffolding (14 tasks)
- Phase 3: Metadata Scaffolding (10 tasks)
- Phase 4: RAG Prep (6 tasks)
- Phase 5: Validation (18 tasks)

**Estimated Time**: ~2-3 hours (structure creation only, no content writing)

**Success Criteria**:
- MDX file has exactly 7 H2 sections, 4 diagram placeholders, 4 AI-block components, 7 glossary terms
- Metadata file has all required fields matching MDX structure exactly
- Chunk file has placeholder function with correct signature
- All files import/compile without errors
- Cross-validation confirms MDX and metadata alignment
- No actual content text (only placeholders)

**Next Step**: Run `/sp.implement` to execute all structure creation tasks
