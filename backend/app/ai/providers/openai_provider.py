"""
OpenAI Provider Implementation

Real OpenAI API integration.
This provider implements the BaseLLMProvider interface for OpenAI models.
"""

from app.ai.providers.base_llm import BaseLLMProvider
from app.config.settings import settings
from openai import AsyncOpenAI
from typing import Optional, List, Dict, Any
import logging

# TODO: Add proper logging configuration
logger = logging.getLogger(__name__)

# Initialize OpenAI client
_client: Optional[AsyncOpenAI] = None


def _get_client() -> AsyncOpenAI:
    """Get or create OpenAI client instance."""
    global _client
    if _client is None:
        if not settings.openai_api_key:
            raise ValueError("OpenAI API key not configured. Set OPENAI_API_KEY environment variable.")
        _client = AsyncOpenAI(api_key=settings.openai_api_key)
    return _client


class OpenAIProvider(BaseLLMProvider):
    """
    OpenAI provider implementation.
    
    This class implements the BaseLLMProvider interface for OpenAI models
    (GPT-4o, GPT-4o-mini, etc.).
    """
    
    async def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        messages: Optional[List[Dict[str, str]]] = None,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """
        Generate response using OpenAI API.
        
        Args:
            prompt: User prompt text
            system: Optional system message
            messages: Optional conversation history
            temperature: Sampling temperature (0.0-2.0)
        
        Returns:
            Dictionary with OpenAI response structure:
            {
                "text": str,              # Generated text response
                "metadata": {
                    "model": str,          # Model used
                    "tokens": int,         # Token count
                    "finish_reason": str   # Completion reason
                }
            }
        """
        try:
            client = _get_client()
            
            # Build messages array
            message_list: List[Dict[str, str]] = []
            if system:
                message_list.append({"role": "system", "content": system})
            
            if messages:
                message_list.extend(messages)
            else:
                message_list.append({"role": "user", "content": prompt})
            
            # Select model
            model = settings.llm_model or settings.default_runtime_model or "gpt-4o-mini"
            
            # Call OpenAI API
            response = await client.chat.completions.create(
                model=model,
                messages=message_list,  # type: ignore
                temperature=temperature
            )
            
            # Extract response
            choice = response.choices[0]
            text = choice.message.content or ""
            
            # Extract metadata
            metadata = {
                "model": response.model,
                "tokens": response.usage.total_tokens if response.usage else 0,
                "finish_reason": choice.finish_reason or "stop"
            }
            
            return {
                "text": text,
                "metadata": metadata
            }
            
        except Exception as e:
            # TODO: Add proper error logging
            logger.error(f"OpenAI API error: {str(e)}")
            raise

