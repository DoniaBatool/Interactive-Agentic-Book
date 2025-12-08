# Implementation Plan: Global AI Block Standardization Across All Chapters

**Branch**: `046-ai-block-global-standardization` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature standardizes all AI blocks across Chapters 1, 2, and 3 to use a unified runtime architecture. It introduces a global contract, subagent registry, unified output formatter, and optional chapter override system. **All implementations are scaffolding only**—no real logic changes to existing runtime behavior.

**Primary Deliverable**: Unified AI block architecture with global contract, registry, formatter, and override system
**Validation**: All chapters use identical interfaces, subagents registered, skills unified, API endpoints use unified router

---

## 1. Global Contract Design

### 1.1 Input/Output Schemas

**Location**: `specs/046-ai-block-global-standardization/contracts/ai-blocks.yaml`

**Design Principles**:
- All 4 AI block types have identical input validation rules
- All block types have standardized output structures
- Error formats are consistent across all blocks
- RAG context usage rules are unified

**Input Schema Structure**:
```yaml
inputs:
  required:
    - chapterId (integer, 1-999)
    - block-specific fields (question, concept, etc.)
  optional:
    - sectionId (string, pattern: ^[a-z0-9-]+$)
    - block-specific optional fields
```

**Output Schema Structure** (varies by block_type):
- `ask-question`: `{answer: str, sources: List[str], confidence: float}`
- `explain-like-el10`: `{explanation: str, analogies: List[str], examples: List[str]}`
- `interactive-quiz`: `{quiz_title: str, questions: List[Question]}`
- `diagram-generator`: `{diagram_prompt: str, diagram_type: str, description: str}`

### 1.2 Error Handling

**Standard Error Format**:
```python
{
    "error": str,      # Human-readable message
    "code": str,       # Error code (INVALID_INPUT, RAG_CONTEXT_ERROR, etc.)
    "details": Dict    # Additional error details
}
```

**Standard Error Codes**:
- `INVALID_INPUT`: Input validation failed (HTTP 400)
- `RAG_CONTEXT_ERROR`: RAG context retrieval failed (HTTP 500)
- `SUBAGENT_NOT_FOUND`: No subagent registered (HTTP 404)
- `LLM_PROVIDER_ERROR`: LLM provider request failed (HTTP 500)
- `FORMATTING_ERROR`: Response formatting failed (HTTP 500)

### 1.3 Shared Context Window Rules

**RAG Context Rules**:
- Max chunks: 5
- Max context length: 2000 characters
- Chunk selection strategy: similarity-based
- Context assembly: sequential (chunks in order)

---

## 2. Runtime Routing Architecture

### 2.1 ai_block_router() Function

**Location**: `backend/app/ai/runtime/engine.py`

**Function Signature**:
```python
async def ai_block_router(
    block_type: str,
    chapter_id: int,
    user_input: Dict[str, Any]
) -> Dict[str, Any]:
```

**Routing Flow**:
1. **Extract Query**: Based on block_type, extract query from user_input
   - `ask-question`: `user_input.get("question")`
   - `explain-like-el10`: `user_input.get("concept")`
   - `interactive-quiz`: General query or empty
   - `diagram-generator`: Build query from diagramType and concepts

2. **RAG Pipeline**: Call unified RAG pipeline
   ```python
   context = await run_rag_pipeline(
       query=query,
       chapter_id=chapter_id,
       top_k=5,
       section_id=user_input.get("sectionId")
   )
   ```

3. **Load Overrides**: Load chapter override if exists
   ```python
   overrides = load_chapter_overrides(chapter_id)  # Returns None if not found
   ```

4. **Subagent Selection**: Get subagent from registry
   ```python
   subagent_class = get_subagent(block_type, chapter_id)
   if not subagent_class:
       return error_response("SUBAGENT_NOT_FOUND", ...)
   subagent = subagent_class()
   ```

5. **Call Subagent**: Call with standardized request
   ```python
   request_data = {
       "block_type": block_type,
       "chapterId": chapter_id,
       **user_input
   }
   result = await subagent.run(request_data, context)
   ```

6. **Format Response**: Use unified formatter
   ```python
   formatted = format_ai_block_response(block_type, result, chapter_id, overrides)
   return formatted
   ```

### 2.2 Cross-Chapter RAG Selection

**Unified RAG Pipeline**: All chapters use `run_rag_pipeline()` from `backend/app/ai/rag/pipeline.py`

**Chapter-Specific Collections**:
- Chapter 1: `settings.qdrant_collection_ch1` or `"chapter_1"`
- Chapter 2: `settings.qdrant_collection_ch2` or `"chapter_2"`
- Chapter 3: `settings.qdrant_collection_ch3` or `"chapter_3"`

**Collection Selection Logic**:
```python
collection_name = f"chapter_{chapter_id}"
if chapter_id == 1 and settings.qdrant_collection_ch1:
    collection_name = settings.qdrant_collection_ch1
# ... etc
```

---

## 3. Subagent Registry Architecture

### 3.1 Registry Design Pattern

**Location**: `backend/app/ai/subagents/registry.py`

**Registry Structure**:
```python
SUBAGENT_REGISTRY: Dict[Tuple[str, int], Type[BaseAgent]] = {}

# Key: (block_type: str, chapter_id: int)
# Value: Subagent class (Type[BaseAgent])
```

**Registration Functions**:
```python
def register_subagent(
    block_type: str,
    chapter_id: int,
    subagent_class: Type[BaseAgent]
) -> None:
    """Register a subagent for a specific block type and chapter."""
    SUBAGENT_REGISTRY[(block_type, chapter_id)] = subagent_class

def get_subagent(
    block_type: str,
    chapter_id: int
) -> Optional[Type[BaseAgent]]:
    """Get subagent class for block type and chapter."""
    return SUBAGENT_REGISTRY.get((block_type, chapter_id))

def list_registered_subagents() -> List[Tuple[str, int]]:
    """List all registered (block_type, chapter_id) pairs."""
    return list(SUBAGENT_REGISTRY.keys())
```

### 3.2 Auto-Registration Strategy

**Import-Time Registration**: Subagents auto-register when imported

**Example**:
```python
# backend/app/ai/subagents/ch3/ask_question_agent.py
from app.ai.subagents.registry import register_subagent

class Ch3AskQuestionAgent(BaseAgent):
    # ... implementation

# Auto-register on import
register_subagent("ask-question", 3, Ch3AskQuestionAgent)
```

**Manual Registration**: Alternative approach for explicit control
```python
# backend/app/ai/subagents/__init__.py
from app.ai.subagents.registry import register_subagent
from app.ai.subagents.ch3.ask_question_agent import Ch3AskQuestionAgent

# Register all Chapter 3 subagents
register_subagent("ask-question", 3, Ch3AskQuestionAgent)
# ... etc
```

### 3.3 Extensibility for Future Chapters

**Adding New Chapter**:
1. Create subagent classes in `backend/app/ai/subagents/ch{N}/`
2. Import subagents in `backend/app/ai/subagents/__init__.py`
3. Register subagents (auto or manual)
4. No changes needed to runtime engine

---

## 4. Skills Enhancement Architecture

### 4.1 Multi-Chapter Support

**Unified Skills**: All skills support all chapters via `chapter_id` parameter

**retrieval_skill.py**:
```python
async def retrieve_content(
    query: str,
    chapter_id: int,  # Supports all chapters
    top_k: int = 5,
    section_id: Optional[str] = None
) -> List[Dict[str, Any]]:
    # Use unified RAG pipeline
    rag_result = await run_rag_pipeline(query, chapter_id, top_k, section_id)
    return rag_result["chunks"]
```

**prompt_builder_skill.py**:
```python
def build_prompt(
    block_type: str,
    user_input: str,
    context: List[Dict[str, Any]],
    chapter_id: int = None  # Supports all chapters
) -> str:
    # Apply chapter override if present
    overrides = load_chapter_overrides(chapter_id)
    # Build prompt with override modifications
    # ...
```

**formatting_skill.py**:
```python
def format_response(
    raw_response: Dict[str, Any],
    block_type: str,
    chapter_id: int = None  # Supports all chapters
) -> Dict[str, Any]:
    # Use unified output formatter
    return format_ai_block_response(block_type, raw_response, chapter_id)
```

### 4.2 Formatting Unification

**Unified Output Formatter**: All formatting goes through `output_formatter.py`

**format_ai_block_response()**:
```python
def format_ai_block_response(
    block_type: str,
    raw_response: Dict[str, Any],
    chapter_id: int,
    overrides: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    # Standardize output structure based on block_type
    # Apply chapter overrides if present
    # Return standardized response
```

---

## 5. Override System Architecture

### 5.1 Tiered Fallback Model

**Precedence Order**:
1. Chapter override (if exists)
2. Global default

**Override Loading**:
```python
def load_chapter_overrides(chapter_id: int) -> Optional[Dict[str, Any]]:
    """Load chapter-specific overrides if file exists."""
    override_path = f"backend/app/content/overrides/chapter_{chapter_id}.py"
    if os.path.exists(override_path):
        # Import and return CHAPTER_OVERRIDES
        # ...
    return None
```

### 5.2 Override Structure

**Override File Template**:
```python
# backend/app/content/overrides/chapter_1.py
CHAPTER_OVERRIDES = {
    "tone": "enthusiastic",  # Override global tone
    "difficulty": "beginner",  # Override global difficulty
    "formatting_style": {
        "max_explanation_length": 500  # Custom formatting rule
    },
    "prompt_modifications": {
        "ask-question": "Use simple language and provide examples.",
        "explain-like-el10": "Use more analogies and real-world examples."
    }
}
```

### 5.3 Override Application

**Prompt Builder**: Apply override modifications
```python
def build_prompt(..., chapter_id: int, ...):
    overrides = load_chapter_overrides(chapter_id)
    if overrides and "prompt_modifications" in overrides:
        block_mod = overrides["prompt_modifications"].get(block_type)
        if block_mod:
            # Apply modification to prompt
```

**Output Formatter**: Apply override formatting
```python
def format_ai_block_response(..., overrides: Optional[Dict] = None):
    if overrides and "formatting_style" in overrides:
        # Apply formatting style overrides
```

### 5.4 Override Constraints

**Allowed Overrides**:
- `tone`: String (formal, casual, enthusiastic)
- `difficulty`: String (beginner, intermediate, advanced)
- `formatting_style`: Dict (custom formatting rules)
- `prompt_modifications`: Dict (block-specific prompt tweaks)

**Disallowed Overrides**:
- Input structure (must match global contract)
- Output structure (must match global contract)
- Error format (must match global contract)
- RAG context structure (must match global contract)

---

## 6. Migration Strategy

### 6.1 Refactoring Approach

**Phase 1: Create Infrastructure** (No breaking changes)
1. Create global contract (YAML)
2. Create subagent registry
3. Create unified output formatter
4. Create override system structure

**Phase 2: Register Existing Subagents** (No breaking changes)
1. Register Chapter 1 subagents
2. Register Chapter 2 subagents
3. Register Chapter 3 subagents
4. Verify registry works

**Phase 3: Update Runtime Engine** (Backward compatible)
1. Add `ai_block_router()` function
2. Keep existing `run_ai_block()` for backward compatibility
3. Gradually migrate endpoints to use router

**Phase 4: Update Skills** (Backward compatible)
1. Update skills to support all chapters
2. Remove chapter-specific logic
3. Use unified formatter

**Phase 5: Update API Endpoints** (Final step)
1. Update all endpoints to use `ai_block_router()`
2. Remove old chapter-specific logic
3. Verify all chapters work identically

### 6.2 Backward Compatibility

**Dual Mode**: Support both old and new approaches during migration
- Old: Direct subagent calls
- New: Registry-based routing

**Gradual Migration**: Migrate one endpoint at a time
- Test each endpoint after migration
- Rollback if issues found

---

## 7. File Structure

```
backend/app/
├── ai/
│   ├── runtime/
│   │   ├── engine.py (updated: add ai_block_router)
│   │   └── output_formatter.py (NEW)
│   ├── subagents/
│   │   ├── registry.py (NEW)
│   │   └── ... (existing subagents)
│   └── skills/
│       ├── retrieval_skill.py (updated: unified chapter support)
│       ├── formatting_skill.py (updated: use unified formatter)
│       └── prompt_builder_skill.py (updated: unified chapter support)
├── content/
│   └── overrides/ (NEW)
│       ├── __init__.py
│       ├── chapter_1.py (template)
│       ├── chapter_2.py (template)
│       └── chapter_3.py (template)
└── api/
    └── ai_blocks.py (updated: use ai_block_router)

specs/046-ai-block-global-standardization/
├── contracts/
│   └── ai-blocks.yaml (NEW)
└── README.md (NEW)
```

---

## 8. Risk Analysis

### 8.1 Top Risks

**Risk 1: Breaking Existing Functionality**
- **Blast Radius**: All AI block endpoints
- **Mitigation**: Gradual migration, backward compatibility, thorough testing
- **Kill Switch**: Revert to old code paths if issues found

**Risk 2: Registry Lookup Failures**
- **Blast Radius**: All AI block requests
- **Mitigation**: Graceful error handling, clear error messages, fallback to old approach
- **Kill Switch**: Fallback to direct subagent calls

**Risk 3: Override System Conflicts**
- **Blast Radius**: Chapter-specific customizations
- **Mitigation**: Clear override rules, validation, precedence documentation
- **Kill Switch**: Disable override loading if issues found

### 8.2 Mitigation Strategies

- **Testing**: Test each chapter after migration
- **Monitoring**: Log registry lookups and override applications
- **Rollback Plan**: Keep old code paths during migration
- **Documentation**: Clear migration guide and override rules

---

## 9. Evaluation and Validation

### 9.1 Definition of Done

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

### 9.2 Validation Criteria

- **Contract Validation**: All responses match global contract
- **Registry Validation**: All subagents registered and accessible
- **Formatting Validation**: All chapters produce identical structures
- **Override Validation**: Overrides work without breaking contract
- **API Validation**: All endpoints use unified router

---

## 10. Architectural Decision Record (ADR)

**Decision**: Use registry pattern for subagent management
**Rationale**: Enables easy extension to new chapters, reduces code duplication, provides single source of truth
**Alternatives Considered**: Direct imports, factory pattern, dependency injection
**Trade-offs**: Slight performance overhead (O(1) lookup), but provides better scalability

**Decision**: Use tiered override system
**Rationale**: Allows chapter-specific customizations while maintaining global contract
**Alternatives Considered**: No overrides (too rigid), full override (too flexible)
**Trade-offs**: Adds complexity but provides needed flexibility

