# Data Model: Global LLM Guardrails

**Feature**: 047-global-llm-guardrails
**Date**: 2025-01-27
**Purpose**: Define data structures and entities for safety middleware

## Entity Definitions

### 1. Guardrail Rules (Configuration Entity)

**Description**: Defines safety rules and content filters

**Storage**: `specs/047-global-llm-guardrails/contracts/llm-guardrails.yaml`

**Structure**:
```yaml
GuardrailRules:
  content_rules:
    allowed_content: List[str]
    disallowed_content: List[str]
  age_appropriateness:
    target_age: int
    reading_level: str
    complexity_rules: Dict[str, Any]
  tone_rules:
    required: List[str]
    prohibited: List[str]
  hallucination_rules:
    confidence_threshold: float
    citation_required: bool
    detection_rules: List[str]
  fallback_strategies: Dict[str, Dict[str, Any]]
```

---

### 2. Safety Processing Result (Data Transfer Object)

**Description**: Result of safety processing operations

**Structure**:
```python
SafetyProcessingResult = {
    "is_safe": bool,
    "sanitized_content": str,
    "triggered_rules": List[str],
    "action": str,  # "allow" | "block" | "sanitize" | "fallback"
    "fallback_message": Optional[str],
    "details": Dict[str, Any]
}
```

---

### 3. Prompt Policy (Configuration Entity)

**Description**: Defines prompt governance rules for block types

**Storage**: `backend/app/ai/prompt/policy.py`

**Structure**:
```python
PromptPolicy = {
    "tone": str,  # "educational" | "safe" | "non-political"
    "explanation_style": str,  # "simple" | "clear" | "age-appropriate"
    "scaffolded_learning": bool,
    "error_messages": Dict[str, str],
    "safety_reminders": List[str],
    "block_specific_rules": Dict[str, Dict[str, Any]]
}
```

---

### 4. Hallucination Detection Result (Data Transfer Object)

**Description**: Result of hallucination detection

**Structure**:
```python
HallucinationDetectionResult = {
    "is_low_confidence": bool,
    "requires_citations": bool,
    "confidence_score": float,
    "detected_issues": List[str],
    "recommended_action": str,  # "allow" | "require_citations" | "fallback"
    "fallback_explanation": Optional[str]
}
```

---

### 5. Safety Log Entry (Data Transfer Object)

**Description**: Log entry for safety events

**Storage**: Logged via `safety_logger.py` (future: persistent storage)

**Structure**:
```python
SafetyLogEntry = {
    "timestamp": str,  # ISO 8601
    "event_type": str,  # "rule_triggered" | "content_blocked" | "override"
    "rule_name": Optional[str],
    "block_type": str,
    "chapter_id": int,
    "details": Dict[str, Any],
    "user_input_snippet": Optional[str],  # Sanitized, no PII
    "response_snippet": Optional[str]  # Sanitized
}
```

---

### 6. Safety Prefix/Suffix (Data Transfer Object)

**Description**: Safety instructions injected into prompts

**Structure**:
```python
SafetyInstructions = {
    "prefix": str,  # Safety prefix text
    "suffix": str,  # Safety suffix text
    "block_type": str,
    "chapter_id": int,
    "customizations": Dict[str, Any]  # Block-specific customizations
}
```

---

## Relationships

### Guardrail Engine → Rules
- Engine loads rules from contract YAML
- Rules are applied during input/output processing
- Rules can be customized per block type

### Runtime Engine → Guardrail Engine
- Runtime engine calls guardrail functions
- Guardrail engine processes input/output
- Results are used to modify LLM calls

### Prompt Governance → LLM Provider
- Prompt policy generates safety instructions
- Safety instructions are injected into prompts
- LLM provider receives enhanced prompts

### Hallucination Filter → Output
- Filter analyzes LLM output
- Detects low confidence or missing citations
- Triggers fallback if needed

### Safety Logger → Events
- Logger records all safety events
- Events are structured for analysis
- No sensitive user data is logged

---

## Data Flow

### Input Safety Flow
```
User Input
  ↓
process_input_safely()
  ↓
Check against disallowed_content rules
  ↓
Strip disallowed content
  ↓
Return SafetyProcessingResult
  ↓
If safe: Continue to LLM
  If blocked: Return fallback message
```

### Output Safety Flow
```
LLM Response
  ↓
enforce_output_rules()
  ↓
Check against allowed/disallowed_content rules
  ↓
Check hallucination_filter()
  ↓
Strip disallowed content
  ↓
Return SafetyProcessingResult
  ↓
If safe: Return to user
  If blocked: Return fallback message
```

### Prompt Enhancement Flow
```
Base Prompt
  ↓
inject_safety_prefix()
  ↓
Enhanced Prompt (with safety prefix)
  ↓
inject_safety_suffix()
  ↓
Final Prompt (with prefix + suffix)
  ↓
Send to LLM Provider
```

### Hallucination Detection Flow
```
LLM Response
  ↓
detect_low_confidence()
  ↓
require_citation_for_facts()
  ↓
HallucinationDetectionResult
  ↓
If issues detected: fallback_to_neutral_explanation()
  If safe: Return original response
```

---

## Notes

- All safety processing is synchronous (for now)
- Safety logs are structured for future analysis
- Fallback messages are educational and helpful
- Guardrails are applied consistently across all chapters

