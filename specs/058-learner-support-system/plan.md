# Implementation Plan: Learner Support System (LSS) — Hints, Summaries & Progress Helper

**Branch**: `058-learner-support-system` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature implements complete scaffolding for Learner Support System. It introduces hints system, section summary engine, progress helper, and LSS API endpoints. **All implementations are scaffolding only—no real AI logic, no real database, no real RAG integration.**

**Primary Deliverable**: Complete LSS scaffolding structure
**Validation**: All LSS modules exist, API endpoints return placeholders, backend starts

---

## 1. Module Architecture

### 1.1 Folder Structure

```
backend/app/ai/lss/
├── __init__.py          # Package init
├── hints.py             # HintEngine class
├── summaries.py         # SummaryEngine class
└── progress.py         # ProgressTracker class

backend/app/api/
└── lss.py               # LSS API router

specs/058-learner-support-system/contracts/
└── lss-api.yaml         # API contract
```

---

### 1.2 File Responsibilities

**hints.py**: 
- HintEngine class
- get_hint() method
- Hint type definitions
- Placeholder hint generation

**summaries.py**:
- SummaryEngine class
- summarize_section() method
- Summary length rules
- Placeholder summary generation

**progress.py**:
- ProgressTracker class
- get_section_status() method
- mark_section_complete() method
- Placeholder progress tracking

**lss.py**:
- API router
- 4 endpoints (hint, summary, progress/update, progress/get)
- Request/response models
- Placeholder responses

---

### 1.3 Class Diagrams (Text-Only)

```
HintEngine
  + get_hint(chapter_id, section_id, user_state) -> str

SummaryEngine
  + summarize_section(chapter_id, section_id) -> str

ProgressTracker
  + get_section_status(user_id, chapter_id) -> dict
  + mark_section_complete(user_id, chapter_id, section_id) -> None
```

---

### 1.4 Data Flow Between Modules

```
API Request
  → lss.py (router)
    → hints.py / summaries.py / progress.py (engine)
      → Return placeholder response
        → lss.py (format response)
          → API Response
```

---

## 2. API Layer Design

### 2.1 Endpoints

**POST /api/lss/hint**:
- Input: chapter_id, section_id, user_state (optional)
- Calls: HintEngine.get_hint()
- Output: hint, hint_type, chapter_id, section_id

**POST /api/lss/summary**:
- Input: chapter_id, section_id
- Calls: SummaryEngine.summarize_section()
- Output: summary, chapter_id, section_id, summary_length

**POST /api/lss/progress/update**:
- Input: user_id, chapter_id, section_id
- Calls: ProgressTracker.mark_section_complete()
- Output: message, user_id, chapter_id, section_id

**GET /api/lss/progress/{user_id}/{chapter_id}**:
- Input: user_id (path), chapter_id (path)
- Calls: ProgressTracker.get_section_status()
- Output: user_id, chapter_id, sections (list)

---

### 2.2 Inputs/Outputs (Placeholder Only)

All endpoints accept placeholder request data and return placeholder responses. No real validation, no real processing.

---

### 2.3 How Endpoints Call LSS Engines

1. Extract request data
2. Call appropriate engine method
3. Format response
4. Return placeholder JSON

---

## 3. Runtime Interaction

### 3.1 Chapter Metadata Integration

**Future Integration**:
- Use chapter metadata for context
- Use section metadata for summaries
- Use metadata for hint generation

**Current (Placeholder)**:
- TODO comments for metadata usage
- Placeholder data only

---

### 3.2 RAG Pipeline Integration

**Future Integration**:
- Use RAG pipeline for context retrieval
- Use embeddings for similarity
- Use retrieved chunks for hints/summaries

**Current (Placeholder)**:
- TODO comments for RAG integration
- No real RAG calls

---

### 3.3 Provider LLM Integration

**Future Integration**:
- Use LLM provider for hint generation
- Use LLM provider for summary generation
- Use LLM provider for context understanding

**Current (Placeholder)**:
- TODO comments for LLM integration
- No real LLM calls

---

## 4. Data Contracts

### 4.1 Hint Request/Response Format

**Request**:
```json
{
  "chapter_id": 1,
  "section_id": "what-is-physical-ai",
  "user_state": {
    "current_section": "what-is-physical-ai",
    "difficulty_level": "medium"
  }
}
```

**Response**:
```json
{
  "hint": "Physical AI combines artificial intelligence with robotics...",
  "hint_type": "concept",
  "chapter_id": 1,
  "section_id": "what-is-physical-ai"
}
```

---

### 4.2 Summary Request/Response Format

**Request**:
```json
{
  "chapter_id": 1,
  "section_id": "what-is-physical-ai"
}
```

**Response**:
```json
{
  "summary": "This section introduces Physical AI, which combines...",
  "chapter_id": 1,
  "section_id": "what-is-physical-ai",
  "summary_length": 150
}
```

---

### 4.3 Progress Tracker Request/Response Format

**Update Request**:
```json
{
  "user_id": "user_123",
  "chapter_id": 1,
  "section_id": "what-is-physical-ai"
}
```

**Update Response**:
```json
{
  "message": "Section marked as complete (placeholder)",
  "user_id": "user_123",
  "chapter_id": 1,
  "section_id": "what-is-physical-ai"
}
```

**Get Response**:
```json
{
  "user_id": "user_123",
  "chapter_id": 1,
  "sections": [
    {
      "section_id": "what-is-physical-ai",
      "status": "completed",
      "completed_at": "2025-01-27T00:00:00Z"
    }
  ]
}
```

---

## 5. Non-Functional Requirements

### 5.1 Must Not Break Existing Runtime

- LSS is optional
- No modifications to existing runtime engine
- No modifications to existing RAG pipeline
- No modifications to existing AI blocks

---

### 5.2 Must Be Fully Optional

- Chapters can exist without LSS
- LSS endpoints are optional
- No required LSS data
- Graceful degradation if LSS unavailable

---

## 6. File-by-File Implementation Order

1. `backend/app/ai/lss/__init__.py` - Package init
2. `backend/app/ai/lss/hints.py` - HintEngine class
3. `backend/app/ai/lss/summaries.py` - SummaryEngine class
4. `backend/app/ai/lss/progress.py` - ProgressTracker class
5. `backend/app/api/lss.py` - LSS API router
6. `backend/app/main.py` - Register LSS router
7. `specs/058-learner-support-system/contracts/lss-api.yaml` - API contract

---

## 7. Constraints

- **NO Real AI Logic**: All implementations must be placeholders
- **Backend Only**: No frontend components
- **Scaffolding Only**: This feature creates structure, not functionality
- **NO Database**: No real progress storage
- **NO RAG Integration**: No real RAG calls

---

## 8. Acceptance Criteria Mapping

| Acceptance Criteria | Implementation Location |
|---------------------|------------------------|
| All scaffolding files created | All files created with placeholder logic |
| New API endpoints compile | All endpoints return placeholder JSON |
| No AI logic implemented | All functions have TODO comments only |
| Backend builds without errors | All imports resolve correctly |
| LSS integrates with chapter metadata | TODO comments for metadata usage |

---

## 9. Risk Analysis

**Risk 1**: LSS may conflict with existing progress tracking (Feature 055)
- **Mitigation**: Use different namespace, different endpoints

**Risk 2**: Import errors if module structure incorrect
- **Mitigation**: Ensure all `__init__.py` files exist, test imports

**Risk 3**: API endpoints may not integrate correctly
- **Mitigation**: Use placeholder logic, test endpoint registration

---

## 10. Future Enhancements

- Real AI-generated hints
- Real AI-generated summaries
- Database-backed progress
- RAG integration for context
- Context-aware hint generation
- Personalized summaries
- Progress analytics
