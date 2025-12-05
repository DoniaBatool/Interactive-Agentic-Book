"""
AI Runtime Engine

Unified entry point for all AI block requests.
Routes requests to appropriate subagents, coordinates RAG pipeline,
selects LLM provider, and formats responses.
"""

from typing import Dict, Any


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

