# Quickstart Guide: Implementing Chapter 2 Written Content

**Feature**: 010-chapter-2-content
**Branch**: `010-chapter-2-content`
**Estimated Time**: 2-4 hours (content writing is time-intensive)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 001 (Base Project Initialization) completed
- [x] Feature 003 (Chapter 1 Content) completed (prerequisite)
- [x] Docusaurus frontend running at `http://localhost:3000`
- [x] FastAPI backend structure exists at `backend/app/`
- [x] Git branch `010-chapter-2-content` checked out
- [x] Read `specs/010-chapter-2-content/spec.md`
- [x] Read `specs/010-chapter-2-content/research.md` (content writing guidelines, ROS 2 analogies)
- [x] Read `specs/010-chapter-2-content/data-model.md` (entity definitions)
- [x] Read `specs/010-chapter-2-content/contracts/content-schema.md` (validation rules)
- [x] Reviewed Chapter 1 content structure (`frontend/docs/chapters/chapter-1.mdx`) for pattern consistency

## Implementation Overview

**Total Steps**: 4 phases
**Primary Deliverable**: MDX file with complete Chapter 2 ROS 2 content
**Secondary Deliverable**: Backend metadata file
**Validation**: Manual review + Docusaurus build test
**Prerequisite**: Chapter 1 must exist (prerequisites=[1] in metadata)

---

## Phase 1: Frontend Content Creation (2-3 hours)

### Step 1.1: Create MDX File with Frontmatter

**Location**: `frontend/docs/chapters/chapter-2.mdx`

**Action**: Create new file and add frontmatter:

```yaml
---
title: "Chapter 2 — ROS 2 Fundamentals"
description: "Learn ROS 2 fundamentals including nodes, topics, services, actions, packages, and launch files for robotics development"
sidebar_position: 2
sidebar_label: "Chapter 2: ROS 2 Fundamentals"
tags: ["ros2", "robotics", "programming", "beginner"]
---
```

**Validation**:
- Title starts with "Chapter 2 — "
- Description is 10-250 characters
- sidebar_position is 2 (matches chapter number)

---

### Step 1.2: Write Section 1 - Introduction to ROS 2

**Content Requirements** (from spec FR-003):
- Definition of ROS 2
- Why ROS 2 exists
- Differences from ROS 1 (brief mention)
- At least 3 real-world examples of ROS 2 usage
- Diagram placeholder: `<!-- DIAGRAM: ros2-ecosystem-overview -->`
- Reading level: 7th-8th grade

**Writing Guidelines** (from research.md):
- Use conversational tone with second-person "you"
- Paragraphs: 3-4 sentences max
- Sentences: 15-20 words average
- Use analogies (post office, restaurant, phone calls)
- Lead with topic sentence, follow with explanation and example

**Example Opening**:
```markdown
## Introduction to ROS 2

Imagine you're building a robot that needs to see, think, and move all at the same time. The camera needs to tell the brain what it sees. The brain needs to tell the wheels where to go. The sensors need to warn about obstacles. How do all these parts talk to each other? That's where **ROS 2** comes in—it's like a language that helps all the robot's parts communicate.

[Continue with definition, why ROS 2 exists, examples...]

<!-- DIAGRAM: ros2-ecosystem-overview -->
<!-- AI-BLOCK: ask-question -->
```

**Validation**:
- Section heading is H2 (`##`)
- Diagram placeholder present and correctly formatted
- AI-block placeholder present (ask-question type)
- Content is at least 200 words
- Uses real-world ROS 2 examples (turtlebot, navigation stacks)

---

### Step 1.3: Write Section 2 - Nodes and Node Communication

**Content Requirements** (from spec FR-004):
- Explanation of what nodes are
- How nodes communicate
- Node lifecycle
- Examples using analogies (restaurant kitchen staff)

**Example Structure**:
```markdown
## Nodes and Node Communication

[Definition of nodes - like independent workers]

[How nodes communicate - through messages]

[Node lifecycle - starting, running, stopping]

[Examples - camera node, motor control node, navigation node]

<!-- DIAGRAM: node-communication-architecture -->
<!-- AI-BLOCK: generate-diagram -->
```

**Validation**:
- Explains node concept clearly
- Uses analogies (restaurant, post office)
- Diagram placeholder present
- AI-block placeholder present (generate-diagram type)

---

### Step 1.4: Write Section 3 - Topics and Messages

**Content Requirements** (from spec FR-005):
- Explanation of topics (publish/subscribe)
- Message types
- Topic naming conventions
- Practical examples (radio broadcast analogy)

**Example Structure**:
```markdown
## Topics and Messages

[What are topics - publish/subscribe pattern]

[How topics work - one publisher, many subscribers]

[Message types - what data flows through topics]

[Topic naming conventions - /camera/image, /motor/velocity]

<!-- DIAGRAM: topic-pubsub-flow -->
<!-- AI-BLOCK: explain-like-i-am-10 -->
```

**Validation**:
- Explains publish/subscribe pattern clearly
- Uses analogies (radio broadcast)
- Diagram placeholder present
- AI-block placeholder present (explain-like-i-am-10 type)

---

### Step 1.5: Write Section 4 - Services and Actions

**Content Requirements** (from spec FR-006):
- Explanation of services (request/response)
- Explanation of actions (long-running tasks)
- Differences between topics/services/actions
- When to use each (phone call vs package delivery analogies)

**Example Structure**:
```markdown
## Services and Actions

[What are services - request/response, immediate answer]

[What are actions - long-running tasks with progress]

[Differences - topics vs services vs actions]

[When to use each - examples]

<!-- DIAGRAM: services-actions-comparison -->
<!-- AI-BLOCK: interactive-quiz -->
```

**Validation**:
- Explains services and actions clearly
- Compares topics/services/actions
- Uses analogies (phone calls, package delivery)
- Diagram placeholder present
- AI-block placeholder present (interactive-quiz type)

---

### Step 1.6: Write Section 5 - ROS 2 Packages

**Content Requirements** (from spec FR-007):
- Explanation of ROS 2 packages
- Package structure
- Dependencies
- How packages organize code

**Example Structure**:
```markdown
## ROS 2 Packages

[What are packages - organizing robot code]

[Package structure - folders and files]

[Dependencies - what packages need from each other]

[How packages organize code - modular design]
```

**Validation**:
- Explains package concept clearly
- Describes structure and organization
- Uses real-world examples

---

### Step 1.7: Write Section 6 - Launch Files and Workflows

**Content Requirements** (from spec FR-008):
- Explanation of launch files
- How to start multiple nodes
- Real-world robotics workflows
- Common patterns

**Example Structure**:
```markdown
## Launch Files and Workflows

[What are launch files - starting multiple nodes together]

[How launch files work - coordinating robot systems]

[Real-world workflows - warehouse robot, navigation stack]

[Common patterns - starting camera, navigation, motor control together]
```

**Validation**:
- Explains launch files clearly
- Uses real-world ROS 2 examples
- Describes workflows

---

### Step 1.8: Write Section 7 - Learning Objectives

**Content Requirements** (from spec FR-009):
- Clear bullet points stating what students should understand after Chapter 2
- Optional reflection questions

**Example Structure**:
```markdown
## Learning Objectives

By the end of this chapter, you should be able to:

- Define ROS 2 and explain its purpose in robotics development
- Identify the key components of ROS 2: nodes, topics, services, actions
- Explain how nodes communicate using topics, services, and actions
- Describe the structure and purpose of ROS 2 packages
- Recognize how launch files coordinate multiple nodes in robotics workflows

**Reflection Questions** (optional):
- How is ROS 2 like a communication system for robots?
- What's the difference between a topic and a service?
```

**Validation**:
- At least 4-6 bullet points
- Uses action verbs (Define, Identify, Explain, Describe, Recognize)
- Aligns with chapter content

---

### Step 1.9: Write Section 8 - Summary

**Content Requirements** (from spec FR-010):
- 6-8 line recap of the chapter content

**Example Structure**:
```markdown
## Summary

In this chapter, we introduced ROS 2—a framework that helps different parts of a robot communicate with each other. We learned about nodes (independent workers), topics (one-way communication channels), services (request-response), and actions (long-running tasks). We explored how ROS 2 packages organize code and how launch files coordinate multiple nodes to create complete robotics systems.

Understanding these ROS 2 fundamentals prepares you to build and program robots that can see, think, and act in the real world. In the next chapters, you'll learn how to use these concepts to create actual robot behaviors and applications.
```

**Validation**:
- 6-8 lines (approximately 150-200 words)
- Recaps major points from all sections
- Forward-looking statement to next chapters

---

### Step 1.10: Write Section 9 - Glossary

**Content Requirements** (from spec FR-011):
- Beginner-friendly definitions for exactly these 7 terms:
  1. ROS 2
  2. Node
  3. Topic
  4. Service
  5. Action
  6. Package
  7. Launch File

**Format** (from contracts/content-schema.md):
```markdown
**Term Name**: Definition text explaining the concept in accessible language.
```

**Example Structure**:
```markdown
## Glossary

**ROS 2**: Robot Operating System 2, a framework that provides tools and libraries for building robot software. ROS 2 helps different parts of a robot (sensors, processors, motors) communicate with each other, making it easier to build complex robotic systems. Think of it as the "nervous system" that connects all the robot's components.

**Node**: An independent program or process in ROS 2 that performs a specific task. Each node has one job—like processing camera images, controlling motors, or planning navigation paths. Nodes communicate with each other to work together, similar to how workers in a restaurant kitchen coordinate to prepare a meal.

**Topic**: A communication channel in ROS 2 where one node publishes messages and other nodes subscribe to receive them. Topics work like radio broadcasts—one station sends out information, and many listeners can tune in. Topics are used for continuous data streams, like camera images or sensor readings.

**Service**: A communication method in ROS 2 where one node sends a request and another node responds with an answer. Services work like phone calls—you ask a question, get an immediate answer, and the conversation ends. Services are used for one-time requests, like "Is the gripper open?" or "What is the current battery level?"

**Action**: A communication method in ROS 2 for long-running tasks that take time to complete. Actions work like package delivery—you place an order, the delivery takes time, you get progress updates, and finally receive the result. Actions are used for tasks like "Move the robot arm to this position" or "Navigate to this location."

**Package**: A folder containing related ROS 2 code, configuration files, and resources. Packages organize robot software into manageable modules, similar to how apps on your phone are organized. Each package has a specific purpose, like camera processing, navigation, or motor control.

**Launch File**: A configuration file in ROS 2 that starts multiple nodes together and sets up how they communicate. Launch files are like a recipe for starting a complete robot system—they tell ROS 2 which nodes to run, what parameters to use, and how everything should work together. This makes it easy to start complex robotics applications with a single command.
```

**Validation**:
- Exactly 7 terms defined
- Each definition is 10-100 words
- Uses analogies or concrete examples (post office, restaurant, phone calls)
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
- Positioned at strategic learning points
- Correct syntax (see contracts/content-schema.md)

### Step 2.2: Verify Diagram Placeholders

**Action**: Review the 4 diagram placeholders placed in Phase 1

**Expected Placeholders**:
1. `<!-- DIAGRAM: ros2-ecosystem-overview -->` - Section 1
2. `<!-- DIAGRAM: node-communication-architecture -->` - Section 2
3. `<!-- DIAGRAM: topic-pubsub-flow -->` - Section 3
4. `<!-- DIAGRAM: services-actions-comparison -->` - Section 4

**Validation**:
- All 4 placeholders present
- Correct naming (kebab-case, matches spec)
- Correct syntax (see contracts/content-schema.md)

---

## Phase 3: Backend Metadata Scaffold (30 minutes)

### Step 3.1: Verify Backend Directory Structure

**Action**: Verify directory exists (created in Chapter 1)

```bash
ls backend/app/content/chapters/
```

**Validation**: Directory exists at `backend/app/content/chapters/`

---

### Step 3.2: Create Chapter Metadata File

**Location**: `backend/app/content/chapters/chapter_2.py`

**Action**: Create new file with complete metadata structure

```python
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
"""

from typing import List

CHAPTER_METADATA = {
    # Core identification
    "id": 2,
    "title": "Chapter 2 — ROS 2 Fundamentals",
    "summary": "An introductory chapter covering ROS 2 fundamentals including nodes, topics, services, actions, packages, and launch files. Explores how robots communicate and coordinate their components using ROS 2 framework. Suitable for beginners with Chapter 1 prerequisite knowledge.",

    # Structure information
    "section_count": 7,
    "sections": [
        "Introduction to ROS 2",
        "Nodes and Node Communication",
        "Topics and Messages",
        "Services and Actions",
        "ROS 2 Packages",
        "Launch Files and Workflows",
        "Learning Objectives",
        "Summary",
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
        "Define ROS 2 and explain its purpose in robotics development",
        "Identify the key components of ROS 2: nodes, topics, services, actions",
        "Explain how nodes communicate using topics, services, and actions",
        "Describe the structure and purpose of ROS 2 packages",
        "Recognize how launch files coordinate multiple nodes in robotics workflows"
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
```

**Validation**:
- File can be imported: `from backend.app.content.chapters.chapter_2 import CHAPTER_METADATA`
- All required fields present (see contracts/content-schema.md)
- Values match MDX content exactly
- `prerequisites` contains [1]
- `id` is 2

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
- Build output includes `chapter-2` in generated pages
- No error messages related to `chapter-2.mdx`

---

### Step 4.2: Frontend Dev Server Test

**Action**: Start dev server and navigate to chapter

```bash
cd frontend
npm start
```

Navigate to: `http://localhost:3000/docs/chapters/chapter-2`

**Expected Behavior**:
- Page renders without errors
- Title displays: "Chapter 2 — ROS 2 Fundamentals"
- All 7 sections visible in page
- Sidebar shows "Chapter 2: ROS 2 Fundamentals" (using sidebar_label)
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
python -c "from app.content.chapters.chapter_2 import CHAPTER_METADATA; print(CHAPTER_METADATA['title'])"
```

**Expected Output**:
```
Chapter 2 — ROS 2 Fundamentals
```

**Common Errors**:
- ModuleNotFoundError: Check directory structure, ensure `__init__.py` files exist
- SyntaxError: Check for typos in Python dictionary
- KeyError: Verify all required fields are present

**Validation**:
- Import succeeds without errors
- Can access all metadata fields
- `prerequisites` field contains [1]

---

### Step 4.4: Metadata Matching Validation

**Action**: Verify metadata matches MDX 100%

**Checklist**:
- [ ] `title` matches MDX frontmatter title exactly
- [ ] `section_count` matches number of H2 sections (7)
- [ ] `sections[]` matches H2 headings in order
- [ ] `ai_blocks[]` matches AI-block placeholders in MDX
- [ ] `diagram_placeholders[]` matches diagram placeholders in MDX
- [ ] `glossary_terms[]` matches terms in Glossary section
- [ ] `prerequisites` contains [1]

**Validation**: All fields match MDX content

---

### Step 4.5: Content Quality Review (Manual)

**Action**: Read through entire chapter content

**Review Checklist**:
- [ ] Reading level feels appropriate for 12+ age group
- [ ] Tone is conversational but educational (matches Chapter 1)
- [ ] Technical terms are defined before use
- [ ] Examples use real-world ROS 2 applications
- [ ] Analogies are clear (post office, restaurant, phone calls)
- [ ] Paragraphs are 3-4 sentences max
- [ ] Sentences are clear and not overly complex (15-20 words)
- [ ] Glossary terms match content
- [ ] Learning objectives align with chapter content
- [ ] Summary accurately recaps all sections
- [ ] Follows Chapter 1 content patterns

**Optional Tools**:
- Flesch-Kincaid readability checker: https://readable.com/
- Grammarly or Hemingway Editor for clarity
- Peer review from someone without ROS 2 background

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
- Reference Chapter 1 content style for consistency

---

### Issue: Prerequisites validation fails

**Cause**: Chapter 1 content doesn't exist or metadata mismatch

**Solution**:
- Verify Chapter 1 MDX file exists: `frontend/docs/chapters/chapter-1.mdx`
- Verify Chapter 1 metadata exists: `backend/app/content/chapters/chapter_1.py`
- Ensure `prerequisites: [1]` in Chapter 2 metadata

---

## Completion Checklist

### Phase 1: Frontend Content ✅
- [ ] MDX file created at `frontend/docs/chapters/chapter-2.mdx`
- [ ] Frontmatter includes all required fields (sidebar_position=2)
- [ ] Section 1 complete with diagram and AI-block placeholders
- [ ] Section 2 complete with diagram and AI-block placeholders
- [ ] Section 3 complete with diagram and AI-block placeholders
- [ ] Section 4 complete with diagram and AI-block placeholders
- [ ] Section 5 complete (ROS 2 Packages)
- [ ] Section 6 complete (Launch Files and Workflows)
- [ ] Section 7 complete (Learning Objectives)
- [ ] Section 8 complete (Summary)
- [ ] Section 9 complete (Glossary with 7 terms)

### Phase 2: Interactive Placeholders ✅
- [ ] Exactly 4 AI-block placeholders present
- [ ] Exactly 4 diagram placeholders present
- [ ] All placeholders use correct syntax
- [ ] Placeholders positioned strategically

### Phase 3: Backend Metadata ✅
- [ ] File `chapter_2.py` created with CHAPTER_METADATA
- [ ] All required metadata fields present
- [ ] Metadata values match MDX content 100%
- [ ] `prerequisites` field contains [1]
- [ ] `id` is 2

### Phase 4: Validation ✅
- [ ] `npm run build` completes without errors
- [ ] Dev server renders chapter without errors
- [ ] Python import of metadata succeeds
- [ ] Metadata matching validation passed
- [ ] Manual content quality review passed
- [ ] Git status shows both files tracked

### Final Verification ✅
- [ ] All acceptance criteria from spec.md met
- [ ] No NEEDS CLARIFICATION markers remain
- [ ] Feature ready for PR and review
- [ ] Chapter 1 prerequisite verified

---

## Next Steps After Implementation

1. **Commit changes**:
   ```bash
   git add frontend/docs/chapters/chapter-2.mdx
   git add backend/app/content/chapters/chapter_2.py
   git commit -m "feat(010): Add Chapter 2 ROS 2 content with placeholders"
   ```

2. **Run `/sp.plan`** command to create architectural plan

3. **Run `/sp.tasks`** command to generate task list

4. **Run `/sp.implement`** to begin implementation (if required)

5. **Create PR** when ready for review

---

## Estimated Time Breakdown

| Phase | Task | Estimated Time |
|-------|------|----------------|
| 1.1   | Create MDX file with frontmatter | 5 min |
| 1.2   | Write Section 1 (Introduction to ROS 2) | 30 min |
| 1.3   | Write Section 2 (Nodes) | 30 min |
| 1.4   | Write Section 3 (Topics) | 30 min |
| 1.5   | Write Section 4 (Services and Actions) | 30 min |
| 1.6   | Write Section 5 (Packages) | 20 min |
| 1.7   | Write Section 6 (Launch Files) | 20 min |
| 1.8   | Write Section 7 (Learning Objectives) | 15 min |
| 1.9   | Write Section 8 (Summary) | 15 min |
| 1.10  | Write Section 9 (Glossary) | 20 min |
| 2     | Verify placeholders | 15 min |
| 3     | Create backend metadata | 30 min |
| 4     | Build validation | 15 min |
| **Total** | | **2-4 hours** |

**Note**: Time varies significantly based on writing speed and subject matter expertise. Content writing is inherently time-intensive. Budget additional time for revisions and quality review.

---

## Support Resources

- **Specification**: `specs/010-chapter-2-content/spec.md`
- **Research**: `specs/010-chapter-2-content/research.md` (writing guidelines, ROS 2 analogies)
- **Data Model**: `specs/010-chapter-2-content/data-model.md` (entity definitions)
- **Contracts**: `specs/010-chapter-2-content/contracts/content-schema.md` (validation rules)
- **Chapter 1 Reference**: `frontend/docs/chapters/chapter-1.mdx` (pattern consistency)
- **Docusaurus Docs**: https://docusaurus.io/docs/markdown-features
- **MDX Docs**: https://mdxjs.com/docs/what-is-mdx/
- **ROS 2 Documentation**: https://docs.ros.org/en/humble/

---

**Last Updated**: 2025-12-05
**Maintainer**: Feature 010 implementation team
