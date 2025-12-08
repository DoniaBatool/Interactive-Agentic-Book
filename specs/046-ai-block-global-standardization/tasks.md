# Task List: Global AI Block Standardization

**Feature**: 046-ai-block-global-standardization
**Created**: 2025-01-27
**Status**: Draft

## Task Groups

### 1. Contract Tasks

- [ ] **T046-001** (P1) - Create `specs/046-ai-block-global-standardization/contracts/ai-blocks.yaml`
  - Define global contract for all 4 AI block types
  - Include input/output schemas, error formats, RAG context rules
  - File: `specs/046-ai-block-global-standardization/contracts/ai-blocks.yaml`

### 2. Registry Tasks

- [ ] **T046-010** (P1) - Create `backend/app/ai/subagents/registry.py`
  - Define `SUBAGENT_REGISTRY: Dict[Tuple[str, int], Type[BaseAgent]]`
  - Implement `register_subagent(block_type, chapter_id, subagent_class)`
  - Implement `get_subagent(block_type, chapter_id)`
  - Implement `list_registered_subagents()`
  - File: `backend/app/ai/subagents/registry.py`

- [ ] **T046-011** (P1) - Auto-register existing subagents
  - Register Chapter 1 subagents (if exist)
  - Register Chapter 2 subagents
  - Register Chapter 3 subagents
  - File: `backend/app/ai/subagents/__init__.py` or individual subagent files

### 3. Runtime Router Tasks

- [ ] **T046-020** (P1) - Add `ai_block_router()` to `backend/app/ai/runtime/engine.py`
  - Function signature: `async def ai_block_router(block_type: str, chapter_id: int, user_input: Dict[str, Any]) -> Dict[str, Any]`
  - Step 1: Extract query from user_input based on block_type
  - Step 2: Call unified RAG pipeline
  - Step 3: Load chapter overrides (if exists)
  - Step 4: Get subagent from registry
  - Step 5: Call subagent with standardized request
  - Step 6: Format response using unified formatter
  - File: `backend/app/ai/runtime/engine.py`

### 4. Output Formatter Tasks

- [ ] **T046-030** (P1) - Create `backend/app/ai/runtime/output_formatter.py`
  - Implement `format_ai_block_response(block_type, raw_response, chapter_id, overrides=None)`
  - Standardize `ask-question` output: `{answer: str, sources: List[str], confidence: float}`
  - Standardize `explain-like-el10` output: `{explanation: str, analogies: List[str], examples: List[str]}`
  - Standardize `interactive-quiz` output: `{quiz_title: str, questions: List[Question]}`
  - Standardize `diagram-generator` output: `{diagram_prompt: str, diagram_type: str, description: str}`
  - Apply chapter overrides if present
  - File: `backend/app/ai/runtime/output_formatter.py`

### 5. Skills Upgrade Tasks

- [ ] **T046-040** (P1) - Update `backend/app/ai/skills/retrieval_skill.py`
  - Ensure `retrieve_content()` supports all chapters via `chapter_id` parameter
  - Remove chapter-specific logic
  - Use unified RAG pipeline
  - Add TODO comments for future optimizations
  - File: `backend/app/ai/skills/retrieval_skill.py`

- [ ] **T046-041** (P1) - Update `backend/app/ai/skills/formatting_skill.py`
  - Ensure `format_response()` uses unified output formatter
  - Remove chapter-specific formatting logic
  - Call `format_ai_block_response()` from output_formatter.py
  - File: `backend/app/ai/skills/formatting_skill.py`

- [ ] **T046-042** (P1) - Update `backend/app/ai/skills/prompt_builder_skill.py`
  - Ensure `build_prompt()` supports all chapters via `chapter_id` parameter
  - Apply chapter overrides if present
  - Remove chapter-specific prompt templates
  - File: `backend/app/ai/skills/prompt_builder_skill.py`

### 6. Override System Tasks

- [ ] **T046-050** (P2) - Create `backend/app/content/overrides/` directory
  - Create `__init__.py`
  - Create `chapter_1.py` template with `CHAPTER_OVERRIDES` structure
  - Create `chapter_2.py` template
  - Create `chapter_3.py` template
  - File: `backend/app/content/overrides/__init__.py`, `chapter_*.py`

- [ ] **T046-051** (P2) - Implement override loading function
  - Create `load_chapter_overrides(chapter_id: int) -> Optional[Dict[str, Any]]`
  - Check if override file exists
  - Import and return `CHAPTER_OVERRIDES` if exists
  - Return `None` if not found
  - File: `backend/app/ai/runtime/engine.py` or separate utility module

- [ ] **T046-052** (P2) - Apply overrides in prompt builder
  - Load overrides in `build_prompt()`
  - Apply `prompt_modifications` if present
  - Apply `tone` and `difficulty` if present
  - File: `backend/app/ai/skills/prompt_builder_skill.py`

- [ ] **T046-053** (P2) - Apply overrides in output formatter
  - Load overrides in `format_ai_block_response()`
  - Apply `formatting_style` if present
  - Ensure overrides don't break contract structure
  - File: `backend/app/ai/runtime/output_formatter.py`

### 7. API Integration Tasks

- [ ] **T046-060** (P1) - Update `backend/app/api/ai_blocks.py`
  - Update `ask_question()` endpoint to call `ai_block_router()`
  - Update `explain_like_10()` endpoint to call `ai_block_router()`
  - Update `quiz()` endpoint to call `ai_block_router()`
  - Update `diagram()` endpoint to call `ai_block_router()`
  - Remove chapter-specific endpoint logic
  - Ensure all endpoints use unified request/response structures
  - File: `backend/app/api/ai_blocks.py`

### 8. Documentation Tasks

- [ ] **T046-070** (P1) - Create `specs/046-ai-block-global-standardization/README.md`
  - Explain unified architecture
  - Explain override system (how chapters can customize)
  - Explain global contract (input/output schemas)
  - Provide examples of adding new chapters
  - Document migration path from old chapter-specific code
  - File: `specs/046-ai-block-global-standardization/README.md`

### 9. Validation Tasks

- [ ] **T046-080** (P1) - Verify all chapters use identical interfaces
  - Test ask-question endpoint for chapters 1, 2, 3
  - Verify identical response structures
  - File: Manual testing or test scripts

- [ ] **T046-081** (P1) - Verify subagent registry works
  - Test registry lookup for all registered subagents
  - Test error handling for missing subagents
  - File: Manual testing or test scripts

- [ ] **T046-082** (P1) - Verify skills support all chapters
  - Test retrieval_skill with chapters 1, 2, 3
  - Test prompt_builder_skill with chapters 1, 2, 3
  - Test formatting_skill with chapters 1, 2, 3
  - File: Manual testing or test scripts

- [ ] **T046-083** (P2) - Verify override system works (if implemented)
  - Test override loading for chapters with override files
  - Test override application in prompt builder
  - Test override application in output formatter
  - Verify overrides don't break contract
  - File: Manual testing or test scripts

---

## Implementation Notes

### Scaffolding Only
- All tasks create scaffolding/placeholders only
- No real logic changes to existing runtime behavior
- TODO comments indicate future implementation

### Priority Levels
- **P1**: Critical for feature completion
- **P2**: Optional enhancements (override system)

### File Paths
- All file paths are relative to project root
- Use exact paths as specified

### Testing
- Manual testing recommended after each task group
- Verify no breaking changes to existing functionality
- Verify all chapters work identically

---

## Task Dependencies

```
T046-001 (Contract) → T046-020 (Router) → T046-060 (API)
T046-010 (Registry) → T046-011 (Register) → T046-020 (Router)
T046-030 (Formatter) → T046-041 (Formatting Skill) → T046-020 (Router)
T046-040 (Retrieval Skill) → T046-020 (Router)
T046-042 (Prompt Builder) → T046-052 (Override in Builder) → T046-020 (Router)
T046-050 (Override Dir) → T046-051 (Override Loading) → T046-052, T046-053
T046-020 (Router) → T046-060 (API)
T046-070 (Docs) → Independent
T046-080-083 (Validation) → After all implementation tasks
```

---

## Acceptance Criteria Checklist

- [ ] Global contract created and validated
- [ ] Subagent registry created and all subagents registered
- [ ] Unified output formatter created
- [ ] Runtime engine updated with `ai_block_router()`
- [ ] Skills updated to support all chapters
- [ ] Override system created (optional)
- [ ] API endpoints updated to use unified router
- [ ] Documentation created
- [ ] All chapters produce identical response structures
- [ ] No breaking changes to existing functionality

