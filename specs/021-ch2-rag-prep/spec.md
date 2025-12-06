# Feature Specification: Chapter 2 — RAG Chunking, Embedding Prep & Knowledge Source Scaffolding

**Feature Branch**: `021-ch2-rag-prep`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "Establish the complete RAG preparation layer for Chapter 2. This includes chunking strategy, embedding markers inside MDX, chapter_2_chunks.py, and the required scaffolding for retrieval integration."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Content Developer Prepares Chapter 2 for RAG (Priority: P1)

As a content developer, I need to add chunk markers to Chapter 2 MDX content and ensure the chunking blueprint file is ready, so that the RAG pipeline can properly retrieve and embed Chapter 2 content for semantic search.

**Why this priority**: This establishes the foundation for Chapter 2 RAG operations. Without proper chunk markers and chunking strategy, the RAG pipeline cannot effectively retrieve relevant content for AI blocks.

**Independent Test**: Can be fully tested by verifying chunk markers exist in MDX file following regex pattern `<!-- CHUNK: [0-9]+ -->`, MDX builds successfully, chapter_2_chunks.py imports without errors, and RAG pipeline has TODO hooks for Chapter 2.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `frontend/docs/chapters/chapter-2.mdx`, **Then** I see:
   - Chunk markers `<!-- CHUNK: x -->` before logical paragraph groups (6-8 markers)
   - Existing `<!-- DIAGRAM: ... -->` markers remain intact
   - Existing AI-block components remain intact
   - Section count matches metadata file (7 sections)

2. **Given** the feature is implemented, **When** I check `backend/app/content/chapters/chapter_2_chunks.py`, **Then** I see:
   - Function `get_chapter_2_chunks()` exists (or `get_chapter_chunks(chapter_id=2)`)
   - TODO comments on chunk size rules (120-220 words)
   - TODO comments on semantic grouping
   - TODO comments on embedding guidelines
   - TODO comments on retrieval linking (future)

3. **Given** the feature is implemented, **When** I check `backend/app/ai/rag/pipeline.py`, **Then** I see:
   - TODO handler for registering Chapter 2 collection name
   - TODO handler for preparing chapter-specific embedding batch
   - TODO placeholder search function for Chapter 2

4. **Given** the feature is implemented, **When** I build the frontend, **Then**:
   - MDX file compiles without errors
   - All chunk markers follow regex pattern `<!-- CHUNK: [0-9]+ -->`
   - Section counts match metadata

### User Story 2 - System Administrator Validates RAG Preparation (Priority: P2)

As a system administrator, I need to validate that Chapter 2 RAG preparation is complete and ready for embedding generation, so that I can ensure the RAG pipeline will work correctly when implemented.

**Why this priority**: Validation ensures the scaffolding is correct before implementing actual RAG logic.

**Independent Test**: Can be tested by running validation checks on MDX structure, chunk markers, and import verification.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I run validation checks, **Then**:
   - MDX builds successfully
   - Chunk markers follow regex pattern
   - All section counts match metadata
   - chapter_2_chunks.py imports cleanly

---

## Functional Requirements

### FR-001: MDX Chunk Markers

**Priority**: P1

**Description**: Update Chapter 2 MDX file with chunk markers before logical paragraph groups.

**Requirements**:
- Insert `<!-- CHUNK: x -->` markers before logical paragraph groups (6-8 markers total)
- Markers must follow regex pattern: `<!-- CHUNK: [0-9]+ -->`
- Preserve existing `<!-- DIAGRAM: ... -->` markers
- Preserve existing AI-block components
- Ensure sections match metadata file (7 sections)

**Input**: `frontend/docs/chapters/chapter-2.mdx` (existing file)

**Output**: Updated MDX file with chunk markers

**Validation**:
- MDX must build successfully after markers are added
- Chunk markers must follow regex pattern
- All section counts must match metadata

**Dependencies**: Feature 014 (Chapter 2 Content) - MDX file must exist

---

### FR-002: Chunking Blueprint File

**Priority**: P1

**Description**: Create or update `backend/app/content/chapters/chapter_2_chunks.py` with chunking strategy documentation and TODO function.

**Requirements**:
- Function `get_chapter_2_chunks()` or `get_chapter_chunks(chapter_id=2)` exists
- Include TODO comments on:
  - Chunk size rules (120-220 words per chunk)
  - Semantic grouping (group by semantic topic, not paragraph count)
  - Embedding guidelines (future embedding generation)
  - Retrieval linking (future RAG ingestion)

**Input**: Existing `chapter_2_chunks.py` file (from Feature 012)

**Output**: Updated chunk file with enhanced TODO comments

**Validation**:
- File must import cleanly
- Function signature must be correct
- TODO comments must be descriptive

**Dependencies**: Feature 012 (Chapter 2 RAG) - chunk file may already exist

---

### FR-003: Embedding Prep Contracts

**Priority**: P1

**Description**: Create `specs/021-ch2-rag-prep/contracts/rag-prep-schema.md` documenting chunk marker contract, placeholder contract, embedding boundaries, and retrieval context rules.

**Requirements**:
- Document chunk marker contract (format, validation rules, placement)
- Document placeholder contract (diagram, AI-block markers)
- Document embedding boundaries (chunk size limits, semantic boundaries)
- Document retrieval context rules (how chunks are assembled for RAG)

**Input**: None (new file)

**Output**: Contract file with complete schema documentation

**Validation**:
- Contract must be complete and clear
- All rules must be testable

**Dependencies**: None

---

### FR-004: RAG Integration Hooks

**Priority**: P1

**Description**: Add TODO handlers to `backend/app/ai/rag/pipeline.py` for Chapter 2 RAG operations.

**Requirements**:
- TODO handler for registering Chapter 2 collection name
- TODO handler for preparing chapter-specific embedding batch
- TODO placeholder search function for Chapter 2

**Input**: Existing `backend/app/ai/rag/pipeline.py` file

**Output**: Updated pipeline file with Chapter 2 TODO hooks

**Validation**:
- File must import cleanly
- TODO comments must be descriptive
- No breaking changes to existing functionality

**Dependencies**: Feature 005 (AI Runtime Engine) - pipeline file must exist

---

### FR-005: Validation Requirements

**Priority**: P2

**Description**: Ensure all validation requirements are met.

**Requirements**:
- MDX must build successfully after markers are added
- Chunk markers must follow regex: `<!-- CHUNK: [0-9]+ -->`
- All section counts must match metadata
- chapter_2_chunks.py must import cleanly

**Input**: All updated files

**Output**: Validation passes

**Validation**:
- All validation checks must pass

**Dependencies**: All other functional requirements

---

## Edge Cases

1. **Chunk markers in glossary section**: Glossary entries should be grouped as single chunks, not split across markers
2. **Chunk markers near diagram placeholders**: Diagram explanations should be included in adjacent chunks
3. **Empty sections**: Sections with only placeholders should still have chunk markers
4. **Chunk marker numbering**: Chunk numbers should be sequential (1, 2, 3, ...) but can restart per section
5. **Existing chunk file**: If `chapter_2_chunks.py` already exists, update it rather than creating new

---

## Non-Functional Requirements

### NFR-001: MDX Build Stability

**Priority**: P1

**Description**: MDX file must build successfully after chunk markers are added.

**Acceptance**: Frontend build completes without errors, MDX compiles correctly.

---

### NFR-002: Import Stability

**Priority**: P1

**Description**: All Python files must import cleanly without errors.

**Acceptance**: `chapter_2_chunks.py` imports without errors, `pipeline.py` imports without errors.

---

### NFR-003: No Breaking Changes

**Priority**: P1

**Description**: No existing functionality should be broken by this feature.

**Acceptance**: Existing Chapter 1 RAG operations continue to work, existing Chapter 2 AI blocks continue to work.

---

### NFR-004: Documentation Completeness

**Priority**: P2

**Description**: All contracts and documentation must be complete and clear.

**Acceptance**: Contract file is complete, all rules are testable, documentation is clear.

---

## Assumptions

1. Chapter 2 MDX file exists from Feature 014
2. `chapter_2_chunks.py` may already exist from Feature 012 (needs update, not creation)
3. RAG pipeline file exists from Feature 005
4. Chunk markers use numbered format `<!-- CHUNK: x -->` (not START/END pairs like Chapter 3)
5. Chunk size guidelines: 120-220 words per chunk
6. Semantic grouping: group by topic, not paragraph count
7. No actual chunking logic implementation in this feature (scaffolding only)

---

## Dependencies

### Internal Dependencies

- **Feature 005** (AI Runtime Engine): RAG pipeline file must exist
- **Feature 012** (Chapter 2 RAG): Chunk file may already exist
- **Feature 014** (Chapter 2 Content): MDX file must exist
- **Feature 020** (Chapter 2 AI Runtime): RAG collection scaffolding exists

### External Dependencies

- None (scaffolding only, no external services)

---

## Out of Scope

1. **Actual chunking implementation**: This feature only adds markers and TODO comments, not real chunking logic
2. **Embedding generation**: No actual embedding API calls
3. **Qdrant operations**: No actual vector database operations
4. **RAG pipeline implementation**: Only TODO hooks, not real pipeline logic
5. **Content writing**: No actual content text is written
6. **Chunk validation logic**: Only documentation, not validation implementation
7. **Automated chunk extraction**: Only markers and strategy, not extraction code

---

## Success Criteria

1. Chapter 2 MDX contains properly structured chunk markers (6-8 markers)
2. Chunk markers follow regex pattern `<!-- CHUNK: [0-9]+ -->`
3. Chunk schema contract documented in `rag-prep-schema.md`
4. `chapter_2_chunks.py` scaffold updated with enhanced TODO comments
5. RAG pipeline updated with TODO hooks for Chapter 2
6. MDX builds successfully after markers are added
7. All files import cleanly
8. No business logic implemented (scaffolding only)

---

## Acceptance Criteria

1. ✅ Chapter 2 MDX file has chunk markers before logical paragraph groups
2. ✅ Chunk markers follow regex pattern `<!-- CHUNK: [0-9]+ -->`
3. ✅ Existing diagram and AI-block markers remain intact
4. ✅ Section count matches metadata (7 sections)
5. ✅ `chapter_2_chunks.py` has enhanced TODO comments on chunking strategy
6. ✅ `pipeline.py` has TODO hooks for Chapter 2 RAG operations
7. ✅ Contract file `rag-prep-schema.md` documents all rules
8. ✅ MDX builds successfully
9. ✅ All Python files import cleanly
10. ✅ No breaking changes to existing functionality

---

## Notes

- This feature focuses on **scaffolding only** - no actual chunking, embedding, or RAG logic implementation
- Chunk markers use numbered format (`<!-- CHUNK: x -->`) as specified in requirements
- Chunk size guidelines: 120-220 words per chunk (from plan section)
- Semantic grouping: group by topic, not paragraph count
- Chapter 3 uses START/END markers, but Chapter 2 uses numbered markers per requirements
