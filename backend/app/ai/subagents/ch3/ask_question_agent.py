"""
Chapter 3 Ask Question Agent

Specialized agent for answering questions about Physical AI concepts using Chapter 3 context.
Uses RAG pipeline to retrieve relevant context and generates answers.
"""

from typing import Dict, Any
from app.ai.subagents.base_agent import BaseAgent


class Ch3AskQuestionAgent(BaseAgent):
    """
    Chapter 3 Ask Question Agent
    
    Processes questions about Physical AI using Chapter 3 RAG context.
    """
    
    async def run(self, request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Chapter 3 question-answering agent.
        
        Process Physical AI questions with Chapter 3 RAG context.
        
        Args:
            request_data: {
                "question": str,                          # User question about Physical AI
                "chapterId": 3,                          # Chapter identifier
                "sectionId": Optional[str]                # Section identifier (optional)
            }
            context: {
                "context": str,                     # Retrieved Chapter 3 context chunks
                "chunks": List[Dict],              # Chunk metadata with Physical AI concepts
                "query_embedding": List[float]     # Query vector
            }
        
        Returns:
            {
                "answer": str,                     # Generated answer text with Physical AI context
                "sources": List[str],              # Source citations (section IDs)
                "confidence": float                # Confidence score (0.0-1.0)
            }
        """
        from app.ai.skills.retrieval_skill import retrieve_content
        from app.ai.skills.prompt_builder_skill import build_prompt
        from app.ai.skills.formatting_skill import format_response
        from app.ai.providers.base_llm import get_provider
        from app.config.settings import settings
        
        try:
            question = request_data.get("question", "")
            chapter_id = request_data.get("chapterId", 3)
            
            # Step 1: Get context from RAG pipeline
            chunks = context.get("chunks", [])
            
            # Step 2: Build prompt - convert chunks to format expected by build_prompt
            context_list = []
            for chunk in chunks:
                # Chunks from RAG pipeline have text and section_id at top level
                text = chunk.get("text", "")
                section_id = chunk.get("section_id", "")
                if text:
                    context_list.append({"text": text, "section_id": section_id})
            
            prompt = build_prompt("ask-question", question, context_list, chapter_id=chapter_id)
            
            # Step 3: Call LLM provider
            provider_name = settings.ai_provider or settings.default_runtime_provider or "openai"
            provider = get_provider(provider_name)
            if not provider:
                raise ValueError(f"Provider {provider_name} not available")
            
            llm_response = await provider.generate(
                prompt=prompt,
                system="You are a helpful tutor answering questions about Physical AI and Robotics.",
                temperature=0.7
            )
            
            # Step 4: Format response
            formatted = format_response(llm_response, "ask-question", chapter_id=chapter_id)
            
            # Extract source citations from chunks
            sources = [chunk.get("section_id", "") for chunk in chunks if chunk.get("section_id")]
            sources = list(set(sources))  # Remove duplicates
            
            # Calculate confidence based on context relevance
            confidence = min(0.9, max(0.5, len(chunks) / 5.0)) if chunks else 0.5
            
            return {
                "answer": formatted.get("answer", llm_response.get("text", "")),
                "sources": sources,
                "confidence": confidence
            }
            
        except Exception as e:
            # TODO: Add proper error logging
            return {
                "answer": f"Error: {str(e)}",
                "sources": [],
                "confidence": 0.0
            }

