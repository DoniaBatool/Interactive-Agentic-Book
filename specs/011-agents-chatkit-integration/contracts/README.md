# API Contracts – Feature 011: Agents/ChatKit Integration

## Endpoint: POST /chat/agent

### Request

```json
{
  "question": "What is Physical AI?",
  "filters": {
    "chapter": "Introduction to Physical AI",
    "section": null
  },
  "stream": false
}
```

### Response (Non-streaming)

```json
{
  "answer": "Physical AI refers to artificial intelligence systems that interact with the physical world through sensors and actuators...",
  "citations": [
    {
      "path": "docs/modules/intro.md",
      "chapter": "Introduction to Physical AI",
      "section": "What is Physical AI?",
      "score": 0.92
    }
  ],
  "stream": false
}
```

### Response (Streaming)

SSE stream with events:
- `event: metadata` - Contains citations
- `event: token` - Contains text chunk
- `event: done` - Signals completion
- `event: error` - Contains error details

## OpenAI Tool Contract

### Tool Definition

```json
{
  "type": "function",
  "function": {
    "name": "retrieve_book_context",
    "description": "Search the textbook for relevant content",
    "parameters": {
      "type": "object",
      "properties": {
        "query": {"type": "string"},
        "chapter_filter": {"type": "string"}
      },
      "required": ["query"]
    }
  }
}
```

### Tool Call (from OpenAI)

```json
{
  "id": "call_abc123",
  "type": "function",
  "function": {
    "name": "retrieve_book_context",
    "arguments": "{\"query\": \"Physical AI\", \"chapter_filter\": \"Introduction to Physical AI\"}"
  }
}
```

### Tool Result (to OpenAI)

```json
{
  "role": "tool",
  "tool_call_id": "call_abc123",
  "content": "Retrieved context from textbook:\n\n1. Physical AI refers to...\n2. Key components include..."
}
```

