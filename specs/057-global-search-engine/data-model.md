# Data Model: Global Search Engine

**Feature**: 057-global-search-engine
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for search system

## Entity Definitions

### 1. Search Query (Input Entity)

**Description**: User search query

**Storage**: Transient (from API request)

**Structure**:
```python
SearchQuery = {
    "query": str,  # User search text
    "limit": Optional[int]  # Max results (default: 10)
}
```

---

### 2. Search Result (Output Entity)

**Description**: Single search result from a chapter

**Storage**: Transient (returned via API response)

**Structure**:
```python
SearchResult = {
    "chapter_id": int,        # Chapter number
    "chapter_title": str,      # Chapter title
    "snippet": str,            # Text snippet
    "score": float,            # Relevance score (0.0-1.0)
    "section_id": str,         # Section identifier
    "chunk_id": Optional[str]  # Chunk identifier
}
```

---

### 3. Chapter Score (Processing Entity)

**Description**: Score for a chapter in search results

**Storage**: In-memory during processing

**Structure**:
```python
ChapterScore = {
    "chapter_id": int,
    "score": float,
    "embedding_score": float,
    "bm25_score": float,
    "combined_score": float
}
```

---

### 4. Search Response (Output Entity)

**Description**: Complete search response

**Storage**: Transient (returned via API response)

**Structure**:
```python
SearchResponse = {
    "results": List[SearchResult],
    "query": str,
    "total_results": int
}
```

---

## Relationships

### Query → Results
- One query generates multiple results
- Results are ranked by score
- Results are limited to top N

### Chapter → Results
- One chapter can have multiple results
- Results are scored independently
- Results are aggregated and ranked

### Score → Ranking
- One score determines ranking position
- Higher scores rank higher
- Scores are normalized to 0.0-1.0

---

## Data Flow

### Search Flow
```
User Query
  → Generate embedding
  → Search all chapter collections
  → Score results
  → Rank results
  → Format results
  → Return SearchResponse
```

### Ranking Flow
```
Search Results
  → Calculate embedding similarity
  → Calculate BM25 score
  → Combine scores
  → Normalize scores
  → Sort by score
  → Return top N results
```

### Formatting Flow
```
Raw Results
  → Extract snippet
  → Normalize score
  → Add chapter context
  → Format as SearchResult
  → Return formatted results
```

---

## Notes

- All data structures are transient (not persisted)
- Search results are computed on-demand
- Scores are calculated during search
- Future: Search result caching
- Future: Search analytics

