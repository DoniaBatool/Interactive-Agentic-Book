# Feature Specification: Docusaurus Book Shell

**Feature Branch**: `001-docusaurus-book`  
**Created**: 2025-12-17  
**Status**: Draft  
**Input**: User description: "Build the Physical AI & Humanoid Robotics textbook with Docusaurus per hackathon requirement #1, following Spec-Kit Plus hands-on and the project constitution."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Navigate the book shell (Priority: P1)

Learners can open the textbook site, see a branded hero, and navigate the course sections from the sidebar that mirrors the hackathon course outline (Intro, ROS 2, Gazebo/Unity, NVIDIA Isaac, VLA/Capstone).

**Why this priority**: Without a working shell and navigation, no content is discoverable; this is the minimum usable book.

**Independent Test**: Start the dev server, load the home page, and confirm the sidebar links render and route without 404s.

**Acceptance Scenarios**:

1. **Given** the Docusaurus site is installed, **When** I open `/` via `npm run start`, **Then** I see the course title, hero CTA, and sidebar sections for all modules in order.
2. **Given** the sidebar renders, **When** I click the ROS 2 module link, **Then** the docs router loads the corresponding page without error.

---

### User Story 2 - Read the first chapter (Priority: P1)

Readers can open a first chapter that summarizes the course overview, learning outcomes, and weekly breakdown derived from the hackathon brief.

**Why this priority**: Provides immediate instructional value and anchors the content model for later chapters.

**Independent Test**: Open the first chapter page and verify required sections (Overview, Learning Outcomes, Weekly Breakdown, Hardware Requirements) are present with course-specific text.

**Acceptance Scenarios**:

1. **Given** I open `/docs/course-overview`, **When** I scroll, **Then** I see sections for Overview, Learning Outcomes, Weekly Breakdown (Weeks 1–13 summary), and Hardware Requirements drawn from the hackathon doc.
2. **Given** the chapter renders, **When** I inspect headings, **Then** the text references Physical AI, ROS 2, Gazebo/Unity, NVIDIA Isaac, and VLA capstone.

---

### User Story 3 - Build and test locally (Priority: P2)

Developers can install dependencies, run tests/build, and get a green build for the book.

**Why this priority**: Ensures repeatable local setup and CI readiness; aligns with constitution TDD gates.

**Independent Test**: From a clean clone, run `npm install`, `npm run test`, and `npm run build`; all complete without errors.

**Acceptance Scenarios**:

1. **Given** a fresh checkout, **When** I run `npm install`, **Then** dependencies install without missing peer errors.
2. **Given** dependencies are installed, **When** I run `npm run test` (content verification + typecheck) and `npm run build`, **Then** both succeed.

### Edge Cases

- What happens when Node.js version is below the required minimum? (Expect clear failure message in docs/readme and engines field)
- How does the system handle missing sidebar entries? (Build should fail due to unresolved doc IDs; tests should catch missing first chapter file)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST scaffold a Docusaurus (v3) site at the repository root using TypeScript.
- **FR-002**: System MUST provide a sidebar that mirrors the hackathon course modules (Intro, ROS 2, Gazebo/Unity, NVIDIA Isaac, VLA/Capstone).
- **FR-003**: Users MUST be able to read the first chapter containing course overview, learning outcomes, weekly breakdown, and hardware requirements extracted from the hackathon brief.
- **FR-004**: System MUST include a home page hero describing "Physical AI & Humanoid Robotics" with CTA to start the course.
- **FR-005**: System MUST provide npm scripts for `start`, `build`, and `test` (where `test` includes content verification) and document usage in README.

### Key Entities *(include if feature involves data)*

- **Chapter**: Markdown/MDX document representing a course section with metadata (title, slug).
- **Sidebar Section**: Navigation grouping for course modules aligning to hackathon outline.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `npm run build` passes on a clean checkout without manual fixes.
- **SC-002**: First chapter page shows all required sections sourced from hackathon text.
- **SC-003**: Sidebar displays 5 module groupings matching the hackathon modules order.
- **SC-004**: `npm run test` (content verification + typecheck) passes, ensuring chapter presence before deployment.

