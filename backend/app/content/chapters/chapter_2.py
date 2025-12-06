"""
Chapter 2 metadata for RAG integration and content management.

This module contains structured metadata for Chapter 2: "ROS 2 Fundamentals"
including section information, placeholder tracking, and learning objectives.

TODO: Future RAG Integration Points
- [ ] Create Pydantic model for ChapterMetadata with validation rules
- [ ] Implement embedding generation for chapter content (OpenAI/local models)
- [ ] Store embeddings in Qdrant vector database with metadata
- [ ] Create API endpoint GET /api/chapters/2 to serve this metadata
- [ ] Add semantic search capability across all chapters
- [ ] Implement chapter recommendation based on prerequisites and difficulty
- [ ] Validate prerequisites (ensure Chapter 1 exists before Chapter 2)
"""

from typing import List

CHAPTER_METADATA = {
    # Core identification
    "id": 2,
    "title": "Chapter 2 — ROS 2 Fundamentals",
    "summary": "An introductory chapter covering ROS 2 fundamentals including nodes, topics, services, actions, packages, and launch files. Explores how ROS 2 enables robot communication through publish/subscribe topics, request/response services, and long-running actions. Introduces package structure and launch file workflows for real-world robotics development. Suitable for beginners with Chapter 1 prerequisite.",

    # Structure information
    "section_count": 7,
    "sections": [
        "Introduction to ROS 2",
        "Nodes and Node Communication",
        "Topics and Messages",
        "Services and Actions",
        "ROS 2 Packages",
        "Launch Files and Workflows",
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
        "ros2-ecosystem-overview",
        "node-communication-architecture",
        "topic-pubsub-flow",
        "services-actions-comparison"
    ],

    # Versioning
    "last_updated": "2025-12-05T00:00:00Z",

    # RAG-specific metadata
    "difficulty_level": "beginner",
    "prerequisites": [1],  # Chapter 1 is prerequisite
    "learning_outcomes": [
        "Define ROS 2 and explain its role in robotics development",
        "Explain how nodes communicate in a ROS 2 system",
        "Distinguish between topics, services, and actions",
        "Identify when to use each communication mechanism",
        "Describe ROS 2 package structure and organization",
        "Explain how launch files coordinate multiple nodes"
    ],
    "glossary_terms": [
        "ROS 2",
        "Node",
        "Topic",
        "Service",
        "Action",
        "Package",
        "Launch File"
    ]
}
