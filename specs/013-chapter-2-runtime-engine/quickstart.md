# Quickstart: Chapter 2 — AI Runtime Engine Integration

**Feature**: 013-chapter-2-runtime-engine
**Feature ID**: 013-chapter-2-runtime-engine
**Created**: 2025-12-05

## Prerequisites

- Feature 005 (AI Runtime Engine) completed - provides runtime engine, subagents, skills, ChatKit scaffolding
- Feature 011 (Chapter 2 AI Blocks) completed - provides Chapter 2 AI blocks integration
- Feature 012 (Chapter 2 RAG) completed - provides Chapter 2 RAG foundations
- Backend Python environment set up
- `.env.example` file exists

## Commands

```
/sp.specify  # ✅ COMPLETED - Specification created
/sp.plan     # Next: Create architecture plan
/sp.tasks    # After plan: Generate implementation tasks
/sp.implement # After tasks: Implement scaffolding
```

## Folder Structure

```
specs/013-chapter-2-runtime-engine/
├── spec.md                    # ✅ Feature specification
├── plan.md                    # TODO: Architecture plan
├── tasks.md                   # TODO: Implementation tasks
├── research.md                # ✅ Runtime engine integration research
├── data-model.md              # ✅ Data structures and entities
├── quickstart.md              # ✅ This file
├── contracts/
│   ├── runtime-flow.yaml      # ✅ Runtime flow contract
│   └── chapter-2-blocks.yaml  # ✅ Chapter 2 blocks contract
└── checklists/
    └── requirements.md        # ✅ Specification quality checklist
```

## Feature Overview

This feature activates the full runtime pathway for Chapter 2 by creating scaffolding for:
1. **Runtime Engine Expansion**: Add chapter_id=2 routing, placeholder LLM invocation, RAG-context consumption
2. **RAG Pipeline Binding**: Ensure pipeline resolves chapter_2_chunks, add placeholder flow comments
3. **AI Block API Binding**: Verify all block types route to run_ai_block with chapterId=2
4. **Subagents for Chapter 2**: Create 4 Chapter 2-specific subagent files (ch2_*)
5. **Reusable Skills Integration**: Add Chapter 2 TODOs to skills files
6. **ChatKit Integration Scaffold**: Add multi-chapter session contexts and Chapter 2 tool definitions
7. **Config Updates**: Add Chapter 2 runtime settings (DEFAULT_CH2_MODEL, DEFAULT_CH2_EMBEDDINGS, ENABLE_CHAPTER_2_RUNTIME)

## Key Files to Modify

### Backend Files

1. **`backend/app/ai/runtime/engine.py`**
   - Add chapter_id=2 routing logic with placeholder comments
   - Add placeholder LLM invocation for Chapter 2
   - Add placeholder RAG-context consumption comments

2. **`backend/app/ai/rag/pipeline.py`**
   - Ensure pipeline resolves chapter_2_chunks when chapter_id=2
   - Add placeholder flow comments for Chapter 2

3. **`backend/app/api/ai_blocks.py`**
   - Verify all block types route to run_ai_block with chapterId=2
   - Add comments indicating Chapter 2 support

4. **`backend/app/ai/subagents/ch2_ask_question_agent.py`** (NEW)
   - Create Chapter 2 question-answering agent blueprint
   - Input/output signatures, TODO placeholders

5. **`backend/app/ai/subagents/ch2_explain_el10_agent.py`** (NEW)
   - Create Chapter 2 explanation agent blueprint
   - Input/output signatures, TODO placeholders

6. **`backend/app/ai/subagents/ch2_quiz_agent.py`** (NEW)
   - Create Chapter 2 quiz agent blueprint
   - Input/output signatures, TODO placeholders

7. **`backend/app/ai/subagents/ch2_diagram_agent.py`** (NEW)
   - Create Chapter 2 diagram agent blueprint
   - Input/output signatures, TODO placeholders

8. **`backend/app/ai/skills/retrieval_skill.py`**
   - Add TODO: chapter-aware retrieval for Chapter 2

9. **`backend/app/ai/skills/prompt_builder_skill.py`**
   - Add TODO: chapter-aware prompt builder for Chapter 2

10. **`backend/app/ai/skills/formatting_skill.py`**
    - Add TODO: formatting rules for Chapter 2

11. **`backend/app/ai/chatkit/session_manager.py`**
    - Add placeholder for multi-chapter session contexts
    - Add TODO comments for Chapter 2 session handling

12. **`backend/app/ai/chatkit/tools.py`**
    - Add tool definitions for Chapter 2 blocks
    - Document Chapter 2 tool schemas

13. **`backend/app/config/settings.py`**
    - Add DEFAULT_CH2_MODEL, DEFAULT_CH2_EMBEDDINGS, ENABLE_CHAPTER_2_RUNTIME settings

14. **`.env.example`**
    - Add 3 new environment variables with descriptions

## Implementation Strategy

### Phase 1: Specification ✅
- Create spec.md with requirements
- Create contracts (runtime-flow.yaml, chapter-2-blocks.yaml)
- Create research.md, data-model.md, checklists, quickstart.md

### Phase 2: Planning (Next)
- Create plan.md with architecture decisions
- Define routing strategy
- Define subagent architecture
- Define skills integration pattern
- Define ChatKit integration pattern

### Phase 3: Task Generation
- Create tasks.md with atomic tasks
- Group tasks by phase (runtime, RAG binding, API, subagents, skills, ChatKit, config)

### Phase 4: Implementation
- Update runtime engine with Chapter 2 routing
- Update RAG pipeline with Chapter 2 binding
- Verify API routing for Chapter 2
- Create 4 Chapter 2 subagent files
- Update skills with Chapter 2 TODOs
- Update ChatKit with Chapter 2 scaffolding
- Update settings.py and .env.example

## Validation Steps

After implementation:

1. **Backend Import Validation**:
   ```bash
   cd backend
   python -c "from app.ai.runtime.engine import run_ai_block; print('SUCCESS')"
   python -c "from app.ai.subagents.ch2_ask_question_agent import ch2_ask_question_agent; print('SUCCESS')"
   python -c "from app.ai.subagents.ch2_explain_el10_agent import ch2_explain_el10_agent; print('SUCCESS')"
   python -c "from app.ai.subagents.ch2_quiz_agent import ch2_quiz_agent; print('SUCCESS')"
   python -c "from app.ai.subagents.ch2_diagram_agent import ch2_diagram_agent; print('SUCCESS')"
   ```

2. **Backend Startup Validation**:
   ```bash
   cd backend
   python -m uvicorn app.main:app --reload
   # Should start without import errors
   ```

3. **Environment Variables Validation**:
   ```bash
   # Check .env.example has new variables
   grep DEFAULT_CH2_MODEL .env.example
   grep DEFAULT_CH2_EMBEDDINGS .env.example
   grep ENABLE_CHAPTER_2_RUNTIME .env.example
   ```

4. **File Existence Validation**:
   ```bash
   # Check all files exist
   ls backend/app/ai/subagents/ch2_*.py
   ls backend/app/ai/runtime/engine.py
   ls backend/app/ai/rag/pipeline.py
   ls backend/app/api/ai_blocks.py
   ```

## Success Criteria

- ✅ Runtime engine can route chapter 2 requests
- ✅ All subagents + skills scaffolding exists
- ✅ ChatKit placeholder integration exists
- ✅ No real AI logic or real RAG logic implemented
- ✅ Backend starts without errors

## Next Steps

1. Run `/sp.plan` to create architecture plan
2. Review plan.md for routing strategy, subagent architecture, skills integration
3. Run `/sp.tasks` to generate implementation tasks
4. Run `/sp.implement` to implement scaffolding

## Notes

- This is a **scaffolding-only** feature. No real AI logic will be implemented.
- All functions return placeholders (empty lists, empty dicts, False, etc.)
- TODO comments explain future implementation requirements.
- Real runtime implementation will be added in future features.
- Chapter 2 subagents follow naming pattern (ch2_*) for clarity.
