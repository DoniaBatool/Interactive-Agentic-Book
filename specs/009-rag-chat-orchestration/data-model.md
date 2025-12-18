# Data Model: RAG Chat Orchestration

Conceptual entities:
- **ChatRequest**: question, filters (chapter, section), stream.
- **RetrievedChunk**: id, text, metadata (path, chapter, section), score.
- **ChatResponse**: answer, citations (list of metadata), stream flag.

