# Implementation Plan: Global LLM Guardrails & Prompt Governance

**Branch**: `047-global-llm-guardrails` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature introduces a unified safety middleware for all LLM calls across Chapters 1, 2, and 3. It includes guardrail engine, prompt governance, hallucination filtering, and safety logging. **All implementations are scaffolding only**—no real safety logic, just structure for future implementation.

**Primary Deliverable**: Unified safety middleware with guardrails, prompt governance, hallucination filtering, and safety logging
**Validation**: All LLM calls pass through guardrails, safety rules enforced, logging works (stubs)

---

## 1. Guardrail Engine Architecture

### 1.1 Flow Diagram

```
User Input
  ↓
process_input_safely()
  ├─► Check disallowed_content rules
  ├─► Strip inappropriate content
  └─► Return sanitized input or error
  ↓
inject_safety_prefix() + inject_safety_suffix()
  ↓
Enhanced Prompt (with safety instructions)
  ↓
LLM Provider Call
  ↓
LLM Response
  ↓
enforce_output_rules()
  ├─► Check allowed/disallowed_content rules
  ├─► Check hallucination_filter()
  └─► Strip inappropriate content
  ↓
Sanitized Response or Fallback
```

### 1.2 Rules Engine Structure

**Location**: `backend/app/ai/guardrails/engine.py`

**Functions**:
- `process_input_safely()`: Input validation and sanitization
- `enforce_output_rules()`: Output validation and sanitization
- `strip_disallowed_content()`: Content filtering
- `inject_safety_prefix()`: Add safety instructions to prompt start
- `inject_safety_suffix()`: Add safety reminders to prompt end

**Rules Loading**:
- Load rules from `contracts/llm-guardrails.yaml`
- Cache rules for performance
- Support block-type-specific rules

---

## 2. Prompt Governance Policy

### 2.1 Policy Structure

**Location**: `backend/app/ai/prompt/policy.py`

**Policy Components**:
- **Tone Rules**: Educational, safe, non-political
- **Explanation Style**: Simple, clear, age-appropriate
- **Scaffolded Learning**: Progressive complexity
- **Error Messages**: Helpful, educational
- **Safety Reminders**: Cite sources, fact-check

**Block-Specific Rules**:
- `ask-question`: Always cite sources, acknowledge uncertainty
- `explain-like-el10`: Use simple language, many analogies
- `interactive-quiz`: Age-appropriate questions, clear explanations
- `diagram-generator`: Educational diagrams, clear descriptions

### 2.2 Chapter-Level Overrides

**Integration with Feature 046**: Use chapter override system from Feature 046

**Override Precedence**:
1. Chapter override (if exists)
2. Block-specific rules
3. Global default rules

---

## 3. Hallucination Filter Architecture

### 3.1 Detection Strategy

**Location**: `backend/app/ai/guardrails/hallucination_filter.py`

**Detection Methods** (Placeholder):
- **Confidence Scoring**: Check if response confidence is below threshold
- **Citation Checking**: Check if factual claims have citations
- **Context Validation**: Check if response contradicts RAG context
- **Uncertainty Detection**: Check if LLM acknowledges uncertainty

### 3.2 Citation Requirement Rules

**Rules**:
- Factual claims MUST have citations
- Statistics MUST be sourced
- Technical claims MUST reference chapter content
- Historical claims MUST be cited

**Enforcement**:
- Check response for factual claims
- Require citations if claims found
- Return fallback if citations missing

### 3.3 Fallback Behavior

**Fallback Strategies**:
- **Low Confidence**: Acknowledge uncertainty, provide general explanation
- **Missing Citations**: Request citations or provide neutral explanation
- **Contradiction**: Provide explanation based on chapter content only
- **Uncertainty**: Acknowledge uncertainty, suggest verification

---

## 4. Integration with Runtime

### 4.1 Middleware Structure

**Location**: `backend/app/ai/runtime/engine.py`

**Integration Points**:
1. **Before LLM Call**:
   - `process_input_safely()` - Validate and sanitize input
   - `inject_safety_prefix()` - Add safety instructions
   - `inject_safety_suffix()` - Add safety reminders

2. **After LLM Call**:
   - `enforce_output_rules()` - Validate and sanitize output
   - `hallucination_filter.detect_low_confidence()` - Check confidence
   - `hallucination_filter.require_citation_for_facts()` - Check citations

3. **RAG Context**:
   - Pass through hallucination-check placeholder
   - Validate context relevance
   - Check context completeness

### 4.2 Updated ai_block_router() Flow

```python
async def ai_block_router(...):
    # Step 1: Process input safely
    input_result = process_input_safely(user_input, block_type, chapter_id)
    if not input_result["is_safe"]:
        return input_result["fallback_message"]
    
    # Step 2: Extract query and get RAG context
    context = await run_rag_pipeline(...)
    
    # Step 3: Inject safety instructions
    safety_prefix = inject_safety_prefix(block_type, chapter_id)
    safety_suffix = inject_safety_suffix(block_type, chapter_id)
    
    # Step 4: Build prompt with safety instructions
    prompt = safety_prefix + base_prompt + safety_suffix
    
    # Step 5: Call LLM provider
    llm_response = await provider.generate(prompt, ...)
    
    # Step 6: Enforce output rules
    output_result = enforce_output_rules(llm_response["text"], block_type, chapter_id)
    if not output_result["is_safe"]:
        return output_result["fallback_message"]
    
    # Step 7: Check hallucination
    hallucination_result = detect_low_confidence(llm_response, context)
    if hallucination_result["requires_citations"]:
        # Require citations or fallback
        ...
    
    # Step 8: Format and return
    return format_ai_block_response(...)
```

---

## 5. Safety Logging Architecture

### 5.1 What Gets Logged

**Event Types**:
- **Rule Triggered**: When a safety rule is activated
- **Content Blocked**: When content is filtered or blocked
- **Override Event**: When guardrails are overridden (if allowed)
- **Hallucination Detected**: When low confidence or missing citations detected

**Log Structure**:
```python
{
    "timestamp": "2025-01-27T10:00:00Z",
    "event_type": "rule_triggered" | "content_blocked" | "override" | "hallucination",
    "rule_name": "disallowed_content",
    "block_type": "ask-question",
    "chapter_id": 1,
    "details": {...},
    "user_input_snippet": "sanitized snippet",  # No PII
    "response_snippet": "sanitized snippet"  # No PII
}
```

### 5.2 Log Usage

**Future Use Cases**:
- Monitor safety rule effectiveness
- Identify patterns in blocked content
- Improve guardrail rules
- Compliance reporting
- User feedback analysis

**Privacy Considerations**:
- Do not log sensitive user data
- Sanitize input/output snippets
- Anonymize user identifiers
- Follow privacy regulations

---

## 6. Extensibility

### 6.1 Adding New Safety Rules

**Process**:
1. Add rule to `contracts/llm-guardrails.yaml`
2. Update `engine.py` to check new rule
3. Add logging for new rule
4. Test with real content

### 6.2 Customizing for New Chapters

**Integration with Feature 046**: Use chapter override system

**Customization Points**:
- Tone rules (via chapter override)
- Complexity rules (via chapter override)
- Block-specific rules (via prompt policy)

### 6.3 Provider-Specific Safety

**Provider Hooks**:
- OpenAI: Moderation API, content filtering
- Gemini: Safety settings (HARM_CATEGORY_*)
- DeepSeek: Safety settings (if available)

**Integration**:
- Provider-level safety runs in addition to custom guardrails
- Both layers provide defense-in-depth
- Log both custom and provider-level safety events

---

## 7. File Structure

```
backend/app/
├── ai/
│   ├── guardrails/
│   │   ├── __init__.py
│   │   ├── engine.py (guardrail engine)
│   │   └── hallucination_filter.py (hallucination detection)
│   ├── prompt/
│   │   ├── __init__.py
│   │   └── policy.py (prompt governance)
│   ├── logging/
│   │   ├── __init__.py
│   │   └── safety_logger.py (safety logging)
│   ├── runtime/
│   │   └── engine.py (updated: guardrail integration)
│   └── providers/
│       ├── openai_provider.py (updated: safety hooks)
│       ├── gemini_provider.py (updated: safety hooks)
│       └── base_llm.py (updated: safety interface)
└── ...

specs/047-global-llm-guardrails/
├── contracts/
│   └── llm-guardrails.yaml (safety rules contract)
└── README.md (documentation)
```

---

## 8. Risk Analysis

### 8.1 Top Risks

**Risk 1: Over-Filtering**
- **Blast Radius**: All AI block responses
- **Mitigation**: Tune rules carefully, use fallbacks, allow overrides
- **Kill Switch**: Disable guardrails if needed

**Risk 2: Performance Impact**
- **Blast Radius**: All LLM calls
- **Mitigation**: Efficient filtering, async processing, caching
- **Kill Switch**: Bypass guardrails for performance-critical paths

**Risk 3: False Positives**
- **Blast Radius**: Legitimate content blocked
- **Mitigation**: Careful rule tuning, fallback messages, user feedback
- **Kill Switch**: Override system for edge cases

### 8.2 Mitigation Strategies

- **Gradual Rollout**: Enable guardrails incrementally
- **Monitoring**: Track rule effectiveness and false positives
- **Tuning**: Adjust rules based on real-world usage
- **Fallbacks**: Always provide helpful fallback messages

---

## 9. Evaluation and Validation

### 9.1 Definition of Done

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

### 9.2 Validation Criteria

- **Guardrail Integration**: All LLM calls use guardrails
- **Rule Enforcement**: Safety rules are checked (placeholder)
- **Logging**: Safety events are logged (stubs)
- **Fallbacks**: Fallback messages are returned when needed
- **Performance**: Guardrails add < 100ms latency

---

## 10. Architectural Decision Record (ADR)

**Decision**: Multi-layer safety approach (input + output + provider-level)
**Rationale**: Defense-in-depth provides better safety coverage
**Alternatives Considered**: Single-layer filtering, provider-only safety
**Trade-offs**: More complexity but better safety coverage

**Decision**: Placeholder implementation for real safety logic
**Rationale**: Allows architecture to be established before implementing complex filtering
**Alternatives Considered**: Full implementation, no guardrails
**Trade-offs**: Architecture ready but logic needs future implementation

