"""
Selection Cleaning Skill

Skill for cleaning and normalizing selected text from user selections.
Removes extra whitespace, normalizes formatting, and prepares text for processing.

TODO: Real cleaning logic will be implemented in a future feature.
Currently returns text as-is.
"""


def clean_selection(selected_text: str) -> str:
    """
    Clean and normalize selected text.
    
    Args:
        selected_text: Raw text selected by user
    
    Returns:
        Cleaned text
    
    TODO: Remove extra whitespace (leading, trailing, multiple spaces)
    TODO: Normalize line breaks (convert \r\n to \n)
    TODO: Remove special characters if needed
    TODO: Handle encoding issues (UTF-8 normalization)
    TODO: Truncate if too long for context window
    TODO: Preserve important formatting (paragraphs, lists)
    """
    # Placeholder: return selected_text as-is
    return selected_text

