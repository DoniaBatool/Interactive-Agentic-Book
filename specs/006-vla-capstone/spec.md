# Feature Specification: Chapter 5 – Vision-Language-Action Capstone

**Feature Branch**: `006-vla-capstone`  
**Created**: 2025-12-17  
**Status**: Draft  
**Input**: Write Chapter 5 covering VLA (Vision-Language-Action) capstone: voice-to-action, planning, navigation, perception, manipulation for humanoids.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Navigate Chapter 5 (P1)
Learner opens Chapter 5 and sees all VLA capstone sections.
**Acceptance**: Chapter has defined headings and renders without errors.

### User Story 2 - Understand voice-to-action flow (P1)
Learner sees how voice input becomes actionable robot goals.
**Acceptance**: Sections cover voice capture, ASR (Whisper), intent parsing, safety gating.

### User Story 3 - Plan and execute actions (P1)
Learner understands planning from natural language to ROS 2 actions/navigation/manipulation.
**Acceptance**: Planning + execution sections explain ROS actions, Nav2, perception hooks, and arm/hand control.

### User Story 4 - Evaluate and iterate (P2)
Learner can see how to test, evaluate, and iterate the capstone.
**Acceptance**: Sections include testing, safety, evaluation metrics, and next steps.

## Requirements
- **FR-001**: Chapter must reside at `docs/modules/vla-capstone.md` and be labeled as “Chapter 5”.
- **FR-002**: Include headings: Chapter title, Overview, Voice-to-Action Pipeline, Intent Parsing & Planning, Navigation & Manipulation Execution, Perception Hooks, Safety & Guardrails, Evaluation & Metrics, Demo Tips, Recap/Key Outcomes, Next Steps.
- **FR-003**: Content grounded in humanoid context (Physical AI stack, ROS 2, Nav2, perception).

## Success Criteria
- **SC-001**: Required headings present and ordered as specified.
- **SC-002**: Voice-to-action flow (ASR → intent → plan → actions) described.
- **SC-003**: Planning/execution covers ROS actions/Nav2/manipulation and perception integration.
- **SC-004**: Safety/guardrails and evaluation/metrics included.
- **SC-005**: `npm test` (content check + typecheck) passes after chapter is added.

