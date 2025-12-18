# Research Notes: RAG Ingestion & Chunking

Choices:
- Embeddings: OpenAI `text-embedding-3-small` (dim 1536) by default.
- Vector DB: Qdrant collection `textbook-chunks`, upsert per rerun.
- Chunking: paragraph-based; tiktoken optional for length control.
- Metadata: include path, chapter, section heading where found.

