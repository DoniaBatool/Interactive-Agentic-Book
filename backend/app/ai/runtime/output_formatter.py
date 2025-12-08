"""
Unified Output Formatter

Standardizes AI block response structures across all chapters.
Ensures identical formatting regardless of chapter.
"""

from typing import Dict, Any, Optional, List


def format_ai_block_response(
    block_type: str,
    raw_response: Dict[str, Any],
    chapter_id: int,
    overrides: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Format AI block response to standardized structure.
    
    Args:
        block_type: Type of AI block ("ask-question", "explain-like-el10", "interactive-quiz", "diagram-generator")
        raw_response: Raw response from subagent
        chapter_id: Chapter ID
        overrides: Optional chapter-specific overrides
    
    Returns:
        Standardized response structure based on block_type
    
    Standardized Structures:
        - ask-question: {answer: str, sources: List[str], confidence: float}
        - explain-like-el10: {explanation: str, analogies: List[str], examples: List[str]}
        - interactive-quiz: {quiz_title: str, questions: List[Question]}
        - diagram-generator: {diagram_prompt: str, diagram_type: str, description: str}
    """
    # Apply chapter overrides if present
    formatting_style = None
    if overrides and "formatting_style" in overrides:
        formatting_style = overrides["formatting_style"]
    
    if block_type == "ask-question":
        return _format_ask_question_response(raw_response, formatting_style)
    elif block_type == "explain-like-el10":
        return _format_explain_el10_response(raw_response, formatting_style)
    elif block_type == "interactive-quiz":
        return _format_quiz_response(raw_response, formatting_style)
    elif block_type == "diagram-generator":
        return _format_diagram_response(raw_response, formatting_style)
    else:
        # Unknown block type - return as-is with warning
        return {
            "message": raw_response.get("message", "Unknown block type"),
            "data": raw_response,
            "warning": f"Unknown block type: {block_type}"
        }


def _format_ask_question_response(
    raw_response: Dict[str, Any],
    formatting_style: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Format ask-question response.
    
    Standardized structure: {answer: str, sources: List[str], confidence: float}
    """
    # TODO: Extract answer, sources, confidence from raw_response
    # TODO: Apply formatting_style if present (e.g., max_answer_length)
    
    answer = raw_response.get("answer", raw_response.get("text", ""))
    sources = raw_response.get("sources", [])
    confidence = raw_response.get("confidence", 0.8)
    
    # Apply formatting style overrides if present
    if formatting_style:
        max_length = formatting_style.get("max_answer_length")
        if max_length and len(answer) > max_length:
            answer = answer[:max_length] + "..."
    
    return {
        "answer": answer,
        "sources": sources,
        "confidence": confidence
    }


def _format_explain_el10_response(
    raw_response: Dict[str, Any],
    formatting_style: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Format explain-like-el10 response.
    
    Standardized structure: {explanation: str, analogies: List[str], examples: List[str]}
    """
    # TODO: Extract explanation, analogies, examples from raw_response
    # TODO: Apply formatting_style if present
    
    explanation = raw_response.get("explanation", raw_response.get("text", ""))
    analogies = raw_response.get("analogies", [])
    examples = raw_response.get("examples", [])
    
    return {
        "explanation": explanation,
        "analogies": analogies,
        "examples": examples
    }


def _format_quiz_response(
    raw_response: Dict[str, Any],
    formatting_style: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Format interactive-quiz response.
    
    Standardized structure: {quiz_title: str, questions: List[Question]}
    """
    # TODO: Extract quiz_title and questions from raw_response
    # TODO: Ensure Question structure is consistent
    # TODO: Apply formatting_style if present
    
    quiz_title = raw_response.get("quiz_title", f"Chapter Quiz")
    questions = raw_response.get("questions", [])
    
    # Ensure questions have consistent structure
    formatted_questions = []
    for q in questions:
        formatted_questions.append({
            "id": q.get("id", ""),
            "question_text": q.get("question_text", q.get("question", "")),
            "type": q.get("type", "multiple-choice"),
            "options": q.get("options", []),
            "correct_answer": q.get("correct_answer", ""),
            "explanation": q.get("explanation", "")
        })
    
    return {
        "quiz_title": quiz_title,
        "questions": formatted_questions
    }


def _format_diagram_response(
    raw_response: Dict[str, Any],
    formatting_style: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Format diagram-generator response.
    
    Standardized structure: {diagram_prompt: str, diagram_type: str, description: str}
    """
    # TODO: Extract diagram_prompt, diagram_type, description from raw_response
    # TODO: Apply formatting_style if present
    
    diagram_prompt = raw_response.get("diagram_prompt", raw_response.get("text", ""))
    diagram_type = raw_response.get("diagram_type", "flowchart")
    description = raw_response.get("description", "")
    
    return {
        "diagram_prompt": diagram_prompt,
        "diagram_type": diagram_type,
        "description": description
    }

