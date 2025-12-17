# Implementation Plan: Docusaurus Book Shell

**Branch**: `001-docusaurus-book` | **Date**: 2025-12-17 | **Spec**: `specs/001-docusaurus-book/spec.md`
**Input**: Feature specification from `/specs/001-docusaurus-book/spec.md`

## Summary

Create the Physical AI & Humanoid Robotics textbook site with Docusaurus v3 (TypeScript). Deliver a branded home page, sidebar aligned to the hackathon course modules, and the first chapter covering overview, learning outcomes, weekly breakdown, and hardware requirements. Provide npm scripts for start/build/test so the site can be built and verified locally and in CI.

## Technical Context

**Language/Version**: TypeScript on Node.js ≥ 18 (engines enforced)  
**Primary Dependencies**: `@docusaurus/core`, `@docusaurus/preset-classic`, React 18  
**Storage**: Static Markdown/MDX files in `docs/` (no DB)  
**Testing**: `npm run test` wired to a lightweight content verification script + `tsc --noEmit`; `npm run build` for acceptance  
**Target Platform**: Static site (GitHub Pages/Vercel compatible)  
**Project Type**: Static documentation site (single-project layout)  
**Performance Goals**: Successful static build; keep bundle size default; images optimized via Docusaurus defaults  
**Constraints**: Must align sidebar with hackathon modules; follow constitution TDD and documentation gates  
**Scale/Scope**: Initial shell + first chapter; future chapters via subagents/skills

## Constitution Check

- Spec exists and is approved for this feature (`spec.md`).  
- Plan documents tooling and tests before implementation (TDD gate).  
- Tests will be codified as `npm run test` (content verification + typecheck) and `npm run build` for acceptance; tests must run red → green.  
- Documentation-first: Docusaurus structure maintained; README to document commands.  
- Security: no secrets involved; ensure `.env` not needed for this feature.  
- Governance: Work on branch `001-docusaurus-book`; create PHR after session.

## Project Structure

### Documentation (this feature)

```text
specs/001-docusaurus-book/
├── plan.md
├── spec.md
└── tasks.md
```

### Source Code (repository root)

```text
docs/
  course-overview.md           # First chapter derived from hackathon doc
  modules/                     # Placeholder folder for future chapters
src/
  pages/
    index.tsx                  # Hero/home customization
  components/                  # Reusable UI (if needed later)
static/                        # Assets (logos, images)
docusaurus.config.ts
sidebars.ts
package.json
tsconfig.json
```

**Structure Decision**: Single Docusaurus project at repo root using classic preset with TypeScript; documentation under `docs/` with future module-specific subfolders.

## Complexity Tracking

No constitutional violations anticipated. Tests are lightweight to satisfy TDD without adding unnecessary dependencies.*** End Patch​

