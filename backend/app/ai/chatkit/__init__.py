"""
ChatKit Integration Module

This package provides ChatKit integration scaffolding:
- Session management
- Tool definitions
"""

from app.ai.chatkit.session_manager import create_session, append_message, get_history

__all__ = [
    "create_session",
    "append_message",
    "get_history"
]

