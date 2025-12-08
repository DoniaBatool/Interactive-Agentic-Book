# Implementation Plan: Global Platform Stabilization & Cross-Chapter Consistency Layer

**Branch**: `056-global-stabilization` | **Date**: 2025-01-27 | **Spec**: [spec.md](spec.md)

## Summary

This feature implements complete scaffolding for global platform stabilization. It introduces unified AI block rules, multi-chapter semantic routing, collection management, global formatting layer, cross-chapter validation, and build stability checks. **All implementations are scaffolding only—no real rule enforcement, no real routing logic, no real validation.**

**Primary Deliverable**: Complete stabilization scaffolding structure
**Validation**: All stabilization modules exist, backend starts, build script exists

---

## 1. Multi-Chapter RAG Routing Design

### 1.1 Chapter Scoring Switch

**File**: `backend/app/ai/rag/pipeline.py` (update existing)

**Purpose**: Add placeholder logic for chapter scoring

**Structure**:
```python
def score_chapters_for_query(query_embedding: List[float]) -> List[Dict]:
    """
    Score all chapters for a query.
    
    TODO: Real scoring logic
    - Generate embeddings for query
    - Search all chapter collections
    - Score each chapter by relevance
    - Return sorted scores
    
    Placeholder: Return placeholder scores
    """
    # TODO: Real scoring logic
    return [
        {"chapter_id": 1, "score": 0.9},
        {"chapter_id": 2, "score": 0.7},
        {"chapter_id": 3, "score": 0.8}
    ]
```

---

### 1.2 Chapter Affinity Routing

**File**: `backend/app/ai/rag/pipeline.py` (update existing)

**Purpose**: Add placeholder logic for affinity routing

**Structure**:
```python
def route_to_best_chapter(query: str) -> int:
    """
    Route query to best matching chapter.
    
    TODO: Real routing logic
    - Score all chapters
    - Select chapter with highest score
    - Return chapter ID
    
    Placeholder: Return placeholder chapter ID
    """
    # TODO: Real routing logic
    scores = score_chapters_for_query(query_embedding)
    return scores[0]["chapter_id"]  # Placeholder
```

---

### 1.3 Fallback Retrieval

**File**: `backend/app/ai/rag/pipeline.py` (update existing)

**Purpose**: Add placeholder logic for fallback

**Structure**:
```python
def fallback_retrieval(query: str) -> List[Dict]:
    """
    Fallback retrieval if primary routing fails.
    
    TODO: Real fallback logic
    - Try all chapters
    - Return best matches across all chapters
    - Handle errors gracefully
    
    Placeholder: Return placeholder results
    """
    # TODO: Real fallback logic
    return []
```

---

## 2. Formatting Pipeline Architecture

### 2.1 Response Formatter

**File**: `backend/app/ai/formatters/response_formatter.py` (new)

**Purpose**: Unified formatting for all AI block responses

**Structure**:
```python
def format_markdown(text: str) -> str:
    """
    Format markdown consistently.
    
    TODO: Real formatting logic
    - Normalize headers
    - Normalize lists
    - Normalize code blocks
    
    Placeholder: Return text as-is
    """
    # TODO: Real formatting logic
    return text

def format_diagram(diagram_data: Dict) -> str:
    """
    Format diagram (Mermaid, PlantUML).
    
    TODO: Real formatting logic
    - Validate syntax
    - Format according to type
    - Return formatted diagram
    
    Placeholder: Return placeholder diagram
    """
    # TODO: Real formatting logic
    return "```mermaid\nplaceholder\n```"

def format_quiz(quiz_data: Dict) -> str:
    """
    Format quiz consistently.
    
    TODO: Real formatting logic
    - Format questions
    - Format answers
    - Format options
    
    Placeholder: Return placeholder quiz
    """
    # TODO: Real formatting logic
    return "Quiz placeholder"
```

---

## 3. AI Block Consistency Rules

### 3.1 AI Block Rules

**File**: `backend/app/ai/runtime/ai_block_rules.py` (new)

**Purpose**: Define rules for consistent AI block behavior

**Structure**:
```python
AI_BLOCK_RULES = {
    "formatting": {
        "markdown": {
            "header_levels": "consistent",
            "list_style": "consistent",
            "code_blocks": "consistent"
        }
    },
    "token_usage": {
        "max_tokens_per_block": 2000,
        "max_context_length": 4000,
        "normalization_strategy": "truncate"
    },
    "retry_strategy": {
        "max_retries": 3,
        "backoff_delay": 1000,
        "backoff_multiplier": 2
    },
    "context_limits": {
        "max_context_length": 4000,
        "truncation_strategy": "end"
    }
}

# TODO: Real rule enforcement logic
```

---

## 4. Cross-Chapter Content Validation Strategy

### 4.1 Chapter Consistency Validator

**File**: `backend/app/content/validation/chapter_consistency.py` (new)

**Purpose**: Validate cross-chapter consistency

**Structure**:
```python
def validate_ai_block_consistency() -> Dict:
    """
    Validate AI block consistency across chapters.
    
    TODO: Real validation logic
    - Check number of AI blocks per chapter
    - Check AI block types
    - Check AI block structure
    
    Placeholder: Return placeholder validation result
    """
    # TODO: Real validation logic
    return {
        "consistent": True,
        "issues": []
    }

def validate_section_ordering() -> Dict:
    """
    Validate section ordering consistency.
    
    TODO: Real validation logic
    - Check section order
    - Check section structure
    - Check section naming
    
    Placeholder: Return placeholder validation result
    """
    # TODO: Real validation logic
    return {
        "consistent": True,
        "issues": []
    }

def validate_glossary_structure() -> Dict:
    """
    Validate glossary structure consistency.
    
    TODO: Real validation logic
    - Check glossary format
    - Check glossary structure
    - Check glossary completeness
    
    Placeholder: Return placeholder validation result
    """
    # TODO: Real validation logic
    return {
        "consistent": True,
        "issues": []
    }
```

---

## 5. Build Stability Sequence

### 5.1 Pre-Build Check Script

**File**: `scripts/pre_build_check.py` (new)

**Purpose**: Validate build prerequisites

**Structure**:
```python
def check_mdx_presence() -> bool:
    """
    Check MDX files exist for all chapters.
    
    TODO: Real validation logic
    - Check chapter 1 MDX exists
    - Check chapter 2 MDX exists
    - Check chapter 3 MDX exists
    
    Placeholder: Return True
    """
    # TODO: Real validation logic
    return True

def check_metadata_presence() -> bool:
    """
    Check metadata exists for all chapters.
    
    TODO: Real validation logic
    - Check chapter 1 metadata
    - Check chapter 2 metadata
    - Check chapter 3 metadata
    
    Placeholder: Return True
    """
    # TODO: Real validation logic
    return True

def check_ai_block_presence() -> bool:
    """
    Check AI blocks exist for all chapters.
    
    TODO: Real validation logic
    - Check chapter 1 AI blocks
    - Check chapter 2 AI blocks
    - Check chapter 3 AI blocks
    
    Placeholder: Return True
    """
    # TODO: Real validation logic
    return True

if __name__ == "__main__":
    # Run all checks
    # TODO: Real check execution
    pass
```

---

## 6. File-by-File Implementation Order

1. `backend/app/ai/runtime/ai_block_rules.py` - AI block rules
2. `backend/app/ai/rag/collections.py` - Collection constants
3. `backend/app/ai/rag/pipeline.py` - Update with routing logic
4. `backend/app/ai/formatters/response_formatter.py` - Formatting layer
5. `backend/app/content/validation/chapter_consistency.py` - Validation
6. `scripts/pre_build_check.py` - Build checks
7. `docs/global/stabilization.md` - Documentation

---

## 7. Constraints

- **NO Real Logic**: All implementations must be placeholders
- **Scaffolding Only**: This feature creates structure, not functionality
- **NO Real Validation**: No real validation logic
- **NO Real Formatting**: No real formatting enforcement

---

## 8. Acceptance Criteria Mapping

| Acceptance Criteria | Implementation Location |
|---------------------|------------------------|
| All scaffolding files created | All files created with placeholder logic |
| No logic implemented | All functions have TODO comments only |
| Backend starts successfully | All imports resolve correctly |
| MDX validation script exists | pre_build_check.py created |
| Documentation added | stabilization.md created |

---

## 9. Risk Analysis

**Risk 1**: Pipeline update may conflict with existing code
- **Mitigation**: Add new functions, don't modify existing ones

**Risk 2**: Import errors if module structure incorrect
- **Mitigation**: Ensure all `__init__.py` files exist, test imports

**Risk 3**: Build script may not run correctly
- **Mitigation**: Use placeholder logic, test script execution

---

## 10. Future Enhancements

- Real rule enforcement
- Real multi-chapter routing
- Real formatting enforcement
- Real validation logic
- Real build validation
- Dynamic rule assignment
- Rule versioning

