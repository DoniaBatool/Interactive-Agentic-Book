"""
Formatting Skill

Reusable skill for formatting LLM responses for frontend.
Handles different response formats based on block type.
"""

from typing import Dict, Any


def format_response(
    raw_response: Dict[str, Any],
    block_type: str,
    chapter_id: int = None
) -> Dict[str, Any]:
    """
    Response formatting skill blueprint.
    
    Expected Input:
        raw_response: {
            "text": str,                       # Raw LLM text
            "metadata": Dict[str, Any]        # LLM metadata
        }
        block_type: str                        # "ask-question", "explain-like-10", "quiz", "diagram"
    
    Expected Output:
        Formatted response matching block_type:
        - ask-question: {answer: str, sources: List[str], confidence: float}
        - explain-like-10: {explanation: str, examples: List[str], analogies: List[str]}
        - quiz: {questions: List[Question], learning_objectives: List[str]}
        - diagram: {diagram_url: str, metadata: Dict}
    
    TODO: Implement response formatting logic
    TODO: Parse raw LLM response based on block_type
    TODO: Extract structured data from LLM text
    TODO: Format sources, examples, questions, etc. based on block_type
    TODO: Add validation for response structure
    TODO: Add error handling for malformed responses
    
    TODO: Chapter 2 formatting rules
    TODO: If chapter_id == 2:
    TODO:     Apply Chapter 2 formatting rules
    TODO:     Include ROS 2-specific metadata
    TODO:     Format ROS 2 source citations
    TODO:     Format ROS 2 examples and analogies
    TODO: Elif chapter_id == 1:
    TODO:     Apply Chapter 1 formatting rules (existing logic)
    """
    # Placeholder return - no real formatting logic
    return {}

