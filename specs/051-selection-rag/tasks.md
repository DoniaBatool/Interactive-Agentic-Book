# Implementation Tasks: Selection-Based RAG Engine

**Feature**: 051-selection-rag  
**Date**: 2025-01-27  
**Status**: Draft

## Task Groups

### A. Frontend Tasks

- [ ] **T001**: Create `frontend/src/components/selection/SelectionRAGBar.tsx` with UI placeholders
  - Props: selectedText, chapterId, onClose
  - Selected text preview (truncated to 200 chars)
  - Textarea for question input
  - "Ask" button
  - "Close" button
  - Minimal styling (functional only)
  - File: `frontend/src/components/selection/SelectionRAGBar.tsx`

- [ ] **T002**: Add MDX wrapper selection listener
  - Use `window.getSelection()` API
  - Listen for `mouseup` and `selectionchange` events
  - Extract selected text using `selection.toString()`
  - Validate selection length (min 10 characters)
  - Store selection in component state
  - Trigger SelectionRAGBar when selection.length > 10
  - File: MDX wrapper component (to be identified/updated)

- [ ] **T003**: Wire selection → state → component
  - Update component state when selection changes
  - Pass selected text to SelectionRAGBar
  - Handle selection clearing
  - File: MDX wrapper component

- [ ] **T004**: POST request to backend using fetch()
  - Implement API call in SelectionRAGBar
  - Request body: { selected_text, question, chapter_id }
  - Handle loading state
  - Display placeholder response
  - Error handling
  - File: `frontend/src/components/selection/SelectionRAGBar.tsx`

---

### B. Backend API Tasks

- [ ] **T005**: Create `backend/app/api/rag.py` router file
  - Create FastAPI router
  - Import necessary dependencies
  - File: `backend/app/api/rag.py`

- [ ] **T006**: Add POST `/api/rag/selection` endpoint with request/response models
  - Create `SelectionRAGRequest` Pydantic model
  - Create `SelectionRAGResponse` Pydantic model
  - Implement POST endpoint handler
  - Validate request
  - File: `backend/app/api/rag.py`

- [ ] **T007**: Return placeholder response
  - Call selection_engine (placeholder)
  - Return { answer: "placeholder", context_used: "placeholder" }
  - File: `backend/app/api/rag.py`

- [ ] **T008**: Register router in main.py
  - Import rag router
  - Include router in FastAPI app
  - File: `backend/app/main.py`

---

### C. RAG Pipeline Tasks

- [ ] **T009**: Create `backend/app/ai/rag/selection_pipeline.py`
  - Create file with module docstring
  - Import necessary dependencies
  - File: `backend/app/ai/rag/selection_pipeline.py`

- [ ] **T010**: Add placeholder function `clean_selected_text(selected_text: str) -> str`
  - TODO: Remove extra whitespace
  - TODO: Normalize line breaks
  - Placeholder: return selected_text as-is
  - File: `backend/app/ai/rag/selection_pipeline.py`

- [ ] **T011**: Add placeholder function `embed_selected_text(selected_text: str) -> List[float]`
  - TODO: Generate embedding for selected text
  - Placeholder: return empty list
  - File: `backend/app/ai/rag/selection_pipeline.py`

- [ ] **T012**: Add placeholder function `run_similarity_search_over_selected(selected_text: str, query: str) -> List[Dict]`
  - TODO: Perform local retrieval within selection
  - Placeholder: return empty list
  - File: `backend/app/ai/rag/selection_pipeline.py`

- [ ] **T013**: Add placeholder function `build_context(selected_text: str, search_results: List[Dict]) -> str`
  - TODO: Build context string from selection and results
  - Placeholder: return selected_text
  - File: `backend/app/ai/rag/selection_pipeline.py`

- [ ] **T014**: Add placeholder function `pass_context_to_llm(context: str, question: str) -> str`
  - TODO: Build prompt with selection context
  - TODO: Call LLM provider
  - Placeholder: return "placeholder answer"
  - File: `backend/app/ai/rag/selection_pipeline.py`

---

### D. Runtime Engine Tasks

- [ ] **T015**: Create `backend/app/ai/runtime/selection_engine.py`
  - Create file with module docstring
  - Import necessary dependencies
  - File: `backend/app/ai/runtime/selection_engine.py`

- [ ] **T016**: Accept selected_text + question
  - Create `process_selection_rag()` function
  - Parameters: selected_text, question, chapter_id
  - File: `backend/app/ai/runtime/selection_engine.py`

- [ ] **T017**: Build prompt template (placeholder)
  - TODO: Build prompt template
  - Placeholder: return template string
  - File: `backend/app/ai/runtime/selection_engine.py`

- [ ] **T018**: Return dummy response
  - Return { answer: "placeholder", context_used: "placeholder" }
  - File: `backend/app/ai/runtime/selection_engine.py`

---

### E. Subagent Tasks

- [ ] **T019**: Create `backend/app/ai/subagents/selection_agent.py`
  - Create file with module docstring
  - Import BaseAgent
  - File: `backend/app/ai/subagents/selection_agent.py`

- [ ] **T020**: Add input/output schemas
  - Input schema: { selected_text, question, chapter_id }
  - Output schema: { answer, context_used }
  - Document schemas in docstrings
  - File: `backend/app/ai/subagents/selection_agent.py`

- [ ] **T021**: Add TODO behaviors
  - Implement SelectionAgent class extending BaseAgent
  - Add async run() method with TODO comments
  - Placeholder return: { answer: "placeholder", context_used: "placeholder" }
  - File: `backend/app/ai/subagents/selection_agent.py`

---

### F. Skills Tasks

- [ ] **T022**: Create `backend/app/ai/skills/selection_cleaning_skill.py` with placeholder methods
  - Create file with module docstring
  - Add `clean_selection(selected_text: str) -> str` method
  - TODO: Remove extra whitespace, normalize formatting
  - Placeholder: return selected_text as-is
  - File: `backend/app/ai/skills/selection_cleaning_skill.py`

- [ ] **T023**: Create `backend/app/ai/skills/selection_context_skill.py` with placeholder methods
  - Create file with module docstring
  - Add `build_selection_context(selected_text: str, question: str) -> str` method
  - TODO: Build context string from selection
  - Placeholder: return selected_text
  - File: `backend/app/ai/skills/selection_context_skill.py`

---

### G. Validation Tasks

- [ ] **T024**: Backend should start with uvicorn
  - Run `uvicorn app.main:app --reload`
  - Verify no import errors
  - Verify endpoint is registered

- [ ] **T025**: Frontend build must pass
  - Run `npm run build` (or equivalent)
  - Verify no TypeScript errors
  - Verify SelectionRAGBar component compiles

- [ ] **T026**: SelectionRAGBar should appear when text is selected
  - Open chapter MDX page
  - Highlight text (10+ characters)
  - Verify SelectionRAGBar appears
  - Verify selected text preview displays

---

## Task Summary

- **Total Tasks**: 26
- **Frontend Tasks**: 4 (T001-T004)
- **Backend API Tasks**: 4 (T005-T008)
- **RAG Pipeline Tasks**: 6 (T009-T014)
- **Runtime Engine Tasks**: 4 (T015-T018)
- **Subagent Tasks**: 3 (T019-T021)
- **Skills Tasks**: 2 (T022-T023)
- **Validation Tasks**: 3 (T024-T026)

---

## Implementation Order

1. Backend scaffolding (API, pipeline, engine, subagent, skills)
2. Frontend scaffolding (SelectionRAGBar, selection listener)
3. Integration (wire frontend to backend)
4. Validation (test all components)

---

## Notes

- All tasks create scaffolding only—no real AI logic
- All functions must have TODO comments explaining expected behavior
- All imports must resolve correctly
- All files must follow existing code patterns

