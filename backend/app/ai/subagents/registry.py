"""
Subagent Registry

Global registry for mapping (block_type, chapter_id) to subagent classes.
Enables unified routing and easy extension to new chapters.
"""

from typing import Dict, Tuple, Type, Optional, List
from app.ai.subagents.base_agent import BaseAgent

# Global registry: (block_type, chapter_id) -> Subagent class
SUBAGENT_REGISTRY: Dict[Tuple[str, int], Type[BaseAgent]] = {}


def register_subagent(
    block_type: str,
    chapter_id: int,
    subagent_class: Type[BaseAgent]
) -> None:
    """
    Register a subagent for a specific block type and chapter.
    
    Args:
        block_type: Type of AI block (e.g., "ask-question", "explain-like-el10")
        chapter_id: Chapter ID (1, 2, 3, ...)
        subagent_class: Subagent class (must extend BaseAgent)
    
    Example:
        register_subagent("ask-question", 3, Ch3AskQuestionAgent)
    """
    SUBAGENT_REGISTRY[(block_type, chapter_id)] = subagent_class


def get_subagent(
    block_type: str,
    chapter_id: int
) -> Optional[Type[BaseAgent]]:
    """
    Get subagent class for block type and chapter.
    
    Args:
        block_type: Type of AI block
        chapter_id: Chapter ID
    
    Returns:
        Subagent class if registered, None otherwise
    
    Example:
        subagent_class = get_subagent("ask-question", 3)
        if subagent_class:
            subagent = subagent_class()
    """
    return SUBAGENT_REGISTRY.get((block_type, chapter_id))


def list_registered_subagents() -> List[Tuple[str, int]]:
    """
    List all registered (block_type, chapter_id) pairs.
    
    Returns:
        List of (block_type, chapter_id) tuples
    
    Example:
        registered = list_registered_subagents()
        # [("ask-question", 1), ("ask-question", 2), ...]
    """
    return list(SUBAGENT_REGISTRY.keys())


# TODO: Auto-register existing subagents for chapters 1, 2, 3
# This will be done in __init__.py or individual subagent files
# Example:
# from app.ai.subagents.ch3.ask_question_agent import Ch3AskQuestionAgent
# register_subagent("ask-question", 3, Ch3AskQuestionAgent)

