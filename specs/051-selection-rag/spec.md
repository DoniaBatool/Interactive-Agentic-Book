# Feature Specification: Selection-Based RAG Engine — Highlight → Context → Answer

**Feature Branch**: `051-selection-rag`
**Created**: 2025-01-27
**Status**: Draft
**Type**: backend-rag-runtime
**Input**: User description: "Implement the complete scaffolding for selection-based RAG used by the textbook UI. When a learner highlights text inside any chapter (MDX), the system extracts that text, sends it to the backend, and answers ONLY from that selected content."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Learner Highlights Text and Gets Contextual Answer (Priority: P1)

As a learner, I need to highlight text in any chapter and ask a question about that specific selection, so I can get precise answers based only on the content I'm reading, without searching the entire chapter.

**Why this priority**: This provides immediate, contextual learning support. Learners can get instant clarification on specific passages without navigating away or losing context.

**Independent Test**: Can be fully tested by highlighting text in a chapter, entering a question, and verifying that the SelectionRAGBar appears and the backend endpoint returns a placeholder response.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I highlight text in any chapter MDX file, **Then** I see a SelectionRAGBar component appear with the selected text preview

2. **Given** the feature is implemented, **When** I enter a question in the SelectionRAGBar and click "Ask", **Then** the frontend sends a POST request to `/api/rag/selection` with `{selected_text, question, chapter_id}`

3. **Given** the feature is implemented, **When** the backend receives a selection request, **Then** it processes the request through the selection pipeline and returns `{answer: str, context_used: str}` (placeholder)

4. **Given** the feature is implemented, **When** I select text less than N characters, **Then** the SelectionRAGBar does not appear (to avoid noise from accidental selections)

---

### User Story 2 - Developer Can Extend Selection RAG Pipeline (Priority: P2)

As a developer, I need a complete scaffolding structure for selection-based RAG with clear separation between frontend selection capture, API contract, pipeline, runtime engine, and subagent, so I can implement real AI logic in future features without restructuring the codebase.

**Why this priority**: Important for maintainability and future development, but not critical for initial scaffolding. The structure enables incremental implementation.

**Independent Test**: Can be fully tested by verifying all required files exist at specified paths, all imports resolve without errors, and the pipeline structure is clear and extensible.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/ai/rag/selection_pipeline.py`, **Then** I see placeholder functions: `clean_selected_text()`, `embed_selected_text()`, `run_similarity_search_over_selected()`, `pass_context_to_llm()`

2. **Given** the feature is implemented, **When** I check `backend/app/ai/runtime/selection_engine.py`, **Then** I see a function that accepts `selected_text` and `question`, builds a prompt template (placeholder), and returns a scaffold response

3. **Given** the feature is implemented, **When** I check `backend/app/ai/subagents/selection_agent.py`, **Then** I see input/output schemas and TODO comments for core selection-based reasoning

4. **Given** the feature is implemented, **When** I check `backend/app/ai/skills/selection_cleaning_skill.py` and `selection_context_skill.py`, **Then** I see placeholder methods with TODO comments

---

### Edge Cases

- What happens when selected text is empty or too short?
  - **Expected**: Frontend should not show SelectionRAGBar, or backend should return error
- What happens when selected text is very long (e.g., entire chapter)?
  - **Expected**: Backend should truncate or handle gracefully, with clear limits
- What happens when question is empty?
  - **Expected**: Backend should return validation error
- What happens when chapter_id is invalid?
  - **Expected**: Backend should return error indicating invalid chapter

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Frontend Selection Extraction

- **FR-001.1**: System MUST update frontend chapter MDX layout to capture text selection:
  - Add invisible selection listener to MDX wrapper component
  - Trigger SelectionRAGBar when `selection.length > N` characters (e.g., N=10)
  - No AI logic — only UI + event capture

- **FR-001.2**: System MUST create `frontend/src/components/selection/SelectionRAGBar.tsx`:
  - Display selected text preview (truncated if long)
  - Textarea for question input
  - "Ask" button
  - Loading state (placeholder)
  - Error state (placeholder)
  - No styling complexity — minimal UI

#### FR-002: Frontend → Backend API Contract

- **FR-002.1**: System MUST create `backend/app/api/rag.py` (or update existing):
  - Add POST `/api/rag/selection` endpoint
  - Request model:
    ```python
    {
        "selected_text": str,  # Required, min_length=10
        "question": str,        # Required, min_length=1
        "chapter_id": int      # Required, valid chapter ID
    }
    ```
  - Response model:
    ```python
    {
        "answer": str,          # Placeholder answer
        "context_used": str     # Placeholder context snippet
    }
    ```
  - No AI logic; return placeholders

#### FR-003: Backend Selection RAG Pipeline (Scaffold Only)

- **FR-003.1**: System MUST create `backend/app/ai/rag/selection_pipeline.py`:
  - Function: `clean_selected_text(selected_text: str) -> str`:
    - TODO: Remove extra whitespace, normalize text
    - Return placeholder cleaned text
  - Function: `embed_selected_text(selected_text: str) -> List[float]`:
    - TODO: Generate embedding for selected text
    - Return placeholder embedding vector
  - Function: `run_similarity_search_over_selected(selected_text: str, query: str, chapter_id: int) -> List[Dict]`:
    - TODO: Perform similarity search within selected text context
    - Return placeholder chunks
  - Function: `pass_context_to_llm(context: str, question: str) -> str`:
    - TODO: Build prompt and call LLM provider
    - Return placeholder answer
  - All functions contain TODO comments only

#### FR-004: Runtime Integration Layer

- **FR-004.1**: System MUST create `backend/app/ai/runtime/selection_engine.py`:
  - Function: `process_selection_query(selected_text: str, question: str, chapter_id: int) -> Dict[str, Any]`:
    - Accepts `selected_text`, `question`, `chapter_id`
    - Calls selection pipeline functions (placeholder)
    - Builds prompt template (placeholder)
    - Calls placeholder LLM provider
    - Returns scaffold response: `{answer: str, context_used: str}`
  - All logic is placeholder with TODO comments

#### FR-005: Subagent for Selection Queries

- **FR-005.1**: System MUST create `backend/app/ai/subagents/selection_agent.py`:
  - Input schema:
    ```python
    {
        "selected_text": str,
        "question": str,
        "chapter_id": int
    }
    ```
  - Output schema:
    ```python
    {
        "answer": str,
        "context_used": str,
        "confidence": float  # Placeholder
    }
    ```
  - TODO: Core selection-based reasoning logic
  - No real logic implementation

#### FR-006: Skills Layer

- **FR-006.1**: System MUST create `backend/app/ai/skills/selection_cleaning_skill.py`:
  - Function: `clean_selection(selected_text: str) -> str`:
    - TODO: Remove noise, normalize whitespace, handle special characters
    - Return placeholder cleaned text

- **FR-006.2**: System MUST create `backend/app/ai/skills/selection_context_skill.py`:
  - Function: `build_selection_context(selected_text: str, retrieved_chunks: List[Dict]) -> str`:
    - TODO: Assemble context from selected text and retrieved chunks
    - Return placeholder context string
  - Both skills contain TODO comments only

#### FR-007: Update Chapter Viewer UI

- **FR-007.1**: System MUST add selection listener to MDX wrapper:
  - Listen for `mouseup` or `selectionchange` events
  - Extract selected text using `window.getSelection()`
  - Check if selection length > N characters
  - Show SelectionRAGBar component when condition met
  - Position SelectionRAGBar near selection (simple positioning)
  - No styling complexity — minimal UI

## Success Criteria

- ✅ Full pipeline exists: Frontend selection → API endpoint → selection pipeline → runtime engine → subagent
- ✅ No real AI or embedding logic is implemented
- ✅ Backend compiles with no errors
- ✅ Frontend selection bar appears (placeholder)
- ✅ spec.md, plan.md, tasks.md created correctly
- ✅ Contract file created
- ✅ Checklist file created
- ✅ Research, data-model, quickstart files created

## Constraints

- **No Real AI Logic**: All AI, embedding, and LLM logic must be placeholders with TODO comments
- **Scaffolding Only**: This feature creates structure only, no business logic
- **Minimal UI**: Frontend components should be minimal, no complex styling
- **No Database**: No persistence layer required
- **No Authentication**: No auth required for this feature

## Dependencies

- Feature 045 (System Integration Phase 2) — for RAG pipeline structure
- Feature 044 (System Integration Phase 1) — for runtime engine structure
- Frontend MDX chapter viewer — must exist

## Out of Scope

- Real embedding generation
- Real LLM provider calls
- Real similarity search
- Complex UI styling
- Selection persistence
- Multi-selection support
- Selection history
