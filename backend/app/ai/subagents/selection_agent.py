"""
Selection Agent

Subagent for processing selection-based RAG queries.
Coordinates with selection skills to process user selections and questions.

TODO: Real AI logic will be implemented in a future feature.
Currently returns placeholder responses.
"""

from typing import Dict, Any
from app.ai.subagents.base_agent import BaseAgent
from app.ai.skills.selection_cleaning_skill import clean_selection
from app.ai.skills.selection_context_skill import build_selection_context


class SelectionAgent(BaseAgent):
    """
    Agent for processing selection-based RAG queries.
    
    Input Schema:
        {
            "selected_text": str,      # Text selected by user (10-5000 chars)
            "question": str,            # User's question (5-500 chars)
            "chapter_id": int          # Chapter number (1-999)
        }
    
    Output Schema:
        {
            "answer": str,             # Generated answer
            "context_used": str        # Context extracted from selection
        }
    
    TODO: Implement core selection-based reasoning
    TODO: Integrate with selection pipeline
    TODO: Use selection skills for cleaning and context building
    TODO: Call LLM provider with selection context
    TODO: Format response for frontend
    """
    
    async def run(self, request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a selection-based RAG request.
        
        Args:
            request_data: Request payload with selected_text, question, chapter_id
            context: Additional context (optional)
        
        Returns:
            Formatted response with answer and context_used
        
        TODO: Extract selected_text, question, chapter_id from request_data
        TODO: Use selection_cleaning_skill to clean selected text
        TODO: Use selection_context_skill to build context
        TODO: Call selection pipeline functions
        TODO: Generate answer using LLM with selection context
        TODO: Format and return response
        """
        # Extract request data
        selected_text = request_data.get("selected_text", "")
        question = request_data.get("question", "")
        chapter_id = request_data.get("chapter_id", 1)
        
        # TODO: Use selection cleaning skill
        cleaned_text = clean_selection(selected_text)
        
        # TODO: Use selection context skill
        context_str = build_selection_context(cleaned_text, question)
        
        # Placeholder response
        return {
            "answer": "placeholder answer",
            "context_used": cleaned_text[:200] + "..." if len(cleaned_text) > 200 else cleaned_text
        }

