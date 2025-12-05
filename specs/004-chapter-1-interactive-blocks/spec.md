# Feature Specification: Chapter 1 — Interactive AI Blocks

**Feature Branch**: `004-chapter-1-interactive-blocks`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "Implement the AI-interactive blocks that were added as placeholders in Chapter 1 content: ask-question, explain-like-i-am-10, interactive-quiz, generate-diagram. This feature provides the backend + frontend scaffolding to make these blocks functional without adding real AI logic yet."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learner Sees Interactive AI Blocks in Chapter 1 (Priority: P1)

As a learner reading Chapter 1, I want to see interactive AI block components rendered in place of the placeholder comments, so I can understand where future AI-powered features will appear and the UI is ready for integration.

**Why this priority**: This is the primary user-facing deliverable. Without visible components, learners cannot see where interactive features will be available. This establishes the UI foundation for future AI logic integration.

**Independent Test**: Can be fully tested by navigating to `/docs/chapters/chapter-1` in the Docusaurus frontend and verifying that all 4 AI block components render correctly in their designated locations, even if they only show placeholder UI.

**Acceptance Scenarios**:

1. **Given** the frontend is running, **When** I navigate to `/docs/chapters/chapter-1`, **Then** I see 4 interactive AI block components rendered where the `<!-- AI-BLOCK: ... -->` comments were placed
2. **Given** I am viewing the Ask Question block, **When** I see the component, **Then** it displays a minimal UI (e.g., input field, button) with placeholder styling
3. **Given** I am viewing the Explain Like I'm 10 block, **When** I see the component, **Then** it displays a minimal UI indicating where simplified explanations will appear
4. **Given** I am viewing the Interactive Quiz block, **When** I see the component, **Then** it displays a minimal UI structure for quiz questions and answers
5. **Given** I am viewing the Generate Diagram block, **When** I see the component, **Then** it displays a minimal UI for diagram generation interface
6. **Given** I interact with any AI block (click button, submit form), **When** the action triggers, **Then** I see console.log output indicating the handler was called (no real API calls yet)

---

### User Story 2 - Developer Verifies Component Integration (Priority: P1)

As a developer, I need to verify that MDX component mapping correctly loads AI block components, so I can ensure the integration between Docusaurus MDX and React components works properly.

**Why this priority**: Critical for ensuring the technical foundation is correct. Without proper MDX integration, components won't render at all, blocking all future development.

**Independent Test**: Can be fully tested by checking `frontend/src/mdx-components.ts` (or equivalent MDX configuration) and verifying that AI block components are mapped correctly, then running Docusaurus build to confirm no compilation errors.

**Acceptance Scenarios**:

1. **Given** the MDX components file exists, **When** I open `frontend/src/mdx-components.ts` (or `docusaurus.config.ts` MDX configuration), **Then** I see all 4 AI block components mapped to their respective names: `AskQuestionBlock`, `ExplainLike10Block`, `InteractiveQuizBlock`, `GenerateDiagramBlock`
2. **Given** the MDX file contains `<!-- AI-BLOCK: ask-question -->`, **When** Docusaurus processes the MDX, **Then** it renders `<AskQuestionBlock />` component in that location
3. **Given** I run `npm run build` in the frontend directory, **When** the build completes, **Then** there are no compilation errors related to AI block components
4. **Given** I run `npm start` in the frontend directory, **When** I navigate to Chapter 1, **Then** all components load without React errors in the browser console

---

### User Story 3 - Backend Provides API Endpoint Scaffolding (Priority: P2)

As a backend developer or future AI integration developer, I need placeholder API endpoints for each AI block, so I can verify the API contract and prepare for real AI logic implementation in future features.

**Why this priority**: Important for establishing API contracts early, but not critical for initial UI rendering. Backend endpoints can be added after frontend components are working.

**Independent Test**: Can be fully tested by starting the FastAPI backend, making POST requests to each endpoint, and verifying they return expected placeholder JSON responses.

**Acceptance Scenarios**:

1. **Given** the backend is running, **When** I make a POST request to `/api/ai/ask-question` with any JSON payload, **Then** I receive a response: `{"message": "AI block placeholder", "received": <payload>}`
2. **Given** the backend is running, **When** I make a POST request to `/api/ai/explain-like-10` with any JSON payload, **Then** I receive a response: `{"message": "AI block placeholder", "received": <payload>}`
3. **Given** the backend is running, **When** I make a POST request to `/api/ai/quiz` with any JSON payload, **Then** I receive a response: `{"message": "AI block placeholder", "received": <payload>}`
4. **Given** the backend is running, **When** I make a POST request to `/api/ai/diagram` with any JSON payload, **Then** I receive a response: `{"message": "AI block placeholder", "received": <payload>}`
5. **Given** I check the backend code, **When** I review `backend/app/api/ai_blocks.py`, **Then** I see all 4 endpoints defined with FastAPI route decorators but containing only placeholder logic (no real AI calls)

---

### Edge Cases

- What happens when an AI block component receives invalid props?
  - Components should handle missing or invalid props gracefully, using default values or showing an error message
- What happens when the backend API endpoint is called but the server is down?
  - Frontend components should handle API errors gracefully, showing user-friendly error messages (even if just console.log for now)
- What happens when MDX file has malformed AI-BLOCK comments?
  - Docusaurus should still compile successfully, but components may not render (acceptable for this scaffolding phase)
- What happens when multiple AI blocks of the same type appear on the same page?
  - Each component instance should work independently with its own state
- What happens when a user interacts with an AI block before backend is ready?
  - Components should handle API failures gracefully, showing placeholder messages or console warnings

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Frontend MUST have 4 React components created in `frontend/src/components/ai/` directory:
  - `AskQuestionBlock.tsx` - Component for asking questions about chapter content
  - `ExplainLike10Block.tsx` - Component for simplified explanations
  - `InteractiveQuizBlock.tsx` - Component for interactive quizzes
  - `GenerateDiagramBlock.tsx` - Component for diagram generation
- **FR-002**: Each AI block component MUST:
  - Accept props interface (even if minimal, e.g., `{ chapterId?: string, sectionId?: string }`)
  - Render minimal UI (input fields, buttons, containers as appropriate)
  - Include placeholder event handlers that log to console (no real API calls)
  - Be written in TypeScript with proper type definitions
  - Follow React best practices (functional components, hooks if needed)
- **FR-003**: MDX component mapping MUST be configured to load AI block components:
  - File location: `frontend/src/mdx-components.ts` (or equivalent Docusaurus MDX configuration)
  - Components mapped to names: `AskQuestionBlock`, `ExplainLike10Block`, `InteractiveQuizBlock`, `GenerateDiagramBlock`
  - Mapping allows components to be used directly in MDX: `<AskQuestionBlock />`
- **FR-004**: Chapter 1 MDX file MUST correctly reference AI block components:
  - Replace or supplement `<!-- AI-BLOCK: ask-question -->` with `<AskQuestionBlock />` (or keep comment and add component)
  - Replace or supplement `<!-- AI-BLOCK: explain-like-i-am-10 -->` with `<ExplainLike10Block />`
  - Replace or supplement `<!-- AI-BLOCK: interactive-quiz -->` with `<InteractiveQuizBlock />`
  - Replace or supplement `<!-- AI-BLOCK: generate-diagram -->` with `<GenerateDiagramBlock />`
- **FR-005**: Backend MUST have API endpoint file: `backend/app/api/ai_blocks.py`
- **FR-006**: Backend MUST define 4 placeholder endpoints:
  - `POST /api/ai/ask-question` - Accepts JSON payload, returns placeholder response
  - `POST /api/ai/explain-like-10` - Accepts JSON payload, returns placeholder response
  - `POST /api/ai/quiz` - Accepts JSON payload, returns placeholder response
  - `POST /api/ai/diagram` - Accepts JSON payload, returns placeholder response
- **FR-007**: Each backend endpoint MUST:
  - Use FastAPI route decorators with appropriate tags (e.g., `tags=["ai-blocks"]`)
  - Accept JSON request body (Pydantic model or dict)
  - Return JSON response: `{"message": "AI block placeholder", "received": <payload>}`
  - Include basic request validation (Pydantic schema)
  - Have no real AI logic (only placeholder/echo functionality)
- **FR-008**: Backend main.py MUST include the AI blocks router:
  - Import router from `app.api.ai_blocks`
  - Include router with prefix `/api/ai` (or appropriate prefix)
- **FR-009**: Frontend components MUST be importable and renderable:
  - No TypeScript compilation errors
  - No React runtime errors when components are used in MDX
  - Components export default or named exports correctly
- **FR-010**: Docusaurus build MUST complete successfully:
  - `npm run build` completes without errors
  - MDX files compile correctly with AI block components
  - No missing component errors

### Assumptions

- **Assumption 1**: Docusaurus 3.x supports MDX component mapping via `mdx-components.ts` or `docusaurus.config.ts` configuration
- **Assumption 2**: React 18+ is available in the frontend (already configured in base project)
- **Assumption 3**: TypeScript is configured for the frontend (already configured in base project)
- **Assumption 4**: FastAPI 0.109+ is available in the backend (already configured in base project)
- **Assumption 5**: Components will be styled with minimal CSS (inline styles or basic CSS modules acceptable for scaffolding)
- **Assumption 6**: No authentication is required for AI block endpoints in this phase (endpoints are public placeholders)
- **Assumption 7**: CORS is already configured in FastAPI backend to allow frontend requests (from base project setup)
- **Assumption 8**: Components can use console.log for placeholder handlers (no real API integration needed yet)
- **Assumption 9**: AI block components can be stateless or use React useState for minimal local state (no global state management needed)

### Key Entities

**AI Block Component**:
- Component name (e.g., "AskQuestionBlock")
- Props interface (chapterId, sectionId, etc.)
- UI structure (minimal)
- Event handlers (placeholder)

**AI Block API Endpoint**:
- Endpoint path (e.g., `/api/ai/ask-question`)
- HTTP method (POST)
- Request schema (Pydantic model)
- Response schema (JSON structure)
- Placeholder logic (echo received payload)

**MDX Component Mapping**:
- Component name (React component)
- MDX usage pattern (`<ComponentName />`)
- Import path (from `src/components/ai/`)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All 4 AI block components exist in `frontend/src/components/ai/` directory and are TypeScript-compliant (no compilation errors)
- **SC-002**: MDX component mapping file exists and correctly maps all 4 AI block components
- **SC-003**: Chapter 1 MDX file renders all 4 AI block components in their designated locations without errors
- **SC-004**: Docusaurus build completes successfully (`npm run build` in frontend) with no errors related to AI blocks
- **SC-005**: All 4 backend API endpoints exist in `backend/app/api/ai_blocks.py` and respond to POST requests with placeholder JSON
- **SC-006**: Backend starts without errors and all 4 endpoints are accessible (verified via curl or Postman)
- **SC-007**: Frontend components can be imported and used in MDX without React runtime errors
- **SC-008**: Component event handlers log to console when triggered (verifying placeholder functionality works)
- **SC-009**: No real AI logic exists in either frontend or backend (only scaffolding/placeholders)

## Scope Boundaries *(mandatory)*

### In Scope

- Creating 4 React TypeScript components with minimal UI
- Configuring MDX component mapping for Docusaurus
- Updating Chapter 1 MDX to use AI block components
- Creating 4 FastAPI placeholder endpoints
- Basic request/response schemas (Pydantic models)
- Console.log placeholder handlers in frontend components
- Echo/placeholder logic in backend endpoints
- TypeScript type definitions for components and API contracts
- Basic component styling (minimal, functional UI)

### Out of Scope

- Real AI logic implementation (OpenAI API calls, LLM integration)
- RAG pipeline integration
- User authentication for AI blocks
- Persistent storage of user interactions
- Real diagram generation
- Real quiz question generation
- Real question answering
- Real simplified explanation generation
- Advanced error handling beyond basic try-catch
- Loading states and spinners (can be added but not required)
- Response streaming
- WebSocket connections
- Rate limiting for AI endpoints
- Cost tracking or usage analytics
- User preference storage
- Personalization based on user profile
- Translation of AI block UI
- Advanced styling or animations
- Accessibility features beyond basic HTML semantics
- Unit tests (will be added in future features per TDD mandate)
- Integration tests with real AI services

### Dependencies

- Docusaurus 3.x frontend (from base project)
- React 18+ (from base project)
- TypeScript (from base project)
- FastAPI 0.109+ backend (from base project)
- Chapter 1 MDX file exists with AI-BLOCK placeholder comments (from 003-chapter-1-content feature)
- Frontend build system (npm/pnpm) configured
- Backend Python environment configured

### Constraints

- Must follow Constitution Principle II (Docusaurus-First) - components must work within Docusaurus MDX
- Must follow Constitution Principle I (SDD) - no code without spec/plan/tasks
- Must prepare for future AI integration (Principle III - RAG-First) but not implement it yet
- Components must be framework-agnostic where possible (React is acceptable as Docusaurus requirement)
- No secrets or API keys in code (all future AI keys will be in environment variables)
- All placeholder code must include TODO comments indicating future implementation
- Components must not break existing Chapter 1 content rendering

## Non-Goals *(mandatory)*

- Implementing real AI functionality (OpenAI, RAG, embeddings)
- Creating production-ready UI/UX (minimal scaffolding is sufficient)
- Adding authentication/authorization to AI block endpoints
- Implementing data persistence for user interactions
- Creating comprehensive error handling
- Adding loading states, animations, or advanced styling
- Implementing real diagram generation algorithms
- Creating real quiz question banks
- Implementing real question-answering logic
- Adding user analytics or tracking
- Creating admin dashboards for AI block management
- Implementing caching for AI responses
- Adding rate limiting or usage quotas
- Creating comprehensive test suites (TDD will be applied in future features)

