"""
Gemini Provider Implementation

Real Google Gemini API integration.
This provider implements the BaseLLMProvider interface for Gemini models.
"""

from app.ai.providers.base_llm import BaseLLMProvider
from app.config.settings import settings
from google import genai
from typing import Optional, List, Dict, Any
import logging
import os

# TODO: Add proper logging configuration
logger = logging.getLogger(__name__)

# Initialize Gemini client
_client: Optional[genai.Client] = None


def _get_client() -> genai.Client:
    """Get or create Gemini client instance."""
    global _client
    if _client is None:
        api_key = settings.gemini_api_key or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Gemini API key not configured. Set GEMINI_API_KEY environment variable or gemini_api_key in settings.")
        _client = genai.Client(api_key=api_key)
    return _client


class GeminiProvider(BaseLLMProvider):
    """
    Gemini provider implementation.
    
    This class implements the BaseLLMProvider interface for Google Gemini models
    (gemini-pro, gemini-2.0-flash, etc.).
    
    TODO: Add native safety settings integration
    - Gemini safety settings (HARM_CATEGORY_*)
    - Block threshold configuration
    - Content filtering settings
    """
    
    async def generate(
        self,
        prompt: str,
        system: Optional[str] = None,
        messages: Optional[List[Dict[str, str]]] = None,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """
        Generate response using Gemini API.
        
        Args:
            prompt: User prompt text
            system: Optional system message
            messages: Optional conversation history (not fully supported in this minimal implementation)
            temperature: Sampling temperature (0.0-2.0)
        
        Returns:
            Dictionary with Gemini response structure:
            {
                "text": str,              # Generated text response
                "metadata": {
                    "model": str,          # Model used
                    "tokens": int,         # Token count (estimated)
                    "finish_reason": str   # Completion reason
                }
            }
        """
        try:
            client = _get_client()
            
            # Build prompt (Gemini uses single prompt string, not messages)
            full_prompt = prompt
            if system:
                full_prompt = f"{system}\n\n{prompt}"
            
            # Select model
            model = settings.llm_model or settings.default_runtime_model or "gemini-2.0-flash"
            
            # Call Gemini API (async)
            response = await client.aio.models.generate_content(
                model=model,
                contents=full_prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=temperature
                )
            )
            
            # Extract response
            text = response.text or ""
            
            # Extract metadata (Gemini response structure)
            metadata = {
                "model": model,
                "tokens": getattr(response, "usage_metadata", {}).get("total_token_count", 0) if hasattr(response, "usage_metadata") else 0,
                "finish_reason": getattr(response.candidates[0], "finish_reason", "STOP").name if response.candidates else "STOP"
            }
            
            return {
                "text": text,
                "metadata": metadata
            }
            
        except Exception as e:
            # TODO: Add proper error logging
            logger.error(f"Gemini API error: {str(e)}")
            raise

