# Feature Specification: Global LLM Safety, Guardrails & Prompt Governance Layer

**Feature Branch**: `047-global-llm-guardrails`
**Created**: 2025-01-27
**Status**: Draft
**Type**: ai-governance
**Input**: User description: "Introduce a unified, global safety middleware for all LLM calls across Chapters 1, 2, and 3. Standardize tone, age-appropriate content, hallucination prevention, fact-checking placeholders, and prompt governance. Ensure all AI Blocks route through a shared compliance layer before LLM output."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Safe AI Responses (Priority: P1)

As a user, I need all AI responses to be safe, age-appropriate, and educational, so I can trust the content and learn effectively without exposure to inappropriate material.

**Why this priority**: Safety is critical for educational content, especially for younger audiences. Without guardrails, LLM responses may contain inappropriate content, hallucinations, or incorrect information.

**Independent Test**: Can be fully tested by verifying that guardrails intercept and filter inappropriate content, enforce age-appropriate rules, and log safety events.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** I ask a question that might trigger inappropriate content, **Then** the guardrails filter it and return a safe fallback response

2. **Given** the feature is implemented, **When** I receive an AI response, **Then** it is age-appropriate (12+) and educational in tone

3. **Given** the feature is implemented, **When** the LLM generates a response with low confidence, **Then** the hallucination filter flags it and requires citations

4. **Given** the feature is implemented, **When** a safety rule is triggered, **Then** it is logged for monitoring and review

---

### User Story 2 - Consistent Prompt Governance (Priority: P1)

As a developer, I need all AI blocks to follow consistent prompt governance rules, so I can ensure educational quality and safety across all chapters without duplicating safety logic.

**Why this priority**: Without unified governance, each chapter might implement safety differently, leading to inconsistencies and potential gaps.

**Independent Test**: Can be fully tested by verifying that all AI blocks use the same prompt governance rules and safety middleware.

**Acceptance Scenarios**:

1. **Given** the feature is implemented, **When** any AI block generates a response, **Then** it follows the same prompt governance rules

2. **Given** the feature is implemented, **When** I add a new chapter, **Then** it automatically uses the global guardrail system

3. **Given** the feature is implemented, **When** I modify prompt governance rules, **Then** all chapters are affected consistently

---

### Edge Cases

- What happens when guardrails block all content?
  - **Expected**: Return safe fallback message indicating content filtering
- What happens when hallucination filter detects low confidence?
  - **Expected**: Require citations or return neutral explanation
- What happens when safety logging fails?
  - **Expected**: Continue processing but log error separately
- What happens when provider has native safety settings?
  - **Expected**: Use provider settings in addition to custom guardrails

## Requirements *(mandatory)*

### Functional Requirements

#### FR-001: Global Guardrail Contract

- **FR-001.1**: System MUST create `specs/047-global-llm-guardrails/contracts/llm-guardrails.yaml`:
  - Define allowed content rules (educational, age-appropriate)
  - Define disallowed content rules (inappropriate, harmful, political)
  - Define age-appropriate rules (12+)
  - Define tone rules (educational, safe, non-political)
  - Define complexity rules (reading level, technical depth)
  - Define hallucination rules (confidence thresholds, citation requirements)
  - Define fallback strategies (what to return when content is blocked)

#### FR-002: Guardrail Engine

- **FR-002.1**: System MUST create `backend/app/ai/guardrails/engine.py`:
  - Implement `process_input_safely(input_text: str, block_type: str, chapter_id: int) -> Dict[str, Any]`:
    - Check input against disallowed content rules
    - Strip disallowed content
    - Return sanitized input or error
  - Implement `enforce_output_rules(output_text: str, block_type: str, chapter_id: int) -> Dict[str, Any]`:
    - Check output against allowed/disallowed content rules
    - Strip disallowed content
    - Return sanitized output or fallback
  - Implement `inject_safety_prefix(block_type: str, chapter_id: int) -> str`:
    - Generate safety prefix for LLM prompts
    - Include age-appropriate, educational tone instructions
  - Implement `inject_safety_suffix(block_type: str, chapter_id: int) -> str`:
    - Generate safety suffix for LLM prompts
    - Include fact-checking and citation requirements

#### FR-003: Prompt Governance Layer

- **FR-003.1**: System MUST create `backend/app/ai/prompt/policy.py`:
  - Implement `define_prompt_policy(block_type: str, chapter_id: int) -> Dict[str, Any]`:
    - Return policy with:
      - Tone rules (educational, safe, non-political)
      - Explanation style (simple, clear, age-appropriate)
      - Scaffolded learning (progressive complexity)
      - Error messages (helpful, educational)
      - Safety reminders (cite sources, fact-check)

#### FR-004: Integration with Runtime Engine

- **FR-004.1**: System MUST update `backend/app/ai/runtime/engine.py`:
  - `ai_block_router()` MUST call guardrail engine before LLM provider:
    1. Process input safely: `process_input_safely()`
    2. Inject safety prefix/suffix: `inject_safety_prefix()`, `inject_safety_suffix()`
    3. Call LLM provider
    4. Enforce output rules: `enforce_output_rules()`
  - RAG context MUST pass through hallucination-check placeholder

#### FR-005: Global Hallucination Prevention

- **FR-005.1**: System MUST create `backend/app/ai/guardrails/hallucination_filter.py`:
  - Implement `detect_low_confidence(response: Dict[str, Any], context: Dict[str, Any]) -> bool`:
    - Check if response confidence is below threshold
    - Check if response lacks citations when required
    - Return True if low confidence detected
  - Implement `require_citation_for_facts(response_text: str) -> bool`:
    - Check if response contains factual claims
    - Return True if citations required
  - Implement `fallback_to_neutral_explanation(original_response: str) -> str`:
    - Generate neutral, safe explanation
    - Indicate uncertainty when appropriate

#### FR-006: Safety Logging

- **FR-006.1**: System MUST create `backend/app/ai/logging/safety_logger.py`:
  - Implement `record_triggered_rules(rule_name: str, block_type: str, chapter_id: int, details: Dict[str, Any]) -> None`:
    - Log when safety rules are triggered
    - Include rule name, block type, chapter, and details
  - Implement `record_blocking_events(content: str, reason: str, block_type: str) -> None`:
    - Log when content is blocked
    - Include content snippet, reason, and block type
  - Implement `record_override_events(override_reason: str, details: Dict[str, Any]) -> None`:
    - Log when guardrails are overridden (if allowed)
    - Include reason and details

#### FR-007: Provider-Level Safety Hooks

- **FR-007.1**: System MUST update `backend/app/ai/providers/openai_provider.py`:
  - Add TODO placeholder for native safety settings:
    - Content filtering
    - Moderation API integration
    - Safety preset configuration

- **FR-007.2**: System MUST update `backend/app/ai/providers/gemini_provider.py`:
  - Add TODO placeholder for native safety settings:
    - Safety settings (HARM_CATEGORY_*)
    - Content filtering
    - Block threshold configuration

- **FR-007.3**: System MUST update `backend/app/ai/providers/base_llm.py`:
  - Add TODO placeholder for provider-level safety interface

#### FR-008: Documentation

- **FR-008.1**: System MUST create `specs/047-global-llm-guardrails/README.md`:
  - Describe safety architecture
  - Diagram of LLM → RAG → Guardrails → Output flow
  - Explain guardrail rules and policies
  - Document safety logging
  - Provide best practices

## Non-Functional Requirements

### NFR-001: Performance
- Guardrail processing must add < 100ms latency
- Safety logging must not block request processing

### NFR-002: Reliability
- Guardrails must not break existing functionality
- Fallback mechanisms must always work

### NFR-003: Security
- Safety logs must not contain sensitive user data
- Guardrail rules must be tamper-resistant

## Acceptance Criteria

- [ ] Runtime engine passes ALL LLM inputs & outputs through guardrails
- [ ] All AI blocks obey global prompt governance rules
- [ ] Hallucination filter integrated (placeholder logic only)
- [ ] Safety logging works (stub only)
- [ ] Provider files updated with safety hooks (TODO placeholders)
- [ ] Spec + plan + tasks + contracts generated correctly
- [ ] Documentation explains safety architecture

## Success Message

Global LLM Guardrails + Prompt Governance Layer successfully scaffolded. All chapters and AI blocks now share a unified educational-safe AI model.

