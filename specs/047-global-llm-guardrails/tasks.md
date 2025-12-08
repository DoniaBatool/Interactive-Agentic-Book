# Task List: Global LLM Guardrails & Prompt Governance

**Feature**: 047-global-llm-guardrails
**Created**: 2025-01-27
**Status**: Draft

## Task Groups

### 1. Contract Tasks

- [ ] **T047-001** (P1) - Create `specs/047-global-llm-guardrails/contracts/llm-guardrails.yaml`
  - Define content rules (allowed/disallowed)
  - Define age-appropriateness rules (12+)
  - Define tone rules (educational, safe, non-political)
  - Define complexity rules
  - Define hallucination rules
  - Define fallback strategies
  - File: `specs/047-global-llm-guardrails/contracts/llm-guardrails.yaml`

### 2. Guardrail Engine Tasks

- [ ] **T047-010** (P1) - Create `backend/app/ai/guardrails/__init__.py`
  - Create package initialization file
  - File: `backend/app/ai/guardrails/__init__.py`

- [ ] **T047-011** (P1) - Create `backend/app/ai/guardrails/engine.py`
  - Implement `process_input_safely(input_text: str, block_type: str, chapter_id: int) -> Dict[str, Any]` (placeholder)
  - Implement `enforce_output_rules(output_text: str, block_type: str, chapter_id: int) -> Dict[str, Any]` (placeholder)
  - Implement `strip_disallowed_content(content: str) -> str` (placeholder)
  - Implement `inject_safety_prefix(block_type: str, chapter_id: int) -> str` (placeholder)
  - Implement `inject_safety_suffix(block_type: str, chapter_id: int) -> str` (placeholder)
  - Add TODO comments for real implementation
  - File: `backend/app/ai/guardrails/engine.py`

### 3. Prompt Governance Tasks

- [ ] **T047-020** (P1) - Create `backend/app/ai/prompt/__init__.py`
  - Create package initialization file
  - File: `backend/app/ai/prompt/__init__.py`

- [ ] **T047-021** (P1) - Create `backend/app/ai/prompt/policy.py`
  - Implement `define_prompt_policy(block_type: str, chapter_id: int) -> Dict[str, Any]` (placeholder)
  - Define policy structure for tone, style, error messages, safety reminders
  - Add block-specific rules
  - Add TODO comments for real implementation
  - File: `backend/app/ai/prompt/policy.py`

### 4. Hallucination Filter Tasks

- [ ] **T047-030** (P1) - Create `backend/app/ai/guardrails/hallucination_filter.py`
  - Implement `detect_low_confidence(response: Dict[str, Any], context: Dict[str, Any]) -> bool` (placeholder)
  - Implement `require_citation_for_facts(response_text: str) -> bool` (placeholder)
  - Implement `fallback_to_neutral_explanation(original_response: str) -> str` (placeholder)
  - Add TODO comments for real implementation
  - File: `backend/app/ai/guardrails/hallucination_filter.py`

### 5. Safety Logging Tasks

- [ ] **T047-040** (P1) - Create `backend/app/ai/logging/__init__.py`
  - Create package initialization file
  - File: `backend/app/ai/logging/__init__.py`

- [ ] **T047-041** (P1) - Create `backend/app/ai/logging/safety_logger.py`
  - Implement `record_triggered_rules(rule_name: str, block_type: str, chapter_id: int, details: Dict[str, Any]) -> None` (placeholder)
  - Implement `record_blocking_events(content: str, reason: str, block_type: str) -> None` (placeholder)
  - Implement `record_override_events(override_reason: str, details: Dict[str, Any]) -> None` (placeholder)
  - Add TODO comments for real implementation
  - File: `backend/app/ai/logging/safety_logger.py`

### 6. Runtime Integration Tasks

- [ ] **T047-050** (P1) - Update `backend/app/ai/runtime/engine.py`
  - Import guardrail engine functions
  - Update `ai_block_router()` to call `process_input_safely()` before LLM call
  - Update `ai_block_router()` to call `inject_safety_prefix()` and `inject_safety_suffix()`
  - Update `ai_block_router()` to call `enforce_output_rules()` after LLM call
  - Update `ai_block_router()` to pass RAG context through hallucination-check placeholder
  - Add TODO comments for real implementation
  - File: `backend/app/ai/runtime/engine.py`

### 7. Provider Update Tasks

- [ ] **T047-060** (P2) - Update `backend/app/ai/providers/openai_provider.py`
  - Add TODO placeholder for OpenAI moderation API integration
  - Add TODO placeholder for content filtering
  - Add TODO placeholder for safety presets
  - File: `backend/app/ai/providers/openai_provider.py`

- [ ] **T047-061** (P2) - Update `backend/app/ai/providers/gemini_provider.py`
  - Add TODO placeholder for Gemini safety settings (HARM_CATEGORY_*)
  - Add TODO placeholder for block thresholds
  - Add TODO placeholder for content filtering
  - File: `backend/app/ai/providers/gemini_provider.py`

- [ ] **T047-062** (P2) - Update `backend/app/ai/providers/base_llm.py`
  - Add TODO placeholder for provider-level safety interface
  - Add abstract method for safety settings (optional)
  - File: `backend/app/ai/providers/base_llm.py`

### 8. Documentation Tasks

- [ ] **T047-070** (P1) - Create `specs/047-global-llm-guardrails/README.md`
  - Describe safety architecture
  - Diagram of LLM → RAG → Guardrails → Output flow
  - Explain guardrail rules and policies
  - Document safety logging
  - Provide best practices
  - File: `specs/047-global-llm-guardrails/README.md`

### 9. Validation Tasks

- [ ] **T047-080** (P1) - Verify guardrail integration
  - Test that all LLM calls pass through guardrails
  - Test input safety processing
  - Test output safety enforcement
  - File: Manual testing or test scripts

- [ ] **T047-081** (P1) - Verify prompt governance
  - Test that safety prefix/suffix are injected
  - Test that prompt policy is applied
  - File: Manual testing or test scripts

- [ ] **T047-082** (P2) - Verify hallucination filter (if implemented)
  - Test low confidence detection
  - Test citation requirements
  - Test fallback mechanisms
  - File: Manual testing or test scripts

- [ ] **T047-083** (P2) - Verify safety logging (if implemented)
  - Test that safety events are logged
  - Test that logs are structured correctly
  - File: Manual testing or test scripts

---

## Implementation Notes

### Scaffolding Only
- All tasks create scaffolding/placeholders only
- No real safety logic implementation
- TODO comments indicate future implementation

### Priority Levels
- **P1**: Critical for feature completion
- **P2**: Optional enhancements (provider hooks, advanced logging)

### File Paths
- All file paths are relative to project root
- Use exact paths as specified

### Testing
- Manual testing recommended after each task group
- Verify guardrails don't break existing functionality
- Verify all LLM calls use guardrails

---

## Task Dependencies

```
T047-001 (Contract) → T047-011 (Engine) → T047-050 (Runtime Integration)
T047-021 (Policy) → T047-011 (Engine) → T047-050 (Runtime Integration)
T047-030 (Hallucination Filter) → T047-050 (Runtime Integration)
T047-041 (Logger) → T047-011 (Engine) → T047-050 (Runtime Integration)
T047-050 (Runtime Integration) → T047-080-083 (Validation)
T047-060-062 (Provider Updates) → Independent
T047-070 (Docs) → Independent
```

---

## Acceptance Criteria Checklist

- [ ] Guardrail engine created with all functions
- [ ] Prompt governance policy created
- [ ] Hallucination filter created
- [ ] Safety logger created
- [ ] Runtime engine integrated with guardrails
- [ ] Provider files updated with safety hooks
- [ ] Documentation created
- [ ] All LLM calls pass through guardrails
- [ ] Safety rules are enforced (placeholder logic)
- [ ] Safety logging works (stubs)

