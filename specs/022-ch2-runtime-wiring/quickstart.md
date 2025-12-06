# Quickstart: Chapter 2 Runtime Wiring

**Feature**: 022-ch2-runtime-wiring

## Prerequisites

- Feature 005: AI Runtime Engine (must exist)
- Feature 012: Chapter 2 RAG Collection (must exist)
- Feature 013: Chapter 2 Subagents (must exist, or created in Feature 020)
- Feature 020: Chapter 2 AI Runtime Extension (must exist)
- Feature 021: Chapter 2 RAG Preparation (must exist)

## Commands

```bash
# Specification phase
/sp.specify

# Architecture plan phase
/sp.plan

# Implementation tasks phase
/sp.tasks

# Implementation phase
/sp.implement
```

## Folder Structure

```
specs/022-ch2-runtime-wiring/
├── spec.md                          # Feature specification
├── plan.md                          # Architecture plan (to be created)
├── tasks.md                         # Implementation tasks (to be created)
├── contracts/
│   └── runtime-wiring.yaml           # Runtime wiring contract
├── research.md                      # Research notes
├── data-model.md                    # Data model documentation
├── quickstart.md                    # This file
└── checklists/
    └── requirements.md              # Specification quality checklist
```

## Feature Overview

This feature wires Chapter 2 into the AI Runtime Engine by:

1. **RAG Pipeline Wiring**: Adding Chapter 2-specific entry points (TODO stubs)
2. **Runtime Engine Routing**: Registering chapter_id=2 handling path
3. **API Endpoint Hooks**: Adding Chapter 2 context loading (TODO stubs)
4. **Subagent Connectors**: Adding Chapter 2 handling path comments (TODO stubs)
5. **Knowledge Source Structure**: Adding structural metadata placeholders

## Key Files to Create/Modify

### Files to Modify

1. `backend/app/ai/rag/pipeline.py`
   - Add `CHAPTER_2_COLLECTION_NAME` constant
   - Add TODO stubs: `embed_chapter_2()`, `retrieve_chapter_2_relevant_chunks()`, `build_context_for_ch2()`

2. `backend/app/ai/runtime/engine.py`
   - Register chapter_id=2 handling path
   - Add TODO comments for context merging and provider selection

3. `backend/app/api/ai_blocks.py`
   - Add TODO comments for loading Chapter 2 context in all endpoints
   - Ensure all endpoints support chapterId=2

4. `backend/app/ai/subagents/ask_question_agent.py`
   - Add TODO comments for Chapter 2 handling path

5. `backend/app/ai/subagents/explain_el10_agent.py`
   - Add TODO comments for Chapter 2 handling path

6. `backend/app/ai/subagents/quiz_agent.py`
   - Add TODO comments for Chapter 2 handling path

7. `backend/app/ai/subagents/diagram_agent.py`
   - Add TODO comments for Chapter 2 handling path

8. `backend/app/content/chapters/chapter_2_chunks.py`
   - Add structural TODO comments: `chunk_count`, `expected_section_map`, `embedding_ready`

### Files to Create

1. `specs/022-ch2-runtime-wiring/contracts/runtime-wiring.yaml`
   - Document chapter selection flow → RAG → LLM → response
   - Document required placeholders
   - Document API-level routing contract
   - Document context-building contract

## Implementation Steps

### Phase 1: Specification (Current)

- ✅ Create `spec.md` with all required sections
- ✅ Create `contracts/runtime-wiring.yaml` with contracts
- ✅ Create `research.md` with research notes
- ✅ Create `data-model.md` with data model documentation
- ✅ Create `quickstart.md` (this file)
- ✅ Create `checklists/requirements.md` with quality checklist

### Phase 2: Architecture Plan (Next)

- Create `plan.md` with detailed architecture plan
- Document integration points
- Document routing logic
- Document context assembly flow

### Phase 3: Implementation Tasks (Following)

- Create `tasks.md` with atomic implementation tasks
- Group tasks by component (RAG Pipeline, Runtime Engine, API Endpoints, Subagents, Knowledge Source)
- Specify file paths, expected content, dependencies, acceptance tests

### Phase 4: Implementation (Final)

- Update `backend/app/ai/rag/pipeline.py` with Chapter 2 TODO stubs
- Update `backend/app/ai/runtime/engine.py` with chapter_id=2 routing
- Update `backend/app/api/ai_blocks.py` with Chapter 2 context loading TODOs
- Update all subagent files with Chapter 2 handling path TODOs
- Update `backend/app/content/chapters/chapter_2_chunks.py` with structural metadata TODOs
- Validate all imports resolve
- Validate backend starts without errors

## Success Criteria

- ✅ Chapter 2 is fully wired into AI runtime scaffolding
- ✅ RAG pipeline contains CH2 entry points (TODO stubs)
- ✅ AI block runtime supports CH2 selection (chapter_id=2 routing)
- ✅ All routing and placeholder comments exist
- ✅ No business logic implemented (scaffolding only)
- ✅ Backend starts with no errors
- ✅ All import paths valid
- ✅ Runtime engine now "aware" of Chapter 2

## Troubleshooting

### Backend Won't Start

- Check all imports resolve: `python -c "from app.ai.rag.pipeline import ..."`
- Check for syntax errors in modified files
- Verify all TODO comments are properly formatted

### Import Errors

- Verify all module paths are correct
- Check that all dependencies exist (Feature 005, 012, 013, 020, 021)
- Ensure all imports use absolute paths from `app.`

### Routing Not Working

- Verify chapter_id=2 handling path exists in `engine.py`
- Check that all API endpoints route to runtime engine
- Verify subagent routing logic includes Chapter 2

## Next Steps

1. Complete specification phase (current)
2. Create architecture plan (`/sp.plan`)
3. Generate implementation tasks (`/sp.tasks`)
4. Implement scaffolding (`/sp.implement`)
