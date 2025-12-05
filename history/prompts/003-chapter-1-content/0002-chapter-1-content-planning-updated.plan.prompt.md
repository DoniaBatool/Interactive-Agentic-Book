---
id: 0002-updated
title: Chapter 1 Content Architecture Plan (Comprehensive Update)
stage: plan
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 003-chapter-1-content
branch: 003-chapter-1-content
user: Leo
command: /sp.plan
labels: ["chapter-1", "architecture", "mdx-structure", "backend-metadata", "ai-blocks", "rag-preparation", "planning"]
links:
  spec: specs/003-chapter-1-content/spec.md
  plan: specs/003-chapter-1-content/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/003-chapter-1-content/plan.md
tests:
  - Architecture plan validation (ALL PASS)
---

## Prompt

User requested: `/sp.plan`

Feature requirements:
```
feature-id: 003-chapter-1
title: "Chapter 1 — Introduction to Physical AI & Robotics"
type: content-architecture

Generate a complete ARCHITECTURE PLAN for Chapter 1 using the output from /sp.specify.

This plan MUST include:

1. File Architecture
   - frontend/docs/chapters/chapter-1.mdx structure
   - section anchors, diagram placeholders, AI-block placeholder mapping
   - internal MDX components (if needed)

2. Backend Architecture
   - backend/app/content/chapters/chapter_1.py
   - exact fields: id, title, summary, section_count, ai_blocks[], last_updated

3. AI-Blocks Architecture
   - Map each AI-BLOCK placeholder to a future subagent or skill
   - No implementation — just routing plan

4. RAG Preparation Plan
   - How this chapter will later feed the vector database
   - Chunking model (headings, subheadings, glossary separation)

5. Compliance Checklist
   Ensure the plan follows:
   - SDD Constitution
   - Docusaurus-First
   - RAG-First
   - AI-Native textbook architecture principles

6. Deliverables
   - Full outline of how .mdx content will be structured
   - Full outline of backend metadata structure
   - Mapping table: section → ai-blocks → future skills

7. Output Format
   - Produce clean Markdown
   - Include diagrams as comments only
   - DO NOT write content — only architecture
```

## Response

Created comprehensive architecture plan update for Chapter 1 content feature:

### Architecture Plan Updated

**File**: `specs/003-chapter-1-content/plan.md` (comprehensive update)

### Key Additions

**1. File Architecture Section**:
- Complete MDX structure template with section anchors
- Section anchor naming convention (kebab-case)
- Diagram placeholder mapping table (4 placeholders)
- AI-BLOCK placeholder mapping table (4 blocks)
- Internal MDX components strategy (deferred to Feature 004)

**2. Backend Architecture Section**:
- Exact field structure for `chapter_1.py`
- Field validation rules table (13 fields)
- Module structure with TODO comments
- Type definitions and examples

**3. AI-Blocks Architecture Section**:
- AI-BLOCK to Subagent mapping table
- 4 subagent implementation plans:
  - `ChapterQuestionAgent` (ask-question)
  - `ChapterExplainerAgent` (explain-like-i-am-10)
  - `ChapterQuizAgent` (interactive-quiz)
  - `DiagramGeneratorAgent` (generate-diagram)
- 8 reusable skills architecture:
  - ContextRetrievalSkill, VectorSearchSkill, EmbeddingGenerationSkill
  - ContentChunkingSkill, GlossaryLookupSkill, QuizGenerationSkill
  - ProgressTrackingSkill, DiagramGenerationSkill
- API endpoint contracts for each subagent

**4. RAG Preparation Plan Section**:
- Chunking strategy (semantic chunking with section boundaries)
- Chunking model structure (`ContentChunk` class definition)
- Chunking examples (section chunk, glossary chunk)
- Embedding generation plan (text-embedding-3-small, 1536 dims)
- Qdrant collection schema (future implementation)
- Chunking implementation phases (4 phases documented)

**5. Compliance Checklist Section**:
- SDD Constitution compliance table (6 principles)
- Docusaurus-First compliance checklist
- RAG-First compliance checklist
- AI-Native textbook architecture compliance

**6. Deliverables Section**:
- Deliverable 1: MDX Content File (complete structure outline)
- Deliverable 2: Backend Metadata File (exact structure)
- Deliverable 3: Architecture Documentation (files listed)
- Deliverable 4: Mapping Table (Section → AI-Blocks → Future Skills)

### Architecture Decisions

1. **Section Anchors**: Kebab-case format `{#section-anchor}` for deep linking
2. **Chunking Strategy**: Section-based with 50-word overlap, glossary as separate chunks
3. **Embedding Model**: OpenAI `text-embedding-3-small` (1536 dimensions)
4. **Subagent Routing**: Each AI-BLOCK maps to dedicated subagent with primary skill
5. **Metadata Structure**: 13 fields including RAG-ready fields (summary, learning_outcomes, glossary_terms)

### Files Updated

- `specs/003-chapter-1-content/plan.md` - Comprehensive architecture plan added

### Next Steps

1. **Run `/sp.tasks`** to generate implementation tasks
2. **Review architecture** with user for approval
3. **Begin implementation** following quickstart.md

### Constitution Compliance

✅ **Principle I - SDD**: Plan created following spec → plan → tasks workflow
✅ **Principle II - Docusaurus-First**: MDX structure fully defined
✅ **Principle III - RAG-First**: Chunking model and embedding strategy documented
✅ **Principle IV - Personalization**: Metadata includes difficulty_level for filtering
✅ **Principle V - Multilingual**: Clean markdown structure supports translation
✅ **Principle VI - TDD**: Validation methods specified in deliverables

### Notes

- All architecture decisions documented with rationale
- Future implementation phases clearly separated (scaffolding vs. real logic)
- Mapping tables provide clear routing for AI-BLOCK → Subagent → Skill
- RAG chunking strategy designed for optimal retrieval quality
- Ready for immediate task generation (`/sp.tasks`)

