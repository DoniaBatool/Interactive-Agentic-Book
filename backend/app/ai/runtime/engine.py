"""
AI Runtime Engine

Unified entry point for all AI block requests.
Routes requests to appropriate subagents, coordinates RAG pipeline,
selects LLM provider, and formats responses.
"""

from typing import Dict, Any

# Knowledge source mapping
knowledge_sources = {
    1: "chapter_1_chunks",  # Existing
    2: "chapter_2_chunks",  # NEW for Chapter 2
}

# TODO: Chapter 2 (ROS 2) RAG Integration
# When chapterId=2:
#   1. Import get_chapter_chunks from app.content.chapters.chapter_2_chunks
#   2. Call get_chapter_chunks(chapter_id=2) to retrieve Chapter 2 chunks
#   3. Use chunks for RAG retrieval (semantic search in Qdrant)
#   4. Filter chunks by section_id when sectionId provided in request
#   5. Pass Chapter 2 context (chunks + metadata) to subagents
#   6. Subagents will use ROS 2-specific context for LLM prompts:
#      - ROS 2 concepts: nodes, topics, services, actions, packages, launch-files
#      - ROS 2 analogies: post office, restaurant, phone calls, package delivery
#      - ROS 2 examples: TurtleBot 3, navigation stack, robot arm control
#
# RAG Pipeline Integration Flow:
#   1. Runtime engine calls run_rag_pipeline(query, chapter_id=2, top_k=5)
#   2. RAG pipeline returns context: {context: str, chunks: List, query_embedding: List}
#   3. Runtime engine passes context to subagent along with request_data
#   4. Subagent uses context in LLM prompt for generating response
#   5. LLM provider generates response with ROS 2 context


async def run_ai_block(
    block_type: str,
    request_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Unified AI block runtime entry point.
    
    Args:
        block_type: Type of AI block ("ask-question", "explain-like-10", "quiz", "diagram")
        request_data: Request payload matching block type:
            - "ask-question": {"question": str, "chapterId": int, "sectionId": str}
            - "explain-like-10": {"concept": str, "chapterId": int}
            - "quiz": {"chapterId": int, "numQuestions": int}
            - "diagram": {"diagramType": str, "chapterId": int, "concepts": List[str]}
    
    Returns:
        Formatted response for frontend (structure depends on block_type)
    
    Runtime Flow (all TODO):
    1. Router: Determine which subagent to use
    2. RAG: Retrieve relevant context
    3. LLM Selection: Choose provider based on config
    4. Subagent: Call appropriate subagent
    5. Response Formatting: Format output for frontend
    
    TODO: Implement routing, RAG, LLM selection, formatting
    TODO: Step 1: Map block_type to subagent function
    TODO: Step 2: Run RAG pipeline to get context
    TODO: Step 3: Select LLM provider from settings.ai_provider
    TODO: Step 4: Call appropriate subagent with request_data + context
    TODO: Step 5: Format response using formatting_skill
    TODO: Add error handling for invalid block_type
    TODO: Add error handling for subagent failures
    TODO: Add logging for runtime execution
    """
    # TODO: Route diagram block → diagram pipeline
    if block_type == "diagram":
        from app.ai.diagrams.pipeline import run_diagram_pipeline
        result = await run_diagram_pipeline(
            diagram_type=request_data.get("diagramType", ""),
            payload=request_data
        )
        return result
    
    # Step 1: Router - Determine which subagent to use (TODO)
    # SUBAGENT_MAP = {
    #     "ask-question": ask_question_agent,
    #     "explain-like-10": explain_el10_agent,
    #     "quiz": quiz_agent,
    # }
    # subagent = SUBAGENT_MAP.get(block_type)
    
    # Step 2: RAG - Retrieve relevant context (TODO)
    # context = await run_rag_pipeline(query, chapter_id)
    
    # TODO: Chapter 2 routing
    # chapter_id = request_data.get("chapterId", 1)
    # if chapter_id == 2:
    #     # TODO: Check ENABLE_CHAPTER_2_RUNTIME flag
    #     # from app.config.settings import ENABLE_CHAPTER_2_RUNTIME
    #     # if not ENABLE_CHAPTER_2_RUNTIME:
    #     #     return {"error": "Chapter 2 runtime disabled"}
    #     
    #     # TODO: Import Chapter 2 subagents
    #     # from app.ai.subagents.ch2_ask_question_agent import ch2_ask_question_agent
    #     # from app.ai.subagents.ch2_explain_el10_agent import ch2_explain_el10_agent
    #     # from app.ai.subagents.ch2_quiz_agent import ch2_quiz_agent
    #     # from app.ai.subagents.ch2_diagram_agent import ch2_diagram_agent
    #     
    #     # TODO: Route to Chapter 2 subagent
    #     # CH2_SUBAGENT_MAP = {
    #     #     "ask-question": ch2_ask_question_agent,
    #     #     "explain-like-10": ch2_explain_el10_agent,
    #     #     "quiz": ch2_quiz_agent,
    #     #     "diagram": ch2_diagram_agent,
    #     # }
    #     # subagent = CH2_SUBAGENT_MAP.get(block_type)
    #     # if not subagent:
    #     #     return {"error": f"Unknown block type: {block_type}"}
    #     
    #     # TODO: Load Chapter 2 RAG context
    #     # from app.ai.rag.pipeline import run_rag_pipeline
    #     # query = request_data.get("question") or request_data.get("concept") or ""
    #     # context = await run_rag_pipeline(query, chapter_id=2, top_k=5)
    #     
    #     # TODO: Placeholder LLM invocation for Chapter 2
    #     # LLM provider will be selected from DEFAULT_CH2_MODEL setting
    #     # LLM will receive ROS 2 context from RAG pipeline
    #     # LLM will generate response with ROS 2 knowledge
    #     
    #     # TODO: Call Chapter 2 subagent with context
    #     # result = await subagent(request_data, context)
    #     
    #     # TODO: Format response
    #     # from app.ai.skills.formatting_skill import format_response
    #     # formatted = format_response(result, block_type, chapter_id=2)
    #     # return formatted
    # elif chapter_id == 1:
    #     from app.content.chapters.chapter_1_chunks import get_chapter_chunks
    #     chunks = get_chapter_chunks(chapter_id=1)
    #     # Existing Chapter 1 logic
    # else:
    #     raise ValueError(f"Unknown chapter_id: {chapter_id}")
    
    # Step 3: LLM Selection - Choose provider based on config (TODO)
    # provider = get_provider()  # Based on settings.ai_provider
    
    # Step 4: Subagent - Call appropriate subagent (TODO)
    # result = await subagent(request_data, context)
    
    # Step 5: Response Formatting - Format output for frontend (TODO)
    # formatted = format_response(result, block_type)
    
    # Placeholder return - no real runtime execution
    return {
        "message": "placeholder",
        "data": {}
    }

