# Research Document: Chapter 2 Written Content (Mechanical Systems)

**Feature**: 033-chapter-2-content
**Date**: 2025-01-27
**Purpose**: Resolve technical clarifications and establish best practices for content creation

## Research Questions & Resolutions

### Q1: What is the optimal structure for MDX frontmatter in Docusaurus 3.x?

**Decision**: Use standard Docusaurus frontmatter with custom fields for chapter metadata (same as Chapter 1)

**Structure**: Follows Chapter 1 pattern with title, description, sidebar_position=2, sidebar_label, tags

**References**: Docusaurus 3.x documentation, Chapter 1 example

---

### Q2: How should AI-interactive block placeholders be positioned for Chapter 2 content?

**Decision**: Position AI blocks at strategic points following pedagogical principles (same as Chapter 1)

**Placement Strategy**: Place all 4 AI blocks logically after core explanations in relevant sections

**References**: Cognitive Load Theory, Retrieval Practice research, Dual Coding Theory

---

### Q3: What content writing style best serves 12+ age group for mechanical systems topics?

**Decision**: Conversational-educational style with scaffolded complexity (same as Chapter 1)

**Style Guidelines**:
- Second-person ("you") for direct connection
- 15-20 words per sentence (7th-8th grade level)
- 3-4 sentences per paragraph max
- Analogies from daily life (playground equipment, household items)
- Define terms when first introduced

**References**: Chapter 1 research.md for detailed guidelines

---

## Technical Decisions

### Decision 1: Follow Chapter 1 Content Structure Pattern

**Rationale**: Consistency across chapters improves learner experience and maintainability

**Implementation**: Follow exact same structure as Chapter 1 (7 sections, 4 diagrams, 4 AI blocks)

---

### Decision 2: Course Document as Authoritative Source

**Rationale**: User explicitly states "according to the course document"

**Implementation**: Follow exact outline provided in DOCUMENTATION.md requirements

---

## Content Writing Guidelines

### Section Structure Template

Each section should follow this structure:
1. Topic Sentence (1 sentence)
2. Explanatory Paragraph 1 (3-4 sentences, 15-20 words each)
3. Explanatory Paragraph 2 (3-4 sentences, 15-20 words each)
4. Example or Application Paragraph (2-3 sentences)
5. Placeholders (where appropriate)

### Glossary Entry Template

Each glossary term should follow this format:
```markdown
**Term Name**: Definition that explains the concept in accessible language (10-100 words). Uses analogies or concrete examples to make the concept relatable.
```

---

## Summary

This research document establishes:
- MDX frontmatter structure (consistent with Chapter 1)
- AI-block placement strategy (pedagogically sound)
- Content writing style (conversational-educational, 7th-8th grade)
- Course document as authoritative source

**Key Principles**:
- Consistency with Chapter 1 structure and style
- Pedagogical soundness in AI-block placement
- Accessibility for 12+ age group
- Course document outline is authoritative

