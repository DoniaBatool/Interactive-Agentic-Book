# Data Model: Chapter 2 Written Content (Mechanical Systems)

**Feature**: 033-chapter-2-content
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for chapter content system

## Entity Definitions

### 1. Chapter Content (Primary Entity)

**Description**: Represents the complete written educational material for a single chapter

**Storage**: MDX file at `frontend/docs/chapters/chapter-2.mdx`

**Structure**: 7 H2 sections following exact outline from course document:
1. Forces & Motion
2. Energy & Work
3. Simple Machines
4. Mechanical Systems in Robotics
5. Learning Objectives
6. Summary
7. Glossary

**Validation Rules**:
- Title MUST start with "Chapter 2 — " format
- MUST contain exactly 7 H2 sections in specified order
- MUST contain exactly 4 `<!-- DIAGRAM: -->` placeholders
- MUST contain exactly 4 `<!-- AI-BLOCK: -->` placeholders
- Reading level MUST be 7th-8th grade (Flesch-Kincaid)

---

### 2. Section (Sub-entity of Chapter Content)

**Description**: A major division within a chapter focusing on a specific topic

**Required Sections**:
- Forces & Motion (with diagram placeholder)
- Energy & Work (with diagram placeholder)
- Simple Machines (with diagram placeholder)
- Mechanical Systems in Robotics (with diagram placeholder)
- Learning Objectives (5-7 bullet points)
- Summary (6-8 line recap)
- Glossary (7 terms)

---

### 3. Glossary Term (Sub-entity of Chapter Content)

**Description**: A key vocabulary word with beginner-friendly definition

**Required Terms**:
1. Force
2. Motion
3. Work
4. Energy
5. Mechanical Advantage
6. Simple Machine
7. Efficiency

**Format**: `**Term**: Definition text (10-100 words)`

---

### 4. Diagram Placeholder (Sub-entity of Chapter Content)

**Description**: A marker indicating where a visual diagram should be rendered

**Required Placeholders**:
1. `force-motion` (Section 1)
2. `energy-work` (Section 2)
3. `simple-machines` (Section 3)
4. `robotics-mechanics` (Section 4)

---

### 5. AI-Interactive Block Placeholder (Sub-entity of Chapter Content)

**Description**: A marker indicating where interactive AI features will be integrated

**Required Types**: ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram

**Placement**: Logically after core explanations in relevant sections

---

### 6. Chapter Metadata (Backend Entity)

**Description**: Structured information about a chapter used by backend systems

**Storage**: Python file at `backend/app/content/chapters/chapter_2.py`

**Required Fields**: id, title, summary, section_count, sections, ai_blocks, diagram_placeholders, last_updated, difficulty_level, prerequisites, learning_outcomes, glossary_terms

---

## Relationships

- Chapter Content → Sections (1:N, exactly 7 sections)
- Chapter Content → Glossary Terms (1:N, exactly 7 terms)
- Chapter Content → Diagram Placeholders (1:N, exactly 4 placeholders)
- Chapter Content → AI-Block Placeholders (1:N, exactly 4 placeholders)

---

## Summary

All structures follow Chapter 1 pattern for consistency. Course document outline is authoritative source for section structure.

