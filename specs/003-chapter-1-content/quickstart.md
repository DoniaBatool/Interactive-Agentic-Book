# Quickstart Guide: Implementing Chapter 1 Written Content

**Feature**: 003-chapter-1-content
**Branch**: `003-chapter-1-content`
**Estimated Time**: 2-4 hours (content writing is time-intensive)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 001 (Base Project Initialization) completed
- [x] Docusaurus frontend running at `http://localhost:3000`
- [x] FastAPI backend structure exists at `backend/app/`
- [x] Git branch `003-chapter-1-content` checked out
- [x] Read `specs/003-chapter-1-content/spec.md`
- [x] Read `specs/003-chapter-1-content/research.md` (content writing guidelines)
- [x] Read `specs/003-chapter-1-content/data-model.md` (entity definitions)
- [x] Read `specs/003-chapter-1-content/contracts/content-schema.md` (validation rules)

## Implementation Overview

**Total Steps**: 4 phases
**Primary Deliverable**: MDX file with complete Chapter 1 content
**Secondary Deliverable**: Backend metadata file
**Validation**: Manual review + Docusaurus build test

---

## Phase 1: Frontend Content Creation (2-3 hours)

### Step 1.1: Create MDX File with Frontmatter

**Location**: `frontend/docs/chapters/chapter-1.mdx`

**Action**: Create new file and add frontmatter:

```yaml
---
title: "Chapter 1 — Introduction to Physical AI & Robotics"
description: "Learn the fundamentals of Physical AI and how robots become intelligent through AI integration"
sidebar_position: 1
sidebar_label: "Chapter 1: Intro to Physical AI"
tags: ["physical-ai", "robotics", "introduction", "beginner"]
---
```

**Validation**:
- Title starts with "Chapter 1 — "
- Description is 10-250 characters
- sidebar_position is 1 (matches chapter number)

---

### Step 1.2: Write Section 1 - What is Physical AI?

**Content Requirements** (from spec FR-003):
- Definition of Physical AI
- Differences between Digital AI vs Physical AI
- At least 3 real-world examples
- Diagram placeholder: `<!-- DIAGRAM: physical-ai-overview -->`
- Reading level: 7th-8th grade

**Writing Guidelines** (from research.md):
- Use conversational tone with second-person "you"
- Paragraphs: 3-4 sentences max
- Sentences: 15-20 words average
- Lead with topic sentence, follow with explanation and example

**Example Opening**:
```markdown
## Section 1: What is Physical AI?

Artificial Intelligence is everywhere today. Your phone recognizes your face. Smart speakers understand your voice. But there's a new kind of AI that doesn't just live in computers—it moves, interacts, and operates in the physical world. This is **Physical AI**.

[Continue with definition, differences, examples...]

<!-- DIAGRAM: physical-ai-overview -->
<!-- AI-BLOCK: ask-question -->
```

**Validation**:
- Section heading is H2 (`##`)
- Diagram placeholder present and correctly formatted
- AI-block placeholder present (ask-question type)
- Content is at least 200 words

---

### Step 1.3: Write Section 2 - What is a Robot?

**Content Requirements** (from spec FR-004):
- Formal definition of a robot
- Explanation of components (sensors, actuators, controllers)
- Examples in daily life
- Diagram placeholder: `<!-- DIAGRAM: robot-anatomy -->`

**Example Structure**:
```markdown
## Section 2: What is a Robot?

[Definition paragraph]

[Components explanation - sensors]

[Components explanation - actuators]

[Components explanation - controllers]

[Daily life examples - Roomba, car parking sensors, etc.]

<!-- DIAGRAM: robot-anatomy -->
<!-- AI-BLOCK: generate-diagram -->
```

**Validation**:
- Covers all 3 components (sensors, actuators, controllers)
- Diagram placeholder present
- AI-block placeholder present (generate-diagram type)

---

### Step 1.4: Write Section 3 - AI + Robotics = Physical AI Systems

**Content Requirements** (from spec FR-005):
- Explanation of why robots need AI
- Description of autonomy levels
- Practical real-world applications
- Diagram placeholder: `<!-- DIAGRAM: ai-robotics-stack -->`

**Example Structure**:
```markdown
## Section 3: AI + Robotics = Physical AI Systems

[Why robots need AI - traditional robots vs AI-powered robots]

[Autonomy levels - from teleoperated to fully autonomous]

<!-- AI-BLOCK: explain-like-i-am-10 -->

[Real-world applications - self-driving cars, warehouse robots, surgical robots]

<!-- DIAGRAM: ai-robotics-stack -->
```

**Validation**:
- Explains autonomy levels concept
- AI-block placeholder present (explain-like-i-am-10 type)
- Diagram placeholder present

---

### Step 1.5: Write Section 4 - Core Concepts Introduced in This Book

**Content Requirements** (from spec FR-006):
- Explanations of 5 core concepts: Embodiment, Perception, Decision-making, Control, Interaction
- Example scenarios for each concept
- Diagram placeholder: `<!-- DIAGRAM: core-concepts-flow -->`

**Example Structure**:
```markdown
## Section 4: Core Concepts Introduced in This Book

This book explores five fundamental concepts that make Physical AI systems work:

**Embodiment**: [Explanation + example]

**Perception**: [Explanation + example]

**Decision-making**: [Explanation + example]

**Control**: [Explanation + example]

**Interaction**: [Explanation + example]

<!-- DIAGRAM: core-concepts-flow -->
<!-- AI-BLOCK: interactive-quiz -->
```

**Validation**:
- All 5 concepts defined with examples
- Diagram placeholder present
- AI-block placeholder present (interactive-quiz type)

---

### Step 1.6: Write Section 5 - Learning Objectives

**Content Requirements** (from spec FR-007):
- Clear bullet points stating what students should understand after Chapter 1
- Optional reflection questions

**Example Structure**:
```markdown
## Section 5: Learning Objectives

By the end of this chapter, you should be able to:

- Define Physical AI and distinguish it from Digital AI
- Identify the key components of robotic systems (sensors, actuators, controllers)
- Explain how AI enables robot autonomy
- Recognize the five core concepts: embodiment, perception, decision-making, control, and interaction
- Describe real-world applications of Physical AI systems

**Reflection Questions** (optional):
- What is the difference between a traditional robot and a Physical AI system?
- Can you think of a Physical AI system you've interacted with recently?
```

**Validation**:
- At least 4 bullet points
- Uses action verbs (Define, Identify, Explain, Recognize, Describe)
- Aligns with chapter content

---

### Step 1.7: Write Section 6 - Summary

**Content Requirements** (from spec FR-008):
- 6-8 line recap of the chapter content

**Example Structure**:
```markdown
## Section 6: Summary

In this chapter, we introduced Physical AI - artificial intelligence systems that interact with the physical world through robotic bodies. We explored what makes something a robot, learning about sensors (for perception), actuators (for movement), and controllers (for decision-making). We discovered how AI transforms traditional robots into autonomous systems capable of learning and adapting.

We also introduced five core concepts that will guide your journey through this book: embodiment (having a physical form), perception (sensing the environment), decision-making (choosing actions), control (executing movements), and interaction (engaging with people and objects). These concepts form the foundation of Physical AI systems, from self-driving cars to surgical robots to warehouse automation.

As you progress through the following chapters, you'll dive deeper into each of these concepts, learning both the theory and practical applications that are shaping the future of robotics.
```

**Validation**:
- 6-8 lines (approximately 150-200 words)
- Recaps major points from all sections
- Forward-looking statement to next chapters

---

### Step 1.8: Write Section 7 - Glossary

**Content Requirements** (from spec FR-009):
- Beginner-friendly definitions for exactly these 7 terms:
  1. Physical AI
  2. Robot
  3. Sensor
  4. Actuator
  5. Autonomy
  6. Perception
  7. Control System

**Format** (from contracts/content-schema.md):
```markdown
**Term Name**: Definition text explaining the concept in accessible language.
```

**Example Structure**:
```markdown
## Section 7: Glossary

**Physical AI**: Artificial intelligence systems that can sense, understand, and act in the physical world through robotic bodies or embodied systems. Unlike digital AI that exists only in software, Physical AI can pick up objects, navigate spaces, and interact with people and environments.

**Robot**: A programmable machine capable of carrying out tasks automatically. Robots have three key components: sensors (to perceive), actuators (to move), and controllers (to make decisions). Examples range from industrial robotic arms to autonomous vacuum cleaners.

**Sensor**: A device that detects changes in the environment and converts them into signals that a robot can understand. Common sensors include cameras (for vision), microphones (for sound), and touch sensors (for physical contact).

**Actuator**: A mechanical component that creates movement in a robot. Actuators are like a robot's muscles - they convert electrical signals into physical actions. Examples include motors, hydraulic pistons, and servo mechanisms.

**Autonomy**: The ability of a robot to make decisions and act independently without human intervention. Autonomy exists on a spectrum from teleoperated (human-controlled) to fully autonomous (completely independent).

**Perception**: The process by which a robot gathers and interprets information about its environment using sensors. Perception enables robots to understand what's around them, similar to how humans use their five senses.

**Control System**: The "brain" of a robot that processes sensor data, makes decisions, and commands actuators to perform actions. Control systems can range from simple pre-programmed routines to complex AI algorithms.
```

**Validation**:
- Exactly 7 terms defined
- Each definition is 10-100 words
- Uses analogies or concrete examples
- Avoids circular definitions
- Written at 12+ age level

---

## Phase 2: Add Interactive Placeholders (15 minutes)

### Step 2.1: Verify Placeholder Positioning

**Action**: Review the 4 AI-block placeholders placed in Phase 1

**Expected Positions** (from research.md):
1. `<!-- AI-BLOCK: ask-question -->` - End of Section 1
2. `<!-- AI-BLOCK: generate-diagram -->` - Within Section 2
3. `<!-- AI-BLOCK: explain-like-i-am-10 -->` - Middle of Section 3
4. `<!-- AI-BLOCK: interactive-quiz -->` - End of Section 4

**Validation**:
- All 4 blocks present
- Positioned at strategic learning points (not randomly placed)
- Correct syntax (see contracts/content-schema.md)

### Step 2.2: Verify Diagram Placeholders

**Action**: Review the 4 diagram placeholders placed in Phase 1

**Expected Placeholders**:
1. `<!-- DIAGRAM: physical-ai-overview -->` - Section 1
2. `<!-- DIAGRAM: robot-anatomy -->` - Section 2
3. `<!-- DIAGRAM: ai-robotics-stack -->` - Section 3
4. `<!-- DIAGRAM: core-concepts-flow -->` - Section 4

**Validation**:
- All 4 placeholders present
- Correct naming (kebab-case, matches spec)
- Correct syntax (see contracts/content-schema.md)

---

## Phase 3: Backend Metadata Scaffold (30 minutes)

### Step 3.1: Create Backend Directory Structure

**Action**: Create directory if it doesn't exist

```bash
mkdir -p backend/app/content/chapters
```

**Validation**: Directory exists at `backend/app/content/chapters/`

---

### Step 3.2: Create Chapter Metadata File

**Location**: `backend/app/content/chapters/chapter_1.py`

**Action**: Create new file with complete metadata structure

```python
"""
Chapter 1 Metadata

This module contains metadata for Chapter 1: Introduction to Physical AI & Robotics.

TODO: Future enhancement - convert to Pydantic model for validation
TODO: Future enhancement - integrate with Qdrant for vector storage
TODO: Future enhancement - add embedding generation pipeline
TODO: Future enhancement - create API endpoint to serve this metadata
"""

from typing import List

CHAPTER_METADATA = {
    # Core identification
    "id": 1,
    "title": "Chapter 1 — Introduction to Physical AI & Robotics",
    "summary": "An introductory chapter covering fundamental concepts of Physical AI, robotics components, and how AI enables autonomous physical systems. Suitable for beginners with no prior robotics knowledge.",

    # Structure information
    "section_count": 7,
    "sections": [
        "What is Physical AI?",
        "What is a Robot?",
        "AI + Robotics = Physical AI Systems",
        "Core Concepts Introduced in This Book",
        "Learning Objectives",
        "Summary",
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
        "physical-ai-overview",
        "robot-anatomy",
        "ai-robotics-stack",
        "core-concepts-flow"
    ],

    # Versioning
    "last_updated": "2025-12-05T00:00:00Z",

    # RAG-specific metadata (for future use)
    "difficulty_level": "beginner",
    "prerequisites": [],  # No prerequisites for Chapter 1
    "learning_outcomes": [
        "Define Physical AI and distinguish it from Digital AI",
        "Identify key components of robotic systems (sensors, actuators, controllers)",
        "Explain how AI enables robot autonomy",
        "Recognize core concepts: embodiment, perception, decision-making, control, interaction"
    ],
    "glossary_terms": [
        "Physical AI",
        "Robot",
        "Sensor",
        "Actuator",
        "Autonomy",
        "Perception",
        "Control System"
    ]
}
```

**Validation**:
- File can be imported: `from backend.app.content.chapters.chapter_1 import CHAPTER_METADATA`
- All required fields present (see contracts/content-schema.md)
- Values match MDX content exactly

---

### Step 3.3: Create __init__.py for Package

**Location**: `backend/app/content/__init__.py`

**Action**: Create empty file (or add docstring)

```python
"""
Content package for chapter metadata.

This package contains metadata files for all chapters in the textbook.
Each chapter has a corresponding Python module with CHAPTER_METADATA dictionary.
"""
```

**Location**: `backend/app/content/chapters/__init__.py`

**Action**: Create empty file (or add imports)

```python
"""
Chapters metadata modules.
"""
```

**Validation**: Python recognizes directories as packages

---

## Phase 4: Build Validation (15 minutes)

### Step 4.1: Frontend Build Test

**Action**: Run Docusaurus build command

```bash
cd frontend
npm run build
```

**Expected Output**: Build completes without errors

**Common Errors**:
- MDX syntax error: Check for unescaped special characters, unmatched brackets
- Frontmatter invalid: Verify YAML is properly formatted
- Missing file: Ensure file is at correct path

**Validation**:
- Build output includes `chapter-1` in generated pages
- No error messages related to `chapter-1.mdx`

---

### Step 4.2: Frontend Dev Server Test

**Action**: Start dev server and navigate to chapter

```bash
cd frontend
npm start
```

Navigate to: `http://localhost:3000/docs/chapters/chapter-1`

**Expected Behavior**:
- Page renders without errors
- Title displays: "Chapter 1 — Introduction to Physical AI & Robotics"
- All 7 sections visible in page
- Sidebar shows "Chapter 1: Intro to Physical AI" (using sidebar_label)
- Diagram and AI-block placeholders are invisible (HTML comments)

**Validation**:
- Page is accessible
- Content is readable
- No broken links or missing sections

---

### Step 4.3: Backend Metadata Import Test

**Action**: Test importing metadata file

```bash
cd backend
python -c "from app.content.chapters.chapter_1 import CHAPTER_METADATA; print(CHAPTER_METADATA['title'])"
```

**Expected Output**:
```
Chapter 1 — Introduction to Physical AI & Robotics
```

**Common Errors**:
- ModuleNotFoundError: Check directory structure, ensure `__init__.py` files exist
- SyntaxError: Check for typos in Python dictionary
- KeyError: Verify all required fields are present

**Validation**:
- Import succeeds without errors
- Can access all metadata fields

---

### Step 4.4: Content Quality Review (Manual)

**Action**: Read through entire chapter content

**Review Checklist**:
- [ ] Reading level feels appropriate for 12+ age group
- [ ] Tone is conversational but educational
- [ ] Technical terms are defined before use
- [ ] Examples are relatable and concrete
- [ ] Paragraphs are 3-4 sentences max
- [ ] Sentences are clear and not overly complex
- [ ] Glossary terms match content
- [ ] Learning objectives align with chapter content
- [ ] Summary accurately recaps all sections

**Optional Tools**:
- Flesch-Kincaid readability checker: https://readable.com/
- Grammarly or Hemingway Editor for clarity
- Peer review from someone without AI/robotics background

**Validation**: Content passes manual review against spec requirements

---

## Troubleshooting

### Issue: Docusaurus build fails with "Unexpected token"

**Cause**: MDX syntax error (unescaped braces, invalid JSX)

**Solution**:
- Check for unescaped `{`, `}`, `<`, `>` characters
- Escape special characters: `\{`, `\}`, `\<`, `\>`
- Verify HTML comment syntax: `<!-- comment -->` not `<!- comment ->`

---

### Issue: Backend import fails with "No module named 'app'"

**Cause**: Missing `__init__.py` files or incorrect directory structure

**Solution**:
- Ensure `__init__.py` exists in:
  - `backend/app/`
  - `backend/app/content/`
  - `backend/app/content/chapters/`
- Run import from `backend/` directory (not repository root)

---

### Issue: Content feels too technical or too simple

**Cause**: Mismatched reading level or audience assumptions

**Solution**:
- Review research.md content writing guidelines
- Check Flesch-Kincaid readability score (target: 7th-8th grade)
- Get feedback from target audience (12+ age group)
- Use more analogies and concrete examples for complex concepts

---

## Completion Checklist

### Phase 1: Frontend Content ✅
- [ ] MDX file created at `frontend/docs/chapters/chapter-1.mdx`
- [ ] Frontmatter includes all required fields
- [ ] Section 1 complete with diagram and AI-block placeholders
- [ ] Section 2 complete with diagram and AI-block placeholders
- [ ] Section 3 complete with diagram and AI-block placeholders
- [ ] Section 4 complete with diagram and AI-block placeholders
- [ ] Section 5 complete (Learning Objectives)
- [ ] Section 6 complete (Summary)
- [ ] Section 7 complete (Glossary with 7 terms)

### Phase 2: Interactive Placeholders ✅
- [ ] Exactly 4 AI-block placeholders present
- [ ] Exactly 4 diagram placeholders present
- [ ] All placeholders use correct syntax
- [ ] Placeholders positioned strategically

### Phase 3: Backend Metadata ✅
- [ ] Directory `backend/app/content/chapters/` created
- [ ] File `chapter_1.py` created with CHAPTER_METADATA
- [ ] All required metadata fields present
- [ ] Metadata values match MDX content
- [ ] `__init__.py` files created for packages

### Phase 4: Validation ✅
- [ ] `npm run build` completes without errors
- [ ] Dev server renders chapter without errors
- [ ] Python import of metadata succeeds
- [ ] Manual content quality review passed
- [ ] Git status shows both files tracked

### Final Verification ✅
- [ ] All acceptance criteria from spec.md met
- [ ] No NEEDS CLARIFICATION markers remain
- [ ] Feature ready for PR and review

---

## Next Steps After Implementation

1. **Commit changes**:
   ```bash
   git add frontend/docs/chapters/chapter-1.mdx
   git add backend/app/content/chapters/chapter_1.py
   git add backend/app/content/__init__.py
   git add backend/app/content/chapters/__init__.py
   git commit -m "feat(003): Add Chapter 1 written content with placeholders"
   ```

2. **Run `/sp.tasks`** command to generate task list

3. **Run `/sp.implement`** to begin TDD implementation (if required)

4. **Create PR** when ready for review

---

## Estimated Time Breakdown

| Phase | Task | Estimated Time |
|-------|------|----------------|
| 1.1   | Create MDX file with frontmatter | 5 min |
| 1.2   | Write Section 1 (What is Physical AI?) | 30 min |
| 1.3   | Write Section 2 (What is a Robot?) | 30 min |
| 1.4   | Write Section 3 (AI + Robotics) | 30 min |
| 1.5   | Write Section 4 (Core Concepts) | 30 min |
| 1.6   | Write Section 5 (Learning Objectives) | 15 min |
| 1.7   | Write Section 6 (Summary) | 15 min |
| 1.8   | Write Section 7 (Glossary) | 20 min |
| 2     | Verify placeholders | 15 min |
| 3     | Create backend metadata | 30 min |
| 4     | Build validation | 15 min |
| **Total** | | **2-4 hours** |

**Note**: Time varies significantly based on writing speed and subject matter expertise. Content writing is inherently time-intensive. Budget additional time for revisions and quality review.

---

## Support Resources

- **Specification**: `specs/003-chapter-1-content/spec.md`
- **Research**: `specs/003-chapter-1-content/research.md` (writing guidelines)
- **Data Model**: `specs/003-chapter-1-content/data-model.md` (entity definitions)
- **Contracts**: `specs/003-chapter-1-content/contracts/content-schema.md` (validation rules)
- **Docusaurus Docs**: https://docusaurus.io/docs/markdown-features
- **MDX Docs**: https://mdxjs.com/docs/what-is-mdx/

---

**Last Updated**: 2025-12-05
**Maintainer**: Feature 003 implementation team
