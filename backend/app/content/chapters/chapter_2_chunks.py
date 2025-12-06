"""
Chapter 2 Content Chunks

Provides chapter content chunks for RAG pipeline.
Chunks are used for semantic search and context retrieval.
"""

from typing import List, Dict, Any


def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 2 with metadata.
    
    Args:
        chapter_id: Chapter identifier (default: 2 for Chapter 2)
    
    Returns:
        List of chunk dictionaries with structure:
        [
            {
                "id": str,                    # Unique chunk ID (e.g., "ch2-s1-c0")
                "text": str,                  # Chunk text content
                "chapter_id": 2,              # Chapter identifier
                "section_id": str,            # Section identifier (e.g., "introduction-to-ros2")
                "position": int,              # Position in chapter (0-based)
                "word_count": int,            # Word count
                "metadata": {                 # Additional metadata
                    "heading": str,          # Section heading
                    "type": str,             # "paragraph", "heading", "glossary", etc.
                    "has_diagram": bool,     # True if section has diagram placeholder
                    "has_ai_block": bool     # True if section has AI block
                }
            },
            ...
        ]
    
    TODO: Implement chunking from Chapter 2 MDX content
    TODO: Load Chapter 2 content from frontend/docs/chapters/chapter-2.mdx
    TODO: Implement chunking strategy:
        - Max token size constraints (e.g., 512 tokens per chunk)
        - Semantic segmentation by section
        - Heading-aware slicing (respect H2 boundaries)
        - Overlapping window strategy (e.g., 50 tokens overlap)
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch2-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Cache chunks for performance
    TODO: Include ROS 2-specific metadata (concepts: nodes, topics, services, actions)
    """
    # Placeholder return - no real chunking implementation
    return []
