# Qdrant Vector Database Configuration

This directory contains configuration placeholders for **Qdrant**, the vector database that will power the RAG (Retrieval-Augmented Generation) chatbot.

## Status: Placeholder

⚠️ **This is a placeholder for future RAG feature implementation.**

No actual Qdrant integration exists in the base project initialization phase. This directory structure is created to support future development according to **Constitution Principle III: RAG-First Chatbot Architecture**.

## Future Implementation

When the RAG chatbot feature is implemented, this directory will contain:

### Configuration Files

- **`qdrant-config.yaml`**: Collection configuration (vector dimensions, distance metric, indexing)
- **`schema.json`**: Payload schema for metadata fields
- **`docker-compose.qdrant.yml`**: Qdrant container configuration

### Purpose

The Qdrant vector database will be used for:

1. **Content Storage**: Store textbook content as embeddings
2. **Semantic Search**: Find relevant content based on user queries
3. **RAG Pipeline**: Retrieve context for GPT-4o chatbot responses
4. **Multilingual Support**: Store both English and Urdu content

### Architecture

```
User Query
    ↓
[OpenAI text-embedding-3-large]
    ↓
Query Vector (3072 dimensions)
    ↓
[Qdrant Semantic Search]
    ↓
Top K Relevant Chunks
    ↓
[GPT-4o with Context]
    ↓
Chatbot Response
```

### Collection Schema (Planned)

**Collection Name**: `textbook_embeddings`

**Vector Configuration**:
- Dimensions: 3072 (OpenAI text-embedding-3-large)
- Distance: Cosine similarity
- HNSW index for fast search

**Metadata Fields**:
- `chapter`: Chapter number/name
- `section`: Section identifier
- `language`: "en" (English) or "ur" (Urdu)
- `content_type`: "text", "code", "image_caption", etc.
- `source_file`: Original markdown file path
- `embedding_model`: "text-embedding-3-large"
- `created_at`: Timestamp

### Setup (When Implemented)

1. **Create Qdrant Cloud Instance**:
   ```bash
   # Sign up at https://cloud.qdrant.io/
   # Create a cluster
   # Copy URL and API key to .env
   ```

2. **Or Run Locally with Docker**:
   ```bash
   docker run -p 6333:6333 qdrant/qdrant
   ```

3. **Configure Environment**:
   ```bash
   # In .env file
   QDRANT_URL=https://your-instance.qdrant.io:6333
   QDRANT_API_KEY=your-api-key-here
   ```

4. **Initialize Collection**:
   ```python
   # Will be implemented in app/services/qdrant_client.py
   from qdrant_client import QdrantClient
   from qdrant_client.models import Distance, VectorParams
   
   client = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)
   
   client.create_collection(
       collection_name="textbook_embeddings",
       vectors_config=VectorParams(size=3072, distance=Distance.COSINE)
   )
   ```

## References

- **Qdrant Documentation**: https://qdrant.tech/documentation/
- **OpenAI Embeddings**: https://platform.openai.com/docs/guides/embeddings
- **RAG Architecture**: https://www.pinecone.io/learn/retrieval-augmented-generation/
- **Constitution Principle III**: See `.specify/memory/constitution.md`

## Next Steps

1. Implement RAG chatbot feature (see `specs/` for feature specification)
2. Create Qdrant client wrapper (`backend/app/services/qdrant_client.py`)
3. Implement content ingestion pipeline
4. Build chat API endpoint with RAG
5. Test semantic search quality

---

**Note**: This infrastructure is prepared as part of **Feature 001 - Base Project Initialization**. Actual implementation will happen in a future feature following the Spec-Driven Development methodology.
