# Feature Specification: Chapter 3 — Planning Layer (Content Architecture, Metadata, Validation, RAG-Prep)

**Feature Branch**: `018-chapter-3-plan`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "Produce the full specification for Chapter 3's implementation foundation. This spec defines MDX structure requirements, section rules, diagram + AI-block placement rules, metadata schema requirements, chunking strategy for future RAG integration, and validation and success criteria."

**Note**: Feature 017-chapter-3-content has already been completed and implemented. This specification (Feature 018) provides an alternative planning layer perspective with different diagram naming conventions and chunk marker requirements.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Content Architect Defines Chapter 3 Planning Layer (Priority: P1)

As a content architect, I need a complete planning layer specification for Chapter 3 that defines content architecture, metadata requirements, validation rules, and RAG preparation strategy, so I can ensure consistent implementation across all Chapter 3 components.

**Why this priority**: This establishes the planning foundation for Chapter 3. Without proper planning layer specification, implementation may be inconsistent and may not properly integrate with RAG and validation systems.

**Independent Test**: Can be fully tested by verifying all required files exist at specified paths, spec defines all architecture requirements, contracts follow templates, and validation rules are clearly documented.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `specs/018-chapter-3-plan/spec.md`, **Then** I see:
   - Complete MDX structure requirements (7 H2 sections, 4 diagrams, 4 AI-blocks)
   - Section rules (paragraph rules, reading level, frontmatter fields)
   - Diagram placement rules (4 diagram placeholders with specific names)
   - AI-block placement rules (4 AI-block placeholders as HTML comments)
   - Chunk marker requirements (CHUNK: START / CHUNK: END markers)
   - Metadata schema requirements (Python dictionary structure)
   - Chunking strategy definition (section-based logical chunks)
   - Validation requirements (MDX compile, metadata import, placeholder validation)
   - Success criteria clearly defined

2. **Given** the feature is implemented, **When** I check `specs/018-chapter-3-plan/contracts/content-schema.md`, **Then** I see:
   - MDX frontmatter schema with validation rules
   - Python metadata schema with field specifications
   - Diagram placeholder schema (4 placeholders: perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
   - AI-block placeholder schema (4 placeholders as HTML comments)
   - Chunk marker schema (CHUNK: START / CHUNK: END)
   - Validation rules for all placeholders

3. **Given** the feature is implemented, **When** I check `specs/018-chapter-3-plan/checklists/requirements.md`, **Then** I see:
   - Content quality checklist
   - Structure validation checklist
   - Placeholder validation checklist
   - RAG preparation checklist

4. **Given** the feature is implemented, **When** I check `specs/018-chapter-3-plan/research.md`, **Then** I see:
   - Content writing style guidelines (Grade 7-8, 3-4 sentences per paragraph)
   - Diagram placement strategy
   - AI-block placement strategy
   - Chunking strategy documentation
   - RAG integration planning

5. **Given** the feature is implemented, **When** I check `specs/018-chapter-3-plan/data-model.md`, **Then** I see:
   - Entity definitions (Chapter Content, Section, Metadata, Chunk Markers, etc.)
   - Data relationships diagram
   - Chunking strategy data model
   - Validation rules

---

### User Story 2 - System Validator Uses Planning Layer Specification (Priority: P2)

As a system validator, I need contracts and schemas that define validation rules for Chapter 3 planning layer, so I can ensure content quality and consistency before implementation.

**Why this priority**: Important for maintaining content quality, but not critical for initial specification. Validation can be added incrementally.

**Independent Test**: Can be fully tested by checking contract files exist, schemas define validation rules, and checklists provide quality criteria.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `specs/018-chapter-3-plan/contracts/content-schema.md`, **Then** I see:
   - MDX frontmatter schema with validation rules
   - Chapter metadata schema (Python) with field specifications
   - Diagram placeholder schema with naming conventions
   - AI-block placeholder schema (HTML comment format)
   - Chunk marker schema
   - Validation rules for all components

2. **Given** the feature is implemented, **When** I check `specs/018-chapter-3-plan/checklists/requirements.md`, **Then** I see:
   - Content quality checklist
   - Structure validation checklist
   - Placeholder validation checklist
   - Chunk marker validation checklist

---

### User Story 3 - Future Developer Uses Planning Layer for Implementation (Priority: P3)

As a future developer, I need clear planning layer specification, chunking strategy, and RAG preparation guidelines documented in contracts and research files, so I can implement Chapter 3 following established patterns and integrate with RAG system.

**Why this priority**: Important for maintainability and developer experience, but not critical for initial specification. Guidelines can be refined during implementation.

**Independent Test**: Can be fully tested by reviewing research.md for planning guidelines, quickstart.md for implementation steps, and data-model.md for entity definitions.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I review `specs/018-chapter-3-plan/research.md`, **Then** I see:
   - Content writing style guidelines (Grade 7-8, 3-4 sentences per paragraph)
   - Diagram placement strategy
   - AI-block placement strategy (HTML comment format)
   - Chunking strategy (section-based logical chunks)
   - Chunk marker placement strategy
   - RAG integration planning

2. **Given** the feature is implemented, **When** I review `specs/018-chapter-3-plan/quickstart.md`, **Then** I see:
   - Step-by-step implementation guide
   - Chunk marker placement instructions
   - RAG preparation steps
   - Validation steps

---

## Functional Requirements

### FR1: MDX Content Requirements

**Requirement**: Define complete MDX structure requirements for Chapter 3.

**Details**:
- **Exactly 7 H2 sections** in correct order:
  1. What Is Perception in Physical AI?
  2. Types of Sensors in Robotics
  3. Computer Vision & Depth Perception
  4. Signal Processing Basics for AI
  5. Feature Extraction & Interpretation
  6. Learning Objectives
  7. Glossary
- **Strict paragraph rules**: 3-4 sentences per paragraph, 15-20 words per sentence
- **Reading level**: Grade 7-8
- **Frontmatter fields**:
  - `title`: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
  - `description`: SEO-optimized summary
  - `sidebar_position`: 3
  - `sidebar_label`: "Chapter 3: Physical AI Perception Systems"
  - `tags`: ["physical-ai", "sensors", "perception", "signal-processing"]
- **Exactly 4 DIAGRAM placeholders** (HTML comments):
  - `<!-- DIAGRAM: perception-overview -->`
  - `<!-- DIAGRAM: sensor-types -->`
  - `<!-- DIAGRAM: cv-depth-flow -->`
  - `<!-- DIAGRAM: feature-extraction-pipeline -->`
- **Exactly 4 AI-BLOCK placeholders** (HTML comments):
  - `<!-- AI-BLOCK: ask-question -->`
  - `<!-- AI-BLOCK: explain-like-i-am-10 -->`
  - `<!-- AI-BLOCK: interactive-quiz -->`
  - `<!-- AI-BLOCK: generate-diagram -->`
- **Chunk markers for RAG preparation**:
  - `<!-- CHUNK: START -->` at beginning of logical chunks
  - `<!-- CHUNK: END -->` at end of logical chunks
  - Chunk markers align with concept boundaries

**Acceptance Criteria**:
- All MDX structure requirements clearly defined
- Diagram placeholder names specified (kebab-case)
- AI-block placeholder format specified (HTML comments)
- Chunk marker format specified
- Section order matches syllabus order

---

### FR2: Metadata (Python) Requirements

**Requirement**: Define complete Python metadata schema requirements for Chapter 3.

**Details**:
- **Required fields**:
  - `id`: 3
  - `title`: Must match MDX frontmatter exactly
  - `summary`: Placeholder (2-3 sentence overview)
  - `section_count`: 7
  - `sections[]`: List of 7 section titles matching MDX order
  - `ai_blocks[]`: List of 4 items (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
  - `diagram_placeholders[]`: List of 4 items (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
  - `difficulty_level`: "intermediate"
  - `prerequisites`: [1, 2]
  - `learning_outcomes[]`: Placeholder list (3-8 items)
  - `glossary_terms[]`: Placeholder list (7 items)
  - `last_updated`: ISO 8601 timestamp placeholder
- **TODO comments required**:
  - Writing actual summary
  - Finalizing learning outcomes
  - Adding glossary terms
  - RAG embedding integration

**Acceptance Criteria**:
- All metadata fields clearly defined
- Field types and constraints specified
- TODO comment requirements documented
- Validation rules specified

---

### FR3: Chunking + RAG Prep Requirements

**Requirement**: Define chunking strategy and RAG preparation requirements for Chapter 3.

**Details**:
- **Chunking strategy**:
  - Section-based logical chunks
  - Chunk markers align with concept boundaries
  - Respect H2 section boundaries
  - Semantic segmentation by concept
- **RAG integration planning**:
  - How Chapter 3 chunks will integrate with embedding pipeline (Feature 020)
  - Qdrant upsert strategy
  - Retrieval context format
  - Chunk metadata structure
- **No real embedding logic**: Specification only, no implementation

**Acceptance Criteria**:
- Chunking strategy clearly defined
- Chunk marker placement rules specified
- RAG integration points documented
- Future embedding pipeline integration planned

---

### FR4: Validation Requirements

**Requirement**: Define validation requirements for Chapter 3 planning layer.

**Details**:
- **MDX validation**:
  - MDX must compile in Docusaurus with zero warnings
  - All frontmatter fields must be valid YAML
  - Section order must match syllabus order
- **Metadata validation**:
  - Metadata must import successfully in Python
  - All required fields must be present
  - Field types must match specifications
- **Placeholder validation**:
  - AI-BLOCK types must match allowed list (ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram)
  - DIAGRAM names must follow kebab-case
  - Glossary must contain exactly 7 items
  - Chunk markers must be properly paired (START/END)

**Acceptance Criteria**:
- All validation requirements clearly defined
- Validation rules for each component specified
- Success criteria for validation documented

---

### FR5: Contracts + Checklists Requirements

**Requirement**: Auto-generate contract files and checklists following templates.

**Details**:
- **Required files**:
  - `contracts/content-schema.md`: MDX frontmatter schema, Python schema, placeholder schemas, validation rules
  - `checklists/requirements.md`: Content quality checklist, structure validation checklist, placeholder validation checklist
  - `research.md`: Content writing guidelines, diagram placement strategy, AI-block placement strategy, chunking strategy, RAG integration planning
  - `quickstart.md`: Step-by-step implementation guide, chunk marker placement, RAG preparation steps
  - `data-model.md`: Entity definitions, data relationships, chunking strategy data model, validation rules
- **Template requirements**:
  - Auto-mdx-frontmatter
  - Auto-python-schema
  - Auto-placeholders
  - Auto-validation-rules
  - Auto-context
  - Auto-references
  - Auto-observations

**Acceptance Criteria**:
- All contract files exist and follow templates
- All documentation files exist with relevant content
- Templates properly filled with Chapter 3-specific information

---

## Writing Style Constraints

### Reading Level
- **Target**: Grade 7-8 reading level
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
- **Match course outline**: Content must align with official syllabus
- **Use analogies**: Sensors as "eyes and ears", signal processing as "filtering noise", etc.

---

## Edge Cases & Error Handling

### EC1: Section Count Mismatch
**Scenario**: MDX has different number of sections than metadata.
**Handling**: Validation step must catch this and report error. Metadata `section_count` must match actual H2 count in MDX (7).

### EC2: Placeholder Naming Inconsistency
**Scenario**: Diagram placeholders don't use kebab-case or don't match specified names.
**Handling**: Validation step must catch this and report error. All placeholders must use kebab-case and match specified names exactly.

### EC3: Missing Chunk Markers
**Scenario**: Chunk markers are not properly paired (START without END, or vice versa).
**Handling**: Validation step must catch this and report error. All chunk markers must be properly paired.

### EC4: AI-BLOCK Format Mismatch
**Scenario**: AI-block placeholders don't use HTML comment format.
**Handling**: Validation step must catch this and report error. All AI-block placeholders must use `<!-- AI-BLOCK: type -->` format.

---

## Assumptions & Dependencies

### Assumptions
1. Chapter 1 and Chapter 2 are complete and available as prerequisites
2. Official syllabus provides sufficient detail for Chapter 3 content structure
3. Writing style guidelines from Chapter 1 and Chapter 2 apply to Chapter 3
4. RAG pipeline will be implemented in Feature 020
5. Embedding pipeline will be implemented in Feature 020
6. Qdrant integration will be implemented in Feature 020

### Dependencies
1. **Feature 003**: Chapter 1 Content (template pattern reference)
2. **Feature 010**: Chapter 2 Content (template pattern reference)
3. **Feature 017**: Chapter 3 Content (already implemented - note differences in diagram names and AI-block format)
4. **Feature 020**: Embedding Pipeline (future dependency for RAG integration)
5. **Frontend**: Docusaurus MDX support
6. **Backend**: Python 3.9+, FastAPI structure

---

## Success Criteria

1. ✅ spec.md fully defines Chapter 3 architecture with no missing fields
2. ✅ All placeholders, metadata, and structure rules included
3. ✅ No implementation details (architecture only)
4. ✅ Chunking strategy clearly defined
5. ✅ RAG integration points documented
6. ✅ Validation requirements clearly specified
7. ✅ All contract files generated following templates
8. ✅ Output ready for /sp.plan phase

---

## Out of Scope

1. **Actual content writing**: This feature only creates planning layer specification
2. **RAG implementation**: RAG pipeline implementation is out of scope (Feature 020)
3. **Embedding implementation**: Embedding pipeline implementation is out of scope (Feature 020)
4. **AI runtime implementation**: AI block runtime logic is out of scope
5. **Diagram generation**: Diagram generation logic is out of scope
6. **Content validation**: Content quality validation is out of scope (only structure validation)

---

## Acceptance Criteria

1. **Specification Complete**: spec.md fully defines Chapter 3 architecture with no missing fields
2. **Placeholders Defined**: All placeholders (diagrams, AI-blocks, chunk markers) clearly defined
3. **Metadata Defined**: All metadata fields and validation rules clearly defined
4. **Chunking Strategy Defined**: Chunking strategy and RAG integration points clearly documented
5. **Contracts Complete**: All contract files exist and follow templates
6. **Validation Ready**: Validation requirements clearly specified and ready for implementation

---

## Notes

- This feature provides a planning layer specification for Chapter 3
- Feature 017-chapter-3-content has already been completed with different diagram names and React component format for AI-blocks
- This specification (Feature 018) uses HTML comment format for AI-blocks and different diagram names
- Chunk markers (CHUNK: START / CHUNK: END) are required for RAG preparation
- Focus on Physical AI perception systems: sensors, vision, signal processing, feature extraction
- Content must be accessible to Grade 7-8 reading level while covering advanced concepts
- All placeholders must use consistent naming conventions (kebab-case for diagrams, HTML comments for AI-blocks)
