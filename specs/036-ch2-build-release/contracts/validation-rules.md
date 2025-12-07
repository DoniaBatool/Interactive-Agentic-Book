# Validation Rules Contract: Chapter 2 Build Validation + Release Packaging

**Feature**: 036-ch2-build-release
**Created**: 2025-01-27
**Status**: Draft

## Overview

This contract defines high-level validation rules for Chapter 2 build validation and release packaging. All validation rules are placeholders with TODO comments—no real validation logic is implemented.

## Frontend Validation Rules

### MDX Structure Validation

**Location**: `scripts/ch2/validate_mdx_structure.py`

**Rules** (High-Level, TODO):
- Validate H2 sections count (expected: 7 sections)
- Check diagram placeholders exist (expected: 4 placeholders)
- Check AI-block placeholders exist (expected: 4 placeholders)
- Check glossary terms exist (expected: 7 terms)
- Validate frontmatter structure

**Placeholder Logic**:
- Function returns placeholder validation results
- No real parsing or validation logic

---

### Frontmatter Validation

**Location**: `scripts/ch2/validate_frontmatter.py`

**Rules** (High-Level, TODO):
- Verify frontmatter fields match schema
- Check required fields: title, description, sidebar_position, sidebar_label, tags
- Validate field types and formats

**Placeholder Logic**:
- Function returns placeholder validation results
- No real parsing or validation logic

---

## Backend Validation Rules

### Metadata Validation

**Location**: `backend/app/validation/ch2_metadata_validator.py`

**Rules** (High-Level, TODO):
- Cross-check metadata vs mdx structure
- Check sections names match between MDX and chapter_2.py
- Check diagram + AI block count matches
- Validate metadata imports without errors

**Placeholder Logic**:
- Function returns placeholder validation results
- No real comparison or validation logic

---

## Build Stability Rules

**Location**: `scripts/ch2/run_all.py`

**Rules** (High-Level, TODO):
- Run all frontend validations
- Run all backend validations
- Check frontend build passes
- Check backend starts without errors
- Generate validation report

**Placeholder Logic**:
- Script contains placeholder imports and TODO steps
- No real validation execution

---

## Release Packaging Rules

**Location**: `scripts/ch2/package_release.py`

**Rules** (High-Level, TODO):
- Gather metadata from chapter_2.py
- Gather MDX content from chapter-2.mdx
- Gather diagrams (future)
- Write chapter-2-export.json with structured data
- Create release folder structure

**Placeholder Logic**:
- Function contains TODO comments for gathering and writing
- No real packaging logic

---

## Release Folder Structure

**Location**: `release/chapter-2/`

**Structure**:
- `README.md` - Release package overview (placeholder)
- `CHANGELOG.md` - Version history (placeholder)
- `chapter-2-export.json` - Structured export data (placeholder JSON)
- `assets/` - Empty folder for future assets

---

## Summary

This contract defines high-level validation rules for Chapter 2. All rules are placeholders with TODO comments. No real validation or packaging logic is implemented—only scaffolding for future implementation.

