---

description: "Task list for Docusaurus book shell and first chapter"
---

# Tasks: Docusaurus Book Shell

**Input**: Design documents from `/specs/001-docusaurus-book/`  
**Prerequisites**: plan.md (required), spec.md (user stories)

**Tests**: Tests are MANDATORY per constitution. Write/execute the verification script and `docusaurus build` before full implementation (red → green).

**Organization**: Tasks grouped by user story.

## Format: `[ID] [P?] [Story] Description`

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 Validate Node.js ≥18 available; document requirement in README.
- [ ] T002 Initialize npm project metadata (name, version, license) if missing.

---

## Phase 2: Foundational (Blocking Prerequisites)

- [ ] T003 Scaffold Docusaurus v3 TypeScript site at repo root (`npx create-docusaurus@latest . classic --typescript`).
- [ ] T004 [P] Add engines field (Node ≥18) and lockfile commit.
- [ ] T005 [P] Configure prettier/eslint defaults shipped by Docusaurus (accept defaults).

**Checkpoint**: Foundation ready.

---

## Phase 3: User Story 1 - Navigate the book shell (Priority: P1) 🎯 MVP

**Tests for User Story 1 (MANDATORY)**

- [ ] T010 [US1] Add `npm run test` script that invokes a content-verification Node script and `tsc --noEmit`; ensure it fails before chapter exists.
- [ ] T011 [US1] Implement `tests/check-course-structure.mjs` that asserts required doc IDs (course-overview) and sidebar sections exist; run to confirm RED.

**Implementation for User Story 1**

- [ ] T012 [US1] Configure `sidebars.ts` to include modules: Introduction, ROS 2, Gazebo/Unity, NVIDIA Isaac, Vision-Language-Action/Capstone (placeholders as needed).
- [ ] T013 [US1] Customize home page hero in `src/pages/index.tsx` with course title, CTA, and brief description referencing Physical AI & Humanoid Robotics.
- [ ] T014 [US1] Add README section with install/run/test instructions.

**Checkpoint**: Shell navigable; test script still RED on missing chapter content.

---

## Phase 4: User Story 2 - Read the first chapter (Priority: P1)

**Tests for User Story 2 (MANDATORY)**

- [ ] T020 [US2] Extend `tests/check-course-structure.mjs` to assert required headings: Overview, Learning Outcomes, Weekly Breakdown, Hardware Requirements; run to confirm RED before content.

**Implementation for User Story 2**

- [ ] T021 [US2] Create `docs/course-overview.md` with content derived from hackathon brief (overview, learning outcomes, weekly breakdown, hardware requirements).
- [ ] T022 [US2] Add module stub pages under `docs/modules/` for sidebar links (can be placeholder text).
- [ ] T023 [US2] Run `npm run test` and `npm run build` to achieve GREEN; update README with chapter link.

**Checkpoint**: Chapter renders with required sections; tests GREEN.

---

## Phase 5: User Story 3 - Build and test locally (Priority: P2)

- [ ] T030 [US3] Verify clean clone install + `npm run test` + `npm run build` succeeds; document in README.
- [ ] T031 [US3] Capture PHR note for this implementation session (per constitution).

---

## Phase N: Polish & Cross-Cutting Concerns

- [ ] T900 [P] Add favicon/logo to `static/` and update config (optional polish).
- [ ] T901 [P] Add CI workflow skeleton to run `npm run test` and `npm run build` (future).

---

## Dependencies & Execution Order

- Setup precedes foundational.
- Tests T010/T011/T020 must be authored and run RED before implementing corresponding content tasks.
- User stories proceed after foundational; User Story 1 before User Story 2 for navigation dependencies.
- Final verification (T030) after all implementation tasks.

