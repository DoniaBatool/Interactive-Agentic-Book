"""
Subagents Module

This package contains specialized AI agents for each AI block type:
- ask_question_agent: Question-answering agent
- explain_el10_agent: Simplified explanation agent
- quiz_agent: Quiz generation agent
- diagram_agent: Diagram generation agent
"""

from app.ai.subagents.ask_question_agent import ask_question_agent
from app.ai.subagents.explain_el10_agent import explain_el10_agent
from app.ai.subagents.quiz_agent import quiz_agent
from app.ai.subagents.diagram_agent import diagram_agent

__all__ = [
    "ask_question_agent",
    "explain_el10_agent",
    "quiz_agent",
    "diagram_agent"
]

