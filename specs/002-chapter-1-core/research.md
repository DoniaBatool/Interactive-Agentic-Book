# Research: Chapter 1 Core Implementation

**Feature**: 002-chapter-1-core
**Date**: 2025-12-05
**Purpose**: Document technical decisions for Chapter 1 infrastructure scaffolding

## Overview

This document captures technical decisions made during the planning phase of Feature 002 (Chapter 1 Core Implementation). The feature focuses on creating the foundational infrastructure for Chapter 1 without implementing actual educational content.

---

## Technical Questions & Decisions

### Question 1: How should chapter IDs be formatted in API routes and folder structures?

**Context**: Need consistent identification scheme for chapters across frontend, backend, and file system.

**Options Considered**:
1. Integer IDs (1, 2, 3) for API, zero-padded strings (01, 02, 03) for folders
2. String slugs (chapter-1-intro, chapter-2-sensors) everywhere
3. UUID-based identifiers for future distributed systems

**Decision**: **Option 1 - Integer IDs with zero-padded folder names**

**Rationale**:
- **Simplicity**: Integer IDs are simple, sequential, and easy to validate in APIs
- **Scalability**: Zero-padded folder names (01, 02, 03, ..., 99) support up to 99 chapters with consistent alphabetical sorting
- **Performance**: Integer-based lookups are faster than string comparisons
- **Convention**: Textbooks naturally use chapter numbers, aligning with user mental model
- **Future-proof**: Can extend to 001, 002 if >99 chapters needed

**Implementation**:
- API endpoints: `/chapters/{chapter_id}` where `chapter_id` is integer (1, 2, 3)
- Folder structure: `/chapters/01-introduction/`, `/chapters/02-sensors/`
- Pydantic model: `chapter: int` field

---

### Question 2: Where should chapter content be stored (raw vs. processed)?

**Context**: Future RAG integration will need to process chapter content into embeddings. Need separation between source content and RAG-optimized data.

**Options Considered**:
1. Single `/chapters/{id}/` directory for all content
2. Separate `/content/{id}/raw/` and `/content/{id}/processed/` directories
3. Database storage with file system cache

**Decision**: **Option 2 - Separate raw and processed directories**

**Rationale**:
- **Clear Separation**: Distinguishes source-of-truth content from derived artifacts
- **RAG Pipeline**: Supports future content ingestion pipeline: raw → chunking → embedding → processed
- **Version Control**: Raw content can be versioned independently from generated embeddings
- **Debugging**: Easy to compare raw vs. processed content during RAG development
- **Constitutional Compliance**: Aligns with Principle III (RAG-First) by planning storage structure upfront

**Implementation**:
- Raw content: `/content/01-introduction/raw/` (source markdown, images, videos)
- Processed content: `/content/01-introduction/processed/` (embeddings, chunked text, metadata JSON)
- `.gitkeep` files to preserve empty directories

---

### Question 3: What should the ChapterMetadata Pydantic model structure include?

**Context**: Need API response schema that serves current needs while anticipating future features.

**Options Considered**:
1. Minimal: `{chapter, title, summary}` only
2. Moderate: `{chapter, title, summary, sections}` (current need)
3. Comprehensive: Include learning objectives, prerequisites, difficulty, tags, etc.

**Decision**: **Option 2 - Moderate with sections array**

**Rationale**:
- **MVP Focus**: Includes only fields needed for current user stories
- **Extensibility**: Pydantic models can be extended later without breaking changes
- **Performance**: Smaller response payloads for initial scaffolding phase
- **No Over-Engineering**: Avoids speculative fields not yet required by any feature
- **Alignment**: Matches spec requirements (FR-008) exactly

**Implementation**:
```python
class ChapterMetadata(BaseModel):
    chapter: int          # Chapter number (1, 2, 3...)
    title: str            # Full chapter title
    summary: str          # Brief description
    sections: List[str]   # Section titles (empty for scaffolding)
```

**Future Extensions** (when needed):
- `difficulty_level: str` - For personalized recommendations
- `prerequisites: List[int]` - Chapter dependencies
- `learning_outcomes: List[str]` - For quiz generation
- `estimated_time_minutes: int` - For progress tracking

---

### Question 4: How much detail should RAG placeholder files contain?

**Context**: Need to guide future development without implementing actual RAG functionality.

**Options Considered**:
1. Empty files with minimal TODO comments (<50 words)
2. Detailed documentation with API examples and integration points (100-300 words)
3. Partial implementation with stubbed functions

**Decision**: **Option 2 - Detailed documentation with examples**

**Rationale**:
- **Knowledge Transfer**: Captures architectural intent for future developers
- **Reduced Rework**: Clear integration points prevent misaligned implementations
- **Constitutional Compliance**: Satisfies NFR-001 (TODO comments >20 words)
- **Educational Value**: Serves as internal documentation for RAG concepts
- **No Premature Code**: Avoids partial implementations that may need refactoring

**Implementation**:
- Agent placeholders: 4 agent types documented with API examples (200+ lines)
- Skill placeholders: 7 skill types with integration guidelines (250+ lines)
- Service layer: 6 RAG integration points with TODO sections
- Each TODO includes: purpose, capabilities, integration points, example code

---

### Question 5: Should the frontend use autogenerated or manual sidebar configuration?

**Context**: Docusaurus supports both autogenerated sidebars (from folder structure) and manual configuration.

**Options Considered**:
1. Fully autogenerated: `{type: 'autogenerated', dirName: '.'}`
2. Fully manual: Explicit list of all pages
3. Hybrid: Manual for Chapter 1, autogenerated for others

**Decision**: **Option 3 - Hybrid approach**

**Rationale**:
- **Visibility**: Explicit Chapter 1 entry ensures it's always visible in sidebar
- **Flexibility**: Autogenerated sections for `/chapters/` directory handle Feature 003 content
- **Control**: Can customize Chapter 1 label and positioning independently
- **Scalability**: Future chapters added to `/chapters/` appear automatically
- **User Experience**: Collapsible categories improve navigation

**Implementation**:
```typescript
tutorialSidebar: [
  {
    type: 'category',
    label: 'Chapter 1',
    items: ['chapter-1/overview'],
  },
  {
    type: 'category',
    label: 'Chapters',
    items: [{type: 'autogenerated', dirName: 'chapters'}],
  },
]
```

---

## Summary of Key Decisions

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Integer chapter IDs | Simplicity, performance | API routes, Pydantic models |
| Separate raw/processed dirs | RAG pipeline readiness | Folder structure, future content ingestion |
| Moderate metadata schema | MVP focus, extensibility | API response structure |
| Detailed placeholder TODOs | Knowledge transfer, reduced rework | Agent/skill files (400+ lines docs) |
| Hybrid sidebar config | Visibility + flexibility | Docusaurus navigation |

---

## Open Questions (Deferred)

The following questions were identified but deferred to future features:

1. **Authentication**: When should chapter access be restricted?
   - Deferred to Feature: User authentication and authorization
   - Note: Current implementation assumes public access

2. **Chapter Versioning**: How to handle content updates?
   - Deferred to Feature: Content versioning system
   - Note: Current implementation uses file system timestamps

3. **Multi-language Support**: How to structure translations?
   - Deferred to Feature: Internationalization (i18n)
   - Note: Current implementation English-only

4. **Content Caching**: When to cache chapter metadata?
   - Deferred to Feature: Performance optimization
   - Note: Current implementation serves fresh data on every request

---

**Next Steps**: Proceed to `data-model.md` to define entity structures and relationships.
