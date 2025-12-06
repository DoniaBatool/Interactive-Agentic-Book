# Quickstart Guide: Validating Chapter 3 — Validation, Testing & Build Stability Layer

**Feature**: 019-chapter-3-validation
**Branch**: `019-chapter-3-validation`
**Estimated Time**: 30-60 minutes (validation checks only, no implementation)

## Prerequisites

Before starting validation, ensure you have:

- [x] Feature 017 (Chapter 3 Content) completed (structure exists)
- [x] Feature 018 (Chapter 3 Planning Layer) completed (structure with chunk markers exists)
- [x] Docusaurus frontend running at `http://localhost:3000`
- [x] FastAPI backend structure exists at `backend/app/`
- [x] Git branch `019-chapter-3-validation` checked out
- [x] Read `specs/019-chapter-3-validation/spec.md`
- [x] Read `specs/019-chapter-3-validation/research.md` (validation methodology)
- [x] Read `specs/019-chapter-3-validation/data-model.md` (validation data structures)
- [x] Read `specs/019-chapter-3-validation/contracts/validation-schema.md` (validation rules)

## Validation Overview

**Total Steps**: 6 validation categories
**Primary Deliverable**: Validation report with all results
**Secondary Deliverable**: Validation schemas and contracts
**Validation**: Manual validation checks + automated build tests

---

## Phase 1: MDX Structure Validation (10 minutes)

### Step 1.1: Validate File Existence

**Action**: Verify MDX file exists at `frontend/docs/chapters/chapter-3.mdx`

**Command**: Check file exists
```bash
# Windows PowerShell
Test-Path frontend\docs\chapters\chapter-3.mdx
```

**Expected Result**: File exists

---

### Step 1.2: Validate Section Count

**Action**: Count H2 sections in MDX file

**Command**: Count H2 sections
```bash
# Windows PowerShell
Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '^## ' | Measure-Object | Select-Object -ExpandProperty Count
```

**Expected Result**: Exactly 7 sections

---

### Step 1.3: Validate Section Order

**Action**: Verify section titles match specification exactly

**Command**: Extract section titles
```bash
# Windows PowerShell
Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '^## ' | ForEach-Object { $_.Line }
```

**Expected Result**: 7 sections in correct order:
1. What Is Perception in Physical AI?
2. Types of Sensors in Robotics
3. Computer Vision & Depth Perception
4. Signal Processing Basics for AI
5. Feature Extraction & Interpretation
6. Learning Objectives
7. Glossary

---

### Step 1.4: Validate Frontmatter

**Action**: Verify frontmatter completeness

**Command**: Check frontmatter fields
- Open `frontend/docs/chapters/chapter-3.mdx`
- Verify frontmatter contains:
  - `title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"`
  - `description: "..."` (non-empty, 10-250 characters)
  - `sidebar_position: 3`
  - `sidebar_label: "Chapter 3: Physical AI Perception Systems"`
  - `tags: ["physical-ai", "sensors", "perception", "signal-processing"]`

**Expected Result**: All frontmatter fields present and valid

---

## Phase 2: Placeholder Validation (10 minutes)

### Step 2.1: Validate Diagram Placeholders

**Action**: Count and verify diagram placeholders

**Command**: Count diagram placeholders
```bash
# Windows PowerShell
Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- DIAGRAM:' | Measure-Object | Select-Object -ExpandProperty Count
```

**Expected Result**: Exactly 4 diagram placeholders:
- `<!-- DIAGRAM: perception-overview -->`
- `<!-- DIAGRAM: sensor-types -->`
- `<!-- DIAGRAM: cv-depth-flow -->`
- `<!-- DIAGRAM: feature-extraction-pipeline -->`

---

### Step 2.2: Validate AI-Block Placeholders

**Action**: Count and verify AI-block HTML comment placeholders

**Command**: Count AI-block placeholders
```bash
# Windows PowerShell
Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- AI-BLOCK:' | Measure-Object | Select-Object -ExpandProperty Count
```

**Expected Result**: Exactly 4 AI-block HTML comment placeholders:
- `<!-- AI-BLOCK: ask-question -->`
- `<!-- AI-BLOCK: explain-like-i-am-10 -->`
- `<!-- AI-BLOCK: interactive-quiz -->`
- `<!-- AI-BLOCK: generate-diagram -->`

---

### Step 2.3: Validate Naming Conventions

**Action**: Verify all placeholders use correct naming conventions

**Validation**:
- All diagram placeholders use kebab-case
- All AI-block placeholders use HTML comment format
- All placeholders match metadata lists exactly

**Expected Result**: All naming conventions correct

---

## Phase 3: Chunk Marker Validation (10 minutes)

### Step 3.1: Validate Chunk Marker Count

**Action**: Count CHUNK: START and CHUNK: END markers

**Command**: Count chunk markers
```bash
# Windows PowerShell
Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- CHUNK: START -->' | Measure-Object | Select-Object -ExpandProperty Count
Select-String -Path 'frontend\docs\chapters\chapter-3.mdx' -Pattern '<!-- CHUNK: END -->' | Measure-Object | Select-Object -ExpandProperty Count
```

**Expected Result**: Exactly 7 START markers and 7 END markers

---

### Step 3.2: Validate Chunk Marker Pairing

**Action**: Verify all chunk markers are properly paired

**Validation**:
- Each CHUNK: START has corresponding CHUNK: END
- Chunk markers align with H2 section boundaries
- Chunk markers are placed at logical semantic boundaries

**Expected Result**: All chunk markers properly paired

---

## Phase 4: Metadata Validation (10 minutes)

### Step 4.1: Validate Metadata Import

**Action**: Test metadata file import

**Command**: Import metadata
```bash
python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA; print('Import: SUCCESS')"
```

**Expected Result**: Import succeeds without errors

---

### Step 4.2: Validate Metadata Fields

**Action**: Verify all required fields present

**Validation**:
- `id: 3`
- `section_count: 7`
- `sections: [...]` (7 items matching MDX)
- `ai_blocks: [...]` (4 items)
- `diagram_placeholders: [...]` (4 items, Feature 018 names)
- `difficulty_level: "intermediate"`
- `prerequisites: [1, 2]`
- `learning_outcomes: [...]` (3-10 items)
- `glossary_terms: [...]` (7 items)

**Expected Result**: All required fields present and valid

---

### Step 4.3: Validate Cross-Validation

**Action**: Verify MDX ↔ metadata consistency

**Validation**:
- MDX `title` matches metadata `title`
- MDX section count matches metadata `section_count`
- MDX section titles match metadata `sections` list
- MDX diagram placeholders match metadata `diagram_placeholders` list
- MDX AI-block placeholders match metadata `ai_blocks` list

**Expected Result**: All cross-validations pass

---

## Phase 5: Build Validation (10 minutes)

### Step 5.1: Validate Frontend Build

**Action**: Run frontend build

**Command**: Build frontend
```bash
cd frontend
npm run build
```

**Expected Result**: Build completes with exit code 0, no errors

---

### Step 5.2: Validate Backend Import

**Action**: Test backend imports

**Command**: Import backend modules
```bash
python -c "from app.content.chapters.chapter_3 import CHAPTER_METADATA; from app.content.chapters.chapter_3_chunks import get_chapter_chunks; print('Imports: SUCCESS')"
```

**Expected Result**: All imports succeed without errors

---

## Phase 6: Validation Report Generation (10 minutes)

### Step 6.1: Generate Validation Report

**Action**: Create validation report with all results

**File**: `specs/019-chapter-3-validation/checklists/validation-report.md`

**Content**:
- All validation results
- Pass/fail status for each category
- Error and warning messages
- Recommendations

**Expected Result**: Comprehensive validation report generated

---

## Success Criteria

### Validation Complete
- [x] All MDX structure validations pass
- [x] All placeholder validations pass
- [x] All chunk marker validations pass
- [x] All metadata validations pass
- [x] All build validations pass
- [x] Validation report generated

### Structure Validated
- [x] Exactly 7 H2 sections
- [x] Exactly 4 diagram placeholders (Feature 018 names)
- [x] Exactly 4 AI-block HTML comment placeholders
- [x] Exactly 7 chunk marker pairs
- [x] Exactly 7 glossary terms

### Metadata Validated
- [x] All required fields present
- [x] Cross-validation passes (MDX ↔ metadata)
- [x] Imports without errors

### Build Validated
- [x] Frontend build passes
- [x] Backend imports without errors

---

## Troubleshooting

### Issue: Section Count Mismatch
**Solution**: Verify MDX file has exactly 7 H2 sections, check for typos in section headings

### Issue: Chunk Marker Pairing Error
**Solution**: Verify each CHUNK: START has corresponding CHUNK: END, check alignment with section boundaries

### Issue: Metadata Import Error
**Solution**: Check Python syntax, verify all required fields present, check for circular dependencies

### Issue: Build Failure
**Solution**: Check MDX syntax, verify frontmatter is valid YAML, check for broken Markdown

### Issue: Placeholder Naming Mismatch
**Solution**: Verify diagram names match Feature 018 names, verify AI-block format is HTML comments

---

## Next Steps

After completing validation:

1. **Planning Phase**: Run `/sp.plan` to create validation plan
2. **Task Generation**: Run `/sp.tasks` to create validation tasks
3. **Implementation**: Run `/sp.implement` to execute validation checks
4. **Report Generation**: Generate comprehensive validation report
5. **Integration**: Validate future AI integration readiness (Feature 020)

---

## Notes

- This validation layer validates the structure created in Feature 018
- Feature 018 uses HTML comment format for AI-blocks (not React components)
- Feature 018 uses different diagram names (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
- Feature 018 requires chunk markers (CHUNK: START / CHUNK: END) for RAG preparation
- All validation checks must be testable and measurable
- Validation report must indicate pass/fail status for each category
