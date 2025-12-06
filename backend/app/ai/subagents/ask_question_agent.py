"""
Ask Question Agent

Specialized agent for answering questions about chapter content.
Uses RAG pipeline to retrieve relevant context and generates answers.
"""

from typing import Dict, Any


async def ask_question_agent(
    question: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Question-answering agent blueprint.
    
    Expected Input:
        question: str                          # User question
        context: {
            "context": str,                     # Retrieved context chunks
            "chunks": List[Dict],              # Chunk metadata
            "query_embedding": List[float]     # Query vector
        }
    
    Expected Output:
        {
            "answer": str,                     # Generated answer text
            "sources": List[str],              # Source citations (section IDs)
            "confidence": float                # Confidence score (0.0-1.0)
        }
    
    Agent Flow (all TODO):
    1. Use retrieval_skill to get additional context if needed
    2. Use prompt_builder_skill to construct question-answering prompt
    3. Call LLM provider with prompt + context
    4. Use formatting_skill to format response with source citations
    5. Return formatted answer
    
    TODO: Implement question-answering logic
    TODO: Step 1: Call retrieve_content() to get more context if needed
    TODO: Step 2: Call build_prompt("ask-question", question, context) to construct prompt
    TODO: Step 3: Call llm_provider.generate(prompt) to generate answer
    TODO: Step 4: Call format_response(response, "ask-question") to format with sources
    TODO: Extract source citations from retrieved chunks
    TODO: Calculate confidence score based on retrieved context relevance
    TODO: Add error handling for LLM failures
    
    # TODO: Chapter 2 (ROS 2) Integration
    # Expected ROS 2 inputs:
    #   - Questions about: nodes, topics, services, actions, packages, launch files
    #   - Section-specific: introduction-to-ros2, nodes-and-node-communication, topics-and-messages, services-and-actions
    # Expected output format: Same as Chapter 1, but with ROS 2 context
    # ROS 2-specific considerations:
    #   - Use ROS 2 analogies (post office, restaurant, phone calls, package delivery)
    #   - Reference real-world examples (TurtleBot 3, navigation stack, robot arm control)
    #   - Handle ROS 2 terminology correctly (nodes, topics, services, actions)
    #   - Include section context when sectionId provided
    #   - Filter chunks by section_id for section-specific questions
    """
    # Placeholder return - no real question-answering logic
    return {
        "answer": "placeholder",
        "sources": [],
        "confidence": 0.0
    }

