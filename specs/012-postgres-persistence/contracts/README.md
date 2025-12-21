# API Contracts – Feature 012: Postgres Persistence

## Endpoint: GET /chat/history

### Request

```
GET /chat/history?session_id=550e8400-e29b-41d4-a716-446655440000&chapter=Introduction%20to%20Physical%20AI
```

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| session_id | string | Yes | UUID session identifier |
| chapter | string | No | Filter by chapter name |
| limit | int | No | Max messages to return (default: 100) |
| offset | int | No | Pagination offset (default: 0) |

### Response

```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "chapter": "Introduction to Physical AI",
  "messages": [
    {
      "id": 1,
      "role": "user",
      "content": "What is Physical AI?",
      "citations": null,
      "created_at": "2025-12-19T12:00:00Z"
    },
    {
      "id": 2,
      "role": "assistant",
      "content": "Physical AI refers to artificial intelligence systems that interact with the physical world...",
      "citations": [
        {
          "path": "docs/modules/intro.md",
          "chapter": "Introduction to Physical AI",
          "section": "What is Physical AI?",
          "score": 0.92
        }
      ],
      "created_at": "2025-12-19T12:00:05Z"
    }
  ],
  "total": 2
}
```

---

## Endpoint: DELETE /chat/history

### Request

```
DELETE /chat/history?session_id=550e8400-e29b-41d4-a716-446655440000
```

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| session_id | string | Yes | UUID session identifier |
| chapter | string | No | Only clear specific chapter (optional) |

### Response

```json
{
  "deleted": 15,
  "message": "Chat history cleared successfully"
}
```

---

## Updated: POST /chat/agent

### Request Headers

```
Content-Type: application/json
X-Session-ID: 550e8400-e29b-41d4-a716-446655440000
```

### Request Body

```json
{
  "question": "What is Physical AI?",
  "filters": {
    "chapter": "Introduction to Physical AI"
  },
  "stream": false
}
```

### Response

Same as before - messages are automatically saved to database.

---

## Frontend Session Management

### localStorage Key

```
rag-chat-session-id
```

### Value Format

```
550e8400-e29b-41d4-a716-446655440000
```

### Generation

```typescript
const getSessionId = (): string => {
  let sessionId = localStorage.getItem('rag-chat-session-id');
  if (!sessionId) {
    sessionId = crypto.randomUUID();
    localStorage.setItem('rag-chat-session-id', sessionId);
  }
  return sessionId;
};
```

