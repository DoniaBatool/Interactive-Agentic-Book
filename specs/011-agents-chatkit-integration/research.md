# Research Notes – Feature 011: Agents/ChatKit Integration

## OpenAI Function Calling

- OpenAI's function calling allows the model to output structured JSON for tool invocation.
- Tools are defined with JSON Schema in the `tools` parameter of chat completions.
- The model returns `tool_calls` in its response when it decides to use a tool.
- After tool execution, results are sent back as `tool` role messages.

## Agent Architecture Patterns

### Option A: Backend-centric Agents (Chosen)
- Agent logic lives entirely in the backend (Python).
- Frontend only switches between `/chat` and `/chat/agent` endpoints.
- Pros: Simpler frontend, full control over agent behavior.
- Cons: Limited client-side customization.

### Option B: Full ChatKit SDK
- Use OpenAI's ChatKit SDK for more complex agent orchestration.
- Would require significant frontend changes.
- Deferred for future enhancement.

## Tool Design: retrieve_book_context

```json
{
  "name": "retrieve_book_context",
  "description": "Search the Physical AI & Humanoid Robotics textbook for relevant content. Use this when the user asks about course topics.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query to find relevant textbook content"
      },
      "chapter_filter": {
        "type": "string",
        "description": "Optional: specific chapter to prioritize (e.g., 'Introduction to Physical AI')"
      }
    },
    "required": ["query"]
  }
}
```

## Qdrant Filtering

- Qdrant supports keyword filtering on payload fields.
- Requires payload indexes for efficient filtering.
- Created indexes for `chapter` and `section` fields.
- Filter syntax: `models.Filter(must=[models.FieldCondition(...)])`

## Response Schema Compatibility

- Both `/chat` and `/chat/agent` return the same `ChatResponse` schema:
  - `answer`: string
  - `citations`: array of Citation objects
  - `stream`: boolean
- Frontend doesn't need to handle different response formats.

## Performance Considerations

- Function calling adds one round-trip to OpenAI API.
- Typical flow: User → OpenAI (decide) → Tool → OpenAI (generate) → Response
- Expected latency increase: 1-2 seconds vs. basic RAG.
- Acceptable trade-off for improved answer quality.

