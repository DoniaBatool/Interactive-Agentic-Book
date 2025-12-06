"""
Diagram Schema Models

Pydantic models for type-safe diagram data structures.
All fields are optional or placeholder to support flexible diagram structures.
"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class DiagramRequest(BaseModel):
    """Request model for diagram generation."""
    diagram_type: str                        # Diagram type identifier
    chapter_id: Optional[int] = None         # Chapter identifier
    concepts: List[str] = []                # Concepts to include in diagram


class DiagramNode(BaseModel):
    """Node structure for diagram representation."""
    id: str                                  # Node identifier (required)
    label: Optional[str] = None              # Node label
    type: Optional[str] = None               # Node type
    position: Optional[Dict[str, float]] = None  # Position coordinates (x, y)
    metadata: Optional[Dict[str, Any]] = None  # Additional metadata


class DiagramEdge(BaseModel):
    """Edge structure for diagram representation."""
    source: str                              # Source node ID (required)
    target: str                              # Target node ID (required)
    label: Optional[str] = None              # Edge label
    type: Optional[str] = None               # Edge type
    metadata: Optional[Dict[str, Any]] = None  # Additional metadata


class DiagramResponse(BaseModel):
    """Response model for diagram generation."""
    nodes: List[DiagramNode] = []            # List of diagram nodes
    edges: List[DiagramEdge] = []           # List of diagram edges
    svg: Optional[str] = None               # SVG string or code
    metadata: Optional[Dict[str, Any]] = None  # Additional metadata

