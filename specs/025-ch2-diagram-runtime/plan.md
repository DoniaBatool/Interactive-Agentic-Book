# Implementation Plan: Chapter 2 — Diagram Generator Runtime

**Branch**: `025-ch2-diagram-runtime` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/025-ch2-diagram-runtime/spec.md`

## Summary

This feature creates the complete diagram generator runtime scaffolding for Chapter 2 that mirrors the architecture of Feature 008 (Chapter 1 Diagram Engine). The implementation establishes the architectural foundation for Chapter 2 diagram runtime orchestrator, prompt template, routing integration, skills extensions, and API integration. **No real AI logic is implemented**—only scaffolding, function signatures, TODO placeholders, and architectural blueprints to prepare for future ROS 2 diagram generation implementation.

**Primary Deliverable**: Complete Chapter 2 diagram generator runtime infrastructure scaffolding (runtime module, prompt template, routing, skills, API integration)
**Validation**: All files exist, imports resolve, backend starts, no runtime errors, no diagram generation logic

## Technical Context

**Language/Version**:
- Backend: Python 3.11+ with FastAPI 0.109+

**Primary Dependencies**:
- Feature 008 (Chapter 1 Diagram Engine) - Required as reference for structure
- Feature 024 (Chapter 2 Backend Runtime Wiring) - Required for runtime engine routing
- Skills layer - Required for skills extension
- Runtime engine - Required for routing integration
- FastAPI 0.109+, Pydantic 2.x (already installed)
- No new runtime dependencies required (scaffolding only)

**Storage**:
- Static files (Python modules, text templates) - no database
- Future: Cache for generated diagrams

**Testing**:
- Manual: File existence verification, import resolution, backend startup
- Backend: Python import test (`python -c "from app.ai.diagram.ch2_diagram_runtime import run"`)
- Backend: Startup test (`uvicorn app.main:app`)
- No automated tests in this phase (scaffolding only)

**Target Platform**:
- Backend: FastAPI server (localhost:8000)

**Project Type**: Backend AI infrastructure scaffolding (diagram runtime for Chapter 2)

**Performance Goals**:
- Backend startup: < 2 seconds (no heavy initialization)
- No performance-critical operations (scaffolding only)

**Constraints**:
- MUST NOT implement real AI logic (no API calls, no diagram generation, no RAG calls, no LLM calls)
- MUST NOT break existing Chapter 1 diagram functionality
- MUST follow same patterns used in Feature 008 (Chapter 1 Diagram Engine)
- MUST ensure backend starts without errors
- MUST ensure all imports resolve correctly
- MUST use Python 3.11+ type hints
- MUST include TODO comments in all placeholder functions

**Scale/Scope**:
- 1 runtime module to create (ch2_diagram_runtime.py)
- 1 prompt template file to create (ch2_diagram_prompt.txt)
- 2 files to update (engine.py, ai_blocks.py)
- 2 skills files to update (prompt_builder_skill.py, formatting_skill.py)
- 1 contract file already created (diagram-contract.yaml)
- ~150-200 lines of scaffolding code (mostly TODOs, comments, and function stubs)

## Constitution Check

*GATE: Must pass before implementation. Re-check after Phase 1 design.*

### ✅ PASS - Principle I: AI-Native Spec-Driven Development

**Status**: COMPLIANT

- Specification created: `specs/025-ch2-diagram-runtime/spec.md` ✓
- Architecture planning: This plan document ✓
- SDD workflow followed: Spec → Plan → Tasks (next) → Implement ✓
- No code written without corresponding spec/plan artifacts ✓

### ✅ PASS - Principle II: Docusaurus-First Documentation Strategy

**Status**: COMPLIANT (Backend Feature)

- Backend diagram runtime supports frontend MDX components (from Feature 023) ✓
- No breaking changes to existing Chapter 1 or Chapter 2 content ✓
- Backend API endpoints support Chapter 2 diagram requests ✓

### ⚠️ PARTIAL - Principle III: RAG-First Chatbot Architecture

**Status**: SCAFFOLDING PHASE (ACCEPTABLE)

- Diagram runtime includes RAG placeholder step ✓
- Runtime engine routing includes Chapter 2 diagram path ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No actual RAG pipeline for Chapter 2 diagrams
  - No Qdrant vector search for Chapter 2 diagrams
  - No embedding generation for Chapter 2 diagrams

**Justification**: This is a scaffolding feature extending Chapter 1 diagram patterns to Chapter 2. RAG integration is explicitly planned for future features. Diagram runtime structure is designed to accept RAG-ready parameters.

### ✅ PASS - Principle IV: Personalization & User-Centric Design

**Status**: COMPLIANT (INFRASTRUCTURE)

- Backend routing supports Chapter 2 diagram context (chapterId=2) ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No user authentication
  - No personalization based on user profile

**Justification**: This feature extends backend infrastructure to Chapter 2 diagrams. Personalization will be added in future features when BetterAuth and user profiles are implemented.

### ✅ PASS - Principle V: Multilingual Support with On-Demand Translation

**Status**: COMPLIANT (STRUCTURE)

- Backend structure supports future translation (reusing from Chapter 1) ✓
- **Not Yet Implemented** (out of scope for this feature):
  - No Urdu translation
  - No translation pipeline

**Justification**: Backend structure is translation-ready. Translation will be added in future features when translation system is implemented.

### ✅ PASS - Principle VI: Test-Driven Quality Gates

**Status**: COMPLIANT (MANUAL TESTING PHASE)

- Clear acceptance criteria defined in spec.md (8 success criteria) ✓
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
| III. RAG-First | ⚠️ SCAFFOLDING | Runtime ready, actual RAG in future |
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
│  POST /api/ai/diagram                                         │
│  - Receives diagram request with chapterId=2                  │
│  - Routes to Chapter 2 diagram runtime                       │
│                                                               │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              Runtime Engine (engine.py)                      │
│                                                               │
│  if block_type == "diagram" AND chapterId == 2:             │
│    → Route to ch2_diagram_runtime.run()                      │
│                                                               │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│        Chapter 2 Diagram Runtime (ch2_diagram_runtime.py)   │
│                                                               │
│  5-Step Pipeline (all TODO):                                │
│  1. Validate diagram request                                 │
│  2. Build prompt (placeholder)                              │
│  3. Call RAG (placeholder)                                  │
│  4. Call provider LLM (placeholder)                          │
│  5. Format response (placeholder)                            │
│                                                               │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
┌───────────────────────┐   ┌───────────────────────────────┐
│  Prompt Template      │   │  Skills Layer                 │
│  (ch2_diagram_        │   │  - build_diagram_prompt_ch2()  │
│   prompt.txt)         │   │  - format_diagram_output_ch2()│
│                       │   │                               │
│  Variables:           │   │  (All placeholders)           │
│  - {{diagram_type}}   │   │                               │
│  - {{chapter_id}}     │   │                               │
│  - {{concepts}}       │   │                               │
└───────────────────────┘   └───────────────────────────────┘
```

### Key Components

1. **Chapter 2 Diagram Runtime**: Orchestrates diagram generation flow for ROS 2 diagrams
2. **Prompt Template**: ROS 2-specific prompt template with variable substitution
3. **Runtime Engine Routing**: Routes Chapter 2 diagram requests to ch2_diagram_runtime
4. **API Layer**: Handles diagram endpoint with chapterId=2 routing
5. **Skills Extensions**: Prompt building and formatting functions for Chapter 2

### Integration Points

- **AI Runtime Engine** (Feature 024): Routes diagram blocks to Chapter 2 diagram runtime
- **Chapter 1 Diagram Runtime** (Feature 008): Reference structure for Chapter 2 implementation
- **Skills Layer**: Provides prompt building and formatting capabilities
- **API Layer**: Receives diagram requests and routes to appropriate runtime

---

## Implementation Phases

### Phase 1: Diagram Runtime Module

**Goal**: Create Chapter 2 diagram runtime module with 5-step blueprint

**Files to Create**:
- `backend/app/ai/diagram/ch2_diagram_runtime.py`

**Implementation Details**:
- Create `async def run(diagram_type: str, chapter_id: int, concepts: List[str]) -> Dict[str, Any]` function
- Add 5-step pipeline blueprint (all TODO):
  1. Validate diagram request (TODO)
  2. Build prompt (placeholder)
  3. Call RAG (placeholder)
  4. Call provider LLM (placeholder)
  5. Format response (placeholder)
- All steps contain TODO markers only
- Placeholder return structure: `{"nodes": [], "edges": [], "svg": "", "metadata": {}}`

**Validation**:
- File exists
- Function is importable: `from app.ai.diagram.ch2_diagram_runtime import run`
- All 5 steps have TODO markers
- No real logic implementation

---

### Phase 2: Prompt Template

**Goal**: Create ROS 2-specific prompt template with placeholder variables

**Files to Create**:
- `backend/app/ai/prompts/diagram/ch2_diagram_prompt.txt`

**Implementation Details**:
- Create directory structure if needed: `backend/app/ai/prompts/diagram/`
- Create template file with placeholder variables:
  - `{{diagram_type}}` - Type of diagram (e.g., "ros2-ecosystem-overview")
  - `{{chapter_id}}` - Chapter identifier (should be 2)
  - `{{concepts}}` - ROS 2 concepts to include
- Add TODO comments for engineering full prompt later
- Include ROS 2-specific context placeholders

**Validation**:
- File exists and is readable
- All 3 variables are present
- TODO comments are present

---

### Phase 3: Runtime Engine Routing

**Goal**: Add Chapter 2 diagram routing to runtime engine

**Files to Update**:
- `backend/app/ai/runtime/engine.py`

**Implementation Details**:
- Add routing case in `run_ai_block()` function:
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
- Comments only, no logic
- Placeholder routing with TODO comments

**Validation**:
- Routing condition checks both `block_type == "diagram"` AND `chapterId == 2`
- Routing is comment-only (no logic)
- TODO comments are present
- File still imports correctly

---

### Phase 4: API Layer Update

**Goal**: Update diagram endpoint to support Chapter 2 routing

**Files to Update**:
- `backend/app/api/ai_blocks.py`

**Implementation Details**:
- Add Chapter 2 routing comment to `diagram()` endpoint:
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
- Add TODO documentation tags
- Ensure routing supports chapterId=2

**Validation**:
- Endpoint accepts chapterId=2
- Routing comments are present
- File still imports correctly
- No breaking changes to existing functionality

---

### Phase 5: Contracts

**Goal**: Document expected placeholders for Chapter 2 diagrams

**Files**:
- `specs/025-ch2-diagram-runtime/contracts/diagram-contract.yaml` (already created in spec phase)

**Validation**:
- Contract file exists
- Documents expected placeholders
- No schemas for actual diagram formats (placeholder only)

---

### Phase 6: Skills Extension

**Goal**: Add Chapter 2 diagram placeholder functions to skills layer

**Files to Update**:
- `backend/app/ai/skills/prompt_builder_skill.py`
- `backend/app/ai/skills/formatting_skill.py`

**Implementation Details**:

**prompt_builder_skill.py**:
- Add `build_diagram_prompt_ch2()` function:
  ```python
  def build_diagram_prompt_ch2(
      diagram_type: str,
      chapter_id: int,
      concepts: List[str]
  ) -> str:
      """
      Build diagram prompt for Chapter 2.
      
      TODO: Implement prompt building for Chapter 2 diagrams
      TODO: Load ch2_diagram_prompt.txt template
      TODO: Replace template variables
      TODO: Add ROS 2-specific context
      TODO: Return constructed prompt string
      """
      return ""  # Placeholder
  ```

**formatting_skill.py**:
- Add `format_diagram_output_ch2()` function:
  ```python
  def format_diagram_output_ch2(
      raw_response: Dict[str, Any]
  ) -> Dict[str, Any]:
      """
      Format diagram output for Chapter 2.
      
      TODO: Implement formatting for Chapter 2 diagram output
      TODO: Parse raw LLM response
      TODO: Extract nodes, edges, SVG
      TODO: Format ROS 2-specific metadata
      TODO: Return formatted diagram structure
      """
      return {}  # Placeholder
  ```

**Validation**:
- Functions are importable
- Functions have TODO comments
- No real logic implementation
- Files still import correctly

---

### Phase 7: Validation

**Goal**: Ensure backend runs and no logic exists

**Validation Steps**:
1. **Backend Startup Test**:
   - Run: `cd backend && uvicorn app.main:app`
   - Expected: Backend starts without errors
   - Check: No import errors, no syntax errors

2. **Module Import Test**:
   - Run: `python -c "from app.ai.diagram.ch2_diagram_runtime import run; print('Import successful')"`
   - Expected: Import succeeds
   - Check: All new modules are importable

3. **Logic Verification**:
   - Verify: No real AI logic implemented
   - Verify: All steps contain TODO markers only
   - Verify: All functions return placeholder values

**Validation Checklist**:
- [ ] Backend starts without errors
- [ ] All imports resolve correctly
- [ ] ch2_diagram_runtime.py exists and is importable
- [ ] ch2_diagram_prompt.txt exists and is readable
- [ ] Runtime engine has Chapter 2 diagram routing (comments only)
- [ ] API layer has Chapter 2 diagram routing comments
- [ ] Skills have Chapter 2 diagram placeholder functions
- [ ] No real AI logic implemented (only placeholders)

---

## Key Decisions

### Decision 1: Create Chapter 2-Specific Runtime Module

**Rationale**: Clear separation between Chapter 1 and Chapter 2 logic, mirrors Feature 008 structure

**Alternative Considered**: Extend existing diagram runtime with Chapter 2 branches

**Chosen**: Create `ch2_diagram_runtime.py` as separate module

**Impact**: Clear separation, easier to implement Chapter 2-specific logic later, maintains consistency with Feature 008

---

### Decision 2: Create Chapter 2 Prompt Template

**Rationale**: ROS 2-specific prompts need different context and examples than Chapter 1

**Alternative Considered**: Reuse Chapter 1 prompt template with variables

**Chosen**: Create `ch2_diagram_prompt.txt` with ROS 2-specific placeholders

**Impact**: Better prompt engineering for ROS 2 diagrams, clear separation of concerns

---

### Decision 3: Placeholder-Only Implementation

**Rationale**: This is a scaffolding feature, no real AI logic should be implemented

**Alternative Considered**: Implement partial logic

**Chosen**: Placeholder-only with TODO comments

**Impact**: Clear separation between scaffolding and implementation phases, prevents premature optimization

---

### Decision 4: Comment-Only Routing

**Rationale**: Routing logic should be documented but not implemented until real AI logic is ready

**Alternative Considered**: Implement routing logic with placeholder calls

**Chosen**: Comment-only routing with TODO markers

**Impact**: Clear documentation of expected flow, prevents import errors, maintains backend stability

---

## Risk Analysis

### Risk 1: Import Errors

**Description**: New modules may have import errors preventing backend startup

**Probability**: Medium

**Impact**: High (blocks backend startup)

**Mitigation**:
- Test all imports after file creation
- Ensure all files are syntactically correct
- Verify backend starts without errors
- Use placeholder imports in routing comments

**Status**: Mitigated by validation phase

---

### Risk 2: Breaking Existing Functionality

**Description**: Changes to runtime engine or API layer may break Chapter 1 diagram functionality

**Probability**: Low

**Impact**: High (breaks existing features)

**Mitigation**:
- Only add placeholders and comments
- Don't modify existing logic
- Test Chapter 1 diagram functionality still works
- Use comment-only routing

**Status**: Mitigated by comment-only approach

---

### Risk 3: Incomplete Scaffolding

**Description**: Missing files or incomplete structure may cause issues in future implementation

**Probability**: Low

**Impact**: Medium (requires refactoring later)

**Mitigation**:
- Follow Feature 008 patterns exactly
- Ensure all required files are created
- Verify all TODO comments are present
- Use comprehensive validation checklist

**Status**: Mitigated by following established patterns

---

## Validation Strategy

### Pre-Implementation Validation

- [ ] Specification reviewed and approved
- [ ] Architecture plan reviewed and approved
- [ ] Dependencies verified (Feature 008, Feature 024)
- [ ] Constitution check passed

### During Implementation Validation

- [ ] Each phase validated before proceeding
- [ ] Files created with correct structure
- [ ] Imports tested after each file creation
- [ ] No real logic implemented (only placeholders)

### Post-Implementation Validation

- [ ] Backend starts without errors
- [ ] All imports resolve correctly
- [ ] All files exist at specified paths
- [ ] All TODO comments are present
- [ ] No real AI logic implemented
- [ ] Chapter 1 diagram functionality still works

---

## Success Criteria

- ✅ Diagram runtime module for Chapter 2 exists (ch2_diagram_runtime.py)
- ✅ Prompt template file exists (ch2_diagram_prompt.txt)
- ✅ Engine correctly routes CH2 diagram requests (if block_type == "diagram" AND chapterId == 2)
- ✅ AI-block diagram endpoint supports chapterId=2
- ✅ Contracts folder contains diagram-contract.yaml
- ✅ Skills have Chapter 2 diagram placeholder functions
- ✅ No LLM or RAG logic implemented (only placeholders and structure)
- ✅ Backend compiles and runs without errors

---

## Next Steps

1. **Task Generation**: Run `/sp.tasks` to generate atomic implementation tasks
2. **Implementation**: Execute tasks in order (Phase 1 → Phase 7)
3. **Validation**: Run validation checklist after each phase
4. **Documentation**: Update PHR after implementation

---

## Summary

This plan establishes the complete architecture for Chapter 2 diagram generator runtime scaffolding. The implementation follows Feature 008 patterns, creates all necessary files with placeholder-only content, and ensures backend stability. All routing is comment-only, all logic is placeholder-only, and all validation focuses on structure and imports rather than functionality.

**Estimated Implementation Time**: 30-45 minutes (scaffolding only)
**Complexity**: Low (scaffolding only, no real AI logic)
**Dependencies**: Feature 008 (Chapter 1 Diagram Engine), Feature 024 (Chapter 2 Backend Runtime Wiring)
**Out of Scope**: Real AI logic, RAG implementation, LLM calls, diagram generation

