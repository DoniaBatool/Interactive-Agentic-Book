"""
Prompt Builder Skill

Reusable skill for constructing prompts for LLM providers.
Builds prompts with system instructions, context, and user input.
"""

from typing import List, Dict, Any


def build_prompt(
    block_type: str,
    user_input: str,
    context: List[Dict[str, Any]],
    chapter_id: int = None
) -> str:
    """
    Prompt construction skill blueprint.
    
    Expected Input:
        block_type: str                        # "ask-question", "explain-like-10", "quiz", "diagram"
        user_input: str                        # User's question or concept
        context: [
            {
                "text": str,                   # Chunk text
                "section_id": str,            # Section identifier
                "score": float                 # Relevance score
            },
            ...
        ]
    
    Expected Output:
        Constructed prompt string for LLM:
        - System instructions based on block_type
        - Retrieved context chunks
        - User input
        - Formatting instructions
    
    TODO: Implement prompt building logic
    TODO: Build system prompt based on block_type:
        - ask-question: "You are a helpful tutor answering questions about Physical AI..."
        - explain-like-10: "Explain this concept like the learner is 10 years old..."
        - quiz: "Generate quiz questions from the following learning objectives..."
        - diagram: "Generate a diagram showing the following concepts..."
    TODO: Include retrieved context chunks in prompt
    TODO: Format context with section references
    TODO: Add user input to prompt
    TODO: Add formatting instructions for structured output
    TODO: Add source citation instructions
    
    TODO: Chapter-aware prompt builder
    TODO: templates for CH2
    TODO: If chapter_id == 2:
    TODO:     Build ROS 2-specific prompts
    TODO:     Use ROS 2 prompt templates
    TODO:     Include ROS 2 concepts, analogies, examples
    TODO:     System prompt: "You are a helpful tutor explaining ROS 2 concepts..."
    TODO:     Include ROS 2 context chunks
    TODO:     Format context with ROS 2-specific instructions
    TODO:     Add ROS 2 terminology guidelines
    TODO: Elif chapter_id == 1:
    TODO:     Build Chapter 1 prompts (existing logic)
    """
    # Placeholder return - no real prompt building logic
    return ""

