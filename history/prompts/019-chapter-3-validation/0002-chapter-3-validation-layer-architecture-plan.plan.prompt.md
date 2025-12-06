---
id: 0002
title: Chapter 3 Validation Layer Architecture Plan
stage: plan
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 019-chapter-3-validation
branch: 019-chapter-3-validation
user: Leo
command: /sp.plan
labels: ["chapter-3", "validation", "physical-ai", "perception", "sensors", "architecture", "plan"]
links:
  spec: specs/019-chapter-3-validation/spec.md
  plan: specs/019-chapter-3-validation/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/019-chapter-3-validation/plan.md
tests:
  - Plan completeness validation
  - Plan actionability validation
---

## Prompt

User requested: `/sp.plan` following instructions from DOCUMENTATION.md (163-242)

Feature details:
- feature-id: 019-chapter-3-validation
- title: "Chapter 3 — Validation, Testing & Build Stability Layer"
- goal: Generate a complete ARCHITECTURE PLAN for Feature 019 including folder structure, validation architecture, component-level plan, test strategy, contracts mapping, acceptance plan, and risks & mitigations

Requirements:
1. Folder Structure Plan: All specification files, contract files, checklist files, documentation files, validator modules, test files
2. Validation Architecture (High-Level): Define all validation layers (MDX, placeholder, frontmatter, metadata, RAG chunk, backend import, frontend build)
3. Component-Level Plan: Describe validator modules (mdx_validator.py, metadata_validator.py, placeholder_validator.py, chunk_validator.py, runtime_checks.py) with TODO logic only
4. Test Strategy: Document manual checks, script-based placeholder checks, build + backend import tests, logical rules for acceptable failures
5. Contracts Mapping: Map each requirement from spec.md to file, validation rule, TODO stub
6. Acceptance Plan: Define success criteria, how to test MDX correctness, how to test metadata correctness, how to ensure build stability
7. Risks & Mitigations: Identify possible issues (section mismatch, wrong placeholders, chunk marker pairing errors, imports failing, build failures, metadata field mismatch, chunk file structure issues)

## Response snapshot

Successfully created comprehensive architecture plan for Chapter 3 validation layer:

**Created Files:**
1. `specs/019-chapter-3-validation/plan.md` - Complete architecture plan with:
   - Summary (validation suite for Chapter 3)
   - Technical context (dependencies, constraints, scale/scope)
   - Folder structure plan (specification files, contract files, checklist files, documentation files, validator modules, test files)
   - Validation architecture (high-level) - 8 validation layers:
     1. MDX Structure Validation
     2. Placeholder Validation
     3. Frontmatter Validation
     4. Metadata Validation
     5. Chunk Marker Validation
     6. RAG Chunk Validation
     7. Backend Import Validation
     8. Frontend Build Validation
   - Component-level plan (5 validator modules with TODO logic only):
     - mdx_validator.py (MDX structure validation)
     - metadata_validator.py (metadata consistency validation)
     - placeholder_validator.py (placeholder validation)
     - chunk_validator.py (chunk marker validation)
     - runtime_checks.py (backend imports, frontend build)
   - Test strategy (manual checks, script-based placeholder checks, build + backend import tests, logical rules for acceptable failures)
   - Contracts mapping (requirement to file mapping, validation rule details)
   - Acceptance plan (success criteria, MDX correctness testing, metadata correctness testing, build stability)
   - Risks & mitigations (7 risks with impact, mitigation, detection)
   - Integration points (Chapter 3 content, future integration)
   - Acceptance checks (7 categories)
   - Next steps

**Key Plan Details:**
- 8 validation layers: MDX Structure, Placeholder, Frontmatter, Metadata, Chunk Marker, RAG Chunk, Backend Import, Frontend Build
- 5 validator modules: mdx_validator.py, metadata_validator.py, placeholder_validator.py, chunk_validator.py, runtime_checks.py
- All validator modules contain TODO logic only (scaffold only, no implementation)
- Test strategy includes manual checks, script-based checks, build tests, logical rules for acceptable failures
- Contracts mapping maps all requirements from spec.md to files, validation rules, TODO stubs
- 7 risks identified with mitigations (section mismatch, wrong placeholders, chunk marker pairing errors, imports failing, build failures, metadata field mismatch, chunk file structure issues)

**Differences from Chapter 1 & 2 Validation:**
- Chunk marker validation: New validation layer for Chapter 3 (not in Chapter 1 & 2)
- HTML comment format validation: Validates AI-block HTML comment format (not React components)
- Feature 018 diagram names: Validates Feature 018 diagram names (perception-overview, sensor-types, cv-depth-flow, feature-extraction-pipeline)
- Chunk validator module: New validator module for chunk marker validation

**Pattern Consistency:**
- Follows Feature 009 (Chapter 1 Validation) and Feature 015 (Chapter 2 Validation) patterns
- Same validation architecture and structure
- Adapted for Chapter 3 content (Physical AI perception systems)
- Includes chunk marker validation for RAG preparation
- Includes HTML comment format validation for AI-blocks

## Outcome

- ✅ Impact: Complete validation architecture plan ready for task generation. All validation layers defined (8 layers). All validator modules planned (5 modules with TODO logic only). Test strategy comprehensive (manual, script-based, build tests). Contracts mapping complete (all requirements mapped). Acceptance plan detailed (success criteria, testing methods, build stability). Risks & mitigations identified (7 risks with mitigations). Integration points documented. Acceptance checks defined (7 categories). Plan is actionable and ready for direct conversion into tasks.
- 🧪 Tests: Plan completeness validation - PASS, Plan actionability validation - PASS
- 📁 Files: 1 plan file created (plan.md with comprehensive validation architecture plan)
- 🔁 Next prompts: `/sp.tasks` to create validation tasks
- 🧠 Reflection: Plan follows established patterns for maintainability. Clear separation between validation layers ensures comprehensive coverage. Chunk marker validation is a new requirement for Chapter 3. HTML comment format validation ensures correct AI-block format. All validator modules contain TODO logic only (scaffold only, no implementation). Test strategy ensures validation can be performed manually and automatically. Note: This is a validation layer plan - no actual validation implementation should be done, only validator module scaffolding with TODO logic.

## Evaluation notes (flywheel)

- Failure modes observed: None - planning phase completed successfully
- Graders run and results (PASS/FAIL): Plan completeness - PASS, Plan actionability - PASS
- Prompt variant (if applicable): Standard /sp.plan workflow following DOCUMENTATION.md instructions
- Next experiment (smallest change to proceed): Run `/sp.tasks` to create validation tasks
