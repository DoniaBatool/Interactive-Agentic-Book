# Quickstart Guide: Chapter 1 Core Implementation

**Feature**: 002-chapter-1-core
**Date**: 2025-12-05
**Estimated Time**: 1-2 hours
**Prerequisites**: Feature 001 (Base Project Initialization) complete

## Overview

This guide provides step-by-step instructions for implementing Feature 002 (Chapter 1 Core Infrastructure). The implementation is divided into 4 phases following the tasks.md structure.

---

## Phase 0: Prerequisites Check

**Time**: 5 minutes

### Step 1: Verify Base Project Setup

```bash
# Check if Feature 001 is complete
ls -la backend/app/api/health.py
ls -la frontend/docusaurus.config.ts

# Verify backend runs
cd backend
uvicorn app.main:app --reload

# Verify frontend runs
cd frontend
npm start
```

**Expected**:
- Backend starts at `http://localhost:8000`
- Frontend starts at `http://localhost:3000`
- Health endpoint returns: `{"status": "ok"}`

---

## Phase 1: Setup Infrastructure

**Time**: 20-30 minutes

### Step 2: Create Folder Structure

```bash
# Navigate to project root
cd /path/to/interactive-agentic-book

# Create chapter directories
mkdir -p chapters/01-introduction
mkdir -p content/01-introduction/raw
mkdir -p content/01-introduction/processed

# Create .gitkeep files
echo "# Chapter 1 directory" > chapters/01-introduction/.gitkeep
echo "# Raw content for Chapter 1" > content/01-introduction/raw/.gitkeep
echo "# Processed content for Chapter 1" > content/01-introduction/processed/.gitkeep

# Verify structure
tree chapters/ content/
```

**Success Criteria**: 3 directories created with .gitkeep files

---

### Step 3: Create Pydantic Model

**File**: `backend/app/models/chapter.py`

```python
"""
Pydantic models for chapter metadata.
"""

from typing import List
from pydantic import BaseModel, Field


class ChapterMetadata(BaseModel):
    """
    Metadata for a single chapter in the textbook.
    """

    chapter: int = Field(
        ...,
        description="Chapter number (e.g., 1, 2, 3)",
        ge=1,
        example=1
    )

    title: str = Field(
        ...,
        description="Full chapter title",
        min_length=10,
        max_length=200,
        example="Introduction to Physical AI & Robotics"
    )

    summary: str = Field(
        ...,
        description="Brief summary of chapter content",
        min_length=50,
        max_length=1000,
        example="Placeholder summary for Chapter 1 introduction"
    )

    sections: List[str] = Field(
        default_factory=list,
        description="List of section titles within the chapter",
        example=[]
    )

    class Config:
        schema_extra = {
            "example": {
                "chapter": 1,
                "title": "Introduction to Physical AI & Robotics",
                "summary": "Placeholder summary for Chapter 1 introduction",
                "sections": []
            }
        }
```

**Test**:
```bash
cd backend
python -c "from app.models.chapter import ChapterMetadata; print('Model imported successfully')"
```

---

### Step 4: Create Service Layer

**File**: `backend/app/services/chapter_service.py`

See full implementation in `specs/002-chapter-1-core/contracts/api-schema.md`

**Key Components**:
- `ChapterService` class with `get_chapter()` method
- Placeholder data for Chapter 1
- 6 TODO sections for future RAG integration

**Test**:
```bash
cd backend
python -c "from app.services.chapter_service import ChapterService; s = ChapterService(); print(s.get_chapter(1))"
```

**Expected Output**:
```
chapter=1 title='Introduction to Physical AI & Robotics' summary='Placeholder summary for Chapter 1 introduction' sections=[]
```

---

### Step 5: Create RAG Placeholder Files

**Files**:
- `backend/app/agents/placeholder_chapter_agent.py` (200+ lines with 4 agent types)
- `backend/app/skills/placeholder_chapter_skill.py` (250+ lines with 7 skill types)

**Content Guidelines**:
- Each agent type: purpose, capabilities, integration points, example API
- Each skill type: purpose, capabilities, implementation example
- All TODOs > 20 words (aim for 50-100 words each)

**Verification**:
```bash
# Check TODO comment length
grep -A 5 "TODO" backend/app/agents/placeholder_chapter_agent.py | wc -l
grep -A 5 "TODO" backend/app/skills/placeholder_chapter_skill.py | wc -l
```

---

### Step 6: Create Test Scaffolding

**File**: `backend/tests/api/test_chapters.py`

```python
"""
Tests for the chapters API endpoints.
"""

import pytest

# TODO: Import TestClient from fastapi.testclient
# TODO: Import app from app.main

@pytest.fixture
def client():
    """TODO: Create FastAPI test client fixture."""
    pass

def test_get_chapter_success():
    """
    Test successful retrieval of chapter 1 metadata.

    TODO: Implement assertions for:
    - HTTP 200 status code
    - Correct JSON structure
    - Proper field values
    """
    pass

def test_get_chapter_not_found():
    """
    Test 404 response for non-existent chapter.

    TODO: Implement assertions for:
    - HTTP 404 status code
    - Error message in response
    """
    pass

# TODO: Add test_chapter_schema_validation
# TODO: Add parametrized tests for edge cases
```

**Verification**:
```bash
cd backend
pytest tests/api/test_chapters.py --collect-only
```

**Expected**: Tests collected (but skipped due to `pass` statements)

---

## Phase 2: Frontend Implementation

**Time**: 15-20 minutes

### Step 7: Create Chapter Overview Page

**File**: `frontend/docs/chapter-1/overview.md`

```markdown
---
sidebar_position: 1
sidebar_label: "Chapter 1 Overview"
---

# Chapter 1: Introduction to Physical AI & Robotics

## Overview

This chapter introduces the fundamental concepts of Physical AI and Robotics. You'll learn how artificial intelligence enables robots to perceive, understand, and interact with the physical world.

## Summary

Placeholder summary for Chapter 1 introduction. This chapter will cover the basics of Physical AI, robot components, and how AI integration creates intelligent physical systems.

## Sections

<!-- Sections will be populated as content is developed -->

The following sections will be covered in this chapter:
- What is Physical AI?
- Robot Components and Architecture
- AI Integration in Robotic Systems
- Real-world Applications

---

**Status**: Scaffolding complete. Educational content will be added in future iterations.
```

**Test**:
```bash
cd frontend
npm start
# Navigate to http://localhost:3000/docs/chapter-1/overview
```

**Expected**: Page renders with title and placeholder content

---

### Step 8: Update Sidebar Configuration

**File**: `frontend/sidebars.ts`

```typescript
const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Chapter 1',
      collapsible: true,
      collapsed: false,
      items: ['chapter-1/overview'],
    },
    {
      type: 'category',
      label: 'Chapters',
      collapsible: true,
      collapsed: false,
      items: [
        {
          type: 'autogenerated',
          dirName: 'chapters',
        },
      ],
    },
    {
      type: 'autogenerated',
      dirName: '.',
    },
  ],
};
```

**Test**:
```bash
cd frontend
npm run build
```

**Expected**: Build succeeds without errors

---

## Phase 3: Backend API Implementation

**Time**: 20-30 minutes

### Step 9: Create FastAPI Router

**File**: `backend/app/api/chapters.py`

```python
"""
FastAPI router for chapter metadata endpoints.
"""

from fastapi import APIRouter, HTTPException, status
from app.models.chapter import ChapterMetadata
from app.services.chapter_service import ChapterService

router = APIRouter(
    prefix="/chapters",
    tags=["chapters"],
    responses={
        404: {"description": "Chapter not found"},
    },
)

chapter_service = ChapterService()


@router.get(
    "/{chapter_id}",
    response_model=ChapterMetadata,
    summary="Get chapter metadata",
)
async def get_chapter(chapter_id: int):
    """Get metadata for a specific chapter."""
    chapter = chapter_service.get_chapter(chapter_id)

    if chapter is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chapter not found"
        )

    return chapter


@router.get(
    "/",
    response_model=list[ChapterMetadata],
    summary="List all chapters",
)
async def list_chapters():
    """Get a list of all available chapters."""
    return chapter_service.list_chapters()
```

**Test**:
```bash
cd backend
python -c "from app.api.chapters import router; print('Router imported successfully')"
```

---

### Step 10: Register Router in Main App

**File**: `backend/app/main.py`

Add import:
```python
from app.api.chapters import router as chapters_router
```

Register router:
```python
app.include_router(chapters_router, tags=["chapters"])
```

**Test**:
```bash
cd backend
uvicorn app.main:app --reload
```

**Verify**:
1. Visit `http://localhost:8000/docs`
2. See `/chapters/{chapter_id}` and `/chapters/` endpoints
3. Test `GET /chapters/1` → HTTP 200 with JSON
4. Test `GET /chapters/999` → HTTP 404

---

## Phase 4: Validation & Polish

**Time**: 10-15 minutes

### Step 11: Verify TODO Comments

```bash
# Count TODO comments in agent file
grep -c "TODO" backend/app/agents/placeholder_chapter_agent.py

# Count TODO comments in skill file
grep -c "TODO" backend/app/skills/placeholder_chapter_skill.py

# Verify each TODO > 20 words
grep -A 10 "TODO" backend/app/agents/placeholder_chapter_agent.py | less
```

**Success Criteria**:
- Agent file: 4+ TODO sections, each >50 words
- Skill file: 7+ TODO sections, each >50 words

---

### Step 12: Run Git Status Check

```bash
git status --short
```

**Expected Output**:
```
?? backend/app/api/chapters.py
?? backend/app/models/chapter.py
?? backend/app/services/chapter_service.py
?? backend/app/agents/placeholder_chapter_agent.py
?? backend/app/skills/placeholder_chapter_skill.py
?? backend/tests/api/test_chapters.py
?? chapters/
?? content/
?? frontend/docs/chapter-1/
M  frontend/sidebars.ts
M  backend/app/main.py
```

All files shown as untracked (??) or modified (M) - ready for commit!

---

### Step 13: Manual Testing

**Backend Tests**:
```bash
# Test Chapter 1 retrieval
curl http://localhost:8000/chapters/1

# Test 404 handling
curl http://localhost:8000/chapters/999

# Test list all chapters
curl http://localhost:8000/chapters/
```

**Frontend Tests**:
```bash
# Start dev server
cd frontend
npm start

# Navigate to:
http://localhost:3000/docs/chapter-1/overview

# Verify:
- Page renders with title
- Sidebar shows "Chapter 1"
- Placeholder content visible
```

---

## Phase 5: Documentation

**Time**: 5-10 minutes

### Step 14: Update tasks.md

Mark all tasks as complete:
```markdown
- [X] T001 Create `/chapters/01-introduction/` directory
- [X] T002 Create `/content/01-introduction/raw/` with .gitkeep
...
- [X] T020 Run git status to verify all files tracked
```

---

### Step 15: Create PHR

Use the PHR template to document implementation:

**File**: `history/prompts/002-chapter-1-core/0001-chapter-1-core-implementation.green.prompt.md`

Include:
- ID, title, stage, date
- All files created
- All tests passed
- Outcome summary
- Next steps

---

## Troubleshooting

### Issue: Import errors in backend

**Symptom**: `ModuleNotFoundError: No module named 'app'`

**Solution**:
```bash
cd backend
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python -c "from app.models.chapter import ChapterMetadata"
```

---

### Issue: Docusaurus build fails

**Symptom**: `Error: Docs markdown file not found`

**Solution**:
- Verify file path: `frontend/docs/chapter-1/overview.md`
- Check frontmatter is valid YAML
- Ensure sidebar reference matches file location

---

### Issue: FastAPI router not appearing in /docs

**Symptom**: `/chapters` endpoints not in Swagger UI

**Solution**:
- Verify router imported in `main.py`
- Verify `app.include_router(chapters_router)` called
- Restart uvicorn server
- Clear browser cache and refresh `/docs`

---

## Summary Checklist

- [X] Phase 0: Prerequisites verified (5 min)
- [X] Phase 1: Infrastructure setup (20-30 min)
  - [X] Folders created with .gitkeep files
  - [X] Pydantic model created
  - [X] Service layer created
  - [X] RAG placeholders created (400+ lines total)
  - [X] Test scaffolding created
- [X] Phase 2: Frontend (15-20 min)
  - [X] Overview page created
  - [X] Sidebar updated
- [X] Phase 3: Backend API (20-30 min)
  - [X] Router created with 2 endpoints
  - [X] Router registered in main.py
  - [X] Manual tests passed
- [X] Phase 4: Validation (10-15 min)
  - [X] TODO comments verified
  - [X] Git status checked
  - [X] Manual testing complete
- [X] Phase 5: Documentation (5-10 min)
  - [X] tasks.md updated
  - [X] PHR created

**Total Time**: 1-2 hours ✓

---

**Next Steps**:
1. Commit changes: `git add .` and `git commit -m "feat: implement Chapter 1 core infrastructure"`
2. Create PR: `/sp.git.commit_pr`
3. Begin Feature 003 (Chapter 1 Content) to add educational material
