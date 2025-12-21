"""
Message model for storing chat messages.
Feature 012: Postgres Persistence
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from backend.app.core.database import Base


class Message(Base):
    """
    Represents a single chat message (user or assistant).
    
    Messages are linked to a session and optionally filtered by chapter.
    Citations are stored as JSONB for efficient querying.
    """
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(
        String(36),
        ForeignKey("sessions.session_id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    chapter = Column(String(255), nullable=True, index=True)
    role = Column(String(20), nullable=False)  # 'user' or 'assistant'
    content = Column(Text, nullable=False)
    citations = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship to session
    session = relationship("Session", back_populates="messages")

    def __repr__(self):
        return f"<Message(id={self.id}, role={self.role}, session_id={self.session_id})>"
    
    def to_dict(self):
        """Convert message to dictionary for API response."""
        return {
            "id": self.id,
            "role": self.role,
            "content": self.content,
            "citations": self.citations,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

