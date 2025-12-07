"""
Chapter Metadata Registry

Registry mapping chapter IDs to metadata modules.
Provides centralized metadata access for all chapters.
"""

from typing import Dict, Any

# Import chapter metadata modules
from app.content.chapters import chapter_1
from app.content.chapters import chapter_2
from app.content.chapters import chapter_3

# Chapter Metadata Registry
# Maps chapter IDs to metadata dictionaries

CHAPTER_METADATA_REGISTRY = {
    1: chapter_1.CHAPTER_METADATA,
    2: chapter_2.CHAPTER_METADATA,
    3: chapter_3.CHAPTER_METADATA
}


def get_chapter_metadata(id: int) -> Dict[str, Any]:
    """
    Get metadata for a specific chapter.

    Args:
        id: Chapter identifier (1, 2, or 3)

    Returns:
        Dictionary with chapter metadata (placeholder: empty dict if not found)

    TODO: Add validation for chapter ID
    TODO: if id not in CHAPTER_METADATA_REGISTRY:
    TODO:     raise ValueError(f"Unknown chapter_id: {id}")

    TODO: Add metadata caching (if needed)
    TODO: Add metadata transformation (if needed)
    """
    return CHAPTER_METADATA_REGISTRY.get(id, {})

