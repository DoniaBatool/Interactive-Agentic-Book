# Implementation Plan: Chapter 5 – Vision-Language-Action Capstone

**Branch**: `006-vla-capstone` | **Date**: 2025-12-17 | **Spec**: `specs/006-vla-capstone/spec.md`

## Summary
Write Chapter 5 at `docs/modules/vla-capstone.md` (Chapter 5: Vision-Language-Action Capstone) covering voice-to-action pipelines, intent parsing/planning, navigation/manipulation execution, perception hooks, safety/guardrails, evaluation/metrics, and demo tips.

## Technical Context
**Stack**: Docusaurus v3 (Markdown/MDX), TypeScript site  
**Target file**: `docs/modules/vla-capstone.md`  
**Testing**: `npm test` (content check + typecheck)  
**Constraints**: Humanoid/VLA context; concise, RAG-friendly sections.

## Constitution Check
- Spec and plan exist before implementation.  
- Tests required: run `npm test` after content changes.  
- Docs-only changes for this feature.

## Project Structure (this feature)
```
specs/006-vla-capstone/
├── spec.md
├── plan.md
├── tasks.md
├── data-model.md
├── research.md
├── quickstart.md
├── contracts/
└── checklists/
```

## Implementation Notes
- Emphasize end-to-end flow: voice → intent → plan → navigation/manipulation → feedback.
- Include safety guardrails and evaluation metrics for the capstone demo.

