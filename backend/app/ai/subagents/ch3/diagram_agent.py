"""
Chapter 3 Diagram Agent

Specialized agent for generating visual diagrams for Physical AI concepts.
Creates diagram descriptions/JSON for rendering.
"""

from typing import Dict, Any
from app.ai.subagents.base_agent import BaseAgent


class Ch3DiagramAgent(BaseAgent):
    """
    Chapter 3 Diagram Agent
    
    Generates visual diagrams for Physical AI concepts using Chapter 3 context.
    """
    
    async def run(self, request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Chapter 3 diagram generation agent.
        
        Process diagram generation requests with Chapter 3 RAG context.
        
        Args:
            request_data: {
                "diagramType": str,                      # Diagram type (e.g., "sensor-types")
                "chapterId": 3,                         # Chapter identifier
                "concepts": Optional[List[str]]          # Concepts to include
            }
            context: {
                "context": str,                     # Retrieved Chapter 3 context chunks
                "chunks": List[Dict],              # Chunk metadata
            }
        
        Returns:
            {
                "diagram_prompt": str,             # Mermaid.js or other diagram syntax
                "diagram_type": str,               # Confirmed diagram type
                "description": str                 # Textual description of the diagram
            }
        """
        from app.ai.skills.prompt_builder_skill import build_prompt
        from app.ai.skills.formatting_skill import format_response
        from app.ai.providers.base_llm import get_provider
        from app.config.settings import settings
        
        try:
            diagram_type = request_data.get("diagramType", "flowchart")
            chapter_id = request_data.get("chapterId", 3)
            concepts = request_data.get("concepts", [])
            
            # Step 1: Get context (optional for diagrams)
            chunks = context.get("chunks", [])
            
            # Step 2: Build diagram prompt - convert chunks to format expected by build_prompt
            user_input = f"Generate a {diagram_type} diagram"
            if concepts:
                user_input += f" showing: {', '.join(concepts)}"
            
            context_list = []
            for chunk in chunks:
                text = chunk.get("text", "")
                section_id = chunk.get("section_id", "")
                if text:
                    context_list.append({"text": text, "section_id": section_id})
            
            prompt = build_prompt("diagram", user_input, context_list, chapter_id=chapter_id)
            
            # Step 3: Call LLM provider
            provider_name = settings.ai_provider or settings.default_runtime_provider or "openai"
            provider = get_provider(provider_name)
            if not provider:
                raise ValueError(f"Provider {provider_name} not available")
            
            llm_response = await provider.generate(
                prompt=prompt,
                system="You are a helpful tutor creating diagrams for Physical AI concepts. Generate Mermaid.js syntax or structured diagram descriptions.",
                temperature=0.7
            )
            
            # Step 4: Format response
            formatted = format_response(llm_response, "diagram", chapter_id=chapter_id)
            
            return {
                "diagram_prompt": formatted.get("diagram_prompt", llm_response.get("text", "")),
                "diagram_type": diagram_type,
                "description": formatted.get("description", llm_response.get("text", ""))
            }
            
        except Exception as e:
            # TODO: Add proper error logging
            return {
                "diagram_prompt": f"Error: {str(e)}",
                "diagram_type": request_data.get("diagramType", "flowchart"),
                "description": "Error generating diagram"
            }

