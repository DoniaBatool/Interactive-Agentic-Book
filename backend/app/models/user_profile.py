"""
UserProfile model for storing user background and preferences.
Feature 013: Auth & Personalization
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from backend.app.core.database import Base


class UserProfile(Base):
    """
    Represents a user's profile with background information.
    
    Used for content personalization based on:
    - Software experience level
    - Hardware experience level
    - Known technologies
    - Learning goals
    """
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True
    )
    
    # Experience levels
    software_level = Column(
        String(20),
        nullable=False,
        default="beginner"
    )  # beginner, intermediate, advanced
    
    hardware_level = Column(
        String(20),
        nullable=False,
        default="none"
    )  # none, some, extensive
    
    # Technologies known (JSONB for flexibility)
    technologies = Column(
        JSONB,
        default={}
    )  # {"python": true, "ros2": true, ...}
    
    # Learning goals
    learning_goals = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    user = relationship("User", back_populates="profile")

    def __repr__(self):
        return f"<UserProfile(user_id={self.user_id}, software={self.software_level})>"
    
    def to_dict(self):
        """Convert profile to dictionary for API response."""
        return {
            "software_level": self.software_level,
            "hardware_level": self.hardware_level,
            "technologies": self.technologies or {},
            "learning_goals": self.learning_goals,
        }

