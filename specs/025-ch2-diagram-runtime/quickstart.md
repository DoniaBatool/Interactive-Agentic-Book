# Quickstart: Chapter 2 Diagram Generator Runtime

**Feature**: 025-ch2-diagram-runtime
**Date**: 2025-01-27
**Purpose**: Step-by-step implementation guide for Chapter 2 diagram runtime scaffolding

## Overview

This quickstart guide provides step-by-step instructions for creating Chapter 2 diagram generator runtime scaffolding. The implementation involves:

1. Creating diagram runtime module (ch2_diagram_runtime.py)
2. Creating prompt template file (ch2_diagram_prompt.txt)
3. Updating runtime engine routing
4. Updating API layer
5. Extending skills layer
6. Validating backend startup

**Estimated Time**: 30-45 minutes (scaffolding only, no real AI logic)

---

## Prerequisites

- ✅ Feature 008 (Chapter 1 Diagram Engine) - Reference structure exists
- ✅ Feature 024 (Chapter 2 Backend Runtime Wiring) - Runtime engine routing exists
- ✅ Skills layer exists
- ✅ FastAPI backend setup
- ✅ Git branch `025-ch2-diagram-runtime` checked out

---

## Phase 1: Diagram Runtime Module (10 minutes)

### Step 1.1: Create Chapter 2 Diagram Runtime

**File**: `backend/app/ai/diagram/ch2_diagram_runtime.py`

**Action**: Create file with blueprint for diagram generation flow

**Template**:
```python
"""
Chapter 2 Diagram Generator Runtime

Orchestrates the complete diagram generation flow for ROS 2 diagrams:
1. Validate diagram request
2. Build prompt (placeholder)
3. Call RAG (placeholder)
4. Call provider LLM (placeholder)
5. Format response (placeholder)
"""

from typing import List, Dict, Any


async def run(
    diagram_type: str,
    chapter_id: int,
    concepts: List[str]
) -> Dict[str, Any]:
    """
    Blueprint for Chapter 2 diagram generation flow.
    
    Args:
        diagram_type: Type of diagram to generate (e.g., "ros2-ecosystem-overview")
        chapter_id: Chapter identifier (should be 2)
        concepts: List of ROS 2 concepts to include
    
    Returns:
        Dictionary with structured diagram:
        {
            "nodes": List[Dict],      # Diagram nodes (placeholder)
            "edges": List[Dict],       # Diagram edges (placeholder)
            "svg": str,                # SVG string (placeholder)
            "metadata": Dict[str, Any] # Additional metadata
        }
    
    Steps (all TODO):
    1. Validate diagram request
    2. Build prompt (placeholder)
    3. Call RAG (placeholder)
    4. Call provider LLM (placeholder)
    5. Format response (placeholder)
    """
    # Step 1: Validate diagram request (TODO)
    # TODO: Check diagram_type is supported for Chapter 2
    # TODO: Validate chapter_id is 2
    # TODO: Validate concepts list
    
    # Step 2: Build prompt (placeholder)
    # TODO: Load ch2_diagram_prompt.txt template
    # TODO: Replace template variables ({{diagram_type}}, {{chapter_id}}, {{concepts}})
    # TODO: Call build_diagram_prompt_ch2() from prompt_builder_skill
    
    # Step 3: Call RAG (placeholder)
    # TODO: Retrieve Chapter 2 context chunks for diagram
    # TODO: Use RAG pipeline to get relevant ROS 2 content
    
    # Step 4: Call provider LLM (placeholder)
    # TODO: Call LLM provider with prompt and context
    # TODO: Generate diagram structure using LLM reasoning
    
    # Step 5: Format response (placeholder)
    # TODO: Call format_diagram_output_ch2() from formatting_skill
    # TODO: Format nodes, edges, SVG structure
    
    # Placeholder return - no real diagram generation
    return {
        "nodes": [],
        "edges": [],
        "svg": "",
        "metadata": {}
    }
```

**Validation**: File should be importable: `from app.ai.diagram.ch2_diagram_runtime import run`

---

## Phase 2: Prompt Template (5 minutes)

### Step 2.1: Create Prompt Template Directory

**Directory**: `backend/app/ai/prompts/diagram/`

**Action**: Create directory if it doesn't exist

---

### Step 2.2: Create Chapter 2 Prompt Template

**File**: `backend/app/ai/prompts/diagram/ch2_diagram_prompt.txt`

**Action**: Create file with placeholder template

**Template**:
```
TODO: Engineer full prompt template for Chapter 2 diagrams

Template variables:
- {{diagram_type}} - Type of diagram (e.g., "ros2-ecosystem-overview", "node-communication-architecture")
- {{chapter_id}} - Chapter identifier (should be 2)
- {{concepts}} - ROS 2 concepts to include (nodes, topics, services, actions, packages, launch-files)

TODO: Add system instructions for ROS 2 diagram generation
TODO: Add context placeholders for RAG chunks
TODO: Add structured output format instructions
TODO: Add ROS 2-specific diagram guidelines
TODO: Include ROS 2 analogies and examples
TODO: Add diagram type-specific instructions
```

**Validation**: File should exist and be readable

---

## Phase 3: Runtime Engine Routing (5 minutes)

### Step 3.1: Update Runtime Engine

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Add Chapter 2 diagram routing case

**Location**: In `run_ai_block()` function, before existing diagram routing

**Template**:
```python
# TODO: Chapter 2 diagram routing
# if block_type == "diagram" AND chapterId == 2:
#     from app.ai.diagram.ch2_diagram_runtime import run as ch2_diagram_run
#     result = await ch2_diagram_run(
#         diagram_type=request_data.get("diagramType", ""),
#         chapter_id=2,
#         concepts=request_data.get("concepts", [])
#     )
#     return result
```

**Validation**: File should still import correctly

---

## Phase 4: API Layer Update (5 minutes)

### Step 4.1: Update Diagram Endpoint

**File**: `backend/app/api/ai_blocks.py`

**Action**: Add Chapter 2 routing comment to diagram endpoint

**Location**: In `diagram()` function, before routing to diagram runtime

**Template**:
```python
# TODO: Chapter 2 diagram routing
# if request.chapterId == 2:
#     from app.ai.diagram.ch2_diagram_runtime import run as ch2_diagram_run
#     result = await ch2_diagram_run(
#         diagram_type=request.diagramType,
#         chapter_id=2,
#         concepts=request.concepts or []
#     )
#     return result
```

**Validation**: File should still import correctly

---

## Phase 5: Skills Extension (10 minutes)

### Step 5.1: Update Prompt Builder Skill

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Action**: Add build_diagram_prompt_ch2() placeholder function

**Template**:
```python
def build_diagram_prompt_ch2(
    diagram_type: str,
    chapter_id: int,
    concepts: List[str]
) -> str:
    """
    Build diagram prompt for Chapter 2.
    
    Args:
        diagram_type: Type of diagram to generate
        chapter_id: Chapter identifier (should be 2)
        concepts: List of ROS 2 concepts to include
    
    Returns:
        Constructed prompt string
    
    TODO: Implement prompt building for Chapter 2 diagrams
    TODO: Load ch2_diagram_prompt.txt template
    TODO: Replace template variables ({{diagram_type}}, {{chapter_id}}, {{concepts}})
    TODO: Add ROS 2-specific context
    TODO: Return constructed prompt string
    """
    # Placeholder return - no real prompt building
    return ""
```

---

### Step 5.2: Update Formatting Skill

**File**: `backend/app/ai/skills/formatting_skill.py`

**Action**: Add format_diagram_output_ch2() placeholder function

**Template**:
```python
def format_diagram_output_ch2(
    raw_response: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Format diagram output for Chapter 2.
    
    Args:
        raw_response: Raw LLM response with diagram data
    
    Returns:
        Formatted diagram structure:
        {
            "nodes": List[Dict],
            "edges": List[Dict],
            "svg": str,
            "metadata": Dict[str, Any]
        }
    
    TODO: Implement formatting for Chapter 2 diagram output
    TODO: Parse raw LLM response
    TODO: Extract nodes, edges, SVG
    TODO: Format ROS 2-specific metadata
    TODO: Return formatted diagram structure
    """
    # Placeholder return - no real formatting
    return {
        "nodes": [],
        "edges": [],
        "svg": "",
        "metadata": {}
    }
```

**Validation**: Files should still import correctly

---

## Phase 6: Validation (5 minutes)

### Step 6.1: Test Backend Startup

**Command**: `cd backend && uvicorn app.main:app`

**Expected**: Backend starts without errors

**Validation Checklist**:
- [ ] No import errors
- [ ] All modules import correctly
- [ ] No syntax errors
- [ ] Backend starts successfully

---

### Step 6.2: Test Module Imports

**Command**: `cd backend && python -c "from app.ai.diagram.ch2_diagram_runtime import run; print('Import successful')"`

**Expected**: Import succeeds

**Validation**: All new modules should be importable

---

## Completion Checklist

- [ ] ch2_diagram_runtime.py created with 5-step blueprint
- [ ] ch2_diagram_prompt.txt created with template variables
- [ ] Runtime engine has Chapter 2 diagram routing (comments only)
- [ ] API layer has Chapter 2 diagram routing comments
- [ ] Skills have Chapter 2 diagram placeholder functions
- [ ] Contract file documents expected placeholders
- [ ] Backend starts without errors
- [ ] All modules import correctly

---

## Troubleshooting

### Issue: Import errors when starting backend

**Solution**: 
- Check all new files are syntactically correct
- Verify import paths are correct
- Check for circular imports

---

### Issue: Prompt template not found

**Solution**:
- Verify directory structure: `backend/app/ai/prompts/diagram/`
- Check file exists: `ch2_diagram_prompt.txt`
- Verify file is readable

---

## Next Steps

After completing this quickstart:

1. **Prompt Engineering**: Engineer full prompt template for ROS 2 diagrams
2. **Runtime Implementation**: Implement 5-step pipeline logic
3. **Skills Implementation**: Implement prompt building and formatting functions
4. **Testing**: Test Chapter 2 diagram generation

---

## Summary

This quickstart creates Chapter 2 diagram runtime scaffolding by:
- ✅ Creating diagram runtime module with 5-step blueprint
- ✅ Creating prompt template with ROS 2 variables
- ✅ Adding runtime engine routing (comments only)
- ✅ Adding API layer routing comments
- ✅ Extending skills with placeholder functions
- ✅ Validating backend startup

**Estimated Total Time**: 30-45 minutes (scaffolding only)

