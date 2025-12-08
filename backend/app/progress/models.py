"""
Progress State Model

Placeholder models for progress tracking.
All models are placeholders with TODO comments for future database integration.

TODO: Real database models will be implemented in a future feature.
"""

from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


class ProgressState(str, Enum):
    """
    Progress state enumeration.
    
    Represents the current progress state of a chapter for a user.
    """
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


@dataclass
class ProgressRecord:
    """
    Progress record dataclass.
    
    Represents a single progress record for a user-chapter pair.
    
    TODO: Real database model will be implemented in a future feature.
    TODO: Add database fields (id, created_at, etc.)
    TODO: Add validation logic
    TODO: Add serialization methods
    """
    user_id: str
    chapter_id: int
    state: ProgressState
    updated_at: datetime
    
    # TODO: Add database model mapping
    # TODO: Add persistence layer integration
    # TODO: Add validation rules
    # TODO: Add serialization to/from database

