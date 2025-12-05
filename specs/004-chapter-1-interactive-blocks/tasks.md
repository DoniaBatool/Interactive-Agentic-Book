# Tasks: Chapter 1 — Interactive AI Blocks

**Feature**: 004-chapter-1-interactive-blocks | **Branch**: `004-chapter-1-interactive-blocks` | **Date**: 2025-12-05
**Generated From**: [plan.md](./plan.md) | [spec.md](./spec.md)

**Purpose**: Convert implementation plan into atomic, executable tasks for creating React components, MDX integration, and backend API endpoints (scaffolding only, no real AI logic).

---

## Task Format

```
- [ ] [TaskID] [Priority] [Story] Description with explicit file path
```

**Legend**:
- `TaskID`: Sequential identifier (T001, T002, etc.)
- `Priority`: P1 (Critical), P2 (Important), P3 (Nice-to-have)
- `Story`: US1 (User Story 1), US2 (User Story 2), US3 (User Story 3), SETUP (Initial setup), POLISH (Final touches)

---

## Phase 0: Setup & Prerequisites

**Purpose**: Verify dependencies and prepare folder structure before creating components.

- [X] [T001] [P1] [SETUP] Verify Chapter 1 MDX file exists at `frontend/docs/chapters/chapter-1.mdx` with 4 AI-BLOCK placeholder comments (`<!-- AI-BLOCK: ask-question -->`, `<!-- AI-BLOCK: explain-like-i-am-10 -->`, `<!-- AI-BLOCK: interactive-quiz -->`, `<!-- AI-BLOCK: generate-diagram -->`)
- [X] [T002] [P1] [SETUP] Create directory `frontend/src/components/ai/` if it doesn't exist
- [ ] [T003] [P1] [SETUP] Verify Docusaurus 3.x is installed and frontend builds successfully: Run `cd frontend && npm run build` to confirm no errors
- [ ] [T004] [P1] [SETUP] Verify FastAPI backend is functional: Run `cd backend && uvicorn app.main:app` to confirm server starts without errors

**Success Criteria**:
- Chapter 1 MDX file exists with AI-BLOCK comments
- `frontend/src/components/ai/` directory exists
- Frontend and backend both start without errors

**Dependencies**: Feature 001 (Base Project) and Feature 003 (Chapter 1 Content) must be complete

---

## Phase 1: Frontend Tasks - React Components (P1)

**User Story**: US1 - Learner Sees Interactive AI Blocks in Chapter 1

**Test Strategy**: Can be tested by creating components, configuring MDX mapping, and verifying components render in Chapter 1 page.

### Component Creation

- [X] [T005] [P1] [US1] Create `frontend/src/components/ai/AskQuestionBlock.tsx` with:
  - TypeScript interface `AskQuestionBlockProps { chapterId?: number; sectionId?: string; }`
  - Functional React component with minimal UI (textarea input, submit button, placeholder message area)
  - Event handler `handleSubmit` that logs to console: `console.log('AskQuestionBlock: Question submitted', { question, chapterId, sectionId })`
  - TODO comment: `// TODO: Call API endpoint POST /api/ai/ask-question`
  - Inline styles for minimal UI (border, padding, basic layout)

- [X] [T006] [P1] [US1] Create `frontend/src/components/ai/ExplainLike10Block.tsx` with:
  - TypeScript interface `ExplainLike10BlockProps { concept?: string; chapterId?: number; }`
  - Functional React component with minimal UI (concept display if provided, "Explain" button, explanation area with placeholder text)
  - Event handler `handleExplain` that logs to console: `console.log('ExplainLike10Block: Explanation requested', { concept, chapterId })`
  - TODO comment: `// TODO: Call API endpoint POST /api/ai/explain-like-10`
  - Inline styles for minimal UI

- [X] [T007] [P1] [US1] Create `frontend/src/components/ai/InteractiveQuizBlock.tsx` with:
  - TypeScript interface `InteractiveQuizBlockProps { chapterId?: number; numQuestions?: number; }`
  - Functional React component with minimal UI ("Start Quiz" button, quiz container placeholder, question/answer placeholders)
  - Event handler `handleStartQuiz` that logs to console: `console.log('InteractiveQuizBlock: Quiz started', { chapterId, numQuestions })`
  - TODO comment: `// TODO: Call API endpoint POST /api/ai/quiz`
  - Inline styles for minimal UI

- [X] [T008] [P1] [US1] Create `frontend/src/components/ai/GenerateDiagramBlock.tsx` with:
  - TypeScript interface `GenerateDiagramBlockProps { diagramType?: string; chapterId?: number; }`
  - Functional React component with minimal UI (diagram type display if provided, "Generate Diagram" button, diagram container placeholder)
  - Event handler `handleGenerate` that logs to console: `console.log('GenerateDiagramBlock: Diagram generation requested', { diagramType, chapterId })`
  - TODO comment: `// TODO: Call API endpoint POST /api/ai/diagram`
  - Inline styles for minimal UI

**Acceptance Test**: All 4 components compile without TypeScript errors: Run `cd frontend && npm run build` - should complete successfully

---

## Phase 2: Frontend Tasks - MDX Integration (P1)

**User Story**: US2 - Developer Verifies Component Integration

**Test Strategy**: Can be tested by configuring MDX mapping and verifying components render in Chapter 1.

### MDX Component Mapping

- [X] [T009] [P1] [US2] Create `frontend/src/mdx-components.ts` with:
  - Import statements for all 4 AI block components from `@site/src/components/ai/`
  - Export default object mapping component names: `{ AskQuestionBlock, ExplainLike10Block, InteractiveQuizBlock, GenerateDiagramBlock }`
  - If `mdx-components.ts` doesn't work with Docusaurus 3.x, document fallback: swizzle `@docusaurus/theme-classic/MDXComponents`

- [ ] [T010] [P1] [US2] Test MDX component mapping: Run `cd frontend && npm run build` to verify no compilation errors related to MDX components

**Alternative Approach (if T009 fails)**:
- [ ] [T010a] [P1] [US2] Swizzle MDXComponents: Run `npm run swizzle @docusaurus/theme-classic MDXComponents` to create `frontend/src/theme/MDXComponents.tsx`
- [ ] [T010b] [P1] [US2] Update `frontend/src/theme/MDXComponents.tsx` to import and include AI block components in the components object

**Acceptance Test**: MDX components file exists and exports all 4 components correctly

---

## Phase 3: Frontend Tasks - Chapter 1 MDX Update (P1)

**User Story**: US1 - Learner Sees Interactive AI Blocks

**Test Strategy**: Can be tested by updating Chapter 1 MDX and verifying components render in place of comments.

### Update Chapter 1 MDX File

- [X] [T011] [P1] [US1] Update `frontend/docs/chapters/chapter-1.mdx`:
  - Replace `<!-- AI-BLOCK: ask-question -->` (after Section 1) with: `<AskQuestionBlock chapterId={1} sectionId="what-is-physical-ai" />`
  - Replace `<!-- AI-BLOCK: generate-diagram -->` (after Section 2) with: `<GenerateDiagramBlock diagramType="robot-anatomy" chapterId={1} />`
  - Replace `<!-- AI-BLOCK: explain-like-i-am-10 -->` (in Section 3) with: `<ExplainLike10Block concept="autonomy" chapterId={1} />`
  - Replace `<!-- AI-BLOCK: interactive-quiz -->` (after Section 4) with: `<InteractiveQuizBlock chapterId={1} numQuestions={5} />`
  - Keep original AI-BLOCK comments as documentation (optional) or remove them

- [ ] [T012] [P1] [US1] Verify Chapter 1 MDX compiles: Run `cd frontend && npm run build` - should complete without errors

- [ ] [T013] [P1] [US1] Test component rendering: Run `cd frontend && npm start`, navigate to `/docs/chapters/chapter-1`, verify all 4 components render in their designated locations

**Acceptance Test**: All 4 AI block components render correctly in Chapter 1 page, no React errors in browser console

---

## Phase 4: Backend Tasks - API Endpoints (P2)

**User Story**: US3 - Backend Provides API Endpoint Scaffolding

**Test Strategy**: Can be tested by creating API endpoints and verifying they respond with placeholder JSON.

### Create API Router File

- [X] [T014] [P2] [US3] Create `backend/app/api/ai_blocks.py` with:
  - Import statements: `from fastapi import APIRouter, HTTPException`, `from pydantic import BaseModel`, `from typing import Optional, List`
  - Router setup: `router = APIRouter(prefix="/api/ai", tags=["ai-blocks"])`
  - Pydantic request models:
    - `AskQuestionRequest(BaseModel): question: str, chapterId: Optional[int] = None, sectionId: Optional[str] = None`
    - `ExplainLike10Request(BaseModel): concept: str, chapterId: Optional[int] = None`
    - `QuizRequest(BaseModel): chapterId: int, numQuestions: Optional[int] = 5`
    - `DiagramRequest(BaseModel): diagramType: str, chapterId: Optional[int] = None, concepts: Optional[List[str]] = []`
  - Pydantic response model: `AIBlockResponse(BaseModel): message: str, received: dict`

- [X] [T015] [P2] [US3] Add endpoint `POST /api/ai/ask-question` in `backend/app/api/ai_blocks.py`:
  - Route decorator: `@router.post("/ask-question", response_model=AIBlockResponse)`
  - Function signature: `async def ask_question(request: AskQuestionRequest) -> AIBlockResponse:`
  - Return placeholder response: `return AIBlockResponse(message="AI block placeholder", received=request.dict())`
  - TODO comment: `# TODO: Implement RAG pipeline, call OpenAI API, return real answer`

- [X] [T016] [P2] [US3] Add endpoint `POST /api/ai/explain-like-10` in `backend/app/api/ai_blocks.py`:
  - Route decorator: `@router.post("/explain-like-10", response_model=AIBlockResponse)`
  - Function signature: `async def explain_like_10(request: ExplainLike10Request) -> AIBlockResponse:`
  - Return placeholder response: `return AIBlockResponse(message="AI block placeholder", received=request.dict())`
  - TODO comment: `# TODO: Implement explanation generation using LLM with ELI10 prompt`

- [X] [T017] [P2] [US3] Add endpoint `POST /api/ai/quiz` in `backend/app/api/ai_blocks.py`:
  - Route decorator: `@router.post("/quiz", response_model=AIBlockResponse)`
  - Function signature: `async def quiz(request: QuizRequest) -> AIBlockResponse:`
  - Return placeholder response: `return AIBlockResponse(message="AI block placeholder", received=request.dict())`
  - TODO comment: `# TODO: Generate quiz questions from chapter learning objectives using LLM`

- [X] [T018] [P2] [US3] Add endpoint `POST /api/ai/diagram` in `backend/app/api/ai_blocks.py`:
  - Route decorator: `@router.post("/diagram", response_model=AIBlockResponse)`
  - Function signature: `async def diagram(request: DiagramRequest) -> AIBlockResponse:`
  - Return placeholder response: `return AIBlockResponse(message="AI block placeholder", received=request.dict())`
  - TODO comment: `# TODO: Generate diagram using OpenAI vision API or diagram generation library`

### Integrate Router in Main App

- [X] [T019] [P2] [US3] Update `backend/app/main.py`:
  - Add import: `from app.api import ai_blocks`
  - Include router: `app.include_router(ai_blocks.router)`
  - Verify no syntax errors: Run `python -m py_compile backend/app/main.py`

**Acceptance Test**: 
- Backend starts without errors: Run `cd backend && uvicorn app.main:app`
- All 4 endpoints respond: Test with `curl -X POST http://localhost:8000/api/ai/ask-question -H "Content-Type: application/json" -d '{"question": "test"}'` - should return `{"message": "AI block placeholder", "received": {...}}`

---

## Phase 5: Validation Tasks (P1)

**Purpose**: Verify all components, MDX integration, and API endpoints work correctly.

### Frontend Validation

- [ ] [T020] [P1] [POLISH] Run Docusaurus build: `cd frontend && npm run build` - verify no TypeScript compilation errors, no MDX parsing errors, build completes successfully

- [ ] [T021] [P1] [POLISH] Test component rendering in dev server: `cd frontend && npm start`, navigate to `/docs/chapters/chapter-1`, verify:
  - All 4 AI block components render in correct locations
  - No React errors in browser console
  - Components display minimal UI (input fields, buttons, placeholders)

- [ ] [T022] [P1] [POLISH] Test component interactions: Click buttons, submit forms in each AI block component, verify console.log output appears in browser console (no API calls should be made)

### Backend Validation

- [ ] [T023] [P1] [POLISH] Test all 4 API endpoints with curl or Postman:
  - `POST /api/ai/ask-question` with `{"question": "test", "chapterId": 1}`
  - `POST /api/ai/explain-like-10` with `{"concept": "autonomy", "chapterId": 1}`
  - `POST /api/ai/quiz` with `{"chapterId": 1, "numQuestions": 5}`
  - `POST /api/ai/diagram` with `{"diagramType": "robot-anatomy", "chapterId": 1}`
  - Verify all return: `{"message": "AI block placeholder", "received": {...}}`

- [X] [T024] [P1] [POLISH] Verify backend code quality: Check `backend/app/api/ai_blocks.py` for:
  - All endpoints have proper type hints
  - All endpoints have TODO comments for future implementation
  - No real AI logic (no OpenAI/Qdrant imports or calls)
  - Pydantic models properly defined

### Integration Validation

- [X] [T025] [P1] [POLISH] Verify no real AI logic exists: Search codebase for:
  - No `openai` API calls (except in placeholder comments)
  - No `qdrant` client calls (except in placeholder comments)
  - No embedding generation code
  - All handlers use console.log or return placeholder responses only

**Acceptance Test**: All validation tasks pass, ready for `/sp.implement` phase

---

## Phase 6: Documentation Tasks (P2)

**Purpose**: Document component usage and API contracts for future development.

- [X] [T026] [P2] [POLISH] Add JSDoc comments to each React component in `frontend/src/components/ai/`:
  - Component purpose
  - Props interface documentation
  - Usage example in MDX
  - TODO note for future AI integration

- [X] [T027] [P2] [POLISH] Add docstrings to backend API endpoints in `backend/app/api/ai_blocks.py`:
  - Endpoint purpose
  - Request/response schema documentation
  - Example request/response
  - TODO note for future RAG/AI integration

- [X] [T028] [P2] [POLISH] Create or update `frontend/src/components/ai/README.md` documenting:
  - Component list and purposes
  - How to use components in MDX
  - Props interface reference
  - Future enhancement roadmap

**Acceptance Test**: Documentation exists and is readable

---

## Task Summary

**Total Tasks**: 28 tasks
- **Phase 0 (Setup)**: 4 tasks
- **Phase 1 (Components)**: 4 tasks
- **Phase 2 (MDX Integration)**: 2 tasks (or 3 if swizzle needed)
- **Phase 3 (MDX Update)**: 3 tasks
- **Phase 4 (Backend API)**: 6 tasks
- **Phase 5 (Validation)**: 6 tasks
- **Phase 6 (Documentation)**: 3 tasks

**Critical Path**: T001 → T005-T008 → T009 → T011 → T014-T018 → T019 → T020-T025

**Estimated Time**: 2-3 hours (component creation + MDX integration + API endpoints + validation)

---

## Success Criteria Validation

### Spec Success Criteria → Task Mapping

| Success Criteria | Task IDs | Validation Method |
|------------------|----------|-------------------|
| **SC-001**: 4 components exist, TypeScript-compliant | T005-T008, T020 | `npm run build` in frontend |
| **SC-002**: MDX mapping file exists and maps all 4 components | T009, T010 | Manual review of `mdx-components.ts` |
| **SC-003**: Chapter 1 MDX renders all 4 components | T011, T012, T021 | Manual test: navigate to Chapter 1 |
| **SC-004**: Docusaurus build succeeds | T020 | `npm run build` completes |
| **SC-005**: 4 backend endpoints exist | T014-T018 | Manual review of `ai_blocks.py` |
| **SC-006**: Backend starts, endpoints accessible | T019, T023 | Start backend, test endpoints |
| **SC-007**: Components importable in MDX | T009, T010, T021 | Components render without React errors |
| **SC-008**: Event handlers log to console | T005-T008, T022 | Manual test: interact with components |
| **SC-009**: No real AI logic exists | T025 | Code review: search for AI imports/calls |

---

## Dependencies & Risks

### Internal Dependencies
- ✅ Feature 001 (Base Project) complete
- ✅ Feature 003 (Chapter 1 Content) complete - MDX file with AI-BLOCK comments exists

### External Dependencies
- ✅ React 18+, TypeScript, Docusaurus 3.x (from Feature 001)
- ✅ FastAPI 0.109+, Pydantic 2.x (from Feature 001)
- ✅ No new dependencies required

### Risks & Mitigations

**Risk 1**: MDX component mapping doesn't work in Docusaurus 3.x
- **Mitigation**: Task T010a-T010b provides swizzle fallback approach

**Risk 2**: Components break existing Chapter 1 rendering
- **Mitigation**: Task T012-T013 validate build and rendering incrementally

**Risk 3**: TypeScript compilation errors
- **Mitigation**: Task T020 validates build, fix types incrementally

---

**Task Generation Complete**: 2025-12-05
**Ready for Implementation**: Yes ✅
**Next Command**: `/sp.implement` (or manual task-by-task execution)

