"""
Base Agent Interface

Abstract base class for all subagents.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAgent(ABC):
    """
    Base interface for all subagents.
    
    TODO: Future polymorphism support
    TODO: Add common methods shared by all subagents
    TODO: Add error handling patterns
    TODO: Add logging patterns
    """
    
    @abstractmethod
    async def run(self, request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Abstract method for processing AI block requests.
        
        Args:
            request_data: Request payload with block-specific data (question, concept, etc.)
            context: RAG context from pipeline (context string, chunks, query_embedding)
        
        Returns:
            Formatted response for frontend
        
        TODO: Define common request structure
        TODO: Define common response structure
        TODO: Add validation for request structure
        """
        pass

