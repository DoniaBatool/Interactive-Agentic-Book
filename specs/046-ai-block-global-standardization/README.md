# Global AI Block Standardization

**Feature**: 046-ai-block-global-standardization
**Created**: 2025-01-27
**Status**: Implementation Complete (Scaffolding)

## Overview

This feature standardizes all AI blocks across Chapters 1, 2, and 3 to use a unified runtime architecture. It introduces a global contract, subagent registry, unified output formatter, and optional chapter override system.

## Architecture

### Unified Runtime Flow

```
API Endpoint
  ↓
ai_block_router(block_type, chapter_id, user_input)
  ↓
1. Extract query from user_input
  ↓
2. Call unified RAG pipeline
  ↓
3. Load chapter overrides (if exists)
  ↓
4. Get subagent from registry
  ↓
5. Call subagent with standardized request
  ↓
6. Format response using unified formatter
  ↓
Standardized Response
```

### Global Contract

All AI blocks follow the same contract defined in `contracts/ai-blocks.yaml`:

- **Input Validation**: Standardized input schemas with required/optional fields
- **Output Structure**: Identical response structures across all chapters
- **Error Format**: Consistent error handling and error codes
- **RAG Context Rules**: Unified context window and chunk selection

### Subagent Registry

The registry (`backend/app/ai/subagents/registry.py`) maps `(block_type, chapter_id)` to subagent classes:

```python
SUBAGENT_REGISTRY = {
    ("ask-question", 1): Ch1AskQuestionAgent,
    ("ask-question", 2): Ch2AskQuestionAgent,
    ("ask-question", 3): Ch3AskQuestionAgent,
    # ... etc
}
```

**Registration**:
- Auto-register on import (recommended)
- Manual registration via `register_subagent()`

**Lookup**:
- `get_subagent(block_type, chapter_id)` returns subagent class or None

### Unified Output Formatter

The output formatter (`backend/app/ai/runtime/output_formatter.py`) ensures all chapters produce identical response structures:

- `ask-question`: `{answer: str, sources: List[str], confidence: float}`
- `explain-like-el10`: `{explanation: str, analogies: List[str], examples: List[str]}`
- `interactive-quiz`: `{quiz_title: str, questions: List[Question]}`
- `diagram-generator`: `{diagram_prompt: str, diagram_type: str, description: str}`

### Chapter Override System

Optional chapter-specific customizations via `backend/app/content/overrides/chapter_{id}.py`:

```python
CHAPTER_OVERRIDES = {
    "tone": "enthusiastic",
    "difficulty": "beginner",
    "formatting_style": {
        "max_explanation_length": 500
    },
    "prompt_modifications": {
        "ask-question": "Use simple language and provide examples."
    }
}
```

**Override Rules**:
- Overrides are optional (file may not exist)
- Overrides take precedence over global defaults
- Overrides MUST NOT break base contract structure
- Cannot override input/output schemas or error format

## Adding New Chapters

### Step 1: Create Subagents

Create subagent classes in `backend/app/ai/subagents/ch{N}/`:

```python
# backend/app/ai/subagents/ch4/ask_question_agent.py
from app.ai.subagents.base_agent import BaseAgent
from app.ai.subagents.registry import register_subagent

class Ch4AskQuestionAgent(BaseAgent):
    async def run(self, request_data: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
        # Implementation
        pass

# Auto-register
register_subagent("ask-question", 4, Ch4AskQuestionAgent)
```

### Step 2: Register Subagents

Subagents auto-register on import, or manually register in `backend/app/ai/subagents/__init__.py`:

```python
from app.ai.subagents.ch4.ask_question_agent import Ch4AskQuestionAgent
register_subagent("ask-question", 4, Ch4AskQuestionAgent)
```

### Step 3: (Optional) Create Override File

Create `backend/app/content/overrides/chapter_4.py` if chapter needs customizations:

```python
CHAPTER_OVERRIDES = {
    "tone": "formal",
    "difficulty": "advanced"
}
```

### Step 4: Verify

Test that all AI blocks work for the new chapter:

```python
# All these should work automatically
result = await ai_block_router("ask-question", 4, {"question": "..."})
result = await ai_block_router("explain-like-el10", 4, {"concept": "..."})
# ... etc
```

## Migration from Old Code

### Before (Chapter-Specific)

```python
# Old approach - chapter-specific logic
if chapter_id == 1:
    result = await ch1_ask_agent.run(request)
elif chapter_id == 2:
    result = await ch2_ask_agent.run(request)
elif chapter_id == 3:
    result = await ch3_ask_agent.run(request)
```

### After (Unified)

```python
# New approach - unified router
result = await ai_block_router("ask-question", chapter_id, user_input)
```

**Benefits**:
- No conditional logic needed
- Automatic support for new chapters
- Consistent behavior across chapters
- Easier to maintain and extend

## File Structure

```
backend/app/
├── ai/
│   ├── runtime/
│   │   ├── engine.py (ai_block_router function)
│   │   └── output_formatter.py (unified formatting)
│   └── subagents/
│       ├── registry.py (subagent registry)
│       └── ... (subagent implementations)
├── content/
│   └── overrides/ (optional chapter overrides)
│       ├── chapter_1.py
│       ├── chapter_2.py
│       └── chapter_3.py
└── api/
    └── ai_blocks.py (updated to use ai_block_router)

specs/046-ai-block-global-standardization/
├── contracts/
│   └── ai-blocks.yaml (global contract)
└── README.md (this file)
```

## Testing

### Verify Identical Structures

Test that all chapters produce identical response structures:

```python
# Test ask-question for all chapters
for chapter_id in [1, 2, 3]:
    result = await ai_block_router("ask-question", chapter_id, {"question": "test"})
    assert "answer" in result
    assert "sources" in result
    assert "confidence" in result
```

### Verify Registry

Test that all subagents are registered:

```python
from app.ai.subagents.registry import list_registered_subagents
registered = list_registered_subagents()
assert ("ask-question", 1) in registered
assert ("ask-question", 2) in registered
assert ("ask-question", 3) in registered
```

### Verify Overrides

Test that overrides work (if implemented):

```python
overrides = load_chapter_overrides(1)
if overrides:
    assert "tone" in overrides or "difficulty" in overrides
```

## Best Practices

1. **Always use `ai_block_router()`** for routing AI block requests
2. **Register subagents** on import for automatic discovery
3. **Use unified formatter** for all response formatting
4. **Keep overrides minimal** - only override what's necessary
5. **Test across chapters** to ensure consistency

## Troubleshooting

**Issue**: Subagent not found
- **Solution**: Ensure subagent is registered in registry

**Issue**: Response structure differs between chapters
- **Solution**: Ensure output_formatter.py is used for all chapters

**Issue**: Override not applying
- **Solution**: Check override file exists and is loaded correctly

## Future Enhancements

- [ ] Add validation against global contract
- [ ] Add metrics for consistency monitoring
- [ ] Add automated testing for contract compliance
- [ ] Add override validation rules
- [ ] Add registry discovery mechanisms

