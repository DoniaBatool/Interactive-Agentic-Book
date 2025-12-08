"""
Search Result Formatter

Placeholder formatters for search result formatting.
All formatting logic is placeholder with TODO comments for future implementation.

TODO: Real formatting logic will be implemented in a future feature.
"""

from typing import Dict, Any


def normalize_score(score: float) -> float:
    """
    Normalize score to 0.0-1.0 range.
    
    Args:
        score: Raw score (may be outside 0.0-1.0 range)
        
    Returns:
        Normalized score (0.0 to 1.0)
        
    TODO: Real normalization:
    1. Apply min-max scaling
    2. Ensure 0.0-1.0 range
    3. Handle edge cases (negative scores, scores > 1.0)
    4. Return normalized score
    
    Placeholder: Return score as-is (clamped to 0.0-1.0)
    """
    # TODO: Real normalization
    # # Min-max scaling
    # min_score = 0.0  # Would need to track min score across all results
    # max_score = 1.0  # Would need to track max score across all results
    # 
    # if max_score == min_score:
    #     return 0.0
    # 
    # normalized = (score - min_score) / (max_score - min_score)
    # return max(0.0, min(1.0, normalized))
    
    # Placeholder: Return score as-is (clamped to 0.0-1.0)
    return max(0.0, min(1.0, score))


def format_search_result(chapter_id: int, chunk: Dict[str, Any], score: float) -> Dict[str, Any]:
    """
    Format search result with chapter title, snippet, score.
    
    Args:
        chapter_id: Chapter number (1, 2, 3)
        chunk: Chunk data dictionary with text and metadata
        score: Relevance score (0.0-1.0)
        
    Returns:
        Formatted search result dictionary:
        {
            "chapter_id": int,
            "chapter_title": str,
            "snippet": str,
            "score": float,
            "section_id": str
        }
        
    TODO: Real formatting:
    1. Get chapter title from metadata
    2. Extract snippet from chunk text (max 200 chars)
    3. Normalize score
    4. Format result
    5. Return formatted result
    
    Placeholder: Return placeholder result
    """
    # TODO: Real formatting
    # from app.content.chapters.registry import get_chapter_metadata
    # 
    # # Get chapter title
    # metadata = get_chapter_metadata(chapter_id)
    # chapter_title = metadata.get("title", f"Chapter {chapter_id}")
    # 
    # # Extract snippet
    # chunk_text = chunk.get("text", "")
    # snippet = chunk_text[:200] + "..." if len(chunk_text) > 200 else chunk_text
    # 
    # # Normalize score
    # normalized_score = normalize_score(score)
    # 
    # # Format result
    # return {
    #     "chapter_id": chapter_id,
    #     "chapter_title": chapter_title,
    #     "snippet": snippet,
    #     "score": normalized_score,
    #     "section_id": chunk.get("section_id", ""),
    #     "chunk_id": chunk.get("id", "")
    # }
    
    # Placeholder: Return placeholder result
    return {
        "chapter_id": chapter_id,
        "chapter_title": f"Chapter {chapter_id}",
        "snippet": chunk.get("text", "")[:200] if chunk.get("text") else "Placeholder snippet...",
        "score": normalize_score(score),
        "section_id": chunk.get("section_id", "")
    }

