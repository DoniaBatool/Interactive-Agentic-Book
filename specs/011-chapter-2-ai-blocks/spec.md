# Feature Specification: Chapter 2 — AI Blocks Integration (ROS 2 Fundamentals)

**Feature Branch**: `011-chapter-2-ai-blocks`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "Enable all four AI-Interactive Blocks (Ask Question, Explain Like I Am 10, Generate Diagram, Interactive Quiz) for Chapter 2 using the existing Runtime Engine, RAG pipeline, subagents, and skills. This feature extends Chapter 2 content with AI-driven functionality without creating new logic."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learner Sees Interactive AI Blocks in Chapter 2 (Priority: P1)

As a learner reading Chapter 2, I want to see interactive AI block components rendered in place of the placeholder comments, so I can interact with AI-powered features for ROS 2 concepts and the UI is ready for integration.

**Why this priority**: This is the primary user-facing deliverable. Without visible components, learners cannot see where interactive features will be available. This establishes the UI foundation for future AI logic integration specific to ROS 2 content.

**Independent Test**: Can be fully tested by navigating to `/docs/chapters/chapter-2` in the Docusaurus frontend and verifying that all 4 AI block components render correctly in their designated locations, even if they only show placeholder UI.

**Acceptance Scenarios**:

1. **Given** the frontend is running, **When** I navigate to `/docs/chapters/chapter-2`, **Then** I see 4 interactive AI block components rendered where the `<!-- AI-BLOCK: ... -->` comments were placed
2. **Given** I am viewing the Ask Question block (after "Introduction to ROS 2" section), **When** I see the component, **Then** it displays a minimal UI with chapterId={2} and sectionId="introduction-to-ros2"
3. **Given** I am viewing the Generate Diagram block (after "Nodes and Node Communication" section), **When** I see the component, **Then** it displays a minimal UI with diagramType="node-communication-architecture" and chapterId={2}
4. **Given** I am viewing the Explain Like I'm 10 block (inside "Topics and Messages" section), **When** I see the component, **Then** it displays a minimal UI with concept="topics" and chapterId={2}
5. **Given** I am viewing the Interactive Quiz block (after "Services and Actions" section), **When** I see the component, **Then** it displays a minimal UI with chapterId={2} and numQuestions={5}
6. **Given** I interact with any AI block (click button, submit form), **When** the action triggers, **Then** I see console.log output indicating the handler was called with Chapter 2 context (no real API calls yet)

---

### User Story 2 - Backend Provides Chapter 2 Runtime Scaffolding (Priority: P2)

As a backend developer or future AI integration developer, I need placeholder scaffolding for Chapter 2 AI blocks in the runtime engine, RAG pipeline, and subagents, so I can verify the integration flow and prepare for real AI logic implementation.

**Why this priority**: Important for establishing backend integration patterns for Chapter 2, but not critical for initial UI rendering. Backend scaffolding can be added after frontend components are working.

**Independent Test**: Can be fully tested by checking that Chapter 2 mappings exist in runtime engine, chapter_2_chunks.py exists with placeholder function, and subagents have TODO sections for Chapter 2.

**Acceptance Scenarios**:

1. **Given** I check the runtime engine, **When** I review `backend/app/ai/runtime/engine.py`, **Then** I see mapping for Chapter 2 knowledge source with TODO comments explaining RAG pipeline integration
2. **Given** I check the chapter chunks file, **When** I review `backend/app/content/chapters/chapter_2_chunks.py`, **Then** I see placeholder function `get_chapter_chunks()` with TODO comments (no real implementation)
3. **Given** I check the API routing, **When** I review `backend/app/api/ai_blocks.py`, **Then** I see that chapterId=2 flows correctly to runtime engine
4. **Given** I check each subagent, **When** I review `backend/app/ai/subagents/*.py`, **Then** I see TODO sections explaining how Chapter 2 will interact with expected inputs/outputs for ROS 2 concepts
5. **Given** the backend is running, **When** I make a POST request to any AI block endpoint with chapterId=2, **Then** I receive a response indicating Chapter 2 context was received

---

### Edge Cases

- What happens when an AI block component receives invalid props for Chapter 2?
  - Components should handle missing or invalid props gracefully, using default values or showing an error message
- What happens when the backend API endpoint is called with chapterId=2 but Chapter 2 chunks don't exist?
  - Backend should handle gracefully, returning placeholder response or error message indicating chunks not yet implemented
- What happens when MDX file has malformed AI-BLOCK comments for Chapter 2?
  - Docusaurus should still compile successfully, but components may not render (acceptable for this scaffolding phase)
- What happens when multiple AI blocks of the same type appear on the same Chapter 2 page?
  - Each component instance should work independently with its own state and Chapter 2 context
- What happens when a user interacts with a Chapter 2 AI block before backend is ready?
  - Components should handle API failures gracefully, showing placeholder messages or console warnings

## Requirements *(mandatory)*

### Functional Requirements

#### Frontend MDX Updates

- **FR-001**: System MUST modify `frontend/docs/chapters/chapter-2.mdx` to replace HTML comment placeholders with React component calls
- **FR-002**: System MUST insert 4 AI Blocks exactly at pedagogically correct positions:
  - `ask-question` block after "Introduction to ROS 2" section (sectionId="introduction-to-ros2")
  - `explain-like-i-am-10` block inside "Topics and Messages" section (concept="topics")
  - `interactive-quiz` block after "Services and Actions" section
  - `generate-diagram` block after "Nodes and Node Communication" section (diagramType="node-communication-architecture")
- **FR-003**: System MUST replace placeholder comments with component calls:
  - `<!-- AI-BLOCK: ask-question -->` → `<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />`
  - `<!-- AI-BLOCK: explain-like-i-am-10 -->` → `<ExplainLike10Block concept="topics" chapterId={2} />`
  - `<!-- AI-BLOCK: interactive-quiz -->` → `<InteractiveQuizBlock chapterId={2} numQuestions={5} />`
  - `<!-- AI-BLOCK: generate-diagram -->` → `<GenerateDiagramBlock diagramType="node-communication-architecture" chapterId={2} />`
- **FR-004**: System MUST add import statements at top of chapter-2.mdx:
  - `import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';`
  - `import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';`
  - `import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';`
  - `import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';`
- **FR-005**: Docusaurus build MUST succeed with Chapter 2 blocks:
  - `npm run build` completes without errors
  - MDX file compiles correctly with AI block components
  - No missing component errors

#### Backend Integration

- **FR-006**: System MUST create `backend/app/content/chapters/chapter_2_chunks.py` with:
  - Placeholder function `get_chapter_chunks()` that returns empty list or placeholder data
  - TODO comments explaining logic to split Chapter 2 text into chunks (no real implementation)
  - Function signature: `def get_chapter_chunks() -> List[Dict[str, Any]]:`
- **FR-007**: System MUST update `backend/app/api/ai_blocks.py` routing:
  - Ensure chapterId=2 flows correctly to runtime engine
  - Add comments indicating Chapter 2 support (no logic changes needed if routing is generic)
- **FR-008**: Backend MUST start cleanly:
  - No import errors when starting FastAPI server
  - All imports resolve correctly
  - No syntax errors in new files

#### Runtime Engine Mapping

- **FR-009**: System MUST update `backend/app/ai/runtime/engine.py`:
  - Add mapping for Chapter 2 knowledge source
  - Add comments explaining how RAG pipeline will retrieve Chapter 2 chunks
  - Add TODO comments for Chapter 2 integration (no real implementation, only scaffold flow)
- **FR-010**: Runtime engine mapping MUST include:
  - Knowledge source identifier for Chapter 2 (e.g., "chapter_2" or chapter_id=2)
  - Comment explaining RAG pipeline integration for Chapter 2
  - Placeholder logic that can be extended later

#### Subagents + Skills Extension

- **FR-011**: System MUST update each subagent file with TODO sections for Chapter 2:
  - `backend/app/ai/subagents/ask_question_agent.py` - Expected inputs for ROS 2 questions, expected output format
  - `backend/app/ai/subagents/explain_el10_agent.py` - Expected inputs for ROS 2 concepts, expected output format
  - `backend/app/ai/subagents/quiz_agent.py` - Expected inputs for ROS 2 quizzes, expected output format
  - `backend/app/ai/subagents/diagram_agent.py` - Expected inputs for ROS 2 diagrams, expected output format
- **FR-012**: Each subagent TODO section MUST include:
  - Expected inputs for ROS 2 concepts (e.g., "nodes", "topics", "services", "actions")
  - Expected output format for Chapter 2 context
  - Placeholders only — no logic implementation
- **FR-013**: All subagent files MUST remain importable:
  - No syntax errors
  - All imports resolve correctly
  - Existing Chapter 1 functionality not broken

### Assumptions

- **Assumption 1**: AI block React components already exist from Feature 004 (Chapter 1 AI blocks)
- **Assumption 2**: Runtime engine, RAG pipeline, and subagents already exist from previous features
- **Assumption 3**: Chapter 2 MDX file exists with HTML comment placeholders (from Feature 010)
- **Assumption 4**: Chapter 2 metadata exists in `backend/app/content/chapters/chapter_2.py` (from Feature 010)
- **Assumption 5**: No new AI logic needs to be implemented (only scaffolding and integration)
- **Assumption 6**: Chapter 2 content chunks will be implemented in future features (this feature only creates placeholder)
- **Assumption 7**: ROS 2-specific context will be handled by existing subagents with Chapter 2 knowledge source
- **Assumption 8**: Docusaurus MDX component mapping already configured (from Feature 004)

### Key Entities

**Chapter 2 AI Block Component**:
- Component name (e.g., "AskQuestionBlock")
- Props interface (chapterId=2, sectionId, concept, diagramType, etc.)
- UI structure (reuses existing components from Feature 004)
- Event handlers (reuses existing handlers, routes to backend with chapterId=2)

**Chapter 2 Runtime Mapping**:
- Knowledge source identifier (chapter_id=2 or "chapter_2")
- RAG pipeline integration point (TODO comments)
- Chunk retrieval function (placeholder in chapter_2_chunks.py)

**Chapter 2 Subagent Integration**:
- Expected ROS 2 concept inputs (nodes, topics, services, actions, packages, launch files)
- Expected output format for ROS 2 context
- TODO sections in each subagent file

## Success Criteria *(mandatory)*

- **SC-001**: Chapter 2 MDX renders all 4 AI blocks correctly at designated positions
- **SC-002**: All backend scaffolding exists for Chapter 2 AI runtime (chapter_2_chunks.py, runtime engine mapping, subagent TODOs)
- **SC-003**: Runtime engine has placeholders for RAG + LLM for Chapter 2
- **SC-004**: No business logic implemented (only scaffolding and placeholders)
- **SC-005**: No errors during frontend or backend startup
- **SC-006**: Docusaurus build succeeds with Chapter 2 AI blocks
- **SC-007**: All imports resolve correctly (frontend and backend)
- **SC-008**: Chapter 2 AI blocks use correct props (chapterId=2, appropriate sectionId/concept/diagramType)

## Constraints *(mandatory)*

- **Constraint 1**: Must reuse existing AI block components from Feature 004 (no new component creation)
- **Constraint 2**: Must not implement real AI logic (only scaffolding and placeholders)
- **Constraint 3**: Must not break existing Chapter 1 AI block functionality
- **Constraint 4**: Must follow same patterns used in Chapter 1 AI blocks integration
- **Constraint 5**: Must not create new subagents (only extend existing ones with TODOs)
- **Constraint 6**: Must not implement RAG chunking logic (only placeholder function)

## Dependencies *(mandatory)*

- **Dependency 1**: Feature 004 (Chapter 1 Interactive AI Blocks) - Required for existing components and patterns
- **Dependency 2**: Feature 010 (Chapter 2 Content) - Required for Chapter 2 MDX file and metadata
- **Dependency 3**: Runtime Engine (from previous features) - Required for AI block routing
- **Dependency 4**: RAG Pipeline (from previous features) - Required for knowledge source mapping
- **Dependency 5**: Subagents (from previous features) - Required for AI block processing

## Out of Scope

- ❌ Implementing real AI logic for Chapter 2
- ❌ Creating new AI block components
- ❌ Implementing RAG chunking for Chapter 2 content
- ❌ Adding ROS 2-specific AI processing
- ❌ Creating new subagents
- ❌ Implementing authentication or personalization
- ❌ Adding real API calls to LLM providers
- ❌ Implementing diagram generation logic
- ❌ Creating quiz question generation logic
