# Checklists

## Content/Structure
- Health route present.
- Settings class reads env vars (OpenAI, Qdrant, Postgres, CORS).
- Folder layout created for api/core/models/services/tests.
- README documents run and env vars.

## Quality
- Minimal deps pinned.
- CORS placeholder for localhost.
- Clean startup with missing non-critical keys handled.

## Testing
- Backend starts and `/health` returns 200.
- `npm test` remains green.

