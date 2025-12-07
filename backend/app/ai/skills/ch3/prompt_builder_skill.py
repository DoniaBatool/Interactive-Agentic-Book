"""
Chapter 3 Prompt Builder Skill

Reusable skill for building LLM prompts for Chapter 3.
Used by subagents to construct prompts with Physical AI context.
"""

from typing import Dict, Any, List
from app.ai.skills.base_skill import BaseSkill


class Ch3PromptBuilderSkill(BaseSkill):
    """
    Chapter 3 Prompt Builder Skill
    
    Provides LLM prompt building for Chapter 3.
    """
    
    def build_prompt(
        self,
        block_type: str,
        request_data: Dict[str, Any],
        context: Dict[str, Any]
    ) -> str:
        """
        Build prompt for any block type.
        
        Expected Input:
            block_type: str                         # Block type ("ask-question", "explain-like-10", "quiz", "diagram")
            request_data: Dict[str, Any]            # Request payload
            context: Dict[str, Any]                 # RAG context
        
        Expected Output:
            Formatted prompt string
        
        TODO: Implement generic prompt building for Chapter 3
        TODO: Select prompt template based on block_type
        TODO: Inject context into prompt template
        TODO: Add Physical AI-specific instructions
        TODO: Return formatted prompt string
        """
        # Placeholder return - no real prompt building logic
        return ""
    
    def build_ask_question_prompt(
        self,
        question: str,
        context: str
    ) -> str:
        """
        Build prompt for ask-question block.
        
        TODO: Implement ask-question prompt building for Chapter 3
        TODO: Use Physical AI question-answering template
        TODO: Inject question and context
        TODO: Add instructions for Physical AI terminology
        """
        # Placeholder return - no real prompt building logic
        return ""
    
    def build_eli10_prompt(
        self,
        concept: str,
        context: str
    ) -> str:
        """
        Build prompt for explain-like-10 block.
        
        TODO: Implement ELI10 prompt building for Chapter 3
        TODO: Use Physical AI ELI10 template
        TODO: Inject concept and context
        TODO: Add instructions for age-appropriate language (7th-8th grade)
        TODO: Add instructions for Physical AI analogies
        """
        # Placeholder return - no real prompt building logic
        return ""
    
    def build_quiz_prompt(
        self,
        num_questions: int,
        context: str,
        learning_objectives: List[str] = None
    ) -> str:
        """
        Build prompt for quiz generation.
        
        TODO: Implement quiz prompt building for Chapter 3
        TODO: Use Physical AI quiz generation template
        TODO: Inject num_questions, context, learning_objectives
        TODO: Add instructions for diverse question types
        TODO: Add instructions for Physical AI terminology
        """
        # Placeholder return - no real prompt building logic
        return ""
    
    def build_diagram_prompt(
        self,
        diagram_type: str,
        concepts: List[str],
        context: str
    ) -> str:
        """
        Build prompt for diagram generation.
        
        TODO: Implement diagram prompt building for Chapter 3
        TODO: Use Physical AI diagram generation template
        TODO: Inject diagram_type, concepts, context
        TODO: Add instructions for diagram format (Mermaid, JSON, SVG)
        TODO: Add instructions for Physical AI concepts
        """
        # Placeholder return - no real prompt building logic
        return ""

