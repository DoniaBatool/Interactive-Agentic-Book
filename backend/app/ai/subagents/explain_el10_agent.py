"""
Explain Like I'm 10 Agent

Specialized agent for generating simplified explanations at age-appropriate level.
Uses ELI10 (Explain Like I'm 10) prompt pattern with RAG context.
"""

from typing import Dict, Any


async def explain_el10_agent(
    concept: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Simplified explanation agent blueprint.
    
    Expected Input:
        concept: str                           # Concept name to explain
        context: {
            "context": str,                     # Retrieved context chunks
            "chunks": List[Dict],              # Chunk metadata
            "query_embedding": List[float]     # Query vector
        }
    
    Expected Output:
        {
            "explanation": str,                # Simplified explanation
            "examples": List[str],             # Analogies or examples
            "analogies": List[str]             # Age-appropriate analogies
        }
    
    Agent Flow (all TODO):
    1. Use prompt_builder_skill to build ELI10 prompt with concept + context
    2. Call LLM provider with ELI10 instructions
    3. Use formatting_skill to extract examples and analogies
    4. Return formatted explanation
    
    TODO: Implement ELI10 explanation logic
    TODO: Step 1: Call build_prompt("explain-like-10", concept, context) with ELI10 instructions
    TODO: Step 2: Call llm_provider.generate(prompt) with temperature=0.8 for creativity
    TODO: Step 3: Call format_response(response, "explain-like-10") to extract examples
    TODO: Ensure explanation is age-appropriate (10-year-old level)
    TODO: Add analogies and real-world examples
    TODO: Add error handling for LLM failures
    
    # TODO: Chapter 2 (ROS 2) Integration
    # Expected ROS 2 inputs:
    #   - Concepts: "topics", "nodes", "services", "actions", "packages", "launch-files"
    #   - Chapter context: chapterId=2
    # Expected output format: Same as Chapter 1, but with ROS 2 analogies
    # ROS 2-specific considerations:
    #   - Use ROS 2 analogies: post office (communication), restaurant (nodes), radio broadcast (topics), phone calls (services), package delivery (actions)
    #   - Reference real-world examples: TurtleBot 3, navigation stack, robot arm control
    #   - Simplify ROS 2 terminology for age-appropriate explanations
    #   - Include visual analogies when helpful
    """
    # Placeholder return - no real explanation logic
    return {
        "explanation": "placeholder",
        "examples": [],
        "analogies": []
    }

