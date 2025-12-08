# Global Platform Stabilization

**Feature**: 056-global-stabilization
**Date**: 2025-01-27
**Status**: Scaffolding Phase

## Overview

This document describes the global stabilization layer for the AI Textbook Platform. The stabilization layer ensures consistent behavior across all chapters, including AI block formatting, multi-chapter routing, and content validation.

## Stabilization Goals

1. **Consistent AI Block Behavior**: All AI blocks follow the same formatting, token usage, and retry rules
2. **Multi-Chapter Routing**: Intelligent routing to the best matching chapter for queries
3. **Formatting Unification**: Consistent markdown, diagram, and quiz formatting across all chapters
4. **Content Validation**: Cross-chapter consistency checks for AI blocks, sections, and glossary

## Multi-Chapter Routing Rules

### Chapter Scoring

- **Relevance Threshold**: 0.7 (minimum score to consider a chapter)
- **Scoring Method**: Embedding similarity
- **Fallback Enabled**: Yes (if no chapter meets threshold)

### Chapter Affinity

- **Routing Strategy**: Best match (highest score wins)
- **Affinity Threshold**: 0.8 (minimum for strong affinity)
- **Multi-Chapter Support**: Yes (can route to multiple chapters)

### Fallback Retrieval

- **Strategy**: Search all chapters if primary routing fails
- **Error Handling**: Graceful degradation
- **Result Limit**: Top 5 results across all chapters

## Formatting Unification

### Markdown Rules

- **Headers**: Consistent level hierarchy (no skipped levels)
- **Lists**: Consistent bullet style and indentation
- **Code Blocks**: Language tags required, consistent formatting

### Diagram Formatting

- **Mermaid**: Syntax validation, type checking
- **PlantUML**: Syntax validation, type checking

### Quiz Formatting

- **Questions**: Clear question text, consistent formatting
- **Answers**: Single correct answer, multiple choice options
- **Structure**: Consistent question-answer-options format

## Validation Strategy

### AI Block Consistency

- **Check**: Number of AI blocks per chapter
- **Check**: AI block types
- **Check**: AI block structure
- **Report**: Inconsistencies and recommendations

### Section Ordering

- **Check**: Section order consistency
- **Check**: Section structure
- **Check**: Section naming
- **Report**: Inconsistencies and recommendations

### Glossary Structure

- **Check**: Glossary format consistency
- **Check**: Glossary structure
- **Check**: Glossary completeness
- **Report**: Inconsistencies and recommendations

## Build Validation

### Pre-Build Checks

1. **MDX Presence**: Verify all chapter MDX files exist
2. **Metadata Presence**: Verify all chapter metadata exists
3. **AI Block Presence**: Verify all chapters have AI blocks

### Validation Script

- **Location**: `scripts/pre_build_check.py`
- **Usage**: `python scripts/pre_build_check.py`
- **Output**: Pass/fail status for each check

## Future Enhancements

- Real rule enforcement
- Real multi-chapter routing
- Real formatting enforcement
- Real validation logic
- Real build validation
- Dynamic rule assignment
- Rule versioning

