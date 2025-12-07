# Feature Specification: Chapter 3 — MDX + Metadata Implementation

**Feature Branch**: `038-ch3-mdx-implementation`
**Created**: 2025-01-27
**Status**: Draft
**Type**: content-implementation
**Input**: User description: "Implement the full MDX file, metadata module, and scaffolding required for Chapter 3 based on the specification created in Feature 037. No real writing — only structure, placeholders, frontmatter, AI blocks, diagram comments, and Python metadata stubs."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Implements Chapter 3 Structure (Priority: P1)

As a developer, I need to implement the MDX file structure and metadata module for Chapter 3 based on Feature 037 specification, so the chapter scaffolding is ready for future content writing and AI block integration.

**Why this priority**: This establishes the structural foundation for Chapter 3. Without proper MDX structure and metadata, content writing and AI integration cannot proceed.

**Independent Test**: Can be fully tested by verifying MDX file exists with correct frontmatter, all 7 sections, all placeholders, and metadata file imports cleanly.

**Acceptance Scenarios**:

1. **Given** the MDX file is created, **When** I open `frontend/docs/chapters/chapter-3.mdx`, **Then** I see correct YAML frontmatter with title, description, sidebar_position=3, sidebar_label, and tags
2. **Given** the MDX file is created, **When** I check the sections, **Then** I see all 7 H2 sections in exact order from Feature 037: What Is Perception in Physical AI?, Types of Sensors in Robotics, Computer Vision & Depth Perception, Signal Processing Basics for AI, Feature Extraction & Interpretation, Learning Objectives, Glossary
3. **Given** the MDX file is created, **When** I search for diagram placeholders, **Then** I see exactly 4 diagram placeholders: perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline
4. **Given** the MDX file is created, **When** I search for AI-block placeholders, **Then** I see exactly 4 AI-block placeholders: ask-question (Section 1 end), generate-diagram (Section 2 middle), explain-like-i-am-10 (Section 3 middle), interactive-quiz (Section 4 end)
5. **Given** the MDX file is created, **When** I check chunk boundaries, **Then** I see `<!-- CHUNK: start -->` and `<!-- CHUNK: end -->` comments wrapping each section
6. **Given** I run `npm run build` in frontend, **When** the build completes, **Then** the MDX file compiles without errors

---

### User Story 2 - Backend System Provides Chapter 3 Metadata (Priority: P2)

As a backend developer or AI agent, I need the backend to provide Chapter 3 metadata via a Python module, so future features can programmatically access chapter information for RAG, progress tracking, or analytics.

**Why this priority**: Infrastructure for future features. Enables backend integration but isn't needed for initial structure delivery.

**Independent Test**: Can be fully tested by importing `backend/app/content/chapters/chapter_3.py` and verifying the data structure matches Feature 037 specification.

**Acceptance Scenarios**:

1. **Given** the metadata file exists, **When** I navigate to `backend/app/content/chapters/`, **Then** I see a file named `chapter_3.py`
2. **Given** the metadata file exists, **When** I import it in Python, **Then** I can access fields: `id` (int=3), `title` (str), `summary` (str with TODO), `section_count` (int=7), `sections` (list), `ai_blocks` (list), `diagram_placeholders` (list), `last_updated` (str), `difficulty_level` (str="intermediate"), `prerequisites` (list=[1,2]), `learning_outcomes` (list with TODO), `glossary_terms` (list with TODO)
3. **Given** I access the metadata, **When** I check the values, **Then** `id=3`, `title="Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"`, `section_count=7`, `ai_blocks` contains 4 items matching Feature 037, `diagram_placeholders` contains 4 items matching Feature 037
4. **Given** the metadata file exists, **When** I check for TODOs, **Then** I see TODO comments for summary, learning_outcomes, glossary_terms, and get_chapter_3_chunks() function

---

### Edge Cases

- What happens when MDX file has incorrect frontmatter format?
  - **Expected**: Docusaurus build fails with clear error message
- What happens when section_count doesn't match number of H2 sections?
  - **Expected**: Manual validation catches this; metadata should match MDX exactly
- What happens when placeholder names don't match Feature 037?
  - **Expected**: Manual validation catches this; placeholders must match specification exactly
- What happens when metadata title doesn't match MDX frontmatter title?
  - **Expected**: Manual validation catches this; titles must match exactly
- What happens when Python file has syntax errors?
  - **Expected**: Python import fails with clear error message

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: MDX File Structure

- **FR-001.1**: System MUST create or update `frontend/docs/chapters/chapter-3.mdx` with required YAML frontmatter:
  - `title`: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
  - `description`: "Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"
  - `sidebar_position`: 3
  - `sidebar_label`: "Chapter 3: Physical AI Perception Systems"
  - `tags`: ["physical-ai", "sensors", "perception", "signal-processing"]

- **FR-001.2**: System MUST add all H2 sections EXACTLY from Feature 037 specification:
  1. What Is Perception in Physical AI?
  2. Types of Sensors in Robotics
  3. Computer Vision & Depth Perception
  4. Signal Processing Basics for AI
  5. Feature Extraction & Interpretation
  6. Learning Objectives
  7. Glossary

- **FR-001.3**: System MUST add AI-block placeholders in correct sections:
  - Section 1: `<!-- AI-BLOCK: ask-question -->` at the end
  - Section 2: `<!-- AI-BLOCK: generate-diagram -->` in the middle
  - Section 3: `<!-- AI-BLOCK: explain-like-i-am-10 -->` in the middle
  - Section 4: `<!-- AI-BLOCK: interactive-quiz -->` at the end

- **FR-001.4**: System MUST add diagram placeholders in correct sections:
  - Section 1: `<!-- DIAGRAM: perception-overview -->` in the middle
  - Section 2: `<!-- DIAGRAM: sensor-types -->` in the middle
  - Section 3: `<!-- DIAGRAM: cv-depth-flow -->` at the end
  - Section 4: `<!-- DIAGRAM: feature-extraction-pipeline -->` in the middle

- **FR-001.5**: System MUST add chunking boundary comments:
  - Each section wrapped in `<!-- CHUNK: start -->` and `<!-- CHUNK: end -->`
  - One chunk boundary pair per section

#### FR-002: Python Metadata Module

- **FR-002.1**: System MUST create or update `backend/app/content/chapters/chapter_3.py` with required fields:
  - `id`: 3 (int)
  - `title`: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)" (str)
  - `summary`: "TODO: 2-3 sentence overview" (str with TODO comment)
  - `section_count`: 7 (int)
  - `sections`: List of 7 section titles matching MDX exactly (List[str])
  - `ai_blocks`: ["ask-question", "generate-diagram", "explain-like-i-am-10", "interactive-quiz"] (List[str])
  - `diagram_placeholders`: ["perception-overview", "sensor-types", "cv-depth-flow", "feature-extraction-pipeline"] (List[str])
  - `last_updated`: ISO 8601 timestamp (str)
  - `difficulty_level`: "intermediate" (str)
  - `prerequisites`: [1, 2] (List[int])
  - `learning_outcomes`: ["TODO: 3-8 learning outcomes"] (List[str] with TODO)
  - `glossary_terms`: ["TODO: 6-10 glossary terms"] (List[str] with TODO)

- **FR-002.2**: System MUST add TODO function `get_chapter_3_chunks()` inside `chapter_3.py`:
  - Function signature: `def get_chapter_3_chunks() -> List[Dict[str, Any]]:`
  - Function body: `# TODO: Implement chunking from Chapter 3 MDX content`
  - Return placeholder: `return []`

#### FR-003: Integrity Rules

- **FR-003.1**: System MUST ensure `section_count` equals number of H2 sections in MDX (7)
- **FR-003.2**: System MUST ensure all placeholder names match Feature 037 specification exactly
- **FR-003.3**: System MUST ensure metadata `title` matches MDX frontmatter `title` exactly (character-for-character)

#### FR-004: RAG Preparation Hooks

- **FR-004.1**: System MUST add chunking boundary comments in MDX:
  - Format: `<!-- CHUNK: start -->` and `<!-- CHUNK: end -->`
  - One pair per section
  - Wraps entire section content

- **FR-004.2**: System MUST add TODO function `get_chapter_3_chunks()` in metadata file for future RAG integration

#### FR-005: Build Validation Requirements

- **FR-005.1**: MDX file MUST compile with `npm run build` in frontend directory with no warnings
- **FR-005.2**: Python file MUST import cleanly: `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"`
- **FR-005.3**: System MUST ensure no real content writing (only structure and placeholders)

---

## Non-Functional Requirements

- **NFR-001**: All placeholders MUST use HTML comment format (not React components for this feature)
- **NFR-002**: All section names MUST match Feature 037 specification exactly
- **NFR-003**: All placeholder names MUST use kebab-case naming convention
- **NFR-004**: Metadata structure MUST follow Chapter 1 and Chapter 2 patterns exactly
- **NFR-005**: No business logic added (scaffolding only)

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: MDX file created with correct frontmatter, headings, and placeholders
- **SC-002**: Metadata file created with correct schema + TODOs
- **SC-003**: All placeholders inserted exactly as defined in Feature 037
- **SC-004**: Project builds cleanly (`npm run build` succeeds)
- **SC-005**: Python file imports cleanly
- **SC-006**: No business logic added (scaffolding only)

---

## Constraints *(mandatory)*

### Technical Constraints

- **C-001**: MUST use MDX format (Markdown + JSX) compatible with Docusaurus 3.x
- **C-002**: MUST NOT implement actual diagram rendering (placeholders only)
- **C-003**: MUST NOT implement actual AI-interactive features (placeholders only)
- **C-004**: MUST NOT write actual content (structure and placeholders only)
- **C-005**: Backend metadata MUST be a simple Python file with data structures (no database, no API endpoints)
- **C-006**: MUST NOT include H3+ headings (only H2 sections allowed)

### Process Constraints

- **C-007**: MUST follow Feature 037 specification exactly
- **C-008**: MUST ensure all placeholders match Feature 037 specification
- **C-009**: MUST ensure metadata matches MDX structure exactly

### Scope Constraints (Out of Scope)

- **OOS-001**: Actual content writing
- **OOS-002**: Diagram generation
- **OOS-003**: AI block implementation
- **OOS-004**: RAG pipeline implementation
- **OOS-005**: Content validation beyond structure

---

## Dependencies *(mandatory)*

### Internal Dependencies

- **D-001**: Feature 001 (Base Project Initialization) MUST be complete
- **D-002**: Feature 037 (Chapter 3 Content Specification) MUST be complete - Source for structure and placeholders
- **D-003**: Feature 003 (Chapter 1 Content) MUST be complete - Reference for MDX structure pattern
- **D-004**: Feature 032 (Chapter 2 Content) MUST be complete - Reference for metadata pattern

### External Dependencies

- **D-005**: No new external dependencies required (scaffolding only)

### Blocking Issues

- None identified. All dependencies resolved.

### Assumptions

- **A-001**: Feature 037 specification is complete and accurate
- **A-002**: Docusaurus frontend is functional
- **A-003**: Python backend environment is functional
- **A-004**: Existing Chapter 3 MDX file can be updated (not replaced)

---

## Implementation Notes *(optional guidance)*

### Recommended Implementation Order

1. **Phase 1: MDX File Structure**
   - Update frontmatter to match Feature 037
   - Update all 7 sections to match Feature 037 exactly
   - Add diagram placeholders in correct positions
   - Add AI-block placeholders in correct positions
   - Add chunk boundaries

2. **Phase 2: Metadata Module**
   - Update metadata dictionary with all required fields
   - Add TODO placeholders for summary, learning_outcomes, glossary_terms
   - Add get_chapter_3_chunks() function with TODO

3. **Phase 3: Validation**
   - Verify MDX compiles
   - Verify Python imports
   - Verify placeholder counts match Feature 037
   - Verify section count matches

---

**Next Steps**: Proceed to `/sp.plan` to create architectural plan for MDX and metadata implementation.

