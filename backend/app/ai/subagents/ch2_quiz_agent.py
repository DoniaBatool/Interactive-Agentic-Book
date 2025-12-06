"""
Chapter 2 Quiz Agent

Specialized agent for generating interactive quizzes for ROS 2 learning objectives.
Uses Chapter 2 context to create questions covering ROS 2 fundamentals.
"""

from typing import Dict, Any, List


async def ch2_quiz_agent(
    chapter_id: int,
    num_questions: int,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Chapter 2 quiz agent blueprint.
    
    Generate ROS 2 quiz with Chapter 2 context.
    
    Expected Input:
        chapter_id: int                        # Chapter ID (should be 2)
        num_questions: int                     # Number of questions to generate
        context: {
            "context": str,                     # Retrieved Chapter 2 context chunks
            "chunks": List[Dict],              # Chunk metadata with ROS 2 concepts
            "query_embedding": List[float]     # Query vector
        }
    
    Expected Output:
        {
            "questions": List[Dict],          # List of quiz questions with answers
            "learning_objectives": List[str]   # Learning objectives covered
        }
    
    Agent Flow (all TODO):
    1. Use retrieval_skill to get learning objectives from Chapter 2 metadata
    2. Use prompt_builder_skill to build quiz generation prompt
    3. Call LLM provider (DEFAULT_CH2_MODEL) to generate questions
    4. Use formatting_skill to structure quiz data
    5. Return formatted quiz
    
    TODO: Implement ROS 2 quiz generation logic
    TODO: Step 1: Call retrieve_content("learning objectives", chapter_id=2) to get Chapter 2 learning objectives
    TODO: Step 2: Call build_prompt("quiz", learning_objectives, context, chapter_id=2) to build quiz generation prompt
    TODO: Step 3: Call LLM provider (DEFAULT_CH2_MODEL) to generate ROS 2 quiz questions
    TODO: Step 4: Call format_response(response, "quiz", chapter_id=2) to structure quiz data
    TODO: Step 5: Return formatted quiz with ROS 2 questions
    
    ROS 2-specific considerations:
    - Generate questions covering all ROS 2 fundamentals
    - Include questions about: node communication, topic pub/sub, services vs actions, package structure, launch files
    - Use ROS 2 terminology correctly in questions and answers
    - Reference real-world ROS 2 examples in questions
    - Cover learning objectives from Chapter 2 metadata
    - ROS 2 concepts: nodes, topics, services, actions, packages, launch files
    """
    # Placeholder return - no real quiz generation logic
    return {
        "questions": [],
        "learning_objectives": []
    }
