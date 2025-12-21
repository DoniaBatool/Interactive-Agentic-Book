"""
Agents/ChatKit integration using OpenAI function calling.

This module implements an agent-based chat system where RAG retrieval
is exposed as a tool that the agent can call when needed.
"""
import json
import logging
import time
from typing import AsyncIterable, List, Optional, Tuple

from fastapi import HTTPException
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageToolCall

from app.core.config import get_settings
from app.models.schemas.chat import ChatRequest, ChatResponse, Citation
from app.services.retrieval import retrieve_chunks


logger = logging.getLogger(__name__)
settings = get_settings()


def _log_event(event: str, **fields) -> None:
    """Structured JSON logging for agent telemetry."""
    payload = {"event": event, **fields}
    logger.info(json.dumps(payload))


def _get_rag_tool_definition() -> dict:
    """Define the RAG retrieval tool for OpenAI function calling."""
    return {
        "type": "function",
        "function": {
            "name": "retrieve_book_context",
            "description": "Retrieve relevant context from the Physical AI & Humanoid Robotics textbook. Use this when you need to answer questions about course content, concepts, modules, or any information from the book.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query or question to find relevant textbook content. Can be a question, topic, or keyword.",
                    },
                    "chapter": {
                        "type": "string",
                        "description": "Optional: Filter by specific chapter name (e.g., 'Introduction to Physical AI', 'ROS 2 Nervous System').",
                    },
                    "section": {
                        "type": "string",
                        "description": "Optional: Filter by specific section within a chapter.",
                    },
                },
                "required": ["query"],
            },
        },
    }


def _execute_rag_tool(
    tool_call: ChatCompletionMessageToolCall,
    filters: Optional[dict] = None,
) -> Tuple[str, List[Citation]]:
    """
    Execute the RAG retrieval tool and return formatted context with citations.
    
    Returns:
        Tuple of (formatted_context_string, list_of_citations)
    """
    try:
        arguments = json.loads(tool_call.function.arguments)
        query = arguments.get("query", "")
        chapter = arguments.get("chapter") or (filters.get("chapter") if filters else None)
        section = arguments.get("section") or (filters.get("section") if filters else None)
        
        if not query:
            return "No query provided.", []
        
        # Use existing retrieval logic
        from app.models.schemas.chat import ChatFilters
        chat_filters = ChatFilters(chapter=chapter, section=section) if chapter or section else None
        
        top_k = settings.retrieval_top_k
        retrieved = retrieve_chunks(query, chat_filters, top_k)
        
        # Format context blocks and citations
        context_blocks = []
        citations: List[Citation] = []
        for text, path, chap, sec, score in retrieved:
            context_blocks.append(f"[{chap}] {text}")
            citations.append(Citation(path=path, chapter=chap, section=sec, score=score))
        
        formatted_context = "\n\n".join(context_blocks)
        return formatted_context, citations
        
    except Exception as e:
        logger.exception(f"Error executing RAG tool: {e}")
        return f"Error retrieving context: {str(e)}", []


async def generate_agent_answer(payload: ChatRequest) -> ChatResponse:
    """
    Generate answer using OpenAI Agents with function calling.
    
    The agent can decide when to call the RAG retrieval tool based on the question.
    """
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    
    stream = payload.stream if payload.stream is not None else settings.default_stream
    _log_start(payload, stream)
    
    start = time.time()
    client = OpenAI(api_key=settings.openai_api_key)
    
    # Prepare filters for tool execution
    filters_dict = {}
    if payload.filters:
        if payload.filters.chapter:
            filters_dict["chapter"] = payload.filters.chapter
        if payload.filters.section:
            filters_dict["section"] = payload.filters.section
    
    # System message for the agent
    current_context = ""
    if payload.filters and payload.filters.chapter:
        current_context = f"\n\nIMPORTANT: The user is currently viewing the chapter/page: '{payload.filters.chapter}'. When they ask about 'this page', 'current page', or 'what I'm reading', they are referring to this chapter. Use the retrieve_book_context tool with this chapter filter to find relevant content."
    
    # User personalization context
    user_context = ""
    if payload.user_context:
        user_info = []
        if payload.user_context.software_level:
            user_info.append(f"Software Level: {payload.user_context.software_level}")
        if payload.user_context.hardware_level:
            user_info.append(f"Hardware Level: {payload.user_context.hardware_level}")
        if payload.user_context.technologies:
            known_tech = [tech for tech, knows in payload.user_context.technologies.items() if knows]
            if known_tech:
                user_info.append(f"Known Technologies: {', '.join(known_tech)}")
        if payload.user_context.learning_goals:
            user_info.append(f"Learning Goals: {payload.user_context.learning_goals}")
        
        if user_info:
            user_context = f"\n\nUSER PROFILE: {' | '.join(user_info)}\nAdapt your explanations to match their experience level. For beginners, provide more detailed explanations and avoid jargon. For advanced users, you can use technical terminology and focus on implementation details."
    
    system_message = (
        "You are an AI assistant for the Physical AI & Humanoid Robotics textbook. "
        "You help students understand concepts, answer questions, and provide explanations. "
        "When you need information from the textbook, use the retrieve_book_context tool. "
        "Always cite sources when using information from the book."
        f"{current_context}"
        f"{user_context}"
    )
    
    # Initial user message
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": payload.question},
    ]
    
    # Get tool definition
    tools = [_get_rag_tool_definition()]
    
    # First call: agent decides if tool is needed
    response = client.chat.completions.create(
        model=settings.chat_model,
        messages=messages,
        tools=tools,
        tool_choice="auto",  # Let agent decide
        stream=False,
    )
    
    if not response.choices or not response.choices[0].message:
        raise HTTPException(status_code=500, detail="OpenAI agent response error")
    
    message = response.choices[0].message
    all_citations: List[Citation] = []
    
    # Handle tool calls if agent requested them
    if message.tool_calls:
        tool_results = []
        for tool_call in message.tool_calls:
            if tool_call.function.name == "retrieve_book_context":
                context, citations = _execute_rag_tool(tool_call, filters_dict)
                all_citations.extend(citations)
                tool_results.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": "retrieve_book_context",
                    "content": f"Retrieved context from textbook:\n\n{context}",
                })
        
        # Add tool results to conversation
        messages.append(message)
        messages.extend(tool_results)
        
        # Second call: agent generates final answer with context
        response = client.chat.completions.create(
            model=settings.chat_model,
            messages=messages,
            tools=tools,
            tool_choice="none",  # No more tools needed
            stream=False,
        )
        
        if not response.choices or not response.choices[0].message:
            raise HTTPException(status_code=500, detail="OpenAI agent final response error")
        
        message = response.choices[0].message
    
    answer = message.content or "I couldn't generate an answer."
    
    duration_ms = int((time.time() - start) * 1000)
    _log_done(False, duration_ms, len(all_citations))
    
    return ChatResponse(answer=answer, citations=all_citations, stream=False)


async def stream_agent_answer(payload: ChatRequest) -> AsyncIterable[str]:
    """
    Stream answer using OpenAI Agents with function calling.
    
    Note: Streaming with function calling is more complex. This implementation
    handles tool calls in a non-streaming first pass, then streams the final answer.
    """
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    
    _log_start(payload, True)
    start = time.time()
    
    client = OpenAI(api_key=settings.openai_api_key)
    
    # Prepare filters
    filters_dict = {}
    if payload.filters:
        if payload.filters.chapter:
            filters_dict["chapter"] = payload.filters.chapter
        if payload.filters.section:
            filters_dict["section"] = payload.filters.section
    
    # Prepare context-aware system message
    current_context = ""
    if payload.filters and payload.filters.chapter:
        current_context = f"\n\nIMPORTANT: The user is currently viewing the chapter/page: '{payload.filters.chapter}'. When they ask about 'this page', 'current page', or 'what I'm reading', they are referring to this chapter. Use the retrieve_book_context tool with this chapter filter to find relevant content."
    
    system_message = (
        "You are an AI assistant for the Physical AI & Humanoid Robotics textbook. "
        "You help students understand concepts, answer questions, and provide explanations. "
        "When you need information from the textbook, use the retrieve_book_context tool. "
        "Always cite sources when using information from the book."
        f"{current_context}"
    )
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": payload.question},
    ]
    
    tools = [_get_rag_tool_definition()]
    all_citations: List[Citation] = []
    
    def _format_sse(event: str, data: dict) -> str:
        return f"event: {event}\ndata: {json.dumps(data)}\n\n"
    
    try:
        # First call: check if tool is needed
        response = client.chat.completions.create(
            model=settings.chat_model,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            stream=False,
        )
        
        if not response.choices or not response.choices[0].message:
            yield _format_sse("error", {"message": "Agent response error"})
            return
        
        message = response.choices[0].message
        
        # Handle tool calls
        if message.tool_calls:
            tool_results = []
            for tool_call in message.tool_calls:
                if tool_call.function.name == "retrieve_book_context":
                    context, citations = _execute_rag_tool(tool_call, filters_dict)
                    all_citations.extend(citations)
                    tool_results.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": "retrieve_book_context",
                        "content": f"Retrieved context from textbook:\n\n{context}",
                    })
            
            messages.append(message)
            messages.extend(tool_results)
            
            # Stream final answer
            stream = client.chat.completions.create(
                model=settings.chat_model,
                messages=messages,
                tools=tools,
                tool_choice="none",
                stream=True,
            )
            
            # Send metadata first
            yield _format_sse(
                "metadata",
                {"citations": [c.model_dump() for c in all_citations], "stream": True},
            )
            
            # Stream tokens
            for chunk in stream:
                if not chunk or not getattr(chunk, "choices", None):
                    continue
                delta = chunk.choices[0].delta.content
                if delta:
                    yield _format_sse("token", {"text": delta})
        else:
            # No tool calls, stream directly
            yield _format_sse(
                "metadata",
                {"citations": [], "stream": True},
            )
            
            # Re-stream the message content (since we got it non-streaming)
            if message.content:
                for char in message.content:
                    yield _format_sse("token", {"text": char})
        
        duration_ms = int((time.time() - start) * 1000)
        _log_done(True, duration_ms, len(all_citations))
        yield _format_sse("done", {"duration_ms": duration_ms})
        
    except Exception as exc:
        logger.exception("agent.stream.error")
        _log_event("agent.error", stream=True, error=str(exc))
        yield _format_sse("error", {"message": "Agent stream failed"})


def _log_start(payload: ChatRequest, stream: bool) -> None:
    filters = payload.filters.model_dump(exclude_none=True) if payload.filters else None
    _log_event(
        "agent.start",
        stream=stream,
        filters=filters,
        question_length=len(payload.question),
    )


def _log_done(stream: bool, duration_ms: int, retrieved_count: int) -> None:
    _log_event(
        "agent.done",
        stream=stream,
        duration_ms=duration_ms,
        retrieved=retrieved_count,
    )
