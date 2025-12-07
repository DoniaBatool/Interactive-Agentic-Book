# Release Checklist: Chapter 2 Build Validation + Release Packaging

**Feature**: 036-ch2-build-release
**Created**: 2025-01-27
**Purpose**: Validate Chapter 2 release readiness

## Build Validation

- [ ] Build passes
  - [ ] Frontend build (`npm run build`) completes without errors
  - [ ] Backend starts without import errors
  - [ ] No runtime exceptions during startup

## Metadata Validation

- [ ] Metadata validated
  - [ ] `chapter_2.py` imports without errors
  - [ ] Metadata structure matches expected schema
  - [ ] Section count matches MDX structure
  - [ ] AI blocks count matches MDX placeholders
  - [ ] Diagram placeholders count matches MDX placeholders

## AI-Block Routing

- [ ] AI-block routing ok
  - [ ] All 4 Chapter 2 endpoints exist (`/ai/ch2/ask`, `/ai/ch2/explain`, `/ai/ch2/quiz`, `/ai/ch2/diagram`)
  - [ ] Endpoints route to runtime engine correctly
  - [ ] Subagents exist and import without errors
  - [ ] Runtime engine handles chapterId=2 routing

## RAG Pipeline

- [ ] RAG pipeline imports ok
  - [ ] `ch2_pipeline.py` imports without errors
  - [ ] `ch2_embedding_client.py` imports without errors
  - [ ] `ch2_qdrant_store.py` imports without errors
  - [ ] `chapter_2_chunks.py` imports without errors
  - [ ] Runtime engine can import ch2_pipeline

## Validation Scripts

- [ ] Validation scripts exist
  - [ ] `scripts/ch2/validate_mdx_structure.py` exists
  - [ ] `scripts/ch2/validate_frontmatter.py` exists
  - [ ] `backend/app/validation/ch2_metadata_validator.py` exists
  - [ ] `scripts/ch2/run_all.py` exists
  - [ ] All scripts import without errors

## Release Packaging

- [ ] Release folder structure exists
  - [ ] `release/chapter-2/` folder exists
  - [ ] `release/chapter-2/README.md` exists
  - [ ] `release/chapter-2/CHANGELOG.md` exists
  - [ ] `release/chapter-2/chapter-2-export.json` exists
  - [ ] `release/chapter-2/assets/` folder exists
  - [ ] `scripts/ch2/package_release.py` exists

## Package.json

- [ ] package.json updated
  - [ ] `"validate:ch2"` command exists
  - [ ] Command points to correct script path

## Contracts and Documentation

- [ ] Contracts exist
  - [ ] `contracts/validation-rules.md` exists
  - [ ] `checklists/release.md` exists (this file)

---

## Validation Results

**Status**: ⏳ Pending (scaffolding phase)

**Notes**: All validation is placeholder-only. Real validation logic will be implemented in future features.

---

## Summary

This checklist ensures Chapter 2 build validation and release packaging scaffolding is complete. All items are placeholders—no real validation or packaging logic is implemented.

