"""
Abstract Base Diagram Provider Interface

Defines the standard interface for all diagram providers (OpenAI, Gemini).
All provider implementations must extend this base class.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseDiagramProvider(ABC):
    """
    Abstract base class for diagram providers.
    
    This interface standardizes how different diagram providers (OpenAI, Gemini)
    are called, ensuring consistent behavior across providers.
    
    All provider implementations must implement the generate_diagram() method.
    """
    
    @abstractmethod
    async def generate_diagram(
        self,
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate diagram from payload.
        
        Args:
            payload: Dictionary with structure:
                {
                    "diagram_type": str,        # "anatomy_robot", "physical_ai_overview", etc.
                    "concepts": List[str],      # Concepts to include
                    "chapter_id": int,          # Chapter identifier
                    "format": str                # "svg", "png", "mermaid"
                }
        
        Returns:
            Dictionary with structure:
            {
                "svg": str,                     # SVG string or diagram code
                "format": str,                  # Output format
                "metadata": Dict[str, Any]       # Additional metadata
            }
        
        TODO: Implement in provider subclasses
        """
        pass

