"""
Chapter 3 Quiz Agent

Specialized agent for generating interactive quiz questions from Chapter 3 content.
Creates diverse question types covering learning objectives.
"""

from typing import Dict, Any
from app.ai.subagents.base_agent import BaseAgent


class Ch3QuizAgent(BaseAgent):
    """
    Chapter 3 Quiz Agent
    
    Generates interactive quiz questions from Chapter 3 content.
    """
    
    async def run(self, request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Chapter 3 quiz generation agent.
        
        Process quiz generation requests with Chapter 3 RAG context.
        
        Args:
            request_data: {
                "chapterId": 3,                          # Chapter identifier
                "numQuestions": int,                     # Number of questions (default: 5)
                "learningObjectives": Optional[List[str]] # Learning objectives to focus on
            }
            context: {
                "context": str,                     # Retrieved Chapter 3 context chunks
                "chunks": List[Dict],              # Chunk metadata
            }
        
        Returns:
            {
                "quiz_title": str,                 # Title of the quiz
                "questions": List[Dict]             # Quiz questions
            }
        """
        from app.ai.skills.prompt_builder_skill import build_prompt
        from app.ai.skills.formatting_skill import format_response
        from app.ai.providers.base_llm import get_provider
        from app.config.settings import settings
        
        try:
            chapter_id = request_data.get("chapterId", 3)
            num_questions = request_data.get("numQuestions", 5)
            learning_objectives = request_data.get("learningObjectives", [])
            
            # Step 1: Get context (all sections for quiz)
            chunks = context.get("chunks", [])
            
            # Step 2: Build quiz prompt - convert chunks to format expected by build_prompt
            user_input = f"Generate {num_questions} quiz questions"
            if learning_objectives:
                user_input += f" covering: {', '.join(learning_objectives)}"
            
            context_list = []
            for chunk in chunks:
                text = chunk.get("text", "")
                section_id = chunk.get("section_id", "")
                if text:
                    context_list.append({"text": text, "section_id": section_id})
            
            prompt = build_prompt("quiz", user_input, context_list, chapter_id=chapter_id)
            
            # Step 3: Call LLM provider
            provider_name = settings.ai_provider or settings.default_runtime_provider or "openai"
            provider = get_provider(provider_name)
            if not provider:
                raise ValueError(f"Provider {provider_name} not available")
            
            llm_response = await provider.generate(
                prompt=prompt,
                system="You are a helpful tutor creating quiz questions about Physical AI and Robotics.",
                temperature=0.7
            )
            
            # Step 4: Format response
            formatted = format_response(llm_response, "quiz", chapter_id=chapter_id)
            
            return {
                "quiz_title": formatted.get("quiz_title", f"Chapter {chapter_id} Quiz"),
                "questions": formatted.get("questions", [])
            }
            
        except Exception as e:
            # TODO: Add proper error logging
            return {
                "quiz_title": f"Chapter {chapter_id} Quiz",
                "questions": []
            }

