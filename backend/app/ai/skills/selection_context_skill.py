"""
Selection Context Skill

Skill for building context from selected text and user question.
Formats selection and question for LLM prompt.

TODO: Real context building logic will be implemented in a future feature.
Currently returns selected text as-is.
"""


def build_selection_context(selected_text: str, question: str) -> str:
    """
    Build context string from selection and question.
    
    Args:
        selected_text: Cleaned selected text
        question: User's question
    
    Returns:
        Context string formatted for LLM prompt
    
    TODO: Build context string from selection
    TODO: Format for LLM prompt (add instructions, examples)
    TODO: Include question in context
    TODO: Add metadata (chapter, section, etc.)
    TODO: Truncate if context exceeds token limit
    TODO: Format as prompt template
    """
    # Placeholder: return selected_text
    return selected_text

