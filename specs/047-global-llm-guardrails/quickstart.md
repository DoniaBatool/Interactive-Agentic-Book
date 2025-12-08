# Quickstart Guide: Global LLM Guardrails

**Feature**: 047-global-llm-guardrails
**Branch**: `047-global-llm-guardrails`
**Estimated Time**: 2-3 hours (scaffolding only)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 046 (Global AI Block Standardization) completed
- [x] Feature 045 (System Integration Phase 2) completed
- [x] Git branch `047-global-llm-guardrails` checked out
- [x] Read `specs/047-global-llm-guardrails/spec.md`

## Implementation Overview

**Total Steps**: 7 phases
**Primary Deliverable**: Unified safety middleware with guardrails, prompt governance, and safety logging
**Validation**: All LLM calls pass through guardrails, safety rules enforced, logging works

---

## Phase 1: Guardrail Contract (15 minutes)

### Step 1.1: Create Contract File

**File**: `specs/047-global-llm-guardrails/contracts/llm-guardrails.yaml`

**Action**: Create YAML contract with:
- Content rules (allowed/disallowed)
- Age-appropriateness rules (12+)
- Tone rules (educational, safe, non-political)
- Complexity rules
- Hallucination rules
- Fallback strategies

---

## Phase 2: Guardrail Engine (30 minutes)

### Step 2.1: Create Engine File

**File**: `backend/app/ai/guardrails/engine.py`

**Action**: Create engine with:
- `process_input_safely()` function (placeholder)
- `enforce_output_rules()` function (placeholder)
- `inject_safety_prefix()` function (placeholder)
- `inject_safety_suffix()` function (placeholder)
- `strip_disallowed_content()` function (placeholder)

---

## Phase 3: Prompt Governance (20 minutes)

### Step 3.1: Create Policy File

**File**: `backend/app/ai/prompt/policy.py`

**Action**: Create policy module with:
- `define_prompt_policy()` function (placeholder)
- Policy structure for tone, style, error messages, safety reminders

---

## Phase 4: Hallucination Filter (20 minutes)

### Step 4.1: Create Filter File

**File**: `backend/app/ai/guardrails/hallucination_filter.py`

**Action**: Create filter with:
- `detect_low_confidence()` function (placeholder)
- `require_citation_for_facts()` function (placeholder)
- `fallback_to_neutral_explanation()` function (placeholder)

---

## Phase 5: Safety Logging (15 minutes)

### Step 5.1: Create Logger File

**File**: `backend/app/ai/logging/safety_logger.py`

**Action**: Create logger with:
- `record_triggered_rules()` function (placeholder)
- `record_blocking_events()` function (placeholder)
- `record_override_events()` function (placeholder)

---

## Phase 6: Runtime Integration (25 minutes)

### Step 6.1: Update Runtime Engine

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Update `ai_block_router()` to:
- Call `process_input_safely()` before LLM call
- Call `inject_safety_prefix()` and `inject_safety_suffix()`
- Call `enforce_output_rules()` after LLM call
- Pass RAG context through hallucination-check placeholder

---

## Phase 7: Provider Updates (15 minutes)

### Step 7.1: Update Provider Files

**Files**: 
- `backend/app/ai/providers/openai_provider.py`
- `backend/app/ai/providers/gemini_provider.py`
- `backend/app/ai/providers/base_llm.py`

**Action**: Add TODO placeholders for:
- Native safety settings
- Content filtering
- Moderation API integration

---

## Validation Checklist

After implementation, verify:

- [ ] Guardrail engine created with all functions
- [ ] Prompt governance policy created
- [ ] Hallucination filter created
- [ ] Safety logger created
- [ ] Runtime engine integrated with guardrails
- [ ] Provider files updated with safety hooks
- [ ] Documentation created
- [ ] No broken imports
- [ ] All functions have TODO placeholders

---

## Next Steps

After completing scaffolding:

1. Test guardrail integration with real LLM calls
2. Verify safety rules are enforced
3. Test fallback mechanisms
4. Verify safety logging works
5. Test with inappropriate content (should be blocked)

---

## Troubleshooting

**Issue**: Guardrails not being called
- **Solution**: Ensure runtime engine calls guardrail functions

**Issue**: Safety logging not working
- **Solution**: Check logger functions are called and file exists

**Issue**: Provider safety settings not applied
- **Solution**: Check provider files have TODO placeholders for safety settings

