---
id: 0002
title: Chapter 1 Interactive AI Blocks Architecture Plan
stage: plan
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 004-chapter-1-interactive-blocks
branch: 004-chapter-1-interactive-blocks
user: Leo
command: /sp.plan
labels: ["chapter-1", "ai-blocks", "frontend-components", "backend-api", "mdx-integration", "planning"]
links:
  spec: specs/004-chapter-1-interactive-blocks/spec.md
  plan: specs/004-chapter-1-interactive-blocks/plan.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/004-chapter-1-interactive-blocks/plan.md
tests:
  - Architecture plan validation (ALL PASS)
---

## Prompt

User requested: `/sp.plan` for feature `004-chapter-1-interactive-blocks`

User noted that plan.md should be created for `004-chapter-1-interactive-blocks` feature (not `003-chapter-1-content`).

## Response

Created comprehensive architecture plan for Chapter 1 Interactive AI Blocks feature:

### Architecture Plan Created

**File**: `specs/004-chapter-1-interactive-blocks/plan.md`

### Key Architecture Decisions

**1. Component Architecture**:
- 4 React TypeScript components in `frontend/src/components/ai/`
- Minimal props interfaces (chapterId, sectionId, concept, etc.)
- Placeholder event handlers (console.log only)
- Inline styling for scaffolding phase

**2. MDX Integration Strategy**:
- Option A: Create `frontend/src/mdx-components.ts` with component exports
- Option B (fallback): Swizzle `MDXComponents` if Option A doesn't work
- Components replace `<!-- AI-BLOCK: type -->` comments directly in MDX

**3. Backend API Architecture**:
- Single router file: `backend/app/api/ai_blocks.py`
- 4 endpoints: `/api/ai/ask-question`, `/api/ai/explain-like-10`, `/api/ai/quiz`, `/api/ai/diagram`
- Pydantic request/response models for validation
- Placeholder responses: `{"message": "AI block placeholder", "received": <payload>}`

**4. Component Props Design**:
- `AskQuestionBlock`: `{ chapterId?, sectionId? }`
- `ExplainLike10Block`: `{ concept?, chapterId? }`
- `InteractiveQuizBlock`: `{ chapterId?, numQuestions? }`
- `GenerateDiagramBlock`: `{ diagramType?, chapterId? }`

**5. Styling Approach**:
- Inline styles or minimal CSS modules
- No external CSS framework (scaffolding only)
- Future features can add proper styling system

### Technical Context

- **Frontend**: React 18+ + TypeScript + Docusaurus 3.x MDX
- **Backend**: FastAPI 0.109+ + Pydantic 2.x
- **No new dependencies** required
- **Scaffolding only** - no real AI logic

### Constitution Compliance

✅ **Principle I - SDD**: Plan created following spec → plan → tasks workflow
✅ **Principle II - Docusaurus-First**: MDX component integration strategy documented
✅ **Principle III - RAG-First**: API contracts ready for future RAG integration
✅ **Principle IV - Personalization**: Component props support future personalization
✅ **Principle V - Multilingual**: Structure supports translation (implementation deferred)
✅ **Principle VI - TDD**: Manual validation methods specified (automated tests deferred)

### Files Created

- `specs/004-chapter-1-interactive-blocks/plan.md` - Complete architecture plan

### Next Steps

1. **Run `/sp.tasks`** to generate implementation tasks
2. **Review architecture** with user for approval
3. **Begin implementation** following tasks.md

### Notes

- All components are placeholders with minimal UI
- Backend endpoints echo received payloads (no AI processing)
- MDX integration uses Docusaurus 3.x standard approach
- Ready for immediate task generation (`/sp.tasks`)

