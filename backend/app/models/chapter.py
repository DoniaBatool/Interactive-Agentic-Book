"""
Pydantic models for chapter metadata.

This module defines the data structures for chapter information
used in API responses and internal data management.
"""

from typing import List
from pydantic import BaseModel, Field


class ChapterMetadata(BaseModel):
    """
    Metadata for a single chapter in the textbook.
    
    This model defines the structure of chapter information returned
    by the API and used throughout the application for chapter management.
    """
    
    chapter: int = Field(
        ...,
        description="Chapter number (e.g., 1, 2, 3)",
        ge=1,
        example=1
    )
    
    title: str = Field(
        ...,
        description="Full chapter title",
        min_length=1,
        max_length=200,
        example="Introduction to Physical AI & Robotics"
    )
    
    summary: str = Field(
        ...,
        description="Brief summary of chapter content",
        min_length=1,
        max_length=1000,
        example="Placeholder summary for Chapter 1 introduction"
    )
    
    sections: List[str] = Field(
        default_factory=list,
        description="List of section titles within the chapter",
        example=[]
    )
    
    class Config:
        schema_extra = {
            "example": {
                "chapter": 1,
                "title": "Introduction to Physical AI & Robotics",
                "summary": "Placeholder summary for Chapter 1 introduction",
                "sections": []
            }
        }
