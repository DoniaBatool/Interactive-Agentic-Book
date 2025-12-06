"""
Chapter 2 Ask Question Agent

Specialized agent for answering questions about ROS 2 concepts using Chapter 2 context.
Uses RAG pipeline to retrieve relevant context and generates answers.
"""

from typing import Dict, Any


async def ch2_ask_question_agent(
    question: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Chapter 2 question-answering agent blueprint.
    
    Process ROS 2 questions with Chapter 2 RAG context.
    
    Expected Input:
        question: str                          # User question about ROS 2
        context: {
            "context": str,                     # Retrieved Chapter 2 context chunks
            "chunks": List[Dict],              # Chunk metadata with ROS 2 concepts
            "query_embedding": List[float]     # Query vector
        }
    
    Expected Output:
        {
            "answer": str,                     # Generated answer text with ROS 2 context
            "sources": List[str],              # Source citations (section IDs)
            "confidence": float                # Confidence score (0.0-1.0)
        }
    
    Agent Flow (all TODO):
    1. Use retrieval_skill to get additional context if needed
    2. Use prompt_builder_skill to construct ROS 2 question-answering prompt
    3. Call LLM provider (DEFAULT_CH2_MODEL) with prompt + context
    4. Use formatting_skill to format response with source citations
    5. Return formatted answer
    
    TODO: Implement ROS 2 question-answering logic
    TODO: Step 1: Call retrieve_content(query, chapter_id=2) to get more context if needed
    TODO: Step 2: Call build_prompt("ask-question", question, context, chapter_id=2) to construct ROS 2 prompt
    TODO: Step 3: Call LLM provider (DEFAULT_CH2_MODEL) with prompt + ROS 2 context
    TODO: Step 4: Call format_response(response, "ask-question", chapter_id=2) to format with sources
    TODO: Extract source citations from retrieved Chapter 2 chunks
    TODO: Calculate confidence score based on retrieved ROS 2 context relevance
    TODO: Add error handling for LLM failures
    
    ROS 2-specific considerations:
    - Use ROS 2 analogies (post office, restaurant, phone calls, package delivery)
    - Reference real-world examples (TurtleBot 3, navigation stack, robot arm control)
    - Handle ROS 2 terminology correctly (nodes, topics, services, actions, packages, launch files)
    - Include section context when sectionId provided
    - Filter chunks by section_id for section-specific questions
    - Questions about: nodes, topics, services, actions, packages, launch files
    - Section-specific: introduction-to-ros2, nodes-and-node-communication, topics-and-messages, services-and-actions
    """
    # Placeholder return - no real question-answering logic
    return {
        "answer": "",
        "sources": [],
        "confidence": 0.0
    }
