"""
Chapter 3 Ask Question Agent

Specialized agent for answering questions about Physical AI concepts using Chapter 3 context.
Uses RAG pipeline to retrieve relevant context and generates answers.
"""

from typing import Dict, Any


async def ch3_ask_question_agent(
    question: str,
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Chapter 3 question-answering agent blueprint.
    
    Process Physical AI questions with Chapter 3 RAG context.
    
    Expected Input:
        question: str                          # User question about Physical AI
        context: {
            "context": str,                     # Retrieved Chapter 3 context chunks
            "chunks": List[Dict],              # Chunk metadata with Physical AI concepts
            "query_embedding": List[float]     # Query vector
        }
    
    Expected Output:
        {
            "answer": str,                     # Generated answer text with Physical AI context
            "sources": List[str],              # Source citations (section IDs)
            "confidence": float                # Confidence score (0.0-1.0)
        }
    
    Agent Flow (all TODO):
    1. Use retrieval_skill to get additional context if needed
    2. Use prompt_builder_skill to construct Physical AI question-answering prompt
    3. Call LLM provider with prompt + context
    4. Use formatting_skill to format response with source citations
    5. Return formatted answer
    
    TODO: Implement Physical AI question-answering logic
    TODO: Step 1: Call retrieve_content(query, chapter_id=3) to get more context if needed
    TODO: Step 2: Call build_prompt("ask-question", question, context, chapter_id=3) to construct Physical AI prompt
    TODO: Step 3: Call LLM provider with prompt + Physical AI context
    TODO: Step 4: Call format_response(response, "ask-question", chapter_id=3) to format with sources
    TODO: Extract source citations from retrieved Chapter 3 chunks
    TODO: Calculate confidence score based on retrieved Physical AI context relevance
    TODO: Add error handling for LLM failures
    
    Physical AI-specific considerations:
    - Use Physical AI analogies (sensors as eyes/ears, signal processing as filtering, perception as understanding)
    - Reference real-world examples (autonomous vehicles, robotics, drones)
    - Handle Physical AI terminology correctly (perception, sensors, computer vision, depth perception, signal processing, feature extraction)
    - Include section context when sectionId provided
    - Filter chunks by section_id for section-specific questions
    - Questions about: perception, sensors, computer vision, depth perception, signal processing, feature extraction
    - Section-specific: what-is-perception-in-physical-ai, types-of-sensors-in-robotics, computer-vision-depth-perception, signal-processing-basics-for-ai
    """
    # Placeholder return - no real question-answering logic
    return {
        "answer": "",
        "sources": [],
        "confidence": 0.0
    }

