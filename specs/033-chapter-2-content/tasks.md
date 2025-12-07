# Task List: Chapter 2 Written Content (Mechanical Systems)

**Feature**: 033-chapter-2-content
**Branch**: `033-chapter-2-content`
**Created**: 2025-01-27
**Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md)

## Overview

This task list implements Feature 033 (Chapter 2 Written Content - Mechanical Systems) by creating complete educational content for Chapter 2: "The Foundations of Mechanical Systems" as an MDX file with strategic placeholders for future diagram and AI-interactive features, plus backend metadata for RAG integration.

**Total Tasks**: 20 tasks across 4 phases
**Estimated Time**: 2-4 hours (content writing) + 30 minutes (validation)
**Primary Deliverable**: `frontend/docs/chapters/chapter-2.mdx`
**Secondary Deliverable**: `backend/app/content/chapters/chapter_2.py` (updated)

---

## Phase 1: Frontend Content Creation (2-3 hours)

### Section 1: Forces & Motion

- [ ] T001 [US1] Write Section 1 content: definition of force and motion, everyday examples, Newton's laws at beginner level (min 200 words, 7th-8th grade level)
- [ ] T002 [US1] Add diagram placeholder `<!-- DIAGRAM: force-motion -->` to Section 1

### Section 2: Energy & Work

- [ ] T003 [US1] Write Section 2 content: definitions of energy, work, mechanical efficiency, real-world examples (min 200 words)
- [ ] T004 [US1] Add diagram placeholder `<!-- DIAGRAM: energy-work -->` to Section 2

### Section 3: Simple Machines

- [ ] T005 [US1] Write Section 3 content: types of simple machines (lever, pulley, wheel & axle, inclined plane, screw, wedge), why mechanical advantage matters (min 200 words)
- [ ] T006 [US1] Add diagram placeholder `<!-- DIAGRAM: simple-machines -->` to Section 3

### Section 4: Mechanical Systems in Robotics

- [ ] T007 [US1] Write Section 4 content: how robots use mechanical systems, actuators + force transmission, safety considerations (min 200 words)
- [ ] T008 [US1] Add diagram placeholder `<!-- DIAGRAM: robotics-mechanics -->` to Section 4

### Section 5: Learning Objectives

- [ ] T009 [US1] Write Section 5 content: 5-7 bullet points with action verbs reflecting course document

### Section 6: Summary

- [ ] T010 [US1] Write Section 6 content: 6-8 line recap of chapter content

### Section 7: Glossary

- [ ] T011 [US1] Write Section 7 content: exactly 7 glossary terms (Force, Motion, Work, Energy, Mechanical Advantage, Simple Machine, Efficiency) with beginner-friendly definitions (10-100 words each)

---

## Phase 2: Add Interactive Placeholders (30 minutes)

- [ ] T012 [US2] Add AI-block placeholder `<!-- AI-BLOCK: ask-question -->` at logical position
- [ ] T013 [US2] Add AI-block placeholder `<!-- AI-BLOCK: explain-like-i-am-10 -->` at logical position
- [ ] T014 [US2] Add AI-block placeholder `<!-- AI-BLOCK: interactive-quiz -->` at logical position
- [ ] T015 [US2] Add AI-block placeholder `<!-- AI-BLOCK: generate-diagram -->` at logical position
- [ ] T016 [US2] Verify all 4 diagram placeholders present with correct names
- [ ] T017 [US2] Verify all 4 AI-block placeholders present with correct types

---

## Phase 3: Backend Metadata Update (30 minutes)

- [ ] T018 [US3] Update `chapter_2.py` with new title: "Chapter 2 — The Foundations of Mechanical Systems"
- [ ] T019 [US3] Update sections list to match new structure
- [ ] T020 [US3] Update diagram_placeholders list: ["force-motion", "energy-work", "simple-machines", "robotics-mechanics"]
- [ ] T021 [US3] Update learning_outcomes list (5-7 items)
- [ ] T022 [US3] Update glossary_terms list (7 terms)
- [ ] T023 [US3] Update summary (2-3 sentences)
- [ ] T024 [US3] Test Python import: `python -c "from app.content.chapters.chapter_2 import CHAPTER_METADATA"`

---

## Phase 4: Validation (30 minutes)

- [ ] T025 [US2] Run `npm run build` in frontend/ directory and verify MDX file compiles without errors
- [ ] T026 [US3] Verify all required metadata fields are accessible
- [ ] T027 [US1] Verify all 7 sections present in correct order
- [ ] T028 [US1] Verify all 7 glossary terms defined with proper formatting
- [ ] T029 [US1] Verify content readability appropriate for 12+ age group

---

## Summary

**Total Tasks**: 29 tasks across 4 phases

**Phase Breakdown**:
- Phase 1 (Content Creation): 11 tasks
- Phase 2 (Placeholders): 6 tasks
- Phase 3 (Backend Metadata): 7 tasks
- Phase 4 (Validation): 5 tasks

**Priority Breakdown**:
- P1 (Critical): 29 tasks

**Estimated Time**: 2-4 hours (content writing is time-intensive)

**Dependencies**: Feature 001 (Base Project Initialization), Feature 003 (Chapter 1 Content)

**Out of Scope**: Diagram generation, AI feature implementation, RAG implementation

