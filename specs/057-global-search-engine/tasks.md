# Implementation Tasks: Global Search + Multi-Chapter Query Engine

**Feature**: 057-global-search-engine  
**Date**: 2025-01-27  
**Status**: Draft

## Task Groups

### A. Search Router Tasks

- [ ] **T001**: Create `backend/app/ai/search/__init__.py`
  - Make search a package
  - File: `backend/app/ai/search/__init__.py`

- [ ] **T002**: Create `backend/app/ai/search/router.py`
  - Add function: `route_search_query(query) -> List[Dict]`
    - TODO: Route search query across all chapters
    - Placeholder: Return placeholder results
  - Add function: `rank_chapters(query) -> List[Dict]`
    - TODO: Rank chapters by relevance
    - Placeholder: Return placeholder rankings
  - Add function: `fallback_search(query) -> List[Dict]`
    - TODO: Fallback if primary search fails
    - Placeholder: Return placeholder results
  - File: `backend/app/ai/search/router.py`

---

### B. Ranking Model Tasks

- [ ] **T003**: Create `backend/app/ai/search/ranking.py`
  - Add function: `calculate_embedding_similarity(query_embedding, chunk_embedding) -> float`
    - TODO: Calculate cosine similarity
    - Placeholder: Return placeholder score
  - Add function: `calculate_bm25_score(query, chunk_text) -> float`
    - TODO: Calculate BM25-style score
    - Placeholder: Return placeholder score
  - Add function: `combine_scores(embedding_score, bm25_score) -> float`
    - TODO: Combine scores with weights
    - Placeholder: Return placeholder score
  - File: `backend/app/ai/search/ranking.py`

---

### C. Search Formatter Tasks

- [ ] **T004**: Create `backend/app/ai/formatters/search_formatter.py`
  - Add function: `normalize_score(score) -> float`
    - TODO: Normalize score to 0.0-1.0 range
    - Placeholder: Return score as-is
  - Add function: `format_search_result(chapter_id, chunk, score) -> Dict`
    - TODO: Format result with chapter title, snippet, score
    - Placeholder: Return placeholder result
  - File: `backend/app/ai/formatters/search_formatter.py`

---

### D. Search API Tasks

- [ ] **T005**: Create `backend/app/api/search.py`
  - Add GET `/api/search?q=...` endpoint
  - Route to search router
  - Return placeholder structure
  - File: `backend/app/api/search.py`

- [ ] **T006**: Register search router in main.py
  - Import: `from app.api.search import router as search_router`
  - Include: `app.include_router(search_router, tags=["search"])`
  - File: `backend/app/main.py`

---

### E. Collections Update Tasks

- [ ] **T007**: Update `backend/app/ai/rag/collections.py`
  - Add list of chapter collections (if not already present)
  - Add TODO: iterate over all collections
  - File: `backend/app/ai/rag/collections.py` (update existing)

---

### F. Embedding Wrapper Tasks

- [ ] **T008**: Update `backend/app/ai/embeddings/embedding_client.py`
  - Add TODO comment: fetch embedding for search query
  - Placeholder comment only
  - File: `backend/app/ai/embeddings/embedding_client.py` (update existing)

---

### G. Frontend Search Bar Tasks

- [ ] **T009**: Update `frontend/src/components/SearchBar/index.tsx`
  - Add input field
  - Add submit handler
  - Placeholder UI (no styling)
  - No real logic
  - File: `frontend/src/components/SearchBar/index.tsx` (update existing or create)

---

### H. Validation Tasks

- [ ] **T010**: Backend starts without errors
  - Verify: `cd backend && uvicorn app.main:app --reload` starts without errors
  - Check: All imports resolve correctly

- [ ] **T011**: Frontend builds without errors
  - Verify: `cd frontend && npm run build` succeeds
  - Check: All components compile

---

## Implementation Notes

- All backend functions must have TODO comments explaining expected behavior
- All functions must be placeholder implementations
- No real search logic should be implemented
- No real ranking logic should be implemented
- No real retrieval logic should be implemented
- All responses are static placeholders
- Search router should not conflict with existing routing

