# Implementation Plan: Chapter 2 — Backend Runtime Wiring for AI Blocks

**Branch**: `024-ch2-runtime-wiring` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/024-ch2-runtime-wiring/spec.md`

## Summary

This feature wires Chapter 2 into the backend runtime system by updating API layer routing, extending runtime engine with Chapter 2 branches, creating Chapter 2 chunks file, creating subagent scaffold files, extending skills layer with placeholder routing, and documenting the runtime flow. **No real AI logic is implemented**—only scaffolding, TODO placeholders, and architectural blueprints to mirror Chapter 1 backend runtime structure for Chapter 2.

**Primary Deliverable**: Complete backend runtime wiring scaffolding for Chapter 2 (API routing, runtime engine branches, chunks file, subagent scaffolds, skills extensions)
**Validation**: Backend starts successfully, all imports resolve, no business logic implemented

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- Feature 006 (AI Runtime Engine) - Runtime engine must exist
- Feature 023 (Chapter 2 AI Block MDX Integration) - Frontend blocks must exist
- Chapter 1 chunks structure - Required as reference for chapter_2_chunks.py
- Existing subagents - Required as reference for subagent structure
- Skills layer - Required for skills extension

**Storage**: 
- Static files (Python modules) - no database

**Testing**:
- Manual: Backend startup verification, import resolution
- Backend: Python import test (`python -c "from app.content.chapters.chapter_2_chunks import get_chapter_chunks"`)
- Backend: Startup test (`uvicorn app.main:app`)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)

**Project Type**: Backend runtime wiring scaffolding (API routing + runtime engine + chunks file + subagents + skills)

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (only scaffolding and placeholders)
- MUST NOT break existing Chapter 1 functionality
- MUST follow same patterns used in Chapter 1 runtime wiring
- MUST ensure backend starts without errors
- MUST ensure all imports resolve correctly

**Scale/Scope**:
- 1 API file to update (ai_blocks.py)
- 1 runtime engine file to update (engine.py)
- 1 chunks file to create (chapter_2_chunks.py)
- 4 subagent files to create (ch2_*_agent.py)
- 3 skills files to update (retrieval_skill.py, prompt_builder_skill.py, formatting_skill.py)
- 1 contract file already created (runtime-flow.yaml)
- ~50-100 lines of scaffolding code (mostly TODOs, comments, and function stubs)

## Constitution Check

*GATE: Must pass before implementation. Re-check after Phase 1 design.*

### ✅ PASS - Principle I: AI-Native Spec-Driven Development

**Status**: COMPLIANT

- Specification created: `specs/024-ch2-runtime-wiring/spec.md` ✓
- Architecture planning: This plan document ✓
- SDD workflow followed: Spec → Plan → Tasks (next) → Implement ✓
- No code written without corresponding spec/plan artifacts ✓

### ✅ PASS - Principle II: Docusaurus-First Documentation Strategy

**Status**: COMPLIANT (Backend Feature)

- Backend wiring supports frontend MDX components (from Feature 023) ✓
- No breaking changes to existing Chapter 1 or Chapter 2 content ✓
- Backend API endpoints support Chapter 2 requests ✓

### ⚠️ PARTIAL - Principle III: RAG-First Chatbot Architecture

**Status**: SCAFFOLDING PHASE (ACCEPTABLE)

- Chapter 2 chunks file prepared for future RAG integration ✓
- Runtime engine routing includes Chapter 2 path ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No actual RAG pipeline for Chapter 2
  - No Qdrant vector search for Chapter 2
  - No embedding generation for Chapter 2

**Justification**: This is a scaffolding feature extending Chapter 1 patterns to Chapter 2. RAG integration is explicitly planned for future features. Chapter 2 chunks structure and runtime engine routing are designed to accept RAG-ready parameters.

### ✅ PASS - Principle IV: Personalization & User-Centric Design

**Status**: COMPLIANT (INFRASTRUCTURE)

- Backend routing supports Chapter 2 context (chapterId=2) ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No user authentication
  - No personalization based on user profile

**Justification**: This feature extends backend infrastructure to Chapter 2. Personalization will be added in future features when BetterAuth and user profiles are implemented.

### ✅ PASS - Principle V: Multilingual Support with On-Demand Translation

**Status**: COMPLIANT (STRUCTURE)

- Backend structure supports future translation (reusing from Chapter 1) ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No Urdu translation
  - No translation pipeline

**Justification**: Backend structure is translation-ready. Translation will be added in future features when translation system is implemented.

### ✅ PASS - Principle VI: Test-Driven Quality Gates

**Status**: COMPLIANT (MANUAL TESTING PHASE)

- Clear acceptance criteria defined in spec.md (7 success criteria) ✓
- Manual validation methods specified (backend startup, import tests) ✓
- **Not Yet Implemented** (automated testing out of scope for scaffolding):
  - No unit tests (scaffolding only, no logic)
  - No integration tests (no real AI logic to test)

**Justification**: This is a scaffolding feature with minimal new logic (mostly integration). Automated tests will be added in future features when real AI functionality is implemented.

---

### Constitution Check Summary

| Principle | Status | Notes |
|-----------|--------|-------|
| I. SDD Workflow | ✅ PASS | Full spec → plan → tasks workflow followed |
| II. Docusaurus-First | ✅ PASS | Backend supports frontend MDX components |
| III. RAG-First | ⚠️ SCAFFOLDING | Chunks file ready, actual RAG in future |
| IV. Personalization | ✅ PASS | Infrastructure supports future personalization |
| V. Multilingual | ✅ PASS | Structure supports translation, implementation deferred |
| VI. TDD Quality Gates | ✅ PASS | Manual validation appropriate for scaffolding phase |

**Overall**: ✅ **APPROVED TO PROCEED**

---

## Architecture Overview

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    API Layer (ai_blocks.py)                  │
│                                                               │
│  POST /api/ai/ask-question (chapterId=2)                     │
│  POST /api/ai/explain-like-10 (chapterId=2)                │
│  POST /api/ai/quiz (chapterId=2)                            │
│  POST /api/ai/diagram (chapterId=2)                         │
│                                                               │
│  Routes to: run_ai_block(block_type, request_data)          │
│  TODO: Chapter 2 runtime call                                │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ Request with chapterId=2
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              Runtime Engine (engine.py)                      │
│                                                               │
│  run_ai_block(block_type, request_data)                     │
│    │                                                          │
│    ├─► Detect chapterId=2                                   │
│    │   └─► Route to Chapter 2 handling path (TODO)          │
│    │       │                                                  │
│    │       ├─► Check ENABLE_CHAPTER_2_RUNTIME (TODO)        │
│    │       ├─► Import Chapter 2 subagents (TODO)            │
│    │       ├─► Route to Chapter 2 subagent (TODO)           │
│    │       └─► Load Chapter 2 RAG context (TODO)            │
│    │           │                                              │
│    │           ▼                                              │
│    │       Expected Flow (Documented):                        │
│    │       request → rag_pipeline → provider → formatter → response │
│    │                                                          │
│    └─► Chapter 2 Chunks (chapter_2_chunks.py)               │
│        └─► get_chapter_chunks(chapter_id=2) → [] (placeholder) │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ Route to subagent
                           ▼
┌─────────────────────────────────────────────────────────────┐
│          Chapter 2 Subagents (ch2_*_agent.py)                │
│                                                               │
│  ch2_ask_question_agent.py (TODO placeholder)               │
│  ch2_explain_el10_agent.py (TODO placeholder)               │
│  ch2_quiz_agent.py (TODO placeholder)                        │
│  ch2_diagram_agent.py (TODO placeholder)                     │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ Use skills
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              Skills Layer (skills/*.py)                      │
│                                                               │
│  retrieval_skill.py                                          │
│    if chapterId == 2: # TODO                                │
│                                                               │
│  prompt_builder_skill.py                                     │
│    if chapterId == 2: # TODO                                │
│                                                               │
│  formatting_skill.py                                          │
│    if chapterId == 2: # TODO                                │
└─────────────────────────────────────────────────────────────┘
```

### Request Flow

1. **API Endpoint**: Receives request with chapterId=2
2. **Runtime Engine**: Detects chapterId=2, routes to Chapter 2 handling path
3. **Chapter 2 Chunks**: Loads chunks (placeholder: empty list)
4. **Chapter 2 Subagent**: Processes request (placeholder: TODO)
5. **Skills Layer**: Applies skills (placeholder: TODO routing)
6. **Response**: Returns to API endpoint

---

## Implementation Phases

### Phase 1: API Layer Updates

**Goal**: Update API layer to route chapterId=2 cases to runtime engine

**Tasks**:
1. Update `backend/app/api/ai_blocks.py`:
   - Verify routing to `run_ai_block()` includes chapterId=2 support
   - Add TODO notes where final logic will go: `# TODO: Chapter 2 runtime call`
   - Ensure all 4 endpoints (ask-question, explain-like-10, quiz, diagram) support chapterId=2

**Deliverables**:
- Updated ai_blocks.py with Chapter 2 routing comments
- All endpoints route chapterId=2 to runtime engine

**Validation**:
- API file routes correctly
- TODO comments are present
- No breaking changes to existing routing

---

### Phase 2: Runtime Engine Routing

**Goal**: Extend runtime engine with Chapter 2 branches

**Tasks**:
1. Update `backend/app/ai/runtime/engine.py`:
   - Verify/add placeholder routing for chapterId=2
   - Document expected request flow: `request → rag_pipeline → provider → formatter → response`
   - Add TODO comments for Chapter 2 routing steps:
     - `# TODO: Check ENABLE_CHAPTER_2_RUNTIME flag`
     - `# TODO: Import Chapter 2 subagents`
     - `# TODO: Route to Chapter 2 subagent`
     - `# TODO: Load Chapter 2 RAG context`

**Deliverables**:
- Updated engine.py with Chapter 2 routing branches
- Documented expected flow in comments

**Validation**:
- Runtime engine has Chapter 2 routing path
- Flow documentation is clear
- No breaking changes to Chapter 1 routing

---

### Phase 3: Chapter 2 Chunk Source

**Goal**: Add chapter_2_chunks.py with empty get_chapter_chunks()

**Tasks**:
1. Create `backend/app/content/chapters/chapter_2_chunks.py`:
   - Define `get_chapter_chunks(chapter_id: int = 2) -> List[Dict[str, Any]]:`
   - Include empty return: `return []`
   - Add TODO comments explaining future implementation
   - Ensure parity with chapter_1_chunks structure

**Deliverables**:
- Created chapter_2_chunks.py file
- Function signature matches chapter_1_chunks
- File is importable

**Validation**:
- File exists and is importable
- Function signature is correct
- Return type matches expected structure

---

### Phase 4: Subagent Structure

**Goal**: Mirror Feature 006 agents, create 4 placeholder agents for CH2

**Tasks**:
1. Create `backend/app/ai/subagents/ch2_ask_question_agent.py`:
   - Empty scaffold with TODO comment: `# TODO: blueprint for Chapter 2 version of the agent`
2. Create `backend/app/ai/subagents/ch2_explain_el10_agent.py`:
   - Empty scaffold with TODO comment
3. Create `backend/app/ai/subagents/ch2_quiz_agent.py`:
   - Empty scaffold with TODO comment
4. Create `backend/app/ai/subagents/ch2_diagram_agent.py`:
   - Empty scaffold with TODO comment

**Deliverables**:
- All 4 subagent files created
- Files are importable
- Files contain TODO placeholders

**Validation**:
- All 4 files exist
- Files are importable without errors
- Files contain TODO comments

---

### Phase 5: Skill Layer Extension

**Goal**: Add placeholder routing for Chapter 2 in skills

**Tasks**:
1. Update `backend/app/ai/skills/retrieval_skill.py`:
   - Add placeholder routing: `if chapterId == 2: # TODO`
   - Keep logic empty
2. Update `backend/app/ai/skills/prompt_builder_skill.py`:
   - Add placeholder routing: `if chapterId == 2: # TODO`
   - Keep logic empty
3. Update `backend/app/ai/skills/formatting_skill.py`:
   - Add placeholder routing: `if chapterId == 2: # TODO`
   - Keep logic empty

**Deliverables**:
- Updated skills files with Chapter 2 placeholder routing
- No logic implemented (only comments)

**Validation**:
- Skills files have Chapter 2 placeholder routing
- Files still import correctly
- No breaking changes to existing skills

---

### Phase 6: Contracts

**Goal**: Document flow requirements in runtime-flow.yaml

**Tasks**:
1. Verify `specs/024-ch2-runtime-wiring/contracts/runtime-flow.yaml` exists (already created in spec phase)
2. Verify contract documents:
   - Expected runtime flow for Chapter 2
   - API → Runtime Engine → Subagent flow
   - Chapter 2-specific routing patterns

**Deliverables**:
- Contract file documents runtime flow
- Flow requirements are clear

**Validation**:
- Contract file exists and is complete
- Flow documentation is accurate

---

### Phase 7: Validation

**Goal**: Ensure backend runs and all imports work

**Tasks**:
1. Test backend startup: `uvicorn app.main:app`
2. Test module imports:
   - `from app.content.chapters.chapter_2_chunks import get_chapter_chunks`
   - `from app.ai.subagents.ch2_ask_question_agent import *`
3. Verify no import errors
4. Verify no syntax errors

**Deliverables**:
- Backend starts successfully
- All imports resolve correctly
- No errors in startup

**Validation**:
- Backend starts without errors
- All new modules are importable
- No circular import errors

---

## Key Decisions

### Decision 1: Create Chapter 2-Specific Subagent Files

**Rationale**: Clear separation between Chapter 1 and Chapter 2 logic, easier to maintain, mirrors Feature 006 structure

**Alternative Considered**: Extend existing subagents with Chapter 2 branches

**Chosen**: Create ch2_*_agent.py files as empty scaffolds

**Impact**: Clear separation, easier to implement Chapter 2-specific logic later

---

### Decision 2: Comment-Only Skills Extensions

**Rationale**: Skills are reusable across chapters, only need to document Chapter 2 handling paths

**Alternative Considered**: Create Chapter 2-specific skills files

**Chosen**: Add placeholder routing comments to existing skills files

**Impact**: Minimal changes, maintains skill reusability

---

### Decision 3: Placeholder-Only Implementation

**Rationale**: This is a scaffolding feature, no real AI logic should be implemented

**Alternative Considered**: Implement partial logic

**Chosen**: Placeholder-only with TODO comments

**Impact**: Clear separation between scaffolding and implementation phases

---

## Risk Analysis

### Risk 1: Import Errors

**Probability**: Medium
**Impact**: High
**Mitigation**: 
- Test all imports after file creation
- Ensure all files are syntactically correct
- Verify backend starts without errors

---

### Risk 2: Breaking Existing Functionality

**Probability**: Low
**Impact**: High
**Mitigation**:
- Only add placeholders and comments
- Don't modify existing logic
- Test Chapter 1 functionality still works

---

### Risk 3: Incomplete Scaffolding

**Probability**: Low
**Impact**: Medium
**Mitigation**:
- Follow Chapter 1 patterns exactly
- Ensure all required files are created
- Verify all TODO comments are present

---

## Non-Functional Requirements

### NFR-001: Code Quality

**Requirement**: Code must follow existing patterns and conventions

**Implementation**:
- Follow Chapter 1 patterns
- Use consistent naming (ch2_* prefix)
- Add clear TODO comments

**Validation**: Code review, pattern consistency check

---

### NFR-002: Maintainability

**Requirement**: Code must be easy to understand and modify

**Implementation**:
- Clear TODO comments
- Documented expected flows
- Consistent structure

**Validation**: Code readability, documentation completeness

---

### NFR-003: Stability

**Requirement**: Backend must start without errors

**Implementation**:
- All imports must resolve
- No syntax errors
- No circular imports

**Validation**: Backend startup test, import tests

---

## Success Criteria

- **SC-001**: Chapter 2 has complete scaffolding for backend runtime ✓
- **SC-002**: All subagent files exist (4 files) ✓
- **SC-003**: Runtime engine references Chapter 2 correctly ✓
- **SC-004**: No AI logic exists—only placeholders and structure ✓
- **SC-005**: Backend compiles and runs ✓
- **SC-006**: All new modules import correctly ✓
- **SC-007**: Contract file documents expected runtime flow ✓

---

## Out of Scope

- ❌ Implementing real AI logic for Chapter 2
- ❌ Implementing RAG pipeline for Chapter 2
- ❌ Implementing chunking logic for Chapter 2
- ❌ Implementing subagent logic for Chapter 2
- ❌ Implementing skills logic for Chapter 2
- ❌ Creating new runtime engine infrastructure
- ❌ Adding authentication or personalization
- ❌ Implementing LLM provider calls

---

## Dependencies

- **Dependency 1**: Feature 006 (AI Runtime Engine) - Required for runtime engine infrastructure
- **Dependency 2**: Feature 023 (Chapter 2 AI Block MDX Integration) - Required for frontend AI blocks
- **Dependency 3**: Chapter 1 chunks structure - Required as reference for chapter_2_chunks.py structure
- **Dependency 4**: Existing subagents - Required as reference for subagent structure
- **Dependency 5**: Skills layer - Required for skills extension

---

## Next Steps

1. **Generate Tasks**: Run `/sp.tasks` to create atomic implementation tasks
2. **Implement Scaffolding**: Run `/sp.implement` to implement backend wiring
3. **Validate**: Test backend startup and imports
4. **Document**: Update contract with actual file structures

---

## Summary

This plan establishes the architecture for wiring Chapter 2 into the backend runtime system. The implementation is straightforward: update API routing, extend runtime engine, create chunks file, create subagent scaffolds, extend skills, and validate. All components mirror Chapter 1 patterns, ensuring consistency and easier maintenance. The focus is on scaffolding only—no backend logic or AI implementation is included in this feature.

**Estimated Implementation Time**: 45-60 minutes (scaffolding only)
**Complexity**: Low (scaffolding only, following established patterns)
**Risk Level**: Low (minimal changes, well-established patterns)

