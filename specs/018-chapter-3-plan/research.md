# Research Document: Chapter 3 — Planning Layer

**Feature**: 018-chapter-3-plan
**Date**: 2025-12-05
**Purpose**: Resolve technical clarifications and establish best practices for Chapter 3 planning layer

## Research Questions & Resolutions

### Q1: What is the optimal structure for Chapter 3 MDX frontmatter?

**Decision**: Use standard Docusaurus frontmatter matching Chapter 1 and Chapter 2 pattern, adapted for Chapter 3

**Structure**:
```yaml
---
title: "Chapter 3 — Physical AI Perception Systems (Sensors & Signal Processing)"
description: "Learn how Physical AI systems perceive the world through sensors, computer vision, signal processing, and feature extraction for autonomous decision-making"
sidebar_position: 3
sidebar_label: "Chapter 3: Physical AI Perception Systems"
tags: ["physical-ai", "sensors", "perception", "signal-processing"]
---
```

**Rationale**:
- `title`: Must start with "Chapter 3 — " for consistency
- `description`: SEO-optimized, mentions key Physical AI perception concepts
- `sidebar_position`: Must be 3 (matches chapter number)
- `sidebar_label`: Abbreviated for sidebar navigation
- `tags`: Include "physical-ai", "sensors", "perception", "signal-processing" for categorization

**References**:
- Feature 003 (Chapter 1) frontmatter pattern
- Feature 010 (Chapter 2) frontmatter pattern
- Docusaurus Documentation: https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs#markdown-front-matter

---

### Q2: How should AI-block placeholders be formatted for Chapter 3?

**Decision**: Use HTML comment format for AI-block placeholders (alternative to React components)

**Placement Strategy** (using HTML comments):
1. **`<!-- AI-BLOCK: ask-question -->`** - End of Section 1 (after introducing perception)
   - **Why**: Encourages active recall after new concept introduction
   - **Learning Theory**: Retrieval practice strengthens memory formation
   - **Physical AI Context**: Questions about perception definition, sensor types, real-world applications

2. **`<!-- AI-BLOCK: generate-diagram -->`** - Within Section 2 (sensor types explanation)
   - **Why**: Visual representation most valuable for sensor categorization
   - **Learning Theory**: Dual coding theory - combining text + visuals improves retention
   - **Physical AI Context**: Diagram showing sensor categories and their applications

3. **`<!-- AI-BLOCK: explain-like-i-am-10 -->`** - Within Section 3 (computer vision explanation)
   - **Why**: Provides alternative explanation for complex vision concepts
   - **Learning Theory**: Multiple representations aid comprehension for diverse learners
   - **Physical AI Context**: Simplified explanation of computer vision and depth perception

4. **`<!-- AI-BLOCK: interactive-quiz -->`** - End of Section 4 (after signal processing)
   - **Why**: Tests understanding of key signal processing concepts
   - **Learning Theory**: Formative assessment provides feedback on learning progress
   - **Physical AI Context**: Quiz covering sensors, vision, signal processing, and feature extraction

**Format**:
```html
<!-- AI-BLOCK: ask-question -->
<!-- AI-BLOCK: explain-like-i-am-10 -->
<!-- AI-BLOCK: interactive-quiz -->
<!-- AI-BLOCK: generate-diagram -->
```

**Rationale**: HTML comment format provides:
- Clear placeholder identification
- Easy parsing for future AI-block integration
- No dependency on React components during planning phase
- Consistent with diagram placeholder format

**Note**: Feature 017 uses React components (`<AskQuestionBlock chapterId={3} />`). This specification (Feature 018) uses HTML comments for planning layer clarity.

**References**:
- Feature 010 (Chapter 2) AI-block pattern
- HTML comment format for placeholders

---

### Q3: What content writing style best serves 12+ age group for Physical AI perception technical topics?

**Decision**: Conversational-educational style with scaffolded complexity, using Physical AI-specific analogies

**Style Guidelines**:

**Tone**:
- Second-person ("you") to create direct connection with learner
- Friendly but not condescending - respect reader's intelligence
- Enthusiastic about Physical AI without being overly casual
- Example: "Have you ever wondered how robots see and understand the world? Physical AI perception systems make this possible!"

**Sentence Structure**:
- Average 15-20 words per sentence (Grade 7-8 level)
- Mix simple and compound sentences for rhythm
- Avoid complex subordinate clauses stacked deeply
- Break dense Physical AI concepts into 2-3 shorter sentences

**Paragraph Structure**:
- 3-4 sentences per paragraph maximum
- One main idea per paragraph
- Use transition sentences to connect concepts
- Break long explanations into multiple paragraphs

**Vocabulary**:
- Introduce Physical AI terms with immediate context
- Use analogies from daily life:
  - **Eyes and ears** for sensors (perception input)
  - **Filtering noise** for signal processing (cleaning data)
  - **Recognizing patterns** for feature extraction (identifying important information)
  - **Depth perception** for 3D understanding (like human vision)
  - **LiDAR** for laser-based sensing (like echolocation)
- Define technical terms on first use with simple explanations

**Examples**:
- Use real-world Physical AI applications:
  - Autonomous vehicles (sensors, vision, LiDAR)
  - Robotics (motion tracking, depth perception)
  - Drones (sensor fusion, signal processing)
  - Smart cameras (computer vision, feature extraction)

**References**:
- Feature 003 (Chapter 1) writing style guidelines
- Feature 010 (Chapter 2) writing style guidelines
- Reading level assessment tools (Flesch-Kincaid, SMOG)

---

### Q4: How should diagram placeholders be positioned for Chapter 3?

**Decision**: Position diagrams at strategic points to support visual learning, adapted for Physical AI perception content

**Placement Strategy**:
1. **`perception-overview`** - Section 1 (What Is Perception in Physical AI?)
   - **Why**: Provides high-level overview of perception system
   - **Content**: Shows how sensors, vision, and signal processing work together
   - **Learning Theory**: Visual overview aids schema formation

2. **`sensor-types`** - Section 2 (Types of Sensors in Robotics)
   - **Why**: Visual categorization of sensor types
   - **Content**: Shows different sensor categories (vision, LiDAR, motion, etc.)
   - **Learning Theory**: Visual categorization improves memory organization

3. **`cv-depth-flow`** - Section 3 (Computer Vision & Depth Perception)
   - **Why**: Visualizes depth perception process
   - **Content**: Shows how depth information is extracted and processed
   - **Learning Theory**: Process diagrams aid understanding of complex workflows

4. **`feature-extraction-pipeline`** - Section 4 (Signal Processing Basics for AI)
   - **Why**: Visualizes feature extraction workflow
   - **Content**: Shows feature extraction steps (filtering, pattern recognition, interpretation)
   - **Learning Theory**: Pipeline diagrams show data flow and transformation

**Placeholder Format**:
```html
<!-- DIAGRAM: perception-overview -->
<!-- DIAGRAM: sensor-types -->
<!-- DIAGRAM: cv-depth-flow -->
<!-- DIAGRAM: feature-extraction-pipeline -->
```

**Rationale**: Based on visual learning principles and cognitive load theory. Diagrams positioned to:
- Support text explanations with visual representations
- Break up dense technical content
- Provide alternative learning modality
- Aid in understanding complex Physical AI concepts

**Note**: Feature 017 uses different diagram names (physical-ai-sensing-overview, sensor-categories-diagram, depth-perception-flow, signal-processing-pipeline). This specification (Feature 018) uses shorter, more concise names.

**References**:
- Visual Learning Theory (Mayer, 2001)
- Cognitive Load Theory (Sweller, 1988)
- Dual Coding Theory (Paivio, 1971)

---

### Q5: How should chunk markers be positioned for RAG preparation?

**Decision**: Place chunk markers at logical semantic boundaries, respecting H2 section boundaries

**Placement Strategy**:
- **Section-based logical chunks**: Each H2 section is a natural chunk boundary
- **Concept boundaries**: Chunk markers align with concept boundaries
- **Semantic segmentation**: Chunks respect semantic meaning
- **H2 boundary respect**: Chunks do not cross H2 section boundaries

**Chunk Marker Format**:
```html
<!-- CHUNK: START -->
[Content chunk - section content, paragraphs, etc.]
<!-- CHUNK: END -->
```

**Placement Rules**:
1. Place `<!-- CHUNK: START -->` at beginning of each logical chunk
2. Place `<!-- CHUNK: END -->` at end of each logical chunk
3. Chunk markers MUST be properly paired (START with END)
4. Chunk markers MUST align with concept boundaries
5. Chunk markers MUST respect H2 section boundaries

**Chunking Strategy**:
- **Section-based**: Each H2 section is a natural chunk boundary
- **Concept-based**: Chunks align with major concepts (perception, sensors, vision, signal processing, feature extraction)
- **Semantic boundaries**: Chunks respect semantic meaning and context
- **No cross-section chunks**: Chunks do not cross H2 section boundaries

**RAG Integration**:
- Chunks will be embedded using embedding model (Feature 020)
- Chunks will be stored in Qdrant collection "chapter_3"
- Chunks will be retrieved with metadata for context assembly
- Chunk markers will guide chunking implementation

**References**:
- RAG chunking best practices
- Semantic segmentation strategies
- Feature 020 (Embedding Pipeline) planning

---

### Q6: What glossary terms are essential for Chapter 3?

**Decision**: Include 7 glossary terms covering core Physical AI perception concepts

**Glossary Terms**:
1. **Perception** - How Physical AI systems sense and understand the world
2. **Sensor** - Device that detects and measures physical properties (like eyes and ears for robots)
3. **Computer Vision** - Technology that enables machines to interpret visual information
4. **Depth Perception** - Ability to understand 3D spatial relationships
5. **Signal Processing** - Techniques for analyzing and filtering sensor data
6. **Feature Extraction** - Process of identifying important information from raw data
7. **LiDAR** - Light Detection and Ranging technology for distance measurement (or alternative term)

**Rationale**:
- Covers all major Physical AI perception concepts
- Provides foundation for understanding advanced topics
- Uses beginner-friendly definitions with analogies
- Aligns with course outline requirements

**References**:
- Feature 003 (Chapter 1) glossary pattern
- Feature 010 (Chapter 2) glossary pattern
- Course outline PDF

---

## Industry References

### Physical AI Perception Systems
- **Autonomous Vehicles**: Tesla, Waymo, Cruise - sensor fusion, computer vision, LiDAR
- **Robotics**: Boston Dynamics, iRobot - motion tracking, depth perception, sensor integration
- **Drones**: DJI, Skydio - computer vision, obstacle avoidance, signal processing

### Educational Resources
- **ROS 2 Perception**: Official ROS 2 documentation on perception systems
- **Computer Vision**: OpenCV tutorials and documentation
- **Signal Processing**: Digital signal processing textbooks and courses

### Best Practices
- **Content Structure**: Follow established patterns from Chapter 1 and Chapter 2
- **Writing Style**: Maintain Grade 7-8 reading level with technical accuracy
- **Visual Learning**: Use diagrams and analogies to support text explanations
- **Assessment**: Include learning objectives and quiz questions for self-assessment

---

## Observations

### Key Content Points
- Physical AI perception is foundational for autonomous systems
- Sensors provide raw data that must be processed and interpreted
- Computer vision and depth perception enable 3D understanding
- Signal processing cleans and filters sensor data
- Feature extraction identifies important patterns for decision-making

### Content Challenges
- Balancing technical accuracy with accessibility (Grade 7-8 level)
- Explaining complex concepts (signal processing, feature extraction) with simple analogies
- Maintaining consistency with Chapter 1 and Chapter 2 writing style
- Ensuring content aligns with course outline PDF

### Technical Considerations
- Chapter 3 is intermediate difficulty (requires Chapters 1 and 2 as prerequisites)
- Chunk markers must be properly paired for RAG preparation
- AI-block placeholders use HTML comment format (alternative to React components)
- Diagram placeholders use shorter, more concise names
- Content must integrate with RAG system (future features)

---

## Technology Stack

### Frontend
- **Docusaurus**: MDX support for content rendering
- **Markdown**: Content structure and formatting
- **HTML Comments**: Placeholder format for AI-blocks and chunk markers

### Backend
- **Python 3.9+**: Metadata and chunk file implementation
- **FastAPI**: Future API integration (out of scope for this feature)
- **Pydantic**: Future data validation (out of scope for this feature)

### Content Management
- **MDX**: Content file format
- **YAML**: Frontmatter configuration
- **Python Dictionary**: Metadata structure

---

## Chunking Strategy

### Section-Based Logical Chunks
- Each H2 section is a natural chunk boundary
- Chunks respect semantic meaning and context
- Chunks do not cross H2 section boundaries
- Chunk markers align with concept boundaries

### Concept Boundaries
- Perception concept (Section 1)
- Sensor types concept (Section 2)
- Computer vision concept (Section 3)
- Signal processing concept (Section 4)
- Feature extraction concept (Section 5)
- Learning objectives (Section 6)
- Glossary terms (Section 7)

### RAG Integration Planning
- **Embedding Pipeline** (Feature 020): Chunks will be embedded using embedding model
- **Qdrant Upsert**: Chunks will be stored in Qdrant collection "chapter_3"
- **Retrieval Context Format**: Chunks will be retrieved with metadata for context assembly
- **Chunk Metadata**: Each chunk will include section_id, position, word_count, and concept metadata

---

## Next Steps

1. **Planning Phase**: Create detailed architecture plan (`/sp.plan`)
2. **Task Generation**: Create implementation tasks (`/sp.tasks`)
3. **Implementation**: Create MDX structure with chunk markers (`/sp.implement`)
4. **Content Writing**: Write actual content (future feature)
5. **Validation**: Validate structure and content quality (future feature)
