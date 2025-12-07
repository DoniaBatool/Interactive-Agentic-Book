"""
Chapter 2 metadata for RAG integration and content management.

This module contains structured metadata for Chapter 2: "The Foundations of Mechanical Systems"
including section information, placeholder tracking, and learning objectives.

TODO: Future RAG Integration Points
- [ ] Create Pydantic model for ChapterMetadata with validation rules
- [ ] Implement embedding generation for chapter content (OpenAI/local models)
- [ ] Store embeddings in Qdrant vector database with metadata
- [ ] Create API endpoint GET /api/chapters/2 to serve this metadata
- [ ] Add semantic search capability across all chapters
- [ ] Implement chapter recommendation based on prerequisites and difficulty
"""

from typing import List

CHAPTER_METADATA = {
    # Core identification
    "id": 2,
    "title": "Chapter 2 — The Foundations of Mechanical Systems",
    "summary": "A foundational chapter covering forces, motion, energy, work, and simple machines. Explores how mechanical systems work, why mechanical advantage matters, and how robots use mechanical systems including actuators and force transmission. Suitable for beginners who have completed Chapter 1.",

    # Structure information
    "section_count": 7,
    "sections": [
        "Forces & Motion",
        "Energy & Work",
        "Simple Machines",
        "Mechanical Systems in Robotics",
        "Learning Objectives",
        "Summary",
        "Glossary"
    ],

    # Placeholder tracking
    "ai_blocks": [
        "ask-question",
        "explain-like-i-am-10",
        "generate-diagram",
        "interactive-quiz"
    ],
    "diagram_placeholders": [
        "force-motion",
        "energy-work",
        "simple-machines",
        "robotics-mechanics"
    ],

    # Versioning
    "last_updated": "2025-01-27T00:00:00Z",

    # RAG-specific metadata
    "difficulty_level": "beginner",
    "prerequisites": [1],  # Chapter 1 is prerequisite
    "learning_outcomes": [
        "Define force and motion and explain Newton's three laws at a beginner level",
        "Explain the concepts of energy, work, and mechanical efficiency with real-world examples",
        "Identify the six types of simple machines and describe how each one makes work easier",
        "Explain mechanical advantage and why it matters in robotic systems",
        "Describe how robots use mechanical systems, including actuators and force transmission",
        "Understand safety considerations when working with mechanical systems in robotics",
        "Recognize how simple machines combine to create complex robotic movements"
    ],
    "glossary_terms": [
        "Force",
        "Motion",
        "Work",
        "Energy",
        "Mechanical Advantage",
        "Simple Machine",
        "Efficiency"
    ]
}
