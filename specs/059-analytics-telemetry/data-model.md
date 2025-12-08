# Data Model: Analytics & Telemetry Scaffolding

**Feature**: 059-analytics-telemetry
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for analytics system

## Entity Definitions

### 1. Analytics Event (Primary Entity)

**Description**: Represents a single analytics event

**Storage**: Not persisted (placeholder)

**Structure**:
```python
AnalyticsEvent = {
    "event_type": str,        # "ai_block_used", "chapter_visit", "error_event"
    "payload": Dict[str, Any], # Event-specific data
    "timestamp": str          # ISO format timestamp
}
```

**Example**:
```python
{
    "event_type": "ai_block_used",
    "payload": {
        "user_id": "user_123",
        "chapter_id": 1,
        "section_id": "what-is-physical-ai",
        "block_type": "ask-question",
        "query": "What is Physical AI?"
    },
    "timestamp": "2025-01-27T00:00:00Z"
}
```

---

### 2. Event Log Request (Input Entity)

**Description**: Request to log an event

**Storage**: Transient (from API request)

**Structure**:
```python
EventLogRequest = {
    "event_type": str,
    "payload": Dict[str, Any]
}
```

---

### 3. Event Log Response (Output Entity)

**Description**: Response from event logging

**Storage**: Transient (returned via API response)

**Structure**:
```python
EventLogResponse = {
    "message": str,
    "event_type": str,
    "timestamp": str
}
```

---

### 4. Telemetry Health Response (Output Entity)

**Description**: Telemetry system health status

**Storage**: Transient (returned via API response)

**Structure**:
```python
TelemetryHealthResponse = {
    "status": str,           # "healthy", "degraded", "unhealthy"
    "message": str,
    "events_logged": int     # Placeholder count
}
```

---

## Relationships

### Event Type → Payload
- One event type has one payload structure
- Payload structure varies by event type
- Payload contains event-specific data

### Event → Timestamp
- One event has one timestamp
- Timestamp is generated on event creation
- Timestamp is ISO format

---

## Data Flow

### Event Logging Flow
```
User Action / System Event
  → EventLogger.log(event_type, payload)
    → Create AnalyticsEvent
    → Generate timestamp
    → Return (placeholder, no persistence)
```

### Telemetry API Flow
```
API Request
  → POST /api/telemetry/log
    → EventLogger.log()
    → Return EventLogResponse (placeholder)
  
  → GET /api/telemetry/health
    → Return TelemetryHealthResponse (placeholder)
```

### Integration Flow
```
AI Block Endpoint
  → Process request
  → EventLogger.log("ai_block_used", {...})
  → Return response
```

---

## Notes

- All data structures are transient (not persisted)
- Events are not stored in database (placeholder)
- Future: Database-backed event storage
- Future: External service integration
- Future: Event aggregation and analytics
