# Checklists

## Content/Structure
- `/chat` endpoint exists with POST payload (question, filters, stream).
- Retrieval hits Qdrant with top-k and optional filters.
- OpenAI generation returns answer + citations (path/chapter/section, score optional).
- Streaming supported when requested.

## Quality
- Configurable top-k, model, and stream flag defaults.
- Error handling for missing keys; clear messages.
- Logging includes latency and retrieved count.

## Testing
- Manual POST `/chat` returns 200 with answer + citations.
- Streaming tested.
- `npm test` remains green.

