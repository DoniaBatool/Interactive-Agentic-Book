"""
Session model for storing chat sessions.
Feature 012: Postgres Persistence
Feature 013: Auth & Personalization (user_id link)
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from backend.app.core.database import Base


class Session(Base):
    """
    Represents a chat session.
    
    A session is tied to a browser/device via session_id stored in localStorage.
    When user logs in, session is linked to user_id.
    """
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(36), unique=True, nullable=False, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationship to messages
    messages = relationship(
        "Message",
        back_populates="session",
        cascade="all, delete-orphan"
    )
    
    # Relationship to user
    user = relationship("User", back_populates="sessions")

    def __repr__(self):
        return f"<Session(session_id={self.session_id}, user_id={self.user_id})>"

