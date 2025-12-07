# Quickstart Guide: Implementing Chapter 2 AI Blocks Integration Layer

**Feature**: 034-chapter-2-ai-blocks
**Branch**: `034-chapter-2-ai-blocks`
**Estimated Time**: 1-2 hours (scaffolding only, no business logic)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 001 (Base Project Initialization) completed
- [x] Feature 033 (Chapter 2 Content) completed
- [x] Feature 005 (AI Runtime Engine) completed
- [x] Backend structure exists at `backend/app/`
- [x] Git branch `034-chapter-2-ai-blocks` checked out
- [x] Read `specs/034-chapter-2-ai-blocks/spec.md`
- [x] Read `specs/034-chapter-2-ai-blocks/plan.md`
- [x] Read `specs/034-chapter-2-ai-blocks/contracts/ai-block-runtime.yaml`

## Implementation Overview

**Total Steps**: 6 phases
**Primary Deliverable**: Complete Chapter 2 AI runtime integration scaffolding
**Validation**: All files exist, imports resolve, backend starts without errors

---

## Phase 1: API Endpoint Routing (30 minutes)

### Step 1.1: Update ai_blocks.py

**Location**: `backend/app/api/ai_blocks.py`

**Action**: Add 4 new endpoints:
- `POST /ai/ch2/ask`
- `POST /ai/ch2/explain`
- `POST /ai/ch2/quiz`
- `POST /ai/ch2/diagram`

Each endpoint should:
- Use existing request models
- Call `run_ai_block(block_type, request_data)` where `request_data` includes `chapterId=2`
- Return placeholder response

---

## Phase 2: Runtime Engine Extensions (30 minutes)

### Step 2.1: Update engine.py

**Location**: `backend/app/ai/runtime/engine.py`

**Action**: Add Chapter 2 routing:
- Add `chapter_id=2` handling path
- Add placeholder routing comments for all 4 block types
- No business logic—flow comments only

---

## Phase 3: Subagent Stubs (30 minutes)

### Step 3.1: Create Subagent Files

**Location**: `backend/app/ai/subagents/`

**Action**: Create 4 files:
- `ch2_ask_agent.py`
- `ch2_explain_agent.py`
- `ch2_quiz_agent.py`
- `ch2_diagram_agent.py`

Each file should:
- Have class structure: `class <AgentName>: def run(self, input): ...`
- Include TODO comments
- Return placeholder values

---

## Phase 4: Skills Layer Hooks (15 minutes)

### Step 4.1: Update prompt_builder_skill.py

**Action**: Add TODO functions for Chapter 2 prompt construction

### Step 4.2: Update formatting_skill.py

**Action**: Add TODO placeholders for Chapter 2 formatting

---

## Phase 5: RAG Pipeline Routing (15 minutes)

### Step 5.1: Update pipeline.py

**Location**: `backend/app/ai/rag/pipeline.py`

**Action**: Add routing for chapter_2:
- `if chapter_id == 2: load chapter_2_chunks`
- Add comments about retrieval steps
- No business logic

---

## Phase 6: Validation (15 minutes)

### Step 6.1: Verify Imports

**Action**: Test that all imports resolve:
```bash
cd backend && python -c "from app.api.ai_blocks import router; print('OK')"
```

### Step 6.2: Verify Backend Starts

**Action**: Start backend and verify no errors:
```bash
cd backend && python -m uvicorn app.main:app --reload
```

---

## Success Criteria

- ✅ All 4 API endpoints exist and route correctly
- ✅ Runtime engine handles chapter_id=2 paths
- ✅ All 4 subagent files exist with class structure
- ✅ Skills files updated with Chapter 2 TODOs
- ✅ RAG pipeline has Chapter 2 routing comments
- ✅ Backend starts without errors
- ✅ All imports resolve successfully

---

## Troubleshooting

### Import Errors
- Verify all file paths are correct
- Check Python path configuration
- Ensure all parent directories have `__init__.py` files

### Backend Startup Errors
- Check for syntax errors in new files
- Verify all imports are correct
- Check for missing dependencies

---

## Notes

- This is scaffolding only—no business logic
- All functions return placeholder values
- All logic is marked with TODO comments
- Follow existing patterns from Chapter 1 and Chapter 3

