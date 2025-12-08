# Implementation Plan: Analytics & Telemetry Scaffolding Layer

**Branch**: `059-analytics-telemetry` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature implements complete scaffolding for analytics and telemetry. It introduces event logger, analytics models, telemetry router, and integration with AI blocks. **All implementations are scaffolding only—no real tracking, no real database, no real external services.**

**Primary Deliverable**: Complete analytics scaffolding structure
**Validation**: All analytics modules exist, API endpoints return placeholders, backend starts

---

## 1. Module Breakdown

### 1.1 Analytics Module Structure

```
backend/app/analytics/
├── __init__.py              # Package init
├── event_logger.py          # EventLogger class
├── analytics_models.py      # AnalyticsEvent class
└── telemetry_router.py      # Telemetry API router
```

---

### 1.2 File Responsibilities

**event_logger.py**:
- EventLogger class
- log() method
- Event type definitions
- Placeholder logging logic

**analytics_models.py**:
- AnalyticsEvent class
- Event structure definition
- Placeholder model

**telemetry_router.py**:
- Telemetry API router
- POST /api/telemetry/log endpoint
- GET /api/telemetry/health endpoint
- Request/response models

---

## 2. Analytics Event Flow

### 2.1 Event Logging Flow

```
User Action / System Event
  → EventLogger.log(event_type, payload)
    → Create AnalyticsEvent instance
    → Generate timestamp
    → Log event (placeholder, no persistence)
    → Return None
```

---

### 2.2 Event Types

**ai_block_used**:
- Triggered when AI block is used
- Payload: user_id, chapter_id, section_id, block_type, query

**chapter_visit**:
- Triggered when chapter is visited
- Payload: user_id, chapter_id, timestamp

**error_event**:
- Triggered when error occurs
- Payload: error_type, error_message, chapter_id (optional), section_id (optional)

---

## 3. Telemetry API Flow

### 3.1 POST /api/telemetry/log

**Flow**:
```
API Request
  → Extract event_type and payload
  → Call EventLogger.log(event_type, payload)
  → Return EventLogResponse (placeholder)
```

---

### 3.2 GET /api/telemetry/health

**Flow**:
```
API Request
  → Return TelemetryHealthResponse (placeholder)
  → Status: "healthy"
  → Events logged: 0 (placeholder)
```

---

## 4. Integration Points with Runtime + AI Blocks

### 4.1 AI Blocks Integration

**File**: `backend/app/api/ai_blocks.py`

**Integration Points**:
- ask_question endpoint: Log "ai_block_used" event
- explain_like_10 endpoint: Log "ai_block_used" event
- quiz endpoint: Log "ai_block_used" event
- diagram endpoint: Log "ai_block_used" event

**Implementation**:
```python
from app.analytics.event_logger import event_logger

# In each AI block endpoint:
event_logger.log("ai_block_used", {
    "user_id": "user_123",  # Placeholder
    "chapter_id": chapter_id,
    "section_id": section_id,
    "block_type": "ask-question",
    "query": request.question
})
```

---

### 4.2 Chapter Visit Integration (Future)

**File**: `backend/app/api/chapters.py` (future integration)

**Integration Points**:
- get_chapter endpoint: Log "chapter_visit" event

**Implementation**:
```python
# TODO: Add chapter visit tracking
event_logger.log("chapter_visit", {
    "user_id": "user_123",  # Placeholder
    "chapter_id": chapter_id
})
```

---

### 4.3 Error Event Integration (Future)

**File**: Error handlers (future integration)

**Integration Points**:
- Global error handler: Log "error_event"

**Implementation**:
```python
# TODO: Add error event tracking
event_logger.log("error_event", {
    "error_type": "ValueError",
    "error_message": str(e),
    "chapter_id": chapter_id
})
```

---

## 5. Non-Functional Constraints

### 5.1 No Database

- Events are not persisted
- No database models
- No database connections
- Placeholder storage only

---

### 5.2 No External APIs

- No external service integration
- No third-party analytics services
- No telemetry aggregation
- Placeholder endpoints only

---

### 5.3 Pure Scaffolding Only

- No real tracking logic
- No real event processing
- No real analytics
- Structure for future implementation

---

## 6. File-by-File Implementation Order

1. `backend/app/analytics/__init__.py` - Package init
2. `backend/app/analytics/analytics_models.py` - AnalyticsEvent class
3. `backend/app/analytics/event_logger.py` - EventLogger class
4. `backend/app/analytics/telemetry_router.py` - Telemetry router
5. `backend/app/main.py` - Register telemetry router
6. `backend/app/api/ai_blocks.py` - Add EventLogger.log() calls
7. `specs/059-analytics-telemetry/contracts/telemetry-api.yaml` - API contract

---

## 7. Constraints

- **NO Real Tracking**: All implementations must be placeholders
- **NO Database**: No real event storage
- **NO External Services**: No real external API integration
- **Scaffolding Only**: This feature creates structure, not functionality

---

## 8. Acceptance Criteria Mapping

| Acceptance Criteria | Implementation Location |
|---------------------|------------------------|
| All modules created and backend compiles | All files created with placeholder logic |
| API endpoints return placeholder JSON | All endpoints return placeholders |
| No actual telemetry storage | No database logic implemented |
| No external services integrated | No external API calls |

---

## 9. Risk Analysis

**Risk 1**: EventLogger calls may slow down AI block endpoints
- **Mitigation**: Use placeholder logic, no real processing

**Risk 2**: Import errors if module structure incorrect
- **Mitigation**: Ensure all `__init__.py` files exist, test imports

**Risk 3**: Integration may break existing AI block endpoints
- **Mitigation**: Add EventLogger calls carefully, test endpoints still work

---

## 10. Future Enhancements

- Real event tracking
- Database-backed storage
- External service integration
- Analytics processing
- Telemetry aggregation
- Real-time dashboards
- Event analytics
