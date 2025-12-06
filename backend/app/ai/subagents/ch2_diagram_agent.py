"""
Chapter 2 Diagram Agent

Specialized agent for generating visual diagrams for ROS 2 concepts.
Uses Chapter 2 context to create diagrams showing ROS 2 architecture and relationships.
"""

from typing import Dict, Any, List


async def ch2_diagram_agent(
    diagram_type: str,
    concepts: List[str],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Chapter 2 diagram agent blueprint.
    
    Generate ROS 2 diagram with Chapter 2 context.
    
    Expected Input:
        diagram_type: str                      # Type of diagram (e.g., "ros2-ecosystem-overview", "node-communication-architecture", "topic-pubsub-flow", "services-actions-comparison")
        concepts: List[str]                    # ROS 2 concepts to include in diagram
        context: {
            "context": str,                     # Retrieved Chapter 2 context chunks
            "chunks": List[Dict],              # Chunk metadata with ROS 2 concepts
            "query_embedding": List[float]     # Query vector
        }
    
    Expected Output:
        {
            "diagram_url": str,                # URL or path to generated diagram
            "metadata": {
                "title": str,                  # Diagram title
                "description": str,            # Diagram description
                "concepts": List[str],         # ROS 2 concepts included
                "format": str                  # Diagram format (e.g., "mermaid", "svg", "png")
            }
        }
    
    Agent Flow (all TODO):
    1. Use prompt_builder_skill to build diagram generation prompt
    2. Call LLM provider (DEFAULT_CH2_MODEL) or diagram generation API
    3. Use formatting_skill to format diagram output
    4. Return diagram URL/metadata
    
    TODO: Implement ROS 2 diagram generation logic
    TODO: Step 1: Call build_prompt("diagram", diagram_type, concepts, context, chapter_id=2) to build diagram generation prompt
    TODO: Step 2: Call LLM provider (DEFAULT_CH2_MODEL) or diagram generation API to generate ROS 2 diagram
    TODO: Step 3: Call format_response(response, "diagram", chapter_id=2) to format diagram output
    TODO: Step 4: Return diagram URL/metadata with ROS 2 diagram structure
    
    ROS 2-specific considerations:
    - Generate diagrams showing ROS 2 architecture (nodes, topics, services, actions)
    - Include node communication graphs
    - Show topic publish/subscribe flows
    - Compare services vs actions visually
    - Use ROS 2 terminology in diagram labels
    - Diagram types: "ros2-ecosystem-overview", "node-communication-architecture", "topic-pubsub-flow", "services-actions-comparison"
    """
    # Placeholder return - no real diagram generation logic
    return {
        "diagram_url": "",
        "metadata": {
            "title": "",
            "description": "",
            "concepts": [],
            "format": ""
        }
    }
