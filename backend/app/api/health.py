"""
Health check endpoint.

Provides application health status and timestamp.
"""

from fastapi import APIRouter
from datetime import datetime
from typing import Literal

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Health check endpoint.
    
    Returns:
        dict: Health status and timestamp in ISO 8601 format.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
