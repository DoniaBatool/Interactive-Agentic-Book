"""
CLI Indexer for Chapter Content

Command-line script to index chapter content into Qdrant vector database.
Reads chapter chunks, generates embeddings, and upserts them into Qdrant.
"""

import asyncio
import argparse
import sys
from typing import Optional

from app.ai.rag.pipeline import embed_chapter_content
from app.ai.rag.qdrant_store import create_collection
from app.config.settings import settings


async def index_chapter(chapter_id: int, create_col: bool = True) -> bool:
    """
    Index a chapter's content into Qdrant.
    
    Args:
        chapter_id: The ID of the chapter to index (1, 2, or 3)
        create_col: Whether to create the collection if it doesn't exist
    
    Returns:
        True if successful, False otherwise
    """
    print(f"Starting indexing for Chapter {chapter_id}...")
    
    # Determine collection name
    collection_name = None
    if chapter_id == 1:
        collection_name = settings.qdrant_collection_ch1 or "chapter_1"
    elif chapter_id == 2:
        collection_name = settings.qdrant_collection_ch2 or "chapter_2"
    elif chapter_id == 3:
        collection_name = settings.qdrant_collection_ch3 or "chapter_3"
    else:
        print(f"Error: Invalid chapter ID: {chapter_id}. Must be 1, 2, or 3.")
        return False
    
    # Create collection if requested
    if create_col:
        print(f"Creating Qdrant collection '{collection_name}' if it doesn't exist...")
        vector_size = 1536  # Default for text-embedding-3-small
        success = await create_collection(collection_name, vector_size=vector_size)
        if not success:
            print(f"Warning: Failed to create collection '{collection_name}'. It may already exist.")
    
    # Embed and upsert chapter content
    print(f"Embedding and upserting Chapter {chapter_id} content...")
    success = await embed_chapter_content(chapter_id)
    
    if success:
        print(f"Successfully indexed Chapter {chapter_id} into Qdrant collection '{collection_name}'.")
    else:
        print(f"Error: Failed to index Chapter {chapter_id}.")
    
    return success


def main():
    """
    Main entry point for CLI indexer.
    """
    parser = argparse.ArgumentParser(
        description="Index chapter content into Qdrant vector database"
    )
    parser.add_argument(
        "--chapter-id",
        type=int,
        required=True,
        choices=[1, 2, 3],
        help="Chapter ID to index (1, 2, or 3)"
    )
    parser.add_argument(
        "--no-create-collection",
        action="store_true",
        help="Skip collection creation (assume collection already exists)"
    )
    
    args = parser.parse_args()
    
    # Run async indexing
    create_col = not args.no_create_collection
    success = asyncio.run(index_chapter(args.chapter_id, create_col=create_col))
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

