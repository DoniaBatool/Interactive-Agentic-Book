# Data Model: RAG Ingestion & Chunking

Conceptual entities:
- **DocumentChunk**: id, text, embedding, metadata (path, chapter, section).
- **IngestionResult**: files_processed, chunks_written, collection.
- **Settings**: embedding model/dim, Qdrant collection, paths.

