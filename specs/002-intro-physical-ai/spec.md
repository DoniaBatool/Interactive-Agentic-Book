# Feature Specification: Intro to Physical AI Chapter

**Feature Branch**: `002-intro-physical-ai`  
**Created**: 2025-12-17  
**Status**: Draft  
**Input**: Write the full Intro to Physical AI chapter based on the hackathon course brief (focus, why it matters, sensors, safety, roadmap).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learn the overview (P1)
Learner opens the Intro chapter and understands what Physical AI is and why it matters.
**Acceptance**: Chapter has sections: Overview, Why Physical AI Matters.

### User Story 2 - See scope and prerequisites (P1)
Learner finds the course scope, prerequisites, and sensor stack upfront.
**Acceptance**: Sections include Scope, Prerequisites, Sensor Stack.

### User Story 3 - Understand roadmap and safety (P1)
Learner sees the module roadmap and safety/ethics guidance.
**Acceptance**: Sections include Module Roadmap, Safety & Ethics, Key Outcomes, Lab Preview.

## Requirements
- **FR-001**: Chapter must live at `docs/modules/intro.md`.
- **FR-002**: Include headings: Overview, Why Physical AI Matters, Scope, Prerequisites, Sensor Stack, Safety & Ethics, Module Roadmap, Key Outcomes, Lab Preview.
- **FR-003**: Use content derived from the hackathon brief (Physical AI focus, sensors, embodied intelligence).

## Success Criteria
- **SC-001**: Required headings exist and render.
- **SC-002**: Content references Physical AI purpose, sensors (LiDAR, depth/RGB, IMU), and safety.
- **SC-003**: `npm test` (content check + typecheck) passes.

