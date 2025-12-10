# Implementation Plan: Physical AI & Humanoid Robotics Complete Textbook

**Branch**: `061-physical-ai-complete-textbook` | **Date**: 2025-12-10 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/061-physical-ai-complete-textbook/spec.md`

## Summary

This plan delivers hackathon Requirement #1: a complete Physical AI & Humanoid Robotics textbook using Docusaurus. The book will cover all 4 course modules (ROS 2, Simulation, NVIDIA Isaac, VLA) structured according to the 13-week curriculum outline. Content will be written in MDX format, organized with proper navigation, and deployed to GitHub Pages.

**Technical Approach**: Replace existing placeholder chapters with comprehensive, curriculum-aligned content. Structure follows Docusaurus documentation best practices with sidebar navigation reflecting the learning progression from introductory concepts through advanced topics.

## Technical Context

**Language/Version**: MDX (Markdown + JSX), Docusaurus 3.9.2, TypeScript 5.6.2  
**Primary Dependencies**: @docusaurus/core, @docusaurus/preset-classic, React 19.0.0  
**Storage**: Static file system (Git repository), future RAG will use Qdrant + Neon Postgres  
**Testing**: Docusaurus build validation, link checker, content coverage verification  
**Target Platform**: Static site deployment to GitHub Pages  
**Project Type**: Web (Docusaurus documentation site with frontend React components)  
**Performance Goals**: Lighthouse score >90, page load <2s, mobile-friendly  
**Constraints**: Must follow hackathon course outline exactly, English content first  
**Scale/Scope**: 4 major modules, 13 weeks of content, ~15-20 pages total

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Compliance Verification

✅ **Principle I (SDD Methodology)**: Followed - this plan is part of the spec/plan/tasks workflow  
✅ **Principle II (Docusaurus-First)**: Followed - using MDX format, Docusaurus features, React components  
⚠️ **Principle III (RAG Architecture)**: Deferred - RAG is Requirement #2, this delivers content foundation  
⚠️ **Principle IV (Personalization)**: Deferred - content structure supports future personalization  
⚠️ **Principle V (Translation)**: Deferred - English content first, translation engine is separate feature  
✅ **Principle VI (TDD)**: Adapted - using build validation and content coverage tests instead of unit tests

**Justification for Deferred Principles**: Hackathon Requirement #1 specifically focuses on "write a book using Docusaurus." Requirements #2-7 (RAG, auth, personalization, translation) are separate deliverables. This feature establishes the content foundation that enables those future features.

### AI Architecture Compliance

✅ Content will use reusable intelligence approach - write one chapter manually, then create subagents/skills for remaining chapters  
✅ PHR will be created for this feature development  
⚠️ ADR may be needed if significant content organization decisions require justification

## Project Structure

### Documentation (this feature)

```text
specs/061-physical-ai-complete-textbook/
├── plan.md              # This file
├── spec.md              # Feature specification (already created)
├── tasks.md             # Will be created by /sp.tasks
└── contracts/
    └── content-schema.md # Content structure and organization contract
```

### Source Code (repository root)

```text
frontend/                           # Existing Docusaurus site
├── docs/                           # Documentation content (MDX files)
│   ├── intro.md                    # Homepage introduction (UPDATE)
│   ├── chapters/                   # Main textbook chapters (REPLACE)
│   │   ├── 00-introduction.mdx     # NEW: Physical AI overview, learning outcomes
│   │   ├── 01-module-1-ros2.mdx    # NEW: The Robotic Nervous System (Weeks 3-5)
│   │   ├── 02-module-2-simulation.mdx # NEW: Digital Twin - Gazebo & Unity (Weeks 6-7)
│   │   ├── 03-module-3-isaac.mdx   # NEW: AI-Robot Brain - NVIDIA Isaac (Weeks 8-10)
│   │   ├── 04-module-4-vla.mdx     # NEW: Vision-Language-Action (Weeks 11-13)
│   │   └── 05-hardware-requirements.mdx # NEW: Equipment specifications
│   └── [existing tutorial folders] # KEEP for now, may remove later
├── sidebars.ts                     # Sidebar navigation configuration (UPDATE)
├── docusaurus.config.ts            # Site configuration (already correct)
└── src/                            # React components (existing, no changes needed)
```

**Structure Decision**: Use existing `frontend/docs/chapters/` directory and replace placeholder chapters with curriculum-aligned content. Each module becomes one comprehensive MDX file with proper heading hierarchy. This structure supports future RAG chunking by section.

## Complexity Tracking

**No constitutional violations requiring justification**. All deferred principles (RAG, personalization, translation) are explicitly scoped as separate hackathon requirements.

## Phase 0: Research

### Research Questions

1. **Content Organization**: Should each module be a single large file or split into multiple sub-pages?
   - **Answer**: Single file per module with section anchors. Rationale: Easier navigation, better for future RAG chunking by semantic sections.

2. **Technical Depth**: What level of detail is appropriate for code examples?
   - **Answer**: High-level conceptual code with comments, not production-ready. This is a textbook, not implementation docs.

3. **Existing Content**: What from current chapters (1-3) should be preserved vs. rewritten?
   - **Answer**: Current chapters are off-topic (not aligned with course outline). Replace entirely with course curriculum content.

4. **Hardware Requirements**: Should hardware specs be in a separate chapter or integrated?
   - **Answer**: Separate chapter at the end. Rationale: Reference material, not learning progression content.

### Existing Patterns

**From Constitution**:
- Content must be in MDX format
- Chapters should include PersonalizationButton and TranslationButton components (placeholders)
- Use existing AI components (AskQuestionBlock, ExplainLike10Block, etc.) but don't require them to function
- Follow Docusaurus sidebar organization best practices

**From Current Site**:
- Existing `sidebars.ts` uses `tutorialSidebar` with items array
- Chapters use frontmatter: `title`, `description`, `sidebar_position`, `sidebar_label`, `tags`
- Components imported from `@site/src/components/`

### Research Artifacts

**Key References**:
1. Hackathon document: Complete course outline (Weeks 1-13)
2. Existing sidebars.ts: Navigation structure pattern
3. Existing chapter-1.mdx: Formatting and component usage example
4. Constitution: Docusaurus-first strategy, content organization principles

**No external dependencies** beyond Docusaurus and existing site structure.

## Phase 1: Design

### Data Model

```yaml
# Content Organization Schema

TextbookStructure:
  - Homepage (intro.md)
  - Introduction Chapter (00-introduction.mdx)
      - What is Physical AI?
      - Why Physical AI Matters
      - Learning Outcomes (6 objectives)
      - Weekly Breakdown Overview
  - Module 1: ROS 2 (01-module-1-ros2.mdx)
      - Weeks 3-5 Content
      - ROS 2 Fundamentals
      - Nodes, Topics, Services, Actions
      - Python Integration (rclpy)
      - URDF for Humanoids
  - Module 2: Simulation (02-module-2-simulation.mdx)
      - Weeks 6-7 Content
      - Gazebo Environment Setup
      - URDF and SDF Formats
      - Physics Simulation
      - Unity Integration
      - Sensor Simulation (LiDAR, Depth Cameras, IMUs)
  - Module 3: NVIDIA Isaac (03-module-3-isaac.mdx)
      - Weeks 8-10 Content
      - Isaac SDK and Isaac Sim
      - Photorealistic Simulation
      - Synthetic Data Generation
      - Isaac ROS (VSLAM, Navigation)
      - Nav2 Path Planning
      - Sim-to-Real Transfer
  - Module 4: VLA (04-module-4-vla.mdx)
      - Weeks 11-13 Content
      - Vision-Language-Action Overview
      - Voice-to-Action (OpenAI Whisper)
      - Cognitive Planning with LLMs
      - Natural Language → ROS 2 Actions
      - Capstone Project Description
  - Hardware Requirements (05-hardware-requirements.mdx)
      - Digital Twin Workstation Specs
      - Physical AI Edge Kit
      - Robot Lab Options (3 tiers)
      - On-Premise vs Cloud-Native Lab
      - Economy Jetson Student Kit
```

### Content Contract

**See**: `contracts/content-schema.md` for detailed content structure, section requirements, and quality standards.

**Key Constraints**:
- Each module chapter must have consistent structure: Overview → Weekly Content → Practical Examples → Summary
- Code examples must use Python for ROS 2 (rclpy)
- Technical terms must have inline explanations or glossary links
- All content must be mobile-friendly (no extremely wide tables or code blocks)
- Frontmatter metadata must be complete (title, description, position, label, tags)

### Interface Contracts

**Input Interfaces**: N/A (static content creation)

**Output Interfaces**:
1. **Docusaurus Build Output**
   - Static HTML/CSS/JS files
   - Sitemap.xml
   - Search index (if search plugin enabled)
   - Responsive pages

2. **Navigation Structure**
   - Sidebar with chapter hierarchy
   - Prev/Next navigation links
   - Breadcrumbs

3. **Future RAG Integration Points**
   - Each module chapter will have semantic sections with clear headings
   - Content organized for easy chunking by section
   - Metadata in frontmatter for filtering (tags, difficulty level)

### Component Architecture

**No new components needed**. Use existing:
- PersonalizationButton (placeholder)
- TranslationButton (placeholder)
- AskQuestionBlock (optional, may not function yet)
- ExplainLike10Block (optional)
- InteractiveQuizBlock (optional)
- GenerateDiagramBlock (optional)

**Component Usage**: Include component imports and placeholders in MDX, but content must be readable without them functioning.

### Testing Strategy

**Build Validation**:
```bash
cd frontend && npm run build
# Must complete with exit code 0
```

**Link Validation**:
- All internal links must resolve (no 404s)
- Sidebar navigation must include all chapters

**Content Coverage**:
- Verify all 4 modules exist as chapters
- Verify introduction chapter exists
- Verify hardware requirements chapter exists
- Cross-reference with course outline to ensure all weeks 1-13 are covered

**Visual Testing**:
- Spot-check chapters on mobile viewport (DevTools)
- Verify code blocks don't overflow horizontally
- Confirm sidebar navigation is usable

### Deployment Strategy

**Build and Deploy**:
```bash
cd frontend
npm run build           # Creates build/ directory with static files
npm run deploy          # Deploys to GitHub Pages (gh-pages branch)
```

**Verification**:
- Visit https://doniabatool.github.io/Interactive-Agentic-Book/
- Navigate through all chapters via sidebar
- Test mobile responsiveness
- Verify no console errors in browser DevTools

## Phase 2: Task Breakdown

**Will be created in `tasks.md` by the `/sp.tasks` command**

High-level task categories:
1. Content Research and Outlining (gather course outline details)
2. Chapter 00: Introduction (write from course Weeks 1-2)
3. Chapter 01: Module 1 ROS 2 (write from course Weeks 3-5)
4. Chapter 02: Module 2 Simulation (write from course Weeks 6-7)
5. Chapter 03: Module 3 Isaac (write from course Weeks 8-10)
6. Chapter 04: Module 4 VLA (write from course Weeks 11-13)
7. Chapter 05: Hardware Requirements (extract from course document)
8. Update Sidebar Navigation Configuration
9. Update Homepage (intro.md)
10. Build and Test
11. Deploy to GitHub Pages
12. Create PHR

## Non-Functional Requirements

### Performance
- Page load time: < 2 seconds on 3G connection
- Lighthouse Performance score: > 90
- No layout shift (CLS < 0.1)

### Accessibility
- Lighthouse Accessibility score: > 95
- Proper heading hierarchy (h1 → h2 → h3)
- Alt text for any images (if added)
- Keyboard navigation functional

### SEO
- Proper meta descriptions in frontmatter
- Semantic HTML structure
- Sitemap generated

### Security
- No secrets or credentials in content
- GitHub Pages HTTPS by default
- No XSS vulnerabilities (static content)

## Risk Analysis

| Risk | Impact | Mitigation |
|------|--------|------------|
| Content scope too large for manual writing | High | Use reusable intelligence: write one chapter manually, create subagent/skill for others |
| Technical depth mismatch (too advanced or too basic) | Medium | Follow course outline exactly, target mixed-level audience as specified |
| Docusaurus build errors from malformed MDX | Medium | Validate build frequently, use linter, test incrementally |
| Course outline interpretation ambiguity | Medium | Document assumptions in content-schema.md contract |
| Hardware requirements section too detailed | Low | Summarize in textbook, link to hackathon doc for full specs |

## Success Metrics

### Quantitative
- ✅ Docusaurus build exits with code 0
- ✅ 6 chapter files created (intro + 4 modules + hardware)
- ✅ All 13 weeks of course content represented
- ✅ 0 broken internal links
- ✅ Lighthouse scores: Performance >90, Accessibility >95
- ✅ Site deployed and accessible at GitHub Pages URL

### Qualitative
- ✅ Content follows logical learning progression
- ✅ Technical explanations are clear and well-structured
- ✅ Code examples are relevant and commented
- ✅ Navigation is intuitive
- ✅ Content is ready for future RAG integration (well-organized sections)

## Open Questions

1. **Should we keep existing tutorial-basics and tutorial-extras folders?**
   - **Recommendation**: Keep for now (don't break existing structure), mark as "sample content" or remove in future cleanup

2. **How detailed should code examples be?**
   - **Recommendation**: Conceptual examples with inline comments, 10-30 lines max per example, focus on illustrating concepts not production code

3. **Should we add images/diagrams?**
   - **Recommendation**: Defer to separate feature. Use placeholder comments like `<!-- DIAGRAM: ros2-architecture -->` for future diagram generation

## Revision History

- **2025-12-10**: Initial plan created
- [Future updates tracked here]

