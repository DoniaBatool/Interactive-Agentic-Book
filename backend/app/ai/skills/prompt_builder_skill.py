"""
Prompt Builder Skill

Reusable skill for constructing prompts for LLM providers.
Builds prompts with system instructions, context, and user input.
"""

from typing import List, Dict, Any, Optional


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
    
    Real implementation: Build prompts with system instructions, context, and user input.
    """
    # Build system prompt based on block_type
    system_prompts = {
        "ask-question": "You are a helpful tutor answering questions about Physical AI and Robotics. Use the provided context to give accurate, clear answers. Cite sources when possible.",
        "explain-like-10": "Explain this concept like the learner is 10 years old. Use simple language, analogies, and examples. Make it fun and easy to understand.",
        "quiz": "Generate quiz questions from the following learning objectives. Create diverse question types (multiple choice, true/false, short answer) with clear explanations.",
        "diagram": "Generate a diagram description showing the following concepts. Use clear, structured format that can be rendered as a visual diagram."
    }
    
    system_prompt = system_prompts.get(block_type, "You are a helpful AI assistant.")
    
    # Format context chunks
    context_text = ""
    if context:
        context_parts = []
        for chunk in context:
            text = chunk.get("text", "")
            section_id = chunk.get("section_id", "")
            if text:
                if section_id:
                    context_parts.append(f"[Section: {section_id}]\n{text}")
                else:
                    context_parts.append(text)
        context_text = "\n\n".join(context_parts)
    
    # Build full prompt
    prompt_parts = [
        f"System: {system_prompt}",
        ""
    ]
    
    if context_text:
        prompt_parts.extend([
            "Context:",
            context_text,
            ""
        ])
    
    prompt_parts.extend([
        f"User: {user_input}",
        "",
        "Instructions: Provide a clear, accurate response based on the context above."
    ])
    
    return "\n".join(prompt_parts)


# TODO: Chapter 2 prompt building functions
# def build_ask_prompt_ch2(question: str, context: List[Dict[str, Any]]) -> str:
#     """
#     Build ask prompt for Chapter 2.
#     
#     Args:
#         question: User question about Mechanical Systems
#         context: Retrieved Chapter 2 context chunks
#     
#     Returns:
#         Constructed prompt string
#     
#     TODO: Build Mechanical Systems ask prompt with Chapter 2 context
#     """
#     pass

# def build_explain_prompt_ch2(concept: str, context: List[Dict[str, Any]]) -> str:
#     """
#     Build explain prompt for Chapter 2.
#     
#     Args:
#         concept: Mechanical Systems concept to explain
#         context: Retrieved Chapter 2 context chunks
#     
#     Returns:
#         Constructed prompt string
#     
#     TODO: Build Mechanical Systems explain prompt with Chapter 2 context
#     """
#     pass

# def build_quiz_prompt_ch2(num_questions: int, context: List[Dict[str, Any]]) -> str:
#     """
#     Build quiz prompt for Chapter 2.
#     
#     Args:
#         num_questions: Number of questions to generate
#         context: Retrieved Chapter 2 context chunks
#     
#     Returns:
#         Constructed prompt string
#     
#     TODO: Build Mechanical Systems quiz prompt with Chapter 2 context
#     """
#     pass

# def build_diagram_prompt_ch2(diagram_type: str, concepts: List[str], context: List[Dict[str, Any]]) -> str:
#     """
#     Build diagram prompt for Chapter 2.
#     
#     Args:
#         diagram_type: Type of diagram to generate
#         concepts: List of Mechanical Systems concepts to include
#         context: Retrieved Chapter 2 context chunks
#     
#     Returns:
#         Constructed prompt string
#     
#     TODO: Build Mechanical Systems diagram prompt with Chapter 2 context
#     """
#     pass

def build_diagram_prompt_ch2(
    diagram_type: str,
    chapter_id: int,
    concepts: List[str]
) -> str:
    """
    Build diagram prompt for Chapter 2.
    
    Args:
        diagram_type: Type of diagram to generate
        chapter_id: Chapter identifier (should be 2)
        concepts: List of Mechanical Systems concepts to include
    
    Returns:
        Constructed prompt string
    
    TODO: Implement prompt building for Chapter 2 diagrams
    TODO: Load ch2_diagram_prompt.txt template
    TODO: Replace template variables ({{diagram_type}}, {{chapter_id}}, {{concepts}})
    TODO: Add Mechanical Systems-specific context
    TODO: Return constructed prompt string
    """
    # Placeholder return - no real prompt building
    return ""


def build_diagram_prompt_ch3(
    diagram_type: str,
    chapter_id: int,
    concepts: List[str]
) -> str:
    """
    Build diagram prompt for Chapter 3.
    
    Args:
        diagram_type: Type of diagram to generate
        chapter_id: Chapter identifier (should be 3)
        concepts: List of Physical AI concepts to include
    
    Returns:
        Constructed prompt string
    
    TODO: Implement prompt building for Chapter 3 diagrams
    TODO: Load ch3_diagram_prompt.txt template
    TODO: Replace template variables ({{diagram_type}}, {{chapter_id}}, {{concepts}})
    TODO: Add Physical AI-specific context
    TODO: Return constructed prompt string
    """
    # Placeholder return - no real prompt building
    return ""


def build_el10_prompt_ch2(
    concept: str,
    chapter_id: int,
    context: Optional[Dict[str, Any]] = None
) -> str:
    """
    Build ELI10 prompt for Chapter 2.
    
    Args:
        concept: ROS 2 concept to explain
        chapter_id: Chapter identifier (should be 2)
        context: Optional RAG context chunks
    
    Returns:
        Constructed prompt string
    
    TODO: Implement prompt building for Chapter 2 ELI10 explanations
    TODO: Load ch2_el10_prompt.txt template
    TODO: Replace template variables ({{concept}}, {{chapter_id}}, {{context}})
    TODO: Add ROS 2-specific context
    TODO: Return constructed prompt string
    """
    # Placeholder return - no real prompt building
    return ""


def build_quiz_prompt_ch2(
    chapter_id: int,
    num_questions: int,
    learning_objectives: Optional[List[str]] = None
) -> str:
    """
    Build quiz prompt for Chapter 2.
    
    Args:
        chapter_id: Chapter identifier (should be 2)
        num_questions: Number of questions to generate
        learning_objectives: Optional list of learning objectives to cover
    
    Returns:
        Constructed prompt string for quiz generation
    
    TODO: Implement prompt building for Chapter 2 quizzes
    TODO: Load ch2_quiz_prompt.txt template
    TODO: Replace template variables ({{chapter_id}}, {{num_questions}}, {{learning_objectives}}, {{context}})
    TODO: Add ROS 2-specific context
    TODO: Return constructed prompt string
    """
    # Placeholder return - no real prompt building
    return ""

