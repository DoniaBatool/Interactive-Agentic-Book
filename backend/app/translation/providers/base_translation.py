"""
Base Translation Provider Interface

Abstract base class for all translation providers.
"""

from abc import ABC, abstractmethod
from typing import List


class BaseTranslationProvider(ABC):
    """
    Abstract base class for translation providers.
    
    All provider implementations must implement:
    - translate_text()
    - translate_batch()
    - supported_languages()
    """
    
    @abstractmethod
    async def translate_text(
        self,
        text: str,
        target_language: str
    ) -> str:
        """
        Translate a single text string.
        
        Args:
            text: Source text to translate
            target_language: Target language code (en, ur, ru, ar)
        
        Returns:
            Translated text string
        
        TODO: Implement in provider subclasses
        """
        pass
    
    @abstractmethod
    async def translate_batch(
        self,
        texts: List[str],
        target_language: str
    ) -> List[str]:
        """
        Translate multiple text strings in batch.
        
        Args:
            texts: List of source texts to translate
            target_language: Target language code (en, ur, ru, ar)
        
        Returns:
            List of translated text strings
        
        TODO: Implement in provider subclasses
        """
        pass
    
    @abstractmethod
    def supported_languages(self) -> List[str]:
        """
        Get list of supported language codes.
        
        Returns:
            List of supported language codes (e.g., ["en", "ur", "ru", "ar"])
        
        TODO: Implement in provider subclasses
        """
        pass

