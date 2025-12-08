"""
Prompt Governance Policy

Defines prompt policies for tone, style, error messages, and safety reminders.
"""

from typing import Dict, Any


def define_prompt_policy(
    block_type: str,
    chapter_id: int
) -> Dict[str, Any]:
    """
    Define prompt governance policy for a specific block type and chapter.
    
    Args:
        block_type: Type of AI block ("ask-question", "explain-like-el10", etc.)
        chapter_id: Chapter ID
    
    Returns:
        PromptPolicy with structure:
        {
            "tone": str,  # "educational" | "safe" | "non-political"
            "explanation_style": str,  # "simple" | "clear" | "age-appropriate"
            "scaffolded_learning": bool,
            "error_messages": Dict[str, str],
            "safety_reminders": List[str],
            "block_specific_rules": Dict[str, Any]
        }
    
    TODO: Load chapter overrides if present (from Feature 046)
    TODO: Apply block-specific rules
    TODO: Apply chapter-specific customizations
    TODO: Return comprehensive policy
    """
    # Placeholder: Return basic policy
    # TODO: Implement real policy definition
    base_policy = {
        "tone": "educational",
        "explanation_style": "age-appropriate",
        "scaffolded_learning": True,
        "error_messages": {
            "uncertain": "I'm not entirely certain about this. Based on the chapter content, [explanation]. Please verify with additional sources.",
            "not_found": "I couldn't find specific information about this in the chapter content. Could you rephrase your question?",
            "inappropriate": "I can only help with educational questions about Physical AI and Robotics. Could you rephrase your question?"
        },
        "safety_reminders": [
            "Cite sources from the provided context when making factual claims",
            "Acknowledge uncertainty rather than guessing",
            "Keep explanations age-appropriate (12+)",
            "Use educational, safe, non-political tone"
        ],
        "block_specific_rules": {}
    }
    
    # Apply block-specific rules
    if block_type == "ask-question":
        base_policy["block_specific_rules"] = {
            "always_cite_sources": True,
            "acknowledge_uncertainty": True
        }
    elif block_type == "explain-like-el10":
        base_policy["block_specific_rules"] = {
            "use_simple_language": True,
            "use_many_analogies": True,
            "keep_fun_and_engaging": True
        }
    elif block_type == "interactive-quiz":
        base_policy["block_specific_rules"] = {
            "age_appropriate_questions": True,
            "clear_explanations": True,
            "diverse_question_types": True
        }
    elif block_type == "diagram-generator":
        base_policy["block_specific_rules"] = {
            "educational_diagrams": True,
            "clear_descriptions": True
        }
    
    # TODO: Load chapter overrides and apply
    # from app.content.overrides import load_chapter_overrides
    # overrides = load_chapter_overrides(chapter_id)
    # if overrides:
    #     base_policy["tone"] = overrides.get("tone", base_policy["tone"])
    #     ...
    
    return base_policy

