# Data Model: Learner Support System (LSS)

**Feature**: 058-learner-support-system
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for LSS system

## Entity Definitions

### 1. Hint Request (Input Entity)

**Description**: Request for a context-aware hint

**Storage**: Transient (from API request)

**Structure**:
```python
HintRequest = {
    "chapter_id": int,
    "section_id": str,
    "user_state": Optional[Dict]  # Current learning state
}
```

---

### 2. Hint Response (Output Entity)

**Description**: Hint response with hint text and type

**Storage**: Transient (returned via API response)

**Structure**:
```python
HintResponse = {
    "hint": str,              # Hint text
    "hint_type": str,         # "concept", "example", "definition"
    "chapter_id": int,
    "section_id": str
}
```

---

### 3. Summary Request (Input Entity)

**Description**: Request for a section summary

**Storage**: Transient (from API request)

**Structure**:
```python
SummaryRequest = {
    "chapter_id": int,
    "section_id": str
}
```

---

### 4. Summary Response (Output Entity)

**Description**: Summary response with summary text

**Storage**: Transient (returned via API response)

**Structure**:
```python
SummaryResponse = {
    "summary": str,           # Summary text (2-3 sentences)
    "chapter_id": int,
    "section_id": str,
    "summary_length": int     # Length in characters
}
```

---

### 5. Progress Update Request (Input Entity)

**Description**: Request to mark section as complete

**Storage**: Transient (from API request)

**Structure**:
```python
ProgressUpdateRequest = {
    "user_id": str,
    "chapter_id": int,
    "section_id": str
}
```

---

### 6. Section Status (Output Entity)

**Description**: Status of a section for a user

**Storage**: Transient (returned via API response)

**Structure**:
```python
SectionStatus = {
    "section_id": str,
    "status": str,            # "not_started", "in_progress", "completed"
    "completed_at": Optional[str]  # ISO datetime
}
```

---

### 7. Progress Response (Output Entity)

**Description**: Complete progress response for a user-chapter pair

**Storage**: Transient (returned via API response)

**Structure**:
```python
ProgressResponse = {
    "user_id": str,
    "chapter_id": int,
    "sections": List[SectionStatus]
}
```

---

## Relationships

### User → Progress
- One user can have multiple progress records
- One progress record belongs to one user
- One progress record per user-chapter-section triple

### Chapter → Hints/Summaries
- One chapter can have multiple hints/summaries
- One hint/summary belongs to one chapter-section pair

### Section → Hint/Summary
- One section can have multiple hints (different types)
- One section has one summary

---

## Data Flow

### Hint Flow
```
User Request
  → POST /api/lss/hint
    → HintEngine.get_hint(chapter_id, section_id, user_state)
    → Return HintResponse (placeholder)
```

### Summary Flow
```
User Request
  → POST /api/lss/summary
    → SummaryEngine.summarize_section(chapter_id, section_id)
    → Return SummaryResponse (placeholder)
```

### Progress Flow
```
User Request
  → POST /api/lss/progress/update
    → ProgressTracker.mark_section_complete(user_id, chapter_id, section_id)
    → Return success response (placeholder)
  
  → GET /api/lss/progress/{user_id}/{chapter_id}
    → ProgressTracker.get_section_status(user_id, chapter_id)
    → Return ProgressResponse (placeholder)
```

---

## Notes

- All data structures are transient (not persisted)
- Progress is not stored in database (placeholder)
- Hints and summaries are generated on-demand (placeholder)
- Future: Database-backed progress
- Future: Cached hints and summaries
- Future: Real AI-generated content
