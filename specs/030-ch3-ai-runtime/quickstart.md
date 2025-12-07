# Quickstart: Chapter 3 — AI Runtime Engine Integration

**Feature**: 030-ch3-ai-runtime
**Feature ID**: 030-ch3-ai-runtime
**Created**: 2025-01-27

## Prerequisites

- Feature 005 (AI Runtime Engine) completed - provides runtime engine, subagents, skills scaffolding
- Feature 017 or 020 (Chapter 2 AI Runtime) completed - provides pattern reference
- Feature 028 (Chapter 3 AI Blocks Integration) completed - provides Chapter 3 MDX and metadata
- Feature 029 (Chapter 3 RAG Prep) completed - provides ch3_pipeline.py
- Backend Python environment set up

## Commands

```
/sp.specify  # ✅ COMPLETED - Specification created
/sp.plan     # Next: Create architecture plan
/sp.tasks    # After plan: Generate implementation tasks
/sp.implement # After tasks: Implement scaffolding
```

## Folder Structure

```
specs/030-ch3-ai-runtime/
├── spec.md                    # ✅ Feature specification
├── plan.md                    # TODO: Architecture plan
├── tasks.md                   # TODO: Implementation tasks
├── research.md                # ✅ Runtime engine integration research
├── data-model.md              # ✅ Data structures and entities
├── quickstart.md              # ✅ This file
├── contracts/
│   └── ch3-ai-runtime.yaml   # ✅ AI runtime integration contract
└── checklists/
    └── requirements.md        # ✅ Specification quality checklist
```

## Feature Overview

This feature connects Chapter 3's AI Blocks to the global AI Runtime Engine by creating scaffolding for:
1. **API Endpoint Routing**: Add 4 new endpoints for Chapter 3 (`/ai/ch3/ask-question`, `/ai/ch3/explain-el10`, `/ai/ch3/quiz`, `/ai/ch3/diagram`)
2. **Runtime Engine Extensions**: Add Chapter 3 routing rules with placeholder flow
3. **Subagent Stubs**: Create 4 Chapter 3 subagent files with TODO blueprints
4. **Skill Extensions**: Add Chapter 3 TODOs to prompt_builder_skill and retrieval_skill
5. **Pipeline Connection**: Add placeholder call to engine pipeline in ch3_pipeline.py
6. **Contract File**: Document runtime flow, subagent responsibilities, placeholder schemas

## Key Files to Create/Modify

### New Files

1. **`backend/app/ai/subagents/ch3_ask_question_agent.py`** (NEW)
   - Create with placeholder function and TODO comments
   - Expected input/output signatures
   - Physical AI context documentation

2. **`backend/app/ai/subagents/ch3_explain_el10_agent.py`** (NEW)
   - Create with placeholder function and TODO comments
   - Expected input/output signatures
   - Physical AI context documentation

3. **`backend/app/ai/subagents/ch3_quiz_agent.py`** (NEW)
   - Create with placeholder function and TODO comments
   - Expected input/output signatures
   - Physical AI context documentation

4. **`backend/app/ai/subagents/ch3_diagram_agent.py`** (NEW)
   - Create with placeholder function and TODO comments
   - Expected input/output signatures
   - Physical AI context documentation

### Modified Files

5. **`backend/app/api/ai_blocks.py`**
   - Add 4 new endpoints for Chapter 3
   - Route to `run_ai_block(block_type, chapter=3, payload=...)`
   - Add request/response models if needed

6. **`backend/app/ai/runtime/engine.py`**
   - Add Chapter 3 routing rules (when chapterId=3)
   - Add placeholder flow for provider selection, RAG invocation, subagent selection, formatting
   - NO business logic (only placeholders and TODOs)

7. **`backend/app/ai/skills/prompt_builder_skill.py`**
   - Add TODO comments for building prompts for Chapter 3 blocks
   - Add placeholder functions if needed

8. **`backend/app/ai/skills/retrieval_skill.py`**
   - Add TODO comments for integrating Chapter 3 chunks
   - Add placeholder routing for chapterId=3

9. **`backend/app/ai/rag/ch3_pipeline.py`**
   - Add placeholder call to engine pipeline
   - Add TODO comments for runtime engine integration

## Implementation Steps

### Step 1: Create Subagent Files

1. Create `ch3_ask_question_agent.py` with placeholder function
2. Create `ch3_explain_el10_agent.py` with placeholder function
3. Create `ch3_quiz_agent.py` with placeholder function
4. Create `ch3_diagram_agent.py` with placeholder function

### Step 2: Add API Endpoints

1. Update `ai_blocks.py` with 4 new Chapter 3 endpoints
2. Route all endpoints to `run_ai_block()`
3. Add request/response models if needed

### Step 3: Extend Runtime Engine

1. Update `engine.py` with Chapter 3 routing rules
2. Add placeholder flow comments
3. Add TODO comments for provider selection, RAG invocation, subagent selection, formatting

### Step 4: Extend Skills

1. Update `prompt_builder_skill.py` with Chapter 3 TODOs
2. Update `retrieval_skill.py` with Chapter 3 TODOs

### Step 5: Connect Pipeline

1. Update `ch3_pipeline.py` with placeholder call to engine pipeline
2. Add TODO comments for runtime engine integration

### Step 6: Test Imports

1. Test all imports resolve without errors
2. Test backend starts successfully
3. Verify no circular dependencies

## Success Criteria

- ✅ All 4 Chapter 3 API endpoints exist and route correctly
- ✅ Runtime engine handles Chapter 3 stub routing
- ✅ All 4 Chapter 3 subagents created with correct signatures
- ✅ Skills extended with Chapter 3 TODOs
- ✅ Pipeline connection added to ch3_pipeline.py
- ✅ Contract file exists and documents structure
- ✅ No actual AI or RAG logic implemented
- ✅ Backend runs without errors
- ✅ All files created at exact paths

## Troubleshooting

### Issue: Import Errors

**Solution**: Check that all new modules have proper `__init__.py` files and correct import paths

### Issue: Backend Won't Start

**Solution**: Check that all new functions have placeholder returns and no syntax errors

### Issue: Missing Subagents

**Solution**: Create missing subagent files following the pattern from Chapter 2 subagents

### Issue: Routing Not Working

**Solution**: Verify runtime engine has Chapter 3 routing logic (even if placeholder)

## Next Steps

After completing this feature:
1. Run `/sp.plan` to create architecture plan
2. Run `/sp.tasks` to generate implementation tasks
3. Run `/sp.implement` to implement scaffolding

