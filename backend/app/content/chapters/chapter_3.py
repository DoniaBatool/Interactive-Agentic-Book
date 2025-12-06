"""
Chapter 3 metadata for RAG integration and content management.

This module contains structured metadata for Chapter 3: "Physical AI Perception Systems"
including section information, placeholder tracking, and learning objectives.

TODO: Future RAG Integration Points
- [ ] Create Pydantic model for ChapterMetadata with validation rules
- [ ] Implement embedding generation for chapter content (OpenAI/local models)
- [ ] Store embeddings in Qdrant vector database with metadata
- [ ] Create API endpoint GET /api/chapters/3 to serve this metadata
- [ ] Add semantic search capability across all chapters
- [ ] Implement chapter recommendation based on prerequisites and difficulty
- [ ] Validate prerequisites (ensure Chapters 1 and 2 exist before Chapter 3)
"""

from typing import List

CHAPTER_METADATA = {
    # Core identification
    "id": 3,
    "title": "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)",
    "summary": "placeholder",  # 2-3 sentence overview

    # Structure information
    "section_count": 7,
    "sections": [
        "What Is Perception in Physical AI?",
        "Types of Sensors in Robotics",
        "Computer Vision & Depth Perception",
        "Signal Processing Basics for AI",
        "Feature Extraction & Interpretation",
        "Learning Objectives",
        "Glossary"
    ],

    # Placeholder tracking
    "ai_blocks": [
        "ask-question",
        "explain-like-i-am-10",
        "interactive-quiz",
        "generate-diagram"
    ],
    "diagram_placeholders": [
        "perception-overview",
        "sensor-types",
        "cv-depth-flow",
        "feature-extraction-pipeline"
    ],

    # Versioning
    "last_updated": "2025-12-05T00:00:00Z",

    # RAG-specific metadata
    "difficulty_level": "intermediate",
    "prerequisites": [1, 2],  # Chapters 1 and 2 are prerequisites
    "learning_outcomes": ["placeholder list"],  # 3-8 items
    "glossary_terms": ["placeholder list"]  # 7 items
}
