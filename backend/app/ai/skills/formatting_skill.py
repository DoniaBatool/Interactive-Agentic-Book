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
    
    Real implementation: Parse and format LLM responses for frontend.
    """
    text = raw_response.get("text", "")
    
    if block_type == "ask-question":
        # Extract answer and sources (simple parsing)
        # TODO: Use structured output or better parsing
        return {
            "answer": text,
            "sources": [],  # TODO: Extract from text or context
            "confidence": 0.8  # TODO: Calculate based on context relevance
        }
    elif block_type == "explain-like-10":
        # Extract explanation, examples, analogies (simple parsing)
        # TODO: Use structured output or better parsing
        return {
            "explanation": text,
            "examples": [],  # TODO: Extract from text
            "analogies": []  # TODO: Extract from text
        }
    elif block_type == "quiz":
        # Extract quiz questions (simple parsing)
        # TODO: Use structured output or better parsing
        return {
            "quiz_title": f"Chapter {chapter_id} Quiz",
            "questions": []  # TODO: Parse questions from text
        }
    elif block_type == "diagram":
        # Extract diagram description
        return {
            "diagram_prompt": text,
            "diagram_type": "flowchart",
            "description": text
        }
    else:
        return {
            "message": text,
            "data": raw_response
        }


# TODO: Chapter 2 formatting functions
# def format_ask_response_ch2(raw_response: Dict[str, Any]) -> Dict[str, Any]:
#     """
#     Format ask response for Chapter 2.
#     
#     Args:
#         raw_response: Raw LLM response
#     
#     Returns:
#         Formatted ask response
#     
#     TODO: Format ask response for Chapter 2
#     """
#     pass

# def format_explain_response_ch2(raw_response: Dict[str, Any]) -> Dict[str, Any]:
#     """
#     Format explain response for Chapter 2.
#     
#     Args:
#         raw_response: Raw LLM response
#     
#     Returns:
#         Formatted explain response
#     
#     TODO: Format explain response for Chapter 2
#     """
#     pass

# def format_quiz_response_ch2(raw_response: Dict[str, Any]) -> Dict[str, Any]:
#     """
#     Format quiz response for Chapter 2.
#     
#     Args:
#         raw_response: Raw LLM response
#     
#     Returns:
#         Formatted quiz response
#     
#     TODO: Format quiz response for Chapter 2
#     """
#     pass

# def format_diagram_response_ch2(raw_response: Dict[str, Any]) -> Dict[str, Any]:
#     """
#     Format diagram response for Chapter 2.
#     
#     Args:
#         raw_response: Raw LLM response
#     
#     Returns:
#         Formatted diagram response
#     
#     TODO: Format diagram response for Chapter 2
#     """
#     pass

def format_diagram_output_ch2(
    raw_response: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Format diagram output for Chapter 2.
    
    Args:
        raw_response: Raw LLM response with diagram data
    
    Returns:
        Formatted diagram structure:
        {
            "nodes": List[Dict],
            "edges": List[Dict],
            "svg": str,
            "metadata": Dict[str, Any]
        }
    
    TODO: Implement formatting for Chapter 2 diagram output
    TODO: Parse raw LLM response
    TODO: Extract nodes, edges, SVG
    TODO: Format Mechanical Systems-specific metadata
    TODO: Return formatted diagram structure
    """
    # Placeholder return - no real formatting
    return {
        "nodes": [],
        "edges": [],
        "svg": "",
        "metadata": {}
    }


def format_diagram_output_ch3(
    raw_response: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Format diagram output for Chapter 3.
    
    Args:
        raw_response: Raw LLM response with diagram data
    
    Returns:
        Formatted diagram structure:
        {
            "nodes": List[Dict],
            "edges": List[Dict],
            "svg": str,
            "metadata": Dict[str, Any]
        }
    
    TODO: Implement formatting for Chapter 3 diagram output
    TODO: Parse raw LLM response
    TODO: Extract nodes, edges, SVG
    TODO: Format Physical AI-specific metadata
    TODO: Return formatted diagram structure
    """
    # Placeholder return - no real formatting
    return {
        "nodes": [],
        "edges": [],
        "svg": "",
        "metadata": {}
    }


def format_el10_output_ch2(
    raw_response: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Format ELI10 output for Chapter 2.
    
    Args:
        raw_response: Raw LLM response with explanation data
    
    Returns:
        Formatted explanation structure:
        {
            "explanation": str,
            "examples": List[str],
            "analogies": List[str]
        }
    
    TODO: Implement formatting for Chapter 2 ELI10 output
    TODO: Parse raw LLM response
    TODO: Extract explanation, examples, analogies
    TODO: Format ROS 2-specific metadata
    TODO: Return formatted explanation structure
    """
    # Placeholder return - no real formatting
    return {
        "explanation": "",
        "examples": [],
        "analogies": []
    }


def format_quiz_output_ch2(
    raw_response: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Format quiz output for Chapter 2.
    
    Args:
        raw_response: Raw LLM response dictionary
    
    Returns:
        Formatted quiz structure with questions, answers, learning_objectives, metadata
    
    TODO: Implement formatting for Chapter 2 quiz output
    TODO: Parse raw LLM response
    TODO: Extract questions, answers, learning_objectives
    TODO: Format ROS 2-specific metadata
    TODO: Return formatted quiz structure
    """
    # Placeholder return - no real formatting
    return {
        "questions": [],
        "learning_objectives": [],
        "metadata": {}
    }

