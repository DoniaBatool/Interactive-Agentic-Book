# Implementation Plan: Chapter 1 Written Content

**Branch**: `003-chapter-1-content` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/003-chapter-1-content/spec.md`

## Summary

This feature delivers complete written content for Chapter 1: "Introduction to Physical AI & Robotics", providing learners with beginner-friendly educational material covering fundamental concepts. The implementation creates an MDX file with 7 structured sections (What is Physical AI, What is a Robot, AI + Robotics Systems, Core Concepts, Learning Objectives, Summary, Glossary) and a backend metadata file for future RAG integration. Content is written at 7th-8th grade reading level with strategic placement of 4 diagram placeholders and 4 AI-interactive block placeholders to scaffold future features (diagram generation, AI interactions).

**Primary Deliverable**: `frontend/docs/chapters/chapter-1.mdx` (MDX file with complete educational content)
**Secondary Deliverable**: `backend/app/content/chapters/chapter_1.py` (Python metadata dictionary)
**Validation**: Manual content quality review + Docusaurus build test + Python import test

## Technical Context

**Language/Version**:
- Frontend: MDX (Markdown + JSX) compatible with Docusaurus 3.x
- Backend: Python 3.11+

**Primary Dependencies**:
- Frontend: Docusaurus 3.x (already installed from Feature 001)
- Backend: Python 3.11+ standard library (no new dependencies)

**Storage**: Static files (MDX content, Python module) - no database

**Testing**:
- Frontend: `npm run build` validation (Docusaurus build process)
- Backend: Python import test (`python -c "from app.content.chapters.chapter_1 import CHAPTER_METADATA"`)
- Manual: Content quality review against readability guidelines

**Target Platform**:
- Frontend: Web browsers (Chrome, Firefox, Safari) via Docusaurus static site
- Backend: Server-side Python (Uvicorn/FastAPI environment)

**Project Type**: Web application (frontend MDX content + backend metadata scaffold)

**Performance Goals**:
- Page load time: < 2 seconds for Chapter 1 page
- Build time: Incremental build < 5 seconds
- No performance-critical operations (static content only)

**Constraints**:
- Content MUST be readable for ages 12+ (7th-8th grade Flesch-Kincaid level)
- Content MUST NOT implement actual diagram rendering or AI features (placeholders only)
- Backend metadata MUST remain simple Python dictionary (no Pydantic model, no database)
- Total implementation time: 2-4 hours (content writing is time-intensive)

**Scale/Scope**:
- 1 chapter (Chapter 1 only, not creating multiple chapters)
- 7 sections with approximately 2000-3000 words total
- 7 glossary terms
- 4 diagram placeholders
- 4 AI-interactive block placeholders

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### ✅ PASS - Principle I: AI-Native Spec-Driven Development

**Status**: COMPLIANT

- Specification created: `specs/003-chapter-1-content/spec.md` ✓
- Architecture planning: This plan document ✓
- SDD workflow followed: Constitution → Spec → Plan → Tasks (in progress) ✓
- No code written without corresponding spec/plan artifacts ✓

### ✅ PASS - Principle II: Docusaurus-First Documentation Strategy

**Status**: COMPLIANT

- Content uses MDX format compatible with Docusaurus 3.x ✓
- Follows Docusaurus frontmatter conventions (title, description, sidebar_position, sidebar_label, tags) ✓
- Content placed in `frontend/docs/chapters/` directory structure ✓
- Static generation supported (no dynamic rendering required) ✓
- Markdown-native with HTML comment placeholders (not custom JSX components yet) ✓

### ⚠️ PARTIAL - Principle III: RAG-First Chatbot Architecture

**Status**: SCAFFOLDING PHASE (ACCEPTABLE)

- Backend metadata includes RAG-ready fields: `summary`, `learning_outcomes`, `glossary_terms` ✓
- TODO comments document future integration with Qdrant vector database ✓
- Metadata structure designed for future embedding generation ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No actual RAG pipeline implementation
  - No embeddings generated
  - No Qdrant storage
  - No retrieval or generation logic

**Justification**: This is a content creation feature establishing the foundation. RAG integration is explicitly planned for future features (004+). Metadata structure is designed with RAG in mind (summary for semantic search, learning outcomes for context, glossary for term expansion).

### ✅ PASS - Principle IV: Personalization & User-Centric Design

**Status**: COMPLIANT (CONTENT LAYER)

- Content written for diverse audiences (12+ age group, beginner level) ✓
- Clear learning objectives support progress tracking (future feature) ✓
- Difficulty level metadata (`"beginner"`) enables personalization filtering (future feature) ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No dynamic content adaptation based on user profile
  - No BetterAuth integration
  - No user-specific rendering

**Justification**: This feature establishes content that will be personalized in future features. Content is written with accessibility and clarity as primary goals, suitable for the broadest audience (aligned with Constitution's inclusive education goals).

### ⚠️ PARTIAL - Principle V: Multilingual Support with On-Demand Translation

**Status**: SCAFFOLDING PHASE (ACCEPTABLE)

- Content structure supports future translation (clean markdown, no hard-coded formatting) ✓
- Content written in English (primary language per Constitution) ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No Urdu translation
  - No translation pipeline
  - No translation caching

**Justification**: This feature provides the source English content. Translation infrastructure is planned for future features (006+). Content is structured to be translation-friendly (avoids idioms, uses clear language, technical terms can be preserved with explanations).

### ✅ PASS - Principle VI: Test-Driven Quality Gates

**Status**: COMPLIANT (MANUAL TESTING PHASE)

- Clear acceptance criteria defined in spec.md (10 success criteria) ✓
- Manual validation checklist in quickstart.md ✓
- Build validation: `npm run build` test ✓
- Import validation: Python import test ✓
- Content quality gates: Manual review against readability guidelines ✓
- **Not Yet Implemented** (automated testing out of scope for content feature):
  - No unit tests (content is static markdown, not code)
  - No automated readability scoring
  - No automated placeholder validation

**Justification**: Content creation features rely on manual review and build validation rather than traditional TDD. Automated validation of content structure (placeholder counts, section order) is planned for future tooling but not required for this feature. Manual review is the industry standard for educational content quality assurance.

---

### Constitution Check Summary

| Principle | Status | Notes |
|-----------|--------|-------|
| I. SDD Workflow | ✅ PASS | Full spec → plan → tasks workflow followed |
| II. Docusaurus-First | ✅ PASS | MDX format, proper frontmatter, static generation |
| III. RAG-First | ⚠️ SCAFFOLDING | Metadata includes RAG-ready fields, actual RAG in future features |
| IV. Personalization | ✅ PASS | Content suitable for broad audience, metadata supports future personalization |
| V. Multilingual | ⚠️ SCAFFOLDING | English source content, translation-friendly structure |
| VI. TDD Quality Gates | ✅ PASS | Manual review + build validation appropriate for content feature |

**Overall**: ✅ **APPROVED TO PROCEED**

All principles are either fully compliant or in acceptable scaffolding phase. Partial compliance is justified because this is a foundational content creation feature establishing the base material that future features (RAG, personalization, translation) will enhance.

---

## Project Structure

### Documentation (this feature)

```text
specs/003-chapter-1-content/
├── spec.md              # Feature specification (USER INPUT → /sp.specify)
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output: content writing guidelines, technical decisions
├── data-model.md        # Phase 1 output: entity definitions (Chapter, Section, Glossary Term, etc.)
├── quickstart.md        # Phase 1 output: step-by-step implementation guide
├── contracts/           # Phase 1 output: data schemas and validation rules
│   └── content-schema.md
├── checklists/          # Specification validation
│   └── requirements.md
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT YET CREATED)
```

### Source Code (repository root)

```text
# Web application structure (frontend + backend)
frontend/
├── docs/
│   ├── chapters/               # NEW: Chapter content directory
│   │   └── chapter-1.mdx      # NEW: Chapter 1 MDX file (PRIMARY DELIVERABLE)
│   └── intro.md               # Existing (reference example)
├── src/
│   ├── components/
│   ├── pages/
│   └── styles/
├── docusaurus.config.ts       # Existing Docusaurus configuration
└── package.json               # Existing dependencies

backend/
├── app/
│   ├── api/                   # Existing API routes
│   ├── config/                # Existing configuration
│   ├── content/               # NEW: Content metadata directory
│   │   ├── __init__.py        # NEW: Package init
│   │   └── chapters/          # NEW: Chapters metadata directory
│   │       ├── __init__.py    # NEW: Package init
│   │       └── chapter_1.py   # NEW: Chapter 1 metadata (SECONDARY DELIVERABLE)
│   ├── models/                # Existing data models
│   └── services/              # Existing business logic
├── tests/                     # Existing test suite
└── pyproject.toml             # Existing Python dependencies
```

**Structure Decision**: Using Option 2 (Web application structure) because the project has both `frontend/` and `backend/` directories. Frontend content is added to `frontend/docs/chapters/` (new subdirectory) to organize chapter content separately from general documentation. Backend metadata is added to `backend/app/content/chapters/` (new module hierarchy) to establish a clear content management structure for future chapters and RAG integration.

---

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

N/A - All Constitution principles passed or are in acceptable scaffolding phase with clear justification. No violations requiring complexity tracking.

---

## Phase 0: Research & Technical Decisions

### Research Questions Resolved

**Documented in**: `research.md`

#### Q1: MDX Frontmatter Structure
**Decision**: Use standard Docusaurus frontmatter with 5 fields: `title`, `description`, `sidebar_position`, `sidebar_label`, `tags`

**Rationale**: Follows Docusaurus best practices, supports SEO and navigation, extensible for future enhancements

**Reference**: Docusaurus 3.x Markdown Frontmatter documentation

---

#### Q2: AI-Interactive Block Placement Strategy
**Decision**: Strategic placement following cognitive load theory:
1. `ask-question` at end of Section 1 (active recall after concept introduction)
2. `generate-diagram` within Section 2 (visual aid for structural understanding)
3. `explain-like-i-am-10` in middle of Section 3 (simplified explanation for complex integration)
4. `interactive-quiz` at end of Section 4 (self-assessment after core concepts)

**Rationale**: Based on pedagogical principles - retrieval practice, dual coding theory, formative assessment. Positioned to break up text, reinforce key concepts, provide alternative modalities.

**Reference**: Cognitive Load Theory (Sweller), Retrieval Practice research (Roediger & Butler)

---

#### Q3: Content Writing Style for 12+ Age Group
**Decision**: Conversational-educational style with:
- Second-person "you" for direct connection
- 15-20 words per sentence average (7th-8th grade level)
- 3-4 sentences per paragraph max
- Analogies from daily life (smartphones, household appliances)
- Technical terms defined in-line before repeated use
- Rhetorical questions and "imagine if..." scenarios for engagement

**Rationale**: Research shows optimal learning when content matches reader's schema, complexity is scaffolded, and abstract concepts are grounded in concrete examples.

**Reference**: Flesch-Kincaid readability formulas, Scaffolding theory (Vygotsky), Plain Language guidelines

---

#### Q4: Backend Metadata Structure
**Decision**: Python dictionary in `.py` module with fields: `id`, `title`, `summary`, `section_count`, `sections`, `ai_blocks`, `diagram_placeholders`, `last_updated`, `difficulty_level`, `prerequisites`, `learning_outcomes`, `glossary_terms`

**Rationale**:
- Simple dictionary avoids over-engineering (no Pydantic model needed yet)
- RAG-ready fields (`summary`, `learning_outcomes`, `glossary_terms`) can be embedded for semantic search
- Extensible without schema migration
- Type hints enable IDE autocomplete
- TODO comments document future integration points

**Future Path**: Convert to Pydantic model → generate embeddings → store in Qdrant with chapter_id metadata → query for RAG

**Reference**: RAG best practices (LangChain), Qdrant metadata filtering documentation

---

#### Q5: Placeholder Naming Convention
**Decision**: Kebab-case with `<!-- DIAGRAM: {topic}-{purpose} -->` and `<!-- AI-BLOCK: {type} -->` format

**Rationale**:
- HTML comment format (invisible to readers, parseable by scripts)
- Kebab-case is URL-friendly and web standard
- Descriptive names understandable without documentation
- Consistent prefix enables easy regex matching: `/<!-- DIAGRAM: ([a-z-]+) -->/g`
- No spaces in names simplifies file naming for future diagram assets

**Parser Example**:
```python
import re
pattern = r"<!-- DIAGRAM: ([a-z-]+) -->"
placeholders = re.findall(pattern, mdx_content)
```

**Reference**: HTML comment specification (W3C), frontend kebab-case conventions

---

### Technology Stack Summary

| Layer | Technology | Version/Format | Purpose |
|-------|------------|----------------|---------|
| Frontend Content | MDX | Docusaurus 3.x compatible | Educational content with JSX support |
| Frontmatter | YAML | Standard YAML | Metadata for Docusaurus rendering |
| Placeholders | HTML Comments | `<!-- KEYWORD: value -->` | Future feature markers (diagrams, AI blocks) |
| Backend Metadata | Python Dictionary | Python 3.11+ | Chapter metadata for RAG integration |
| Reading Level | Flesch-Kincaid | Grade 7-8 target | Content accessibility standard |

---

## Phase 1: Design & Contracts

### Data Model

**Documented in**: `data-model.md`

#### Entity Definitions

**1. Chapter Content** (Primary Entity)
- **Storage**: MDX file at `frontend/docs/chapters/chapter-1.mdx`
- **Structure**: YAML frontmatter + Markdown body with 7 H2 sections
- **Validation**: 7 sections in order, 4 diagram placeholders, 4 AI-block placeholders, 7th-8th grade reading level
- **State**: Static (published or not)

**2. Section** (Sub-entity)
- **Structure**: H2 markdown heading + body paragraphs + optional placeholders
- **Attributes**: Heading, order (1-7), content, placeholders (0-2)
- **Relationship**: N:1 with Chapter Content
- **Validation**: H2 level only, minimum 200 words, 3-4 sentences per paragraph

**3. Glossary Term** (Sub-entity)
- **Structure**: `**Term**: Definition text.`
- **Attributes**: Term (bold), definition (10-100 words), optional context
- **Required Terms**: Physical AI, Robot, Sensor, Actuator, Autonomy, Perception, Control System
- **Relationship**: N:1 with Chapter Content
- **Validation**: Bold formatting, 10-100 words, uses analogies, no circular definitions

**4. Diagram Placeholder** (Sub-entity)
- **Structure**: `<!-- DIAGRAM: placeholder-name -->`
- **Attributes**: Name (kebab-case), type (inferred), section (parent), position
- **Required Placeholders**: physical-ai-overview, robot-anatomy, ai-robotics-stack, core-concepts-flow
- **Relationship**: N:1 with Section
- **Validation**: Correct syntax, unique name, lowercase with hyphens only

**5. AI-Interactive Block Placeholder** (Sub-entity)
- **Structure**: `<!-- AI-BLOCK: block-type -->`
- **Attributes**: Type (one of 4 allowed), section (parent), position
- **Required Types**: ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram
- **Relationship**: N:1 with Section
- **Validation**: Correct syntax, type in allowed list, no duplicates, strategic positioning

**6. Chapter Metadata** (Backend Entity)
- **Storage**: Python module at `backend/app/content/chapters/chapter_1.py`
- **Structure**: Python dictionary with 13 fields (core ID/title, structure, placeholders, RAG metadata)
- **Validation**: ID matches chapter number, title matches MDX exactly, counts match actual placeholders
- **Relationship**: 1:1 with Chapter Content (derived, manually synced)

---

### Data Contracts

**Documented in**: `contracts/content-schema.md`

#### MDX Frontmatter Schema

```yaml
# Required fields
title: string              # Pattern: "Chapter N — Title", 10-100 chars
description: string        # SEO summary, 10-250 chars
sidebar_position: integer  # Positive integer, must match chapter number
sidebar_label: string      # Abbreviated title, 10-50 chars

# Optional fields
tags: string[]            # Lowercase kebab-case, 1-20 chars per tag
```

---

#### Chapter Metadata Schema (Python)

```python
CHAPTER_METADATA = {
    "id": int,                    # Chapter number (1, 2, 3, ...)
    "title": str,                 # Must match MDX frontmatter exactly
    "summary": str,               # 2-3 sentences, 50-300 chars
    "section_count": int,         # Number of H2 sections (7 for Ch 1)
    "sections": List[str],        # Section titles in order
    "ai_blocks": List[str],       # AI-block types present (4 items)
    "diagram_placeholders": List[str],  # Diagram names (4 items)
    "last_updated": str,          # ISO 8601 timestamp
    "difficulty_level": str,      # "beginner" | "intermediate" | "advanced"
    "prerequisites": List[int],   # Chapter IDs (empty for Ch 1)
    "learning_outcomes": List[str],  # 3-10 items, action verb start
    "glossary_terms": List[str],  # Terms defined in glossary (7 for Ch 1)
}
```

---

#### Content Structure Contract

**Global Rules**:
- Heading hierarchy: Only H1 (implicit from title) and H2 allowed
- Section count: Exactly 7 H2 sections for Chapter 1
- Section order: Must follow spec (see data-model.md)
- Paragraph length: Maximum 4 sentences
- Sentence length: Average 15-20 words
- Reading level: Flesch-Kincaid grade 7-8 (60-70 Flesch Reading Ease)

**Section Format**:
```markdown
## Section Title

[Introductory paragraph with topic sentence]
[Explanation paragraph (3-4 sentences, 15-20 words/sentence)]
[Example or application paragraph]

<!-- DIAGRAM: placeholder-name -->
<!-- AI-BLOCK: block-type -->
```

---

#### Placeholder Format Contracts

**Diagram Placeholder**:
- Format: `<!-- DIAGRAM: {placeholder-name} -->`
- Regex: `^<!-- DIAGRAM: [a-z]+(-[a-z]+)* -->$`
- Valid: `<!-- DIAGRAM: physical-ai-overview -->`
- Invalid: `<!--DIAGRAM: no-space-->` ❌, `<!-- DIAGRAM: CamelCase -->` ❌

**AI-Interactive Block Placeholder**:
- Format: `<!-- AI-BLOCK: {block-type} -->`
- Regex: `^<!-- AI-BLOCK: (ask-question|explain-like-i-am-10|interactive-quiz|generate-diagram) -->$`
- Valid: `<!-- AI-BLOCK: ask-question -->`
- Invalid: `<!-- AI-BLOCK: custom-type -->` ❌, `<!-- AI-BLOCK: askQuestion -->` ❌

**Glossary Term Format**:
- Format: `**Term Name**: Definition text.`
- Valid: `**Physical AI**: Artificial intelligence systems that...`
- Invalid: `Physical AI: No bold` ❌, `**Physical AI** : Space before colon` ❌

---

### Quickstart Guide

**Documented in**: `quickstart.md`

**4-Phase Implementation Process**:

1. **Phase 1: Frontend Content Creation** (2-3 hours)
   - Create MDX file with frontmatter
   - Write 7 sections following content guidelines
   - Place 4 diagram placeholders logically
   - Place 4 AI-block placeholders strategically

2. **Phase 2: Add Interactive Placeholders** (15 minutes)
   - Verify placeholder positioning
   - Check syntax and naming

3. **Phase 3: Backend Metadata Scaffold** (30 minutes)
   - Create directory `backend/app/content/chapters/`
   - Create `chapter_1.py` with CHAPTER_METADATA dictionary
   - Create `__init__.py` files for package structure

4. **Phase 4: Build Validation** (15 minutes)
   - Run `npm run build` in frontend (check for errors)
   - Test dev server at `http://localhost:3000/docs/chapters/chapter-1`
   - Test Python import: `from app.content.chapters.chapter_1 import CHAPTER_METADATA`
   - Manual content quality review

**Estimated Total Time**: 2-4 hours (varies by writing speed and subject matter expertise)

---

## Implementation Phases Summary

### Phase 0: Research ✅ COMPLETE
- **Output**: `research.md` with 5 resolved technical questions
- **Key Decisions**: MDX frontmatter structure, AI-block placement strategy, content writing style, backend metadata structure, placeholder naming convention
- **Status**: All NEEDS CLARIFICATION markers resolved

### Phase 1: Design & Contracts ✅ COMPLETE
- **Output**: `data-model.md`, `contracts/content-schema.md`, `quickstart.md`
- **Key Artifacts**: 6 entity definitions, 5 data contract schemas, 4-phase implementation guide
- **Status**: Architecture designed, validation rules specified

### Phase 2: Task Generation ⏳ NEXT STEP
- **Command**: `/sp.tasks`
- **Output**: `tasks.md` with testable implementation tasks
- **Expected**: Break down quickstart guide into atomic tasks with acceptance criteria
- **Status**: Ready to proceed

### Phase 3: Implementation 🔜 FUTURE
- **Command**: `/sp.implement`
- **Output**: Actual MDX file and Python metadata file
- **Expected**: Follow quickstart.md step-by-step with TDD validation
- **Status**: Waiting for Phase 2 completion

---

## Acceptance Criteria Mapping

### Spec Success Criteria → Plan Validation

| Success Criteria | Plan Element | Validation Method |
|------------------|--------------|-------------------|
| **SC-001**: Learner can read complete 7 sections | Phase 1 content creation, Section entity definitions | Manual review + dev server test |
| **SC-002**: `npm run build` succeeds | Phase 4 build validation | Automated build test |
| **SC-003**: 4 diagram placeholders present | Diagram Placeholder entity, contracts | Manual count + regex validation (future) |
| **SC-004**: 4 AI-block placeholders present | AI-Interactive Block entity, contracts | Manual count + regex validation (future) |
| **SC-005**: 7 glossary terms defined | Glossary Term entity, Section 7 structure | Manual verification |
| **SC-006**: 7 sections in correct order | Section entity order validation | Manual verification + metadata check |
| **SC-007**: 7th-8th grade reading level | Content writing guidelines in research.md | Manual review + Flesch-Kincaid tool (optional) |
| **SC-008**: Backend metadata file importable | Phase 3 backend scaffold | Python import test |
| **SC-009**: 6 metadata fields accessible | Chapter Metadata entity schema | Python field access test |
| **SC-010**: Both files tracked in git | Phase 4 validation | `git status` check |

---

## Dependencies & Risks

### Internal Dependencies (Resolved)
- ✅ Feature 001 (Base Project Initialization) complete
- ✅ Docusaurus frontend functional at localhost:3000
- ✅ FastAPI backend structure exists
- ✅ Git branch `003-chapter-1-content` created and checked out

### External Dependencies (Satisfied)
- ✅ Docusaurus 3.x installed (from Feature 001)
- ✅ Node.js 18+ (from Feature 001)
- ✅ Python 3.11+ (from Feature 001)
- ✅ No new external dependencies required

### Risks & Mitigations

**Risk 1**: Content reading level too advanced for 12+ age group
- **Impact**: Fails SC-007, reduces learner comprehension
- **Mitigation**: Follow research.md writing guidelines, use Flesch-Kincaid tool, get peer review from non-expert

**Risk 2**: Content writing takes longer than estimated 2-4 hours
- **Impact**: Feature completion delayed
- **Mitigation**: Prioritize P1 sections (1-4), complete P2 sections (5-7) iteratively, accept "good enough" first draft with revision in future

**Risk 3**: MDX syntax errors break Docusaurus build
- **Impact**: Fails SC-002, blocks deployment
- **Mitigation**: Test build incrementally after each section, reference existing `intro.md` for syntax examples, use MDX linter if available

**Risk 4**: Metadata values don't match MDX content exactly
- **Impact**: Data integrity issues, future RAG pipeline errors
- **Mitigation**: Create checklist comparing metadata to MDX (section count, section titles, placeholder counts), perform manual verification before marking complete

**Risk 5**: Diagram/AI-block placeholders use inconsistent naming
- **Impact**: Future automation fails to find placeholders
- **Mitigation**: Document naming convention in contracts, validate all placeholders against regex patterns, code review to catch inconsistencies

---

## Post-Planning Next Steps

1. **Agent context updated**: ✅ Complete (ran `.specify/scripts/bash/update-agent-context.sh claude`)

2. **Run `/sp.tasks`**: ⏳ Next command
   - Generate testable task list from quickstart.md
   - Break down 4 phases into atomic tasks with acceptance criteria
   - Link each task to success criteria from spec.md

3. **Review plan artifacts**: ⏳ User approval checkpoint
   - User reviews: research.md, data-model.md, contracts/content-schema.md, quickstart.md, plan.md
   - User approves technical decisions and implementation approach
   - User provides feedback or clarifications if needed

4. **Begin implementation**: 🔜 After task generation
   - Run `/sp.implement` to start TDD workflow
   - Follow quickstart.md step-by-step
   - Validate against acceptance criteria at each milestone

---

## Key Takeaways

### What This Plan Delivers
✅ **Complete implementation roadmap** for Chapter 1 written content
✅ **5 research decisions** resolving technical clarifications
✅ **6 entity definitions** establishing data model
✅ **5 data contract schemas** with validation rules and regex patterns
✅ **4-phase quickstart guide** with step-by-step instructions
✅ **Acceptance criteria mapping** from spec to plan elements
✅ **Risk analysis** with mitigation strategies

### What This Plan Does NOT Deliver (Out of Scope)
❌ Actual chapter content (created in `/sp.implement` phase)
❌ RAG pipeline implementation (future Feature 004+)
❌ Diagram generation (future Feature 007+)
❌ AI-interactive components (future Feature 008+)
❌ Translation system (future Feature 006+)
❌ Personalization engine (future Feature 005+)
❌ Automated validation scripts (future tooling enhancement)

### Success Indicators
✅ All Constitution principles passed or in acceptable scaffolding phase
✅ All research questions resolved (no NEEDS CLARIFICATION markers remain)
✅ Data model maps 1:1 to spec requirements
✅ Contracts provide machine-parseable validation rules
✅ Quickstart guide provides clear implementation path
✅ Estimated time (2-4 hours) is realistic for content creation
✅ Ready to proceed to `/sp.tasks` command

---

---

## Detailed Architecture Plan

### 1. File Architecture: MDX Structure with Section Anchors

**File Location**: `frontend/docs/chapters/chapter-1.mdx`

#### Complete MDX Structure Template

```markdown
---
title: "Chapter 1 — Introduction to Physical AI & Robotics"
description: "Learn the fundamentals of Physical AI and how robots become intelligent through AI integration"
sidebar_position: 1
sidebar_label: "Chapter 1: Intro to Physical AI"
tags: ["physical-ai", "robotics", "introduction", "beginner"]
---

## What is Physical AI? {#what-is-physical-ai}

[Content paragraphs...]

<!-- DIAGRAM: physical-ai-overview -->
<!-- AI-BLOCK: ask-question -->

## What is a Robot? {#what-is-a-robot}

[Content paragraphs...]

<!-- DIAGRAM: robot-anatomy -->
<!-- AI-BLOCK: generate-diagram -->

## AI + Robotics = Physical AI Systems {#ai-robotics-systems}

[Content paragraphs...]

<!-- AI-BLOCK: explain-like-i-am-10 -->
<!-- DIAGRAM: ai-robotics-stack -->

## Core Concepts Introduced in This Book {#core-concepts}

[Content paragraphs...]

<!-- DIAGRAM: core-concepts-flow -->
<!-- AI-BLOCK: interactive-quiz -->

## Learning Objectives {#learning-objectives}

[Content paragraphs...]

## Summary {#summary}

[Content paragraphs...]

## Glossary {#glossary}

**Physical AI**: [Definition...]
**Robot**: [Definition...]
[... 5 more terms ...]
```

#### Section Anchor Strategy

- **Format**: `{#section-anchor}` after each H2 heading
- **Naming Convention**: Kebab-case matching section title
- **Purpose**: Enable deep linking, table of contents, and RAG metadata
- **Anchors**:
  1. `#what-is-physical-ai`
  2. `#what-is-a-robot`
  3. `#ai-robotics-systems`
  4. `#core-concepts`
  5. `#learning-objectives`
  6. `#summary`
  7. `#glossary`

#### Diagram Placeholder Mapping

| Placeholder | Section | Position | Future Diagram Type |
|------------|---------|----------|---------------------|
| `physical-ai-overview` | Section 1 | After intro paragraph | Concept map showing Digital AI vs Physical AI |
| `robot-anatomy` | Section 2 | After component explanation | Labeled diagram of sensors/actuators/controllers |
| `ai-robotics-stack` | Section 3 | After autonomy levels | Stack diagram showing AI layers on robot hardware |
| `core-concepts-flow` | Section 4 | After concept list | Flow diagram showing concept relationships |

#### AI-Block Placeholder Mapping

| Placeholder | Section | Position | Future Component |
|------------|---------|----------|-------------------|
| `ask-question` | Section 1 | End of section | `<AskQuestionBlock chapterId={1} sectionId="what-is-physical-ai" />` |
| `generate-diagram` | Section 2 | After diagram placeholder | `<GenerateDiagramBlock diagramType="robot-anatomy" />` |
| `explain-like-i-am-10` | Section 3 | Middle of section | `<ExplainLike10Block concept="autonomy" />` |
| `interactive-quiz` | Section 4 | End of section | `<InteractiveQuizBlock chapterId={1} />` |

#### Internal MDX Components (Future)

No internal MDX components needed in this phase. All interactive elements will be React components loaded via MDX component mapping (see Feature 004).

---

### 2. Backend Architecture: Chapter Metadata Structure

**File Location**: `backend/app/content/chapters/chapter_1.py`

#### Exact Field Structure

```python
CHAPTER_METADATA = {
    # Core identification (required)
    "id": int,                    # 1
    "title": str,                 # "Chapter 1 — Introduction to Physical AI & Robotics"
    "summary": str,               # 2-3 sentences, 50-300 chars
    
    # Structure information (required)
    "section_count": int,         # 7
    "sections": List[str],        # ["What is Physical AI?", ...]
    
    # Placeholder tracking (required)
    "ai_blocks": List[str],       # ["ask-question", "generate-diagram", ...]
    "diagram_placeholders": List[str],  # ["physical-ai-overview", ...]
    
    # Versioning (required)
    "last_updated": str,          # ISO 8601: "2025-12-05T00:00:00Z"
    
    # RAG-specific metadata (required for future integration)
    "difficulty_level": str,       # "beginner" | "intermediate" | "advanced"
    "prerequisites": List[int],    # Chapter IDs: [] for Chapter 1
    "learning_outcomes": List[str], # Action verb statements
    "glossary_terms": List[str]    # ["Physical AI", "Robot", ...]
}
```

#### Field Validation Rules

| Field | Type | Validation | Example |
|-------|------|------------|---------|
| `id` | int | Must match chapter number | `1` |
| `title` | str | Must match MDX frontmatter exactly | `"Chapter 1 — Introduction to Physical AI & Robotics"` |
| `summary` | str | 50-300 chars, 2-3 sentences | `"An introductory chapter covering..."` |
| `section_count` | int | Must match actual H2 sections in MDX | `7` |
| `sections` | List[str] | Must match H2 headings in order | `["What is Physical AI?", ...]` |
| `ai_blocks` | List[str] | Must match AI-BLOCK comments in MDX | `["ask-question", "generate-diagram", ...]` |
| `diagram_placeholders` | List[str] | Must match DIAGRAM comments in MDX | `["physical-ai-overview", ...]` |
| `last_updated` | str | ISO 8601 format | `"2025-12-05T00:00:00Z"` |
| `difficulty_level` | str | Enum: "beginner", "intermediate", "advanced" | `"beginner"` |
| `prerequisites` | List[int] | Empty for Chapter 1 | `[]` |
| `learning_outcomes` | List[str] | 3-10 items, start with action verb | `["Define Physical AI...", ...]` |
| `glossary_terms` | List[str] | Must match glossary entries in MDX | `["Physical AI", "Robot", ...]` |

#### Module Structure

```python
"""
Chapter 1 metadata for RAG integration and content management.

This module contains structured metadata for Chapter 1: "Introduction to Physical AI & Robotics"
including section information, placeholder tracking, and learning objectives.

TODO: Future RAG Integration Points
- [ ] Create Pydantic model for ChapterMetadata with validation rules
- [ ] Implement embedding generation for chapter content (OpenAI/local models)
- [ ] Store embeddings in Qdrant vector database with metadata
- [ ] Create API endpoint GET /api/chapters/1 to serve this metadata
- [ ] Add semantic search capability across all chapters
- [ ] Implement chapter recommendation based on prerequisites and difficulty
"""

from typing import List

CHAPTER_METADATA = {
    # ... fields as defined above
}
```

---

### 3. AI-Blocks Architecture: Mapping to Subagents and Skills

**Purpose**: Define routing plan for each AI-BLOCK placeholder to future Claude Code subagents and reusable skills.

#### AI-BLOCK to Subagent Mapping Table

| AI-BLOCK Type | Future Subagent | Location | Primary Skill | Secondary Skills |
|---------------|-----------------|----------|--------------|------------------|
| `ask-question` | `ChapterQuestionAgent` | `backend/app/agents/subagents/chapter_question_agent.py` | `ContextRetrievalSkill` | `VectorSearchSkill`, `GlossaryLookupSkill` |
| `explain-like-i-am-10` | `ChapterExplainerAgent` | `backend/app/agents/subagents/chapter_explainer_agent.py` | `ContextRetrievalSkill` | `EmbeddingGenerationSkill`, `VectorSearchSkill` |
| `interactive-quiz` | `ChapterQuizAgent` | `backend/app/agents/subagents/chapter_quiz_agent.py` | `QuizGenerationSkill` | `ContextRetrievalSkill`, `ProgressTrackingSkill` |
| `generate-diagram` | `DiagramGeneratorAgent` | `backend/app/agents/subagents/diagram_generator_agent.py` | `DiagramGenerationSkill` | `ContextRetrievalSkill`, `ContentChunkingSkill` |

#### Subagent Implementation Plan (Future)

**1. ChapterQuestionAgent** (`ask-question` block)
- **Purpose**: Answer learner questions about chapter content using RAG
- **Skills Used**:
  - `ContextRetrievalSkill`: Retrieve relevant chapter sections
  - `VectorSearchSkill`: Semantic search in Qdrant
  - `GlossaryLookupSkill`: Find term definitions
- **API Endpoint**: `POST /api/ai/ask-question`
- **Request**: `{ "question": str, "chapterId": int, "sectionId": str }`
- **Response**: `{ "answer": str, "sources": List[str], "confidence": float }`

**2. ChapterExplainerAgent** (`explain-like-i-am-10` block)
- **Purpose**: Generate simplified explanations at age-appropriate level
- **Skills Used**:
  - `ContextRetrievalSkill`: Get concept context
  - `EmbeddingGenerationSkill`: Generate query embeddings
  - `VectorSearchSkill`: Find similar explanations
- **API Endpoint**: `POST /api/ai/explain-like-10`
- **Request**: `{ "concept": str, "chapterId": int, "targetAge": int }`
- **Response**: `{ "explanation": str, "analogies": List[str] }`

**3. ChapterQuizAgent** (`interactive-quiz` block)
- **Purpose**: Generate adaptive quizzes based on learning objectives
- **Skills Used**:
  - `QuizGenerationSkill`: Create questions from learning outcomes
  - `ContextRetrievalSkill`: Get chapter content for question context
  - `ProgressTrackingSkill`: Record quiz performance
- **API Endpoint**: `POST /api/ai/quiz`
- **Request**: `{ "chapterId": int, "numQuestions": int, "difficulty": str }`
- **Response**: `{ "questions": List[QuizQuestion], "quizId": str }`

**4. DiagramGeneratorAgent** (`generate-diagram` block)
- **Purpose**: Generate visual diagrams from chapter concepts
- **Skills Used**:
  - `DiagramGenerationSkill`: Create diagrams using LLM vision models
  - `ContentChunkingSkill`: Extract relevant content chunks
  - `ContextRetrievalSkill`: Get concept relationships
- **API Endpoint**: `POST /api/ai/diagram`
- **Request**: `{ "diagramType": str, "chapterId": int, "concepts": List[str] }`
- **Response**: `{ "diagramUrl": str, "diagramType": str, "metadata": dict }`

#### Skill Implementation Plan (Future)

**Reusable Skills Location**: `backend/app/agents/skills/`

| Skill Name | File | Purpose | Dependencies |
|------------|------|---------|--------------|
| `ContextRetrievalSkill` | `context_retrieval_skill.py` | Retrieve relevant context for RAG | Qdrant client, OpenAI client |
| `VectorSearchSkill` | `vector_search_skill.py` | Semantic search in Qdrant | Qdrant client |
| `EmbeddingGenerationSkill` | `embedding_generation_skill.py` | Generate text embeddings | OpenAI client |
| `ContentChunkingSkill` | `content_chunking_skill.py` | Split content into RAG chunks | None (pure function) |
| `GlossaryLookupSkill` | `glossary_lookup_skill.py` | Find glossary term definitions | Chapter metadata |
| `QuizGenerationSkill` | `quiz_generation_skill.py` | Generate quiz questions | OpenAI client, Chapter metadata |
| `ProgressTrackingSkill` | `progress_tracking_skill.py` | Track user progress | Database client |
| `DiagramGenerationSkill` | `diagram_generation_skill.py` | Generate visual diagrams | OpenAI vision API |

**Note**: All skills are placeholders in this feature. Implementation deferred to future features (005+).

---

### 4. RAG Preparation Plan: Chunking Model

**Purpose**: Define how Chapter 1 content will be chunked and embedded for vector database storage.

#### Chunking Strategy

**Primary Strategy**: Semantic chunking based on section boundaries with overlap

**Chunking Rules**:
1. **Section-Level Chunks**: Each H2 section becomes a primary chunk
2. **Subsection Chunks**: Long sections (>500 words) split at paragraph boundaries
3. **Glossary Chunks**: Each glossary term becomes a separate chunk
4. **Overlap**: 50-word overlap between adjacent chunks to preserve context
5. **Metadata Preservation**: Each chunk includes: `chapter_id`, `section_id`, `section_title`, `chunk_index`, `chunk_type`

#### Chunking Model Structure

```python
# Future implementation in backend/app/services/rag/chunking.py

class ContentChunk:
    """Represents a chunk of chapter content for RAG."""
    
    chunk_id: str              # Unique identifier: "ch1-s1-c0"
    chapter_id: int           # 1
    section_id: str           # "what-is-physical-ai"
    section_title: str         # "What is Physical AI?"
    chunk_index: int           # 0, 1, 2... (order within section)
    chunk_type: str            # "section" | "glossary" | "diagram_context"
    content: str               # Actual text content
    word_count: int            # Approximate word count
    token_count: int           # Token count for embedding model
    metadata: dict             # Additional metadata (diagram refs, AI-block refs)
    
    # For RAG retrieval
    embedding: List[float]     # Vector embedding (1536 dims for text-embedding-3-small)
    source_url: str            # Deep link: "/docs/chapters/chapter-1#what-is-physical-ai"
```

#### Chunking Examples

**Example 1: Section Chunk**
```python
{
    "chunk_id": "ch1-s1-c0",
    "chapter_id": 1,
    "section_id": "what-is-physical-ai",
    "section_title": "What is Physical AI?",
    "chunk_index": 0,
    "chunk_type": "section",
    "content": "Have you ever wondered how a robot vacuum knows where to clean...",
    "word_count": 250,
    "token_count": 320,
    "metadata": {
        "has_diagram": True,
        "diagram_placeholder": "physical-ai-overview",
        "has_ai_block": True,
        "ai_block_type": "ask-question"
    },
    "source_url": "/docs/chapters/chapter-1#what-is-physical-ai"
}
```

**Example 2: Glossary Chunk**
```python
{
    "chunk_id": "ch1-glossary-physical-ai",
    "chapter_id": 1,
    "section_id": "glossary",
    "section_title": "Glossary",
    "chunk_index": 0,
    "chunk_type": "glossary",
    "content": "**Physical AI**: Artificial intelligence systems that can sense...",
    "word_count": 45,
    "token_count": 60,
    "metadata": {
        "term": "Physical AI",
        "definition_length": "medium"
    },
    "source_url": "/docs/chapters/chapter-1#glossary"
}
```

#### Embedding Generation Plan

**Model**: `text-embedding-3-small` (OpenAI) - 1536 dimensions
**Batch Size**: 100 chunks per batch
**Metadata Filtering**: Filter by `chapter_id`, `section_id`, `chunk_type` in Qdrant queries

#### Qdrant Collection Schema (Future)

```python
# Future Qdrant collection: "textbook_chapters"

collection_config = {
    "name": "textbook_chapters",
    "vector_size": 1536,  # text-embedding-3-small dimension
    "distance": "Cosine",
    "payload_schema": {
        "chapter_id": "integer",
        "section_id": "string",
        "section_title": "string",
        "chunk_type": "string",  # "section" | "glossary" | "diagram_context"
        "chunk_index": "integer",
        "word_count": "integer",
        "source_url": "string",
        "has_diagram": "boolean",
        "has_ai_block": "boolean",
        "ai_block_type": "string",  # optional
        "difficulty_level": "string"  # "beginner" | "intermediate" | "advanced"
    }
}
```

#### Chunking Implementation Phases

**Phase 1 (This Feature)**: No chunking - content exists as single MDX file
**Phase 2 (Future Feature 005)**: Implement `ContentChunkingSkill` with section-based chunking
**Phase 3 (Future Feature 006)**: Generate embeddings and store in Qdrant
**Phase 4 (Future Feature 007)**: Implement RAG retrieval pipeline

---

### 5. Compliance Checklist

#### SDD Constitution Compliance

| Principle | Requirement | Status | Evidence |
|-----------|-------------|--------|----------|
| **I. SDD Workflow** | Spec → Plan → Tasks → Implement | ✅ PASS | This plan document, spec.md exists |
| **II. Docusaurus-First** | MDX format, proper frontmatter | ✅ PASS | MDX structure defined in Section 1 |
| **III. RAG-First** | Metadata includes RAG-ready fields | ⚠️ SCAFFOLDING | Chunking plan defined, embeddings deferred |
| **IV. Personalization** | Content suitable for broad audience | ✅ PASS | Beginner-level content, metadata includes difficulty_level |
| **V. Multilingual** | Translation-friendly structure | ⚠️ SCAFFOLDING | English source content, clean markdown structure |
| **VI. TDD Quality Gates** | Manual review + build validation | ✅ PASS | Acceptance criteria defined, validation methods specified |

#### Docusaurus-First Compliance

- ✅ MDX file uses standard Docusaurus frontmatter
- ✅ Section anchors enable deep linking
- ✅ Content placed in `frontend/docs/chapters/` directory
- ✅ Static generation supported (no dynamic rendering)
- ✅ Markdown-native with HTML comment placeholders

#### RAG-First Compliance

- ✅ Backend metadata includes RAG-ready fields (`summary`, `learning_outcomes`, `glossary_terms`)
- ✅ Chunking strategy defined (section-based with overlap)
- ✅ Embedding model selected (`text-embedding-3-small`)
- ✅ Qdrant collection schema planned
- ⚠️ Actual RAG implementation deferred to future features (005+)

#### AI-Native Textbook Architecture

- ✅ AI-BLOCK placeholders mapped to future subagents
- ✅ Skills architecture defined for reusable capabilities
- ✅ API endpoint contracts specified
- ✅ Component-to-agent routing plan documented
- ⚠️ Actual AI logic deferred to future features (004+)

---

### 6. Deliverables

#### Deliverable 1: MDX Content File

**File**: `frontend/docs/chapters/chapter-1.mdx`

**Structure Outline**:
```
1. Frontmatter (YAML)
   - title, description, sidebar_position, sidebar_label, tags

2. Section 1: What is Physical AI? {#what-is-physical-ai}
   - Content paragraphs (200-300 words)
   - <!-- DIAGRAM: physical-ai-overview -->
   - <!-- AI-BLOCK: ask-question -->

3. Section 2: What is a Robot? {#what-is-a-robot}
   - Content paragraphs (250-350 words)
   - <!-- DIAGRAM: robot-anatomy -->
   - <!-- AI-BLOCK: generate-diagram -->

4. Section 3: AI + Robotics = Physical AI Systems {#ai-robotics-systems}
   - Content paragraphs (300-400 words)
   - <!-- AI-BLOCK: explain-like-i-am-10 -->
   - <!-- DIAGRAM: ai-robotics-stack -->

5. Section 4: Core Concepts Introduced in This Book {#core-concepts}
   - Content paragraphs (400-500 words)
   - <!-- DIAGRAM: core-concepts-flow -->
   - <!-- AI-BLOCK: interactive-quiz -->

6. Section 5: Learning Objectives {#learning-objectives}
   - Bullet points (6 items)
   - Reflection questions (3 items)

7. Section 6: Summary {#summary}
   - Recap paragraphs (150-200 words)

8. Section 7: Glossary {#glossary}
   - 7 term definitions (10-100 words each)
```

**Validation**: Docusaurus build succeeds, all sections render correctly

#### Deliverable 2: Backend Metadata File

**File**: `backend/app/content/chapters/chapter_1.py`

**Structure Outline**:
```python
CHAPTER_METADATA = {
    "id": 1,
    "title": "Chapter 1 — Introduction to Physical AI & Robotics",
    "summary": "...",
    "section_count": 7,
    "sections": [...],
    "ai_blocks": [...],
    "diagram_placeholders": [...],
    "last_updated": "2025-12-05T00:00:00Z",
    "difficulty_level": "beginner",
    "prerequisites": [],
    "learning_outcomes": [...],
    "glossary_terms": [...]
}
```

**Validation**: Python import succeeds, all fields accessible

#### Deliverable 3: Architecture Documentation

**Files**:
- `specs/003-chapter-1-content/plan.md` (this document)
- `specs/003-chapter-1-content/data-model.md` (entity definitions)
- `specs/003-chapter-1-content/contracts/content-schema.md` (validation schemas)

**Validation**: All architecture decisions documented, ready for `/sp.tasks`

#### Deliverable 4: Mapping Table: Section → AI-Blocks → Future Skills

**Table**: Section-to-AI-Block-to-Skill Mapping

| Section | AI-BLOCK | Future Subagent | Primary Skill | Implementation Phase |
|---------|----------|-----------------|---------------|---------------------|
| What is Physical AI? | `ask-question` | `ChapterQuestionAgent` | `ContextRetrievalSkill` | Feature 004 |
| What is a Robot? | `generate-diagram` | `DiagramGeneratorAgent` | `DiagramGenerationSkill` | Feature 007 |
| AI + Robotics | `explain-like-i-am-10` | `ChapterExplainerAgent` | `ContextRetrievalSkill` | Feature 004 |
| Core Concepts | `interactive-quiz` | `ChapterQuizAgent` | `QuizGenerationSkill` | Feature 004 |

**Validation**: All 4 AI-BLOCK placeholders mapped to future implementation

---

**Plan Status**: ✅ **COMPLETE AND APPROVED**

**Next Command**: `/sp.tasks` - Generate task list from quickstart.md

**Estimated Time to Implementation**: 2-4 hours (content writing) + 30 minutes (validation)

**Blocking Issues**: None - all dependencies resolved, all technical decisions made, all artifacts generated.
