# Release Schema: Chapter 2 Release Packaging

**Feature**: 016-chapter-2-release-package
**Created**: 2025-12-05
**Type**: Release Engineering / Packaging

## Overview

This contract defines the release packaging schema for Chapter 2. All release components follow a consistent structure with copy-only operations (no code modifications).

## Release Folder Structure

### Directory Layout

```
releases/chapter-2/
├── README.md                    # Package documentation
├── content/                     # MDX content files
│   └── chapter-2.mdx
├── metadata/                    # Chapter metadata
│   └── chapter_2.py
├── rag/                         # RAG chunk files
│   └── chapter_2_chunks.py
├── ai-blocks/                   # AI runtime components
│   ├── ai_blocks.py            # (Chapter 2 excerpts)
│   ├── ch2_ask_question_agent.py
│   ├── ch2_explain_el10_agent.py
│   ├── ch2_quiz_agent.py
│   └── ch2_diagram_agent.py
├── contracts/                   # Specification contracts
│   ├── spec.md
│   ├── plan.md
│   ├── tasks.md
│   └── content-schema.md
├── diagrams/                    # Diagram placeholders (documentation)
│   └── README.md               # Diagram placeholder list
└── validation/                  # Validation reports
    ├── validation-report.md
    └── validation-schema.md
```

## Content Packaging Schema

### MDX Content File

**Source**: `frontend/docs/chapters/chapter-2.mdx`
**Destination**: `releases/chapter-2/content/chapter-2.mdx`

**Required Elements**:
- YAML frontmatter (title, description, sidebar_position, sidebar_label, tags)
- Exactly 7 H2 sections
- 4 diagram placeholders (kebab-case)
- 4 AI-block React components (chapterId={2})
- Glossary section with 7 placeholder terms
- All content preserved (no modifications)

**Validation**:
- Frontmatter preserved
- All sections included
- All placeholders included
- All components included

---

## Metadata Packaging Schema

### Chapter Metadata File

**Source**: `backend/app/content/chapters/chapter_2.py`
**Destination**: `releases/chapter-2/metadata/chapter_2.py`

**Required Fields**:
- `id: 2`
- `title: "Chapter 2 — ROS 2 Fundamentals"`
- `section_count: 7`
- `sections: [...]` (7 items)
- `ai_blocks: [...]` (4 items)
- `diagram_placeholders: [...]` (4 items)
- `glossary_terms: [...]` (7 items)
- `learning_outcomes: [...]` (6 items)
- `prerequisites: [1]`

**Validation**:
- All fields present
- File contents preserved
- No modifications made

### Chunk File

**Source**: `backend/app/content/chapters/chapter_2_chunks.py`
**Destination**: `releases/chapter-2/rag/chapter_2_chunks.py`

**Required Elements**:
- Function `get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]`
- Placeholder return structure
- Comprehensive TODO comments

**Validation**:
- Function signature preserved
- File contents preserved
- No modifications made

---

## AI Runtime Packaging Schema

### AI Blocks API

**Source**: `backend/app/api/ai_blocks.py` (Chapter 2 excerpts)
**Destination**: `releases/chapter-2/ai-blocks/ai_blocks.py`

**Required Elements**:
- Chapter 2 request/response models
- Chapter 2 endpoint routes (if applicable)
- Chapter 2 routing logic (TODOs acceptable)

**Validation**:
- Chapter 2-specific code included
- File structure preserved
- No modifications made

### Chapter 2 Subagents

**Source Files**:
- `backend/app/ai/subagents/ch2_ask_question_agent.py`
- `backend/app/ai/subagents/ch2_explain_el10_agent.py`
- `backend/app/ai/subagents/ch2_quiz_agent.py`
- `backend/app/ai/subagents/ch2_diagram_agent.py`

**Destination**: `releases/chapter-2/ai-blocks/`

**Required Elements**:
- Function signatures
- TODO placeholders
- ROS 2-specific comments

**Validation**:
- All 4 subagent files copied
- File contents preserved
- No modifications made

---

## Contracts Packaging Schema

### Specification Files

**Source Files**:
- `specs/014-chapter-2-content/spec.md`
- `specs/014-chapter-2-content/plan.md`
- `specs/014-chapter-2-content/tasks.md`
- `specs/014-chapter-2-content/contracts/content-schema.md`

**Destination**: `releases/chapter-2/contracts/`

**Required Elements**:
- Complete specification documents
- Architecture plans
- Task lists
- Content schemas

**Validation**:
- All contract files copied
- File contents preserved
- No modifications made

---

## Validation Packaging Schema

### Validation Reports

**Source Files**:
- `specs/015-chapter-2-validation/checklists/validation-report.md`
- `specs/015-chapter-2-validation/contracts/validation-schema.md`

**Destination**: `releases/chapter-2/validation/`

**Required Elements**:
- Validation results (7 categories, all PASS)
- Validation schemas
- Test results

**Validation**:
- Both validation files copied
- File contents preserved
- No modifications made

---

## README Packaging Schema

### Package README

**File**: `releases/chapter-2/README.md`

**Required Sections**:
1. **Chapter Purpose**: Overview of Chapter 2 content and goals
2. **File Structure Overview**: Directory layout and file descriptions
3. **How AI-Block Runtime Works**: Explanation of Chapter 2 AI block integration
4. **How RAG Pipeline Consumes Chapter 2**: Explanation of RAG integration
5. **Build Instructions**: Frontend and backend build steps
6. **Testing Instructions**: How to run tests and validations
7. **Integration Instructions**: Standalone vs full book integration

**Content Requirements**:
- Clear, actionable instructions
- Code examples where applicable
- File path references
- Integration guidance

**Validation**:
- All required sections present
- Instructions are clear
- Examples are accurate

---

## Release Consistency Check Schema

### File Existence Validation

**Check List**:
- [ ] `releases/chapter-2/content/chapter-2.mdx` exists
- [ ] `releases/chapter-2/metadata/chapter_2.py` exists
- [ ] `releases/chapter-2/rag/chapter_2_chunks.py` exists
- [ ] `releases/chapter-2/ai-blocks/` contains all 4 subagent files
- [ ] `releases/chapter-2/contracts/` contains all contract files
- [ ] `releases/chapter-2/validation/` contains validation reports
- [ ] `releases/chapter-2/README.md` exists

### Content Validation

**Check List**:
- [ ] MDX file has 7 sections
- [ ] MDX file has 4 diagram placeholders
- [ ] MDX file has 4 AI-block components
- [ ] MDX file has 7 glossary terms
- [ ] Metadata file has all required fields
- [ ] Chunk file has correct function signature
- [ ] All subagent files exist

### Import Resolution Validation

**Check List**:
- [ ] Document import path differences in README.md
- [ ] Note standalone vs integrated usage
- [ ] Provide import path guidance

---

## Packaging Operations Schema

### Copy Operations

**Operation Type**: Copy-only (no modifications)

**Operations**:
1. Copy MDX file: `frontend/docs/chapters/chapter-2.mdx` → `releases/chapter-2/content/chapter-2.mdx`
2. Copy metadata: `backend/app/content/chapters/chapter_2.py` → `releases/chapter-2/metadata/chapter_2.py`
3. Copy chunks: `backend/app/content/chapters/chapter_2_chunks.py` → `releases/chapter-2/rag/chapter_2_chunks.py`
4. Copy AI blocks: `backend/app/api/ai_blocks.py` (excerpts) → `releases/chapter-2/ai-blocks/ai_blocks.py`
5. Copy subagents: `backend/app/ai/subagents/ch2_*.py` → `releases/chapter-2/ai-blocks/`
6. Copy contracts: `specs/014-chapter-2-content/*.md` → `releases/chapter-2/contracts/`
7. Copy validation: `specs/015-chapter-2-validation/**/*.md` → `releases/chapter-2/validation/`

**Validation**:
- All copy operations succeed
- File contents preserved
- No modifications made

---

## Release Package Checklist

- [ ] Release folder structure created
- [ ] Content files copied
- [ ] Metadata files copied
- [ ] RAG chunk files copied
- [ ] AI runtime components copied
- [ ] Contracts copied
- [ ] Validation reports copied
- [ ] README.md generated
- [ ] Release consistency check passes
- [ ] No missing components
- [ ] No code modifications made

---

## Notes

- All operations are copy-only. No code modifications should be made.
- README.md should provide comprehensive documentation for package usage.
- Package should be usable both standalone and integrated into full book.
- Import paths may differ in packaged structure - document in README.md.
- Release consistency check ensures package completeness.
