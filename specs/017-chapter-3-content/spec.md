# Feature Specification: Chapter 3 Written Content — Structure, Metadata, Schema & Contracts

**Feature Branch**: `017-chapter-3-content`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "Define the full content specification for Chapter 3 based on the course outline. This chapter covers perception systems in Physical AI: sensors, vision, motion tracking, LiDAR, signal processing fundamentals, feature extraction, noise filtering, and how perception enables autonomous decision-making."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Content Developer Creates Chapter 3 Structure (Priority: P1)

As a content developer, I need a complete Chapter 3 content framework with MDX skeleton, metadata schema, and contracts, so I can write the actual content following the established structure and validation rules.

**Why this priority**: This establishes the foundation for Chapter 3 content. Without proper structure and contracts, content writing will be inconsistent and may not integrate properly with the AI blocks and RAG system.

**Independent Test**: Can be fully tested by verifying all required files exist at specified paths, MDX file has correct structure (7 H2 sections, 4 AI blocks, 4 diagrams, glossary), metadata file imports without errors, and contracts follow templates.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `frontend/docs/chapters/chapter-3.mdx`, **Then** I see:
   - YAML frontmatter with placeholder fields (title, description, sidebar_position=3, sidebar_label, tags)
   - Exactly 7 H2 sections:
     1. What Is Perception in Physical AI?
     2. Types of Sensors in Robotics
     3. Computer Vision & Depth Perception
     4. Signal Processing Basics for AI
     5. Feature Extraction & Interpretation
     6. Learning Objectives
     7. Glossary
   - 4 AI-block placeholders (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
   - 4 diagram placeholders using kebab-case:
     - physical-ai-sensing-overview
     - sensor-categories-diagram
     - depth-perception-flow
     - signal-processing-pipeline
   - Glossary section with 7 placeholder items
   - No actual content text (only placeholders)

2. **Given** the feature is implemented, **When** I check `backend/app/content/chapters/chapter_3.py`, **Then** I see:
   - `id: 3`
   - `title: placeholder` (matches MDX frontmatter)
   - `summary: placeholder`
   - `section_count: 7`
   - `sections: placeholder array` (7 items matching MDX exactly)
   - `ai_blocks: 4 placeholder entries`
   - `diagram_placeholders: 4 placeholder entries`
   - `difficulty_level: "intermediate"`
   - `prerequisites: [1, 2]`
   - `learning_outcomes: placeholder list` (3-8 items)
   - `glossary_terms: placeholder list` (7 items)
   - `last_updated: placeholder timestamp`

3. **Given** the feature is implemented, **When** I check `backend/app/content/chapters/chapter_3_chunks.py`, **Then** I see:
   - Function `get_chapter_chunks()` that returns `["TODO: chunk 1", "TODO: chunk 2"]`

4. **Given** the feature is implemented, **When** I check `specs/017-chapter-3-content/contracts/`, **Then** I see:
   - `content-schema.md` following template from global agent config
   - `checklists/requirements.md` following template

5. **Given** the feature is implemented, **When** I check `specs/017-chapter-3-content/`, **Then** I see:
   - `research.md` documenting content writing guidelines
   - `quickstart.md` with implementation guide
   - `data-model.md` with entity definitions

---

### User Story 2 - System Validates Chapter 3 Structure (Priority: P2)

As a system validator, I need contracts and schemas that define validation rules for Chapter 3 content, so I can ensure content quality and consistency before publishing.

**Why this priority**: Important for maintaining content quality, but not critical for initial scaffolding. Validation can be added incrementally.

**Independent Test**: Can be fully tested by checking contract files exist, schemas define validation rules, and checklists provide quality criteria.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `specs/017-chapter-3-content/contracts/content-schema.md`, **Then** I see:
   - MDX frontmatter schema with validation rules
   - Chapter metadata schema (Python) with field specifications
   - Glossary schema with validation rules
   - AI-block placeholder schema
   - Diagram placeholder schema

2. **Given** the feature is implemented, **When** I check `specs/017-chapter-3-content/checklists/requirements.md`, **Then** I see:
   - Content quality checklist
   - Structure validation checklist
   - Placeholder validation checklist

---

### User Story 3 - Future Content Writer Uses Chapter 3 Framework (Priority: P3)

As a future content writer, I need clear structure, placeholders, and writing guidelines documented in contracts and research files, so I can write Chapter 3 content that follows established patterns and integrates with AI blocks.

**Why this priority**: Important for maintainability and developer experience, but not critical for initial scaffolding. Guidelines can be refined during content writing.

**Independent Test**: Can be fully tested by reviewing research.md for writing guidelines, quickstart.md for implementation steps, and data-model.md for entity definitions.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I review `specs/017-chapter-3-content/research.md`, **Then** I see:
   - Content writing style guidelines (7th-8th grade level)
   - AI-block placement strategy
   - Diagram placement strategy
   - Glossary writing guidelines
   - Physical AI perception systems writing guidelines

2. **Given** the feature is implemented, **When** I review `specs/017-chapter-3-content/quickstart.md`, **Then** I see:
   - Step-by-step implementation guide
   - File creation instructions
   - Validation steps

---

## Functional Requirements

### FR1: MDX Chapter File Structure

**Requirement**: Create `frontend/docs/chapters/chapter-3.mdx` with complete structure scaffolding.

**Details**:
- YAML frontmatter:
  - `title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"`
  - `description: placeholder` (2-3 sentence overview)
  - `sidebar_position: 3`
  - `sidebar_label: "Chapter 3: Physical AI Perception Systems"`
  - `tags: ["physical-ai", "sensors", "perception", "signal-processing"]`
- Exactly 7 H2 sections (no H3 or other levels in scaffolding):
  1. `## What Is Perception in Physical AI? {#what-is-perception-in-physical-ai}`
  2. `## Types of Sensors in Robotics {#types-of-sensors-in-robotics}`
  3. `## Computer Vision & Depth Perception {#computer-vision-depth-perception}`
  4. `## Signal Processing Basics for AI {#signal-processing-basics-for-ai}`
  5. `## Feature Extraction & Interpretation {#feature-extraction-interpretation}`
  6. `## Learning Objectives {#learning-objectives}`
  7. `## Glossary {#glossary}`
- 4 diagram placeholders (HTML comments):
  - `<!-- DIAGRAM: physical-ai-sensing-overview -->`
  - `<!-- DIAGRAM: sensor-categories-diagram -->`
  - `<!-- DIAGRAM: depth-perception-flow -->`
  - `<!-- DIAGRAM: signal-processing-pipeline -->`
- 4 AI-block React components:
  - `<AskQuestionBlock chapterId={3} sectionId="..." />`
  - `<ExplainLike10Block concept="..." chapterId={3} />`
  - `<InteractiveQuizBlock chapterId={3} numQuestions={5} />`
  - `<GenerateDiagramBlock diagramType="..." chapterId={3} />`
- Glossary section with 7 placeholder terms:
  - Perception
  - Sensor
  - Computer Vision
  - Depth Perception
  - Signal Processing
  - Feature Extraction
  - LiDAR (or alternative term)
- All content is placeholder comments (no actual text)

**Acceptance Criteria**:
- MDX file compiles without errors
- Exactly 7 H2 sections verified
- 4 diagram placeholders verified
- 4 AI-block components verified
- 7 glossary terms verified
- Frontmatter complete and valid

---

### FR2: Backend Chapter Metadata

**Requirement**: Create `backend/app/content/chapters/chapter_3.py` with `CHAPTER_METADATA` dictionary.

**Details**:
- Core identification:
  - `id: 3`
  - `title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"` (exact match to MDX)
  - `summary: placeholder` (2-3 sentence overview)
- Structure information:
  - `section_count: 7`
  - `sections: ["What Is Perception in Physical AI?", "Types of Sensors in Robotics", "Computer Vision & Depth Perception", "Signal Processing Basics for AI", "Feature Extraction & Interpretation", "Learning Objectives", "Glossary"]`
- Placeholder tracking:
  - `ai_blocks: ["ask-question", "explain-like-i-am-10", "interactive-quiz", "generate-diagram"]`
  - `diagram_placeholders: ["physical-ai-sensing-overview", "sensor-categories-diagram", "depth-perception-flow", "signal-processing-pipeline"]`
- Versioning:
  - `last_updated: "2025-12-05T00:00:00Z"`
- RAG-specific metadata:
  - `difficulty_level: "intermediate"`
  - `prerequisites: [1, 2]` (Chapters 1 and 2 are prerequisites)
  - `learning_outcomes: placeholder list` (3-8 items covering perception, sensors, vision, signal processing, feature extraction)
  - `glossary_terms: placeholder list` (7 items matching MDX glossary)

**Acceptance Criteria**:
- Python file imports without errors
- All required fields present
- `section_count` matches MDX (7)
- `sections` list matches MDX exactly
- `ai_blocks` count matches MDX (4)
- `diagram_placeholders` count matches MDX (4)
- `glossary_terms` count matches MDX (7)
- `difficulty_level` is "intermediate"
- `prerequisites` is [1, 2]

---

### FR3: RAG Chunk File Scaffold

**Requirement**: Create `backend/app/content/chapters/chapter_3_chunks.py` with placeholder function.

**Details**:
- Function signature: `get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]`
- Return type: `List[Dict[str, Any]]`
- Placeholder return: `[]` (empty list)
- TODO comments for future implementation:
  - Load Chapter 3 MDX content
  - Chunk content by section
  - Generate embeddings
  - Store in Qdrant collection "chapter_3"

**Acceptance Criteria**:
- File exists at specified path
- Function exists with correct signature
- Function imports without errors
- Return type annotation is correct

---

### FR4: Contracts & Documentation

**Requirement**: Create specification contracts and documentation files.

**Details**:
- `specs/017-chapter-3-content/contracts/content-schema.md`:
  - MDX frontmatter schema
  - Chapter metadata schema (Python)
  - Glossary schema
  - AI-block placeholder schema
  - Diagram placeholder schema
- `specs/017-chapter-3-content/checklists/requirements.md`:
  - Content quality checklist
  - Structure validation checklist
  - Placeholder validation checklist
- `specs/017-chapter-3-content/research.md`:
  - Content writing style guidelines (7th-8th grade level)
  - AI-block placement strategy
  - Diagram placement strategy
  - Glossary writing guidelines
  - Physical AI perception systems writing guidelines
- `specs/017-chapter-3-content/data-model.md`:
  - Entity definitions (ChapterMetadata, Section, GlossaryTerm, etc.)
  - Data relationships
  - Validation rules
- `specs/017-chapter-3-content/quickstart.md`:
  - Step-by-step implementation guide
  - File creation instructions
  - Validation steps

**Acceptance Criteria**:
- All contract files exist
- All documentation files exist
- Files follow templates from previous features
- Content is relevant to Chapter 3

---

## Writing Style Constraints

### Reading Level
- **Target**: 7th-8th grade reading level
- **Sentence length**: 15-20 words per sentence
- **Paragraph length**: 3-4 sentences per paragraph
- **Vocabulary**: Define all technical terms clearly on first use

### Tone & Style
- **Tone**: Conversational-educational
- **Approach**: Use analogies and simplified examples
- **Examples**: Real-world Physical AI applications (autonomous vehicles, robotics, drones)
- **Technical terms**: Define clearly with analogies when possible

### Content Guidelines
- **No implementation details**: Focus on concepts, not code
- **No RAG or AI runtime references**: Keep content focused on Physical AI perception
- **No code examples**: Text-only chapter
- **Match course outline**: Content must align with course outline PDF
- **Use analogies**: Sensors as "eyes and ears", signal processing as "filtering noise", etc.

---

## Edge Cases & Error Handling

### EC1: Section Count Mismatch
**Scenario**: MDX has different number of sections than metadata.
**Handling**: Validation step must catch this and report error. Metadata `section_count` must match actual H2 count in MDX.

### EC2: Placeholder Mismatch
**Scenario**: Diagram placeholders in MDX don't match metadata `diagram_placeholders` list.
**Handling**: Validation step must catch this and report error. All placeholders must match exactly.

### EC3: Missing Glossary Terms
**Scenario**: Glossary section has fewer than 7 terms.
**Handling**: Validation step must catch this and report error. Exactly 7 glossary terms required.

### EC4: Invalid Frontmatter
**Scenario**: MDX frontmatter is missing required fields or has invalid values.
**Handling**: Docusaurus build will fail. Validation step should catch this before build.

---

## Assumptions & Dependencies

### Assumptions
1. Chapter 1 and Chapter 2 are complete and available as prerequisites
2. Course outline PDF provides sufficient detail for Chapter 3 content structure
3. Writing style guidelines from Chapter 1 and Chapter 2 apply to Chapter 3
4. AI-block components from Chapter 1 and Chapter 2 work with Chapter 3
5. RAG pipeline will be implemented in future features
6. Diagram generation will be implemented in future features

### Dependencies
1. **Feature 010**: Chapter 2 content structure (for pattern reference)
2. **Feature 014**: Chapter 2 content framework (for pattern reference)
3. **Frontend**: Docusaurus MDX support, React components for AI blocks
4. **Backend**: Python 3.9+, FastAPI structure
5. **Templates**: Content schema template, checklist template from previous features

---

## Success Criteria

1. ✅ MDX file exists with correct structure (7 sections, 4 diagrams, 4 AI blocks, 7 glossary terms)
2. ✅ Metadata file exists with all required fields matching MDX
3. ✅ Chunk file exists with placeholder function
4. ✅ All contract files exist and follow templates
5. ✅ All documentation files exist
6. ✅ Structure validation passes (section count, placeholders, glossary terms)
7. ✅ Metadata validation passes (all fields present, correct types, matches MDX)
8. ✅ Ready for planning phase (`/sp.plan`)

---

## Out of Scope

1. **Actual content writing**: This feature only creates structure and placeholders
2. **RAG implementation**: RAG pipeline implementation is out of scope
3. **AI runtime implementation**: AI block runtime logic is out of scope
4. **Diagram generation**: Diagram generation logic is out of scope
5. **Content validation**: Content quality validation is out of scope (only structure validation)
6. **Integration testing**: Integration with AI blocks and RAG is out of scope

---

## Acceptance Criteria

1. **Structure Complete**: MDX file has exactly 7 H2 sections, 4 diagram placeholders, 4 AI-block components, 7 glossary terms
2. **Metadata Complete**: Python metadata file has all required fields with correct values matching MDX
3. **Contracts Complete**: All contract files exist and follow templates
4. **Documentation Complete**: All documentation files exist with relevant content
5. **Validation Ready**: Structure can be validated against contracts and schemas

---

## Notes

- This feature follows the same pattern as Feature 014 (Chapter 2 content framework)
- Chapter 3 is intermediate difficulty, requiring Chapters 1 and 2 as prerequisites
- Focus on Physical AI perception systems: sensors, vision, signal processing, feature extraction
- Content must be accessible to 7th-8th grade reading level while covering advanced concepts
- All placeholders must use consistent naming conventions (kebab-case for diagrams, camelCase for section IDs)
