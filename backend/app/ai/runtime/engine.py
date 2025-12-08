"""
AI Runtime Engine

Unified entry point for all AI block requests.
Routes requests to appropriate subagents, coordinates RAG pipeline,
selects LLM provider, and formats responses.
"""

from typing import Dict, Any, Optional
from app.ai.subagents.registry import get_subagent
from app.ai.runtime.output_formatter import format_ai_block_response
from app.ai.rag.pipeline import run_rag_pipeline
from app.ai.guardrails.engine import process_input_safely, enforce_output_rules, inject_safety_prefix, inject_safety_suffix
from app.ai.guardrails.hallucination_filter import detect_low_confidence, require_citation_for_facts, fallback_to_neutral_explanation

# Knowledge source mapping
knowledge_sources = {
    1: "chapter_1_chunks",  # Existing
    2: "chapter_2_chunks",  # NEW for Chapter 2
    3: "chapter_3_chunks",  # NEW for Chapter 3
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
    # TODO: Chapter 2 diagram routing
    # if block_type == "diagram" AND chapterId == 2:
    #     from app.ai.diagram.ch2_diagram_runtime import run as ch2_diagram_run
    #     result = await ch2_diagram_run(
    #         diagram_type=request_data.get("diagramType", ""),
    #         chapter_id=2,
    #         concepts=request_data.get("concepts", [])
    #     )
    #     return result
    # Routes Chapter 2 diagram requests to ch2_diagram_runtime (placeholder routing)
    
    # TODO: Chapter 2 ELI10 routing
    # if block_type == "explain-like-i-am-10" AND chapterId == 2:
    #     from app.ai.explain.ch2_el10_runtime import run as ch2_el10_run
    #     result = await ch2_el10_run(
    #         concept=request_data.get("concept", ""),
    #         chapter_id=2,
    #         context=request_data.get("context")
    #     )
    #     return result
    # Routes Chapter 2 ELI10 requests to ch2_el10_runtime (placeholder routing)
    
    # TODO: Chapter 3 routing
    # if request_data.get("chapterId") == 3:
    #     # TODO: Route to Chapter 3 RAG pipeline
    #     # TODO: Call run_rag_pipeline(query, chapter_id=3, top_k=5)
    #     # TODO: Call Chapter 3 subagents (ch3_ask_agent, ch3_explain_agent, ch3_quiz_agent, ch3_diagram_agent)
    #     # TODO: Return Chapter 3 response
    #     pass
    
    # TODO: Chapter 2 quiz routing
    # if block_type == "interactive-quiz" AND chapterId == 2:
    #     from app.ai.quiz.ch2_quiz_runtime import run as ch2_quiz_run
    #     result = await ch2_quiz_run(
    #         chapter_id=2,
    #         num_questions=request_data.get("numQuestions", 5),
    #         learning_objectives=request_data.get("learningObjectives")
    #     )
    #     return result
    # Routes Chapter 2 quiz requests to ch2_quiz_runtime (placeholder routing)
    
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
    chapter_id = request_data.get("chapterId", 1)
    if chapter_id == 2:
        # TODO: Route to Chapter 2 subagent
        # TODO: Import Chapter 2 subagents
        # TODO: from app.ai.subagents.ch2_ask_agent import Ch2AskAgent
        # TODO: from app.ai.subagents.ch2_explain_agent import Ch2ExplainAgent
        # TODO: from app.ai.subagents.ch2_quiz_agent import Ch2QuizAgent
        # TODO: from app.ai.subagents.ch2_diagram_agent import Ch2DiagramAgent
        # TODO: CH2_SUBAGENT_MAP = {
        # TODO:     "ask-question": Ch2AskAgent(),
        # TODO:     "explain-like-i-am-10": Ch2ExplainAgent(),
        # TODO:     "interactive-quiz": Ch2QuizAgent(),
        # TODO:     "generate-diagram": Ch2DiagramAgent()
        # TODO: }
        # TODO: subagent = CH2_SUBAGENT_MAP.get(block_type)
        
        # TODO: When chapterId=2, call run_ch2_rag_pipeline()
        # TODO: Import ch2_pipeline for Chapter 2 RAG operations
        # TODO: from app.ai.rag.ch2_pipeline import run_ch2_rag_pipeline
        # TODO: Extract query from request_data
        # TODO: query = request_data.get("question") or request_data.get("concept") or ""
        # TODO: Call run_ch2_rag_pipeline(query, top_k=5) to get context
        # TODO: context = await run_ch2_rag_pipeline(query, top_k=5)
        # TODO: Pass context to Chapter 2 subagents
        # TODO: Routing rules: chapter="2" → use ch2_pipeline
        
        # TODO: Select provider for Chapter 2
        # TODO: Use settings.ch2_llm_model for Chapter 2 (if configured)
        # TODO: Fallback to default provider if Chapter 2 model not configured
        
        # TODO: Call appropriate Chapter 2 subagent
        # TODO: result = await subagent.run({"input": request_data, "context": context})
        
        # TODO: Format response
        # TODO: from app.ai.skills.formatting_skill import format_response
        # TODO: formatted = format_response(result, block_type, chapter_id=2)
        # TODO: return formatted
        
        # Expected flow: request → pipeline (chapter_id=2) → provider → subagent → formatter → response
        pass
    elif chapter_id == 3:
        # Chapter 3 routing - Real implementation
        from app.ai.subagents.ch3.ask_question_agent import Ch3AskQuestionAgent
        from app.ai.subagents.ch3.explain_el10_agent import Ch3ExplainEl10Agent
        from app.ai.subagents.ch3.quiz_agent import Ch3QuizAgent
        from app.ai.subagents.ch3.diagram_agent import Ch3DiagramAgent
        from app.ai.rag.pipeline import run_rag_pipeline
        
        # Map block_type to Ch3*Agent classes
        CH3_SUBAGENT_MAP = {
            "ask-question": Ch3AskQuestionAgent(),
            "explain-like-10": Ch3ExplainEl10Agent(),
            "quiz": Ch3QuizAgent(),
            "diagram": Ch3DiagramAgent()
        }
        
        subagent = CH3_SUBAGENT_MAP.get(block_type)
        if not subagent:
            return {"error": f"Unknown block type: {block_type} for Chapter 3"}
        
        # RAG stage - Load Chapter 3 RAG context
        # Extract query from request_data based on block_type
        query = ""
        if block_type == "ask-question":
            query = request_data.get("question", "")
        elif block_type == "explain-like-10":
            query = request_data.get("concept", "")
        elif block_type == "quiz":
            # For quiz, use a general query or empty string to get all sections
            query = "quiz questions about Physical AI"
        elif block_type == "diagram":
            # For diagram, use diagram type and concepts
            diagram_type = request_data.get("diagramType", "")
            concepts = request_data.get("concepts", [])
            query = f"{diagram_type} diagram about {', '.join(concepts) if concepts else 'Physical AI'}"
        
        # Get section_id if provided
        section_id = request_data.get("sectionId")
        
        # Call RAG pipeline to get context
        context = await run_rag_pipeline(
            query=query,
            chapter_id=3,
            top_k=5,
            section_id=section_id
        )
        
        # Call Chapter 3 subagent with request_data and context
        result = await subagent.run(request_data, context)
        
        return result
    elif chapter_id == 1:
        # Existing Chapter 1 logic
        pass
    else:
        # TODO: Handle unknown chapter_id
        pass
    
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


# TODO: Chapter 2 handler functions
async def handle_ch2_ask_question(
    request_data: Dict[str, Any],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Handle Chapter 2 ask-question block.
    
    Args:
        request_data: Request payload with question and chapterId=2
        context: RAG context from Chapter 2 collection
    
    Returns:
        Formatted response with answer
    
    TODO: Implement Chapter 2 ask-question handler
    TODO: Call ch2_ask_question_agent with request_data and context
    TODO: Format response for frontend
    """
    return {"answer": "TODO: Implement Chapter 2 ask-question handler"}


async def handle_ch2_explain_el10(
    request_data: Dict[str, Any],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Handle Chapter 2 explain-like-10 block.
    
    Args:
        request_data: Request payload with concept and chapterId=2
        context: RAG context from Chapter 2 collection
    
    Returns:
        Formatted response with explanation
    
    TODO: Implement Chapter 2 explain-like-10 handler
    TODO: Call ch2_el10_agent with request_data and context
    TODO: Format response for frontend
    """
    return {"explanation": "TODO: Implement Chapter 2 explain-like-10 handler"}


async def handle_ch2_quiz(
    request_data: Dict[str, Any],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Handle Chapter 2 quiz block.
    
    Args:
        request_data: Request payload with chapterId=2 and numQuestions
        context: RAG context from Chapter 2 collection
    
    Returns:
        Formatted response with quiz questions
    
    TODO: Implement Chapter 2 quiz handler
    TODO: Call ch2_quiz_agent with request_data and context
    TODO: Format response for frontend
    """
    return {"quiz": "TODO: Implement Chapter 2 quiz handler"}


async def handle_ch2_diagram(
    request_data: Dict[str, Any],
    context: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Handle Chapter 2 diagram block.
    
    Args:
        request_data: Request payload with diagramType, chapterId=2, and concepts
        context: RAG context from Chapter 2 collection
    
    Returns:
        Formatted response with diagram
    
    TODO: Implement Chapter 2 diagram handler
    TODO: Call ch2_diagram_agent with request_data and context
    TODO: Format response for frontend
    """
    return {"diagram": "TODO: Implement Chapter 2 diagram handler"}


def load_chapter_overrides(chapter_id: int) -> Optional[Dict[str, Any]]:
    """
    Load chapter-specific overrides if file exists.
    
    Args:
        chapter_id: Chapter ID
    
    Returns:
        CHAPTER_OVERRIDES dict if file exists, None otherwise
    """
    try:
        # Dynamic import of override module
        override_module_name = f"app.content.overrides.chapter_{chapter_id}"
        override_module = __import__(override_module_name, fromlist=["CHAPTER_OVERRIDES"])
        overrides = getattr(override_module, "CHAPTER_OVERRIDES", None)
        if overrides and isinstance(overrides, dict):
            return overrides
    except (ImportError, AttributeError):
        # Override file doesn't exist or doesn't have CHAPTER_OVERRIDES
        pass
    return None


async def ai_block_router(
    block_type: str,
    chapter_id: int,
    user_input: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Global AI block router - unified routing for all chapters.
    
    Args:
        block_type: Type of AI block ("ask-question", "explain-like-el10", "interactive-quiz", "diagram-generator")
        chapter_id: Chapter ID (1, 2, 3, ...)
        user_input: Block-specific input data
    
    Returns:
        Standardized response structure based on block_type
    
    Flow:
        1. Process input safely (guardrails)
        2. Extract query from user_input based on block_type
        3. Call unified RAG pipeline (with hallucination-check placeholder)
        4. Load chapter overrides (if exists)
        5. Get subagent from registry
        6. Call subagent with standardized request (subagent uses safety prefix/suffix)
        7. Enforce output rules (guardrails)
        8. Check hallucination
        9. Format response using unified formatter
    """
    try:
        # Step 1: Process input safely (guardrails)
        # TODO: Extract input text from user_input for safety check
        input_text = str(user_input)  # Placeholder: convert to string for safety check
        input_result = process_input_safely(input_text, block_type, chapter_id)
        if not input_result["is_safe"]:
            return {
                "error": input_result.get("fallback_message", "Input blocked by safety rules"),
                "code": "CONTENT_BLOCKED",
                "details": input_result.get("details", {})
            }
        
        # Step 2: Extract query from user_input based on block_type
        query = ""
        if block_type == "ask-question":
            query = user_input.get("question", "")
        elif block_type == "explain-like-el10":
            query = user_input.get("concept", "")
        elif block_type == "interactive-quiz":
            query = "quiz questions"  # General query for quiz
        elif block_type == "diagram-generator":
            diagram_type = user_input.get("diagramType", "")
            concepts = user_input.get("concepts", [])
            query = f"{diagram_type} diagram about {', '.join(concepts) if concepts else 'chapter content'}"
        else:
            return {
                "error": f"Unknown block type: {block_type}",
                "code": "INVALID_INPUT",
                "details": {"block_type": block_type}
            }
        
        # Step 3: Call unified RAG pipeline (with hallucination-check placeholder)
        section_id = user_input.get("sectionId")
        context = await run_rag_pipeline(
            query=query,
            chapter_id=chapter_id,
            top_k=5,
            section_id=section_id
        )
        # TODO: Pass context through hallucination-check placeholder
        # context = check_context_for_hallucination(context)  # Placeholder
        
        # Step 4: Load chapter overrides (if exists)
        overrides = load_chapter_overrides(chapter_id)
        
        # Step 5: Get subagent from registry
        subagent_class = get_subagent(block_type, chapter_id)
        if not subagent_class:
            return {
                "error": f"No subagent registered for block type '{block_type}' and chapter {chapter_id}",
                "code": "SUBAGENT_NOT_FOUND",
                "details": {"block_type": block_type, "chapter_id": chapter_id}
            }
        
        # Step 6: Call subagent with standardized request
        # Note: Subagent should use safety prefix/suffix via prompt_builder_skill
        request_data = {
            "block_type": block_type,
            "chapterId": chapter_id,
            **user_input
        }
        subagent = subagent_class()
        result = await subagent.run(request_data, context)
        
        # Step 7: Enforce output rules (guardrails)
        # Extract text from result for safety check
        result_text = result.get("text", result.get("answer", result.get("explanation", str(result))))
        output_result = enforce_output_rules(result_text, block_type, chapter_id)
        if not output_result["is_safe"]:
            # Return fallback message
            return {
                "error": output_result.get("fallback_message", "Output blocked by safety rules"),
                "code": "CONTENT_BLOCKED",
                "details": output_result.get("details", {})
            }
        
        # Step 8: Check hallucination
        hallucination_result = detect_low_confidence(result, context)
        if hallucination_result["is_low_confidence"] or hallucination_result["requires_citations"]:
            # TODO: Require citations or use fallback
            if hallucination_result["recommended_action"] == "fallback":
                fallback_text = fallback_to_neutral_explanation(result_text)
                result["text"] = fallback_text
                result["answer"] = fallback_text  # Update result with fallback
        
        # Step 9: Format response using unified formatter
        formatted = format_ai_block_response(block_type, result, chapter_id, overrides)
        
        # Step 10: Translation hook (if needed)
        # TODO: If translation needed, call translation pipeline before response
        # TODO: Check if target_language is provided in user_input
        # TODO: If target_language != "en", call translate_snippet() or translate_chapter()
        # TODO: Return translated response
        
        # Step 11: Streaming hook (if enabled)
        # TODO: If streaming mode enabled, yield tokens instead of returning complete response
        # TODO: Check settings.ai_streaming_enabled
        # TODO: If enabled, yield tokens as AsyncGenerator
        # TODO: Format tokens as streaming chunks
        
        return formatted
        
    except Exception as e:
        # TODO: Add proper error logging
        return {
            "error": f"Error processing AI block: {str(e)}",
            "code": "PROCESSING_ERROR",
            "details": {"block_type": block_type, "chapter_id": chapter_id}
        }

