# Data Model: Chapter 3 Content Specification

**Feature**: 037-ch3-content-spec
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for Chapter 3 content specification

## Entity Definitions

### 1. Content Specification (Primary Entity)

**Description**: Represents the complete content blueprint for Chapter 3, defining structure, placeholders, glossary, and formatting rules

**Storage**: Specification files in `specs/037-ch3-content-spec/`

**Structure**:
```yaml
Content Specification:
  sections: List[SectionSpec]
  metadata: MetadataSpec
  placeholders: PlaceholderSpec
  glossary: GlossarySpec
  formatting: FormattingRules
```

**Specification Components**:
- Section definitions (7 sections)
- Metadata requirements
- Placeholder definitions (diagrams, AI blocks)
- Glossary term definitions
- Formatting rules

---

### 2. Section Specification (Sub-entity)

**Description**: Defines a single section with purpose, outcomes, content description, and placeholders

**Structure**:
```yaml
SectionSpec:
  title: str                    # Section title
  purpose: str                  # What the section teaches
  expected_outcome: str          # What students should understand
  content_description: str       # What content will appear
  ai_blocks: List[AIBlockSpec]  # Required AI blocks
  diagrams: List[DiagramSpec]    # Required diagrams
```

**Chapter 3 Sections** (7 total):
1. What Is Perception in Physical AI?
2. Types of Sensors in Robotics
3. Computer Vision & Depth Perception
4. Signal Processing Basics for AI
5. Feature Extraction & Interpretation
6. Learning Objectives
7. Glossary

---

### 3. Metadata Specification (Sub-entity)

**Description**: Defines required metadata fields and constraints

**Structure**:
```python
MetadataSpec:
  id: int = 3
  title: str = "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
  summary: str  # 50-300 characters
  section_count: int = 7
  sections: List[str]  # 7 section titles
  ai_blocks: List[str]  # 4 AI block types
  diagram_placeholders: List[str]  # 4 diagram names
  difficulty_level: str = "intermediate"
  prerequisites: List[int] = [1, 2]
  learning_outcomes: List[str]  # 3-8 items
  glossary_terms: List[str]  # 6-10 items
  last_updated: str  # ISO 8601 timestamp
```

---

### 4. Placeholder Specification (Sub-entity)

**Description**: Defines diagram and AI-block placeholder requirements

**Structure**:
```yaml
PlaceholderSpec:
  diagrams:
    - name: str  # Kebab-case
      section: int  # Section number
      position: str  # "middle" or "end"
  ai_blocks:
    - type: str  # "ask-question", "explain-like-i-am-10", etc.
      section: int  # Section number
      position: str  # "middle" or "end"
```

**Required Placeholders**:
- Diagrams: perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline
- AI Blocks: ask-question, generate-diagram, explain-like-i-am-10, interactive-quiz

---

### 5. Glossary Specification (Sub-entity)

**Description**: Defines glossary term requirements

**Structure**:
```yaml
GlossarySpec:
  terms: List[TermSpec]
  
TermSpec:
  term: str  # Term name
  definition_style: str  # "10-100 words, plain language, analogies"
```

**Required Terms** (6-10):
- Perception
- Sensor
- Computer Vision
- Depth Perception
- Signal Processing
- Feature Extraction
- LiDAR (or alternative)

---

### 6. Formatting Rules (Sub-entity)

**Description**: Defines content formatting constraints

**Structure**:
```yaml
FormattingRules:
  reading_level: str = "Grade 7-8"
  paragraph_max_sentences: int = 4
  sentence_avg_words: int = 15-20
  tone: str = "conversational-educational"
  section_order: List[str]  # Must follow course document
```

---

## Relationships

- Content Specification → Section Specifications (1:N)
- Content Specification → Metadata Specification (1:1)
- Content Specification → Placeholder Specification (1:1)
- Content Specification → Glossary Specification (1:1)
- Content Specification → Formatting Rules (1:1)

---

## Data Flow

1. **Specification**: Content Specification → Section Definitions → Placeholder Mappings
2. **Validation**: Specification → Validation Rules → Checklist
3. **Implementation**: Specification → MDX Structure → Metadata File

---

## Summary

All structures are specification definitions. No actual content is written—only the blueprint structure is defined.

