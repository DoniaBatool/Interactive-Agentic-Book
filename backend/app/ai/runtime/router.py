"""
Runtime Router

Centralized router that routes requests to appropriate chapter runtime.
Uses runtime registry for chapter lookup and calls runtime engine with correct parameters.
"""

from typing import Dict, Any

# TODO: Import runtime registry
# from app.ai.runtime.registry import CHAPTER_RUNTIMES

# TODO: Import runtime engine
# from app.ai.runtime.engine import run_ai_block


async def route(
    chapter_id: int,
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Route request to appropriate chapter runtime.

    Args:
        chapter_id: Chapter identifier (1, 2, or 3)
        block_type: Type of AI block ("ask-question", "explain-like-10", "quiz", "diagram")
        request_data: Request payload matching block type

    Returns:
        Response from runtime engine (placeholder: empty dict)

    Routing Flow (all TODO):
    1. Look up chapter_id in runtime registry
    2. Route to appropriate chapter runtime
    3. Call runtime engine with chapter_id, block_type, request_data
    4. Return response from runtime engine

    TODO: Import runtime registry
    TODO: from app.ai.runtime.registry import CHAPTER_RUNTIMES
    TODO: Look up chapter_id in CHAPTER_RUNTIMES

    TODO: Import runtime engine
    TODO: from app.ai.runtime.engine import run_ai_block
    TODO: Call run_ai_block(block_type, request_data) with chapter_id in request_data

    TODO: Move to dynamic registry later (Phase 2)
    TODO: Replace switch statement with dynamic registry lookup
    TODO: Use runtime objects instead of strings (Phase 2)
    """
    # Placeholder switch logic for chapters 1, 2, 3
    if chapter_id == 1:
        # TODO: Route to Chapter 1 runtime
        # TODO: Call runtime engine with chapter_id=1
        # TODO: result = await run_ai_block(block_type, {**request_data, "chapterId": 1})
        # TODO: return result
        return {}
    elif chapter_id == 2:
        # TODO: Route to Chapter 2 runtime
        # TODO: Call runtime engine with chapter_id=2
        # TODO: result = await run_ai_block(block_type, {**request_data, "chapterId": 2})
        # TODO: return result
        return {}
    elif chapter_id == 3:
        # TODO: Route to Chapter 3 runtime
        # TODO: Call runtime engine with chapter_id=3
        # TODO: result = await run_ai_block(block_type, {**request_data, "chapterId": 3})
        # TODO: return result
        return {}
    else:
        # TODO: Handle unknown chapter
        # TODO: Return error or placeholder response
        # TODO: raise ValueError(f"Unknown chapter_id: {chapter_id}")
        return {}

