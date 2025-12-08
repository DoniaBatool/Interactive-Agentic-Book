# Implementation Plan: Selection-Based RAG Engine — Highlight → Context → Answer

**Branch**: `051-selection-rag` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/051-selection-rag/spec.md`

## Summary

This feature implements complete scaffolding for selection-based RAG used by the textbook UI. When a learner highlights text inside any chapter (MDX), the system extracts that text, sends it to the backend, and answers ONLY from that selected content. **All implementations are scaffolding only—no real AI logic, embeddings, or LLM calls.**

**Primary Deliverable**: Complete scaffolding structure for selection-based RAG pipeline
**Validation**: All scaffolded files exist, imports work, frontend selection bar appears, backend endpoint returns placeholders

---

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ (FastAPI)
- Frontend: TypeScript/React (Docusaurus MDX)

**Primary Dependencies**:
- Feature 044: System Integration Phase 1 (unified runtime)
- Feature 045: System Integration Phase 2 (RAG pipeline structure)
- Frontend MDX chapter viewer exists
- Backend RAG pipeline structure exists

**External Dependencies**:
- Browser Selection API (window.getSelection())
- FastAPI for backend endpoints
- React for frontend components

**Storage**:
- No persistent storage required (scaffolding only)

**Testing**:
- Manual: Verify selection listener works, SelectionRAGBar appears, API endpoint accepts requests
- Automated: Placeholder test stubs (future)

**Target Platform**:
- Backend: FastAPI server
- Frontend: Docusaurus MDX pages

**Project Type**: Scaffolding / Architecture Foundation

**Performance Goals**:
- Selection capture: < 100ms
- API response: < 500ms (placeholder)

**Constraints**:
- MUST NOT implement real AI logic
- MUST NOT implement real embedding generation
- MUST NOT implement real LLM calls
- MUST only create scaffolding with TODO comments
- MUST ensure all imports resolve correctly

**Scale/Scope**:
- 1 frontend component (SelectionRAGBar)
- 1 backend API endpoint
- 1 RAG pipeline file (selection_pipeline.py)
- 1 runtime engine file (selection_engine.py)
- 1 subagent file (selection_agent.py)
- 2 skill files (cleaning_skill, context_skill)
- ~500-800 lines of scaffolding code

---

## 1. Overview

### Architecture Purpose

The Selection-Based RAG Engine enables learners to highlight specific text passages in chapters and ask questions about only that selected content. This provides precise, context-aware learning experiences.

### High-Level Architecture

```
Frontend MDX Chapter Viewer
    ↓ (user highlights text)
Selection Listener (invisible)
    ↓ (selection.length > N)
SelectionRAGBar Component (appears)
    ↓ (user submits question)
POST /api/rag/selection
    ↓
Backend Selection RAG Pipeline (selection_pipeline.py) ← NEW
    ├─► Clean Selected Text (placeholder)
    ├─► Embed Selected Text (placeholder)
    ├─► Similarity Search (placeholder)
    └─► Build Context (placeholder)
    ↓
Selection Runtime Engine (selection_engine.py) ← NEW
    ├─► Build Prompt Template (placeholder)
    └─► Call LLM Provider (placeholder)
    ↓
Selection Agent (selection_agent.py) ← NEW
    ├─► Selection Cleaning Skill (placeholder)
    └─► Selection Context Skill (placeholder)
    ↓
Response: { answer, context_used }
```

---

## 2. Frontend Architecture

### 2.1 MDX Wrapper Selection Detection

**File**: MDX wrapper component (to be identified/updated)

**Implementation**:
- Add invisible selection listener using `window.getSelection()` API
- Listen for `mouseup` and `selectionchange` events
- Extract selected text using `selection.toString()`
- Validate selection length (min 10 characters)
- Store selection in component state

**Code Structure**:
```typescript
// Pseudo-code structure
useEffect(() => {
  const handleSelection = () => {
    const selection = window.getSelection();
    if (selection && selection.toString().length > 10) {
      setSelectedText(selection.toString());
      setShowSelectionBar(true);
    }
  };
  document.addEventListener('mouseup', handleSelection);
  return () => document.removeEventListener('mouseup', handleSelection);
}, []);
```

**Acceptance**:
- Selection listener captures text
- SelectionRAGBar appears when text is selected
- Selection state updates correctly

---

### 2.2 SelectionRAGBar Component

**File**: `frontend/src/components/selection/SelectionRAGBar.tsx`

**Props**:
```typescript
interface SelectionRAGBarProps {
  selectedText: string;
  chapterId: number;
  onClose: () => void;
}
```

**UI Structure**:
- Selected text preview (truncated to 200 chars)
- Textarea for question input
- "Ask" button
- "Close" button

**Implementation**:
- Display selected text preview
- Accept question input
- On "Ask" click: POST to `/api/rag/selection`
- Display placeholder response
- Minimal styling (functional only)

**Acceptance**:
- Component renders correctly
- Selected text preview displays
- Question input works
- API call triggered on "Ask"
- Close button works

---

### 2.3 Data Flow: Selection → Component → API

**Flow**:
1. User highlights text in MDX
2. Selection listener captures text
3. SelectionRAGBar appears with selected text
4. User enters question
5. User clicks "Ask"
6. Component sends POST request:
   ```json
   {
     "selected_text": "...",
     "question": "...",
     "chapter_id": 1
   }
   ```
7. Component receives response:
   ```json
   {
     "answer": "placeholder answer",
     "context_used": "placeholder context"
   }
   ```
8. Component displays response (placeholder)

---

## 3. Backend API Architecture

### 3.1 Endpoint Structure

**File**: `backend/app/api/rag.py` (new or update existing)

**Endpoint**: `POST /api/rag/selection`

**Router Registration**: Update `backend/app/main.py` to include rag router

**Request Model**:
```python
from pydantic import BaseModel

class SelectionRAGRequest(BaseModel):
    selected_text: str  # 10-5000 chars
    question: str       # 5-500 chars
    chapter_id: int     # 1-999
```

**Response Model**:
```python
class SelectionRAGResponse(BaseModel):
    answer: str
    context_used: str
```

**Implementation**:
- Accept POST request
- Validate request model
- Call selection_engine (placeholder)
- Return placeholder response
- Error handling for invalid requests

**Acceptance**:
- Endpoint accepts POST requests
- Request validation works
- Placeholder response returned
- Error handling works

---

## 4. RAG Pipeline (Selection Mode)

### 4.1 Pipeline Responsibilities

**File**: `backend/app/ai/rag/selection_pipeline.py`

**Functions**:
1. `clean_selected_text(selected_text: str) -> str`
   - TODO: Remove extra whitespace
   - TODO: Normalize line breaks
   - TODO: Remove special characters if needed
   - Placeholder: return selected_text as-is

2. `embed_selected_text(selected_text: str) -> List[float]`
   - TODO: Generate embedding for selected text
   - TODO: Use existing embedding client
   - Placeholder: return empty list

3. `run_similarity_search_over_selected(selected_text: str, query: str) -> List[Dict]`
   - TODO: Perform local retrieval within selection
   - TODO: Extract relevant passages from selection
   - Placeholder: return empty list

4. `build_context(selected_text: str, search_results: List[Dict]) -> str`
   - TODO: Build context string from selection and results
   - Placeholder: return selected_text

5. `pass_context_to_llm(context: str, question: str) -> str`
   - TODO: Build prompt with selection context
   - TODO: Call LLM provider
   - Placeholder: return "placeholder answer"

**Flow Diagram**:
```
selected_text → clean_selected_text() → embed_selected_text() 
    ↓
run_similarity_search_over_selected() → build_context() 
    ↓
pass_context_to_llm() → answer
```

**Acceptance**:
- All functions exist with correct signatures
- TODO comments explain expected behavior
- Imports resolve correctly

---

## 5. Subagent Architecture

### 5.1 Selection Agent

**File**: `backend/app/ai/subagents/selection_agent.py`

**Input Schema**:
```python
{
    "selected_text": str,
    "question": str,
    "chapter_id": int
}
```

**Output Schema**:
```python
{
    "answer": str,
    "context_used": str
}
```

**Responsibility Boundary**:
- Accepts selection request
- Coordinates with selection skills
- Calls selection pipeline
- Returns formatted response

**Integration with Skills**:
- Uses `selection_cleaning_skill` to clean selected text
- Uses `selection_context_skill` to build context
- TODO: Core selection-based reasoning

**Implementation**:
```python
class SelectionAgent(BaseAgent):
    async def run(self, request_data: Dict, context: Dict) -> Dict:
        # TODO: Implement selection-based reasoning
        return {
            "answer": "placeholder answer",
            "context_used": "placeholder context"
        }
```

**Acceptance**:
- File exists with input/output schemas
- Integrates with base_agent.py pattern
- TODO comments for future implementation

---

## 6. Skills Architecture

### 6.1 Selection Cleaning Skill

**File**: `backend/app/ai/skills/selection_cleaning_skill.py`

**Methods**:
- `clean_selection(selected_text: str) -> str`
  - TODO: Remove extra whitespace
  - TODO: Normalize formatting
  - Placeholder: return selected_text

**Acceptance**:
- File exists with placeholder method
- TODO comments explain expected behavior

---

### 6.2 Selection Context Skill

**File**: `backend/app/ai/skills/selection_context_skill.py`

**Methods**:
- `build_selection_context(selected_text: str, question: str) -> str`
  - TODO: Build context string from selection
  - TODO: Format for LLM prompt
  - Placeholder: return selected_text

**Acceptance**:
- File exists with placeholder method
- TODO comments explain expected behavior

---

## 7. Runtime Integration

### 7.1 Selection Engine

**File**: `backend/app/ai/runtime/selection_engine.py`

**Function**:
```python
async def process_selection_rag(
    selected_text: str,
    question: str,
    chapter_id: int
) -> Dict[str, str]:
    # TODO: Build prompt template
    # TODO: Call selection pipeline
    # TODO: Call LLM provider
    # TODO: Format response
    return {
        "answer": "placeholder answer",
        "context_used": "placeholder context"
    }
```

**Integration**:
- Called from `/api/rag/selection` endpoint
- Uses selection_pipeline.py functions
- Uses selection_agent.py for coordination
- Returns formatted response

**Acceptance**:
- File exists with placeholder logic
- Function accepts correct parameters
- Returns scaffold response structure

---

## 8. Filepaths

### Files to Create

**Backend**:
- `backend/app/api/rag.py` (new - selection endpoint)
- `backend/app/ai/rag/selection_pipeline.py` (new)
- `backend/app/ai/runtime/selection_engine.py` (new)
- `backend/app/ai/subagents/selection_agent.py` (new)
- `backend/app/ai/skills/selection_cleaning_skill.py` (new)
- `backend/app/ai/skills/selection_context_skill.py` (new)

**Frontend**:
- `frontend/src/components/selection/SelectionRAGBar.tsx` (new)

**Files to Update**:
- `backend/app/main.py` (register rag router)
- MDX wrapper component (add selection listener)

---

## 9. Constraints

- **No Real AI Logic**: All AI, embedding, and LLM logic must be placeholders only
- **Scaffolding Only**: This feature creates structure, not functionality
- **No Database**: No persistence layer required
- **Minimal UI**: SelectionRAGBar should be minimal, functional placeholder
- **Browser Selection API**: Must use standard browser APIs (no external libraries)

---

## 10. Acceptance Criteria Mapping

| Acceptance Criteria | Implementation Location |
|---------------------|------------------------|
| Full pipeline exists | All files created with placeholder logic |
| No real AI logic | All functions return placeholders |
| Backend compiles | All imports resolve correctly |
| Frontend selection bar appears | SelectionRAGBar component created |
| spec.md, plan.md, tasks.md created | All specification files exist |

---

## 11. Risk Analysis

**Risk 1**: Selection listener may not work in all MDX contexts
- **Mitigation**: Test in Docusaurus MDX environment, use standard browser APIs

**Risk 2**: Selected text may contain formatting that breaks processing
- **Mitigation**: Cleaning skill will normalize text (placeholder for now)

**Risk 3**: Selection boundaries may not align with semantic chunks
- **Mitigation**: Selection RAG will work with raw selected text (no chunking needed)

---

## 12. Future Enhancements

- Real LLM calls for selection-based answers
- Real embedding generation for selected text
- Real similarity search within selection
- Multi-selection support
- Selection history and persistence
- Selection-based diagram generation

