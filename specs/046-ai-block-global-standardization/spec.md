# Feature Specification: Global AI Block Standardization Across All Chapters

**Feature Branch**: `046-ai-block-global-standardization`
**Created**: 2025-01-27
**Status**: Draft
**Type**: runtime-consolidation
**Input**: User description: "Ensure all Chapters (1, 2, 3) use a single unified AI Block Runtime. Standardize AI block inputs, outputs, schemas, subagents, skills, and pipeline behavior across the entire project. Guarantee identical performance, formatting, and RAG-context delivery."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Unified AI Block Interface (Priority: P1)

As a user, I need all AI blocks across all chapters to have identical interfaces, formatting, and behavior, so I can have a consistent learning experience regardless of which chapter I'm studying.

**Why this priority**: Consistency is critical for user experience. Different formatting or behavior across chapters creates confusion and reduces trust in the system.

**Independent Test**: Can be fully tested by verifying that all AI block endpoints (ask-question, explain-like-10, quiz, diagram) produce identical response structures across chapters 1, 2, and 3.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I call ask-question endpoint for Chapter 1, 2, or 3, **Then** I receive responses with identical structure: `{answer: str, sources: List[str], confidence: float}`

2. **Given** the feature is implemented, **When** I call explain-like-10 endpoint for any chapter, **Then** I receive responses with identical structure: `{explanation: str, analogies: List[str], examples: List[str]}`

3. **Given** the feature is implemented, **When** I call quiz endpoint for any chapter, **Then** I receive responses with identical structure: `{quiz_title: str, questions: List[Question]}`

4. **Given** the feature is implemented, **When** I call diagram endpoint for any chapter, **Then** I receive responses with identical structure: `{diagram_prompt: str, diagram_type: str, description: str}`

5. **Given** the feature is implemented, **When** I switch between chapters while using AI blocks, **Then** the interface and behavior remain consistent

---

### User Story 2 - Developer Can Extend with New Chapters (Priority: P1)

As a developer, I need a unified registry system for AI blocks and subagents, so I can easily add new chapters without duplicating code or breaking existing functionality.

**Why this priority**: Scalability is essential. Without a unified system, adding new chapters requires duplicating code and increases maintenance burden.

**Independent Test**: Can be fully tested by verifying that new chapters can be added by simply registering subagents in the registry without modifying core runtime logic.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I add a new chapter (e.g., Chapter 4), **Then** I can register its subagents in the global registry without modifying runtime engine

2. **Given** the feature is implemented, **When** I add a new chapter, **Then** all existing AI blocks automatically work with the new chapter using the same unified interface

3. **Given** the feature is implemented, **When** I add a new chapter, **Then** I can optionally override tone/difficulty/formatting via chapter override files

---

### Edge Cases

- What happens when a chapter doesn't have a subagent registered?
  - **Expected**: Runtime engine should return a clear error message indicating missing subagent registration
- What happens when chapter override conflicts with global contract?
  - **Expected**: Chapter override should take precedence, but must still conform to base contract structure
- What happens when RAG context is empty for a chapter?
  - **Expected**: All chapters should handle empty context identically, returning appropriate fallback messages
- What happens when a new AI block type is added?
  - **Expected**: New block type must be added to global contract, and all chapters must support it or explicitly opt out

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Global AI Block Contract

- **FR-001.1**: System MUST create `specs/046-ai-block-global-standardization/contracts/ai-blocks.yaml`:
  - Define global contract for all 4 AI block types:
    - `ask-question`
    - `explain-like-el10` (note: standardized naming)
    - `interactive-quiz`
    - `diagram-generator`
  - Include for each block type:
    - Required inputs (with types and constraints)
    - Required outputs (with types and structure)
    - Error format (standardized error response structure)
    - RAG context usage rules (how context is passed and used)
    - Validation rules (input validation requirements)

#### FR-002: Global Runtime Router

- **FR-002.1**: System MUST update `backend/app/ai/runtime/engine.py`:
  - Implement `ai_block_router(block_type: str, chapter_id: int, user_input: Dict[str, Any]) -> Dict[str, Any]` function
  - Standardize RAG invocation order:
    1. Extract query from user_input based on block_type
    2. Call unified RAG pipeline with chapter_id
    3. Retrieve context
    4. Select subagent from registry
    5. Call subagent with standardized request_data and context
    6. Format response using unified formatter
  - Standardize subagent selection:
    - Use global subagent registry
    - Map block_type → subagent class
    - Handle missing subagent gracefully
  - Standardize prompt formatting:
    - Use unified prompt builder skill
    - Apply chapter-specific overrides if present
  - Standardize provider selection:
    - Use settings.default_runtime_provider
    - Allow chapter-specific provider override via settings

#### FR-003: Global Subagent Registry

- **FR-003.1**: System MUST create `backend/app/ai/subagents/registry.py`:
  - Define `SUBAGENT_REGISTRY: Dict[Tuple[str, int], Type[BaseAgent]]`:
    - Key: (block_type, chapter_id)
    - Value: Subagent class
  - Provide registration functions:
    - `register_subagent(block_type: str, chapter_id: int, subagent_class: Type[BaseAgent]) -> None`
    - `get_subagent(block_type: str, chapter_id: int) -> Optional[Type[BaseAgent]]`
    - `list_registered_subagents() -> List[Tuple[str, int]]`
  - Auto-register existing subagents for chapters 1, 2, 3
  - Ensure future chapters can auto-register via import-time registration

#### FR-004: Shared Skills Upgrade

- **FR-004.1**: System MUST update `backend/app/ai/skills/retrieval_skill.py`:
  - Ensure `retrieve_content()` supports all chapters via chapter_id parameter
  - Remove chapter-specific logic, use unified RAG pipeline
  - Add TODO comments for any chapter-specific optimizations (future)

- **FR-004.2**: System MUST update `backend/app/ai/skills/formatting_skill.py`:
  - Ensure `format_response()` produces identical output structure across chapters
  - Remove chapter-specific formatting logic
  - Use unified output formatter (see FR-005)

- **FR-004.3**: System MUST update `backend/app/ai/skills/prompt_builder_skill.py`:
  - Ensure `build_prompt()` supports all chapters via chapter_id parameter
  - Apply chapter-specific tone/difficulty via override system (see FR-006)
  - Remove chapter-specific prompt templates

#### FR-005: Unified Output Formatting

- **FR-005.1**: System MUST create `backend/app/ai/runtime/output_formatter.py`:
  - Implement `format_ai_block_response(block_type: str, raw_response: Dict[str, Any], chapter_id: int) -> Dict[str, Any]`:
    - Standardize answer blocks: `{answer: str, sources: List[str], confidence: float}`
    - Standardize diagrams: `{diagram_prompt: str, diagram_type: str, description: str}`
    - Standardize quizzes: `{quiz_title: str, questions: List[Question]}` where Question has consistent structure
    - Standardize explain-like-10: `{explanation: str, analogies: List[str], examples: List[str]}`
  - Guarantee all chapters produce identical output structure
  - Apply chapter-specific overrides if present (see FR-006)

#### FR-006: Chapter Overrides (Optional)

- **FR-006.1**: System MUST create optional override path structure:
  - Create `backend/app/content/overrides/` directory
  - Create `backend/app/content/overrides/chapter_{id}.py` template file:
    - Define override structure:
      ```python
      CHAPTER_OVERRIDES = {
          "tone": str,  # e.g., "formal", "casual", "enthusiastic"
          "difficulty": str,  # e.g., "beginner", "intermediate", "advanced"
          "formatting_style": Dict[str, Any],  # Custom formatting rules
          "prompt_modifications": Dict[str, str]  # Block-specific prompt tweaks
      }
      ```
  - Update runtime engine to load overrides if present
  - Apply overrides in prompt builder and output formatter
  - Ensure overrides don't break global contract structure

#### FR-007: API Layer Update

- **FR-007.1**: System MUST update `backend/app/api/ai_blocks.py`:
  - All endpoints MUST call the new global router: `ai_block_router()`
  - Remove chapter-specific endpoint logic
  - Ensure all endpoints use unified request/response structures
  - Add validation using global contract schemas

#### FR-008: Documentation

- **FR-008.1**: System MUST create `specs/046-ai-block-global-standardization/README.md`:
  - Explain unified architecture
  - Explain override system (how chapters can customize)
  - Explain global contract (input/output schemas)
  - Provide examples of adding new chapters
  - Document migration path from old chapter-specific code

## Non-Functional Requirements

### NFR-001: Performance
- All AI blocks must respond within acceptable latency regardless of chapter
- RAG pipeline must perform consistently across chapters

### NFR-002: Maintainability
- Adding new chapters must not require modifying core runtime logic
- Chapter-specific customizations must be isolated to override files

### NFR-003: Consistency
- All chapters must produce identical response structures
- Error handling must be consistent across chapters

## Acceptance Criteria

- [ ] All chapters use the SAME AI block interfaces
- [ ] All AI block endpoints produce identical formatting styles
- [ ] Subagents follow a single registry
- [ ] Skills do not need chapter-specific forks
- [ ] No chapter breaks the flow when switching inputs
- [ ] New chapters can be added by registering subagents only
- [ ] Chapter overrides work without breaking global contract
- [ ] API endpoints use unified router
- [ ] Documentation explains architecture and override system

## Success Message

AI Block Global Standardization complete. All chapters now share a unified, predictable, scalable AI runtime architecture.

