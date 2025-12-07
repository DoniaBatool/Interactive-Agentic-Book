# Implementation Plan: Chapter 3 — MDX + Metadata Implementation

**Branch**: `038-ch3-mdx-implementation` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/038-ch3-mdx-implementation/spec.md` and Feature 037 specification

## Summary

This feature implements the full MDX file structure and Python metadata module for Chapter 3 based on the specification created in Feature 037. The implementation creates an MDX file with 7 sections, 4 diagram placeholders, 4 AI-block placeholders, chunk boundaries, and a backend metadata file with all required fields and TODO placeholders. **No real content writing**—only structure, placeholders, frontmatter, and metadata stubs.

**Primary Deliverable**: `frontend/docs/chapters/chapter-3.mdx` (MDX file structure with placeholders)
**Secondary Deliverable**: `backend/app/content/chapters/chapter_3.py` (Python metadata dictionary with TODOs)
**Validation**: MDX build test + Python import test + Integrity validation

---

## Technical Context

**Language/Version**:
- Frontend: MDX (Markdown + JSX) compatible with Docusaurus 3.x
- Backend: Python 3.11+

**Primary Dependencies**:
- Feature 001 (Base Project Initialization) - Docusaurus frontend and FastAPI backend
- Feature 037 (Chapter 3 Content Specification) - Source for structure and placeholders
- Feature 003 (Chapter 1 Content) - Reference for MDX structure pattern
- Feature 032 (Chapter 2 Content) - Reference for MDX structure pattern
- Frontend: Docusaurus 3.x (already installed)
- Backend: Python 3.11+ standard library (no new dependencies)

**Storage**: Static files (MDX content structure, Python module) - no database

**Testing**:
- Frontend: `npm run build` validation (Docusaurus build process)
- Backend: Python import test (`python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"`)
- Manual: Integrity validation (section count, placeholder counts, title matching)

**Target Platform**:
- Frontend: Web browsers via Docusaurus static site
- Backend: Server-side Python (Uvicorn/FastAPI environment)

**Project Type**: Web application (frontend MDX content structure + backend metadata scaffold)

**Performance Goals**:
- Build time: Incremental build < 5 seconds
- No performance-critical operations (static content only)

**Constraints**:
- MUST NOT write actual content (structure and placeholders only)
- MUST follow Feature 037 specification exactly
- MUST ensure all placeholders match Feature 037 specification
- MUST ensure metadata matches MDX structure exactly
- Backend metadata MUST remain simple Python dictionary (no Pydantic model, no database)

**Scale/Scope**:
- 1 MDX file (chapter-3.mdx)
- 1 Python metadata file (chapter_3.py)
- 7 sections with structure
- 4 diagram placeholders
- 4 AI-block placeholders
- Chunk boundaries for RAG processing

---

## 1. Folder + File Creation Plan

### 1.1 MDX File

**Location**: `frontend/docs/chapters/chapter-3.mdx`
**Status**: Update existing file (structure already exists, needs alignment with Feature 037)
**Action**: Update frontmatter, sections, placeholders, and chunk boundaries to match Feature 037 exactly

### 1.2 Python Metadata File

**Location**: `backend/app/content/chapters/chapter_3.py`
**Status**: Update existing file (metadata already exists, needs alignment with Feature 037)
**Action**: Update metadata dictionary with all required fields, add TODO placeholders, add get_chapter_3_chunks() function

### 1.3 Chapter Registry

**Status**: No chapter registry file required (chapters are auto-discovered by Docusaurus)
**Action**: None

---

## 2. MDX Structure Plan

### 2.1 Frontmatter Structure

**Required Fields**:
```yaml
---
title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
description: "Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"
sidebar_position: 3
sidebar_label: "Chapter 3: Physical AI Perception Systems"
tags: ["physical-ai", "sensors", "perception", "signal-processing"]
---
```

**Validation**: Title must match Feature 037 specification exactly

### 2.2 Section Structure Mapping

**All 7 Sections** (from Feature 037):
1. **What Is Perception in Physical AI?**
   - Diagram: `<!-- DIAGRAM: perception-overview -->` (middle)
   - AI Block: `<!-- AI-BLOCK: ask-question -->` (end)
   - Chunk boundaries: Wrapped

2. **Types of Sensors in Robotics**
   - Diagram: `<!-- DIAGRAM: sensor-types -->` (middle)
   - AI Block: `<!-- AI-BLOCK: generate-diagram -->` (middle)
   - Chunk boundaries: Wrapped

3. **Computer Vision & Depth Perception**
   - Diagram: `<!-- DIAGRAM: cv-depth-flow -->` (end)
   - AI Block: `<!-- AI-BLOCK: explain-like-i-am-10 -->` (middle)
   - Chunk boundaries: Wrapped

4. **Signal Processing Basics for AI**
   - Diagram: `<!-- DIAGRAM: feature-extraction-pipeline -->` (middle)
   - AI Block: `<!-- AI-BLOCK: interactive-quiz -->` (end)
   - Chunk boundaries: Wrapped

5. **Feature Extraction & Interpretation**
   - No diagram
   - No AI block
   - Chunk boundaries: Wrapped

6. **Learning Objectives**
   - No diagram
   - No AI block
   - Chunk boundaries: Wrapped

7. **Glossary**
   - No diagram
   - No AI block
   - Chunk boundaries: Wrapped

### 2.3 AI-Block Placement Plan

**Placement Rules** (from Feature 037):
- Section 1: `ask-question` at the end
- Section 2: `generate-diagram` in the middle
- Section 3: `explain-like-i-am-10` in the middle
- Section 4: `interactive-quiz` at the end

**Format**: HTML comments `<!-- AI-BLOCK: block-type -->`

### 2.4 Diagram Placeholder Plan

**Placement Rules** (from Feature 037):
- Section 1: `perception-overview` in the middle
- Section 2: `sensor-types` in the middle
- Section 3: `cv-depth-flow` at the end
- Section 4: `feature-extraction-pipeline` in the middle

**Format**: HTML comments `<!-- DIAGRAM: placeholder-name -->`

### 2.5 Chunking Boundary Positions

**Strategy**: One chunk boundary pair per section
- `<!-- CHUNK: start -->` at section start
- `<!-- CHUNK: end -->` at section end
- Wraps entire section content including placeholders

---

## 3. Metadata Plan

### 3.1 MDX → Metadata Field Mapping

**Core Identification**:
- `id`: 3 (from Feature 037)
- `title`: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)" (must match MDX frontmatter exactly)
- `summary`: "TODO: 2-3 sentence overview" (placeholder for future content)

**Structure Information**:
- `section_count`: 7 (must match number of H2 sections in MDX)
- `sections`: List of 7 section titles (must match MDX H2 headings in order)

**Placeholder Tracking**:
- `ai_blocks`: ["ask-question", "generate-diagram", "explain-like-i-am-10", "interactive-quiz"] (from Feature 037)
- `diagram_placeholders`: ["perception-overview", "sensor-types", "cv-depth-flow", "feature-extraction-pipeline"] (from Feature 037)

**Versioning**:
- `last_updated`: ISO 8601 timestamp (current date)

**RAG-Specific Metadata**:
- `difficulty_level`: "intermediate" (from Feature 037)
- `prerequisites`: [1, 2] (from Feature 037)
- `learning_outcomes`: ["TODO: 3-8 learning outcomes"] (placeholder for future content)
- `glossary_terms`: ["TODO: 6-10 glossary terms"] (placeholder for future content)

### 3.2 Validation Rules

**Section Count Validation**:
- `section_count` (7) MUST equal number of H2 sections in MDX
- Manual validation required

**Placeholder Count Validation**:
- Number of `<!-- DIAGRAM: -->` in MDX MUST equal length of `diagram_placeholders[]` (4)
- Number of `<!-- AI-BLOCK: -->` in MDX MUST equal length of `ai_blocks[]` (4)
- Manual validation required

**Title Matching Validation**:
- Metadata `title` MUST match MDX frontmatter `title` exactly (character-for-character)
- Manual validation required

**Section Order Validation**:
- Metadata `sections[]` MUST match MDX H2 headings in order
- Manual validation required

### 3.3 RAG Preparation Function

**Function**: `get_chapter_3_chunks()`
**Purpose**: Future RAG integration for chunking Chapter 3 content
**Implementation**: TODO placeholder with function signature
**Return Type**: `List[Dict[str, Any]]`
**Body**: `return []` (placeholder)

---

## 4. Build Impact

### 4.1 Expected Docusaurus Build Behavior

**Build Command**: `npm run build` in `frontend/` directory
**Expected Result**: Build succeeds with no errors or warnings
**Validation**: MDX file compiles correctly, frontmatter is valid YAML, all sections render

### 4.2 Expected Backend Import Behavior

**Import Command**: `python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA"`
**Expected Result**: Import succeeds, `CHAPTER_METADATA` dictionary is accessible
**Validation**: All fields accessible, no syntax errors, type hints valid

---

## 5. Constraints

### 5.1 No Content Writing

- **Constraint**: MUST NOT write actual content (structure and placeholders only)
- **Rationale**: Content writing is separate feature
- **Implementation**: Use content placeholder comments only

### 5.2 Only Scaffolding + Placeholders

- **Constraint**: MUST only create structure, placeholders, and metadata stubs
- **Rationale**: This is scaffolding feature, not content feature
- **Implementation**: No real content, only HTML comments and TODO placeholders

### 5.3 Feature 037 Compliance

- **Constraint**: MUST follow Feature 037 specification exactly
- **Rationale**: Feature 037 is authoritative source for structure
- **Implementation**: All sections, placeholders, and metadata must match Feature 037

---

## 6. Success Criteria

- ✅ MDX file created with correct frontmatter, headings, placeholders
- ✅ Metadata file created with correct schema + TODOs
- ✅ All placeholders inserted exactly as defined in Feature 037
- ✅ Project builds cleanly (`npm run build` succeeds)
- ✅ Python file imports cleanly
- ✅ No business logic added (scaffolding only)

---

## 7. Dependencies + Risks

### Dependencies:
- Feature 001: Base Project Initialization
- Feature 037: Chapter 3 Content Specification (authoritative source)
- Feature 003: Chapter 1 Content (reference pattern)
- Feature 032: Chapter 2 Content (reference pattern)

### Risks:
1. **Risk**: Existing Chapter 3 MDX file may have different structure
   - **Mitigation**: Update existing file to match Feature 037 exactly
2. **Risk**: Placeholder names may not match Feature 037
   - **Mitigation**: Use Feature 037 as authoritative source, validate manually
3. **Risk**: Metadata may not match MDX structure
   - **Mitigation**: Validate section count, title matching, placeholder counts

---

## Summary

This plan establishes the complete architecture for Chapter 3 MDX and metadata implementation. The implementation follows Feature 037 specification exactly, creates MDX structure with all sections and placeholders, and creates metadata file with all required fields and TODO placeholders. All components are scaffolding only—no actual content is written.

**Estimated Implementation Time**: 1-2 hours (structure implementation only, no content writing)
**Complexity**: Low (following existing patterns, Feature 037 as source)
**Dependencies**: Feature 001, Feature 037, Feature 003, Feature 032
**Out of Scope**: Actual content writing, diagram generation, AI block implementation

