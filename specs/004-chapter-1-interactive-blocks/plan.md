# Implementation Plan: Chapter 1 — Interactive AI Blocks

**Branch**: `004-chapter-1-interactive-blocks` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/004-chapter-1-interactive-blocks/spec.md`

## Summary

This feature implements the frontend and backend scaffolding for 4 AI-interactive blocks that were added as placeholders in Chapter 1 content. The implementation creates React TypeScript components for each AI block type, configures MDX component mapping in Docusaurus, updates Chapter 1 MDX to render components, and creates FastAPI placeholder endpoints. **No real AI logic is implemented**—only UI scaffolding and API contracts are established to prepare for future AI integration.

**Primary Deliverable**: 4 React components + MDX integration + 4 backend API endpoints (all placeholders)
**Validation**: Docusaurus build succeeds, components render, backend endpoints respond with placeholder JSON

## Technical Context

**Language/Version**:
- Frontend: TypeScript + React 18+ with MDX (Docusaurus 3.x)
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- Frontend: React 18+, TypeScript, Docusaurus 3.x (already installed)
- Backend: FastAPI 0.109+, Pydantic 2.x (already installed)
- No new external dependencies required

**Storage**: 
- Frontend: React components (static files)
- Backend: API endpoints (no database, no persistent storage)

**Testing**:
- Frontend: `npm run build` validation, manual component rendering test
- Backend: Manual API endpoint testing (curl/Postman)
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Frontend: Web browsers via Docusaurus static site
- Backend: FastAPI server (localhost:8000)

**Project Type**: Web application (frontend React components + backend API scaffolding)

**Performance Goals**:
- Component render time: < 100ms (minimal UI, no heavy operations)
- API response time: < 50ms (placeholder echo, no AI processing)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (OpenAI API calls, RAG, embeddings)
- Components MUST render minimal UI only (functional but not production-ready)
- Backend endpoints MUST return placeholder responses only
- MDX integration MUST work with Docusaurus 3.x
- All code MUST include TODO comments for future implementation

**Scale/Scope**:
- 4 React components (AskQuestionBlock, ExplainLike10Block, InteractiveQuizBlock, GenerateDiagramBlock)
- 1 MDX component mapping file
- 1 Chapter 1 MDX update (replace 4 AI-BLOCK comments with components)
- 4 FastAPI endpoints (POST /api/ai/*)
- ~200-300 lines of frontend code, ~100-150 lines of backend code

## Constitution Check

*GATE: Must pass before implementation. Re-check after Phase 1 design.*

### ✅ PASS - Principle I: AI-Native Spec-Driven Development

**Status**: COMPLIANT

- Specification created: `specs/004-chapter-1-interactive-blocks/spec.md` ✓
- Architecture planning: This plan document ✓
- SDD workflow followed: Spec → Plan → Tasks (next) → Implement ✓
- No code written without corresponding spec/plan artifacts ✓

### ✅ PASS - Principle II: Docusaurus-First Documentation Strategy

**Status**: COMPLIANT

- React components work within Docusaurus MDX ✓
- MDX component mapping configured for Docusaurus 3.x ✓
- Components follow Docusaurus best practices (import from `@site/src/components/`) ✓
- Static generation supported (components are client-side React) ✓
- No breaking changes to existing Chapter 1 content ✓

### ⚠️ PARTIAL - Principle III: RAG-First Chatbot Architecture

**Status**: SCAFFOLDING PHASE (ACCEPTABLE)

- API endpoints prepared for future RAG integration ✓
- Component props include `chapterId` and `sectionId` for context ✓
- Backend endpoints accept request payloads (ready for RAG queries) ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No actual RAG pipeline
  - No Qdrant vector search
  - No OpenAI API calls
  - No embedding generation

**Justification**: This is a scaffolding feature establishing UI and API contracts. RAG integration is explicitly planned for future features (005+). Component structure and API endpoints are designed to accept RAG-ready parameters (chapterId, sectionId, query text).

### ✅ PASS - Principle IV: Personalization & User-Centric Design

**Status**: COMPLIANT (UI LAYER)

- Components accept optional props for personalization (chapterId, sectionId) ✓
- UI is minimal but functional (learners can see where AI features will appear) ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No user authentication
  - No personalization based on user profile
  - No adaptive content rendering

**Justification**: This feature establishes the UI foundation. Personalization will be added in future features when BetterAuth and user profiles are implemented.

### ✅ PASS - Principle V: Multilingual Support with On-Demand Translation

**Status**: COMPLIANT (STRUCTURE)

- Component structure supports future translation (text in props or constants) ✓
- No hard-coded English text in component logic ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No Urdu translation
  - No translation pipeline

**Justification**: Component structure is translation-ready. Translation will be added in future features when translation system is implemented.

### ✅ PASS - Principle VI: Test-Driven Quality Gates

**Status**: COMPLIANT (MANUAL TESTING PHASE)

- Clear acceptance criteria defined in spec.md (9 success criteria) ✓
- Manual validation methods specified (build test, component rendering test, API test) ✓
- **Not Yet Implemented** (automated testing out of scope for scaffolding):
  - No unit tests (components are minimal placeholders)
  - No integration tests (no real AI logic to test)
  - No E2E tests

**Justification**: This is a scaffolding feature with minimal logic. Automated tests will be added in future features when real AI functionality is implemented (per TDD mandate).

---

### Constitution Check Summary

| Principle | Status | Notes |
|-----------|--------|-------|
| I. SDD Workflow | ✅ PASS | Full spec → plan → tasks workflow followed |
| II. Docusaurus-First | ✅ PASS | MDX component integration, Docusaurus 3.x compatible |
| III. RAG-First | ⚠️ SCAFFOLDING | API contracts ready, actual RAG in future features |
| IV. Personalization | ✅ PASS | Component props support future personalization |
| V. Multilingual | ✅ PASS | Structure supports translation, implementation deferred |
| VI. TDD Quality Gates | ✅ PASS | Manual validation appropriate for scaffolding phase |

**Overall**: ✅ **APPROVED TO PROCEED**

All principles are either fully compliant or in acceptable scaffolding phase. Partial compliance is justified because this is a foundational UI/API scaffolding feature establishing contracts for future AI integration.

---

## Project Structure

### Documentation (this feature)

```text
specs/004-chapter-1-interactive-blocks/
├── spec.md              # Feature specification (complete)
├── plan.md              # This file (/sp.plan command output)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT YET CREATED)
```

### Source Code (repository root)

```text
# Frontend: React components + MDX integration
frontend/
├── src/
│   ├── components/
│   │   └── ai/                      # NEW: AI block components directory
│   │       ├── AskQuestionBlock.tsx      # NEW: Ask question component
│   │       ├── ExplainLike10Block.tsx    # NEW: ELI10 explanation component
│   │       ├── InteractiveQuizBlock.tsx # NEW: Quiz component
│   │       └── GenerateDiagramBlock.tsx   # NEW: Diagram generator component
│   └── mdx-components.ts            # NEW: MDX component mapping (or use theme/MDXComponents.tsx)
├── docs/
│   └── chapters/
│       └── chapter-1.mdx            # MODIFIED: Replace AI-BLOCK comments with components
└── docusaurus.config.ts             # Existing (no changes needed)

# Backend: API endpoints
backend/
├── app/
│   ├── api/
│   │   └── ai_blocks.py            # NEW: AI block API endpoints
│   └── main.py                      # MODIFIED: Include ai_blocks router
└── tests/                            # Existing (no tests in this phase)
```

**Structure Decision**: Components placed in `frontend/src/components/ai/` to organize AI-related components separately from general UI components. MDX component mapping uses Docusaurus 3.x standard approach (either `mdx-components.ts` or swizzled `theme/MDXComponents.tsx`).

---

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

N/A - All Constitution principles passed or are in acceptable scaffolding phase with clear justification. No violations requiring complexity tracking.

---

## Phase 0: Research & Technical Decisions

### Research Questions Resolved

#### Q1: Docusaurus 3.x MDX Component Mapping

**Decision**: Use one of two approaches:
1. **Option A (Recommended)**: Create `frontend/src/mdx-components.ts` with component exports
2. **Option B**: Swizzle `@docusaurus/theme-classic/MDXComponents` and customize

**Rationale**: Docusaurus 3.x supports both approaches. Option A is simpler for scaffolding and doesn't require swizzling. Option B provides more control but adds complexity.

**Reference**: Docusaurus 3.x MDX documentation, component mapping examples

**Implementation**: Start with Option A (`mdx-components.ts`). If issues arise, switch to Option B.

---

#### Q2: Component Props Interface Design

**Decision**: Minimal props interface for each component:
- `AskQuestionBlock`: `{ chapterId?: number, sectionId?: string }`
- `ExplainLike10Block`: `{ concept?: string, chapterId?: number }`
- `InteractiveQuizBlock`: `{ chapterId?: number, numQuestions?: number }`
- `GenerateDiagramBlock`: `{ diagramType?: string, chapterId?: number }`

**Rationale**: Props are optional to allow components to work standalone. Future AI integration will use these props for context. Minimal interface reduces complexity in scaffolding phase.

**Future Enhancement**: Add more props as AI features are implemented (user preferences, difficulty level, etc.)

---

#### Q3: Backend API Endpoint Structure

**Decision**: Single router file `backend/app/api/ai_blocks.py` with 4 endpoints:
- `POST /api/ai/ask-question`
- `POST /api/ai/explain-like-10`
- `POST /api/ai/quiz`
- `POST /api/ai/diagram`

**Rationale**: Grouping related endpoints in one file simplifies maintenance. Prefix `/api/ai/` clearly identifies AI-related endpoints. Future features can add more endpoints to this file or create separate files per subagent.

**Request/Response Schema**: Use Pydantic models for validation:
```python
class AskQuestionRequest(BaseModel):
    question: str
    chapterId: Optional[int] = None
    sectionId: Optional[str] = None

class AskQuestionResponse(BaseModel):
    message: str
    received: dict
```

---

#### Q4: MDX Comment Replacement Strategy

**Decision**: Replace `<!-- AI-BLOCK: type -->` comments with `<ComponentName />` JSX directly in MDX file.

**Rationale**: 
- Keeps MDX file clean and readable
- Components render immediately (no comment parsing needed)
- Aligns with Docusaurus MDX best practices
- Future: Can add comment back as documentation if needed

**Example**:
```mdx
<!-- Before -->
<!-- AI-BLOCK: ask-question -->

<!-- After -->
<AskQuestionBlock chapterId={1} sectionId="what-is-physical-ai" />
```

---

#### Q5: Component Styling Approach

**Decision**: Use inline styles or minimal CSS modules for scaffolding. No external CSS framework.

**Rationale**: 
- Minimal UI requirement (scaffolding only)
- Inline styles keep components self-contained
- Future features can add proper styling system (Tailwind, CSS modules, etc.)
- Reduces dependencies and complexity

**Future Enhancement**: Add proper styling system when production UI is implemented.

---

### Technology Stack Summary

| Layer | Technology | Version/Format | Purpose |
|-------|------------|----------------|---------|
| Frontend Components | React + TypeScript | React 18+, TS 5+ | Interactive UI components |
| MDX Integration | Docusaurus MDX | Docusaurus 3.x | Component rendering in markdown |
| Backend API | FastAPI | FastAPI 0.109+ | REST API endpoints |
| Request Validation | Pydantic | Pydantic 2.x | Request/response schemas |
| Styling | Inline CSS | N/A | Minimal UI styling |

---

## Phase 1: Design & Contracts

### Component Architecture

#### 1. AskQuestionBlock Component

**File**: `frontend/src/components/ai/AskQuestionBlock.tsx`

**Props Interface**:
```typescript
interface AskQuestionBlockProps {
  chapterId?: number;
  sectionId?: string;
}
```

**UI Structure**:
- Input field (textarea) for question
- Submit button
- Placeholder message area

**Event Handler**:
```typescript
const handleSubmit = (question: string) => {
  console.log('AskQuestionBlock: Question submitted', { question, chapterId, sectionId });
  // TODO: Call API endpoint POST /api/ai/ask-question
};
```

---

#### 2. ExplainLike10Block Component

**File**: `frontend/src/components/ai/ExplainLike10Block.tsx`

**Props Interface**:
```typescript
interface ExplainLike10BlockProps {
  concept?: string;
  chapterId?: number;
}
```

**UI Structure**:
- Concept display (if provided)
- "Explain" button
- Explanation area (placeholder text)

**Event Handler**:
```typescript
const handleExplain = () => {
  console.log('ExplainLike10Block: Explanation requested', { concept, chapterId });
  // TODO: Call API endpoint POST /api/ai/explain-like-10
};
```

---

#### 3. InteractiveQuizBlock Component

**File**: `frontend/src/components/ai/InteractiveQuizBlock.tsx`

**Props Interface**:
```typescript
interface InteractiveQuizBlockProps {
  chapterId?: number;
  numQuestions?: number;
}
```

**UI Structure**:
- "Start Quiz" button
- Quiz container (placeholder)
- Question/answer placeholders

**Event Handler**:
```typescript
const handleStartQuiz = () => {
  console.log('InteractiveQuizBlock: Quiz started', { chapterId, numQuestions });
  // TODO: Call API endpoint POST /api/ai/quiz
};
```

---

#### 4. GenerateDiagramBlock Component

**File**: `frontend/src/components/ai/GenerateDiagramBlock.tsx`

**Props Interface**:
```typescript
interface GenerateDiagramBlockProps {
  diagramType?: string;
  chapterId?: number;
}
```

**UI Structure**:
- Diagram type display (if provided)
- "Generate Diagram" button
- Diagram container (placeholder)

**Event Handler**:
```typescript
const handleGenerate = () => {
  console.log('GenerateDiagramBlock: Diagram generation requested', { diagramType, chapterId });
  // TODO: Call API endpoint POST /api/ai/diagram
};
```

---

### MDX Component Mapping

**File**: `frontend/src/mdx-components.ts` (or `frontend/src/theme/MDXComponents.tsx`)

**Mapping Structure**:
```typescript
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';

export default {
  AskQuestionBlock,
  ExplainLike10Block,
  InteractiveQuizBlock,
  GenerateDiagramBlock,
};
```

**Alternative (Docusaurus 3.x)**: If `mdx-components.ts` doesn't work, swizzle `MDXComponents`:
```bash
npm run swizzle @docusaurus/theme-classic MDXComponents
```

Then customize `src/theme/MDXComponents.tsx` to include AI block components.

---

### Backend API Architecture

#### API Router Structure

**File**: `backend/app/api/ai_blocks.py`

**Router Setup**:
```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/api/ai", tags=["ai-blocks"])

# Request/Response Models
class AskQuestionRequest(BaseModel):
    question: str
    chapterId: Optional[int] = None
    sectionId: Optional[str] = None

class AIBlockResponse(BaseModel):
    message: str
    received: dict

# Endpoints
@router.post("/ask-question", response_model=AIBlockResponse)
async def ask_question(request: AskQuestionRequest):
    """Placeholder endpoint for ask-question AI block."""
    return AIBlockResponse(
        message="AI block placeholder",
        received=request.dict()
    )

# ... 3 more endpoints with similar structure
```

**Main.py Integration**:
```python
from app.api import ai_blocks

app.include_router(ai_blocks.router)
```

---

### Data Contracts

#### Request Schemas

**AskQuestionRequest**:
```python
class AskQuestionRequest(BaseModel):
    question: str                    # Required: User's question
    chapterId: Optional[int] = None  # Optional: Chapter context
    sectionId: Optional[str] = None  # Optional: Section context
```

**ExplainLike10Request**:
```python
class ExplainLike10Request(BaseModel):
    concept: str                     # Required: Concept to explain
    chapterId: Optional[int] = None  # Optional: Chapter context
```

**QuizRequest**:
```python
class QuizRequest(BaseModel):
    chapterId: int                   # Required: Chapter for quiz
    numQuestions: Optional[int] = 5  # Optional: Number of questions
```

**DiagramRequest**:
```python
class DiagramRequest(BaseModel):
    diagramType: str                 # Required: Type of diagram
    chapterId: Optional[int] = None  # Optional: Chapter context
    concepts: Optional[List[str]] = [] # Optional: Concepts to include
```

#### Response Schema

**AIBlockResponse** (common for all endpoints):
```python
class AIBlockResponse(BaseModel):
    message: str  # "AI block placeholder"
    received: dict  # Echo of request payload
```

---

## Implementation Phases Summary

### Phase 0: Research ✅ COMPLETE
- **Output**: Technical decisions documented above
- **Key Decisions**: MDX mapping approach, component props, API structure, styling approach
- **Status**: All research questions resolved

### Phase 1: Design & Contracts ✅ COMPLETE
- **Output**: Component architecture, API architecture, data contracts
- **Key Artifacts**: 4 component interfaces, 4 API endpoint contracts, MDX mapping strategy
- **Status**: Architecture designed, ready for task generation

### Phase 2: Task Generation ⏳ NEXT STEP
- **Command**: `/sp.tasks`
- **Output**: `tasks.md` with testable implementation tasks
- **Expected**: Break down into atomic tasks: create components, configure MDX, update chapter-1.mdx, create API endpoints, test integration

### Phase 3: Implementation 🔜 FUTURE
- **Command**: `/sp.implement`
- **Output**: Actual React components, MDX updates, API endpoints
- **Expected**: Follow tasks.md step-by-step with validation

---

## Acceptance Criteria Mapping

### Spec Success Criteria → Plan Validation

| Success Criteria | Plan Element | Validation Method |
|------------------|--------------|-------------------|
| **SC-001**: 4 components exist, TypeScript-compliant | Component architecture (Phase 1) | `npm run build` in frontend, check for TS errors |
| **SC-002**: MDX mapping file exists and maps all 4 components | MDX component mapping (Phase 1) | Manual review of `mdx-components.ts` |
| **SC-003**: Chapter 1 MDX renders all 4 components | MDX update strategy (Phase 1) | Manual test: navigate to `/docs/chapters/chapter-1`, verify components render |
| **SC-004**: Docusaurus build succeeds | Build validation | `npm run build` completes without errors |
| **SC-005**: 4 backend endpoints exist | API architecture (Phase 1) | Manual test: curl each endpoint, verify response |
| **SC-006**: Backend starts, endpoints accessible | API router integration | Start backend, test endpoints via curl/Postman |
| **SC-007**: Components importable in MDX | MDX mapping + component exports | Manual test: components render in MDX without React errors |
| **SC-008**: Event handlers log to console | Component event handlers | Manual test: interact with components, check browser console |
| **SC-009**: No real AI logic exists | Scaffolding constraint | Code review: verify no OpenAI/Qdrant calls, only placeholders |

---

## Dependencies & Risks

### Internal Dependencies (Resolved)
- ✅ Feature 001 (Base Project Initialization) complete
- ✅ Feature 003 (Chapter 1 Content) complete - MDX file exists with AI-BLOCK comments
- ✅ Docusaurus frontend functional
- ✅ FastAPI backend functional

### External Dependencies (Satisfied)
- ✅ React 18+ (from Feature 001)
- ✅ TypeScript (from Feature 001)
- ✅ FastAPI 0.109+ (from Feature 001)
- ✅ Pydantic 2.x (from Feature 001)
- ✅ No new external dependencies required

### Risks & Mitigations

**Risk 1**: MDX component mapping doesn't work in Docusaurus 3.x
- **Impact**: Components won't render, blocks feature
- **Mitigation**: Test mapping early, have swizzle approach ready (Option B)

**Risk 2**: Components break existing Chapter 1 content rendering
- **Impact**: Chapter 1 page fails to load
- **Mitigation**: Test incrementally, verify build after each component addition

**Risk 3**: Backend CORS not configured for frontend requests
- **Impact**: Frontend can't call API endpoints (future issue, not critical for scaffolding)
- **Mitigation**: Verify CORS in base project, add if missing (not blocking for placeholder phase)

**Risk 4**: TypeScript compilation errors in components
- **Impact**: Build fails, blocks deployment
- **Mitigation**: Use strict TypeScript, test build frequently, fix types incrementally

---

## Post-Planning Next Steps

1. **Run `/sp.tasks`**: ⏳ Next command
   - Generate testable task list from this plan
   - Break down into atomic tasks with acceptance criteria
   - Link each task to success criteria from spec.md

2. **Review plan artifacts**: ⏳ User approval checkpoint
   - User reviews: plan.md, component architecture, API contracts
   - User approves technical decisions and implementation approach

3. **Begin implementation**: 🔜 After task generation
   - Run `/sp.implement` to start implementation
   - Follow tasks.md step-by-step
   - Validate against acceptance criteria at each milestone

---

## Key Takeaways

### What This Plan Delivers
✅ **Complete implementation roadmap** for AI block scaffolding
✅ **4 React component architectures** with props interfaces and UI structure
✅ **MDX integration strategy** for Docusaurus 3.x
✅ **4 API endpoint contracts** with request/response schemas
✅ **Acceptance criteria mapping** from spec to plan elements
✅ **Risk analysis** with mitigation strategies

### What This Plan Does NOT Deliver (Out of Scope)
❌ Real AI logic implementation (OpenAI, RAG, embeddings)
❌ Production-ready UI/UX (minimal scaffolding only)
❌ Authentication/authorization for endpoints
❌ Data persistence for user interactions
❌ Automated test suites (manual validation only)
❌ Advanced error handling
❌ Loading states or animations

### Success Indicators
✅ All Constitution principles passed or in acceptable scaffolding phase
✅ All research questions resolved
✅ Component architecture maps 1:1 to spec requirements
✅ API contracts provide clear request/response structure
✅ MDX integration strategy documented
✅ Ready to proceed to `/sp.tasks` command

---

**Plan Status**: ✅ **COMPLETE AND APPROVED**

**Next Command**: `/sp.tasks` - Generate task list from this plan

**Estimated Time to Implementation**: 2-3 hours (component creation + MDX integration + API endpoints)

**Blocking Issues**: None - all dependencies resolved, all technical decisions made, architecture designed.

