"""
Selection Runtime Engine

Runtime engine for processing selection-based RAG queries.
Coordinates between selection pipeline, selection agent, and LLM providers.

TODO: Real AI logic will be implemented in a future feature.
Currently returns placeholder responses.
"""

from typing import Dict, Any
from app.ai.rag.selection_pipeline import (
    clean_selected_text,
    embed_selected_text,
    run_similarity_search_over_selected,
    build_context,
    pass_context_to_llm
)
from app.ai.subagents.selection_agent import SelectionAgent


async def process_selection_rag(
    selected_text: str,
    question: str,
    chapter_id: int
) -> Dict[str, str]:
    """
    Process a selection-based RAG query.
    
    Args:
        selected_text: Text selected by user
        question: User's question about the selection
        chapter_id: Chapter number where selection was made
    
    Returns:
        Dictionary with answer and context_used
    
    TODO: Build prompt template
    TODO: Call selection pipeline
    TODO: Call LLM provider
    TODO: Format response
    TODO: Integrate with selection agent
    """
    # TODO: Clean selected text
    cleaned_text = clean_selected_text(selected_text)
    
    # TODO: Embed selected text
    embedding = embed_selected_text(cleaned_text)
    
    # TODO: Perform similarity search
    search_results = run_similarity_search_over_selected(cleaned_text, question)
    
    # TODO: Build context
    context = build_context(cleaned_text, search_results)
    
    # TODO: Call LLM with context
    answer = pass_context_to_llm(context, question)
    
    # Placeholder response
    return {
        "answer": answer,
        "context_used": cleaned_text[:200] + "..." if len(cleaned_text) > 200 else cleaned_text
    }

