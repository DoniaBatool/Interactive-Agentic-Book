# Release Schema: Chapter 3 Release Packaging

**Feature**: 043-ch3-release-package
**Created**: 2025-01-27
**Status**: Draft

## Overview

This contract defines the release packaging schema for Chapter 3. All release components follow a consistent structure with path references (not file copies). The package includes manifest.json, runtime documentation, build reports, and submission notes.

## Release Folder Structure

### Directory Layout

```
releases/chapter-3/
├── manifest.json              # Release manifest with metadata
├── RUNTIME_OVERVIEW.md         # Runtime structure documentation
├── BUILD_REPORT.md             # Build validation report
├── SUBMISSION_NOTES.md         # Hackathon submission notes
└── CH3_VALIDATION.md           # Validation report (from Feature 042)
```

## Manifest Schema

### manifest.json Structure

```json
{
  "chapter_id": 3,
  "version": "1.0.0",
  "mdx_file": "frontend/docs/chapters/chapter-3.mdx",
  "metadata_file": "backend/app/content/chapters/chapter_3.py",
  "ai_blocks": [
    "ask-question",
    "explain-like-10",
    "interactive-quiz",
    "generate-diagram"
  ],
  "diagrams": [
    "perception-overview",
    "sensor-types",
    "cv-depth-flow",
    "feature-extraction-pipeline"
  ],
  "rag_enabled": false,
  "generated_at": "2025-01-27T00:00:00Z"
}
```

**Fields**:
- `chapter_id`: Chapter identifier (3)
- `version`: Release version (1.0.0)
- `mdx_file`: Path to MDX file (reference, not copy)
- `metadata_file`: Path to metadata file (reference, not copy)
- `ai_blocks`: List of AI block types (4 items)
- `diagrams`: List of diagram placeholders (4 items)
- `rag_enabled`: RAG pipeline enabled status (placeholder: false)
- `generated_at`: ISO 8601 timestamp

---

## Runtime Overview Schema

### RUNTIME_OVERVIEW.md Structure

**Sections**:
1. Runtime Structure Tree
2. Module Responsibilities
3. AI Runtime Components
4. RAG Pipeline Overview
5. Subagents/Skills Overview

**Content** (Placeholder):
- Backend runtime structure tree
- Module responsibilities documentation
- AI runtime components overview
- RAG pipeline overview
- Subagents/skills overview

---

## Build Report Schema

### BUILD_REPORT.md Structure

**Sections**:
1. Build Time (placeholder)
2. Warnings (placeholder)
3. Bundle Size Summary (placeholder)
4. MDX Validation Summary (placeholder)

**Content** (Placeholder):
- Build time: TODO
- Warnings: TODO
- Bundle size: TODO
- MDX validation: TODO

---

## Submission Notes Schema

### SUBMISSION_NOTES.md Structure

**Sections**:
1. Overview
2. Feature Summary
3. Implementation Status
4. What's Included / Not Included

**Content** (Placeholder):
- Overview of Chapter 3
- Feature summary
- Implementation status (scaffolding complete)
- What's included / not included

---

## Validation Artifacts

### CH3_VALIDATION.md

**Source**: Feature 042 (Chapter 3 Validation)
**Location**: `CH3_VALIDATION.md` (root) or `releases/chapter-3/CH3_VALIDATION.md`

**Content**: Complete validation report with test matrix

---

## Summary

This contract defines the complete release packaging schema for Chapter 3. All components use path references (not file copies) and placeholder content. The contract follows Chapter 2 release packaging patterns exactly.

