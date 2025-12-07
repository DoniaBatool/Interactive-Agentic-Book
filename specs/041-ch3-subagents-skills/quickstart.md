# Quickstart Guide: Chapter 3 Subagents + Skills Integration

**Feature**: 041-ch3-subagents-skills
**Branch**: `041-ch3-subagents-skills`
**Estimated Time**: 45-60 minutes (scaffolding only, no real AI logic)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 001 (Base Project Initialization) completed
- [x] Feature 040 (Chapter 3 RAG + Runtime Integration) completed
- [x] Feature 024 (Chapter 2 Runtime Wiring) completed - Reference for patterns
- [x] Git branch `041-ch3-subagents-skills` checked out
- [x] Read `specs/041-ch3-subagents-skills/spec.md`
- [x] Read `specs/024-ch2-runtime-wiring/spec.md` (reference pattern)

## Implementation Overview

**Total Steps**: 6 phases
**Primary Deliverable**: Complete subagent + skills scaffolding for Chapter 3
**Validation**: Backend starts without errors, all imports resolve, no real AI calls

---

## Phase 1: Base Contracts (10 minutes)

### Step 1.1: Create base_agent.py

**File**: `backend/app/ai/subagents/base_agent.py`

**Action**: Create file with abstract base class:

```python
"""
Base Agent Interface

Abstract base class for all subagents.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAgent(ABC):
    """
    Base interface for all subagents.
    
    TODO: Future polymorphism support
    TODO: Add common methods shared by all subagents
    """
    
    @abstractmethod
    def run(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Abstract method for processing AI block requests.
        
        Args:
            request: Request payload with block-specific data
        
        Returns:
            Formatted response for frontend
        """
        pass
```

**Validation**: File exists, abstract class defined, imports resolve

---

### Step 1.2: Create base_skill.py

**File**: `backend/app/ai/skills/base_skill.py`

**Action**: Create file with basic placeholder interface:

```python
"""
Base Skill Interface

Basic placeholder interface for all skills.
"""

from abc import ABC


class BaseSkill(ABC):
    """
    Base interface for all skills.
    
    TODO: Future polymorphism support
    TODO: Add common methods shared by all skills
    """
    pass
```

**Validation**: File exists, abstract class defined, imports resolve

---

## Phase 2: Subagents Folder (15 minutes)

### Step 2.1: Create ch3/ folder

**Action**: Create `backend/app/ai/subagents/ch3/` folder

### Step 2.2: Create ask_question_agent.py

**File**: `backend/app/ai/subagents/ch3/ask_question_agent.py`

**Action**: Create file with class stub:

```python
"""
Chapter 3 Ask Question Agent

Specialized agent for answering questions about Physical AI concepts.
"""

from typing import Dict, Any
from app.ai.subagents.base_agent import BaseAgent


class Ch3AskQuestionAgent(BaseAgent):
    """
    Chapter 3 Ask Question Agent
    
    Processes questions about Physical AI using Chapter 3 RAG context.
    """
    
    def run(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        TODO: Implement Physical AI question-answering logic
        TODO: Step 1: Use retrieval_skill to get additional context
        TODO: Step 2: Use prompt_builder_skill to construct prompt
        TODO: Step 3: Call LLM provider with prompt + context
        TODO: Step 4: Use formatting_skill to format response
        TODO: Step 5: Return formatted answer
        """
        return {
            "answer": "",
            "sources": [],
            "confidence": 0.0
        }
```

**Validation**: File exists, class defined, imports resolve

---

### Step 2.3: Create explain_el10_agent.py

**File**: `backend/app/ai/subagents/ch3/explain_el10_agent.py`

**Action**: Create similar structure for explain agent

### Step 2.4: Create quiz_agent.py

**File**: `backend/app/ai/subagents/ch3/quiz_agent.py`

**Action**: Create similar structure for quiz agent

### Step 2.5: Create diagram_agent.py

**File**: `backend/app/ai/subagents/ch3/diagram_agent.py`

**Action**: Create similar structure for diagram agent

---

## Phase 3: Skills Folder (15 minutes)

### Step 3.1: Create ch3/ folder

**Action**: Create `backend/app/ai/skills/ch3/` folder

### Step 3.2: Create retrieval_skill.py

**File**: `backend/app/ai/skills/ch3/retrieval_skill.py`

**Action**: Create file with class stub:

```python
"""
Chapter 3 Retrieval Skill

Reusable skill for content retrieval from Chapter 3 content.
"""

from typing import List, Dict, Any
from app.ai.skills.base_skill import BaseSkill


class Ch3RetrievalSkill(BaseSkill):
    """
    Chapter 3 Retrieval Skill
    
    Provides RAG context pulling for Chapter 3.
    """
    
    def retrieve_content(self, query: str, chapter_id: int = 3, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        TODO: Implement content retrieval logic
        TODO: Call RAG pipeline with query and chapter_id=3
        TODO: Filter chunks by section_id if provided
        TODO: Return top-k most relevant chunks
        """
        return []
```

**Validation**: File exists, class defined, imports resolve

---

### Step 3.3: Create prompt_builder_skill.py

**File**: `backend/app/ai/skills/ch3/prompt_builder_skill.py`

**Action**: Create similar structure for prompt builder

### Step 3.4: Create formatting_skill.py

**File**: `backend/app/ai/skills/ch3/formatting_skill.py`

**Action**: Create similar structure for formatting

---

## Phase 4: Runtime Routing (10 minutes)

### Step 4.1: Update engine.py

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Add Chapter 3 routing branch:

```python
elif chapter_id == 3:
    # TODO: Route to Chapter 3 subagents
    # TODO: Import Ch3 subagents
    # from app.ai.subagents.ch3.ask_question_agent import Ch3AskQuestionAgent
    # from app.ai.subagents.ch3.explain_el10_agent import Ch3ExplainEl10Agent
    # from app.ai.subagents.ch3.quiz_agent import Ch3QuizAgent
    # from app.ai.subagents.ch3.diagram_agent import Ch3DiagramAgent
    
    # TODO: Map block_type to Ch3*Agent classes
    # CH3_SUBAGENT_MAP = {
    #     "ask-question": Ch3AskQuestionAgent(),
    #     "explain-like-10": Ch3ExplainEl10Agent(),
    #     "interactive-quiz": Ch3QuizAgent(),
    #     "generate-diagram": Ch3DiagramAgent()
    # }
    
    # TODO: Call subagent.run(request_data + context)
    pass
```

**Validation**: File updated, Chapter 3 routing added, no syntax errors

---

## Phase 5: API Verification (5 minutes)

### Step 5.1: Verify ai_blocks.py

**File**: `backend/app/api/ai_blocks.py`

**Action**: Verify chapterId=3 is properly passed (should already work via runtime engine)

**Validation**: Endpoints accept chapterId=3 parameter, routing handled by runtime engine

---

## Phase 6: Validation (10 minutes)

### Step 6.1: Backend Startup Test

**Action**: Run `uvicorn app.main:app --reload` in backend directory
**Expected**: Backend starts without errors

### Step 6.2: Import Test

**Action**: Test imports:
```python
from app.ai.subagents.ch3.ask_question_agent import Ch3AskQuestionAgent
from app.ai.skills.ch3.retrieval_skill import Ch3RetrievalSkill
```

**Expected**: All imports resolve successfully

---

## Success Criteria

- ✅ All subagent + skill scaffolding exists in correct paths
- ✅ Runtime engine successfully imports and routes to chapter 3 placeholder classes
- ✅ ai_blocks endpoints work with chapterId=3 without errors
- ✅ No AI logic implemented (strictly scaffolding)
- ✅ Backend server starts cleanly

---

## Troubleshooting

### Import Errors
- Verify ch3/ folders exist
- Check class names match imports
- Verify Python path includes backend directory

### Backend Startup Errors
- Check all imports resolve
- Verify base_agent.py and base_skill.py exist
- Check for syntax errors in new files

### Routing Errors
- Verify runtime engine has Chapter 3 routing
- Check request_data includes chapterId=3
- Verify subagent classes are importable

---

## Notes

- This is scaffolding only—no real subagent or skills logic implemented
- All classes return placeholder values
- TODO comments mark future implementation points
- Follows Chapter 2 subagents/skills patterns exactly
- Backend architecture ready for future AI logic

