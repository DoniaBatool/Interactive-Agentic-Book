# Tasks: Chapter 2 Written Content — Structure, Metadata, Schema & Contracts

**Feature**: 014-chapter-2-content | **Branch**: `014-chapter-2-content` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating Chapter 2 content structure (scaffolding only, no real content text).

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

**Purpose**: Verify dependencies and prerequisites before implementing Chapter 2 content structure.

- [ ] [T001] [P1] [SETUP] Verify Docusaurus frontend is functional: Run `cd frontend && npm run build` to confirm build succeeds
- [ ] [T002] [P1] [SETUP] Verify backend directory structure exists: Check that `backend/app/content/chapters/` directory exists
- [ ] [T003] [P1] [SETUP] Verify Chapter 1 exists: Check that `frontend/docs/chapters/chapter-1.mdx` exists (template reference)
- [ ] [T004] [P1] [SETUP] Verify Chapter 1 metadata exists: Check that `backend/app/content/chapters/chapter_1.py` exists (template reference)
- [ ] [T005] [P1] [SETUP] Verify React components exist: Check that `frontend/src/components/ai/AskQuestionBlock.tsx`, `ExplainLike10Block.tsx`, `InteractiveQuizBlock.tsx`, `GenerateDiagramBlock.tsx` exist (from Feature 011)
- [ ] [T006] [P1] [SETUP] Check existing chapter-2.mdx: Verify if `frontend/docs/chapters/chapter-2.mdx` exists from Feature 010 (may have 9 sections, needs update to 7)
- [ ] [T007] [P1] [SETUP] Check existing chapter_2.py: Verify if `backend/app/content/chapters/chapter_2.py` exists from Feature 010 (may need update)
- [ ] [T008] [P1] [SETUP] Check existing chapter_2_chunks.py: Verify if `backend/app/content/chapters/chapter_2_chunks.py` exists from Feature 011
- [ ] [T009] [P1] [SETUP] Verify contract files exist: Check that `specs/014-chapter-2-content/contracts/content-schema.md` and other contract files exist (created in spec phase)

**Success Criteria**:
- All prerequisite files and directories exist
- Existing files identified for potential updates
- Ready to create/update structure files

**Dependencies**: Feature 003 (Chapter 1 Content), Feature 010 (Chapter 2 Content), Feature 011 (Chapter 2 AI Blocks)

---

## PHASE 1 — MDX Skeleton

**User Story**: US1 - Content Developer Creates Chapter 2 Structure

**Test Strategy**: Can be tested by creating/updating MDX file with correct structure and verifying build succeeds.

### Create or Update MDX File with Frontmatter

- [ ] [T010] [P1] [US1] Create or update `frontend/docs/chapters/chapter-2.mdx` with YAML frontmatter:
  - Add or verify: `title: "Chapter 2 — ROS 2 Fundamentals"`
  - Add or verify: `description: "Learn ROS 2 fundamentals including nodes, topics, services, actions, packages, and launch files for robotics development"`
  - Add or verify: `sidebar_position: 2`
  - Add or verify: `sidebar_label: "Chapter 2: ROS 2 Fundamentals"`
  - Add or verify: `tags: ["ros2", "robotics", "programming", "beginner"]`

- [ ] [T011] [P1] [US1] Add React component imports to `frontend/docs/chapters/chapter-2.mdx`:
  - Add: `import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';`
  - Add: `import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';`
  - Add: `import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';`
  - Add: `import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';`

### Create Section 1 - Introduction to ROS 2

- [ ] [T012] [P1] [US1] Add Section 1 to `frontend/docs/chapters/chapter-2.mdx`:
  - Add H2 heading: `## Introduction to ROS 2 {#introduction-to-ros2}`
  - Add content placeholder comment: `<!-- Content placeholder: Definition of ROS 2, why ROS 2 exists, differences from ROS 1, and at least 3 real-world examples of ROS 2 usage (TurtleBot 3, navigation stack, etc.). Use post office analogy for communication system. Min 200 words, 7th-8th grade level. -->`
  - Add diagram placeholder: `<!-- DIAGRAM: ros2-ecosystem-overview -->`
  - Add AI block component: `<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />`

### Create Section 2 - Nodes and Node Communication

- [ ] [T013] [P1] [US1] Add Section 2 to `frontend/docs/chapters/chapter-2.mdx`:
  - Add H2 heading: `## Nodes and Node Communication {#nodes-and-node-communication}`
  - Add content placeholder comment: `<!-- Content placeholder: Explanation of what nodes are, how nodes communicate, node lifecycle, and examples using restaurant analogy (each chef = node). Min 200 words. -->`
  - Add diagram placeholder: `<!-- DIAGRAM: node-communication-architecture -->`
  - Add AI block component: `<GenerateDiagramBlock diagramType="node-communication-architecture" chapterId={2} />`

### Create Section 3 - Topics and Messages

- [ ] [T014] [P1] [US1] Add Section 3 to `frontend/docs/chapters/chapter-2.mdx`:
  - Add H2 heading: `## Topics and Messages {#topics-and-messages}`
  - Add content placeholder comment: `<!-- Content placeholder: Explanation of topics (publish/subscribe), message types, topic naming conventions, and practical examples using radio broadcast analogy. Min 200 words. -->`
  - Add AI block component: `<ExplainLike10Block concept="topics" chapterId={2} />`
  - Add diagram placeholder: `<!-- DIAGRAM: topic-pubsub-flow -->`

### Create Section 4 - Services and Actions

- [ ] [T015] [P1] [US1] Add Section 4 to `frontend/docs/chapters/chapter-2.mdx`:
  - Add H2 heading: `## Services and Actions {#services-and-actions}`
  - Add content placeholder comment: `<!-- Content placeholder: Explanation of services (request/response), actions (long-running tasks), differences between topics/services/actions, when to use each, examples using phone call (services) and package delivery (actions) analogies. Min 200 words. -->`
  - Add diagram placeholder: `<!-- DIAGRAM: services-actions-comparison -->`
  - Add AI block component: `<InteractiveQuizBlock chapterId={2} numQuestions={5} />`

### Create Section 5 - ROS 2 Packages

- [ ] [T016] [P1] [US1] Add Section 5 to `frontend/docs/chapters/chapter-2.mdx`:
  - Add H2 heading: `## ROS 2 Packages {#ros2-packages}`
  - Add content placeholder comment: `<!-- Content placeholder: Explanation of ROS 2 packages, package structure, dependencies, and how packages organize code. Min 200 words. -->`
  - No diagram or AI block (content-only section)

### Create Section 6 - Launch Files and Workflows

- [ ] [T017] [P1] [US1] Add Section 6 to `frontend/docs/chapters/chapter-2.mdx`:
  - Add H2 heading: `## Launch Files and Workflows {#launch-files-and-workflows}`
  - Add content placeholder comment: `<!-- Content placeholder: Explanation of launch files, how to start multiple nodes, real-world robotics workflows, and common patterns. Min 200 words. -->`
  - No diagram or AI block (content-only section)

### Create Section 7 - Glossary

- [ ] [T018] [P1] [US1] Add Section 7 (Glossary) to `frontend/docs/chapters/chapter-2.mdx`:
  - Add H2 heading: `## Glossary {#glossary}`
  - Add content placeholder comment listing 7 terms:
    ```markdown
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

### Handle Existing File Discrepancy (if chapter-2.mdx exists with 9 sections)

- [ ] [T019] [P1] [US1] If `frontend/docs/chapters/chapter-2.mdx` exists with 9 sections, update to 7 sections:
  - Remove or merge "Learning Objectives" section (Section 7) - content can be merged into Glossary or removed
  - Remove or merge "Summary" section (Section 8) - content can be merged into Glossary or removed
  - Keep only 7 H2 sections: Introduction, Nodes, Topics, Services, Packages, Launch Files, Glossary
  - Verify section count is exactly 7

- [ ] [T020] [P1] [US1] Verify MDX file has exactly 7 H2 sections: Run `grep -c "^## " frontend/docs/chapters/chapter-2.mdx` or manually count H2 headings

- [ ] [T021] [P1] [US1] Verify all content is placeholder comments: Check that no actual text content exists (only `<!-- Content placeholder: ... -->` comments)

**Acceptance Test**: MDX file has correct frontmatter, exactly 7 H2 sections, 4 diagram placeholders, 4 AI-block components, glossary with 7 placeholder terms, all content is placeholder comments

---

## PHASE 2 — Backend Metadata

**User Story**: US1 - Content Developer Creates Chapter 2 Structure

**Test Strategy**: Can be tested by creating/updating metadata file and verifying imports work.

### Create or Update Metadata File

- [ ] [T022] [P1] [US1] Create or update `backend/app/content/chapters/chapter_2.py` with module docstring:
  - Add: `"""Chapter 2 metadata for RAG integration and content management."""`
  - Add: `"""This module contains structured metadata for Chapter 2: "ROS 2 Fundamentals" including section information, placeholder tracking, and learning objectives."""`

- [ ] [T023] [P1] [US1] Add imports to `backend/app/content/chapters/chapter_2.py`:
  - Add: `from typing import List`

- [ ] [T024] [P1] [US1] Create `CHAPTER_METADATA` dictionary in `backend/app/content/chapters/chapter_2.py` with core identification:
  - Add: `"id": 2`
  - Add: `"title": "Chapter 2 — ROS 2 Fundamentals"` (must match MDX frontmatter exactly)
  - Add: `"summary": "An introductory chapter covering ROS 2 fundamentals including nodes, topics, services, actions, packages, and launch files. Explores how ROS 2 enables robot communication through publish/subscribe topics, request/response services, and long-running actions. Suitable for beginners with Chapter 1 prerequisite."`

- [ ] [T025] [P1] [US1] Add structure information to `CHAPTER_METADATA` in `backend/app/content/chapters/chapter_2.py`:
  - Add: `"section_count": 7`
  - Add: `"sections": ["Introduction to ROS 2", "Nodes and Node Communication", "Topics and Messages", "Services and Actions", "ROS 2 Packages", "Launch Files and Workflows", "Glossary"]`

- [ ] [T026] [P1] [US1] Add placeholder tracking to `CHAPTER_METADATA` in `backend/app/content/chapters/chapter_2.py`:
  - Add: `"ai_blocks": ["ask-question", "generate-diagram", "explain-like-i-am-10", "interactive-quiz"]`
  - Add: `"diagram_placeholders": ["ros2-ecosystem-overview", "node-communication-architecture", "topic-pubsub-flow", "services-actions-comparison"]`

- [ ] [T027] [P1] [US1] Add versioning to `CHAPTER_METADATA` in `backend/app/content/chapters/chapter_2.py`:
  - Add: `"last_updated": "2025-12-05T00:00:00Z"` (ISO 8601 format)

- [ ] [T028] [P1] [US1] Add RAG-specific metadata to `CHAPTER_METADATA` in `backend/app/content/chapters/chapter_2.py`:
  - Add: `"difficulty_level": "beginner"`
  - Add: `"prerequisites": [1]` (Chapter 1 is prerequisite)
  - Add: `"learning_outcomes": ["Define ROS 2 and explain its role in robotics development", "Explain how nodes communicate in a ROS 2 system", "Distinguish between topics, services, and actions", "Identify when to use each communication mechanism", "Describe ROS 2 package structure and organization", "Explain how launch files coordinate multiple nodes"]`
  - Add: `"glossary_terms": ["ROS 2", "Node", "Topic", "Service", "Action", "Package", "Launch File"]`

### Handle Existing File Discrepancy (if chapter_2.py exists with section_count: 9)

- [ ] [T029] [P1] [US1] If `backend/app/content/chapters/chapter_2.py` exists with `section_count: 9`, update to match 7-section structure:
  - Update: `"section_count": 7`
  - Update: `"sections"` list to have 7 items matching MDX order
  - Remove "Learning Objectives" and "Summary" from sections list if present

- [ ] [T030] [P1] [US1] Verify metadata file imports successfully: Run `cd backend && python -c "from app.content.chapters.chapter_2 import CHAPTER_METADATA; print('Import successful'); print(f'Chapter ID: {CHAPTER_METADATA[\"id\"]}'); print(f'Sections: {len(CHAPTER_METADATA[\"sections\"])}')"` - should complete without errors

- [ ] [T031] [P1] [US1] Verify metadata matches MDX structure:
  - Verify `section_count` is 7
  - Verify `sections` list has 7 items matching MDX H2 headings
  - Verify `ai_blocks` has 4 items matching component types
  - Verify `diagram_placeholders` has 4 items matching placeholder names
  - Verify `glossary_terms` has 7 items

**Acceptance Test**: Metadata file imports without errors, all fields match spec requirements, section_count is 7, sections list matches MDX order

---

## PHASE 3 — Chunk Source

**User Story**: US1 - Content Developer Creates Chapter 2 Structure

**Test Strategy**: Can be tested by verifying chunk file exists with placeholder function.

### Verify or Create Chunk File

- [ ] [T032] [P1] [US1] Verify `backend/app/content/chapters/chapter_2_chunks.py` exists (from Feature 011):
  - Check file exists at path
  - If exists, verify it has placeholder function

- [ ] [T033] [P1] [US1] If `backend/app/content/chapters/chapter_2_chunks.py` does not exist, create it with:
  - Module docstring: `"""Chapter 2 Content Chunks - Provides chapter content chunks for RAG pipeline."""`
  - Import: `from typing import List`
  - Function: `def get_chapter_chunks(chapter_id: int = 2) -> List[str]:`
  - Placeholder return: `return ["TODO: chunk 1", "TODO: chunk 2"]`
  - Comprehensive TODO comments for future chunking implementation

- [ ] [T034] [P1] [US1] Verify chunk file function signature: Check that `get_chapter_chunks(chapter_id: int = 2) -> List[str]` exists

- [ ] [T035] [P1] [US1] Verify chunk file returns placeholder: Run `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; chunks = get_chapter_chunks(2); assert isinstance(chunks, list), 'Should return list'; print('Placeholder return verified')"` - should complete without errors

**Acceptance Test**: Chunk file exists with placeholder function, imports work, function returns List[str] placeholder

---

## PHASE 4 — Contracts Folder

**User Story**: US2 - System Validates Chapter 2 Structure

**Test Strategy**: Can be tested by verifying all contract files exist and follow templates.

### Verify Contract Files Exist (All Created in Spec Phase)

- [ ] [T036] [P2] [US2] Verify `specs/014-chapter-2-content/contracts/content-schema.md` exists:
  - Check file exists
  - Verify it follows Feature 003 template
  - Verify it includes Chapter 2-specific schemas

- [ ] [T037] [P2] [US2] Verify `specs/014-chapter-2-content/checklists/requirements.md` exists:
  - Check file exists
  - Verify it follows Feature 003 template
  - Verify it includes Chapter 2-specific validation criteria

- [ ] [T038] [P2] [US2] Verify `specs/014-chapter-2-content/research.md` exists:
  - Check file exists
  - Verify it follows Feature 003 template
  - Verify it includes ROS 2-specific content guidelines

- [ ] [T039] [P2] [US2] Verify `specs/014-chapter-2-content/data-model.md` exists:
  - Check file exists
  - Verify it follows Feature 003 template
  - Verify it includes Chapter 2-specific entity definitions

- [ ] [T040] [P2] [US2] Verify `specs/014-chapter-2-content/quickstart.md` exists:
  - Check file exists
  - Verify it follows Feature 003 template
  - Verify it includes Chapter 2-specific implementation steps

**Acceptance Test**: All 5 contract files exist, follow templates, include Chapter 2-specific content

---

## PHASE 5 — Validation

**User Story**: US1, US2, US3 - All User Stories

**Test Strategy**: Comprehensive validation of all structure files.

### MDX Structure Validation

- [ ] [T041] [P1] [US1] Verify MDX file has exactly 7 H2 sections:
  - Run: `grep -c "^## " frontend/docs/chapters/chapter-2.mdx` or manually count
  - Expected: 7 sections

- [ ] [T042] [P1] [US1] Verify MDX file has exactly 4 diagram placeholders:
  - Run: `grep -c "<!-- DIAGRAM:" frontend/docs/chapters/chapter-2.mdx` or manually count
  - Expected: 4 placeholders
  - Verify all use kebab-case naming

- [ ] [T043] [P1] [US1] Verify MDX file has exactly 4 AI-block components:
  - Run: `grep -c "chapterId={2}" frontend/docs/chapters/chapter-2.mdx` or manually count
  - Expected: 4 components
  - Verify all have `chapterId={2}`

- [ ] [T044] [P1] [US1] Verify MDX file has glossary section with 7 placeholder terms:
  - Check Glossary section exists
  - Check placeholder comment lists 7 terms: ROS 2, Node, Topic, Service, Action, Package, Launch File

- [ ] [T045] [P1] [US1] Verify all content is placeholder comments:
  - Check that no actual text paragraphs exist
  - All content should be `<!-- Content placeholder: ... -->` comments

### Metadata Validation

- [ ] [T046] [P1] [US1] Verify metadata file imports successfully:
  - Run: `cd backend && python -c "from app.content.chapters.chapter_2 import CHAPTER_METADATA; print('Import successful')"` - should complete without errors

- [ ] [T047] [P1] [US1] Verify metadata fields match spec:
  - Verify `id` is 2
  - Verify `title` matches MDX frontmatter exactly
  - Verify `section_count` is 7
  - Verify `sections` list has 7 items
  - Verify `ai_blocks` has 4 items
  - Verify `diagram_placeholders` has 4 items
  - Verify `prerequisites` is `[1]`
  - Verify `glossary_terms` has 7 items

### Cross-Validation

- [ ] [T048] [P1] [US1] Verify MDX section count matches metadata:
  - Count H2 sections in MDX (should be 7)
  - Check metadata `section_count` (should be 7)
  - Verify they match

- [ ] [T049] [P1] [US1] Verify MDX section titles match metadata:
  - Extract H2 headings from MDX
  - Compare with metadata `sections` list
  - Verify order and titles match exactly

- [ ] [T050] [P1] [US1] Verify MDX diagram placeholders match metadata:
  - Extract diagram placeholder names from MDX
  - Compare with metadata `diagram_placeholders` list
  - Verify all match (kebab-case)

- [ ] [T051] [P1] [US1] Verify MDX AI-block types match metadata:
  - Extract AI-block component types from MDX
  - Compare with metadata `ai_blocks` list
  - Verify all match

- [ ] [T052] [P1] [US1] Verify MDX glossary terms match metadata:
  - Extract glossary terms from MDX placeholder comment
  - Compare with metadata `glossary_terms` list
  - Verify all 7 terms match

### Docusaurus Build Validation

- [ ] [T053] [P1] [US1] Verify Docusaurus build succeeds:
  - Run: `cd frontend && npm run build`
  - Expected: Build completes without errors
  - Expected: Chapter 2 appears in navigation

- [ ] [T054] [P1] [US1] Verify Chapter 2 page renders:
  - Navigate to `http://localhost:3000/docs/chapters/chapter-2` (if dev server running)
  - Or verify build output includes chapter-2 page
  - Expected: Page renders with 7 sections visible

### Chunk File Validation

- [ ] [T055] [P1] [US1] Verify chunk file imports successfully:
  - Run: `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; print('Import successful')"` - should complete without errors

- [ ] [T056] [P1] [US1] Verify chunk file returns placeholder:
  - Run: `cd backend && python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks; chunks = get_chapter_chunks(2); assert isinstance(chunks, list), 'Should return list'; print('Placeholder return verified')"` - should complete without errors

### Consistency Validation

- [ ] [T057] [P1] [US1] Verify structure matches Chapter 1 pattern:
  - Compare section count (both should be 7)
  - Compare diagram count (both should be 4)
  - Compare AI-block count (both should be 4)
  - Compare glossary count (both should be 7)
  - Compare frontmatter structure (same fields)
  - Compare metadata structure (same fields)

- [ ] [T058] [P1] [US1] Verify no real content text exists:
  - Check MDX file for actual paragraphs (not placeholder comments)
  - Expected: Only placeholder comments, no actual text

**Acceptance Test**: All validations pass, MDX structure matches spec, metadata matches MDX, build succeeds, imports work, structure matches Chapter 1 pattern, no real content text

---

## Summary

**Total Tasks**: 58 tasks across 5 phases
- Phase 0: Setup & Prerequisites (9 tasks)
- Phase 1: MDX Skeleton (11 tasks)
- Phase 2: Backend Metadata (10 tasks)
- Phase 3: Chunk Source (4 tasks)
- Phase 4: Contracts Folder (5 tasks)
- Phase 5: Validation (19 tasks)

**Estimated Time**: ~1-2 hours (structure creation only, no content writing)

**Success Criteria**:
- Chapter 2 MDX file exists with correct skeleton (7 H2 sections, 4 AI blocks, 4 diagrams, glossary)
- Metadata file imports in backend without errors
- Chunk file exists with TODO list
- Contracts folder created with correct templates (all created in spec phase)
- All placeholders, AI-block markers, and diagrams validated
- No actual content text written (only structure and placeholders)
- Structure matches Chapter 1 pattern exactly

**Next Step**: Run `/sp.implement` to execute all tasks
