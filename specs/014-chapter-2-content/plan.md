# Implementation Plan: Chapter 2 Written Content — Structure, Metadata, Schema & Contracts

**Branch**: `014-chapter-2-content` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/014-chapter-2-content/spec.md`

## Summary

This feature establishes the complete Chapter 2 content framework: MDX structure with placeholders, metadata schema, glossary items, AI-block markers, diagram placeholders, and backend metadata file. **NO real text content is written**—only structure and placeholders. The implementation creates an MDX skeleton with exactly 7 H2 sections, 4 diagram placeholders, 4 AI-block React components, and a glossary section with 7 placeholder terms. A backend metadata file provides structured information for future RAG integration, and comprehensive contracts document validation rules and content writing guidelines.

**Primary Deliverable**: `frontend/docs/chapters/chapter-2.mdx` (MDX skeleton with structure only)
**Secondary Deliverable**: `backend/app/content/chapters/chapter_2.py` (Python metadata dictionary)
**Tertiary Deliverable**: Contract files (content-schema.md, checklists, research.md, quickstart.md, data-model.md)
**Validation**: Manual structure review + Docusaurus build test + Python import test

## Technical Context

**Language/Version**:
- Frontend: MDX (Markdown + JSX) compatible with Docusaurus 3.x
- Backend: Python 3.11+

**Primary Dependencies**:
- Frontend: Docusaurus 3.x (already installed)
- Backend: Python 3.11+ standard library (no new dependencies)
- Feature 003 (Chapter 1 Content): Template pattern reference
- Feature 011 (Chapter 2 AI Blocks): React components available

**Storage**: Static files (MDX content, Python module) - no database

**Testing**:
- Frontend: `npm run build` validation (Docusaurus build process)
- Backend: Python import test (`python -c "from app.content.chapters.chapter_2 import CHAPTER_METADATA"`)
- Manual: Structure validation (section count, placeholder count, naming conventions)

**Target Platform**:
- Frontend: Web browsers (Chrome, Firefox, Safari) via Docusaurus static site
- Backend: Server-side Python (Uvicorn/FastAPI environment)

**Project Type**: Web application (frontend MDX structure + backend metadata scaffold)

**Performance Goals**:
- Page load time: < 2 seconds for Chapter 2 page (structure only, no content)
- Build time: Incremental build < 5 seconds
- No performance-critical operations (static structure only)

**Constraints**:
- MUST NOT write actual content text (only placeholders)
- MUST have exactly 7 H2 sections (not 9 as in existing chapter-2.mdx from Feature 010)
- MUST follow Chapter 1 structure pattern (Feature 003)
- MUST use kebab-case for diagram placeholders
- MUST use valid AI-block component types (from Feature 011)
- Backend metadata MUST remain simple Python dictionary (no Pydantic model, no database)

**Scale/Scope**:
- 1 chapter (Chapter 2 only)
- 7 H2 sections (structure only, no content)
- 7 glossary term placeholders
- 4 diagram placeholders (kebab-case)
- 4 AI-block React components (chapterId={2})
- 1 backend metadata file
- 5 contract files

---

## 1. MDX Structure Plan

### 1.1 Section Headings (Exactly 7 H2 Sections)

**Decision**: Use exactly 7 H2 sections matching spec requirements, not 9 as in existing chapter-2.mdx

**Section Structure**:
```markdown
## Section 1: Introduction to ROS 2 {#introduction-to-ros2}
## Section 2: Nodes and Node Communication {#nodes-and-node-communication}
## Section 3: Topics and Messages {#topics-and-messages}
## Section 4: Services and Actions {#services-and-actions}
## Section 5: ROS 2 Packages {#ros2-packages}
## Section 6: Launch Files and Workflows {#launch-files-and-workflows}
## Section 7: Glossary {#glossary}
```

**Rationale**:
- **7 sections**: Matches spec requirement (FR-009)
- **No separate Learning Objectives/Summary**: These are not counted as separate sections per spec (unlike existing file which has 9 sections)
- **Anchor IDs**: Kebab-case section IDs for linking and AI-block integration
- **Consistent naming**: Matches Chapter 1 pattern (H2 headings with descriptive titles)

**Note**: Existing `chapter-2.mdx` from Feature 010 has 9 sections (includes separate "Learning Objectives" and "Summary" sections). This plan requires 7 sections total. During implementation, these may be:
- Option A: Remove Learning Objectives and Summary as separate sections (merge into Glossary or remove)
- Option B: Keep them but don't count as separate H2 sections (use H3 or inline)
- Option C: Update spec to match existing structure (requires spec change)

**Recommendation**: Follow spec requirement (7 sections) and update existing file if needed.

---

### 1.2 AI-Block Placement Rules

**Decision**: Place AI blocks at strategic points following pedagogical principles, using React components from Feature 011

**Placement Strategy**:

1. **`<AskQuestionBlock />`** - End of Section 1 (Introduction to ROS 2)
   - **Position**: After content placeholder, after diagram placeholder
   - **Props**: `chapterId={2}`, `sectionId="introduction-to-ros2"`
   - **Why**: Encourages active recall after new concept introduction
   - **Learning Theory**: Retrieval practice strengthens memory formation

2. **`<GenerateDiagramBlock />`** - Within Section 2 (Nodes and Node Communication)
   - **Position**: After content placeholder, before or after diagram placeholder
   - **Props**: `diagramType="node-communication-architecture"`, `chapterId={2}`
   - **Why**: Visual representation most valuable for structural/component understanding
   - **Learning Theory**: Dual coding theory - combining text + visuals improves retention

3. **`<ExplainLike10Block />`** - Within Section 3 (Topics and Messages)
   - **Position**: After content placeholder, before diagram placeholder
   - **Props**: `concept="topics"`, `chapterId={2}`
   - **Why**: Provides alternative explanation for complex pub/sub concept
   - **Learning Theory**: Multiple representations aid comprehension for diverse learners

4. **`<InteractiveQuizBlock />`** - End of Section 4 (Services and Actions)
   - **Position**: After content placeholder, after diagram placeholder
   - **Props**: `chapterId={2}`, `numQuestions={5}`
   - **Why**: Tests understanding of key ROS 2 communication mechanisms
   - **Learning Theory**: Formative assessment provides feedback on learning progress

**Component Format**:
```jsx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';

// In section:
<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />
```

**Validation Rules**:
- All components MUST have `chapterId={2}`
- `sectionId` MUST match section anchor ID (kebab-case)
- `concept` MUST be ROS 2 concept name (for ELI10)
- `diagramType` MUST match diagram placeholder name
- Components MUST be imported at top of MDX file

---

### 1.3 Diagram Placeholder Placement Rules

**Decision**: Place diagrams at strategic points using kebab-case HTML comments

**Placement Strategy**:

1. **`<!-- DIAGRAM: ros2-ecosystem-overview -->`** - Section 1 (Introduction to ROS 2)
   - **Position**: After content placeholder, before AI block
   - **Purpose**: Visual overview of ROS 2 ecosystem

2. **`<!-- DIAGRAM: node-communication-architecture -->`** - Section 2 (Nodes and Node Communication)
   - **Position**: After content placeholder, before AI block
   - **Purpose**: Visual representation of node communication structure

3. **`<!-- DIAGRAM: topic-pubsub-flow -->`** - Section 3 (Topics and Messages)
   - **Position**: After content placeholder, after AI block
   - **Purpose**: Visual flow of publish/subscribe mechanism

4. **`<!-- DIAGRAM: services-actions-comparison -->`** - Section 4 (Services and Actions)
   - **Position**: After content placeholder, before AI block
   - **Purpose**: Visual comparison of services vs actions

**Format**:
```html
<!-- DIAGRAM: {kebab-case-name} -->
```

**Naming Convention**:
- **Kebab-case**: Lowercase with hyphens (e.g., `ros2-ecosystem-overview`)
- **Descriptive**: Name reflects diagram content (e.g., `node-communication-architecture`)
- **ROS 2-specific**: Names include ROS 2 concepts (nodes, topics, services, actions)

**Validation Rules**:
- Format MUST be `<!-- DIAGRAM: {name} -->` (with spaces)
- Name MUST be kebab-case (lowercase, hyphens only, no spaces/underscores)
- Name MUST be unique within chapter
- Name MUST match `diagram_placeholders` in metadata file

---

### 1.4 Glossary Placement Rules

**Decision**: Place glossary as Section 7 (final section) with 7 placeholder terms

**Structure**:
```markdown
## Glossary {#glossary}

<!-- Content placeholder: Exactly 7 glossary terms with beginner-friendly definitions (10-100 words each, uses analogies from post office, restaurant, phone calls, package delivery):
- ROS 2
- Node
- Topic
- Service
- Action
- Package
- Launch File
-->
```

**Glossary Terms** (7 items):
1. **ROS 2** - Robot Operating System 2 definition
2. **Node** - Node concept with restaurant analogy
3. **Topic** - Topic concept with radio broadcast analogy
4. **Service** - Service concept with phone call analogy
5. **Action** - Action concept with package delivery analogy
6. **Package** - Package structure and organization
7. **Launch File** - Launch file purpose and usage

**Format Rules**:
- Terms listed in placeholder comment (not actual definitions)
- Terms MUST match `glossary_terms` in metadata file
- Terms MUST use ROS 2 analogies (post office, restaurant, radio, phone calls, package delivery)
- Definitions will be written in future feature (not this one)

**Validation Rules**:
- Exactly 7 terms (not more, not less)
- Terms MUST match metadata `glossary_terms` list exactly
- Terms MUST be listed in placeholder comment format

---

### 1.5 Placeholder Text Strategy

**Decision**: Use HTML comments for all content placeholders, no actual text

**Placeholder Format**:
```markdown
<!-- Content placeholder: Description of what content should be written here. Min 200 words, 7th-8th grade level. -->
```

**Placeholder Content Requirements**:
- **Section 1**: Definition of ROS 2, why ROS 2 exists, differences from ROS 1, 3+ real-world examples, post office analogy. Min 200 words.
- **Section 2**: What nodes are, how nodes communicate, node lifecycle, restaurant analogy. Min 200 words.
- **Section 3**: Topics (publish/subscribe), message types, topic naming, radio broadcast analogy. Min 200 words.
- **Section 4**: Services (request/response), actions (long-running), differences, when to use each, phone call and package delivery analogies. Min 200 words.
- **Section 5**: ROS 2 packages, package structure, dependencies, code organization. Min 200 words.
- **Section 6**: Launch files, starting multiple nodes, real-world workflows, common patterns. Min 200 words.
- **Section 7**: 7 glossary terms with definitions (10-100 words each, analogies).

**Validation Rules**:
- All content MUST be placeholder comments (no actual text)
- Placeholders MUST describe what content should be written
- Placeholders MUST include word count requirements
- Placeholders MUST reference ROS 2 analogies where applicable

---

## 2. Metadata Architecture

### 2.1 MDX → Python Metadata Mapping

**Decision**: Map MDX structure to Python dictionary following Chapter 1 pattern

**Mapping Structure**:
```python
CHAPTER_METADATA = {
    # Core identification (from MDX frontmatter)
    "id": 2,                                    # Chapter number
    "title": "Chapter 2 — ROS 2 Fundamentals", # From MDX frontmatter title
    "summary": "placeholder",                    # 2-3 sentence description (50-300 chars)
    
    # Structure information (from MDX body)
    "section_count": 7,                         # Count of H2 sections in MDX
    "sections": [                               # H2 section titles in order
        "Introduction to ROS 2",
        "Nodes and Node Communication",
        "Topics and Messages",
        "Services and Actions",
        "ROS 2 Packages",
        "Launch Files and Workflows",
        "Glossary"
    ],
    
    # Placeholder tracking (from MDX body)
    "ai_blocks": [                              # AI-block component types
        "ask-question",
        "generate-diagram",
        "explain-like-i-am-10",
        "interactive-quiz"
    ],
    "diagram_placeholders": [                    # Diagram placeholder names
        "ros2-ecosystem-overview",
        "node-communication-architecture",
        "topic-pubsub-flow",
        "services-actions-comparison"
    ],
    
    # Versioning
    "last_updated": "2025-12-05T00:00:00Z",    # ISO 8601 timestamp
    
    # RAG-specific metadata
    "difficulty_level": "beginner",             # Enum: beginner | intermediate | advanced
    "prerequisites": [1],                       # Chapter IDs ([1] for Chapter 2)
    "learning_outcomes": [                      # Measurable learning objectives (3-10 items)
        "Define ROS 2 and explain its role in robotics development",
        "Explain how nodes communicate in a ROS 2 system",
        "Distinguish between topics, services, and actions",
        "Identify when to use each communication mechanism",
        "Describe ROS 2 package structure and organization",
        "Explain how launch files coordinate multiple nodes"
    ],
    "glossary_terms": [                          # Terms defined in glossary (7 items)
        "ROS 2",
        "Node",
        "Topic",
        "Service",
        "Action",
        "Package",
        "Launch File"
    ]
}
```

**Field Mapping Rules**:
- `id`: Always `2` for Chapter 2
- `title`: Must match MDX frontmatter `title` exactly (character-for-character)
- `summary`: Placeholder for now (will be written in future feature)
- `section_count`: Must equal number of H2 sections in MDX (7)
- `sections`: Must match H2 headings in MDX in exact order
- `ai_blocks`: Must match AI-block component types in MDX (4 items)
- `diagram_placeholders`: Must match diagram placeholder names in MDX (4 items, kebab-case)
- `prerequisites`: Must be `[1]` (Chapter 1 is prerequisite)
- `glossary_terms`: Must match terms in Glossary section (7 items)

---

### 2.2 Validation Rules

**MDX Validation**:
- Frontmatter MUST have all required fields (title, description, sidebar_position: 2, sidebar_label, tags)
- MUST have exactly 7 H2 sections
- MUST have exactly 4 diagram placeholders (kebab-case)
- MUST have exactly 4 AI-block components (chapterId={2})
- MUST have exactly 7 glossary term placeholders
- All content MUST be placeholder comments (no actual text)

**Metadata Validation**:
- `id` MUST be 2
- `title` MUST match MDX frontmatter title exactly
- `section_count` MUST be 7
- `sections` list MUST have 7 items matching MDX order
- `ai_blocks` MUST have 4 items matching component types
- `diagram_placeholders` MUST have 4 items matching placeholder names
- `prerequisites` MUST be `[1]`
- `glossary_terms` MUST have 7 items matching glossary section
- File MUST import without errors: `from app.content.chapters.chapter_2 import CHAPTER_METADATA`

**Cross-Validation**:
- MDX section count MUST match metadata `section_count`
- MDX section titles MUST match metadata `sections` list in order
- MDX diagram placeholders MUST match metadata `diagram_placeholders` list
- MDX AI-block types MUST match metadata `ai_blocks` list
- MDX glossary terms MUST match metadata `glossary_terms` list

---

## 3. Diagram & AI-Block Placement Logic

### 3.1 Placement Pattern (Mirrors Chapter 1)

**Decision**: Follow Chapter 1 placement pattern but adapt for ROS 2 content

**Chapter 1 Pattern** (Feature 003):
- Section 1: Diagram + Ask Question
- Section 2: Diagram + Generate Diagram
- Section 3: Diagram + Explain Like 10
- Section 4: Diagram + Interactive Quiz

**Chapter 2 Pattern** (This Feature):
- Section 1: Diagram + Ask Question
- Section 2: Diagram + Generate Diagram
- Section 3: Explain Like 10 + Diagram
- Section 4: Diagram + Interactive Quiz

**Rationale**:
- **Consistent pattern**: Similar distribution across sections
- **Strategic placement**: Blocks positioned at learning-critical points
- **ROS 2-specific**: Adapts to ROS 2 content flow (topics explanation benefits from ELI10 before diagram)

**Placement Details**:

| Section | Diagram | AI Block | Position |
|---------|---------|----------|----------|
| 1. Introduction to ROS 2 | `ros2-ecosystem-overview` | `AskQuestionBlock` | Diagram → AI Block |
| 2. Nodes and Node Communication | `node-communication-architecture` | `GenerateDiagramBlock` | Diagram → AI Block |
| 3. Topics and Messages | `topic-pubsub-flow` | `ExplainLike10Block` | AI Block → Diagram |
| 4. Services and Actions | `services-actions-comparison` | `InteractiveQuizBlock` | Diagram → AI Block |
| 5. ROS 2 Packages | None | None | Content only |
| 6. Launch Files and Workflows | None | None | Content only |
| 7. Glossary | None | None | Glossary terms only |

---

### 3.2 Naming Consistency (Kebab-Case)

**Decision**: Use kebab-case for all diagram placeholders, matching Chapter 1 pattern

**Naming Rules**:
- **Format**: `{ros2-concept}-{purpose}` or `{concept}-{relationship}`
- **Case**: Lowercase only
- **Separator**: Hyphens (not underscores, not spaces)
- **Examples**:
  - ✅ `ros2-ecosystem-overview`
  - ✅ `node-communication-architecture`
  - ✅ `topic-pubsub-flow`
  - ✅ `services-actions-comparison`
  - ❌ `ros2_ecosystem_overview` (snake_case)
  - ❌ `ros2EcosystemOverview` (CamelCase)
  - ❌ `ros2 ecosystem overview` (spaces)

**Rationale**:
- **URL-friendly**: Kebab-case works well for file naming if diagrams generated as assets
- **Consistent**: Matches Chapter 1 pattern
- **Parseable**: Easy regex matching: `/<!-- DIAGRAM: ([a-z-]+) -->/g`
- **Human-readable**: Clear and descriptive

**Validation**:
- All diagram placeholders MUST use kebab-case
- Names MUST be unique within chapter
- Names MUST match metadata `diagram_placeholders` list

---

## 4. Contract File Generation

### 4.1 Content Schema Contract

**File**: `specs/014-chapter-2-content/contracts/content-schema.md`

**Purpose**: Define data contracts and validation schemas for Chapter 2 content structure

**Content** (following Feature 003 template):
- MDX frontmatter schema with validation rules
- Chapter metadata schema (Python) with field specifications
- Content structure contract (7 sections)
- Placeholder format contracts (diagram HTML comments, AI-block React components)
- Glossary term format contract
- Validation checklist

**Template Source**: Feature 003 `contracts/content-schema.md`

**Adaptations for Chapter 2**:
- Chapter number: 2 (not 1)
- Section count: 7 (not 7, same as Chapter 1)
- ROS 2-specific examples and analogies
- AI-block components (not HTML comments - from Feature 011)
- Prerequisites: `[1]` (Chapter 1 is prerequisite)

---

### 4.2 Requirements Checklist

**File**: `specs/014-chapter-2-content/checklists/requirements.md`

**Purpose**: Validate specification completeness and quality

**Content** (following Feature 003 template):
- Content quality checklist
- Requirement completeness checklist
- Feature readiness checklist
- Validation results

**Template Source**: Feature 003 `checklists/requirements.md`

**Adaptations for Chapter 2**:
- Chapter 2-specific validation criteria
- Structure validation (7 sections, not 9)
- ROS 2-specific considerations

---

### 4.3 Research Document

**File**: `specs/014-chapter-2-content/research.md`

**Purpose**: Resolve technical clarifications and establish best practices for Chapter 2 content structure

**Content** (following Feature 003 template):
- MDX frontmatter structure for Chapter 2
- AI-block placement strategy for ROS 2 content
- Content writing style guidelines (7th-8th grade, ROS 2 analogies)
- Backend metadata structure for Chapter 2
- Diagram placeholder naming convention
- Glossary term structure for Chapter 2
- Technology stack summary

**Template Source**: Feature 003 `research.md`

**Adaptations for Chapter 2**:
- ROS 2-specific content considerations
- ROS 2 analogies (post office, restaurant, radio, phone calls, package delivery)
- ROS 2 examples (TurtleBot 3, navigation stack, robot arm control)
- Chapter 2 prerequisites and dependencies

---

### 4.4 Data Model Document

**File**: `specs/014-chapter-2-content/data-model.md`

**Purpose**: Define data structures and entities for Chapter 2 content structure system

**Content** (following Feature 003 template):
- Entity definitions (Chapter Content, Section, Diagram Placeholder, AI Block Component, Glossary Term, Chapter Metadata, Chapter Chunks)
- Data relationships diagram
- Data flow (current and future state)
- Validation summary

**Template Source**: Feature 003 `data-model.md`

**Adaptations for Chapter 2**:
- Chapter 2-specific entity examples
- ROS 2-specific data structures
- Chapter 2 metadata structure
- Prerequisites relationship (Chapter 2 depends on Chapter 1)

---

### 4.5 Quickstart Document

**File**: `specs/014-chapter-2-content/quickstart.md`

**Purpose**: Step-by-step implementation guide for Chapter 2 content structure

**Content** (following Feature 003 template):
- Prerequisites
- Implementation overview (4 phases)
- Step-by-step instructions for MDX structure creation
- Backend metadata creation
- Contracts creation
- Validation & testing steps
- Success criteria
- Troubleshooting

**Template Source**: Feature 003 `quickstart.md`

**Adaptations for Chapter 2**:
- Chapter 2-specific implementation steps
- ROS 2-specific validation criteria
- Structure-only focus (no content writing)
- 7 sections (not 9) validation

---

## 5. RAG Preparation

### 5.1 Metadata Fields for RAG

**Decision**: Include RAG-ready fields in metadata following Chapter 1 pattern

**RAG-Ready Fields**:
- `summary`: 2-3 sentence description (50-300 chars) - will be embedded for semantic search
- `learning_outcomes`: List of measurable objectives - will be embedded for context
- `glossary_terms`: List of terms - will be used for semantic search expansion
- `sections`: List of section titles - will be used for section-based filtering
- `prerequisites`: Chapter dependencies - will be used for learning path recommendations

**Future RAG Integration** (Feature 012/013):
- Generate embeddings for `summary` + `learning_outcomes`
- Store embeddings in Qdrant collection "chapter_2"
- Use `glossary_terms` for term expansion in queries
- Use `sections` for section-based chunk filtering
- Use `prerequisites` for cross-chapter context

**Rationale**:
- **RAG-ready**: Fields designed for embedding and semantic search
- **Future-proof**: Structure prepared for RAG pipeline integration
- **Consistent**: Matches Chapter 1 pattern for maintainability

---

### 5.2 Chunk File Preparation

**File**: `backend/app/content/chapters/chapter_2_chunks.py`

**Current State**: Exists from Feature 011 with placeholder function

**Required Updates**:
- Verify function exists: `get_chapter_chunks(chapter_id: int = 2) -> List[str]`
- Verify placeholder return: `["TODO: chunk 1", "TODO: chunk 2"]`
- Verify comprehensive TODO comments for future chunking implementation

**Future Chunking** (not this feature):
- Load Chapter 2 MDX content
- Implement chunking strategy (section-based, semantic, or overlapping windows)
- Generate embeddings for chunks
- Store in Qdrant collection "chapter_2"
- Return chunks with metadata (section_id, position, word_count)

**Rationale**:
- **Placeholder only**: Real chunking implementation in future feature
- **Structure ready**: Function signature and TODOs prepare for implementation
- **RAG integration**: Chunks will feed into RAG pipeline (Feature 012)

---

## 6. Consistency Rules

### 6.1 Must Follow Course Syllabus

**Decision**: Structure must align with course document provided (referenced but not implemented in this feature)

**Course Syllabus Alignment**:
- Chapter 2 covers ROS 2 fundamentals
- Topics: nodes, topics, services, actions, packages, launch files
- Prerequisites: Chapter 1 (Physical AI & Robotics introduction)
- Difficulty: Beginner level
- Learning outcomes: ROS 2 communication mechanisms, package structure, launch workflows

**Rationale**:
- **Syllabus compliance**: Structure must support course learning objectives
- **Future content**: Real content will be written following course document
- **Consistency**: Structure prepares for content that matches syllabus

**Note**: Course document not provided in this feature - structure is generic but syllabus-compliant.

---

### 6.2 Must Match Chapter 1 Structure Style

**Decision**: Replicate Chapter 1 structure pattern exactly, but with Chapter 2 content focus

**Chapter 1 Structure** (Feature 003):
- 7 H2 sections
- 4 diagram placeholders (kebab-case)
- 4 AI-block placeholders (HTML comments in Feature 003, React components in Feature 011)
- 1 glossary section with 7 terms
- YAML frontmatter with standard fields
- Backend metadata with RAG-ready fields

**Chapter 2 Structure** (This Feature):
- 7 H2 sections (same count)
- 4 diagram placeholders (kebab-case, same count)
- 4 AI-block components (React components, same count, chapterId={2})
- 1 glossary section with 7 terms (same count)
- YAML frontmatter with standard fields (same structure)
- Backend metadata with RAG-ready fields (same structure)

**Consistency Points**:
- **Section count**: Both have 7 sections
- **Placeholder count**: Both have 4 diagrams and 4 AI blocks
- **Glossary count**: Both have 7 terms
- **Frontmatter**: Same fields (title, description, sidebar_position, sidebar_label, tags)
- **Metadata**: Same fields (id, title, summary, section_count, sections, ai_blocks, diagram_placeholders, difficulty_level, prerequisites, learning_outcomes, glossary_terms)

**Differences** (acceptable):
- **Content focus**: Chapter 1 = Physical AI, Chapter 2 = ROS 2
- **Analogies**: Chapter 1 = general robotics, Chapter 2 = ROS 2-specific (post office, restaurant, radio, phone calls, package delivery)
- **Prerequisites**: Chapter 1 = `[]`, Chapter 2 = `[1]`
- **AI blocks**: Chapter 1 used HTML comments (Feature 003), Chapter 2 uses React components (Feature 011)

---

### 6.3 No Real Content Yet

**Decision**: This feature creates structure only, no actual content text

**Structure-Only Approach**:
- All content MUST be placeholder comments
- Placeholders MUST describe what content should be written
- Placeholders MUST include requirements (word count, analogies, examples)
- No actual paragraphs, sentences, or definitions

**Rationale**:
- **Clear separation**: Structure (this feature) vs. content writing (future feature)
- **Framework first**: Establish structure before writing content
- **Validation focus**: This feature validates structure, not content quality

**Future Content Writing**:
- Content will be written in future feature following placeholders
- Content will follow research.md guidelines (7th-8th grade, ROS 2 analogies)
- Content will integrate with AI blocks and diagrams

---

## 7. File & Folder Plan

### 7.1 Files to Create

```
frontend/docs/chapters/
└── chapter-2.mdx                    # NEW or UPDATE: MDX skeleton with 7 sections, placeholders

backend/app/content/chapters/
├── chapter_2.py                     # NEW or UPDATE: Python metadata dictionary
└── chapter_2_chunks.py              # VERIFY: Exists from Feature 011, verify placeholder function

specs/014-chapter-2-content/
├── spec.md                          # ✅ EXISTS: Feature specification
├── plan.md                          # ✅ THIS FILE: Architecture plan
├── research.md                      # ✅ EXISTS: Research document
├── data-model.md                    # ✅ EXISTS: Data model
├── quickstart.md                    # ✅ EXISTS: Quickstart guide
├── contracts/
│   └── content-schema.md            # ✅ EXISTS: Content schema contract
└── checklists/
    └── requirements.md              # ✅ EXISTS: Requirements checklist
```

### 7.2 Files to Update

**If chapter-2.mdx exists from Feature 010**:
- Update section count from 9 to 7 (remove or merge Learning Objectives and Summary)
- Verify all placeholders match spec requirements
- Verify AI-block components use React components (not HTML comments)
- Verify diagram placeholders use kebab-case

**If chapter_2.py exists from Feature 010**:
- Update `section_count` from 9 to 7
- Update `sections` list to match 7-section structure
- Verify all fields match spec requirements
- Verify `prerequisites` is `[1]`

**If chapter_2_chunks.py exists from Feature 011**:
- Verify placeholder function exists
- Verify comprehensive TODO comments
- No changes needed (already has placeholder)

### 7.3 File Modification Summary

**New Files**: 0-2 files (depending on what exists from Feature 010/011)
- `chapter-2.mdx` - May need creation or update
- `chapter_2.py` - May need creation or update

**Updated Files**: 0-2 files
- `chapter-2.mdx` - Update to 7 sections if exists
- `chapter_2.py` - Update metadata if exists

**Verified Files**: 1 file
- `chapter_2_chunks.py` - Verify placeholder function

**Contract Files**: 5 files (all created in spec phase)
- `content-schema.md` - ✅ Created
- `checklists/requirements.md` - ✅ Created
- `research.md` - ✅ Created
- `data-model.md` - ✅ Created
- `quickstart.md` - ✅ Created

**Total**: ~100-200 lines of structure code (MDX skeleton, Python metadata, placeholders)

---

## 8. Risks / Constraints

### 8.1 Risk Assessment

#### Risk 1: Existing chapter-2.mdx Has 9 Sections, Spec Requires 7
**Severity**: Medium
**Probability**: High
**Impact**: Medium

**Description**: Existing `chapter-2.mdx` from Feature 010 has 9 sections (includes separate Learning Objectives and Summary), but spec requires exactly 7 sections.

**Mitigation**:
- Option A: Update existing file to 7 sections (remove/merge Learning Objectives and Summary)
- Option B: Update spec to match existing structure (requires spec change)
- Option C: Keep 7 content sections + 2 standard sections (Learning Objectives, Summary) but don't count standard sections as separate H2
- **Recommendation**: Follow spec requirement (7 sections) and update existing file

#### Risk 2: No Real Content Allowed at This Stage
**Severity**: Low
**Probability**: Low
**Impact**: Low

**Description**: This is a structure-only feature. No actual content text should be written.

**Mitigation**:
- Clear placeholder comments describing what content should be written
- Validation checks ensure no actual text (only placeholders)
- Code review to ensure structure-only approach

#### Risk 3: Metadata Mismatch with Existing File
**Severity**: Medium
**Probability**: Medium
**Impact**: Medium

**Description**: Existing `chapter_2.py` from Feature 010 may have `section_count: 9` but spec requires `section_count: 7`.

**Mitigation**:
- Verify existing metadata file
- Update `section_count` and `sections` list to match 7-section structure
- Ensure all fields match spec requirements
- Cross-validate MDX and metadata

#### Risk 4: AI-Block Component Integration
**Severity**: Low
**Probability**: Low
**Impact**: Low

**Description**: AI blocks must use React components from Feature 011 (not HTML comments).

**Mitigation**:
- Verify components exist from Feature 011
- Use correct component props (chapterId={2}, sectionId, concept, diagramType)
- Import components at top of MDX file
- Validate components render correctly in Docusaurus

#### Risk 5: Diagram Placeholder Naming Inconsistency
**Severity**: Low
**Probability**: Low
**Impact**: Low

**Description**: Diagram placeholders must use kebab-case naming.

**Mitigation**:
- Enforce kebab-case in validation
- Provide examples of correct naming
- Validate against regex pattern
- Cross-check with metadata `diagram_placeholders` list

---

## 9. Acceptance Criteria Mapping

### 9.1 Success Criteria

- ✅ Chapter 2 MDX file exists with correct skeleton (7 H2 sections, 4 AI blocks, 4 diagrams, glossary)
- ✅ Metadata file imports in backend without errors
- ✅ Chunk file exists with TODO list
- ✅ Contracts folder created with correct templates
- ✅ All placeholders, AI-block markers, and diagrams validated
- ✅ No actual content text written (only structure and placeholders)

### 9.2 Validation Steps

1. **MDX Structure Validation**:
   - Count H2 sections (must be 7)
   - Count diagram placeholders (must be 4, kebab-case)
   - Count AI-block components (must be 4, chapterId={2})
   - Count glossary term placeholders (must be 7)
   - Verify all content is placeholder comments

2. **Metadata Validation**:
   - Import test: `from app.content.chapters.chapter_2 import CHAPTER_METADATA`
   - Verify `id` is 2
   - Verify `section_count` is 7
   - Verify `sections` list has 7 items
   - Verify `ai_blocks` has 4 items
   - Verify `diagram_placeholders` has 4 items
   - Verify `prerequisites` is `[1]`
   - Verify `glossary_terms` has 7 items

3. **Chunk File Validation**:
   - Import test: `from app.content.chapters.chapter_2_chunks import get_chapter_chunks`
   - Verify function returns List[str] (placeholder)
   - Verify TODO comments present

4. **Docusaurus Build Validation**:
   - Run `npm run build` in frontend
   - Verify build completes without errors
   - Verify Chapter 2 appears in navigation

5. **Contract Files Validation**:
   - Verify all 5 contract files exist
   - Verify files follow templates from Feature 003
   - Verify Chapter 2-specific content included

---

## 10. Dependencies & Risks

### 10.1 Dependencies

- **Feature 003** (Chapter 1 Content): Provides template structure and patterns
- **Feature 010** (Chapter 2 Content): May have created initial structure (to be validated/updated)
- **Feature 011** (Chapter 2 AI Blocks): Provides React components for AI blocks
- **Feature 012** (Chapter 2 RAG): May have created chunk file (to be verified)

### 10.2 Blocking Dependencies

- None (all dependencies already exist or are optional)

### 10.3 Future Dependencies

- Real content writing (future feature)
- Real chunking implementation (future feature)
- Real diagram generation (future feature)

---

## 11. Next Steps

1. Run `/sp.tasks` to generate implementation tasks
2. Review tasks.md for atomic task breakdown
3. Run `/sp.implement` to implement structure
4. Validate all files updated correctly
5. Test Docusaurus build and Python imports

---

**Status**: Plan complete, ready for `/sp.tasks`
