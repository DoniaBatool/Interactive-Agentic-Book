# Feature Specification: Chapter 2 — AI Runtime Engine Integration (LLM Routing, RAG Wiring, Subagents, ChatKit)

**Feature Branch**: `013-chapter-2-runtime-engine`
**Created**: 2025-12-05
**Status**: Draft
**Input**: User description: "Activate the full runtime pathway for Chapter 2 so all AI Blocks (ask-question, explain-like-i-am-10, quiz, diagram) correctly route through the AI Runtime Engine. The logic remains placeholder-only, similar to Feature 005 for Chapter 1."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Sets Up Chapter 2 Runtime Engine Infrastructure (Priority: P1)

As a backend developer, I need Chapter 2 runtime engine scaffolding in place with routing, RAG binding, subagents, skills, and ChatKit integration defined, so I can implement real AI logic in future features without restructuring the codebase.

**Why this priority**: This establishes the complete runtime pathway for Chapter 2 AI blocks. Without proper scaffolding, future AI implementation will require refactoring and restructuring, causing delays and technical debt.

**Independent Test**: Can be fully tested by verifying all required files exist at specified paths, all imports resolve without errors, backend starts successfully, and all modules contain TODO placeholders for future implementation.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/ai/runtime/engine.py`, **Then** I see chapter_id=2 routing with placeholder LLM invocation and RAG-context consumption comments
2. **Given** the feature is implemented, **When** I check `backend/app/ai/rag/pipeline.py`, **Then** I see placeholder flow comments for pipeline.load_chapter(2) resolving to chapter_2_chunks
3. **Given** the feature is implemented, **When** I check `backend/app/api/ai_blocks.py`, **Then** I see all block types route to `run_ai_block(block_type, chapter_id=2)` for Chapter 2 requests
4. **Given** the feature is implemented, **When** I check `backend/app/ai/subagents/`, **Then** I see 4 Chapter 2-specific agent files (`ch2_ask_question_agent.py`, `ch2_explain_el10_agent.py`, `ch2_quiz_agent.py`, `ch2_diagram_agent.py`) with TODO blueprints
5. **Given** the feature is implemented, **When** I check `backend/app/ai/skills/`, **Then** I see TODO comments for chapter-aware prompt builder, formatting rules for Chapter 2, and retrieval-skills connection notes
6. **Given** the feature is implemented, **When** I check `backend/app/ai/chatkit/session_manager.py`, **Then** I see placeholder for multi-chapter session contexts
7. **Given** the feature is implemented, **When** I check `backend/app/ai/chatkit/tools.py`, **Then** I see tool definitions for Chapter 2 blocks
8. **Given** the feature is implemented, **When** I check `backend/app/config/settings.py`, **Then** I see new settings for `DEFAULT_CH2_MODEL`, `DEFAULT_CH2_EMBEDDINGS`, `ENABLE_CHAPTER_2_RUNTIME`
9. **Given** the feature is implemented, **When** I start the backend server, **Then** it starts without import errors or runtime exceptions

---

### User Story 2 - System Administrator Configures Chapter 2 Runtime Settings (Priority: P2)

As a system administrator, I need environment variables and configuration settings for Chapter 2 runtime operations (default model, embeddings, runtime enable flag), so I can configure the system for Chapter 2 runtime without code changes.

**Why this priority**: Important for deployment flexibility and Chapter 2-specific configuration, but not critical for initial scaffolding. Configuration can be added incrementally.

**Independent Test**: Can be fully tested by checking `backend/app/config/settings.py` for new settings, verifying `.env.example` includes all new variables, and confirming backend can read these variables without errors.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I check `backend/app/config/settings.py`, **Then** I see new settings for `DEFAULT_CH2_MODEL`, `DEFAULT_CH2_EMBEDDINGS`, `ENABLE_CHAPTER_2_RUNTIME`
2. **Given** the feature is implemented, **When** I check `.env.example`, **Then** I see all new environment variables documented with descriptions and placeholder values
3. **Given** the backend is running, **When** I check the startup logs, **Then** I see configuration status for Chapter 2 runtime settings (even if values are not set)
4. **Given** I update `.env` with Chapter 2 runtime settings, **When** I restart the backend, **Then** the backend reads and validates the new configuration without errors

---

### User Story 3 - Future Developer Implements Chapter 2 Runtime Logic (Priority: P3)

As a future developer implementing real AI logic for Chapter 2, I need clear TODO placeholders, function signatures, expected input/output contracts, and architectural blueprints in all runtime modules, so I can implement AI features incrementally without architectural changes.

**Why this priority**: Important for maintainability and developer experience, but not critical for initial scaffolding. Blueprints can be refined during implementation.

**Independent Test**: Can be fully tested by reviewing all runtime module files for TODO comments, function signatures, docstrings describing expected behavior, and architectural notes explaining the flow.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I review any runtime module file, **Then** I see TODO comments explaining what needs to be implemented
2. **Given** the feature is implemented, **When** I review function signatures, **Then** I see clear input/output type hints and docstrings
3. **Given** the feature is implemented, **When** I review `backend/app/ai/runtime/engine.py`, **Then** I see placeholder flow comments explaining the routing → RAG → LLM → response formatting sequence for Chapter 2
4. **Given** the feature is implemented, **When** I review Chapter 2 subagent files, **Then** I see blueprints explaining how each agent should process ROS 2 requests and generate responses

---

### Edge Cases

- What happens when Chapter 2 runtime environment variables are not set?
  - Backend should start successfully with warnings logged, runtime should default to configured defaults
- What happens when RAG pipeline is called with chapterId=2 but Chapter 2 chunks don't exist?
  - RAG pipeline should handle gracefully, returning placeholder response or error message indicating chunks not yet implemented
- What happens when a Chapter 2 subagent file is missing?
  - Runtime engine should handle missing agents gracefully, logging errors and returning appropriate error responses
- What happens when ChatKit session manager is called for Chapter 2 before implementation?
  - Session manager should have placeholder functions that return empty sessions or mock data with Chapter 2 context
- What happens when Chapter 2 runtime is disabled via ENABLE_CHAPTER_2_RUNTIME=False?
  - Runtime engine should skip Chapter 2 routing, returning appropriate error or placeholder response

## Requirements *(mandatory)*

### Functional Requirements

#### Runtime Engine Expansion

- **FR-001**: System MUST update `backend/app/ai/runtime/engine.py`:
  - Add chapter_id=2 routing logic with placeholder comments
  - Add placeholder LLM invocation for chapter 2 with TODO markers
  - Add placeholder RAG-context consumption comments
  - Add TODO notes for future logic implementation
  - Ensure existing Chapter 1 routing remains unchanged

#### RAG Pipeline Binding

- **FR-002**: System MUST update `backend/app/ai/rag/pipeline.py`:
  - Ensure pipeline can resolve chapter_2_chunks when chapter_id=2
  - Add placeholder flow comments for Chapter 2 (embed, search, assemble context)
  - Add TODO comments for Chapter 2-specific retrieval logic
  - No real RAG logic implemented (placeholder only)

#### AI Block API Binding

- **FR-003**: System MUST update `backend/app/api/ai_blocks.py`:
  - Ensure all block types route to `run_ai_block(block_type, chapter_id=2)` for Chapter 2 requests
  - Verify chapterId parameter accepts value 2
  - Add comments indicating Chapter 2 support (no logic changes needed if routing is generic)
  - All 4 endpoints (ask-question, explain-like-10, quiz, diagram) must support chapterId=2

#### Subagents for Chapter 2

- **FR-004**: System MUST create Chapter 2-specific subagent files:
  - `backend/app/ai/subagents/ch2_ask_question_agent.py` - TODO blueprint for Chapter 2 question-answering
  - `backend/app/ai/subagents/ch2_explain_el10_agent.py` - TODO blueprint for Chapter 2 simplified explanation
  - `backend/app/ai/subagents/ch2_quiz_agent.py` - TODO blueprint for Chapter 2 quiz generation
  - `backend/app/ai/subagents/ch2_diagram_agent.py` - TODO blueprint for Chapter 2 diagram generation
- **FR-005**: Each Chapter 2 subagent file MUST include:
  - Input/output signatures with type hints
  - TODO placeholders explaining future implementation
  - ROS 2-specific context documentation
  - No business logic (scaffolding only)

#### Reusable Skills Integration

- **FR-006**: System MUST update `backend/app/ai/skills/` files:
  - `retrieval_skill.py` - Add TODO: chapter-aware retrieval for Chapter 2
  - `formatting_skill.py` - Add TODO: formatting rules for Chapter 2 responses
  - `prompt_builder_skill.py` - Add TODO: chapter-aware prompt builder for Chapter 2
  - `quiz_formatting_skill.py` - Add TODO: Chapter 2 quiz formatting rules
  - `diagram_skill.py` - Add TODO: Chapter 2 diagram generation rules
- **FR-007**: Each skill file MUST include:
  - TODO comments for Chapter 2 integration
  - Documentation of Chapter 2-specific considerations
  - No business logic changes (scaffolding only)

#### ChatKit Integration Scaffold

- **FR-008**: System MUST update `backend/app/ai/chatkit/session_manager.py`:
  - Add placeholder for multi-chapter session contexts
  - Add TODO comments for Chapter 2 session handling
  - Document how sessions will track Chapter 2 context
  - No real implementation (placeholder only)

- **FR-009**: System MUST update `backend/app/ai/chatkit/tools.py`:
  - Add tool definitions for Chapter 2 blocks (ask-question, explain-like-10, quiz, diagram)
  - Document Chapter 2 tool schemas
  - Add TODO comments for Chapter 2 tool implementation
  - No real implementation (placeholder only)

#### Config Updates

- **FR-010**: System MUST update `backend/app/config/settings.py`:
  - Add `DEFAULT_CH2_MODEL` setting (default LLM model for Chapter 2)
  - Add `DEFAULT_CH2_EMBEDDINGS` setting (default embedding model for Chapter 2)
  - Add `ENABLE_CHAPTER_2_RUNTIME` setting (boolean flag to enable/disable Chapter 2 runtime)
  - All settings must read from environment variables with defaults

- **FR-011**: System MUST update `.env.example`:
  - Add `DEFAULT_CH2_MODEL="gpt-4o"` with description
  - Add `DEFAULT_CH2_EMBEDDINGS="text-embedding-3-small"` with description
  - Add `ENABLE_CHAPTER_2_RUNTIME=True` with description
  - All variables must have clear descriptions

#### Contracts

- **FR-012**: System MUST create `specs/013-chapter-2-runtime-engine/contracts/runtime-flow.yaml`:
  - Define runtime flow contract for Chapter 2
  - Include routing, RAG binding, LLM invocation flow
  - Document Chapter 2-specific flow patterns

- **FR-013**: System MUST create `specs/013-chapter-2-runtime-engine/contracts/chapter-2-blocks.yaml`:
  - Define Chapter 2 AI block contracts
  - Include request/response schemas for all 4 block types
  - Document Chapter 2-specific parameters and context

### Assumptions

- **Assumption 1**: Runtime engine (`engine.py`) already exists from Feature 005 with Chapter 1 routing
- **Assumption 2**: RAG pipeline (`pipeline.py`) already has Chapter 2 flow comments from Feature 012
- **Assumption 3**: AI blocks API (`ai_blocks.py`) already supports chapterId parameter from Feature 011
- **Assumption 4**: Skills files already exist from Feature 005
- **Assumption 5**: ChatKit files already exist from Feature 005
- **Assumption 6**: Chapter 2 chunks file exists from Feature 011
- **Assumption 7**: No real AI logic needs to be implemented (only scaffolding and TODO placeholders)
- **Assumption 8**: Chapter 2 subagents will reuse patterns from Chapter 1 subagents but with ROS 2 context

### Key Entities

**Chapter 2 Runtime Engine Routing**:
- Function: `run_ai_block(block_type, request_data)` with chapter_id=2 routing
- Routing logic: Placeholder comments for Chapter 2 → subagent mapping
- RAG integration: Placeholder comments for RAG context consumption
- LLM invocation: Placeholder comments for Chapter 2 LLM calls

**Chapter 2 Subagents**:
- `ch2_ask_question_agent.py` - ROS 2 question-answering agent blueprint
- `ch2_explain_el10_agent.py` - ROS 2 simplified explanation agent blueprint
- `ch2_quiz_agent.py` - ROS 2 quiz generation agent blueprint
- `ch2_diagram_agent.py` - ROS 2 diagram generation agent blueprint

**Chapter 2 Skills Integration**:
- Chapter-aware prompt builder for ROS 2 concepts
- Chapter 2 formatting rules for responses
- Chapter 2 retrieval context handling

**Chapter 2 ChatKit Integration**:
- Multi-chapter session context tracking
- Chapter 2 tool definitions (ask-question, explain-like-10, quiz, diagram)

## Out of Scope

- Real LLM API calls (only placeholder comments)
- Real RAG pipeline execution (only placeholder flow comments)
- Real ChatKit integration (only placeholder tool definitions)
- Real session management (only placeholder functions)
- Chapter 2 content extraction (handled by Feature 010)
- Chapter 2 RAG implementation (handled by Feature 012)

## Success Criteria

- ✅ Runtime engine can route chapter 2 requests
- ✅ All subagents + skills scaffolding exists
- ✅ ChatKit placeholder integration exists
- ✅ No real AI logic or real RAG logic implemented
- ✅ Backend starts without errors

## Acceptance Criteria

- Runtime engine can route chapter 2 requests
- All subagents + skills scaffolding exists
- ChatKit placeholder integration exists
- No real AI logic or real RAG logic implemented
- Backend starts without errors
