# Global LLM Guardrails & Prompt Governance

**Feature**: 047-global-llm-guardrails
**Created**: 2025-01-27
**Status**: Implementation Complete (Scaffolding)

## Overview

This feature introduces a unified safety middleware for all LLM calls across Chapters 1, 2, and 3. It includes guardrail engine, prompt governance, hallucination filtering, and safety logging to ensure educational, age-appropriate, and safe AI responses.

## Architecture

### Safety Flow

```
User Input
  ↓
process_input_safely() [Guardrails]
  ├─► Check disallowed_content rules
  ├─► Strip inappropriate content
  └─► Return sanitized input or error
  ↓
inject_safety_prefix() + inject_safety_suffix() [Prompt Governance]
  ↓
Enhanced Prompt (with safety instructions)
  ↓
LLM Provider Call
  ↓
LLM Response
  ↓
enforce_output_rules() [Guardrails]
  ├─► Check allowed/disallowed_content rules
  ├─► Strip inappropriate content
  └─► Return sanitized output or fallback
  ↓
detect_low_confidence() [Hallucination Filter]
  ├─► Check confidence score
  ├─► Check citation requirements
  └─► Trigger fallback if needed
  ↓
Safe, Educational Response
```

### Guardrail Engine

**Location**: `backend/app/ai/guardrails/engine.py`

**Functions**:
- `process_input_safely()`: Validates and sanitizes user input
- `enforce_output_rules()`: Validates and sanitizes LLM output
- `strip_disallowed_content()`: Removes inappropriate content
- `inject_safety_prefix()`: Adds safety instructions to prompt start
- `inject_safety_suffix()`: Adds safety reminders to prompt end

### Prompt Governance

**Location**: `backend/app/ai/prompt/policy.py`

**Policy Components**:
- Tone rules (educational, safe, non-political)
- Explanation style (simple, clear, age-appropriate)
- Scaffolded learning (progressive complexity)
- Error messages (helpful, educational)
- Safety reminders (cite sources, fact-check)

**Block-Specific Rules**:
- `ask-question`: Always cite sources, acknowledge uncertainty
- `explain-like-el10`: Use simple language, many analogies
- `interactive-quiz`: Age-appropriate questions, clear explanations
- `diagram-generator`: Educational diagrams, clear descriptions

### Hallucination Filter

**Location**: `backend/app/ai/guardrails/hallucination_filter.py`

**Detection Methods**:
- Confidence scoring (check if below threshold)
- Citation checking (require citations for factual claims)
- Context validation (check if contradicts RAG context)
- Uncertainty detection (check if LLM acknowledges uncertainty)

**Fallback Strategies**:
- Low confidence: Acknowledge uncertainty, provide general explanation
- Missing citations: Request citations or provide neutral explanation
- Contradiction: Provide explanation based on chapter content only

### Safety Logging

**Location**: `backend/app/ai/logging/safety_logger.py`

**Event Types**:
- Rule triggered: When a safety rule is activated
- Content blocked: When content is filtered or blocked
- Override event: When guardrails are overridden (if allowed)
- Hallucination detected: When low confidence or missing citations detected

**Privacy**:
- Do not log sensitive user data
- Sanitize input/output snippets
- Anonymize user identifiers

## Integration with Runtime

The guardrails are integrated into `ai_block_router()` in `backend/app/ai/runtime/engine.py`:

1. **Input Safety**: `process_input_safely()` before subagent call
2. **Safety Instructions**: `inject_safety_prefix()` and `inject_safety_suffix()` (via prompt builder)
3. **Output Safety**: `enforce_output_rules()` after subagent call
4. **Hallucination Check**: `detect_low_confidence()` after output enforcement

## Safety Rules

### Content Rules

**Allowed**:
- Educational content about Physical AI, Robotics, Computer Science
- Age-appropriate explanations (12+)
- Technical concepts explained simply
- Real-world examples and analogies

**Disallowed**:
- Inappropriate language or content
- Harmful or dangerous instructions
- Political content or opinions
- Discriminatory or biased content

### Age-Appropriateness (12+)

- Reading level: Grade 7-8
- Use simple language
- Avoid overly technical jargon
- Provide analogies for complex concepts
- Use real-world examples

### Tone Rules

**Required**:
- Educational
- Safe
- Non-political
- Encouraging
- Clear and concise

**Prohibited**:
- Casual or slang (excessive)
- Political opinions
- Biased language
- Discriminatory language

## Fallback Strategies

### Content Blocked
- Message: "I cannot provide that information. Please ask about educational content related to Physical AI and Robotics."
- Action: Return fallback message

### Low Confidence
- Message: "I'm not entirely certain about this. Based on the chapter content, [neutral explanation]. Please verify with additional sources."
- Action: Require citations or provide neutral explanation

### Hallucination Detected
- Message: "I want to make sure I'm accurate. Let me provide a general explanation based on what I know from the chapter content."
- Action: Fallback to neutral explanation

## Provider Integration

### OpenAI
- TODO: Use OpenAI Moderation API
- TODO: Configure content filtering
- TODO: Set safety presets

### Gemini
- TODO: Use Gemini safety settings (HARM_CATEGORY_*)
- TODO: Configure block thresholds
- TODO: Set content filtering

## Testing

### Verify Guardrail Integration
- Test that all LLM calls pass through guardrails
- Test input safety processing
- Test output safety enforcement

### Verify Prompt Governance
- Test that safety prefix/suffix are injected
- Test that prompt policy is applied

### Verify Hallucination Filter
- Test low confidence detection
- Test citation requirements
- Test fallback mechanisms

## Best Practices

1. **Always use guardrails** for all LLM calls
2. **Log safety events** for monitoring and improvement
3. **Tune rules carefully** to avoid over-filtering
4. **Provide helpful fallbacks** when content is blocked
5. **Monitor false positives** and adjust rules accordingly

## Troubleshooting

**Issue**: Guardrails blocking legitimate content
- **Solution**: Tune rules, check false positives, adjust thresholds

**Issue**: Safety logging not working
- **Solution**: Check logger functions are called and file exists

**Issue**: Hallucination filter too aggressive
- **Solution**: Adjust confidence thresholds, tune citation requirements

## Future Enhancements

- [ ] Real content filtering implementation
- [ ] ML-based hallucination detection
- [ ] Automated fact-checking
- [ ] User feedback integration
- [ ] Advanced safety analytics

