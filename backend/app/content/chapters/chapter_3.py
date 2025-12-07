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

from typing import List, Dict, Any

CHAPTER_METADATA = {
    # Core identification
    "id": 3,
    "title": "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)",
    "summary": "TODO: 2-3 sentence overview",  # 2-3 sentence description

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
        "generate-diagram",
        "explain-like-i-am-10",
        "interactive-quiz"
    ],
    "diagram_placeholders": [
        "perception-overview",
        "sensor-types",
        "cv-depth-flow",
        "feature-extraction-pipeline"
    ],

    # Versioning
    "last_updated": "2025-01-27T00:00:00Z",

    # RAG-specific metadata
    "difficulty_level": "intermediate",
    "prerequisites": [1, 2],  # Chapters 1 and 2 are prerequisites
    "learning_outcomes": ["TODO: 3-8 learning outcomes"],  # 3-8 items
    "glossary_terms": ["TODO: 6-10 glossary terms"]  # 6-10 items
}


def get_chapter_3_chunks() -> List[Dict[str, Any]]:
    """
    TODO: Implement chunking from Chapter 3 MDX content.
    
    Returns list of chunks with metadata for RAG integration.
    Each chunk should include:
    - id: Unique chunk identifier
    - text: Chunk text content
    - chapter_id: 3
    - section_id: Section identifier
    - position: Position in chapter (0-based)
    - metadata: Additional metadata (heading, type, etc.)
    
    TODO: Load Chapter 3 content from frontend/docs/chapters/chapter-3.mdx
    TODO: Implement chunking strategy (section-by-section or semantic chunking)
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch3-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Cache chunks for performance
    """
    return []
