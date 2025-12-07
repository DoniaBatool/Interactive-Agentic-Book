# Quickstart: Chapter 3 Diagram Generator Runtime Layer

**Feature**: 031-ch3-diagram-runtime
**Date**: 2025-01-27
**Purpose**: Step-by-step implementation guide for Chapter 3 diagram runtime scaffolding

## Overview

This quickstart guide provides step-by-step instructions for creating Chapter 3 diagram generator runtime scaffolding. The implementation involves:

1. Creating diagram runtime module (ch3_diagram_runtime.py)
2. Creating prompt template file (ch3_diagram_prompt.txt)
3. Updating runtime engine routing
4. Updating API layer
5. Extending skills layer
6. Adding RAG integration stub
7. Validating backend startup

**Estimated Time**: 30-45 minutes (scaffolding only, no real AI logic)

---

## Prerequisites

- ✅ Feature 025 (Chapter 2 Diagram Runtime) - Reference structure exists
- ✅ Feature 030 (Chapter 3 AI Runtime Engine Integration) - Subagent exists
- ✅ Skills layer exists
- ✅ FastAPI backend setup
- ✅ Git branch `031-ch3-diagram-runtime` checked out

---

## Phase 1: Diagram Runtime Module (10 minutes)

### Step 1.1: Create Chapter 3 Diagram Runtime

**File**: `backend/app/ai/diagram/ch3_diagram_runtime.py`

**Action**: Create file with blueprint for diagram generation flow

**Template**: Follow ch2_diagram_runtime.py structure with:
- Function signature: `async def run(diagram_type: str, chapter_id: int, concepts: List[str]) -> Dict[str, Any]`
- 5 steps (all TODO): Validate, Build prompt, Call RAG, Call provider LLM, Format response
- Placeholder return structure

---

## Phase 2: Prompt Template (5 minutes)

### Step 2.1: Create Chapter 3 Diagram Prompt Template

**File**: `backend/app/ai/prompts/diagram/ch3_diagram_prompt.txt`

**Action**: Create placeholder template with variables:
- `{{diagram_type}}`
- `{{chapter_id}}`
- `{{concepts}}`

**Template**: Include TODO comments for future prompt engineering

---

## Phase 3: Runtime Engine Routing (5 minutes)

### Step 3.1: Update Runtime Engine

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Add Chapter 3 diagram routing (comments only):
```python
# TODO: Chapter 3 diagram routing
# if block_type == "diagram" AND chapterId == 3:
#     from app.ai.diagram.ch3_diagram_runtime import run as ch3_diagram_run
#     result = await ch3_diagram_run(...)
```

---

## Phase 4: API Layer Update (5 minutes)

### Step 4.1: Update API Endpoint

**File**: `backend/app/api/ai_blocks.py`

**Action**: Update `/ai/ch3/diagram` endpoint to route to ch3_diagram_runtime:
- Route to `run_ai_block(block_type="diagram", chapter=3, payload=request)`
- Add TODO documentation tags

---

## Phase 5: Skills Extension (10 minutes)

### Step 5.1: Update Prompt Builder Skill

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Action**: Add `build_diagram_prompt_ch3()` placeholder function

### Step 5.2: Update Formatting Skill

**File**: `backend/app/ai/skills/formatting_skill.py`

**Action**: Add `format_diagram_output_ch3()` placeholder function

---

## Phase 6: RAG Integration Stub (5 minutes)

### Step 6.1: Update RAG Pipeline

**File**: `backend/app/ai/rag/ch3_pipeline.py`

**Action**: Add TODO for retrieve diagram-related context

---

## Phase 7: Validation (5 minutes)

### Step 7.1: Test Backend Startup

**Command**: `cd backend && python -c "from app.main import app; print('Backend imports OK')"`

**Expected**: No import errors

### Step 7.2: Test Module Imports

**Command**: `cd backend && python -c "from app.ai.diagram.ch3_diagram_runtime import run; print('Module imports OK')"`

**Expected**: No import errors

---

## Success Criteria

- ✅ All files created at correct paths
- ✅ Diagram endpoint routes to runtime engine
- ✅ Diagram runtime module exists with placeholders
- ✅ Skills extended with Chapter 3 TODOs
- ✅ Contract file created
- ✅ No logic implemented
- ✅ Backend starts without errors

---

## Next Steps

After completing this quickstart:
1. Proceed with `/sp.plan` for detailed architecture
2. Proceed with `/sp.tasks` for atomic task list
3. Proceed with `/sp.implement` for implementation

---

## Troubleshooting

### Import Errors
- Check file paths match exactly
- Verify Python syntax is correct
- Ensure all dependencies exist

### Backend Won't Start
- Check for syntax errors in new files
- Verify all imports resolve
- Check for circular import issues

---

## Notes

- All implementation is placeholder-only
- No real AI logic should be added
- Follow Feature 025 patterns exactly
- Subagent (ch3_diagram_agent) already exists from Feature 030

