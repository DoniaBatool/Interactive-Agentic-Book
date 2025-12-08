# Quickstart Guide: Global AI Block Standardization

**Feature**: 046-ai-block-global-standardization
**Branch**: `046-ai-block-global-standardization`
**Estimated Time**: 3-4 hours (scaffolding only)

## Prerequisites

Before starting implementation, ensure you have:

- [x] Feature 045 (System Integration Phase 2) completed
- [x] Feature 044 (System Integration Phase 1) completed
- [x] Feature 041 (Chapter 3 Subagents + Skills) completed
- [x] Git branch `046-ai-block-global-standardization` checked out
- [x] Read `specs/046-ai-block-global-standardization/spec.md`
- [x] Read `specs/046-ai-block-global-standardization/plan.md`
- [x] Read `specs/046-ai-block-global-standardization/tasks.md`

## Implementation Overview

**Total Steps**: 8 phases
**Primary Deliverable**: Unified AI block architecture with global contract, registry, and formatter
**Validation**: All chapters use identical interfaces, subagents registered, skills unified

---

## Phase 1: Global Contract (15 minutes)

### Step 1.1: Create Contract File

**File**: `specs/046-ai-block-global-standardization/contracts/ai-blocks.yaml`

**Action**: Create YAML contract with:
- All 4 AI block types (ask-question, explain-like-el10, interactive-quiz, diagram-generator)
- Input/output schemas
- Error formats
- RAG context usage rules

---

## Phase 2: Subagent Registry (20 minutes)

### Step 2.1: Create Registry File

**File**: `backend/app/ai/subagents/registry.py`

**Action**: Create registry with:
- `SUBAGENT_REGISTRY` dictionary
- `register_subagent()` function
- `get_subagent()` function
- `list_registered_subagents()` function
- Auto-register existing subagents for chapters 1, 2, 3

---

## Phase 3: Global Runtime Router (30 minutes)

### Step 3.1: Update Runtime Engine

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Add `ai_block_router()` function:
- Extract query from user_input based on block_type
- Call unified RAG pipeline
- Select subagent from registry
- Call subagent with standardized request_data and context
- Format response using unified formatter

---

## Phase 4: Unified Output Formatter (25 minutes)

### Step 4.1: Create Output Formatter

**File**: `backend/app/ai/runtime/output_formatter.py`

**Action**: Create formatter with:
- `format_ai_block_response()` function
- Standardized formats for all 4 block types
- Chapter override support (placeholder)

---

## Phase 5: Skills Upgrade (30 minutes)

### Step 5.1: Update Retrieval Skill

**File**: `backend/app/ai/skills/retrieval_skill.py`

**Action**: Ensure unified chapter support:
- Remove chapter-specific logic
- Use unified RAG pipeline
- Add TODO comments

### Step 5.2: Update Formatting Skill

**File**: `backend/app/ai/skills/formatting_skill.py`

**Action**: Ensure unified output:
- Remove chapter-specific formatting
- Use unified output formatter
- Add TODO comments

### Step 5.3: Update Prompt Builder Skill

**File**: `backend/app/ai/skills/prompt_builder_skill.py`

**Action**: Ensure unified prompt building:
- Support all chapters via chapter_id
- Apply chapter overrides if present
- Remove chapter-specific templates

---

## Phase 6: Chapter Overrides (20 minutes)

### Step 6.1: Create Override Directory

**Directory**: `backend/app/content/overrides/`

**Action**: Create directory and template:
- `__init__.py`
- `chapter_1.py` (template)
- `chapter_2.py` (template)
- `chapter_3.py` (template)

### Step 6.2: Update Runtime to Load Overrides

**File**: `backend/app/ai/runtime/engine.py`

**Action**: Add override loading logic:
- Load chapter override if present
- Apply overrides in prompt builder and formatter
- Ensure overrides don't break contract

---

## Phase 7: API Layer Update (20 minutes)

### Step 7.1: Update API Endpoints

**File**: `backend/app/api/ai_blocks.py`

**Action**: Update all endpoints:
- Call `ai_block_router()` instead of chapter-specific logic
- Use unified request/response structures
- Add validation using global contract

---

## Phase 8: Documentation (15 minutes)

### Step 8.1: Create README

**File**: `specs/046-ai-block-global-standardization/README.md`

**Action**: Write documentation:
- Explain unified architecture
- Explain override system
- Explain global contract
- Provide examples

---

## Validation Checklist

After implementation, verify:

- [ ] All chapters use identical AI block interfaces
- [ ] Subagent registry works for all chapters
- [ ] Skills support all chapters
- [ ] Output formatter produces identical structures
- [ ] Chapter overrides work (if implemented)
- [ ] API endpoints use unified router
- [ ] Documentation complete
- [ ] No broken imports
- [ ] All tests pass (if any)

---

## Next Steps

After completing scaffolding:

1. Test with real AI blocks across all chapters
2. Verify identical response structures
3. Test chapter override system
4. Add new chapter to verify scalability
5. Update frontend to use unified structures

---

## Troubleshooting

**Issue**: Subagent not found
- **Solution**: Ensure subagent is registered in registry.py

**Issue**: Response structure differs between chapters
- **Solution**: Ensure output_formatter.py is used for all chapters

**Issue**: Override not applying
- **Solution**: Check override file exists and is loaded correctly

