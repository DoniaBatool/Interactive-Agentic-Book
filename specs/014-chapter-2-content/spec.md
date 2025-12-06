# Feature Specification: Chapter 2 Written Content — Structure, Metadata, Schema & Contracts

**Feature Branch**: `014-chapter-2-content`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "Establish the complete Chapter 2 content framework: MDX structure, placeholders, metadata schema, glossary items, AI-block markers, diagram placeholders, and backend metadata file. NO real text content should be written—only structure."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Content Developer Creates Chapter 2 Structure (Priority: P1)

As a content developer, I need a complete Chapter 2 content framework with MDX skeleton, metadata schema, and contracts, so I can write the actual content following the established structure and validation rules.

**Why this priority**: This establishes the foundation for Chapter 2 content. Without proper structure and contracts, content writing will be inconsistent and may not integrate properly with the AI blocks and RAG system.

**Independent Test**: Can be fully tested by verifying all required files exist at specified paths, MDX file has correct structure (7 H2 sections, 4 AI blocks, 4 diagrams, glossary), metadata file imports without errors, and contracts follow templates.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `frontend/docs/chapters/chapter-2.mdx`, **Then** I see:
   - YAML frontmatter with placeholder fields
   - Exactly 7 H2 sections
   - 4 AI-block placeholders (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
   - 4 diagram placeholders using kebab-case
   - Glossary section with 7 placeholder items
   - No actual content text (only placeholders)

2. **Given** the feature is implemented, **When** I check `backend/app/content/chapters/chapter_2.py`, **Then** I see:
   - `id: 2`
   - `title: placeholder` (matches MDX frontmatter)
   - `summary: placeholder`
   - `section_count: 7`
   - `sections: placeholder array` (7 items)
   - `ai_blocks: 4 placeholder entries`
   - `diagram_placeholders: 4 placeholder entries`
   - `difficulty_level: placeholder`
   - `prerequisites: [1]`
   - `learning_outcomes: placeholder list`
   - `glossary_terms: placeholder list` (7 items)
   - `last_updated: placeholder timestamp`

3. **Given** the feature is implemented, **When** I check `backend/app/content/chapters/chapter_2_chunks.py`, **Then** I see:
   - Function `get_chapter_chunks()` that returns `["TODO: chunk 1", "TODO: chunk 2"]`

4. **Given** the feature is implemented, **When** I check `specs/014-chapter-2-content/contracts/`, **Then** I see:
   - `content-schema.md` following template from global agent config
   - `checklists/requirements.md` following template

5. **Given** the feature is implemented, **When** I check `specs/014-chapter-2-content/`, **Then** I see:
   - `research.md` documenting content writing guidelines
   - `quickstart.md` with implementation guide
   - `data-model.md` with entity definitions

---

### User Story 2 - System Validates Chapter 2 Structure (Priority: P2)

As a system validator, I need contracts and schemas that define validation rules for Chapter 2 content, so I can ensure content quality and consistency before publishing.

**Why this priority**: Important for maintaining content quality, but not critical for initial scaffolding. Validation can be added incrementally.

**Independent Test**: Can be fully tested by checking contract files exist, schemas define validation rules, and checklists provide quality criteria.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `specs/014-chapter-2-content/contracts/content-schema.md`, **Then** I see:
   - MDX frontmatter schema with validation rules
   - Chapter metadata schema (Python) with field specifications
   - Glossary schema with validation rules
   - AI-block placeholder schema
   - Diagram placeholder schema

2. **Given** the feature is implemented, **When** I check `specs/014-chapter-2-content/checklists/requirements.md`, **Then** I see:
   - Content quality checklist
   - Structure validation checklist
   - Placeholder validation checklist

---

### User Story 3 - Future Content Writer Uses Chapter 2 Framework (Priority: P3)

As a future content writer, I need clear structure, placeholders, and writing guidelines documented in contracts and research files, so I can write Chapter 2 content that follows established patterns and integrates with AI blocks.

**Why this priority**: Important for maintainability and developer experience, but not critical for initial scaffolding. Guidelines can be refined during content writing.

**Independent Test**: Can be fully tested by reviewing research.md for writing guidelines, quickstart.md for implementation steps, and data-model.md for entity definitions.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I review `specs/014-chapter-2-content/research.md`, **Then** I see:
   - Content writing style guidelines (7th-8th grade level)
   - AI-block placement strategy
   - Diagram placement strategy
   - Glossary writing guidelines

2. **Given** the feature is implemented, **When** I review `specs/014-chapter-2-content/quickstart.md`, **Then** I see:
   - Step-by-step implementation guide
   - File creation instructions
   - Validation steps

---

### Edge Cases

- What happens when MDX file has incorrect number of sections?
  - Validation should catch this during build or manual review
- What happens when metadata file has mismatched section_count?
  - Backend validation should raise error on import
- What happens when glossary has incorrect number of terms?
  - Contract validation should flag this
- What happens when AI-block placeholders use invalid types?
  - Schema validation should reject invalid types
- What happens when diagram placeholders don't use kebab-case?
  - Schema validation should enforce naming convention

## Requirements *(mandatory)*

### Functional Requirements

#### MDX Skeleton Creation

- **FR-001**: System MUST create `frontend/docs/chapters/chapter-2.mdx` with:
  - YAML frontmatter containing placeholder fields:
    - `title: placeholder` (pattern: "Chapter 2 — Title")
    - `description: placeholder` (10-250 characters)
    - `sidebar_position: 2`
    - `sidebar_label: placeholder`
    - `tags: placeholder array`
  - Exactly 7 H2 sections (structure only, no content)
  - 4 AI-block placeholders:
    - `ask-question`
    - `explain-like-i-am-10`
    - `interactive-quiz`
    - `generate-diagram`
  - 4 diagram placeholders using kebab-case naming
  - 1 glossary section with 7 placeholder items
  - No actual content text (only placeholder comments)

#### Backend Metadata Creation

- **FR-002**: System MUST create `backend/app/content/chapters/chapter_2.py` with:
  - `id: 2`
  - `title: placeholder` (must match MDX frontmatter)
  - `summary: placeholder` (2-3 sentences, 50-300 characters)
  - `section_count: 7`
  - `sections: placeholder array` (7 section titles)
  - `ai_blocks: 4 placeholder entries` (matching MDX placeholders)
  - `diagram_placeholders: 4 placeholder entries` (matching MDX placeholders)
  - `difficulty_level: placeholder` (enum: "beginner" | "intermediate" | "advanced")
  - `prerequisites: [1]` (Chapter 1 is prerequisite)
  - `learning_outcomes: placeholder list` (3-10 items)
  - `glossary_terms: placeholder list` (7 items)
  - `last_updated: placeholder timestamp` (ISO 8601 format)

#### Chunk Source File Creation

- **FR-003**: System MUST create or verify `backend/app/content/chapters/chapter_2_chunks.py` with:
  - Function `get_chapter_chunks()` that returns placeholder list: `["TODO: chunk 1", "TODO: chunk 2"]`
  - Function signature: `def get_chapter_chunks(chapter_id: int = 2) -> List[str]:`
  - Comprehensive TODO comments for future chunking implementation

#### Contracts Creation

- **FR-004**: System MUST create `specs/014-chapter-2-content/contracts/content-schema.md`:
  - Following template from global agent config (Feature 003 pattern)
  - MDX frontmatter schema with validation rules
  - Chapter metadata schema (Python) with field specifications
  - Glossary schema with validation rules
  - AI-block placeholder schema
  - Diagram placeholder schema

- **FR-005**: System MUST create `specs/014-chapter-2-content/checklists/requirements.md`:
  - Following template from global agent config
  - Content quality checklist
  - Structure validation checklist
  - Placeholder validation checklist

#### Research and Documentation

- **FR-006**: System MUST create `specs/014-chapter-2-content/research.md`:
  - Content writing style guidelines (7th-8th grade level)
  - AI-block placement strategy for Chapter 2
  - Diagram placement strategy for Chapter 2
  - Glossary writing guidelines
  - ROS 2-specific content considerations

- **FR-007**: System MUST create `specs/014-chapter-2-content/quickstart.md`:
  - Step-by-step implementation guide
  - File creation instructions
  - Validation steps
  - Prerequisites

- **FR-008**: System MUST create `specs/014-chapter-2-content/data-model.md`:
  - Entity definitions (Chapter Content, Section, Glossary Term, etc.)
  - Relationships between entities
  - Validation rules
  - Data flow diagrams

#### Structural Constraints

- **FR-009**: System MUST ensure MDX file has exactly 7 H2 sections (not counting frontmatter or glossary as separate)
- **FR-010**: System MUST ensure glossary section contains exactly 7 placeholder items
- **FR-011**: System MUST ensure all diagram placeholders use kebab-case naming (e.g., `ros2-ecosystem-overview`)
- **FR-012**: System MUST ensure all AI-block placeholders use valid types from allowed list
- **FR-013**: System MUST ensure no actual content text is written (only placeholder comments)

#### Consistency Requirements

- **FR-014**: System MUST replicate the style of Chapter 1 scaffolding (Feature 003)
- **FR-015**: System MUST NOT copy content from Chapter 1 (only structure)
- **FR-016**: System MUST follow the course document provided for real content later (referenced but not implemented in this feature)

## Assumptions

- Chapter 1 content framework (Feature 003) exists and can be used as a template
- Docusaurus frontend structure supports MDX files in `frontend/docs/chapters/`
- Backend Python structure supports metadata files in `backend/app/content/chapters/`
- Global agent config templates exist for contracts and checklists
- Course document with real Chapter 2 content will be provided in future feature
- Chapter 2 content will be written in future feature (not this one)

## Dependencies

- **Feature 003** (Chapter 1 Content): Provides template structure and patterns
- **Feature 010** (Chapter 2 Content): May have created initial structure (to be validated/updated)
- **Feature 011** (Chapter 2 AI Blocks): May have created chunk file (to be verified)
- Docusaurus frontend: Must support MDX with frontmatter
- Python backend: Must support metadata file imports

## Success Criteria

- Chapter 2 MDX file exists with correct skeleton (7 H2 sections, 4 AI blocks, 4 diagrams, glossary)
- Metadata file imports in backend without errors
- Chunk file exists with TODO list
- Contracts folder created with correct templates (content-schema.md, checklists/requirements.md)
- Research, quickstart, and data-model files created
- All placeholders, AI-block markers, and diagrams validated
- No actual content text written (only structure and placeholders)

## Acceptance Criteria

- ✅ MDX file compiles with no errors in Docusaurus
- ✅ Metadata file imports successfully: `from app.content.chapters.chapter_2 import CHAPTER_METADATA`
- ✅ Chunk file exists with placeholder function
- ✅ All contract files follow templates from Feature 003
- ✅ Structure matches Chapter 1 pattern (7 sections, 4 AI blocks, 4 diagrams, glossary)
- ✅ All placeholders use correct naming conventions (kebab-case for diagrams, valid types for AI blocks)
- ✅ No real content text (only placeholder comments)
