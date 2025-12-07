"""
Chapter 3 Explain Like I'm 10 Agent

Specialized agent for generating simplified explanations of Physical AI concepts.
Uses age-appropriate language and analogies for better understanding.
"""

from typing import Dict, Any
from app.ai.subagents.base_agent import BaseAgent


class Ch3ExplainEl10Agent(BaseAgent):
    """
    Chapter 3 Explain Like I'm 10 Agent
    
    Generates simplified explanations of Physical AI concepts using Chapter 3 context.
    """
    
    async def run(self, request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Chapter 3 ELI10 explanation agent.
        
        Process Physical AI concept explanations with Chapter 3 RAG context.
        
        Args:
            request_data: {
                "concept": str,                          # Concept to explain (e.g., "computer-vision")
                "chapterId": 3                          # Chapter identifier
            }
            context: {
                "context": str,                     # Retrieved Chapter 3 context chunks
                "chunks": List[Dict],              # Chunk metadata with Physical AI concepts
                "query_embedding": List[float]     # Query vector
            }
        
        Returns:
            {
                "explanation": str,                     # Simplified explanation text
                "analogies": List[str],                  # Analogies used
                "examples": List[str]                    # Real-world examples
            }
        """
        from app.ai.skills.prompt_builder_skill import build_prompt
        from app.ai.skills.formatting_skill import format_response
        from app.ai.providers.base_llm import get_provider
        from app.config.settings import settings
        
        try:
            concept = request_data.get("concept", "")
            chapter_id = request_data.get("chapterId", 3)
            
            # Step 1: Get context from RAG pipeline
            chunks = context.get("chunks", [])
            
            # Step 2: Build ELI10 prompt - convert chunks to format expected by build_prompt
            context_list = []
            for chunk in chunks:
                text = chunk.get("text", "")
                section_id = chunk.get("section_id", "")
                if text:
                    context_list.append({"text": text, "section_id": section_id})
            
            prompt = build_prompt("explain-like-10", concept, context_list, chapter_id=chapter_id)
            
            # Step 3: Call LLM provider
            provider_name = settings.ai_provider or settings.default_runtime_provider or "openai"
            provider = get_provider(provider_name)
            if not provider:
                raise ValueError(f"Provider {provider_name} not available")
            
            llm_response = await provider.generate(
                prompt=prompt,
                system="You are a helpful tutor explaining Physical AI concepts to a 10-year-old. Use simple language, analogies, and examples.",
                temperature=0.7
            )
            
            # Step 4: Format response
            formatted = format_response(llm_response, "explain-like-10", chapter_id=chapter_id)
            
            return {
                "explanation": formatted.get("explanation", llm_response.get("text", "")),
                "analogies": formatted.get("analogies", []),
                "examples": formatted.get("examples", [])
            }
            
        except Exception as e:
            # TODO: Add proper error logging
            return {
                "explanation": f"Error: {str(e)}",
                "analogies": [],
                "examples": []
            }

