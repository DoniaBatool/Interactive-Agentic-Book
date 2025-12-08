# Data Model: Global Platform Stabilization

**Feature**: 056-global-stabilization
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for stabilization system

## Entity Definitions

### 1. AI Block Rules (Configuration Entity)

**Description**: Rules for consistent AI block behavior

**Storage**: Static dictionary in `backend/app/ai/runtime/ai_block_rules.py`

**Structure**:
```python
AI_BLOCK_RULES = {
    "formatting": {
        "markdown": {...},
        "diagrams": {...},
        "quizzes": {...}
    },
    "token_usage": {
        "max_tokens_per_block": 2000,
        "max_context_length": 4000
    },
    "retry_strategy": {
        "max_retries": 3,
        "backoff_delay": 1000
    }
}
```

---

### 2. Chapter Collection (Configuration Entity)

**Description**: Collection names for chapter embeddings

**Storage**: Constants in `backend/app/ai/rag/collections.py`

**Structure**:
```python
CH1_COLLECTION_NAME = "chapter_1_embeddings"
CH2_COLLECTION_NAME = "chapter_2_embeddings"
CH3_COLLECTION_NAME = "chapter_3_embeddings"
```

---

### 3. Routing Score (Processing Entity)

**Description**: Score for chapter routing

**Storage**: In-memory during processing

**Structure**:
```python
RoutingScore = {
    "chapter_id": int,
    "score": float,
    "relevance": float
}
```

---

### 4. Formatting Rules (Configuration Entity)

**Description**: Rules for response formatting

**Storage**: Static dictionary in `backend/app/ai/formatters/response_formatter.py`

**Structure**:
```python
FORMATTING_RULES = {
    "markdown": {...},
    "diagrams": {...},
    "quizzes": {...}
}
```

---

## Relationships

### AI Block → Rules
- One AI block follows one set of rules
- Rules are applied consistently
- Rules can be overridden per chapter (future)

### Chapter → Collection
- One chapter has one collection
- Collections are named consistently
- Collections can be queried together

### Query → Routing Score
- One query generates multiple routing scores
- Scores determine routing
- Highest score wins

---

## Data Flow

### Multi-Chapter Routing Flow
```
Query
  → Generate embedding
  → Score all chapters
  → Select best chapter
  → Route to chapter RAG
  → Return results
```

### Formatting Flow
```
AI Block Response
  → Apply formatting rules
  → Normalize markdown
  → Format diagrams/quizzes
  → Return formatted response
```

### Validation Flow
```
Chapter Content
  → Check AI block consistency
  → Check section ordering
  → Check glossary structure
  → Return validation results
```

---

## Notes

- All data structures are static (not persisted)
- Rules are defined in code, not database
- Future: Database-backed rules
- Future: Dynamic rule assignment
- Future: Rule versioning

