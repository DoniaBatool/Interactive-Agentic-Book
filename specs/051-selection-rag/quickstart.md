# Quickstart Guide: Selection-Based RAG Engine

**Feature**: 051-selection-rag
**Branch**: `051-selection-rag`
**Estimated Time**: 2-3 hours (scaffolding only)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 045 (System Integration Phase 2) completed
- [x] Feature 044 (System Integration Phase 1) completed
- [x] Frontend MDX chapter viewer exists
- [x] Git branch `051-selection-rag` checked out
- [x] Read `specs/051-selection-rag/spec.md`
- [x] Read `specs/051-selection-rag/plan.md`
- [x] Read `specs/051-selection-rag/tasks.md`

## Implementation Overview

**Total Steps**: 7 phases
**Primary Deliverable**: Complete scaffolding for selection-based RAG with frontend selection capture, API endpoint, pipeline, runtime engine, subagent, and skills
**Validation**: SelectionRAGBar appears on text selection, API endpoint returns placeholder response

---

## Phase 1: Frontend Selection Extraction (30 minutes)

### Step 1.1: Create SelectionRAGBar Component

**File**: `frontend/src/components/selection/SelectionRAGBar.tsx`

**Action**: Create component with:
- Selected text preview (truncated)
- Textarea for question
- "Ask" button
- Loading state (placeholder)
- Error state (placeholder)
- Minimal UI styling

### Step 1.2: Add Selection Listener to MDX Wrapper

**File**: Update chapter MDX wrapper component

**Action**: Add selection listener:
- Listen for `mouseup` or `selectionchange` events
- Extract selected text using `window.getSelection()`
- Check if selection length > 10 characters
- Show SelectionRAGBar when condition met
- Position SelectionRAGBar near selection

---

## Phase 2: Backend API Endpoint (20 minutes)

### Step 2.1: Create Selection RAG Endpoint

**File**: `backend/app/api/rag.py` (or create new file)

**Action**: Add POST `/api/rag/selection` endpoint:
- Request model: `{selected_text: str, question: str, chapter_id: int}`
- Response model: `{answer: str, context_used: str}`
- Validation: min_length checks
- Return placeholder response

### Step 2.2: Register Router

**File**: `backend/app/main.py`

**Action**: Include selection RAG router if separate file created

---

## Phase 3: Selection Pipeline (25 minutes)

### Step 3.1: Create Selection Pipeline File

**File**: `backend/app/ai/rag/selection_pipeline.py`

**Action**: Create placeholder functions:
- `clean_selected_text(selected_text: str) -> str` (TODO)
- `embed_selected_text(selected_text: str) -> List[float]` (TODO)
- `run_similarity_search_over_selected(selected_text: str, query: str, chapter_id: int) -> List[Dict]` (TODO)
- `pass_context_to_llm(context: str, question: str) -> str` (TODO)

---

## Phase 4: Runtime Engine (20 minutes)

### Step 4.1: Create Selection Engine

**File**: `backend/app/ai/runtime/selection_engine.py`

**Action**: Create `process_selection_query()` function:
- Accepts `selected_text`, `question`, `chapter_id`
- Calls selection pipeline functions (placeholder)
- Builds prompt template (placeholder)
- Returns scaffold response

---

## Phase 5: Subagent (15 minutes)

### Step 5.1: Create Selection Agent

**File**: `backend/app/ai/subagents/selection_agent.py`

**Action**: Create subagent with:
- Input schema: `{selected_text, question, chapter_id}`
- Output schema: `{answer, context_used, confidence}`
- TODO comments for core logic

---

## Phase 6: Skills (20 minutes)

### Step 6.1: Create Selection Cleaning Skill

**File**: `backend/app/ai/skills/selection_cleaning_skill.py`

**Action**: Create `clean_selection()` function:
- TODO: Remove noise, normalize whitespace
- Return placeholder cleaned text

### Step 6.2: Create Selection Context Skill

**File**: `backend/app/ai/skills/selection_context_skill.py`

**Action**: Create `build_selection_context()` function:
- TODO: Assemble context from selected text and chunks
- Return placeholder context string

---

## Phase 7: Integration & Validation (20 minutes)

### Step 7.1: Wire Components Together

**Action**: Ensure all components connect:
- Frontend → API endpoint
- API endpoint → Runtime engine
- Runtime engine → Pipeline → Subagent
- Skills integrated into pipeline

### Step 7.2: Test Scaffolding

**Action**: Verify:
- Backend starts without errors
- Frontend builds without errors
- SelectionRAGBar appears on text selection
- API endpoint returns placeholder response

---

## Validation Checklist

After implementation, verify:

- [ ] SelectionRAGBar component exists and renders
- [ ] Selection listener works in MDX wrapper
- [ ] API endpoint `/api/rag/selection` exists
- [ ] Selection pipeline file exists with placeholder functions
- [ ] Runtime engine file exists
- [ ] Subagent file exists
- [ ] Skills files exist
- [ ] All imports resolve
- [ ] Backend starts without errors
- [ ] Frontend builds without errors
- [ ] SelectionRAGBar appears when text is selected (>10 chars)

---

## Next Steps

After completing scaffolding:

1. Test selection capture in frontend
2. Test API endpoint with sample data
3. Verify pipeline structure
4. Implement real AI logic in future features

---

## Troubleshooting

**Issue**: SelectionRAGBar doesn't appear
- **Solution**: Check selection listener is attached, verify minimum character threshold

**Issue**: API endpoint not found
- **Solution**: Verify router is registered in main.py

**Issue**: Import errors
- **Solution**: Check all file paths and __init__.py files exist
