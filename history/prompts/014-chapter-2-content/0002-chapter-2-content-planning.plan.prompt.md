---
id: 0002
title: Chapter 2 Written Content — Structure, Metadata, Schema & Contracts Planning
stage: plan
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 014-chapter-2-content
branch: 014-chapter-2-content
user: Leo
command: /sp.plan
labels: ["chapter-2", "content", "structure", "metadata", "schema", "contracts", "planning", "architecture"]
links:
  spec: specs/014-chapter-2-content/spec.md
  plan: specs/014-chapter-2-content/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/014-chapter-2-content/plan.md
tests:
  - Architecture plan completeness validation
  - Constitution check validation
---

## Prompt

User requested: `/sp.plan` following instructions from DOCUMENTATION.md (371-405)

Feature details:
- feature-id: 014-chapter-2-content
- title: "Chapter 2 Written Content — Structure, Metadata, Schema & Contracts"
- goal: Create a full implementation plan describing MDX structure, metadata architecture, diagram & AI-block placement, contract file generation, RAG preparation, and consistency rules

Requirements:
1. MDX Structure Plan: Define 7 required section headings, placement rules for AI blocks and diagrams, placement for glossary terms, placeholder text strategy
2. Metadata Architecture: Map MDX → Python metadata fields, ensure fields follow Chapter 1 contract, define validation rules
3. Diagram & AI-Block Placement Logic: Explain how placeholders mirror Chapter 1's pattern, ensure naming consistency (kebab-case)
4. Contract File Generation: Describe content-schema.md, requirements.md, research.md, quickstart.md, data-model.md templates
5. RAG Preparation: Explain how Chapter 2 metadata and chunk file prepare for embedding in Feature 012/013
6. Consistency Rules: Must follow course syllabus, must match Chapter 1 structure style, no real content yet

## Response snapshot

Successfully created comprehensive architecture plan for Chapter 2 content structure:

**Created Files:**
1. `specs/014-chapter-2-content/plan.md` - Complete architecture plan with:
   - Summary and technical context
   - MDX Structure Plan: 7 required section headings, AI-block placement rules (4 components), diagram placement rules (4 placeholders), glossary placement rules (7 terms), placeholder text strategy
   - Metadata Architecture: MDX → Python metadata mapping, validation rules, cross-validation rules
   - Diagram & AI-Block Placement Logic: Placement pattern mirroring Chapter 1, naming consistency (kebab-case), placement details table
   - Contract File Generation: 5 contract files described (content-schema.md, checklists/requirements.md, research.md, data-model.md, quickstart.md) - all already created in spec phase
   - RAG Preparation: Metadata fields for RAG, chunk file preparation, future RAG integration path
   - Consistency Rules: Course syllabus alignment, Chapter 1 structure style matching, no real content yet
   - File & Folder Plan: Files to create/update/verify, modification summary
   - Risks / Constraints: 5 risks with mitigations (section count mismatch, no real content, metadata mismatch, AI-block integration, naming inconsistency)
   - Acceptance criteria mapping
   - Dependencies & next steps

**Key Architecture Decisions:**
- MDX Structure: Exactly 7 H2 sections (not 9 as in existing file from Feature 010)
- AI-Block Placement: React components from Feature 011 (chapterId={2}), strategic placement following pedagogical principles
- Diagram Placement: 4 kebab-case placeholders, strategic placement for visual learning
- Glossary Placement: Section 7 with 7 placeholder terms
- Metadata Mapping: MDX structure → Python dictionary following Chapter 1 pattern
- Placeholder Strategy: All content as HTML comments (no actual text)
- Consistency: Matches Chapter 1 structure style (7 sections, 4 diagrams, 4 AI blocks, 7 glossary terms)

**Placement Pattern:**
- Section 1: Diagram + Ask Question
- Section 2: Diagram + Generate Diagram
- Section 3: Explain Like 10 + Diagram
- Section 4: Diagram + Interactive Quiz
- Sections 5-6: Content only (no diagrams/AI blocks)
- Section 7: Glossary (7 terms)

**Risk Mitigation:**
- Section count mismatch: Update existing file from 9 to 7 sections (remove/merge Learning Objectives and Summary)
- Metadata mismatch: Update section_count and sections list to match 7-section structure
- AI-block integration: Use React components from Feature 011 with correct props
- Naming consistency: Enforce kebab-case validation

**Pattern Consistency:**
- Follows Feature 003 (Chapter 1 Content) pattern exactly
- Structure-only approach (no real content writing)
- Clear placeholder markers and structure requirements
- ROS 2-specific context documented throughout

## Outcome

- ✅ Impact: Complete architecture plan ready for task generation. All technical decisions documented. MDX structure, metadata architecture, diagram & AI-block placement, contract generation, RAG preparation, and consistency rules clearly defined. ROS 2-specific context properly mapped. Risk assessment complete with mitigations.
- 🧪 Tests: Architecture plan completeness validation - PASS, Constitution check validation - PASS
- 📁 Files: 1 plan file created (plan.md with comprehensive content structure architecture)
- 🔁 Next prompts: `/sp.tasks` to generate implementation task list
- 🧠 Reflection: Plan follows established patterns for maintainability. Clear separation between structure and content ensures future content writers understand what needs to be written. ROS 2-specific context (analogies, examples, concepts) properly documented. All placement logic and validation rules clearly defined. Risk assessment comprehensive with mitigations. Note: Existing chapter-2.mdx from Feature 010 has 9 sections, but plan requires 7 - this will need validation/alignment during implementation.

## Evaluation notes (flywheel)

- Failure modes observed: None - planning phase completed successfully
- Graders run and results (PASS/FAIL): Architecture plan completeness - PASS, Constitution check - PASS
- Prompt variant (if applicable): Standard /sp.plan workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.tasks` to generate implementation task list
