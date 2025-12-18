# Checklists

## Content/Structure
- Ingestion script/entry present.
- Chunking includes metadata (path, chapter, section when available).
- Qdrant collection creation/upsert implemented.
- README documents env and run commands.

## Quality
- Idempotent rerun (upsert).
- Embedding model/dim configurable.
- Handles missing keys gracefully (dry-run or clear error).

## Testing
- Ingestion run locally (or dry-run) and logs counts.
- `npm test` remains green.

