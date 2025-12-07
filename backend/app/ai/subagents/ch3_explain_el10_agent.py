"""
Chapter 3 Explain Like I'm 10 Agent

Specialized agent for generating simplified explanations for Physical AI concepts.
Uses Chapter 3 context to provide age-appropriate explanations with analogies.
"""

from typing import Dict, Any


async def ch3_explain_el10_agent(
    concept: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Chapter 3 explanation agent blueprint.
    
    Generate Physical AI explanation with Chapter 3 context.
    
    Expected Input:
        concept: str                           # Physical AI concept to explain (e.g., "perception", "sensors", "computer-vision", "signal-processing")
        context: {
            "context": str,                     # Retrieved Chapter 3 context chunks
            "chunks": List[Dict],              # Chunk metadata with Physical AI concepts
            "query_embedding": List[float]     # Query vector
        }
    
    Expected Output:
        {
            "explanation": str,                # Age-appropriate explanation text
            "examples": List[str],             # Real-world Physical AI examples
            "analogies": List[str]            # Simple analogies (sensors as eyes/ears, signal processing as filtering, etc.)
        }
    
    Agent Flow (all TODO):
    1. Use prompt_builder_skill to build ELI10 prompt with Physical AI context
    2. Call LLM provider with ELI10 instructions
    3. Use formatting_skill to extract examples and analogies
    4. Return formatted explanation
    
    TODO: Implement Physical AI explanation generation logic
    TODO: Step 1: Call build_prompt("explain-like-10", concept, context, chapter_id=3) to build ELI10 prompt
    TODO: Step 2: Call LLM provider with ELI10 instructions + Physical AI context
    TODO: Step 3: Call format_response(response, "explain-like-10", chapter_id=3) to extract examples and analogies
    TODO: Step 4: Return formatted explanation with Physical AI examples and analogies
    
    Physical AI-specific considerations:
    - Use Physical AI analogies: sensors as eyes/ears (perception), signal processing as filtering (cleaning data), perception as understanding (making sense of the world)
    - Reference real-world examples: autonomous vehicles, robotics, drones
    - Simplify Physical AI terminology for age-appropriate explanations
    - Include visual analogies when helpful
    - Concepts: "perception", "sensors", "computer-vision", "depth-perception", "signal-processing", "feature-extraction"
    """
    # Placeholder return - no real explanation logic
    return {
        "explanation": "",
        "examples": [],
        "analogies": []
    }

