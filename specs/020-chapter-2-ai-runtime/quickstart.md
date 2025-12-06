# Quickstart: AI Runtime Engine Extension for Chapter 2

**Feature**: 020-chapter-2-ai-runtime
**Feature ID**: 020-chapter-2-ai-runtime
**Created**: 2025-12-05

## Prerequisites

- Feature 005 (AI Runtime Engine) completed - provides runtime engine, subagents, skills, ChatKit scaffolding
- Feature 012 (Chapter 2 RAG) completed - provides Chapter 2 RAG foundations
- Feature 013 (Chapter 2 Runtime Engine) completed - may have created some subagents (verify and extend)
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
specs/020-chapter-2-ai-runtime/
├── spec.md                    # ✅ Feature specification
├── plan.md                    # TODO: Architecture plan
├── tasks.md                   # TODO: Implementation tasks
├── research.md                # ✅ Runtime engine extension research
├── data-model.md              # ✅ Data structures and entities
├── quickstart.md              # ✅ This file
├── contracts/
│   └── runtime-extension.yaml # ✅ Runtime extension contract
└── checklists/
    └── requirements.md        # ✅ Specification quality checklist
```

## Feature Overview

This feature extends the existing AI Runtime Engine (Feature 005) to support Chapter 2 content by creating scaffolding for:
1. **RAG Collection Setup**: Create `ch2_collection.py` with TODO stubs
2. **Embedding Pipeline Extension**: Add chapter=2 support to embedding client
3. **Chapter 2 Knowledge Source**: Verify `chapter_2_chunks.py` exists
4. **AI Block Runtime Routing Extension**: Route chapterId=2 calls to CH2 RAG
5. **Subagents Extension**: Verify or create Chapter 2 subagents
6. **Skills Reuse**: Add TODO comments for CH2 support
7. **ChatKit Session Support**: Extend session manager to track chapterId=2
8. **Environment & Config**: Add Chapter 2 settings to settings.py and .env.example
9. **API Stability**: Verify ai_blocks.py routes chapterId=2 correctly

## Key Files to Create/Modify

### New Files

1. **`backend/app/ai/rag/collections/ch2_collection.py`** (NEW)
   - Create RAG collection setup with TODO stubs
   - Add constant `CH2_COLLECTION_NAME = "chapter_2"`
   - Add functions: `create_collection()`, `upsert_vectors()`, `search()`

### Modified Files

2. **`backend/app/ai/embeddings/embedding_client.py`**
   - Add TODO stubs for chapter=2 support
   - Add placeholder for batch embedding for CH2

3. **`backend/app/content/chapters/chapter_2_chunks.py`**
   - Verify function `get_chapter_2_chunks()` exists (from Feature 012)
   - Add TODO comments if function is placeholder

4. **`backend/app/ai/runtime/engine.py`**
   - Add chapterId=2 routing to CH2 RAG
   - Add placeholder handler functions for CH2

5. **`backend/app/ai/subagents/ch2_ask_question_agent.py`** (Verify or create)
   - Verify file exists (from Feature 013) or create if missing
   - Add input/output schema placeholders
   - Add TODO: orchestrate provider + RAG

6. **`backend/app/ai/subagents/ch2_el10_agent.py`** (Verify or create)
   - Verify file exists (from Feature 013) or create if missing
   - Add input/output schema placeholders
   - Add TODO: orchestrate provider + RAG

7. **`backend/app/ai/subagents/ch2_quiz_agent.py`** (Verify or create)
   - Verify file exists (from Feature 013) or create if missing
   - Add input/output schema placeholders
   - Add TODO: orchestrate provider + RAG

8. **`backend/app/ai/subagents/ch2_diagram_agent.py`** (Verify or create)
   - Verify file exists (from Feature 013) or create if missing
   - Add input/output schema placeholders
   - Add TODO: orchestrate provider + RAG

9. **`backend/app/ai/skills/retrieval_skill.py`**
   - Add TODO: support CH2 collection name

10. **`backend/app/ai/skills/prompt_builder_skill.py`**
    - Add TODO: templates for CH2

11. **`backend/app/ai/chatkit/session_manager.py`**
    - Extend session_manager to track chapterId=2
    - Add TODO stub: attach CH2 memory nodes

12. **`backend/app/config/settings.py`**
    - Add `QDRANT_COLLECTION_CH2: Optional[str] = None`
    - Add `CH2_EMBEDDING_MODEL: Optional[str] = None`
    - Add `CH2_LLM_MODEL: Optional[str] = None`

13. **`.env.example`**
    - Add `QDRANT_COLLECTION_CH2="chapter_2"`
    - Add `CH2_EMBEDDING_MODEL="text-embedding-3-small"`
    - Add `CH2_LLM_MODEL="gpt-4o-mini"`

14. **`backend/app/api/ai_blocks.py`** (Verify)
    - Verify chapterId=2 routes correctly to runtime engine
    - Add comments if needed

## Implementation Steps

### Step 1: Verify Existing Files

1. Check if `chapter_2_chunks.py` exists (from Feature 012)
2. Check if Chapter 2 subagents exist (from Feature 013)
3. Check if `ai_blocks.py` routes chapterId=2 correctly

### Step 2: Create New Files

1. Create `backend/app/ai/rag/collections/` directory
2. Create `ch2_collection.py` with TODO stubs

### Step 3: Extend Existing Files

1. Update `embedding_client.py` with chapter=2 support
2. Update `engine.py` with chapterId=2 routing
3. Update skills files with CH2 TODOs
4. Update `session_manager.py` with chapterId=2 tracking
5. Update `settings.py` with Chapter 2 settings
6. Update `.env.example` with Chapter 2 variables

### Step 4: Verify or Create Subagents

1. Verify Chapter 2 subagents exist
2. Create missing subagents if needed
3. Ensure all subagents have TODO placeholders

### Step 5: Test Imports

1. Test all imports resolve without errors
2. Test backend starts successfully
3. Verify no circular dependencies

## Success Criteria

- ✅ All new Chapter 2 RAG, subagents, skills, and runtime stubs exist
- ✅ No real logic implemented (scaffolding only)
- ✅ Backend runs successfully
- ✅ No imports fail
- ✅ All TODO placeholders are descriptive and actionable
- ✅ Configuration settings are added to settings.py and .env.example
- ✅ API routes chapterId=2 requests correctly to runtime engine

## Troubleshooting

### Issue: Import Errors

**Solution**: Check that all new modules have proper `__init__.py` files and correct import paths

### Issue: Backend Won't Start

**Solution**: Check that all new settings in `settings.py` are optional (default to None)

### Issue: Missing Subagents

**Solution**: Create missing subagent files following the pattern from Feature 013

### Issue: Configuration Not Loading

**Solution**: Verify `.env.example` has correct variable names and restart backend

## Next Steps

After completing this feature:
1. Run `/sp.plan` to create architecture plan
2. Run `/sp.tasks` to generate implementation tasks
3. Run `/sp.implement` to implement scaffolding
