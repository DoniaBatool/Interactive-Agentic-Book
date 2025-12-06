"""
Chapter 2 Explain Like I'm 10 Agent

Specialized agent for generating simplified explanations for ROS 2 concepts.
Uses Chapter 2 context to provide age-appropriate explanations with analogies.
"""

from typing import Dict, Any


async def ch2_explain_el10_agent(
    concept: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Chapter 2 explanation agent blueprint.
    
    Generate ROS 2 explanation with Chapter 2 context.
    
    Expected Input:
        concept: str                           # ROS 2 concept to explain (e.g., "topics", "nodes", "services", "actions")
        context: {
            "context": str,                     # Retrieved Chapter 2 context chunks
            "chunks": List[Dict],              # Chunk metadata with ROS 2 concepts
            "query_embedding": List[float]     # Query vector
        }
    
    Expected Output:
        {
            "explanation": str,                # Age-appropriate explanation text
            "examples": List[str],             # Real-world ROS 2 examples
            "analogies": List[str]            # Simple analogies (post office, restaurant, etc.)
        }
    
    Agent Flow (all TODO):
    1. Use prompt_builder_skill to build ELI10 prompt with ROS 2 context
    2. Call LLM provider (DEFAULT_CH2_MODEL) with ELI10 instructions
    3. Use formatting_skill to extract examples and analogies
    4. Return formatted explanation
    
    TODO: Implement ROS 2 explanation generation logic
    TODO: Step 1: Call build_prompt("explain-like-10", concept, context, chapter_id=2) to build ELI10 prompt
    TODO: Step 2: Call LLM provider (DEFAULT_CH2_MODEL) with ELI10 instructions + ROS 2 context
    TODO: Step 3: Call format_response(response, "explain-like-10", chapter_id=2) to extract examples and analogies
    TODO: Step 4: Return formatted explanation with ROS 2 examples and analogies
    
    ROS 2-specific considerations:
    - Use ROS 2 analogies: post office (communication), restaurant (nodes), radio broadcast (topics), phone calls (services), package delivery (actions)
    - Reference real-world examples: TurtleBot 3, navigation stack, robot arm control
    - Simplify ROS 2 terminology for age-appropriate explanations
    - Include visual analogies when helpful
    - Concepts: "topics", "nodes", "services", "actions", "packages", "launch-files"
    """
    # Placeholder return - no real explanation logic
    return {
        "explanation": "",
        "examples": [],
        "analogies": []
    }
