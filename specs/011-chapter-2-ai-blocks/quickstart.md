# Quickstart: Chapter 2 AI Blocks Integration

**Feature**: 011-chapter-2-ai-blocks
**Date**: 2025-12-05
**Purpose**: Step-by-step implementation guide for integrating AI blocks into Chapter 2

## Overview

This quickstart guide provides step-by-step instructions for enabling AI-interactive blocks in Chapter 2 (ROS 2 Fundamentals) using existing infrastructure from Chapter 1. The implementation involves:

1. Updating Chapter 2 MDX file with React components
2. Creating Chapter 2 chunks placeholder file
3. Extending runtime engine with Chapter 2 mapping
4. Adding TODO sections to subagents
5. Validating integration

**Estimated Time**: 1-2 hours (scaffolding only, no real AI logic)

---

## Prerequisites

- ✅ Feature 004 (Chapter 1 Interactive AI Blocks) - Components and infrastructure exist
- ✅ Feature 010 (Chapter 2 Content) - Chapter 2 MDX file exists with HTML comment placeholders
- ✅ Docusaurus frontend running
- ✅ FastAPI backend running
- ✅ Git branch `011-chapter-2-ai-blocks` checked out

---

## Phase 1: Frontend MDX Updates (30 minutes)

### Step 1.1: Add Component Imports

**File**: `frontend/docs/chapters/chapter-2.mdx`

**Action**: Add import statements at the top of the file (after frontmatter):

```mdx
import AskQuestionBlock from '@site/src/components/ai/AskQuestionBlock';
import ExplainLike10Block from '@site/src/components/ai/ExplainLike10Block';
import InteractiveQuizBlock from '@site/src/components/ai/InteractiveQuizBlock';
import GenerateDiagramBlock from '@site/src/components/ai/GenerateDiagramBlock';
```

**Validation**: Save file, check for TypeScript errors.

---

### Step 1.2: Replace Ask Question Placeholder

**File**: `frontend/docs/chapters/chapter-2.mdx`

**Location**: After "Introduction to ROS 2" section

**Action**: Replace:
```mdx
<!-- AI-BLOCK: ask-question -->
```

With:
```mdx
<AskQuestionBlock chapterId={2} sectionId="introduction-to-ros2" />
```

**Validation**: Component should render in designated location.

---

### Step 1.3: Replace Generate Diagram Placeholder

**File**: `frontend/docs/chapters/chapter-2.mdx`

**Location**: After "Nodes and Node Communication" section

**Action**: Replace:
```mdx
<!-- AI-BLOCK: generate-diagram -->
```

With:
```mdx
<GenerateDiagramBlock diagramType="node-communication-architecture" chapterId={2} />
```

**Validation**: Component should render in designated location.

---

### Step 1.4: Replace Explain Like 10 Placeholder

**File**: `frontend/docs/chapters/chapter-2.mdx`

**Location**: Inside "Topics and Messages" section

**Action**: Replace:
```mdx
<!-- AI-BLOCK: explain-like-i-am-10 -->
```

With:
```mdx
<ExplainLike10Block concept="topics" chapterId={2} />
```

**Validation**: Component should render in designated location.

---

### Step 1.5: Replace Interactive Quiz Placeholder

**File**: `frontend/docs/chapters/chapter-2.mdx`

**Location**: After "Services and Actions" section

**Action**: Replace:
```mdx
<!-- AI-BLOCK: interactive-quiz -->
```

With:
```mdx
<InteractiveQuizBlock chapterId={2} numQuestions={5} />
```

**Validation**: Component should render in designated location.

---

### Step 1.6: Validate Docusaurus Build

**Command**: `cd frontend && npm run build`

**Expected**: Build completes without errors

**Validation Checklist**:
- [ ] No TypeScript compilation errors
- [ ] No missing component errors
- [ ] MDX file compiles successfully
- [ ] All 4 AI block components imported correctly

---

## Phase 2: Backend Chunks File (15 minutes)

### Step 2.1: Create Chapter 2 Chunks File

**File**: `backend/app/content/chapters/chapter_2_chunks.py`

**Action**: Create file with placeholder function:

```python
"""
Chapter 2 Content Chunks

Provides chapter content chunks for RAG pipeline.
Chunks are used for semantic search and context retrieval.
"""

from typing import List, Dict, Any


def get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:
    """
    Return list of text chunks from Chapter 2 with metadata.
    
    Args:
        chapter_id: Chapter identifier (default: 2 for Chapter 2)
    
    Returns:
        List of chunk dictionaries with structure:
        [
            {
                "id": str,                    # Unique chunk ID
                "text": str,                  # Chunk text content
                "chapter_id": 2,             # Chapter identifier
                "section_id": str,           # Section identifier (e.g., "introduction-to-ros2")
                "position": int,              # Position in chapter (0-based)
                "word_count": int,           # Word count
                "metadata": {                # Additional metadata
                    "heading": str,         # Section heading
                    "type": str             # "paragraph", "heading", "glossary", etc.
                }
            },
            ...
        ]
    
    TODO: Implement chunking from Chapter 2 MDX content
    TODO: Load Chapter 2 content from frontend/docs/chapters/chapter-2.mdx
    TODO: Implement chunking strategy:
        - Option 1: Chunk by section (H2 headings)
        - Option 2: Chunk by paragraph
        - Option 3: Semantic chunking (overlapping windows)
    TODO: Extract metadata (section titles, positions, word counts)
    TODO: Generate unique chunk IDs (format: "ch2-s{section}-c{chunk}")
    TODO: Handle special content (glossary, diagrams, AI blocks)
    TODO: Cache chunks for performance
    """
    # Placeholder return - no real chunking implementation
    return []
```

**Validation**: File should be importable: `python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks"`

---

## Phase 3: Runtime Engine Mapping (15 minutes)

### Step 3.1: Add Chapter 2 Knowledge Source Mapping

**File**: `backend/app/ai/runtime/engine.py`

**Location**: Near knowledge source definitions

**Action**: Add Chapter 2 mapping and TODO comments:

```python
# Knowledge source mapping
knowledge_sources = {
    1: "chapter_1_chunks",  # Existing
    2: "chapter_2_chunks",  # NEW for Chapter 2
}

# TODO: Chapter 2 (ROS 2) RAG Integration
# When chapterId=2:
#   1. Import get_chapter_chunks from app.content.chapters.chapter_2_chunks
#   2. Call get_chapter_chunks(chapter_id=2) to retrieve Chapter 2 chunks
#   3. Use chunks for RAG retrieval (semantic search in Qdrant)
#   4. Filter chunks by section_id when sectionId provided in request
#   5. Pass Chapter 2 context (chunks + metadata) to subagents
#   6. Subagents will use ROS 2-specific context for LLM prompts
```

**Validation**: File should import without errors.

---

### Step 3.2: Add Chapter 2 Routing Logic (Placeholder)

**File**: `backend/app/ai/runtime/engine.py`

**Location**: In `run_ai_block()` function

**Action**: Add placeholder routing logic:

```python
# TODO: Chapter 2 routing
# if request_data.get("chapterId") == 2:
#     from app.content.chapters.chapter_2_chunks import get_chapter_chunks
#     chunks = get_chapter_chunks(chapter_id=2)
#     # Use chunks for RAG retrieval
#     # Pass to subagent with Chapter 2 context
```

**Validation**: File should import without errors, no breaking changes to Chapter 1.

---

## Phase 4: Subagent TODO Sections (20 minutes)

### Step 4.1: Add TODO to Ask Question Agent

**File**: `backend/app/ai/subagents/ask_question_agent.py`

**Location**: After existing TODO comments

**Action**: Add Chapter 2 TODO section:

```python
# TODO: Chapter 2 (ROS 2) Integration
# Expected ROS 2 inputs:
#   - Questions about: nodes, topics, services, actions, packages, launch files
#   - Section-specific: introduction-to-ros2, nodes-and-node-communication, topics-and-messages, services-and-actions
# Expected output format: Same as Chapter 1, but with ROS 2 context
# ROS 2-specific considerations:
#   - Use ROS 2 analogies (post office, restaurant, phone calls, package delivery)
#   - Reference real-world examples (TurtleBot 3, navigation stack, robot arm control)
#   - Handle ROS 2 terminology correctly (nodes, topics, services, actions)
#   - Include section context when sectionId provided
```

**Validation**: File should import without errors.

---

### Step 4.2: Add TODO to Explain Like 10 Agent

**File**: `backend/app/ai/subagents/explain_el10_agent.py`

**Location**: After existing TODO comments

**Action**: Add Chapter 2 TODO section:

```python
# TODO: Chapter 2 (ROS 2) Integration
# Expected ROS 2 inputs:
#   - Concepts: "topics", "nodes", "services", "actions", "packages", "launch-files"
#   - Chapter context: chapterId=2
# Expected output format: Same as Chapter 1, but with ROS 2 analogies
# ROS 2-specific considerations:
#   - Use ROS 2 analogies: post office (communication), restaurant (nodes), radio broadcast (topics), phone calls (services), package delivery (actions)
#   - Reference real-world examples: TurtleBot 3, navigation stack, robot arm control
#   - Simplify ROS 2 terminology for age-appropriate explanations
#   - Include visual analogies when helpful
```

**Validation**: File should import without errors.

---

### Step 4.3: Add TODO to Quiz Agent

**File**: `backend/app/ai/subagents/quiz_agent.py`

**Location**: After existing TODO comments

**Action**: Add Chapter 2 TODO section:

```python
# TODO: Chapter 2 (ROS 2) Integration
# Expected ROS 2 inputs:
#   - Chapter context: chapterId=2
#   - Learning objectives from Chapter 2 metadata
#   - ROS 2 concepts: nodes, topics, services, actions, packages, launch files
# Expected output format: Same as Chapter 1, but with ROS 2 questions
# ROS 2-specific considerations:
#   - Generate questions covering all ROS 2 fundamentals
#   - Include questions about: node communication, topic pub/sub, services vs actions, package structure, launch files
#   - Use ROS 2 terminology correctly in questions and answers
#   - Reference real-world ROS 2 examples in questions
```

**Validation**: File should import without errors.

---

### Step 4.4: Add TODO to Diagram Agent

**File**: `backend/app/ai/subagents/diagram_agent.py`

**Location**: After existing TODO comments

**Action**: Add Chapter 2 TODO section:

```python
# TODO: Chapter 2 (ROS 2) Integration
# Expected ROS 2 inputs:
#   - Diagram types: "ros2-ecosystem-overview", "node-communication-architecture", "topic-pubsub-flow", "services-actions-comparison"
#   - Chapter context: chapterId=2
#   - ROS 2 concepts: nodes, topics, services, actions
# Expected output format: Same as Chapter 1, but with ROS 2 diagram content
# ROS 2-specific considerations:
#   - Generate diagrams showing ROS 2 architecture (nodes, topics, services, actions)
#   - Include node communication graphs
#   - Show topic publish/subscribe flows
#   - Compare services vs actions visually
#   - Use ROS 2 terminology in diagram labels
```

**Validation**: File should import without errors.

---

## Phase 5: API Routing Validation (10 minutes)

### Step 5.1: Verify API Routing

**File**: `backend/app/api/ai_blocks.py`

**Action**: Verify that chapterId=2 flows correctly to runtime engine (should work automatically if routing is generic)

**Check**: Review routing logic, ensure no chapterId-specific restrictions

**Validation**: API endpoints should accept chapterId=2 in requests.

---

### Step 5.2: Test Backend Startup

**Command**: Start FastAPI backend

**Expected**: Backend starts without errors

**Validation Checklist**:
- [ ] No import errors
- [ ] All modules import correctly
- [ ] API endpoints registered
- [ ] No syntax errors

---

## Phase 6: Integration Testing (20 minutes)

### Step 6.1: Test Frontend Component Rendering

**Command**: `cd frontend && npm start`

**Action**: Navigate to `/docs/chapters/chapter-2`

**Validation Checklist**:
- [ ] All 4 AI block components render correctly
- [ ] Components appear in correct locations
- [ ] No React errors in browser console
- [ ] Components display placeholder UI

---

### Step 6.2: Test Component Props

**Action**: Inspect each AI block component in browser DevTools

**Validation Checklist**:
- [ ] AskQuestionBlock has `chapterId={2}` and `sectionId="introduction-to-ros2"`
- [ ] GenerateDiagramBlock has `diagramType="node-communication-architecture"` and `chapterId={2}`
- [ ] ExplainLike10Block has `concept="topics"` and `chapterId={2}`
- [ ] InteractiveQuizBlock has `chapterId={2}` and `numQuestions={5}`

---

### Step 6.3: Test API Endpoints (Optional)

**Command**: Use curl or Postman to test endpoints

**Example Request**:
```bash
curl -X POST http://localhost:8000/api/ai/ask-question \
  -H "Content-Type: application/json" \
  -d '{"question": "What is ROS 2?", "chapterId": 2, "sectionId": "introduction-to-ros2"}'
```

**Expected Response**:
```json
{
  "message": "AI block placeholder",
  "received": {
    "question": "What is ROS 2?",
    "chapterId": 2,
    "sectionId": "introduction-to-ros2"
  }
}
```

**Validation**: All 4 endpoints should accept chapterId=2 and return placeholder responses.

---

## Completion Checklist

- [ ] Chapter 2 MDX file updated with all 4 AI block components
- [ ] Component imports added to chapter-2.mdx
- [ ] All HTML comment placeholders replaced with React components
- [ ] chapter_2_chunks.py created with placeholder function
- [ ] Runtime engine updated with Chapter 2 knowledge source mapping
- [ ] All 4 subagents have Chapter 2 TODO sections
- [ ] API routing verified for chapterId=2
- [ ] Docusaurus build succeeds
- [ ] Backend starts without errors
- [ ] All imports resolve correctly
- [ ] Components render correctly in browser
- [ ] No React errors in console
- [ ] No backend errors in logs

---

## Troubleshooting

### Issue: Components don't render in chapter-2.mdx

**Solution**: 
- Check import statements are correct
- Verify component names match exactly
- Check Docusaurus build for errors
- Verify MDX component mapping is configured

### Issue: Backend import errors

**Solution**:
- Check `chapter_2_chunks.py` file exists and is importable
- Verify function signature matches expected pattern
- Check all subagent files have valid Python syntax
- Verify runtime engine imports resolve

### Issue: API endpoints don't accept chapterId=2

**Solution**:
- Check API routing logic is generic (not hardcoded to chapterId=1)
- Verify request models accept chapterId parameter
- Check runtime engine mapping includes chapterId=2

---

## Next Steps

After completing this quickstart:

1. **Content Writing**: Write actual Chapter 2 content (if not already done)
2. **Chunking Implementation**: Implement real chunking logic in `chapter_2_chunks.py`
3. **RAG Integration**: Connect Chapter 2 chunks to RAG pipeline
4. **Subagent Implementation**: Implement ROS 2-specific logic in subagents
5. **Testing**: Test AI blocks with real Chapter 2 content

---

## Summary

This quickstart enables AI-interactive blocks in Chapter 2 by:
- ✅ Reusing existing components and infrastructure
- ✅ Adding Chapter 2-specific context (chapterId=2, section IDs, concepts)
- ✅ Creating placeholder scaffolding for future implementation
- ✅ Maintaining consistency with Chapter 1 patterns

**Estimated Total Time**: 1-2 hours (scaffolding only)
