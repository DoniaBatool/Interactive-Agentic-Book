"""
ChatKit Tools

Documentation of tools needed for ChatKit integration.
Tools will be implemented when ChatKit is fully integrated.
"""

# ChatKit Tools Documentation
# Tools needed for future ChatKit integration:

# 1. diagram_tool: Generate visual diagrams
#    - Input: {
#        "diagram_type": str,      # "robot-anatomy", "ai-robotics-stack", etc.
#        "concepts": List[str]     # Concepts to include
#      }
#    - Output: {
#        "diagram_url": str,       # URL or base64-encoded image
#        "metadata": Dict          # Diagram metadata
#      }
#    - Purpose: Allow ChatKit to generate diagrams during conversations

# 2. quiz_tool: Generate interactive quizzes
#    - Input: {
#        "chapter_id": int,        # Chapter identifier
#        "num_questions": int      # Number of questions
#      }
#    - Output: {
#        "questions": List[Dict], # Quiz questions with answers
#        "learning_objectives": List[str]  # Covered objectives
#      }
#    - Purpose: Allow ChatKit to generate quizzes during conversations

# 3. explanation_tool: Generate simplified explanations
#    - Input: {
#        "concept": str,           # Concept name
#        "age_level": str         # "10", "12", "adult"
#      }
#    - Output: {
#        "explanation": str,       # Simplified explanation
#        "examples": List[str],    # Analogies or examples
#        "analogies": List[str]   # Age-appropriate analogies
#      }
#    - Purpose: Allow ChatKit to explain concepts at different age levels

# TODO: Implement tool definitions when ChatKit integrated
# TODO: Define tool schemas using ChatKit tool format
# TODO: Register tools with ChatKit session
# TODO: Handle tool calls from ChatKit
# TODO: Return tool results to ChatKit

# TODO: Chapter 2 Tool Definitions
# 
# ch2_ask_question_tool:
#   name: "ch2_ask_question"
#   description: "Ask questions about ROS 2 concepts"
#   input: {
#     "question": str,
#     "sectionId": str (optional)
#   }
#   output: {
#     "answer": str,
#     "sources": List[str]
#   }
# 
# ch2_explain_el10_tool:
#   name: "ch2_explain_el10"
#   description: "Explain ROS 2 concepts like I'm 10"
#   input: {
#     "concept": str
#   }
#   output: {
#     "explanation": str,
#     "examples": List[str]
#   }
# 
# ch2_quiz_tool:
#   name: "ch2_quiz"
#   description: "Generate ROS 2 quizzes"
#   input: {
#     "numQuestions": int
#   }
#   output: {
#     "questions": List[Dict],
#     "learning_objectives": List[str]
#   }
# 
# ch2_diagram_tool:
#   name: "ch2_diagram"
#   description: "Generate ROS 2 diagrams"
#   input: {
#     "diagramType": str,
#     "concepts": List[str]
#   }
#   output: {
#     "diagram_url": str,
#     "metadata": Dict
#   }
# 
# TODO: Implement tool definitions when ChatKit integrated
# TODO: Register tools with ChatKit session
# TODO: Handle tool calls from ChatKit
# TODO: Return tool results to ChatKit

