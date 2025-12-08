# Quickstart Guide: Global Search Engine

**Feature**: 057-global-search-engine
**Branch**: `057-global-search-engine`
**Estimated Time**: 2-3 hours (scaffolding only)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 045 (System Integration Phase 2) completed
- [x] Feature 056 (Global Stabilization) completed
- [x] Git branch `057-global-search-engine` checked out
- [x] Read `specs/057-global-search-engine/spec.md`
- [x] Read `specs/057-global-search-engine/plan.md`
- [x] Read `specs/057-global-search-engine/tasks.md`

## Implementation Overview

**Total Steps**: 7 phases
**Primary Deliverable**: Complete search scaffolding with router, ranking, formatter, API endpoint, and frontend search bar
**Validation**: All search modules exist, API endpoint returns placeholders, frontend search bar renders

---

## Phase 1: Search Router (25 minutes)

### Step 1.1: Create Search Router

**File**: `backend/app/ai/search/router.py`

**Action**: Create placeholder functions:
- Scoring rules
- Chapter ranking logic
- Fallback search logic
- TODO comments

---

## Phase 2: Ranking Model (20 minutes)

### Step 2.1: Create Ranking Module

**File**: `backend/app/ai/search/ranking.py`

**Action**: Create placeholder functions:
- BM25-style scoring skeleton
- Embedding similarity score placeholder
- TODO comments

---

## Phase 3: Search Formatter (20 minutes)

### Step 3.1: Create Search Formatter

**File**: `backend/app/ai/formatters/search_formatter.py`

**Action**: Create placeholder functions:
- Normalize score
- Format chapter title + snippet + score
- TODO comments

---

## Phase 4: Search API (25 minutes)

### Step 4.1: Create Search API Endpoint

**File**: `backend/app/api/search.py`

**Action**: Create GET `/api/search?q=...` endpoint:
- Route to search router
- Return placeholder structure
- Register router in main.py

---

## Phase 5: Collections Update (15 minutes)

### Step 5.1: Update Collections File

**File**: `backend/app/ai/rag/collections.py`

**Action**: Add:
- List of chapter collections
- TODO: iterate over all collections

---

## Phase 6: Embedding Wrapper (10 minutes)

### Step 6.1: Update Embedding Client

**File**: `backend/app/ai/embeddings/embedding_client.py`

**Action**: Add TODO comment:
- Fetch embedding for search query

---

## Phase 7: Frontend Search Bar (20 minutes)

### Step 7.1: Update Search Bar Component

**File**: `frontend/src/components/SearchBar/index.tsx`

**Action**: Add:
- Input field
- Submit handler
- Placeholder UI (no styling)

---

## Validation Checklist

After implementation, verify:

- [ ] router.py exists with routing functions
- [ ] ranking.py exists with ranking functions
- [ ] search_formatter.py exists with formatting functions
- [ ] search.py exists with API endpoint
- [ ] collections.py updated with collection list
- [ ] embedding_client.py updated with TODO
- [ ] SearchBar/index.tsx updated with input
- [ ] Backend starts without errors
- [ ] Frontend builds without errors

---

## Next Steps

After completing scaffolding:

1. Test search endpoint with sample queries
2. Test search router functions
3. Test ranking functions
4. Implement real search logic in future features

---

## Troubleshooting

**Issue**: Import errors
- **Solution**: Check all __init__.py files exist

**Issue**: Search endpoint not found
- **Solution**: Verify router is registered in main.py

**Issue**: Frontend search bar doesn't render
- **Solution**: Check SearchBar component imports

