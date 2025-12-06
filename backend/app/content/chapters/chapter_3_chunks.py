"""
Chapter 3 Content Chunks

Provides chapter content chunks for RAG pipeline.
Chunks are used for semantic search and context retrieval.
"""

from typing import List, Dict, Any


def get_chapter_chunks(chapter_id: int = 3) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 3 with metadata.
    
    Chunks respect chunk markers (CHUNK: START / CHUNK: END).
    
    Args:
        chapter_id: Chapter identifier (default: 3 for Chapter 3)
    
    Returns:
        List of chunk dictionaries with structure:
        [
            {
                "id": str,                    # Unique chunk ID (e.g., "ch3-s1-c0")
                "text": str,                  # Chunk text content
                "chapter_id": 3,              # Chapter identifier
                "section_id": str,            # Section identifier (e.g., "what-is-perception-in-physical-ai")
                "position": int,              # Position in chapter (0-based)
                "word_count": int,            # Word count
                "metadata": {                 # Additional metadata
                    "heading": str,          # Section heading
                    "type": str,             # "paragraph", "heading", "glossary", etc.
                    "has_diagram": bool,     # True if section has diagram placeholder
                    "has_ai_block": bool,    # True if section has AI block
                    "chunk_markers": bool     # True if chunk has START/END markers
                }
            },
            ...
        ]
    
    TODO: Implement chunking from Chapter 3 MDX content
    TODO: Load Chapter 3 content from frontend/docs/chapters/chapter-3.mdx
    TODO: Implement chunking strategy:
        - Respect chunk markers (CHUNK: START / CHUNK: END)
        - Section-based logical chunks (each H2 section is a natural chunk boundary)
        - Semantic segmentation by section
        - Heading-aware slicing (respect H2 boundaries)
        - Max token size constraints (e.g., 512 tokens per chunk)
        - Overlapping window strategy (e.g., 50 tokens overlap)
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch3-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Include Physical AI-specific metadata (concepts: perception, sensors, vision, signal processing)
    TODO: Include chunk marker metadata (chunk_markers: bool flag)
    TODO: Future: Generate embeddings for each chunk using embedding model
    TODO: Future: Store embeddings in Qdrant collection "chapter_3"
    TODO: Future: Include chunk metadata for semantic search
    """
    # Placeholder return - no real chunking implementation
    return []
