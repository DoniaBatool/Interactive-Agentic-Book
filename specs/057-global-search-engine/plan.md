# Implementation Plan: Global Search + Multi-Chapter Query Engine

**Branch**: `057-global-search-engine` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature implements complete scaffolding for global search across all chapters. It introduces multi-chapter retrieval pipeline, search API endpoint, ranking model, search formatter, and frontend search bar. **All implementations are scaffolding only—no real search logic, no real ranking, no real retrieval.**

**Primary Deliverable**: Complete search scaffolding structure
**Validation**: All search modules exist, API endpoint returns placeholders, frontend search bar renders

---

## 1. Multi-Chapter Retrieval Architecture

### 1.1 Search Router

**File**: `backend/app/ai/search/router.py` (new)

**Purpose**: Route search queries to appropriate chapters

**Structure**:
```python
async def route_search_query(query: str) -> List[Dict]:
    """
    Route search query across all chapters.
    
    TODO: Real routing logic:
    1. Generate query embedding
    2. Search all chapter collections
    3. Score results
    4. Rank results
    5. Return top results
    
    Placeholder: Return placeholder results
    """
    # TODO: Real routing logic
    return [
        {
            "chapter_id": 1,
            "chapter_title": "Introduction to Physical AI & Robotics",
            "snippet": "Physical AI combines...",
            "score": 0.85
        }
    ]
```

---

### 1.2 Chapter Ranking

**File**: `backend/app/ai/search/router.py` (new)

**Purpose**: Rank chapters by relevance

**Structure**:
```python
async def rank_chapters(query: str) -> List[Dict]:
    """
    Rank chapters by relevance to query.
    
    TODO: Real ranking logic:
    1. Score all chapters
    2. Sort by score
    3. Return ranked list
    
    Placeholder: Return placeholder rankings
    """
    # TODO: Real ranking logic
    return [
        {"chapter_id": 1, "score": 0.9},
        {"chapter_id": 2, "score": 0.7},
        {"chapter_id": 3, "score": 0.8}
    ]
```

---

### 1.3 Fallback Search

**File**: `backend/app/ai/search/router.py` (new)

**Purpose**: Fallback if primary search fails

**Structure**:
```python
async def fallback_search(query: str) -> List[Dict]:
    """
    Fallback search if primary search fails.
    
    TODO: Real fallback logic:
    1. Try all chapters
    2. Return best matches
    3. Handle errors gracefully
    
    Placeholder: Return placeholder results
    """
    # TODO: Real fallback logic
    return []
```

---

## 2. Ranking Flow

### 2.1 Ranking Model

**File**: `backend/app/ai/search/ranking.py` (new)

**Purpose**: Score and rank search results

**Structure**:
```python
def calculate_embedding_similarity(query_embedding: List[float], chunk_embedding: List[float]) -> float:
    """
    Calculate embedding similarity score.
    
    TODO: Real similarity calculation:
    1. Calculate cosine similarity
    2. Normalize to 0.0-1.0
    3. Return score
    
    Placeholder: Return placeholder score
    """
    # TODO: Real similarity calculation
    return 0.85

def calculate_bm25_score(query: str, chunk_text: str) -> float:
    """
    Calculate BM25-style score.
    
    TODO: Real BM25 calculation:
    1. Calculate term frequencies
    2. Apply BM25 formula
    3. Normalize to 0.0-1.0
    4. Return score
    
    Placeholder: Return placeholder score
    """
    # TODO: Real BM25 calculation
    return 0.75

def combine_scores(embedding_score: float, bm25_score: float) -> float:
    """
    Combine embedding and BM25 scores.
    
    TODO: Real score combination:
    1. Weight scores (0.7 embedding, 0.3 BM25)
    2. Combine weighted scores
    3. Normalize to 0.0-1.0
    4. Return combined score
    
    Placeholder: Return placeholder score
    """
    # TODO: Real score combination
    return 0.8
```

---

## 3. Search API Routing

### 3.1 Search API Endpoint

**File**: `backend/app/api/search.py` (new)

**Purpose**: Expose search endpoint

**Structure**:
```python
@router.get("/search")
async def search(query: str = Query(...)) -> Dict:
    """
    Search across all chapters.
    
    TODO: Real search logic:
    1. Call search router
    2. Format results
    3. Return response
    
    Placeholder: Return placeholder response
    """
    # TODO: Real search logic
    return {
        "results": [],
        "query": query,
        "total_results": 0
    }
```

---

## 4. Formatter Design

### 4.1 Search Formatter

**File**: `backend/app/ai/formatters/search_formatter.py` (new)

**Purpose**: Format search results

**Structure**:
```python
def normalize_score(score: float) -> float:
    """
    Normalize score to 0.0-1.0 range.
    
    TODO: Real normalization:
    1. Apply min-max scaling
    2. Ensure 0.0-1.0 range
    3. Return normalized score
    
    Placeholder: Return score as-is
    """
    # TODO: Real normalization
    return max(0.0, min(1.0, score))

def format_search_result(chapter_id: int, chunk: Dict, score: float) -> Dict:
    """
    Format search result with chapter title, snippet, score.
    
    TODO: Real formatting:
    1. Get chapter title
    2. Extract snippet
    3. Format result
    4. Return formatted result
    
    Placeholder: Return placeholder result
    """
    # TODO: Real formatting
    return {
        "chapter_id": chapter_id,
        "chapter_title": f"Chapter {chapter_id}",
        "snippet": chunk.get("text", "")[:200],
        "score": score,
        "section_id": chunk.get("section_id", "")
    }
```

---

## 5. Frontend Integration Plan

### 5.1 Search Bar Component

**File**: `frontend/src/components/SearchBar/index.tsx` (update existing or create)

**Purpose**: Search input and submit handler

**Structure**:
```typescript
export default function SearchBar() {
  const [query, setQuery] = useState('');
  
  const handleSearch = async () => {
    // TODO: Call /api/search endpoint
    // TODO: Display results
    console.log('Search query:', query);
  };
  
  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search across all chapters..."
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
}
```

---

## 6. File-by-File Implementation Order

1. `backend/app/ai/search/__init__.py` - Make search a package
2. `backend/app/ai/search/router.py` - Search router
3. `backend/app/ai/search/ranking.py` - Ranking model
4. `backend/app/ai/formatters/search_formatter.py` - Search formatter
5. `backend/app/api/search.py` - Search API endpoint
6. `backend/app/main.py` - Register search router
7. `backend/app/ai/rag/collections.py` - Update with collection list
8. `backend/app/ai/embeddings/embedding_client.py` - Add TODO comment
9. `frontend/src/components/SearchBar/index.tsx` - Update search bar

---

## 7. Constraints

- **NO Real Search Logic**: All implementations must be placeholders
- **Scaffolding Only**: This feature creates structure, not functionality
- **NO Real Ranking**: No real ranking algorithm implementation
- **NO Real Retrieval**: No real multi-chapter retrieval logic

---

## 8. Acceptance Criteria Mapping

| Acceptance Criteria | Implementation Location |
|---------------------|------------------------|
| Single endpoint working | search.py endpoint created |
| All files created | All files created with placeholder logic |
| No real search logic | All functions have TODO comments only |
| Backend builds without error | All imports resolve correctly |
| Frontend search bar renders | SearchBar component updated |

---

## 9. Risk Analysis

**Risk 1**: Search router may conflict with existing routing
- **Mitigation**: Use separate search router, don't modify existing routers

**Risk 2**: Import errors if module structure incorrect
- **Mitigation**: Ensure all `__init__.py` files exist, test imports

**Risk 3**: Frontend search bar may not integrate with UI
- **Mitigation**: Create standalone component, integration in future features

---

## 10. Future Enhancements

- Real search algorithm
- Real ranking algorithm
- Real multi-chapter retrieval
- Search result caching
- Search analytics
- Advanced filtering
- Search suggestions

