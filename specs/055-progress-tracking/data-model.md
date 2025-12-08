# Data Model: Chapter Progress Tracking Layer

**Feature**: 055-progress-tracking
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for progress tracking system

## Entity Definitions

### 1. Progress State (Enum)

**Description**: Represents the progress state of a chapter for a user

**Storage**: Enum in `backend/app/progress/models.py`

**Structure**:
```python
class ProgressState(Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
```

**State Meanings**:
- `NOT_STARTED`: Chapter has not been started by user
- `IN_PROGRESS`: User has started reading the chapter
- `COMPLETED`: User has completed the chapter

---

### 2. Progress Record (Primary Entity)

**Description**: Represents a single progress record for a user-chapter pair

**Storage**: Future database (not persisted in scaffolding)

**Structure**:
```python
@dataclass
class ProgressRecord:
    user_id: str              # User identifier
    chapter_id: int           # Chapter number (1, 2, 3, ...)
    state: ProgressState      # Current progress state
    updated_at: datetime      # Last update timestamp
```

**Example**:
```python
ProgressRecord(
    user_id="user_123",
    chapter_id=1,
    state=ProgressState.COMPLETED,
    updated_at=datetime(2025, 1, 27, 12, 0, 0)
)
```

---

### 3. Progress List (Data Transfer Object)

**Description**: List of progress records for a user

**Storage**: Transient (returned via API response)

**Structure**:
```python
ProgressList = {
    "progress": List[ProgressRecord]
}
```

**Example**:
```json
{
  "progress": [
    {
      "user_id": "user_123",
      "chapter_id": 1,
      "state": "completed",
      "updated_at": "2025-01-27T00:00:00Z"
    },
    {
      "user_id": "user_123",
      "chapter_id": 2,
      "state": "in_progress",
      "updated_at": "2025-01-27T01:00:00Z"
    }
  ]
}
```

---

## Relationships

### User → Progress Records
- One user can have multiple progress records
- One progress record belongs to one user
- One progress record per user-chapter pair

### Chapter → Progress Records
- One chapter can have multiple progress records (from different users)
- One progress record belongs to one chapter

### Progress Record → Progress State
- One progress record has one state
- State can change over time (NOT_STARTED → IN_PROGRESS → COMPLETED)

---

## Data Flow

### Mark Started Flow
```
Frontend calls updateProgress(chapterId, "in_progress")
  → POST /progress/{chapter_id}/start
    → Extract user_id from request.state (placeholder)
    → Call service.mark_started(user_id, chapter_id)
    → Return ProgressRecord with IN_PROGRESS state
```

### Mark Completed Flow
```
Frontend calls updateProgress(chapterId, "completed")
  → POST /progress/{chapter_id}/complete
    → Extract user_id from request.state (placeholder)
    → Call service.mark_completed(user_id, chapter_id)
    → Return ProgressRecord with COMPLETED state
```

### Get Progress Flow
```
Frontend calls getProgress()
  → GET /progress/
    → Extract user_id from request.state (placeholder)
    → Call service.get_progress(user_id)
    → Return list of ProgressRecords
```

---

## Notes

- All data structures are transient (no persistence in scaffolding)
- Progress records are not persisted
- Future: Database-backed persistence
- Future: Progress history tracking
- Future: Progress analytics

