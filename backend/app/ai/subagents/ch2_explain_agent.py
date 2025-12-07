"""
Chapter 2 Explain Like I'm 10 Agent

Specialized agent for explaining Mechanical Systems concepts in simple terms using Chapter 2 context.
Uses RAG pipeline to retrieve relevant context and generates age-appropriate explanations.
"""

from typing import Dict, Any


class Ch2ExplainAgent:
    """
    Chapter 2 Explain Like I'm 10 Agent
    
    Processes explanations for Mechanical Systems concepts using Chapter 2 RAG context.
    """
    
    def run(self, input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Chapter 2 explain-like-i-am-10 agent blueprint.
        
        Generate Mechanical Systems explanations with Chapter 2 RAG context.
        
        Expected Input:
            input: {
                "concept": str,                          # Mechanical Systems concept to explain
                "context": {
                    "context": str,                     # Retrieved Chapter 2 context chunks
                    "chunks": List[Dict],              # Chunk metadata with Mechanical Systems concepts
                    "query_embedding": List[float]     # Query vector
                }
            }
        
        Expected Output:
            {
                "explanation": str,                 # Generated explanation text with Mechanical Systems context
                "examples": List[str],              # Real-world examples
                "analogies": List[str]              # Age-appropriate analogies
            }
        
        Agent Flow (all TODO):
        1. Use retrieval_skill to get additional context if needed
        2. Use prompt_builder_skill to construct Mechanical Systems explain prompt
        3. Call LLM provider (DEFAULT_CH2_MODEL) with prompt + context
        4. Use formatting_skill to format response with examples and analogies
        5. Return formatted explanation
        
        TODO: Implement Mechanical Systems explanation logic
        TODO: Step 1: Call retrieve_content(concept, chapter_id=2) to get more context if needed
        TODO: Step 2: Call build_prompt("explain-like-i-am-10", concept, context, chapter_id=2) to construct Mechanical Systems prompt
        TODO: Step 3: Call LLM provider (DEFAULT_CH2_MODEL) with prompt + Mechanical Systems context
        TODO: Step 4: Call format_response(response, "explain-like-i-am-10", chapter_id=2) to format with examples and analogies
        TODO: Extract examples from retrieved Chapter 2 chunks
        TODO: Generate age-appropriate analogies for Mechanical Systems concepts
        TODO: Add error handling for LLM failures
        TODO: Add logging for explanation generation execution
        """
        # TODO: implement model prompting in future feature
        return {
            "explanation": "",
            "examples": [],
            "analogies": []
        }

