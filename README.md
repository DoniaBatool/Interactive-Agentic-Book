# Physical AI & Humanoid Robotics Textbook

Built with Docusaurus v3 (TypeScript). Each chapter is a feature with spec → plan → tasks per the project constitution.

## Prerequisites

- Node.js ≥ 18 (nvm recommended)
- npm (bundled with Node)

## Install

```bash
npm install
```

## Develop

```bash
npm start
```

## Test (content + typecheck)

```bash
npm test
```

## Build

```bash
npm run build
```

## Structure

- `docs/course-overview.md`: first chapter (overview, outcomes, weekly breakdown, hardware)
- `docs/modules/*`: module stubs (Introduction, ROS 2, Gazebo/Unity, NVIDIA Isaac, VLA capstone)
- `sidebars.ts`: manual sidebar matching the course outline
- `tests/check-course-structure.mjs`: validates required docs and sidebar links

## Prompt History

Record prompts under `history/prompts/` (per-feature folders plus `history/prompts/general` for shared prompts).
