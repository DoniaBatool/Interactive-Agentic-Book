"""
Abstract Base LLM Provider Interface

Defines the standard interface for all LLM providers (OpenAI, Gemini, DeepSeek).
All provider implementations must extend this base class.
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any


class BaseLLMProvider(ABC):
    """
    Abstract base class for LLM providers.
    
    This interface standardizes how different LLM providers (OpenAI, Gemini, DeepSeek)
    are called, ensuring consistent behavior across providers.
    
    All provider implementations must implement the generate() method.
    """
    
    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        messages: Optional[List[Dict[str, str]]] = None,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """
        Generate response from LLM.
        
        Args:
            prompt: User prompt text (required)
            system: Optional system message for role definition
            messages: Optional conversation history in format:
                [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]
            temperature: Sampling temperature (0.0-2.0), default 0.7
        
        Returns:
            Dictionary with structure:
            {
                "text": str,              # Generated text response
                "metadata": {
                    "model": str,          # Model used
                    "tokens": int,         # Token count
                    "finish_reason": str   # Completion reason
                }
            }
        
        TODO: Implement in provider subclasses
        """
        pass

